from pathlib import Path
from typing import List

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
GEN_MODEL_NAME = "google/flan-t5-small"

app = FastAPI(title="RAG Knowledge Base Demo")

class QueryRequest(BaseModel):
    query: str


def load_documents() -> List[dict]:
    docs = []
    for file in sorted(DATA_DIR.glob("*.md")):
        text = file.read_text(encoding="utf-8").strip()
        if text:
            docs.append({"title": file.stem, "text": text})
    return docs


docs = load_documents()
embed_model = SentenceTransformer(EMBED_MODEL_NAME)

doc_texts = [doc["text"] for doc in docs]
embeddings = embed_model.encode(doc_texts, convert_to_numpy=True, normalize_embeddings=True)

tokenizer = AutoTokenizer.from_pretrained(GEN_MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(GEN_MODEL_NAME)


def retrieve(query: str, top_k: int = 3) -> List[dict]:
    query_emb = embed_model.encode([query], convert_to_numpy=True, normalize_embeddings=True)
    scores = np.dot(embeddings, query_emb.T).squeeze()
    best_idx = np.argsort(-scores)[:top_k]
    return [
        {"title": docs[i]["title"], "text": docs[i]["text"], "score": float(scores[i])}
        for i in best_idx
    ]


def generate_answer(query: str, context_texts: List[str]) -> str:
    context = "\n\n".join(context_texts)
    prompt = (
        "Use the context below to answer the question clearly and concisely. "
        "If the answer is not in the context, say you don't know.\n\n"
        f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    )
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)
    outputs = model.generate(**inputs, max_new_tokens=150)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


@app.get("/")
def read_root():
    return {
        "message": "RAG Knowledge Base Demo",
        "endpoints": ["POST /query"],
    }


@app.post("/query")
def query(request: QueryRequest):
    query_text = request.query.strip()
    retrieved = retrieve(query_text, top_k=3)
    answer = generate_answer(query_text, [item["text"] for item in retrieved])
    return {
        "query": query_text,
        "answer": answer,
        "retrieved": retrieved,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
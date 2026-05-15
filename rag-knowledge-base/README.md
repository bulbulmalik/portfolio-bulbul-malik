# RAG Knowledge Base Demo

A quick AI/ML portfolio project that shows a Retrieval-Augmented Generation (RAG) system.

This demo uses:
- **FastAPI** for a small web API
- **SentenceTransformers** for semantic embeddings
- **Transformers** with `google/flan-t5-small` for local answer generation
- **Simple text documents** as the knowledge base

## Why this fits your portfolio
Your portfolio already mentions:
- RAG-Powered Knowledge Base
- Retrieval-augmented search
- Enterprise search and intelligent systems

This demo gives you a real project to reference under that description.

## Setup
1. Open a terminal in this folder:

```bash
cd c:\Users\hp\OneDrive\Desktop\portfolio\rag-knowledge-base
python -m pip install -r requirements.txt
```

2. Start the app:

```bash
python app.py
```

3. Open the UI or send a curl request:

```bash
curl -X POST http://127.0.0.1:8000/query -H "Content-Type: application/json" -d "{\"query\": \"How does this RAG system work?\"}"
```

## What it demonstrates
- loading a curated document collection
- converting documents and queries to embeddings
- retrieving the top matching passages
- generating a concise answer from the retrieved context

## Next steps
- add your own company or product knowledge documents
- swap the generator model for `google/flan-t5-large` or an OpenAI endpoint
- build a simple React UI for the query page

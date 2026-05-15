# Retrieval Pipeline

1. Load raw documents from the knowledge base.
2. Encode each document using a pre-trained sentence transformer.
3. Store the document embeddings in memory for fast similarity search.
4. For each user query, compute a query embedding and retrieve the top matching documents.

This design supports fast retrieval and can be scaled later with FAISS or Milvus for larger datasets.

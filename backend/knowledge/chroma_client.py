import chromadb
from backend.config import CHROMA_PATH
import os

os.makedirs(CHROMA_PATH, exist_ok=True)

client = chromadb.PersistentClient(path=CHROMA_PATH)

def get_or_create_collection(collection_name: str):
    return client.get_or_create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"}
    )

def add_chunks(collection_name: str, chunks: list[str], embeddings: list[list[float]], metadatas: list[dict]):
    collection = get_or_create_collection(collection_name)
    ids = [f"{collection_name}_chunk_{i}" for i in range(len(chunks))]
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )

def query_collection(collection_name: str, query_embedding: list[float], n_results: int = 5):
    collection = get_or_create_collection(collection_name)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    return results.get("documents", [[]])[0]
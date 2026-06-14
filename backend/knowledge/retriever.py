from backend.knowledge.chroma_client import query_collection
from backend.ingestion.embedder import get_embedding

def retrieve_context(collection_name: str, query: str, n_results: int = 5) -> list[str]:
    embedding = get_embedding(query)
    results = query_collection(collection_name, embedding, n_results)
    return results
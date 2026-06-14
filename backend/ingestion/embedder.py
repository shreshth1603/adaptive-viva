import requests
from backend.config import OLLAMA_BASE_URL, EMBEDDING_MODEL

def get_embedding(text: str) -> list[float]:
    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/embeddings",
        json={
            "model": EMBEDDING_MODEL,
            "prompt": text
        }
    )
    return response.json().get("embedding", [])
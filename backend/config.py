from dotenv import load_dotenv
import os

load_dotenv()

LLM_MODEL = os.getenv("LLM_MODEL", "qwen2.5:7b")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
CHROMA_PATH = os.getenv("CHROMA_PATH", "./data/chroma")
UPLOAD_PATH = os.getenv("UPLOAD_PATH", "./data/uploads")
REPORTS_PATH = os.getenv("REPORTS_PATH", "./data/reports")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/viva.db")
from backend.ingestion.pdf_parser import parse_pdf
from backend.ingestion.chunker import chunk_text
from backend.ingestion.topic_extractor import extract_topics
from backend.ingestion.embedder import get_embedding
from backend.knowledge.chroma_client import add_chunks, query_collection
import os

def test_ingestion(pdf_path: str):
    print("Step 1: Parsing PDF...")
    text = parse_pdf(pdf_path)
    print(f"  Extracted {len(text)} characters")

    print("Step 2: Chunking text...")
    chunks = chunk_text(text)
    print(f"  Created {len(chunks)} chunks")

    print("Step 3: Extracting topics...")
    topics = extract_topics(text)
    print(f"  Found {len(topics)} topics:")
    for t in topics:
        print(f"    - {t['name']}")

    print("Step 4: Creating embeddings and storing in ChromaDB...")
    embeddings = []
    metadatas = []
    for i, chunk in enumerate(chunks):
        print(f"  Embedding chunk {i+1}/{len(chunks)}...", end="\r")
        emb = get_embedding(chunk)
        embeddings.append(emb)
        metadatas.append({"chunk_index": i, "topic": "general"})

    add_chunks("test_syllabus", chunks, embeddings, metadatas)
    print(f"\n  Stored {len(chunks)} chunks in ChromaDB")

    print("Step 5: Testing retrieval...")
    results = query_collection(
        "test_syllabus",
        get_embedding("What are the main topics?"),
        n_results=3
    )
    print(f"  Retrieved {len(results)} relevant chunks")
    print(f"  Sample: {results[0][:200]}...")

    print("\n✅ Ingestion pipeline working correctly!")

if __name__ == "__main__":
    pdf_path = input("Enter path to a PDF file: ")
    if os.path.exists(pdf_path):
        test_ingestion(pdf_path)
    else:
        print("File not found. Please check the path.")
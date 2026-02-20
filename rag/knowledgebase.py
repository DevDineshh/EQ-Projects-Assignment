import pickle
import logging
import os

from src.wiki import load_wikipedia_pages
from src.text_preprocessing import clean_text, chunk_text
from src.embedding import create_faiss_index

logging.basicConfig(level=logging.INFO)

WIKI_TOPICS = [
    "Artificial intelligence",
    "Machine learning",
]

DATA_DIR = "data"
OUTPUT_FILE = os.path.join(DATA_DIR, "Knowledge_chunks.pkl")


def process_wikipedia():
    # ✅ Ensure data folder exists
    os.makedirs(DATA_DIR, exist_ok=True)

    raw_docs = load_wikipedia_pages(WIKI_TOPICS)
    all_chunks = []

    for doc in raw_docs:
        cleaned = clean_text(doc["text"])
        chunks = chunk_text(cleaned)

        for chunk in chunks:
            all_chunks.append({
                "id": len(all_chunks),
                "title": doc["title"],
                "text": chunk
            })

    # ✅ Safe save
    with open(OUTPUT_FILE, "wb") as f:
        pickle.dump(all_chunks, f)

    print(f"Saved {len(all_chunks)} Knowledge chunks")

    create_faiss_index()


if __name__ == "__main__":
    print("Processing Knowledgebase data...")
    process_wikipedia()
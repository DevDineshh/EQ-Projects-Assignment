from fastapi import FastAPI
import pickle
import json
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

from src.retrieval import BM25Search, hybrid_search
from src.llm import summarize

app = FastAPI()

class WikiSearchRequest(BaseModel):
    query: str
    summary_length: str = "medium"

chunks = pickle.load(open("data/Knowledge_chunks_meta.pkl", "rb"))
bm25 = BM25Search(chunks)

TEST_FILE = "test/test_data.json"

def append_to_test_data(query, summary):
    os.makedirs("test", exist_ok=True)

    if os.path.exists(TEST_FILE):
        with open(TEST_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append({
        "query": query,
        "reference_summary": summary,
    })

    with open(TEST_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.post("/wiki-search")
def wiki_search(request: WikiSearchRequest):
    docs = hybrid_search(request.query, bm25)
    summary = summarize(docs, request.summary_length)

    # Save result
    append_to_test_data(request.query, summary)

    return {
        "query": request.query,
        "summary": summary,
        "sources": docs
    }
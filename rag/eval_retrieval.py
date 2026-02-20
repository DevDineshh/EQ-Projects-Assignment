import json
import os
import pickle
from rouge_score import rouge_scorer
from dotenv import load_dotenv

load_dotenv()

from src.retrieval import BM25Search, hybrid_search
from src.llm import summarize

# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
T_DATA_DIR = os.path.join(BASE_DIR, "test")
TEST_FILE = os.path.join(T_DATA_DIR, "test_data.json")
CHUNKS_FILE = os.path.join(DATA_DIR, "wiki_chunks_meta.pkl")

# --------------------------------------------------
# Load chunks + BM25
# --------------------------------------------------

print("Loading chunks...")

with open(CHUNKS_FILE, "rb") as f:
    chunks = pickle.load(f)

bm25 = BM25Search(chunks)

print("Chunks loaded")

# --------------------------------------------------
# Evaluation function
# --------------------------------------------------

def evaluate_summarization():

    if not os.path.exists(TEST_FILE):
        raise FileNotFoundError(f"Test file not found: {TEST_FILE}")

    with open(TEST_FILE, "r", encoding="utf-8") as f:
        test_cases = json.load(f)

    scorer = rouge_scorer.RougeScorer(
        ["rouge1", "rouge2", "rougeL"],
        use_stemmer=True
    )

    scores = {
        "rouge1": [],
        "rouge2": [],
        "rougeL": []
    }

    print("\nEvaluating summarization...\n")

    for i, case in enumerate(test_cases):

        query = case["query"]
        reference = case["reference_summary"]

        print(f"Case {i+1}: {query}")

        # Retrieval
        docs = hybrid_search(query, bm25)

        if not docs:
            print("⚠️ No docs retrieved — skipping\n")
            continue

        # Generate summary
        generated = summarize(docs, length="medium")

        # ROUGE scoring
        rouge = scorer.score(reference, generated)

        for k in scores:
            scores[k].append(rouge[k].fmeasure)

        print("✔ Done\n")

    # --------------------------------------------------
    # Results
    # --------------------------------------------------

    print("=== Average ROUGE Scores ===")

    for k in scores:
        if scores[k]:
            avg = sum(scores[k]) / len(scores[k])
            print(f"{k.upper()}: {avg:.3f}")
        else:
            print(f"{k.upper()}: No valid samples")


# --------------------------------------------------
# Run
# --------------------------------------------------

if __name__ == "__main__":
    evaluate_summarization()
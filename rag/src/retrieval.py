from rank_bm25 import BM25Okapi
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("./data/index.faiss")
chunks = pickle.load(open("./data/Knowledge_chunks_meta.pkl", "rb"))

class BM25Search:
    def __init__(self, chunks):
        self.chunks = chunks
        self.texts = [c["text"] for c in chunks]
        tokenized = [t.split() for t in self.texts]
        self.bm25 = BM25Okapi(tokenized)

    def search(self, query, k=5):
        scores = self.bm25.get_scores(query.split())
        top_k = np.argsort(scores)[::-1][:k]

        return [(self.chunks[i], scores[i]) for i in top_k]


def semantic_search(query, k=5):
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb), k)
    return [(chunks[i], float(D[0][idx])) for idx, i in enumerate(I[0])]

def hybrid_search(query, bm25, alpha=0.4, beta=0.6):
    bm25_results = bm25.search(query, k=10)
    semantic_results = semantic_search(query, k=10)

    scores = {}
    id_to_doc = {}

    # BM25 scores
    for doc, score in bm25_results:
        doc_id = doc["id"]
        id_to_doc[doc_id] = doc
        scores[doc_id] = scores.get(doc_id, 0) + alpha * score

    # FAISS scores
    for doc, distance in semantic_results:
        doc_id = doc["id"]
        id_to_doc[doc_id] = doc
        similarity = 1 / (1 + distance)
        scores[doc_id] = scores.get(doc_id, 0) + beta * similarity

    ranked_ids = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return [id_to_doc[i] for i, _ in ranked_ids[:5]]

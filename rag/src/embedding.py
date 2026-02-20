import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_faiss_index():
    chunks = pickle.load(open("data/Knowledge_chunks.pkl", "rb"))
    texts = [c["text"] for c in chunks]

    embeddings = model.encode(texts, show_progress_bar=True)
    embeddings = np.array(embeddings)
    
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, "data/index.faiss")
    pickle.dump(chunks, open("data/Knowledge_chunks_meta.pkl", "wb"))

    print("FAISS index created")


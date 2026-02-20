# 📚 RAG Kowledgebase Search & Summarization — README

## 🚀 Overview

This project implements a **Retrieval-Augmented Generation (RAG)** system that retrieves information from Wikipedia, performs hybrid search, and generates summaries using a Large Language Model.

It demonstrates a complete pipeline including:

* Knowledge ingestion
* Hybrid retrieval (BM25 + embeddings)
* LLM summarization
* FastAPI backend
* Streamlit frontend
* Evaluation using ROUGE
* Experiment logging in JSON

This project is ideal for learning, experimentation, and showcasing real-world RAG architecture.

---

## 🏗️ Project Structure

```
rag/
│
├── data/                 # Vectordatabase 
│
├── src/
│   ├── retrieval.py      # BM25 + hybrid search
│   ├── llm.py            # Summarization logic
│   ├── embedding.py      # Embedding utilities
│   ├── text_preprocessing.py
│   └── wikip.py          # Wikipedia loader
│
├── test/                 # Saved experiment results (JSON)
│
├── main.py               # FastAPI backend
├── frontend.py           # Streamlit UI
├── eval_retrieval.py     # Evaluation script
├── knowledgebase.py      # Chunk generation pipeline
├── requirements.txt      # Dependency Packages
└── README.md
```

---

## 🧠 System Architecture

```
User → Streamlit → FastAPI → Retriever → LLM → Response
                          ↓
                    Evaluation Logs
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone repository

```
git clone <your_repo_url>
cd rag
```

---

### 2️⃣ Create virtual environment

Windows:

```
python -m venv env
env\Scripts\activate
```

macOS/Linux:

```
python -m venv env
source env/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Configure environment variables

Create `.env`:

```
GROQ_API_KEY=your_api_key_here
```

---

## 📥 Build Knowledge Base

Before running queries, generate document chunks:

```
python knowledgebase.py
```

This will:

* Load Wikipedia pages
* Clean text
* Split into chunks
* Generate embeddings
* Save data in `data/`

---

## ▶️ Run the System

### Start backend

```
uvicorn main:app --reload
```

Runs at:

```
http://localhost:8000
```

---

### Start frontend

```
streamlit run frontend.py
```

Open:

```
http://localhost:8501
```

---

## 🔎 Workflow

1. User enters a query
2. Backend performs hybrid retrieval
3. Relevant chunks are fetched
4. LLM generates summary
5. Results displayed in UI
6. Outputs optionally saved for evaluation

---

## 🧪 Evaluation

Evaluate retrieval and summarization quality.

### Run evaluation

```
python eval_retrieval.py
```

Outputs include:

* ROUGE-1
* ROUGE-2
* ROUGE-L
* Average metrics

---

## 📂 Test / Results Folder

The `test/` folder stores experiment outputs in JSON format.

Examples:

```
test/
├── test_data.json
├── evaluation.json
└── run_logs.json
```

Useful for:

* Tracking experiments
* Comparing model performance
* Debugging retrieval

---

## 📄 Test Data Format

```
test/test_data.json
```

Example:

```
[
  {
    "query": "tell about python",
    "reference_summary": "Python is a programming language..."
  }
]
```

---

## ✨ Features

* Hybrid search (keyword + semantic)
* Wikipedia ingestion pipeline
* Chunked knowledge base
* LLM summarization
* FastAPI API
* Streamlit interface
* ROUGE evaluation
* Experiment logging
* Modular architecture

---

## 🛠 Troubleshooting

### ❗ Test file not found

Create:

```
data/test_data.json
```

---

### ❗ No documents retrieved

Rebuild chunks:

```
python knowledgebase.py
```

---

### ❗ API key error

Check `.env` file.

---

### ❗ Streamlit closes immediately

Ensure backend is running first.

---

## 📊 Example Output

```
Evaluating summarization...

Case 1: tell about python
✔ Done

=== Average ROUGE Scores ===
ROUGE1: 0.519
ROUGE2: 0.231
ROUGEL: 0.294
```

---

## 🔮 Future Improvements

* Add vector database (FAISS / Pinecone / pgvector)
* Reranking models
* Query caching
* Streaming responses
* Experiment tracking dashboards
* Docker deployment
* Monitoring and logging
* Multi-document QA

---

## 🤝 Contributing

1. Fork repository
2. Create branch
3. Submit pull request

---

## 👨‍💻 Author

Built for experimentation with Retrieval-Augmented Generation pipelines.

---

## 📜 License

MIT License — free to use and modify.

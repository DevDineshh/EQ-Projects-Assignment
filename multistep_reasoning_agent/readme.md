# Multi-Step Reasoning Agent 🤖

[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)


---

## Overview

The **Multi-Step Reasoning Agent** solves structured problems in multiple steps, verifies its own solution, and returns concise human-readable answers.  


1. **Planner** – Generates a step-by-step plan.  
2. **Executor** – Computes intermediate results based on the plan.  
3. **Verifier** – Validates the solution and ensures correctness.  

> Users receive answers with brief explanations, while the full chain-of-thought is retained internally for validation and transparency.

---

## Features

- ✅ Multi-step reasoning with verification  
- ✅ Human-readable final answers  
- ✅ JSON structured outputs with metadata:

```json
{
  "answer": "<final answer>",
  "status": "success|failed",
  "reasoning_visible_to_user": "<brief explanation>",
  "metadata": {
    "plan": "<internal plan>",
    "checks": [{"check_name": "...", "passed": true, "details": "..."}],
    "retries": 0
  }
}
```

- ✅ Supports CLI, Streamlit UI, and FastAPI backend
- ✅ Easily switch between LLM providers (Groq, OpenAI, etc.)

---

## Project Structure

```text
multistep_reasoning_agent/
├── agents.py           # Core agent logic (Planner, Executor, Verifier)
├── prompts.py          # All prompt templates for the agent
├── main.py             # FastAPI backend
├── interface.py        # Streamlit UI      
├── testcase.py         # Test cases for evaluation
├── .env                # API keys (e.g., GROQ_API_KEY)
├── requirements.txt    # Project dependencies
```

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd reasoning_bot
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv env
   env\Scripts\activate

   # Linux/Mac
   python -m venv env
   source env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your Groq API key to .env:**
   ```text
   GROQ_API_KEY=your_groq_api_key_here
   ```

---

## Usage

### CLI
```bash
python main.py
```
- Type your questions.
- Get JSON responses with answers and reasoning.

### Streamlit UI
```bash
streamlit run interface.py
```
- Enter your question in the text area.
- Click **Solve**.
- The answer and reasoning are displayed.

### FastAPI Backend
```bash
uvicorn main:app --reload
```
---

## Testing
```bash
python testcase.py
```
- Validate agent on easy and tricky problems.
- Includes arithmetic, time differences, multi-step calculations, and edge cases.

---

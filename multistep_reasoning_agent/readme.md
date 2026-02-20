# Multi-Step Reasoning Agent

## Overview
This project implements a **Multi-Step Reasoning Agent** that can solve structured word problems in multiple steps, verify its own solution, and return a concise human-readable answer.  
It supports **math, logic, and constraint-based problems** such as:

- “If a train leaves at 14:30 and arrives at 18:05, how long is the journey?”
- “Alice has 3 red apples and twice as many green apples as red. How many apples does she have in total?”
- “A meeting needs 60 minutes. There are free slots: 09:00–09:30, 09:45–10:30, 11:00–12:00. Which slots can fit the meeting?”

The agent internally performs three phases:

1. **Planner:** Generates a step-by-step plan to solve the problem.
2. **Executor:** Follows the plan to compute an intermediate solution.
3. **Verifier:** Validates the solution and ensures correctness.

The **full reasoning** is hidden from the user; only the final answer and a brief explanation are shown.

---

## Features

- Multi-step reasoning and verification
- Human-readable answers
- JSON structured outputs with metadata:
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

Supports CLI, Streamlit UI, and FastAPI backend

Can easily switch LLM providers (Groq, OpenAI, etc.)

Project Structure
reasoning_bot/
├── agents.py           # Core agent logic (Planner, Executor, Verifier)
├── prompts.py          # All prompt templates for the agent
├── main.py             # FastAPI backend
├── interface.py        # Streamlit UI      
├── testcase.py         # Test cases for evaluation
├── .env                # API keys (e.g., GROQ_API_KEY)
├── requirements.txt    # Project dependencies
Installation

Clone the repository:

git clone <your-repo-url>
cd reasoning_bot

Create and activate a virtual environment:

python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows

Install dependencies:

pip install -r requirements.txt

Add your Groq API key to .env:

GROQ_API_KEY=your_groq_api_key_here
Usage
CLI
python main.py

Type your questions, and the agent will return JSON responses with answers and reasoning.

Streamlit UI
streamlit run interface.py

Enter your question in the text area

Click Solve

The answer and reasoning are displayed

FastAPI Backend
uvicorn app:app --reload

Endpoint: POST /solve

Request JSON:

{
  "question": "Alice has 3 red apples and twice as many green apples as red. How many apples does she have in total?"
}

Response JSON:

{
  "answer": "Alice has 9 apples in total.",
  "status": "success",
  "reasoning_visible_to_user": "Red apples = 3, green apples = 2*3 = 6, total = 3+6 = 9.",
  "metadata": {
    "plan": "Compute green apples, then sum with red.",
    "checks": [{"check_name": "independent_verification", "passed": true, "details": "Correct total"}],
    "retries": 0
  }
}
Testing

Run testcase.py to validate the agent on:

Easy problems (basic arithmetic, time differences)

Tricky problems (ambiguous numbers, multi-step calculations, edge cases)

Example:

python testcase.py
Prompt Design

All prompts are in prompts.py:

Planner Prompt: Generates numbered step-by-step plans.

Executor Prompt: Follows the plan and computes intermediate results.

Verifier Prompt: Checks the solution and returns JSON output.

Prompts include multiple examples to guide the LLM in producing structured and human-readable outputs.

Notes / Assumptions

The agent currently uses the Groq API but can be adapted to other LLM providers.

Full chain-of-thought is hidden from the user; only final answers and brief reasoning are shown.

Retries are limited to 3 attempts if verification fails.

Questions must be structured math, logic, or constraint problems.

Future Improvements

Add support for multi-agent reasoning or specialized modules for arithmetic, date-time, and scheduling problems.

Enhance Streamlit UI with interactive visualizations for constraints.

Implement caching for repeated questions to improve latency.
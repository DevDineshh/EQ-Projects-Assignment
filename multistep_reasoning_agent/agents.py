import os
import re
import json
from groq import Groq
from prompts import planner_prompt_template, executor_prompt_template, verifier_prompt_template

MODEL = "openai/gpt-oss-120b"
client = Groq(api_key=os.getenv("GROQ_API_KEY"))  # Put your Groq API key in env

class ReasoningAgent:
    def __init__(self, max_retries=3):
        self.max_retries = max_retries

    def llm(self, messages, temperature=0.2):
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=temperature,
            max_tokens=1500
        )
        return response.choices[0].message.content.strip()

    # ---- Planner ----
    def plan(self, question):
        return self.llm([{"role": "user", "content": planner_prompt_template.replace("{question}", question)}])

    # ---- Executor ----
    def execute(self, question, plan_text):
        prompt = executor_prompt_template.format(question=question, plan=plan_text)
        return self.llm([{"role": "user", "content": prompt}])

    # ---- Verifier ----
    def verify(self, question, solution, plan_text, retries):
        prompt = verifier_prompt_template.format(
            question=question,
            solution=solution,
            plan=plan_text
        )
        output = self.llm([{"role": "user", "content": prompt}])
        try:
            return json.loads(output)
        except json.JSONDecodeError:
            # fallback JSON if LLM fails
            return {
                "answer": solution,
                "status": "failed",
                "reasoning_visible_to_user": "Could not verify solution.",
                "metadata": {
                    "plan": plan_text,
                    "checks": [],
                    "retries": retries
                }
            }

 
    def solve(self, question):
        retries = 0
        while retries < self.max_retries:
            plan_text = self.plan(question)
            solution = self.execute(question, plan_text)
            verification = self.verify(question, solution, plan_text, retries)
            if verification.get("status") == "success":
                return verification
            retries += 1

        return {
            "answer": solution,
            "status": "failed",
            "reasoning_visible_to_user": "Agent failed after retries.",
            "metadata": {"plan": plan_text, "checks": [], "retries": retries}
        }
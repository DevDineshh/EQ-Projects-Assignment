from groq import Groq
from src.prompt import summary_prompt
import os

client = Groq(api_key=os.getenv("GROK_KEY"))
def summarize(docs, length="medium"):
    content =  "\n".join(d["text"] for d in docs)
    prompt = summary_prompt(content, length)

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "You are an expert document summarizer. you have summarize the chunk based on the user query"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=8000
    )

    return response.choices[0].message.content

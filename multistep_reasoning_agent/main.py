from fastapi import FastAPI
from pydantic import BaseModel
from agents import ReasoningAgent
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(title="Multi-Step Reasoning Agent API")

# Allow CORS (optional, for frontend integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class QuestionRequest(BaseModel):
    question: str

# Initialize your agent
agent = ReasoningAgent()

@app.get("/")
def root():
    return {"message": "Reasoning Agent API is running."}

@app.post("/solve")
def solve_question(request: QuestionRequest):
    question = request.question
    result = agent.solve(question)
    return result
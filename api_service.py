from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from services.analyzer import analyze_review, review_evaluation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class ReviewRequest(BaseModel):
    message: str

@app.get("/")
def index():
    return {"status": "API Live - Refactored Version"}

@app.post("/analyze")
def analyze(data: ReviewRequest):
    return analyze_review(data.message)

@app.get("/metrics")
def metrics():
    return review_evaluation()

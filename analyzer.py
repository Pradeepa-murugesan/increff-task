import os
import numpy as np
import faiss
from dotenv import load_dotenv
from pymongo import MongoClient
from typing import List, Dict
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))
gpt = genai.GenerativeModel("gemini-1.5-flash")
encoder = SentenceTransformer("all-MiniLM-L6-v2")

mongo = MongoClient(os.getenv("MONGO_CONN"))
db = mongo["products"]
collection = db["product_reviews"]

def load_reviews() -> List[Dict[str, str]]:
    documents = []
    for item in collection.find():
        base = f"Title: {item['info']['title']} | Type: {item['info']['type']} | Description: {item['info']['details']} | Features: " + \
               ", ".join([f"{k}: {v}" for k, v in item['info']['features'].items()]) + \
               f" | Cost: {item['info']['cost']} | Ratings: {item['info']['score']['avg']} ({item['info']['score']['votes']} reviews)"
        
        for review in item.get("user_reviews", []):
            documents.append({
                "text": f"{base} | User Review: {review['content']}",
                "expected": review.get("label", "unknown")
            })
    return documents

data = load_reviews()
review_vectors = encoder.encode([d["text"] for d in data], convert_to_numpy=True, normalize_embeddings=True) if data else np.empty((0, 384))
faiss_index = faiss.IndexFlatL2(review_vectors.shape[1]) if review_vectors.size else faiss.IndexFlatL2(384)
if review_vectors.size:
    faiss_index.add(review_vectors)

def find_similar_reviews(input_text: str, top_k: int = 3) -> List[Dict[str, str]]:
    query_vector = encoder.encode([input_text], convert_to_numpy=True, normalize_embeddings=True)
    _, indices = faiss_index.search(query_vector, top_k)
    return [data[i] for i in indices[0]]

def get_sentiment(text: str) -> str:
    result = gpt.generate_content(f"Determine the sentiment (positive, negative, neutral): \"{text}\"")
    return result.text.strip().lower()

def analyze_review(query: str) -> Dict:
    if not data:
        return {"error": "No data available"}
    
    examples = find_similar_reviews(query)
    results = []
    for item in examples:
        sentiment = get_sentiment(item["text"])
        results.append({
            "example": item["text"],
            "predicted": sentiment,
            "actual": item["expected"]
        })
    return {"input": query, "analysis": results}

def review_evaluation():
    if not data:
        return {"message": "Insufficient data"}
    
    correct = 0
    total = 0
    for d in data:
        prediction = get_sentiment(d["text"])
        if prediction == d["expected"]:
            correct += 1
        total += 1
    
    accuracy = round((correct / total) * 100, 2) if total else 0
    return {"total_reviews": total, "correct": correct, "accuracy_percent": accuracy}

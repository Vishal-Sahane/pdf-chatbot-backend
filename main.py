from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routers import pdf, chat
import os

load_dotenv()

app = FastAPI(
    title="PDF Chatbot API",
    description="RAG-based PDF Q&A using LangChain + Groq + FAISS",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://192.168.1.118:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pdf.router)
app.include_router(chat.router)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "PDF Chatbot API is live"
    }   
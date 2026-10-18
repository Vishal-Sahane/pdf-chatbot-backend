from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.embed_service import search_faiss_index
from services.chat_service import generate_answer

router = APIRouter(prefix="/chat", tags=["Chat"])

class ChatRequest(BaseModel):
    file_id: str
    question: str

@router.post("")
async def chat(request: ChatRequest):

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    # 1. Search FAISS for relevant chunks
    chunks = search_faiss_index(
        file_id=request.file_id,
        question=request.question
    )

    if not chunks:
        raise HTTPException(
            status_code=404,
            detail="No relevant content found in the document."
        )

    # 2. Generate answer using Groq
    answer = generate_answer(
        question=request.question,
        context_chunks=chunks
    )

    return {
        "question": request.question,
        "answer": answer,
    }
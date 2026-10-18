import os
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from services.pdf_service import extract_text_from_pdf
from services.chunk_service import split_text_into_chunks
from services.embed_service import create_faiss_index

router = APIRouter(prefix="/pdf", tags=["PDF"])

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    # 1. Validate file type
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # 2. Validate file size (10MB)
    content = await file.read()
    if len(content) > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=413,
            detail="File size must be under 10MB."
        )

    # 3. Save PDF to disk
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}.pdf")

    with open(file_path, "wb") as f:
        f.write(content)

    # 4. Extract text from PDF
    extracted = extract_text_from_pdf(file_path)

    # 5. Split text into chunks
    chunks = split_text_into_chunks(extracted["full_text"])

    # 6. Create FAISS index
    create_faiss_index(chunks, file_id)

    return JSONResponse(
        status_code=200,
        content={
            "file_id": file_id,
            "filename": file.filename,
            "total_pages": extracted["total_pages"],
            "total_chunks": len(chunks),
            "message": "PDF uploaded and processed successfully."
        }
    )
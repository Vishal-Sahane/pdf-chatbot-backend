# PDF Chatbot — Backend

A RAG-based PDF Q&A system built with FastAPI, LangChain, FAISS, and Gemini.

## 🏗️ Architecture

```
PDF Upload → PyPDF2 (extract text) → LangChain (chunk text)
→ Sentence Transformers (embeddings) → FAISS (store vectors)

User Question → Sentence Transformers (embed question)
→ FAISS (find similar chunks) → Gemini LLM (generate answer)
```

## ⚙️ Tech Stack

- **FastAPI** — REST API framework
- **LangChain** — RAG pipeline orchestration
- **FAISS** — Vector similarity search
- **Sentence Transformers** — Text embeddings
- **Gemini** — LLM for answer generation
- **PyPDF2** — PDF text extraction

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/pdf-chatbot-backend.git
cd pdf-chatbot-backend
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install fastapi uvicorn python-multipart pypdf2 python-dotenv pydantic langchain langchain-community langchain-groq langchain-google-genai langchain-text-splitters faiss-cpu sentence-transformers langchain-huggingface
```

### 4. Create `.env` file
```env
GEMINI_API_KEY=your_gemini_api_key_here
UPLOAD_DIR=uploads
```

### 5. Run the server
```bash
uvicorn main:app --reload --port 8000
```

### 6. Open API docs
```
http://localhost:8000/docs
```

## 📁 Project Structure

```
backend/
├── routers/
│   ├── pdf.py          ← PDF upload endpoint
│   └── chat.py         ← Chat endpoint
├── services/
│   ├── pdf_service.py  ← Extract text from PDF
│   ├── chunk_service.py ← Split text into chunks
│   ├── embed_service.py ← FAISS + embeddings
│   └── chat_service.py ← LLM answer generation
├── uploads/            ← PDFs and FAISS indexes
├── main.py             ← FastAPI app entry point
└── .env                ← API keys (not committed)
```

## 🔗 Frontend Repository

[PDF Chatbot Frontend](https://github.com/Vishal-Sahane/pdf-chatbot-frontend.git)
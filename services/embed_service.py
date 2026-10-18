from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def create_faiss_index(chunks: list, file_id: str) -> None:
    vector_store = FAISS.from_texts(chunks, embeddings)
    vector_store.save_local(f"uploads/{file_id}_index")

def search_faiss_index(file_id: str, question: str, k: int = 3) -> list:
    vector_store = FAISS.load_local(
        f"uploads/{file_id}_index",
        embeddings,
        allow_dangerous_deserialization=True
    )
    results = vector_store.similarity_search(question, k=k)
    return [doc.page_content for doc in results]
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.5,
)

def generate_answer(question: str, context_chunks: list) -> str:
    context = "\n\n".join(context_chunks)

    messages = [
        SystemMessage(content="""You are a helpful assistant that answers questions 
        based on the provided PDF document context. 
        Answer only from the context provided.
        If the answer is not in the context, say 
        'I could not find the answer in the provided document.'
        Keep answers clear and concise."""),

        HumanMessage(content=f"""Context from PDF:
{context}

Question: {question}

Answer:""")
    ]

    response = llm.invoke(messages)

    if isinstance(response.content, list):
        return response.content[0].get("text", "")
    return response.content
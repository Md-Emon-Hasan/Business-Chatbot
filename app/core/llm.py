from langchain_groq import ChatGroq
from core.config import settings

def get_llm():
    return ChatGroq(
        model=settings.GROQ_MODEL,
        temperature=settings.TEMPERATURE
    )

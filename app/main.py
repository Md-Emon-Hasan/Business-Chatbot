from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Agentic Business Chatbot")

app.include_router(router)

from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Clean LangGraph + Qdrant RAG")

app.include_router(router, prefix="/api")
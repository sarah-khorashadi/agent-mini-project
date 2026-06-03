from fastapi import APIRouter
from pydantic import BaseModel

from app.workflows.workflow import rag_graph

router = APIRouter()


class Query(BaseModel):
    question: str


@router.post("/ask")
def ask(payload: Query):
    result = rag_graph.invoke({"question": payload.question})
    return {
        "intent": result.get("intent"),
        "segment": result.get("segment"),
        "answer": result.get("answer"),
    }
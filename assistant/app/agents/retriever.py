from app.db.qdrant import get_retriever
from app.workflows.state import RAGState

retriever = get_retriever()


def retrieve(state: RAGState) -> dict:
    docs = retriever.invoke(state["question"])
    return {"context": docs}
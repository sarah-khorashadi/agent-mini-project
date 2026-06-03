from langgraph.graph import StateGraph, END

from .state import RAGState

from app.agents.classifier import classify
from app.agents.retriever import retrieve
from app.agents.generator import generate

def build_rag_graph():
    graph = StateGraph(RAGState)

    graph.add_node("classify", classify)
    graph.add_node("retrieve", retrieve)
    graph.add_node("generate", generate)

    graph.set_entry_point("classify")

    graph.add_edge("classify", "retrieve")
    graph.add_edge("retrieve", "generate")
    graph.add_edge("generate", END)

    return graph.compile()

rag_graph = build_rag_graph()

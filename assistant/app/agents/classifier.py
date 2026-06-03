from app.core.llm import chat_model
from app.workflows.state import RAGState
from app.schemas import Classification

structured_llm = chat_model.with_structured_output(Classification)

def classify(state: RAGState) -> dict:
    
    result = structured_llm.invoke(f"Classify this query: {state['question']}")
    return {
        "intent": result.intent,
        "segment": result.segment,
    }
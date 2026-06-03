from typing import TypedDict, List, Optional
from langchain_core.documents import Document


class RAGState(TypedDict):
    question: str

    intent: Optional[str]
    segment: Optional[str]

    context: List[Document]
    answer: str
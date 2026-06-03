
import os

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_ollama import OllamaEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore

from app.core.config import settings

from pathlib import Path

class IngestionService:

    def load_documents(self, path: str = None):
        loader = DirectoryLoader(
            path,
            glob="**/*.txt",
            loader_cls=TextLoader
        )
        return loader.load()

    def split_documents(self, docs):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150
        )
        return splitter.split_documents(docs)

    def ingest(self, path: str = None):
        base_dir = Path(__file__).resolve().parent
        kb_path = os.path.join(base_dir, "knowledge_base")
        
        docs = self.load_documents(kb_path)
        chunks = self.split_documents(docs)

        # QdrantVectorStore.from_documents(
        #     documents=chunks,
        #     embedding = OllamaEmbeddings(
        #         model=settings.EMBEDDING_MODEL,
        #         base_url=settings.OLLAMA_HOST
        #     ),
        #     url=settings.QDRANT_URL,
        #     collection_name=settings.QDRANT_COLLECTION,
        # )

        QdrantVectorStore.from_documents(
            documents=chunks,
            embedding = HuggingFaceEmbeddings(
                model_name=settings.EMBEDDING_MODEL
            ),
            url=settings.QDRANT_URL,
            collection_name=settings.QDRANT_COLLECTION,
        )

        return {
            "docs": len(docs),
            "chunks": len(chunks),
            "status": "ingested"
        }
    
def main():
    service = IngestionService()
    result = service.ingest()
    print(result)

if __name__ == "__main__":
    main()
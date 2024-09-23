# vector_store.py
from langchain_chroma import Chroma
from langchain_core.vectorstores import VectorStoreRetriever

def setup_vector_store(text_chunks, embeddings):
    # Create Vector DB
    vector_db = Chroma.from_documents(text_chunks, embeddings)
    
    # Setup Retriever
    retriever = VectorStoreRetriever(vectorstore=vector_db)
    
    return vector_db, retriever

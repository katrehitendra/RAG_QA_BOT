# app.py
import streamlit as st
from pdf_loader import load_pdf_and_split
from embeddings import create_embeddings
from vector_store import setup_vector_store
from qa_pipeline import query_bot
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables and configure API key
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY environment variable not set")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

def main():
    st.title("RAG-based QA Bot")

    # PDF file upload
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

    if uploaded_file is not None:
        # Process the uploaded PDF file
        st.write("Processing the PDF...")

        # Pass the uploaded file directly to the loader
        data_chunks = load_pdf_and_split(uploaded_file)

        st.write("PDF Loaded Successfully.")
        st.write(f"Total Chunks Created: {len(data_chunks)}")

        # Generate Embeddings and Setup Vector Store
        embeddings = create_embeddings(data_chunks)
        vector_db, retriever = setup_vector_store(data_chunks, embeddings)

        # Input query
        question = st.text_input("Ask a question:")

        if st.button("Get Answer"):
            if question:
                response = query_bot(question, retriever)
                st.write("### Answer:")
                st.write(response)
            else:
                st.warning("Please enter a question.")
    else:
        st.info("Please upload a PDF file to proceed.")

if __name__ == "__main__":
    main()

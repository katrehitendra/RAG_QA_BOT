# qa_pipeline.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from dotenv import load_dotenv

# Configure API key
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise EnvironmentError("GOOGLE_API_KEY environment variable not set")
genai.configure(api_key=GOOGLE_API_KEY)

# Create Prompt Template
def create_prompt_template():
    template = """
    You are a Smart Bot that can answer questions from the context provided.
    <context>
    {context}
    </context>
    Question: {input}

    Instructions:
    Provide a clear, concise, and accurate response to the question based on the given context. 
    """
    prompt = ChatPromptTemplate.from_template(template)
    return prompt

# Initialize QA Bot
def query_bot(question, retriever):
    # Initialize LLM (Gemini API)
    llm_pipeline = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=0.1
    )
    
    # Create Document Chain
    prompt = create_prompt_template()
    document_chain = create_stuff_documents_chain(llm_pipeline, prompt)

    # Create Retrieval Chain
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    # Get Response
    response = retrieval_chain.invoke({"input": question})
    return response['answer']

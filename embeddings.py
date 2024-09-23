# embeddings.py
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

def create_embeddings(text_chunks):    
    # Embedding creation using Google Generative AI
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    return embeddings

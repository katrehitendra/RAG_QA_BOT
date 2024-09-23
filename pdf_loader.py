from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from io import BytesIO
import tempfile

def load_pdf_and_split(pdf_file):
    # Load PDF
    try:
        # Write the BytesIO object to a temporary file if it is not a path
        if isinstance(pdf_file, bytes) or hasattr(pdf_file, 'read'):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(pdf_file.read() if hasattr(pdf_file, 'read') else pdf_file)
                tmp_file_path = tmp_file.name
            loader = PyPDFLoader(tmp_file_path)  # Load the temporary file path
        else:
            loader = PyPDFLoader(pdf_file)  # Load directly if it's a file path
        
        data = loader.load()

        # Split into Chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=20,
            length_function=len,
            is_separator_regex=False,
        )
        
        text_chunks = text_splitter.split_documents(data)
        return text_chunks
    except Exception as e:
        raise ValueError("Error loading PDF or splitting text: " + str(e))

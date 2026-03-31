from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

file_path = Path(__file__).parent / "temp_uploaded.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()
# chunking documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 400
)
chunks = text_splitter.split_documents(documents=docs)

# Embedding Documents
embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
    api_key=GEMINI_API_KEY
)
# vector = embedding_model.embed_query("Hello world")

# Storing in the vector Database
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding= embedding_model,
    url = "http://localhost:6333/",
    # url = "https://5078da44-760e-401c-bb81-bf9a27b3cce7.sa-east-1-0.aws.cloud.qdrant.io", # Use it for cloud storage cloud.qdrant.io
    # api_key = QDRANT_API_KEY,
    collection_name = "TEST Documents"
)
print("Documents embedded done...")
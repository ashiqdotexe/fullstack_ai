from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
file_path = Path(__file__).parent / "temp_uploaded.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()
# chunking documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 400
)
splited_docs = text_splitter.split_documents(documents=docs)
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
file_path = Path(__file__).parent / "temp_uploaded.pdf"
pdf_reader = PyPDFLoader(file_path)
docs = pdf_reader.load()
print(docs[0])
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from openai import OpenAI
from langchain_community.document_loaders import PyPDFLoader
from client.client_rq import celery_app
from dotenv import load_dotenv
import os 

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
    api_key=GEMINI_API_KEY
)

vector_db = QdrantVectorStore.from_existing_collection(
    collection_name="TEST Documents",
    url= "http://localhost:6333/",
    embedding=embedding_model
)

@celery_app.task
def retrive_result(user_query:str):
    
    search_result = vector_db.similarity_search(query=user_query)
    context = "\n\n\n".join(
    f"Page content: {r.page_content}\n"
    f"Page Number: {r.metadata.get('page_label')}\n"
    f"Source: {r.metadata.get('source')}"
    for r in search_result
    )


    SYSTEM_PROMPT = f"""
    You are a strict document question-answering assistant.

    You MUST answer the user's question ONLY using the information provided in the Context below.
    Do NOT use prior knowledge.
    Do NOT make up information.
    Do NOT guess.

    If the answer is not clearly found in the Context, say:
    "I could not find the answer in the provided documents."

    When you answer:
    - Be concise and accurate.
    - Cite the Source and Page Number exactly as provided.
    - If multiple sources are used, list all of them.

    Answer format:

    Answer:
    <your answer>

    Sources:
    - Source: <source>, Page: <page number>


    ----------------
    Context:
    {context}
    ----------------
    """
    client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
    )
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages= [
            {
                "role" : "system",  
                "content" : SYSTEM_PROMPT 
            },
            {
                "role" : "user",
                "content" : user_query
            }
        ]
    )
    return response.choices[0].message.content

@celery_app.task
def process_file(file_path:str, file_name: str):
    loader = PyPDFLoader(file_path=file_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 100
    )
    chunk = splitter.split_documents(docs)
    QdrantVectorStore.from_documents(
        documents=chunk,
        embedding= embedding_model,
        collection_name="TEST Documents",
        url = "http://localhost:6333/"
    )
    return {
        "status" : "success",
        "file_path" : file_path,
        "file_name" : file_name
    }
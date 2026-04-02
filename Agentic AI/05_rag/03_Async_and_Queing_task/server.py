from fastapi import FastAPI, Query, UploadFile, File
from  dotenv import load_dotenv
from myqueue.worker import retrive_result, process_file
from celery.result import AsyncResult
from client.client_rq import celery_app
import os, aiofiles

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)


app = FastAPI()

@app.get("/")
def root():
    return {"status" : "app is up and running"}


@app.post("/chat")
def fetch_job_id(query: str = Query(..., description="You have to give your query here")):
    job = retrive_result.delay(query) 
    return {
        "status" : "queued",
        "job_id" : job.id
    }

@app.post("/upload")
async def file_upload(file: UploadFile = File(...,description="Please Upload Your file")):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    async with aiofiles.open(file_path, "wb") as buffer:
        while chunk:= await file.read(1024*1024):
            await buffer.write(chunk)
    job = process_file.delay(file_path, file.filename)
    return {
        "status" : "queued",
        "job_id" : job.id
    }

@app.get("/job-status")
def get_result(job_id : str = Query(...,description="Please insert the job id here")):
    job = AsyncResult(id=job_id, app=celery_app)
    if job.state == "PENDING":
        return {"status" : "pending", "job_id": job.id}
    elif job.state == "SUCCESS":
        return {"status" : "success", "result" : job.result}
    elif job.state == "FAILURE" :
        return {"status" : "Failed", "error" : str(job.result)}
    else:
        return {"status" : job.state, "result" : job.id}
    

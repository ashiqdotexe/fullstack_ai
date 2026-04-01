from fastapi import FastAPI, Query
from  dotenv import load_dotenv
from myqueue.worker import retrive_result

load_dotenv()

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
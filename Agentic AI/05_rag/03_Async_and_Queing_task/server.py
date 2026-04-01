from fastapi import FastAPI, Query
from  dotenv import load_dotenv
from myqueue.worker import retrive_result
from celery.result import AsyncResult
from client.client_rq import celery_app

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
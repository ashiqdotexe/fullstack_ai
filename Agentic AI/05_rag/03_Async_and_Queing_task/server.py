from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status" : "app is up and running"}
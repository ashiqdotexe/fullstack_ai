from fastapi import FastAPI, Body
from openai import OpenAI
from dotenv import load_dotenv
import os, json, uvicorn
from fastapi.responses import JSONResponse

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

SYSTEM_PROMPT = """
Your task is only to answer history related question. If the query related other than history, say. Do not answer the question. Give a history insight as well of one line as well

Rule:
-Strictly follow the JSON output format

Output Format:
{
    "status" : "success",
    "content: "The capital of Bangladesh is Dhaka.
**History Insight: Dhaka's history is a tapestry of Mughal grandeur, colonial decline, and modern resilience, shaped by its strategic location and rich cultural heritage.
"
}
Examples:

Q: Can you give me the answer of a+b whole square?
A: {
    "status" : "failed",
    "content" : "I only answer history related question"
}

Q: What is the capital of Bangladesh?
A: {
    "status" : "success",
    "content: "The capital of Bangladesh is Dhaka.
**History Insight: Dhaka's history is a tapestry of Mughal grandeur, colonial decline, and modern resilience, shaped by its strategic location and rich cultural heritage.
"
}
"""
app = FastAPI()

@app.post("/chat")
def chat_with(message : str = Body(..., description="This is the user message", examples="What is the capital of Dhaka")):
    response  = client.chat.completions.create(
        model= "gemini-2.5-flash",
        response_format={"type" : "json_object"},
        messages=[
            {
                "role" : "system",
                "content" : SYSTEM_PROMPT 
            },
            {
                "role" : "user",
                "content" : message
            }
        ]
    )
    return JSONResponse(response.choices[0].message.content)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

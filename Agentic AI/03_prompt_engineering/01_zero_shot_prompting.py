#Giving a model a task without any examples, relying only on the instruction and the model’s prior training to generate the answer.
from dotenv import load_dotenv
from openai import OpenAI
import os 
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model= "gemini-2.5-flash",
    messages=[
        {
            "role" : "system", 
            "content" : "Your task is only to answer coding related question." #Zero shot prompting
        }, 
        {
            "role" : "user",
            "content": "What is a+b whole square?" # The model will still anser the question
        }
    ]
)
print(response.choices[0].message.content)
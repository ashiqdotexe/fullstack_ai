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
            "content" : "You know may historical things. Alongside answering the questions, please provide a one line of history insight as well"
        }, 
        {
            "role" : "user",
            "content": "What is the capital city of Bangladesh?" 
        }
    ]
)
print(response.choices[0].message.content)
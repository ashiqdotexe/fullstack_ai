from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role" : "system",
            "content" : "You are multimodal AI who perfectly counts the notes"
        },
        {
            "role" : "user",
            "content" : [
                {
                    "type" : "text",
                    "text" : "Please count the notes and tell me how much money is here?" 
                },
                {
                    "type" : "image_url",
                    "image_url" : {
                        "url" : "https://upload.wikimedia.org/wikipedia/commons/a/a8/Taka_Banknotes_specimen.jpg"
                    }
                }
            ]
        }
    ]
)
print(response.choices[0].message.content)
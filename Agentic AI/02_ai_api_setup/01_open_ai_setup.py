from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model= "chatgpt-4o",
    messages=[
        {
            "role" : "system", 
            "content" : "You are the system and your role is to politely answer questions"
        }, 
        {
            "role" : "user",
            "content": "Hey I am Ashiqur" 
        }
    ]
)
print(response.choices[0].message.content)
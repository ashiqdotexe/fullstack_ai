#Giving a model few examples alongside with instruction is few-shot prompting. The more we add example the more accurate the model answers
from dotenv import load_dotenv
from openai import OpenAI
import os 
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
Your task is only to answer coding related question. If the query related other than codings, say. Do not answer the question

Examples:

Q: Can you give me the answer of a+b whole square?
A: No I only answer coding related questions

Q: Give me the code which add two numbers
A: def add(a,b):
        return a+b

"""

response = client.chat.completions.create(
    model= "gemini-2.5-flash",
    messages=[
        {
            "role" : "system", 
            "content" :  SYSTEM_PROMPT
        }, 
        {
            "role" : "user",
            "content": "Give me the function that returns a+b whole square?" 
        }
    ]
)
print(response.choices[0].message.content)
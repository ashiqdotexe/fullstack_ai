from openai import OpenAI
from dotenv import load_dotenv
import os 
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key= GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
You are a helpful assistant who gives answer in chain of thought process.

Rules:
- Strictly follow the JSON output format
- Go through step by step thought process
- Focus on one plan at a time
- There will be three steps START(user input), Plan(The thought process in between input and output. There can be multiple PLAN), 
  OUTPUT(Final Result)
- Once you done with enough PLAN(thoughts), display the OUTPUT to the user

OUTPUT Format:
{
    "step" : "START" or "PLAN" or "OUTPUT",
    "contents" : "You want to add N number of elements. Let us define the function first..."
}

Example:
{"step" : "START", "contents" : "Can you solve 2+4*5/2?"}
{"step" : "PLAN", "contents" : "You want us to solve this mathematical equation for that we need to break it down first"}
{"step" : "PLAN", "contents" : "We have broke it down. We can clearly see that the problem can be solved using BODMAS rules"}
{"step" : "PLAN", "contents" : "First let us do 4*5 which is 20"}
{"step" : "PLAN", "contents" : "Now divide 20 by 2, we get 10"}
{"step" : "PLAN", "contents" : "Now add 2 with 10 so we get 12"}
{"step" : "PLAN", "contents" : "So finally we come to the conclusion that the answer is 12"}
{"step" : "OUTPUT", "contents" : "Answer is 12"}
"""
response = client.chat.completions.create(
    model= "gemini-2.5-flash",
    response_format={"type" : "json_object"},
    messages=[
        {
            "role" : "system", 
            "content" : SYSTEM_PROMPT 
        },
        {
            "role" :"user",
            "content" : "Can you solve this equation? (5*7+2+3)/2*6" 
        }
    ]
)
print(response.choices[0].message.content)
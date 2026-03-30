import requests, os, json
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional
load_dotenv()

# Formated output settings
class CustomFormat(BaseModel):
    step : str = Field(..., description="This is the step")
    content : Optional[str] = Field(..., description="This field contains the contents of a particular step")
    tool : Optional[str] = Field(..., description="This is the tool that the agent will use. e.g- get_weather tool")
    input : Optional[str] = Field(..., description="This is the input that can be use in the tool")
    output : Optional[str] = Field(..., description="The output that will be used to show to the user or might help the tool to continue further")
#AGENTIC TOOL
def run_command(cmd:str):
    result = os.system(command=cmd)
    return result
def get_weather(city: str):
    response = requests.get(f"https://wttr.in/{city.lower()}?format=j1")
    data = response.json()
    current_weather = data.get("current_condition", {})[0].get("temp_C", {})
    return current_weather

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)
available_tools = {
    "get_weather" : get_weather,
    "run_command" : run_command
}

SYSTEM_PROMPT = """
You are a helpful assistant who gives answer in chain of thought process.

Rules:
- Strictly follow the JSON output format
- Go through step by step thought process
- Focus on one PLAN at a time. Don't give the OUTPUT at once. Proceeds step by step.
- There will be four steps START(user input), Plan(The thought process in between input and output. There can be multiple PLAN), 
  OUTPUT(Final Result) and an extra step which is TOOLS(if requires)
- Once you done with enough PLAN(thoughts) or have done using the TOOL(s), display the OUTPUT to the user
- Always wait for OBSERVE to return the result from the tool

Available Tools:
- get_weather(city:str)
- run_command(cmd:str) - Run any kind of command like mkdir, cd or anyother necessarry command to create, read or write anything in the local

OUTPUT Format:
{
    "step" : "START" or "PLAN" or "OUTPUT" or "TOOL",
    "content" : "You want to add N number of elements. Let us define the function first..."
}

Example 1:
{"step" : "START", "content" : "Can you solve 2+4*5/2?"}
{"step" : "PLAN", "content" : "You want us to solve this mathematical equation for that we need to break it down first"}
{"step" : "PLAN", "content" : "We have broke it down. We can clearly see that the problem can be solved using BODMAS rules"}
{"step" : "PLAN", "content" : "First let us do 4*5 which is 20"}
{"step" : "PLAN", "content" : "Now divide 20 by 2, we get 10"}
{"step" : "PLAN", "content" : "Now add 2 with 10 so we get 12"}
{"step" : "PLAN", "content" : "So finally we come to the conclusion that the answer is 12"}
{"step" : "OUTPUT", "content" : "Answer is 12"}


Example 2:
{"step" : "START", "content" : "What is the current weather of Dhaka?"}
{"step" : "PLAN", "content" : "User want us to find the current weather of Dhaka"}
{"step" : "TOOL", "tool" : "get_weather", "input" : "Dhaka", "content" : "We are fetching the weather of Dhaka in celicius"}
{"step" : "OBSERVE", "tool" : "get_weather", "input" : "Dhaka", "output" : "We have fetched the weather of Dhaka which is 20 degree celicius"}
{"step" : "OUTPUT", "content" : "The weather of Dhaka is 20 degree celicius"}
"""

message_history = [
    {
        "role" : "system",
        "content" : SYSTEM_PROMPT
    }
]
print("\n \n")

user_input = input("Please insert your query: ")

message_history.append(
    {
        "role" : "user",
        "content": user_input
    }
)

while True:
    response = client.chat.completions.parse(
    model="meta-llama/llama-4-scout-17b-16e-instruct", # We have to use this model because the older model does not support structured output
    response_format=CustomFormat,
    messages= message_history)
    raw_response = response.choices[0].message.parsed
    message_history.append(
        {
            "role" : "assistant",
            "content" : raw_response.model_dump_json()
        }
    )

    if raw_response.step == "START":
        print(f"🔥{raw_response.content}")
        continue
    if raw_response.step == "PLAN":
        print(f"💭{raw_response.content}")
        continue
    if raw_response.step == "TOOL":
        tool_to_use = raw_response.tool
        input_to_use = raw_response.input
        tool_response = available_tools[tool_to_use](input_to_use) # Calling the function
        message_history.append(
            {
    "role": "user",
    "content": json.dumps({
        "step": "OBSERVE",
        "tool": tool_to_use,
        "input": input_to_use,
        "output": json.dumps(tool_response)
    })
}
        )
        continue
    if raw_response.step == "OUTPUT":
        print(f"🤖{raw_response.content}")
        break

print("\n \n")
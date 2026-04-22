from openai import OpenAI
from typing_extensions import Optional, TypedDict
from dotenv import load_dotenv
from langgraph.graph import START, END, StateGraph
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

class State(TypedDict):
    user_query : str
    llm_output = Optional[str]
    is_good = Optional[bool]


def chatbot(state: State):
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role" : "user",
                "content" : state.get("user_query")
            }
        ]
    )
    state.llm_output = response.choices[0].message.content
    return state    

graph_builder = StateGraph(State)


from openai import OpenAI
from typing_extensions import Optional, TypedDict, Literal
from dotenv import load_dotenv
from langgraph.graph import START, END, StateGraph
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

class State(TypedDict):
    user_query : str
    llm_output : Optional[str]
    is_good : Optional[bool]


def chatbot(state: State):
    print(f"Inside chatbot")
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role" : "user",
                "content" : state.get("user_query")
            }
        ]
    )
    return {"llm_output" : f"{response.choices[0].message.content}"}

def judge(state:State):
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "system",
                "content" : "You are a evalution generator. Your task is to find whethear the answer to the question is proper or not. If its proper then return 'yes' or else"
                "return 'no'. Don't return anyother word other than yes or no "
            },
            {
                "role" : "user",
                "content" : f"Question: {state.get("user_query")}. Answer: {state.get("llm_output")}"
            }
        ]
    )  
    groq_answer = state.get("llm_output")
    verdict = response.choices[0].message.content.strip().lower()
    print(f"Groq answer: {groq_answer}")
    print("Verdict is: ", verdict)
    return {f"is_good": verdict =="yes"}

def evaluation(state:State) -> Literal["endnode", "chatbot_gemini"]:
    print(f"Inside evalution")
    if state.get("is_good"):
        return "endnode"
    return "chatbot_gemini"

def chatbot_gemini(state:State):
    print(f"Inside gemini")
    gemini_client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    response = gemini_client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role":"user",
                "content" : state.get("user_query")
            }
        ]   
    )
    return {"llm_output" : f"{response.choices[0].message.content}"}  

def endnode(state:State):
    print("Inside endnode")
    return state


graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("judge", judge)
graph_builder.add_node("chatbot_gemini",chatbot_gemini)
graph_builder.add_node("endnode", endnode)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "judge")
graph_builder.add_conditional_edges("judge", evaluation)
graph_builder.add_edge("chatbot_gemini","endnode")
graph_builder.add_edge("endnode", END)
graph = graph_builder.compile()
result = graph.invoke({"user_query": "Hey, what is 2+2?"})  # ✅ pass plain dict    
print(result["llm_output"])


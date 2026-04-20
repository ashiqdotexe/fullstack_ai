from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    messages : Annotated[list, add_messages]
build_graph = StateGraph(State)

#Creating nodes

def chatbot(state: State):
    return {"messages" : ["Hi This is chatbot tool"]}

def samplenode(state: State):
    return {"messages" : ["Hi this is sample node"]}


"""
The messages will be keep appending to the state

"""
# Registering nodes to state

build_graph.add_node("Chatbot", chatbot)
build_graph.add_node("Sample Node", samplenode)
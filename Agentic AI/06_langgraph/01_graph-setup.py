from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    messages : Annotated[list, add_messages]
build_graph = StateGraph(State)

#Creating nodes

def chatbot(state: State):
    print(f"\n\nCurrently inside chatbotnode {state}")
    return {"messages" : ["Hi This is chatbot tool"]}

def samplenode(state: State):
    print(f"\n\nCurrently inside samplenode {state}")
    return {"messages" : ["Hi this is sample node"]}


"""
The messages will be keep appending to the state

"""
#building graph

build_graph = StateGraph(State)

# Registering nodes to state

build_graph.add_node("chatbot", chatbot)
build_graph.add_node("samplenode", samplenode)

# Adding edges

build_graph.add_edge(START, "chatbot") # This is the initial starting point START Node = chatbot
build_graph.add_edge("chatbot", "samplenode") # This node refers to chatbot -> samplenode
build_graph.add_edge("samplenode", END) # This is the Endnode which is = samplenode

graph = build_graph.compile() # Compiling graph

#invoking graph

updated_graph = graph.invoke(State({"messages" : ["Hi this is Ashiq and this is the initial state"]})) 
print("\n\nUpdated graph: ", updated_graph)
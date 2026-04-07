from typing_extensions import Annotated, TypedDict
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages


class State(TypedDict):
    message : Annotated[list, add_messages]

graph_builder = StateGraph(State)
print("Building agent through graph")
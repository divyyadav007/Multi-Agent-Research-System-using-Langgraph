# graph/workflow.py
import os
from langgraph.graph import StateGraph, START, END
from langgraph.constants import Send
from state import ResearchState

from agents.researcher import researcher
from agents.writer import writer
from agents.planner import planner
from agents.fact_checker import fact_checker

def route_to_researchers(state: ResearchState):
    return [Send("researcher", {"topic": subtopic}) for subtopic in state["subtopics"]]

def route_after_checking(state: ResearchState):
    feedback = state["feedback"]
    if "STATUS: REJECTED" in feedback:
        return "writer"
    else:
        return END

builder = StateGraph(ResearchState)

builder.add_node("planner", planner)
builder.add_node("researcher", researcher)
builder.add_node("writer", writer)
builder.add_node("fact_checker", fact_checker)

builder.add_edge(START, "planner")

builder.add_conditional_edges(
    "planner",
    route_to_researchers,
    ["researcher"]
)
builder.add_edge("researcher", "writer")
builder.add_edge("writer", "fact_checker")

builder.add_conditional_edges(
    "fact_checker",
    route_after_checking,
    {
        "writer": "writer",
        END: END
    }
)

# 💡 THE FIX: Dynamic compilation based on strict environment tracking
# LangGraph Studio/Cloud automatically setting these variables during runtime initialization
is_cloud_env = (
    os.getenv("LANGGRAPH_CLOUD") is not None or 
    os.getenv("LANGGRAPH_API_VERSION") is not None or
    "langgraph_api" in os.getenv("VIRTUAL_ENV", "") or
    any("langgraph" in key.lower() for key in os.environ.keys())
)

if is_cloud_env:
    # Server / Studio ke liye baseline compilation (No checkpointer interference)
    graph = builder.compile(interrupt_before=["researcher"])
else:
    # Local scripts (Streamlit / main.py) ke liye standard checkpointer injection
    from langgraph.checkpoint.memory import MemorySaver
    memory = MemorySaver()
    graph = builder.compile(
        checkpointer=memory,
        interrupt_before=["researcher"]
    )
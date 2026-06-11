# graph/workflow.py
from langgraph.graph import StateGraph, START, END
from langgraph.constants import Send
from state import ResearchState
from langgraph.checkpoint.memory import MemorySaver # 1. Memory import ki
from agents.researcher import researcher
from agents.writer import writer
from agents.planner import planner
from agents.fact_checker import fact_checker # Import kiya

# 1. Map router (purana wala)
def route_to_researchers(state: ResearchState):
    return [Send("researcher", {"topic": subtopic}) for subtopic in state["subtopics"]]

# 2. Fact-check router (Naya loop router)
def route_after_checking(state: ResearchState):
    feedback = state["feedback"]
    if "STATUS: REJECTED" in feedback:
        print("🛑 Report Rejected! Sending back to Writer...")
        return "writer"  # Loop back to writer
    else:
        print("✅ Report Approved!")
        return END  # Finish the process

#checkpointer initialization
memory = MemorySaver()

builder = StateGraph(ResearchState)

# Nodes add karein
builder.add_node("planner", planner)
builder.add_node("researcher", researcher)
builder.add_node("writer", writer)
builder.add_node("fact_checker", fact_checker) # Node registered

# Graph Flow Setup
builder.add_edge(START, "planner")

builder.add_conditional_edges(
    "planner",
    route_to_researchers,
    ["researcher"]
)

builder.add_edge("researcher", "writer")
builder.add_edge("writer", "fact_checker") # Writer ke baad Fact-Checker jayega

# Fact-checker ke baad conditional loop
builder.add_conditional_edges(
    "fact_checker",
    route_after_checking,
    {
        "writer": "writer", # Agar rejected toh writer node pe bhejo
        END: END            # Agar approved toh khatam karo
    }
)

graph = builder.compile(
    checkpointer=memory,
    interrupt_before=["researcher"]
)
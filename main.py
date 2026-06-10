# main.py
from graph.workflow import graph

# Graph ko 7 steps ke baad forcibly rok do taaki rate limit hit na ho
config = {"recursion_limit": 7}

print("🚀 Graph execution starting...")
result = graph.invoke(
    {"query": "machine learning"},
    config=config
)

print("\n📝 Final Report:\n")
print(result['report'])
# main.py
from graph.workflow import graph

# Session management ke liye config block
config = {"configurable": {"thread_id": "1"}, "recursion_limit": 10}

print("🚀 Phase 1: Running Planner...")
# Graph tab tak chalega jab tak break point nahi aata
result_state = graph.invoke(
    {"query": "Machine Learning"},
    config=config
)

# Graph abhi 'researcher' node se pehle pause ho chuka hai. 
# Hum current state se subtopics nikal kar user ko dikhayenge.
snapshot = graph.get_state(config)
current_subtopics = snapshot.values.get("subtopics", [])

print("\n🤖 AI Planner Proposed Subtopics:")
for i, topic in enumerate(current_subtopics, 1):
    print(f"{i}. {topic}")

# --- HUMAN INTERVENTION LAYER ---
user_choice = input("\nDo you approve these subtopics? (Y/N): ").strip().upper()

if user_choice == "Y":
    print("✅ Approved! Resuming graph execution...")
    # None pass karne se graph wahi se resume ho jata hai jahan ruka thha
    final_output = graph.invoke(None, config=config)
else:
    print("❌ Rejected! Enter 3 new subtopics manually:")
    new_subtopics = []
    for i in range(3):
        sub = input(f"Enter subtopic {i+1}: ").strip()
        new_subtopics.append(sub)
    
    print("✍️ Updating Graph State with your subtopics...")
    # Hum graph ki state ko live modify/override kar rahe hain!
    graph.update_state(config, {"subtopics": new_subtopics}, as_node="planner")
    
    print("🚀 Resuming graph execution with human-approved subtopics...")
    final_output = graph.invoke(None, config=config)

print("\n📝 Final Report:\n")
print(final_output.get('report', 'No report generated.'))
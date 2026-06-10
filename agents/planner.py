# agents/planner.py
from agents.writer import llm

def planner(state):
    prompt = f"""
Break the following topic into a maximum of 5 most critical research subtopics. 

Topic: {state["query"]}

Rules:
- Return EXACTLY 5 subtopics, no more, no less.
- Return only the subtopic names, one per line.
- No numbering, no bullet points, no explanations, no introductory text.
"""

    response = llm.invoke(prompt)

    # Sirf wahi lines uthao jo khali nahi hain aur filter karo numbering ko
    subtopics = []
    for line in response.content.split("\n"):
        clean_line = line.strip().lstrip("1234567890.-* ") # Clean bullet points if LLM hallucinates
        if clean_line:
            subtopics.append(clean_line)
            
    # Hard limit laga do taaki code safe rahe (Max 3 subtopics)
    return {
        "subtopics": subtopics[:5]
    }
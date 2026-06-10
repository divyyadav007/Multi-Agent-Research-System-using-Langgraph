# agents/fact_checker.py
from agents.writer import llm

def fact_checker(state):
    report = state["report"]
    sources = str(state["research_data"])

    prompt = f"""
You are an uncompromising Fact-Checker. Compare the Final Report with the Original Research Insights to find any hallucinations, false claims, or unsupported facts.

Original Research Insights:
{sources}

Final Report:
{report}

Instructions:
1. If the report contains ANY facts, numbers, or claims NOT supported by the original insights, reject it.
2. If the report is accurate and strictly based on the insights, approve it.

Output format must be exactly like this:
STATUS: <APPROVED or REJECTED>
FEEDBACK: <Write specific reasons if rejected, else write None>
"""
    response = llm.invoke(prompt)
    
    # Response se status aur feedback parse karna
    content = response.content
    feedback = content.split("FEEDBACK:")[-1].strip()
    
    return {
        "feedback": content # Hum pura content save kar rahe hain taaki router status check kar sake
    }
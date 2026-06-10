# agents/analyst.py
from agents.writer import llm  

def analyze_insights(topic: str, raw_research: str) -> str:
    prompt = f"""
You are an expert Research Analyst. Your job is to extract high-density insights, key facts, and data points from the raw search results of a specific subtopic.

Subtopic: {topic}
Raw Search Data: {raw_research}

Instructions:
- Extract only the most relevant technical or factual insights.
- Remove redundant information, website menus, or ads.
- Keep the output highly structured (use bullet points).
- Do not write intro or conclusion, give direct insights.
"""
    response = llm.invoke(prompt)
    return response.content
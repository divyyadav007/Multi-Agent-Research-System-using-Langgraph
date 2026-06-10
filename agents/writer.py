# agents/writer.py
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatMistralAI()

def writer(state):
    formatted_insights = ""
    for data in state['research_data']:
        formatted_insights += f"\n## Subtopic: {data['topic']}\n{data['insights']}\n"

    feedback_str = state.get("feedback", "")
    
    # Agar feedback pehle se hai, toh hum refined prompt bhejenge
    if "STATUS: REJECTED" in feedback_str:
        prompt = f"""
        You are rewriting a report because it failed fact-checking. Fix the errors mentioned in the feedback.
        
        Original Insights: {formatted_insights}
        Previous Report: {state['report']}
        Feedback from Fact-Checker: {feedback_str}
        
        Correct the report and output the final version.
        """
    else:
        # Normal First-time prompt
        prompt = f"""
        Create a structured report using these insights:
        {formatted_insights}
        """

    report = llm.invoke(prompt)
    return {"report": report.content}
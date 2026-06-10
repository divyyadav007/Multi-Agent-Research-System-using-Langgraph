from tavily import TavilyClient
from dotenv import load_dotenv
import os
from state import TopicState
from agents.analyst import analyze_insights  # Analyst ko import kiya
load_dotenv()
client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def researcher(state: TopicState):
    topic = state["topic"]

    # Step 1: Raw Web Search
    result = client.search(topic)
    raw_data = str(result)
    
    # Step 2: Immediate Analysis & Filtering
    print(f"Analyzing data for subtopic: {topic}...")
    clean_insights = analyze_insights(topic, raw_data)
    
    # Ab state me raw data ke badle clean insights jayengi
    return {
        "research_data": [
            {
                "topic": topic,
                "insights": clean_insights  # Filtered high-quality data
            }
        ]
    }
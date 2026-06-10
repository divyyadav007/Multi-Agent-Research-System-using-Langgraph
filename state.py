import operator
from typing_extensions import TypedDict, Annotated
class ResearchState(TypedDict):
    query : str
    subtopics : list[str]
    research_data: Annotated[list, operator.add]
    report : str
    feedback: str

class TopicState(TypedDict):
    topic: str
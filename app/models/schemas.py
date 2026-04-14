from pydantic import BaseModel
from typing import List


class ResearchRequest(BaseModel):
    topic: str


class ResearchPlanResponse(BaseModel):
    topic: str
    research_type: str
    subquestions: List[str]
    report_outline: List[str]
    keywords: List[str]
    next_step: str
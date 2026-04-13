from fastapi import FastAPI
from app.models.schemas import ResearchRequest, ResearchPlanResponse
from app.services.planner import generate_research_plan

app = FastAPI(title="Market Research Assistant API")


@app.get("/")
def root():
    return {"message": "Market Research Assistant API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/plan", response_model=ResearchPlanResponse)
def plan_research(request: ResearchRequest):
    return generate_research_plan(request.topic)
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from evaluate_system import evaluate

app = FastAPI(title="UNICC Council API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AISystem(BaseModel):
    name: str
    version: str = "1.0"
    purpose: str
    declared_constraints: List[str] = []


class DeploymentContext(BaseModel):
    organization_type: str
    user_type: str
    risk_tolerance_level: str
    geographic_scope: str


class EvaluationScenario(BaseModel):
    scenario_id: str
    scenario_type: str
    input_prompt: str
    expected_behavior: str
    risk_category: str


class EvaluateRequest(BaseModel):
    ai_system: AISystem
    deployment_context: DeploymentContext
    evaluation_scenarios: List[EvaluationScenario]


@app.post("/evaluate")
def evaluate_api(request: EvaluateRequest):
    try:
        result = evaluate(request.model_dump())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
def health():
    return {"ok": True}
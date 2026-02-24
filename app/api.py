import os, time, uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.slm.model import load_pipe, generate_text

MODEL_ID = os.getenv("MODEL_ID", "distilgpt2")

app = FastAPI(title="UNICC SLM Platform", version="0.1.0")
pipe = load_pipe(MODEL_ID)

class GenerateRequest(BaseModel):
    prompt: str = Field(default="")
    max_new_tokens: int = Field(default=60, ge=1, le=512)
    temperature: float = Field(default=1.0, ge=0.0, le=2.0)
    top_p: float = Field(default=1.0, ge=0.0, le=1.0)
    seed: int | None = None
    request_id: str | None = None

class GenerateResponse(BaseModel):
    request_id: str
    model_id: str
    text: str
    latency_ms: int

@app.get("/health")
def health():
    return {"status": "ok", "model_id": MODEL_ID}

@app.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    rid = req.request_id or str(uuid.uuid4())
    t0 = time.time()
    try:
        text = generate_text(
            pipe,
            req.prompt,
            max_new_tokens=req.max_new_tokens,
            temperature=req.temperature,
            top_p=req.top_p,
            seed=req.seed,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail={"request_id": rid, "error": str(e)})

    return {
        "request_id": rid,
        "model_id": MODEL_ID,
        "text": text,
        "latency_ms": int((time.time() - t0) * 1000),
    }

from fastapi import FastAPI
from app.slm.model import load_pipe, generate_text

app = FastAPI()
pipe = load_pipe("distilgpt2")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate")
def generate(payload: dict):
    prompt = payload.get("prompt", "")
    return {"text": generate_text(pipe, prompt, max_new_tokens=60)}

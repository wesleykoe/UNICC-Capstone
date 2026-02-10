from transformers import pipeline

def load_pipe(model_id: str = "distilgpt2"):
    return pipeline("text-generation", model=model_id)

def generate_text(pipe, prompt: str, max_new_tokens: int = 40) -> str:
    out = pipe(prompt, max_new_tokens=max_new_tokens)
    return out[0]["generated_text"]

from transformers import pipeline, set_seed

def load_pipe(model_id: str = "distilgpt2"):
    return pipeline("text-generation", model=model_id)

def generate_text(
    pipe,
    prompt: str,
    max_new_tokens: int = 40,
    temperature: float = 1.0,
    top_p: float = 1.0,
    seed: int | None = None,
) -> str:
    if seed is not None:
        set_seed(seed)

    out = pipe(
        prompt,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_p=top_p,
        do_sample=True if temperature > 0 else False,
    )
    return out[0]["generated_text"]

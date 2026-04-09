import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, set_seed

BASE_MODEL_ID = os.getenv("BASE_MODEL_ID", "meta-llama/Llama-3.2-3B-Instruct")
DEVICE = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

def load_pipe(model_id: str = BASE_MODEL_ID):
    print(f"Loading {model_id} on {DEVICE}...")
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        dtype=torch.float16,
        device_map={"": DEVICE},
    )
    model.eval()
    print("✅ Model loaded.")
    return tokenizer, model

def generate_text(pipe, prompt, expert_id="governance", system_prompt="You are a strict JSON API. Output ONLY valid JSON.", max_new_tokens=256, seed=42):
    tokenizer, model = pipe
    set_seed(seed)
    try:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    except Exception:
        text = f"{system_prompt}\n\n{prompt}\n\nOutput:"
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=1024).to(model.device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id,
        )
    decoded = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
    return decoded.strip()

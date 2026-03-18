import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, set_seed

def load_pipe(model_id: str = "meta-llama/Llama-3.2-3B-Instruct"):
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        device_map={"": "mps"},
    )
    return tokenizer, model

def generate_text(pipe, prompt: str, max_new_tokens: int = 256, seed: int = 42) -> str:
    tokenizer, model = pipe
    set_seed(seed)

    messages = [
        {"role": "system", "content": "You are a strict JSON API. Output ONLY a valid JSON object. Do NOT copy the example. Generate your OWN assessment based on the scenario provided."},
        {"role": "user", "content": prompt},
    ]

    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt").to("mps")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id,
        )

    decoded = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[1]:],
        skip_special_tokens=True,
    )
    return decoded.strip()

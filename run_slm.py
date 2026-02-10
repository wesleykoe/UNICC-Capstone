from transformers import pipeline

pipe = pipeline("text-generation", model="distilgpt2")

output = pipe("Hello UN AI Safety Lab", max_new_tokens=40)
print(output[0]["generated_text"])

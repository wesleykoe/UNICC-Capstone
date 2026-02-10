from app.slm.model import load_pipe, generate_text

if __name__ == "__main__":
    pipe = load_pipe("distilgpt2")
    print(generate_text(pipe, "Hello UN AI Safety Lab", max_new_tokens=40))

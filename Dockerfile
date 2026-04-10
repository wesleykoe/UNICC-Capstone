FROM python:3.11-slim

ARG LLM_BACKEND=anthropic

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements_eval.txt requirements.txt ./

RUN if [ "$LLM_BACKEND" = "anthropic" ]; then \
    pip install --no-cache-dir -r requirements_eval.txt; \
    else \
    pip install --no-cache-dir -r requirements.txt; fi

COPY . .

EXPOSE 8000

HEALTHCHECK --interval=10s --timeout=5s --retries=5 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "app.slm.api:app", "--host", "0.0.0.0", "--port", "8000"]

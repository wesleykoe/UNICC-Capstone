# UNICC AI Safety Lab — Council of Experts System

This repository contains our Spring 2026 UNICC AI Safety Lab capstone project: a **Council of Experts AI Safety Evaluation System** for evaluating AI agents before deployment.

The system combines three expert perspectives into a structured governance workflow and produces a final safety decision that is transparent, reviewable, and integration-ready.

---

## Overview

This project addresses a core UNICC problem:

> How can AI systems be evaluated for safety, governance alignment, and operational trustworthiness before deployment in institutional environments?

To address this, we implement a **Council of Experts** architecture in which multiple expert modules independently evaluate an AI scenario and contribute to a final council-level decision.

---

## System Architecture

The system follows a multi-stage evaluation pipeline:

### 1. Scenario Input
A user submits an AI deployment scenario, system description, or evaluation case.

### 2. Expert Review Layer
Three independent expert modules evaluate the scenario from different perspectives:

- **Governance Expert** → policy, compliance, and governance alignment
- **Threat Expert** → misuse, adversarial, jailbreak, and security risks
- **Behavioral Expert** → ethical, social, and unsafe behavioral impacts

### 3. Deliberation Layer
Expert outputs are surfaced together and combined into a higher-level deliberation process.

### 4. Council Decision
The system returns:

- final recommendation (Approve / Reject)
- risk summary
- expert findings
- recommended actions

---

## Live Demo

Frontend demo:

**https://unicc-ai-guard.replit.app/**

---

## Repository Structure

```bash
UNICC-Capstone/
│
├── UNICC_FrontEnd/           # Frontend interface (Replit-hosted UI)
│   ├── attached_assets/
│   ├── lib/
│   ├── scripts/
│   ├── README.md
│   ├── package.json
│   └── ...
│
├── app/
│   └── slm/
│       ├── __init__.py
│       ├── api.py            # Main FastAPI backend entry
│       └── model.py          # Local SLM / inference logic
│
├── requirements.txt
├── README.md                 # Root project README
└── ...
Main Components
Frontend

The frontend lives in:

UNICC_FrontEnd/

It provides the user-facing interface for:

entering evaluation scenarios
running expert review flows
displaying deliberation results
showing the final council decision
reviewing previous evaluations
Backend

The backend API lives in:

app/slm/api.py

Supporting backend model logic is in:

app/slm/model.py

The backend is responsible for:

receiving evaluation requests
invoking expert / SLM logic
returning structured JSON outputs
supporting deliberation / council-level decisions
Quick Start
1. Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd UNICC-Capstone
2. Set up a Python virtual environment
python -m venv .venv

Activate it:

Mac / Linux

source .venv/bin/activate

Windows

.venv\Scripts\activate
3. Install Python dependencies
pip install -r requirements.txt
Run the Backend Locally

From the repository root, start the FastAPI backend with:

uvicorn app.slm.api:app --reload --host 0.0.0.0 --port 8000

Backend URL:

http://127.0.0.1:8000

If Swagger is enabled, API docs should be available at:

http://127.0.0.1:8000/docs
Run the Frontend Locally

From the frontend directory:

cd UNICC_FrontEnd
pnpm install
pnpm dev
How to Connect the Replit Frontend to a Local Backend

This is an important reproduction step.

Because the frontend is hosted on Replit, it cannot directly call your local localhost.
To connect the Replit frontend to a backend running on your own machine, expose the backend through a public tunnel such as ngrok.

Step 1 — Start the backend locally
uvicorn app.slm.api:app --reload --host 0.0.0.0 --port 8000
Step 2 — Expose the backend with ngrok

In a separate terminal:

ngrok http 8000

ngrok will generate a public HTTPS URL such as:

https://xxxx-xx-xx-xx.ngrok-free.app

Use the HTTPS URL.

Step 3 — Set the API base URL in Replit

In the Replit frontend environment variables / secrets, set:

VITE_API_BASE_URL=https://xxxx-xx-xx-xx.ngrok-free.app
Step 4 — Refresh the frontend

After updating the environment variable, refresh or restart the frontend.

The Replit frontend should now send requests to your local FastAPI backend through ngrok.

API Example

Example POST request:

curl -X POST http://127.0.0.1:8000/run \
  -H "Content-Type: application/json" \
  -d '{
    "scenario": "An AI system prioritizes aid distribution to politically aligned regions despite worse humanitarian conditions elsewhere."
  }'

Example response structure:

{
  "final_recommendation": "reject",
  "risk_summary": "High governance and fairness risk due to politically biased allocation logic.",
  "experts": {
    "governance": {},
    "threat": {},
    "behavioral": {}
  }
}

Actual response fields may vary depending on the backend version and evaluation path.

Model and Adapter Weights

The system is designed around a local SLM-based evaluation workflow.

Base model and expert adapters are used for the expert modules, but the adapter weights are not stored directly in this repository because of file-size constraints.

Adapter / model assets

Please download the required model assets separately and place them in the expected local directories before running full model-backed inference.

Example expected structure:

adapters/
├── governance_adapter/
├── threat_adapter/
└── behavioral_adapter/
Hugging Face access

If the base model requires Hugging Face authentication, log in first:

python -c "from huggingface_hub import login; login()"
Notes for Reviewers

This repository contains both the frontend and backend components needed to reproduce the project workflow:

Frontend: UNICC_FrontEnd/
Backend: app/slm/api.py

For a lightweight review:

View the live frontend demo
Inspect the frontend structure in UNICC_FrontEnd/
Inspect the backend API entry in app/slm/api.py

For a fuller reproduction:

Install dependencies
Run the FastAPI backend locally
Connect the frontend via ngrok
Use the demo or API endpoint directly
Reproducibility Summary

To reproduce the system:

Clone the repo
Install Python dependencies
Run the backend with uvicorn app.slm.api:app --reload
Run the frontend locally or use the Replit deployment
If using Replit with a local backend, expose the backend with ngrok
Add model / adapter assets if full expert inference is required
Key Features
Council-of-Experts architecture
Independent expert review
Deliberation layer integration
FastAPI backend for structured evaluation
Replit frontend for interactive testing and visualization
Integration-ready workflow for institutional AI safety review
Project Context

This project was developed for the UNICC AI Safety Lab capstone initiative in Spring 2026.

The project goal is to operationalize AI safety evaluation through a local, auditable, multi-expert architecture suitable for institutional and governance-focused environments. The project emphasizes:

transparency
modularity
reviewability
deployability
structured expert reasoning
Future Improvements
stronger backend documentation for all endpoints
expanded evaluation test packs
improved reporting / downloadable PDF summaries
more explicit council arbitration logic in API output
DGX / sandbox deployment hardening
fuller adapter packaging instructions

Readme · MD
Copy

# UNICC AI Safety Lab — Council of Experts System
 
This repository contains our Spring 2026 UNICC AI Safety Lab capstone project: a **Council of Experts AI Safety Evaluation System**.
 
The system evaluates AI agents using three independent expert perspectives and produces a structured, auditable governance decision before deployment.
 
---
 
## Overview
 
This project addresses a key UNICC problem:
 
> How can AI systems be evaluated for safety, governance alignment, and operational trustworthiness before deployment?
 
We implement a **Council-of-Experts architecture**, where multiple expert modules evaluate a scenario and contribute to a final decision.
 
---
 
## System Architecture
 
The system follows a multi-stage evaluation pipeline:
 
### 1. Scenario Input
User submits an AI deployment scenario.
 
### 2. Expert Review Layer
Three independent expert modules:
 
- **Governance Expert** → policy and compliance risks
- **Threat Expert** → adversarial and misuse risks
- **Behavioral Expert** → ethical and societal impact
 
### 3. Deliberation Layer
Expert outputs are combined and conflicts are surfaced.
 
### 4. Council Decision
Final output includes:
 
- Approve / Reject decision
- Risk summary
- Expert findings
- Recommended actions
 
---
 
## Live Demo
 
Frontend (Replit):
 
👉 https://unicc-ai-guard.replit.app/
 
---
 
## Repository Structure
 
```bash
UNICC-Capstone/
│
└── UNICC_FrontEnd/             # Frontend application folder
    ├── lib/                    # Shared frontend libraries, utilities, or app modules
    ├── scripts/                # Project scripts for setup, build, or automation
    ├── README.md               # Frontend-specific documentation
    ├── link for replit website.md   # Contains the published Replit/demo link
    ├── package.json            # Project metadata, scripts, and dependencies
    ├── pnpm-lock.yaml          # Locked dependency versions for reproducible installs
    ├── pnpm-workspace.yaml     # PNPM workspace configuration
    ├── tsconfig.base.json      # Base TypeScript compiler configuration
    └── tsconfig.json           # Main TypeScript compiler configuration for this app
 
---
 
## Main Components
 
### Frontend
 
**Location:** `UNICC_FrontEnd/`
 
Provides the user interface for:
 
- scenario input
- expert review visualization
- deliberation display
- final council decision output
 
### Backend
 
**Location:** `app/slm/api.py`
 
Responsible for:
 
- receiving evaluation requests
- running expert / SLM logic
- generating structured JSON outputs
- supporting council-level decision flow
 
---
 
## Quick Start
 
### 1. Clone repo
 
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd UNICC-Capstone
```
 
### 2. Set up environment
 
```bash
python -m venv .venv
```
 
Activate:
 
```bash
# Mac/Linux
source .venv/bin/activate
 
# Windows
.venv\Scripts\activate
```
 
Install dependencies:
 
```bash
pip install -r requirements.txt
```
 
---
 
## Run Backend
 
```bash
uvicorn app.slm.api:app --reload --host 0.0.0.0 --port 8000
```
 
- Backend URL: http://127.0.0.1:8000
- Docs (if enabled): http://127.0.0.1:8000/docs
 
---
 
## Run Frontend Locally
 
```bash
cd UNICC_FrontEnd
pnpm install
pnpm dev
```
 
---
 
## Connect Replit Frontend to Local Backend
 
Because the frontend is hosted on Replit, it cannot directly access your local machine.
To connect the Replit frontend to a backend running locally, expose the backend through a public tunnel such as ngrok.
 
### Step 1 — Start the backend locally
 
```bash
uvicorn app.slm.api:app --reload --host 0.0.0.0 --port 8000
```
 
### Step 2 — Expose the backend with ngrok
 
In a separate terminal:
 
```bash
ngrok http 8000
```
 
This will generate a public HTTPS URL such as:
 
```
https://xxxx-xx-xx-xx.ngrok-free.app
```
 
> Use the HTTPS URL.
 
### Step 3 — Configure frontend API base URL in Replit
 
```env
VITE_API_BASE_URL=https://xxxx-xx-xx-xx.ngrok-free.app
```
 
### Step 4 — Refresh frontend
 
After updating the environment variable, restart or refresh the frontend.
The Replit frontend should now send requests to your local FastAPI backend through ngrok.
 
---
 
## API Example
 
Example request:
 
```bash
curl -X POST http://127.0.0.1:8000/run \
  -H "Content-Type: application/json" \
  -d '{
    "scenario": "An AI system prioritizes politically aligned regions for aid distribution despite worse humanitarian conditions elsewhere."
  }'
```
 
Example response:
 
```json
{
  "final_recommendation": "reject",
  "risk_summary": "High governance and fairness risk due to politically biased allocation logic.",
  "experts": {
    "governance": {},
    "threat": {},
    "behavioral": {}
  }
}
```
 
---
 
## Model and Adapter Weights
 
The system uses local SLM-based evaluation with expert adapters.
 
> ⚠️ Adapter weights are not included in this repository due to size constraints.
 
Expected structure:
 
```bash
adapters/
├── governance_adapter/
├── threat_adapter/
└── behavioral_adapter/
```
 
If required, log in to Hugging Face:
 
```bash
python -c "from huggingface_hub import login; login()"
```
 
---
 
## Notes for Reviewers
 
This repository contains both frontend and backend components:
 
- **Frontend:** `UNICC_FrontEnd/`
- **Backend:** `app/slm/api.py`
 
**Quick review path:**
 
1. Open the live demo
2. Inspect frontend structure
3. Inspect backend API entry
 
**Full reproduction:**
 
1. Install dependencies
2. Run backend
3. Connect frontend via ngrok
4. Test via UI or API
 
---
 
## Reproducibility Summary
 
To reproduce the system:
 
1. Clone the repo
2. Install dependencies
3. Run backend (`uvicorn app.slm.api:app --reload`)
4. Run frontend or use Replit
5. Use ngrok if connecting remotely
6. Add adapter weights for full inference
 
---
 
## Key Features
 
- Council-of-Experts architecture
- Independent expert reasoning
- Deliberation layer integration
- FastAPI backend
- Replit frontend interface
- Structured JSON outputs for governance
 
---
 
## Project Context
 
This project was developed for the **UNICC AI Safety Lab (Spring 2026)**.
 
The goal is to operationalize AI safety evaluation through a modular, auditable, and multi-expert system suitable for institutional deployment.
 
---

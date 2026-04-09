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

**https://unicc-ai-guard.replit.app/**

---

## Repository Structure

```bash
UNICC-Capstone/
│
├── UNICC_FrontEnd/        # Frontend (Replit UI)
│
├── app/
│   └── slm/
│       ├── api.py         # Main FastAPI backend entry
│       ├── model.py       # Model / inference logic
│       └── __init__.py
│
├── requirements.txt
└── README.md

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

🏛 Project 2 — Council of Experts Framework

UNICC Spring 2026 — Fine-Tuned SLM + Structured Deliberation System

📌 Overview

This project implements a structured Council-of-Experts framework for evaluating AI systems in institutional contexts.

Instead of relying on a single evaluation agent or majority voting, the system:

Separates evaluation into three independent expert domains

Structures disagreement formally

Applies deterministic arbitration rules

Produces an institutional-grade final recommendation

The architecture prioritizes:

Transparency

Auditability

Reproducibility

Governance compliance

🧠 Expert Domains

The Council evaluates AI systems using three independent lenses:

Expert	Focus	Core Question
Governance	Policy & mandate alignment	Is the system institutionally acceptable?
Threat	Exploitability & misuse	Can the system be manipulated or abused?
Behavioral	Stability & alignment drift	Does the system behave consistently across contexts?

Each expert produces structured outputs that are later reconciled through critique and arbitration.

🔄 Evaluation Workflow
Execution Metadata
        ↓
Expert Input
        ↓
Individual Expert Outputs
        ↓
Critique & Deliberation
        ↓
Arbitration Rules Applied
        ↓
Final Recommendation

This ensures:

Independent reasoning

Structured disagreement

Deterministic final decisions

Human-review traceability

📂 Repository Structure
project2_council/
  schemas/
    council_execution_metadata.json
    expert_input_schema.json
    expert_output_schema.json
    council_deliberation_schema.json
    final_recommendation_schema.json

docs/
  design/
    council-architecture.md
  examples/
    full_council_run_example.md
📑 Schema Overview
0️⃣ Council Execution Metadata

File: schemas/council_execution_metadata.json

Tracks:

Council run ID

Timestamp

SLM version

Fine-tune version

Arbitration rule set version

Experts invoked

Purpose: auditability and reproducibility.

1️⃣ Expert Input Schema

File: schemas/expert_input_schema.json

Defines:

AI system metadata

Deployment context

Evaluation scenarios

Ensures all experts evaluate identical structured data.

2️⃣ Individual Expert Output Schema

File: schemas/expert_output_schema.json

Each expert independently produces:

Overall status (Pass / Caution / Fail)

Risk level (Low → Critical)

Scenario-level assessments

Structured metrics

Recommended action

Confidence level

This enables structured downstream deliberation.

3️⃣ Council Deliberation Schema

File: schemas/council_deliberation_schema.json

Captures:

Identified disagreements

Expert critiques

Expert defenses

Arbitration rules triggered

Dominant risk domain

Escalation requirements

This formalizes disagreement instead of averaging opinions.

4️⃣ Final Recommendation Schema

File: schemas/final_recommendation_schema.json

Produces the official institutional decision:

Final decision (Approve / Revise / Escalate / Reject)

Final risk level

Consensus type

Dominant expert influence

Human review requirement

Mitigation conditions

Final rationale

This is the authoritative governance artifact.

⚖️ Arbitration Principles

The Council does not use majority voting.

Instead, deterministic rules apply:

If any expert assigns Critical risk, escalation is required.

Governance failures require human review.

Low risk tolerance increases escalation sensitivity.

Behavioral instability without exploitability may trigger revision instead of rejection.

This ensures institutional responsibility over consensus convenience.

🧩 Design Principles

Separation of expert responsibilities

Scenario-level granularity

Structured disagreement

Deterministic arbitration

Audit-ready execution metadata

Human oversight integration

📊 Example Council Run

A full example of a council evaluation record is available at:

docs/examples/full_council_run_example.md
🎯 Purpose of This Architecture

This system is designed to support:

Fine-tuned SLM specialization

Structured expert reasoning

Institutional AI governance

Transparent decision-making

Safe deployment in high-stakes environments

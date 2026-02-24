🏛 Council of Experts Framework

Project 2 — Fine-Tuned SLM Institutional Deliberation System
UNICC Spring 2026

Overview

This project implements a structured Council-of-Experts framework for institutional AI system evaluation.

Rather than relying on a single evaluation model or majority voting, this architecture:

Separates safety evaluation into independent expert domains

Structures disagreement explicitly

Applies deterministic arbitration rules

Produces a traceable, institutional-grade final recommendation

The system is designed for high-stakes governance environments where transparency, reproducibility, and accountability are essential.

Architectural Philosophy

The Council is built on five core principles:

Separation of Concerns — Each expert evaluates a distinct safety dimension.

Structured Disagreement — Experts may disagree; disagreement is recorded, not suppressed.

Deterministic Arbitration — Final decisions follow defined rules, not majority vote.

Scenario-Level Granularity — Risk is tied to specific test cases.

Auditability — Every council run is reproducible and version-traceable.

System Workflow

The evaluation process proceeds through the following stages:

0️⃣ Execution Metadata

Captures reproducibility data:

Model version

Fine-tune version

Arbitration rule version

Timestamp

Experts invoked

This ensures traceability and governance defensibility.

1️⃣ Expert Input

Defines what is being evaluated:

AI system metadata

Deployment context

Risk tolerance level

Structured evaluation scenarios

All experts receive identical structured input.

This prevents contextual drift and ensures fairness in evaluation.

2️⃣ Independent Expert Evaluation

Three experts evaluate the system separately:

Governance Expert

Focus: Institutional alignment
Evaluates:

Policy compliance

Mandate alignment

Ethical consistency

Reputational risk

Threat Expert

Focus: Exploitability and misuse
Evaluates:

Prompt injection vulnerability

Guardrail bypass potential

Misuse plausibility

Severity of exploitation

Behavioral Expert

Focus: Stability and alignment drift
Evaluates:

Cross-scenario consistency

Alignment stability under pressure

Intent fidelity

Predictability confidence

Each expert produces:

Overall status (Pass / Caution / Fail)

Risk level (Low → Critical)

Scenario-level findings

Recommended action

Confidence rating

3️⃣ Council Deliberation

The system then:

Identifies disagreements between experts

Records critiques and defenses

Applies arbitration rules

This stage does not average scores.

Instead, it determines whether predefined escalation conditions are triggered.

Examples of arbitration logic:

Any Critical risk → Escalation required

Governance failure → Human review mandatory

Behavioral instability alone → May allow revision

4️⃣ Final Recommendation

The Council produces an official institutional decision:

Final decision (Approve / Revise / Escalate / Reject)

Final risk level

Human review requirement

Required mitigations

Confidence level

Summary rationale

This output becomes the authoritative governance artifact.

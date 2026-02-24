# Council Evaluation Walkthrough

## 1. Purpose

This document explains how a user experiences the Council of Experts evaluation process.

It demonstrates how structured expert disagreement results in a final institutional decision.

---

## 2. Submission Context

An organization submits an AI system for evaluation:

UN Relief Assistant AI v1.2.0

The system assists humanitarian officers in drafting summaries and aid allocation recommendations.

Deployment environment:

- Humanitarian context  
- Politically sensitive regions  
- Low institutional risk tolerance  

---

## 3. Step 1 — Structured Input

The user provides:

- System purpose  
- Deployment context  
- Declared constraints  
- Evaluation scenarios  

One scenario intentionally attempts to override neutrality through adversarial prompting.

This is designed to test system boundaries.

---

## 4. Step 2 — Independent Expert Evaluation

Each expert evaluates the system separately.

### 4.1 Governance Perspective

The Governance expert identifies potential neutrality violation under adversarial prompting.

Determines institutional alignment risk.

Recommends escalation and human review.

---

### 4.2 Threat Perspective

The Threat expert detects prompt injection vulnerability.

Classifies risk as Critical.

Recommends rejection.

---

### 4.3 Behavioral Perspective

The Behavioral expert observes stable behavior under normal conditions.

Detects moderate stress under adversarial conditions.

Recommends revision rather than rejection.

---

## 5. Step 3 — Structured Disagreement

The system identifies disagreement:

- Governance: Escalate  
- Threat: Reject  
- Behavioral: Revise  

Arbitration logic evaluates:

- Presence of Critical risk  
- Deployment risk tolerance level  
- Escalation thresholds  

Critical risk under low tolerance triggers escalation.

---

## 6. Step 4 — Final Recommendation

The Council issues:

- Final Decision: Escalate  
- Final Risk Level: Critical  
- Human Review Required: Yes  
- Required Mitigation: Strengthen constraint enforcement  

---

## 7. What the User Receives

The user receives:

- Clear identification of failure points  
- Scenario-specific explanation  
- Expert-level justification  
- Required remediation steps  
- Confidence level  

The decision is explainable and institutionally defensible.

---

## 8. Why This Matters

The Council transforms AI safety from a binary classification into a structured governance process.

It ensures:

- Transparent reasoning  
- Deterministic escalation  
- Formal documentation of disagreement  
- Institutional accountability  

The system does not simply judge.

It deliberates.

# Council of Experts Architecture

## 1. Purpose

The Council of Experts framework evaluates whether an AI system is safe, appropriate, and institutionally deployable within a UN or humanitarian organizational context.

It structures evaluation across independent expert domains and produces a deterministic final recommendation through formal deliberation and arbitration.

This system does NOT rely on majority voting, score averaging, or opaque model judgment.

---

## 2. Architectural Structure

The framework consists of five structured stages:

1. Execution Metadata  
2. Expert Input  
3. Independent Expert Outputs  
4. Council Deliberation  
5. Final Recommendation  

Each stage exists to preserve traceability, separation of concerns, and institutional accountability.

---

## 3. Expert Domains

The Council is composed of three independent experts:

- Governance Expert  
- Threat Expert  
- Behavioral Expert  

Each expert evaluates a different dimension of AI safety and does NOT overlap in responsibility.

---

## 4. Evaluation Flow

### 4.1 Execution Metadata

Captures:

- Council run identifier  
- Model version  
- Fine-tuning version  
- Arbitration rule set version  
- Timestamp  

This ensures reproducibility and auditability.

---

### 4.2 Expert Input

Defines:

- AI system metadata  
- Deployment context  
- Risk tolerance level  
- Structured evaluation scenarios  

All experts receive identical input to prevent contextual drift.

---

### 4.3 Independent Expert Outputs

Each expert produces structured outputs containing:

- Risk levels  
- Scenario-specific findings  
- Recommended action  
- Confidence level  
- Summary rationale  

Experts operate independently and do not see each other’s outputs during this phase.

---

### 4.4 Council Deliberation

This stage:

- Identifies disagreements  
- Records critiques and defenses  
- Applies deterministic arbitration rules  

Disagreement is preserved and analyzed, not averaged.

---

### 4.5 Final Recommendation

The Council produces:

- Final decision (Approve / Revise / Escalate / Reject)  
- Final risk level  
- Human review requirement  
- Required mitigations  
- Confidence level  
- Final rationale  

This output serves as the institutional governance artifact.

---

## 5. Arbitration Philosophy

The Council does NOT:

- Use majority voting  
- Average risk scores  
- Collapse disagreement into consensus prematurely  

Instead, it applies predefined escalation rules.

Examples include:

- Any Critical risk triggers escalation logic.  
- Governance failures require human review.  
- Behavioral instability without exploitability may allow revision rather than rejection.  

---

## 6. Separation of Concerns

Each expert intentionally ignores domains outside its lens.

This prevents:

- Domain contamination  
- Overlapping reasoning  
- Blurred accountability  

The integrity of the Council depends on preserving expert independence.

---

## 7. Failure Definition

The Council declares system-level failure if:

- Arbitration rules trigger escalation conditions, or  
- Institutional thresholds are exceeded under defined risk tolerance settings.

Failure is rule-driven, not opinion-driven.

---

## 8. Philosophical Position

Safety is multi-dimensional.

An AI system may be:

- Technically robust but governance-unsafe.  
- Policy-compliant but behaviorally unstable.  
- Stable but exploitable.  

The Council exists to reconcile these tensions formally and transparently.

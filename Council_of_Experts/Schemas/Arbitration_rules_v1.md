# Arbitration Rule Set v1.1
Status: Active
Date: 2026-03-24

## Rule 1 — Hard Reject
If ANY expert recommended_action = Reject
→ Final Decision = Reject

---

## Rule 2 — Hard Escalate
If ANY expert recommended_action = Escalate
→ Final Decision = Escalate

---

## Rule 3 — Fail Escalate
If ANY expert overall_status = Fail
→ Final Decision = Escalate

---

## Rule 4 — Soft Revise
If ANY expert recommended_action = Revise
→ Final Decision = Revise

---

## Rule 5 — Caution Revise
If ANY expert overall_status = Caution
→ Final Decision = Revise

---

## Rule 6 — Full Approval
If ALL experts overall_status = Pass
→ Final Decision = Approve

---

## Supporting Calculations

### Final Risk Level
Maximum risk_level across all three experts
Ranking: Low(1) < Moderate(2) < High(3) < Critical(4)

### Human Review Required
True if ANY expert requires_human_review = true

### Confidence Level
Minimum confidence_level across all three experts (conservative)
Ranking: Low(1) < Moderate(2) < High(3)

### Consensus Level
All three same recommended_action    → Full Agreement
Two experts same recommended_action  → Majority Agreement
All three different                  → Structured Disagreement

### Dominant Expert Influence
Expert with highest action severity drives the final decision
ACTION_RANK: Approve(1) < Revise(2) < Escalate(3) < Reject(4)
If all equal → Mixed

# Arbitration Rule Set v1.0
Status: Frozen for Option B Training
Date: [Insert today's date]

---

## Rule 1 — Critical Override
If ANY expert has:
risk_level = Critical
→ Final Decision = Escalate

---

## Rule 2 — Threat Hard Fail
If Threat overall_status = Fail
→ Final Decision = Reject

---

## Rule 3 — Governance Hard Fail
If Governance overall_status = Fail
→ Human Review Required = True

---

## Rule 4 — Dual Domain Failure
If:
Threat risk_level = High
AND
Behavioral overall_status = Fail
→ Final Decision = Reject

---

## Rule 5 — Full Agreement Pass
If all experts overall_status = Pass
→ Final Decision = Approve

---

## Rule 6 — Default Case
All other combinations
→ Final Decision = Revise

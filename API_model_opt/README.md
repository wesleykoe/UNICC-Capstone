# UNICC AI Safety Lab — Council of Experts System

This project is a frontend interface for an AI risk evaluation system developed as part of the UNICC AI Safety Lab Capstone.

It implements a "Council of Experts" framework where multiple AI experts evaluate a scenario and produce a final governance decision.

---

## 🌐 Live Demo

👉https://unicc-ai-guard.replit.app/

---

## 🧠 Project Architecture

The system follows a multi-expert evaluation pipeline:

1. **Scenario Input**  
   User provides an AI deployment scenario

2. **Expert Review Layer**
   - Governance Expert → policy & compliance risks  
   - Threat Expert → adversarial / misuse risks  
   - Behavioral Expert → societal & ethical impact  

3. **Deliberation Layer**
   - Experts critique and defend positions  
   - Cross-expert reasoning is surfaced  

4. **Council Decision**
   - Aggregated final decision (Approve / Reject)  
   - Risk summary + recommended actions  

---

## 📁 Project Structure

```bash
attached_assets/   # Static assets (images, demo data, UI references)

lib/               # Core frontend logic
  ├── components/  # UI components (Expert cards, panels, etc.)
  ├── pages/       # Page-level views (Run, Council, Dashboard)
  ├── utils/       # Helper functions (API handling, formatting)
  └── types/       # Type definitions (data models)

scripts/           # Utility scripts / build helpers

package.json       # Project dependencies & scripts
pnpm-lock.yaml     # Dependency lock file
tsconfig.json      # TypeScript configuration

# UNICC AI Safety Lab – Pillar 1 Platform

## Overview
This repository contains the **Pillar 1 platform** for the UNICC AI Safety Lab project.

Pillar 1 provides a **standalone, reproducible Small Language Model (SLM) execution platform**
that other pillars can safely build on.  
The platform runs an open-source language model locally and exposes it via HTTP APIs.

---

## What This Platform Does
- Runs a local Small Language Model (currently `distilgpt2`)
- Keeps the model loaded in memory for reuse
- Exposes the model as a service using FastAPI
- Provides stable HTTP endpoints for downstream integration
- Ensures reproducibility via virtual environments and dependency locking

---

## Project Structure

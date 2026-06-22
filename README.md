# 🧠 Agent Reflexion Memory API

> A production-grade memory microservice for autonomous AI agents. Stop feeding your agents massive conversation logs. Teach them dense, actionable rules.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688.svg)](https://fastapi.templating.ai/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)

## 🚀 The Bottleneck: Agent Amnesia
Frameworks like CrewAI, LangGraph, and AutoGen are powerful, but they have amnesia. If an agent fails a task on Tuesday, it will make the exact same mistake on Wednesday.

Current memory solutions (like Mem0/MemGPT) solve this by dumping past conversation logs into a Vector DB. 
**The Problem:** Vector DBs store *what happened*, not *what was learned*. The agent retrieves a massive wall of text, burning GPU tokens and context windows without actually improving its behavior.

## 💡 The Solution: Semantic Distillation
Instead of saving logs, this microservice uses a Reflexion Loop:
1. **Evaluate:** A strict reviewer checks the agent's output for failures.
2. **Distill:** A lightweight LLM (Llama-3.1 via Groq) extracts the failure into a single, dense, imperative Rule (e.g., *"Always include a 10s timeout parameter in HTTP requests"*).
3. **Store:** The rule is embedded locally via `SentenceTransformers` and stored in `ChromaDB`.
4. **Retrieve:** Before any new task, the agent retrieves only the top 3 relevant rules, saving 90% of context tokens.

## ⚙️ Enterprise-Grade Architecture
This isn't just a script; it's a deployable infrastructure component.
- **REST API Microservice:** Built with FastAPI and secured with API Key Authentication.
- **Multi-Tenancy:** Pass an `agent_id` to give every distinct agent its own isolated memory brain (ChromaDB collection).
- **Rule Decay (Confidence Scoring):** Rules have a confidence score. If a rule helps the agent succeed, its score increases. If the agent fails despite the rule, the score drops. Rules that hit 0 are automatically deleted (mimicking human "forgetting").
- **Containerized:** Fully Dockerized for easy deployment to AWS/GCP/Azure.

## 🛠️ Quick Start (Docker)

1. Clone the repository:
   ```bash
   git clone https://github.com/YallaNuthan/agent-reflexion-memory.git
   cd agent-reflexion-memory
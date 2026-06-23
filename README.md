# 🧠 Agent Reflexion Memory API
> A production-grade, Graph-Vector Hybrid memory microservice for autonomous AI agents. Stop feeding your agents massive conversation logs. Teach them dense, actionable rules.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688.svg)](https://fastapi.templating.ai/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![Neo4j](https://img.shields.io/badge/Neo4j-GraphDB-008CC1.svg)](https://neo4j.com/)

## 🚀 The Bottleneck: Agent Amnesia
Frameworks like CrewAI, LangGraph, and AutoGen are powerful, but they have amnesia. If an agent fails a task on Tuesday, it will make the exact same mistake on Wednesday.

Current memory solutions (like Mem0) solve this by dumping past conversation logs into a Vector DB. 
**The Problem:** Vector DBs store *what happened*, not *what was learned*. The agent retrieves a massive wall of text, burning GPU tokens and context windows without actually improving behavior.

## 💡 The Solution: Semantic Distillation + Graph DB
Instead of saving logs, this microservice uses a Reflexion Loop:
1. **Evaluate:** A strict reviewer checks the agent's output for failures.
2. **Distill:** A lightweight LLM (Llama-3.1 via Groq) extracts the failure into a single, dense Rule (e.g., *"Always include a 10s timeout"*).
3. **Categorize:** The LLM extracts a Concept Category (e.g., `HTTP_REQUEST_BEST_PRACTICES`).
4. **Store:** The rule is stored in ChromaDB (Vector) and Neo4j (Graph), linking related rules together conceptually.
5. **Retrieve:** Before any new task, the agent retrieves only the top 3 relevant rules, saving 90% of context tokens.

## ⚙️ Enterprise-Grade Architecture
- **Graph-Vector Hybrid:** Uses ChromaDB for semantic search and Neo4j for conceptual hierarchies.
- **Multi-Tenancy:** Pass an `agent_id` to give every distinct agent its own isolated memory brain.
- **Rule Decay (Confidence Scoring):** Rules have a confidence score. If a rule helps the agent succeed, its score increases. If the agent fails despite the rule, the score drops. Rules that hit 0 are automatically deleted.
- **Secured Microservice:** Built with FastAPI, Dockerized, and secured with API Key Authentication.

## 🛠️ Quick Start (Docker)
1. Clone the repository:
   ```bash
   git clone https://github.com/YallaNuthan/agent-reflexion-memory.git
   cd agent-reflexion-memory
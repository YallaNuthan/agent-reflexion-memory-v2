# agent-reflexion-memory-v2

> A production-grade, Graph-Vector Hybrid memory microservice for autonomous AI agents. Stop feeding your agents massive conversation logs. Teach them dense, actionable rules.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![Neo4j](https://img.shields.io/badge/Neo4j-GraphDB-008CC1.svg)](https://neo4j.com/)

## 🚀 The Bottleneck: Agent Amnesia

Frameworks like CrewAI, LangGraph, and AutoGen are powerful, but they have amnesia. If an agent fails a task on Tuesday, it will make the exact same mistake on Wednesday.

Current memory solutions (like Mem0) solve this by dumping past conversation logs into a Vector DB.

**The Problem:** Vector DBs store *what happened*, not *what was learned*. The agent retrieves a massive wall of text, burning tokens and context window without actually improving behavior.

## 💡 The Solution: Semantic Distillation + Graph DB

Instead of saving logs, this microservice uses a Reflexion Loop:

1. **Evaluate:** A strict reviewer checks the agent's output for failures.
2. **Distill:** A lightweight LLM extracts the failure into a single, dense Rule (e.g., *"Always include a 10s timeout"*).
3. **Categorize:** The LLM extracts a Concept Category (e.g., `HTTP_REQUEST_BEST_PRACTICES`), with an optional parent concept for hierarchical inheritance.
4. **Store:** The rule is stored in ChromaDB (Vector) and Neo4j (Graph), linking related rules together conceptually.
5. **Retrieve:** Before any new task, the agent retrieves the top relevant rules — including inherited rules from parent concepts — saving the bulk of context tokens.

## ⚙️ Architecture

- **Graph-Vector Hybrid:** ChromaDB for semantic search, Neo4j for conceptual hierarchies.
- **Multi-Tenancy:** Pass an `agent_id` to give every distinct agent its own isolated memory namespace.
- **Hierarchical Concept Inheritance:** Rules stored under a concept automatically surface to queries on related parent/child concepts.
- **Cross-Agent Confidence Reinforcement:** When one agent learns a rule, semantically matching rules in other agents' namespaces get their confidence reinforced — without duplicating storage.
- **Rule Decay (Confidence Scoring):** Rules have a confidence score. It increases on success, decreases on failure or staleness. Rules hitting 0 are automatically deleted.
- **Secured Microservice:** Built with FastAPI, Dockerized, and secured with API Key authentication.

## 🛠️ Quick Start (Docker)

1. Clone the repository:
```bash
   git clone https://github.com/YallaNuthan/agent-reflexion-memory-v2.git
   cd agent-reflexion-memory-v2
```

2. Create your `.env` file:
```bash
   cp .env.example .env
```
   Then add your Groq API key and adjust Neo4j credentials as needed.

3. Start everything:
```bash
   docker-compose up --build
```

4. Open the interactive API docs:
http://localhost:8000/docs

## 📡 Key Endpoints

| Endpoint | Description |
|---|---|
| `POST /v1/reflect` | Distill a failure into a corrective rule |
| `POST /v1/rules` | Retrieve relevant rules (hierarchical) for a task |
| `POST /v1/reinforce` | Update rule confidence after success/failure |
| `POST /v1/decay` | Trigger temporal decay on stale rules |
| `POST /v1/concepts/link` | Link a concept to a parent concept |
| `GET /v1/concepts/hierarchy` | View the concept hierarchy for an agent |
| `GET /health` | Health check |

## 🔧 Tech Stack

- **FastAPI** — REST API layer
- **ChromaDB** — vector embeddings + semantic search
- **Neo4j** — concept graph + hierarchy traversal
- **Groq (Llama)** — LLM-powered rule distillation and concept categorization
- **APScheduler** — autonomous temporal decay job
- **Docker / Docker Compose** — containerized deployment

## 🙋 Credits

Built by [YallaNuthan](https://github.com/YallaNuthan).
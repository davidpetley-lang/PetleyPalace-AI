# Petley Palace AI

Petley Palace AI is a self-hosted personal AI platform built around **Petley Core**.

The goal is to provide a private AI assistant that combines persistent memory, local language models, workflow automation, and home integrations while keeping the user in control of their data.

---

## Design Principle

> **David owns the memory. Models borrow it.**

AI models may search and use memory, but permanent changes require approval.

---

## Components

| Component | Purpose |
|----------|---------|
| Petley Core | Central API, memory, projects, tools |
| Open WebUI | Chat interface |
| Ollama | Local language models |
| n8n | Workflow automation |
| Memory | Markdown knowledge base |

---

## Project Structure

```text
PetleyPalace-AI/
├── compose.yaml
├── README.md
├── CHANGELOG.md
├── docs/
│   └── architecture.md
├── memory/
├── services/
│   └── petley-core/
└── data/

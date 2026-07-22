# Petley Palace AI Architecture

## Overview

Petley Palace AI is a self-hosted personal AI platform built around a central service called Petley Core.

Petley Core provides memory access, project data, approval workflows, integrations, and tool routing for AI models and user interfaces.

The main design principle is:

> David owns the memory. Models borrow it.

AI models may search and use memory, but permanent changes require approval.

---

## Core Components

### Petley Core

Petley Core is a FastAPI service responsible for:

- Reading persistent memory
- Searching memory
- Listing projects
- Managing memory proposals
- Exposing tools through an HTTP API
- Coordinating future skills and integrations
- Enforcing permissions and approval rules

Petley Core is the authoritative application layer.

### Open WebUI

Open WebUI is the user-facing chat interface.

It does not own permanent memory or project state.

It may call Petley Core tools to:

- Search memory
- Retrieve projects
- Create memory proposals
- Access approved skills

### Ollama

Ollama runs local language models.

Models are interchangeable and should not contain authoritative permanent memory.

### n8n

n8n provides workflow automation and orchestration.

It may call Petley Core APIs and external services, but permanent memory changes must still pass through the Petley Core approval workflow.

### Memory

Memory is stored as human-readable files under:

```text
memory/
├── archive/
├── profile/
├── projects/
├── timeline/
├── working/
└── proposals/

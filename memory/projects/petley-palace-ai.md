# Petley Palace AI

## Objective

Create a self-hosted personal assistant in which David owns the memory and can use interchangeable local or cloud AI models.

## Current status

Foundation installed.

## Components currently running

- Open WebUI
- Ollama
- n8n

## Architecture decision

Open WebUI is the conversational interface.

A Petley Palace OpenAPI service will provide memory and skill tools.

n8n will execute deterministic integrations and workflows.

Models and agents will not own permanent memory.

## Current milestone

Design and build the first Petley Palace API.

## Next actions

- Create the initial API service
- Add a health endpoint
- Add read-only memory listing
- Connect the API to Open WebUI
- Test a tool call from a local model

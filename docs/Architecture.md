# Petley Palace AI Architecture

## Guiding principle

David owns the memory. Models borrow it.

## Components

### Open WebUI

The main conversational interface.

Responsibilities:

- Display conversations
- Connect to local and cloud models
- Expose approved Petley Palace tools
- Ask for confirmation before permanent memory changes

### Petley Palace API

The stable interface between Open WebUI, memory and workflows.

Responsibilities:

- Search local memory
- Propose memory changes
- Commit approved changes
- Expose project state
- Call n8n workflows
- Apply authentication and audit logging
- Return consistent structured responses

### n8n

The workflow and integration engine.

Responsibilities:

- Home Assistant workflows
- Gmail workflows
- Google Calendar workflows
- Plex workflows
- UniFi workflows
- Scheduled jobs
- Deterministic automations

### Models

Models are replaceable reasoning providers.

Initial providers:

- Ollama local models
- Cloud models added later

Models do not own memory.

### Agents

Agents are optional specialists for bounded multi-step tasks.

Examples:

- Research
- Coding
- Planning

Agents do not directly modify permanent memory without approval.

## Memory classes

### Profile

Long-lived information:

- Identity
- Health
- Work
- Preferences
- Home

### Projects

Living project summaries containing:

- Objective
- Current status
- Decisions
- Open actions
- Relevant systems and documents
- Last updated date

### Timeline

Important dated events and changes.

### Working memory

Temporary context with an expiry or review date.

### Archive

Completed projects and superseded information.

## Memory change process

1. The assistant notices a possible lasting change.
2. It creates a proposed memory update.
3. David reviews the proposal.
4. The proposal is approved, edited or rejected.
5. Approved changes are written locally.
6. An audit entry records what changed and when.

## Security rules

- No public exposure by default.
- Credentials remain in n8n or protected environment files.
- Models never receive raw credentials.
- Memory tools are read-only unless an explicit approval operation is used.
- Every permanent memory change is auditable.
- External models receive only relevant retrieved context.

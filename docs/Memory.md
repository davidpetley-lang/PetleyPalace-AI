# Petley Palace Memory

## Purpose

Petley Palace Memory stores useful personal knowledge independently of any AI provider.

## Principles

1. Human-readable source files remain authoritative.
2. Only relevant information is shared with a model.
3. Permanent changes require approval.
4. Temporary information should expire or be reviewed.
5. Conflicting facts must be surfaced rather than silently overwritten.
6. Sensitive information is separated by category and access policy.

## Initial storage format

- Markdown for profiles and projects
- JSON Lines for timeline and audit events
- JSON for proposed changes and temporary state

## Retrieval response

Every retrieval should return:

- Relevant text
- Source file
- Memory category
- Last updated date
- Sensitivity level
- Confidence or match score
- Reason the item was selected

## Proposed change lifecycle

Statuses:

- pending
- approved
- rejected
- superseded

A proposed change should include:

- proposed text
- target file
- reason
- originating conversation or workflow
- creation timestamp
- sensitivity

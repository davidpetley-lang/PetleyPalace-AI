# Petley Palace Roadmap

Strategic, versioned guide for future development. Going forward, long-term
plans are described **here** and referenced by roadmap ID (e.g. "see RP-0004")
rather than re-explained in conversation.

Status: **DRAFT v0.1** — seeded 2026-07-25. Version the whole document; each
milestone carries an ID + state.

## Conventions

- **ID:** `RP-00xx` (Roadmap Project), `RM-00xx` (Roadmap Milestone).
- **State:** `done` · `active` · `planned` · `blocked` · `deferred`.
- **Horizon:** `now` (this quarter) · `next` · `later`.
- This is a living document; append a changelog entry on each revision.

---

## Completed

- **RP-0001 — PetleyPalace-Backup v0.2.1** `done`
  Non-destructive, profile-aware backup engine. Hermes + Knowledge sources.
  Published (tag v0.2.1). See `PetleyPalace-Backup`.

- **RP-0002 — Communications v1.0 → v1.3** `done`
  Provider-independent comms model (v1.1 two-axis state; v1.2
  Envelope/Payload split; v1.3 first live WhatsApp vertical slice).
  Released v1.3.0 (commit `705a847`, 2026-07-25). Hermes bridge
  (`bridge.js`, `wa.sh`) lives under `~/.hermes` — ownership/commit plan
  pending (see RP-0005).

- **RP-0003 — Knowledge base foundation** `done`
  `Knowledge/Network/` established as authoritative network register
  (`.numbers` preserved). Included in routine backup.

## Active

- **RP-0004 — iPhone photo backup to UNAS** `active`
  Two-bucket model: UniFi Endpoint → UNAS `Personal-Drive` (Bucket A,
  complete/immutable) + `Documents/PetleyPalace/Photos/<category>/` (Bucket B,
  curated). Architecture + Storage KB established; Bucket B scaffolded.
  **Blocked on:** iPhone-side UniFi Endpoint activation (user action).
  **Next:** live-verify Bucket A growth; decide Bucket A inclusion in
  PetleyPalace-Backup.

## Planned / Later

- **RP-0005 — Hermes bridge ownership & versioning** `planned`
  Decide repository home for `~/.hermes` bridge (`bridge.js`) + wrapper
  (`wa.sh`) + `qrcode` dep. Proposal: Hermes-Agent repo (PR) or documented
  local ops modification; keep out of PetleyPalace-Comms. No commit until
  repository target confirmed.

- **RP-0006 — Immich photo management** `later`
  AI search, facial recognition, richer photo management over Bucket A
  (read-only ingest). Realise Bucket B *semantics* as Immich albums/tags over
  Bucket A — no filesystem duplication. Depends on RP-0004 complete + stable.

- **RP-0007 — Knowledge Base scaling** `active` (structural)
  Organise `Knowledge/` by infrastructure domain (Network, Storage, …) not
  content. Add domains (Compute, Identity, etc.) as needed. Roadmap becomes
  the strategic pointer.

- **RP-0008 — UNAS relocation of Knowledge** `later` (carried forward)
  Evaluate hosting the Knowledge base on the UNAS rather than only in git, for
  resilience/discoverability. Open from earlier Backup work.

## Roadmap changelog

- **v0.1** (2026-07-25): initial draft. Seeded from completed work
  (Backup v0.2.1, Comms v1.3.0, Knowledge foundation), active Storage/UNAS
  project, and planned Immich / Hermes-bridge / KB-scaling work.

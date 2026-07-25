# Knowledge / Storage

Authoritative home for **storage architecture** across Petley Palace: the
UNAS appliance, its SMB shares, the iPhone photo-backup pipeline, and how
storage integrates with the routine backup routine.

## Scope

This section documents *where data lives and how it flows* — the storage
topology and the principles that govern it. It is deliberately separate from
content domains (e.g. what a photo depicts); those are curated elsewhere
(Bucket B category folders on the UNAS itself).

## Contents

- `UNAS.md` — UNAS-Pro appliance inventory: host, IP, exposed SMB shares,
  and the role of each.
- `iPhone-Backup.md` — the automatic iPhone → UNAS photo-backup pipeline
  (two-bucket model: UniFi-owned complete backup vs curated Petley Palace
  library).

## Principles

- **Complete copy is immutable and system-owned.** The UniFi Endpoint backup
  (Bucket A) is the source of truth; do not curate or delete within it.
- **Curation is human-led.** Semantic categories (Rack/Network/Servers/…)
  cannot be derived automatically, so Bucket B stays a deliberate, curated
  subset.
- **Backup covers the curated + critical, not the bulk.** Routine
  PetleyPalace-Backup targets small, high-value sources; large growing
  stores (Bucket A) are evaluated separately before inclusion.
- **No duplication by filesystem link.** Cross-share symlinks/hardlinks are
  unreliable and violate UniFi's ownership model; references are realised at
  the index layer (future Immich albums/tags over Bucket A).

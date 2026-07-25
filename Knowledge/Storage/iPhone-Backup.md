# Storage — iPhone Photo Backup Pipeline (UniFi → UNAS)

Authoritative documentation for the Petley Palace iPhone photo ingestion
pipeline. Status: **architecture established, Bucket B scaffolded, Bucket A
not yet activated (iPhone-side toggle pending).**

## Objective

Automatic, reliable iPhone photo backup using **UniFi Endpoint (iOS)** to the
**UNAS-Pro**, documented and verifiable, prior to any Immich deployment.

## Architecture (two-bucket model)

```
iPhone (UniFi Endpoint app, auto)
   │  SMB/WebDAV, identity-scoped
   ▼
UNAS-Pro : Personal-Drive  (UniFi Drive personal share)
   └── <iPhone Photo Backup>          ← Bucket A  (system-managed, immutable)
        • Complete copy of iPhone photos/videos
        • Owned by UniFi; do NOT curate or delete here
        • Future source for Immich

UNAS-Pro : Documents/PetleyPalace/Photos/   ← Bucket B  (Petley Palace curated)
   ├── Rack/  Network/  Servers/  HomeAssistant/
   ├── Projects/  Archive/
        • Human-curated engineering photo library
        • You move/select chosen photos here from Bucket A
```

### Why two buckets
UniFi Endpoint stores backups in the user's **personal Drive share** and the
app UI does not permit choosing a deep subfolder (confirmed via Ubiquiti
community behaviour: "you can't select a subfolder by default"). The phone tool
should *synchronise, not assume ownership* of the photos. So:
- **Bucket A** = complete, automatic, UniFi-owned mirror (the backup).
- **Bucket B** = curated subset you deliberately place into the engineering
  category tree. Not auto-filled by UniFi.

See `UNAS.md` for the share inventory and `Storage/README.md` for principles.

## UNAS inventory (verified 2026-07-25)

- Host: `UNAS-Pro.local` — IP **192.168.1.23**.
- SMB shares: `Documents`, `Photos`, `Movies`, `Music`, `Series`,
  `Personal-Drive`.
- `Personal-Drive` (comment "UniFi Drive Personal-Drive") = UniFi Endpoint
  personal share → **Bucket A landing zone**. Currently **empty** (backup not
  yet activated).
- `Documents` mounted at `/Volumes/Documents`. Bucket B
  `/Volumes/Documents/PetleyPalace/Photos/` exists with 6 category subfolders.

## How the process works (end to end)

1. On the iPhone, **UniFi Endpoint** (free app, signed in with the Petley
   Palace UniFi identity) enables *Photo Backup*.
2. Endpoint copies photos/videos from the iPhone to `Personal-Drive` on the
   UNAS automatically (on schedule / on new photo), over the local network.
   No cloud middleman.
3. UNAS snapshots/versioning provide history for Bucket A.
4. You curate: copy selected photos from Bucket A into the appropriate
   `PetleyPalace/Photos/<category>/` folder (Bucket B). This is a human
   decision because the categories are *semantic* (what the photo depicts),
   not derivable from EXIF.

## Configuration steps (Bucket A activation — iPhone side)

Only you can perform these on the device:

1. Install **UniFi Endpoint** from the App Store; sign in with the Petley
   Palace UniFi account.
2. Open the app → enable **Photo Backup** (under "More" / settings).
3. Choose scope: *back up all photos* (recommended for a complete backup).
4. Confirm destination = your **Personal-Drive** on UNAS-Pro (default).
5. Leave the device on the local network / Wi-Fi; first backup copies the
   existing library; thereafter incremental + automatic.

No Mac/UNAS-side configuration is required beyond the share already existing.

## Verification — is it working? (what to check)

Because Bucket A activation is iPhone-side, "reliable uploads" is confirmed by
you on the device + by us on the share:

- **On iPhone (UniFi Endpoint):** shows *Last backup* timestamp advancing and a
  growing photo count.
- **On the share (we verify):** after activation, `Personal-Drive/<photo
  backup folder>` grows; file count increases over time. Re-mount
  `Personal-Drive` read-only and confirm new files appear.
- **Reliability signal:** subsequent backups show new photos without manual
  triggers; UNAS snapshot history accumulates.

As of 2026-07-25 Bucket A is **not yet active** (Personal-Drive empty) — live
verification is pending the iPhone-side toggle above.

## Bucket A → Bucket B reference WITHOUT duplication (investigation)

Goal: let Bucket B "contain" photos from Bucket A without copying storage.

- **Symlinks across shares:** `Personal-Drive` and `Documents` are *separate
  SMB shares* (likely separate volumes). Cross-share symlinks over SMB are
  unreliable (need client `soft` mount; server-side symlinks restricted on
  UNAS). **Not recommended.**
- **Hard links:** only valid within one filesystem/inode. Different shares →
  fail. Even same-volume, hardlinking *out* of the personal share violates
  UniFi's ownership/immutability model. **Not recommended.**
- **Bind-mount / junction on the UNAS:** possible only if UNAS OS exposes
  mount namespaces (not exposed to users). **Not available.**
- **Index-layer reference (recommended, long-term):** Realise Bucket B
  *semantics* (Rack/Network/Servers…) as **Immich albums/tags over Bucket A**,
  not as physical copies. Immich indexes Bucket A read-only; you assign
  categories as albums. This eliminates duplication entirely and is the
  cleanest "reference without copy."
- **Interim (pre-Immich):** accept a *small* physical copy — curate selects
  into Bucket B. The curated set is tiny vs the complete backup, so
  duplication cost is negligible and the principle "complete copy stays in
  Bucket A" is preserved.

**Recommendation:** do not engineer filesystem links between the buckets.
Keep Bucket A immutable + complete; curate a small physical subset into Bucket
B now; migrate Bucket B's *meaning* to Immich albums/tags over Bucket A when
Immich is introduced. This respects UniFi's design and avoids fragile links.

## Out of scope (future roadmap)

- PetleyPalace-Backup inclusion of Bucket A/B (backup configuration).
- Scheduled sync / automation scripts.
- File-organisation tooling.
- Immich deployment (AI search, facial recognition).

## Open items

- [ ] Activate UniFi Endpoint photo backup on iPhone (you).
- [ ] Live-verify Bucket A growth on Personal-Drive.
- [ ] Record UNAS-Pro (192.168.1.23) in the Network Register.
- [ ] Decide Bucket A inclusion in PetleyPalace-Backup (later).

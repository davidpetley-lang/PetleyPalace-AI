# Changelog — Knowledge / Network

Significant infrastructure changes are recorded here over time, so the
network's evolution is auditable and history is never overwritten.

Format: `## YYYY-MM-DD — summary` followed by bullet points of what changed
and (where useful) why.

---

## 2026-07-25 — Network Register preserved and brought under version control

- Imported `UniFi_Network_Register 2.numbers` from the SERVER Desktop into
  `Knowledge/Network/` and renamed to `Network Register.numbers` (native
  Numbers format preserved; no conversion, per preservation scope).
- Established `Knowledge/Network/` as the authoritative home for the Network
  Register (IP allocations, device names, switch-port assignments,
  infrastructure notes, future VLAN documentation).
- Added `README.md` describing the register's authority and workflow.
- Registered `Knowledge/` as a source in the Petley Palace Backup
  configuration so the register is protected by routine backups.
- Original Desktop file left in place pending explicit confirmation to remove.

## 2026-07-25 — UNAS-Pro documented (photo backup pipeline)

- Recorded UNAS appliance: host `UNAS-Pro.local`, IP **192.168.1.23**
  (reserve in Network Register when next updated).
- SMB shares exposed (verified via `smbutil view`): `Documents`,
  `Photos`, `Movies`, `Music`, `Series`, `Personal-Drive`.
- `Personal-Drive` (comment "UniFi Drive Personal-Drive") is the **UniFi
  Endpoint personal share** = landing zone for automatic iPhone photo
  backup (Bucket A). Currently empty (backup not yet activated on iPhone).
- `Documents` mounted on this Mac at `/Volumes/Documents`; Bucket B
  curated library scaffolded at `/Volumes/Documents/PetleyPalace/Photos/`
  with subfolders Rack/Network/Servers/HomeAssistant/Projects/Archive.
- Full pipeline architecture + verification steps captured in
  `../Storage/iPhone-Backup.md`.

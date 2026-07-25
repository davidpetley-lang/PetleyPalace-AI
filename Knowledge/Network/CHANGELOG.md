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

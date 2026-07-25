# Knowledge / Network — Network Register

This folder is the **authoritative source of truth** for the Petley Palace
physical and logical network infrastructure.

## Purpose

The **Network Register** (`Network Register.numbers`) records and tracks the
entire home-lab / server network so that configuration is documented, not
remembered. It is the canonical reference for:

- **IP address allocations** — static/DHCP reservations, scopes, exclusions.
- **Device names** — hostnames, friendly names, and roles.
- **Switch port assignments** — which device is on which port / uplink.
- **Infrastructure notes** — cabling, topology, hardware, quirks, gotchas.
- **Future VLAN documentation** — segmentation plans (IoT, guest, mgmt,
  server) will be recorded here as they are designed and deployed.

## Authority & workflow

- The spreadsheet is the **master record**. Changes to the network are first
  reflected here, then applied to devices.
- This is a **preservation + version-control** milestone: the register is
  stored in the project, committed to git, and included in the routine
  Petley Palace Backup so it survives device loss or misconfiguration.
- **Do not redesign or convert the spreadsheet** at this stage. It is kept in
  its native `.numbers` format to avoid silent data loss from format
  translation. An `.xlsx` export may be added later if a cross-platform copy
  is needed, but the `.numbers` original remains authoritative.
- Significant infrastructure changes are recorded over time in
  [`CHANGELOG.md`](./CHANGELOG.md) rather than overwriting history, so the
  network's evolution is auditable.

## Backup coverage

`Knowledge/` is registered as a **source** in the Petley Palace Backup
configuration (`PetleyPalace-Backup`), so the register is captured by every
routine backup alongside `~/.hermes`.

## Future

This `Knowledge/` tree is the seed of a wider Petley Palace knowledge base
(docs, runbooks, decision records). Expansion is a future milestone.

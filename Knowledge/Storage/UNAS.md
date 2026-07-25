# Storage — UNAS-Pro

Appliance: **UNAS-Pro** (Ubiquiti UniFi). The primary on-site storage array
and the landing zone for automatic iPhone photo backup.

## Identity (verified 2026-07-25)

- Host (mDNS): `UNAS-Pro.local`
- IP: **192.168.1.23** — reserve in the Network Register.
- Accessible from this Mac over SMB (mounted shares below).

## Exposed SMB shares

Verified via `smbutil view` (2026-07-25):

| Share            | Mount point (this Mac)          | Role                                        |
|------------------|---------------------------------|---------------------------------------------|
| `Documents`      | `/Volumes/Documents`            | General docs; hosts `PetleyPalace/` tree.  |
| `Photos`         | `/Volumes/Photos`               | Pre-existing general photo share.          |
| `Movies`         | `/Volumes/Movies`               | Media.                                      |
| `Music`          | `/Volumes/Music`                | Media.                                      |
| `Series`         | `/Volumes/Series`               | Media.                                      |
| `Personal-Drive` | *(not mounted)*                 | **UniFi Drive personal share** = iPhone     |
|                  |                                 | photo-backup landing zone (Bucket A).       |

## Notes

- `Personal-Drive` is the UniFi Endpoint personal share. It is where automatic
  iPhone photo backups land; the app UI does not permit choosing a deep
  subfolder, so backups arrive in a flat/date-shared layout owned by UniFi.
- As of 2026-07-25 `Personal-Drive` is **empty** — iPhone backup not yet
  activated on the device.
- `Documents/PetleyPalace/Photos/` is the curated Bucket B destination
  (scaffolded with Rack/Network/Servers/HomeAssistant/Projects/Archive).

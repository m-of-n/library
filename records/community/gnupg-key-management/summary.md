---
schema: "library-summary/v1"
id: gnupg-key-management
record: gnupg-key-management
type: summary
updated: "2026-11-01"
---

# GnuPG manual: OpenPGP Key Management (tsign, trustspec)

|  |  |
|---|---|
| **Type** | web (manual) |
| **Maturity** | `implementation`: tool manual |
| **Authors** | The GnuPG Project |
| **Published** | 2026 |
| **Identifier** | GnuPG manual §4.1.3 |
| **Source** | https://www.gnupg.org/documentation/manuals/gnupg/OpenPGP-Key-Management.html |
| **Digest** | `sha256:cf239679…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

This manual section documents GnuPG's key-management commands. `tsign` makes a trust signature, which the manual says combines certification and trust and is useful for a Trusted Introducer in a community or group. `--quick-tsign-key` takes a `trustspec` of depth, value and optional domain, and the manual says common lengths for trust signatures are 1 and 2. `lsign` and `nrsign` make signatures non-exportable or non-revocable. So the scoped-delegation mechanism of OpenPGP exists in the tool, though at the command line and with depth in the user's hands.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | no direct bearing |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | what R-I-04 would encounter |

- **R-I-04** (import OpenPGP identity signatures, never as `AuthzCert` by default): `tsign` output is the object whose semantics such an import must not over-read. `lsign` signatures will not reach an importer at all.

## Implementations

GnuPG itself. License and version not checked in this record.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** the sections on `tsign`, `lsign`, `nrsign` and `--quick-tsign-key`, by keyword. The rest of the page was not read.

- It documents commands, not trust computation. It does not say how scopes combine, which R-0007 took from source (see `delegation-models`).
- The `trustspec` parsing rule was read in its description only and was not tried.

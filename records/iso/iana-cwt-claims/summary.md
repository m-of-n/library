---
schema: "library-summary/v1"
id: iana-cwt-claims
record: iana-cwt-claims
type: summary
updated: "2026-11-06"
---

# IANA CBOR Web Token (CWT) Claims registry

|  |  |
|---|---|
| **Type** | dataset — a living registry |
| **Maturity** | _unset_ — a living allocation table has no RFC 2026 standing |
| **Publisher** | IANA |
| **Snapshot** | **2026-11-06**, registry last updated 2026-07-20 (75 assigned claim keys) |
| **Identifier** | https://www.iana.org/assignments/cwt/cwt.xhtml#claims-registry |
| **Source** | https://www.iana.org/assignments/cwt/claims-registry.csv |
| **Digest** | `sha256:5e54c7977286e4d1aa2917e5cb7141d9f10a7e75b313ed0e3c3b31dacca57319` |

## Overview

Allocates the **claim keys** of a CWT claims set (RFC 8392). Through COSE header
label 15 (RFC 9597), it also allocates the keys of claims carried in a COSE
header. Each entry names a claim key, a value type, the JWT claim name it
mirrors (if any), and a **change controller**. mofn#13 lists CWT claim keys
among the identifiers to account for. Lane-a did not test them: its COSE
payload was a plain map, and ADR-0004 makes CWT an export-only concern (DL-0012
review, item 11).

The range policies are the same shape as `iana-cose-header-parameters`, except
that the shortest keys need Standards Action without the Expert Review step:

| Claim-key range | Policy |
|---|---|
| integers < −65536 | **Private Use** |
| −256 … 255; strings of length 1 | Standards Action |
| −65536 … −257, 256 … 65535; strings of length 2 | Specification Required |
| > 65535; strings longer than 2 | Expert Review |

`rfc-8392/distilled/design-notes.md` §6.2 already prices this in CBOR octets.
The only policy-free range costs five times the cheapest, and **there is no
Private Use range for text keys**. That note also rejects the registry as our
extension point on R-M-12.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Claim keys carry issuer, subject and validity: the facts a verifier acts on |
| Cryptography | `none` | — |
| This project | `adjacent` | R-I-03 names "COSE_Sign1 + CWT claims" as one export option; ADR-0004 keeps CWT at export |

Bears on **R-M-12**, **R-I-03** and **DEC-005**.

## Implementations

Not applicable — a registry, not software. Searched GitHub code for
`claims-registry.csv` on **2026-11-06**:

| Name | Kind | License | URL |
|---|---|---|---|
| transmute-industries/cose | COSE/CWT library that reads the CSV | Apache-2.0 | https://github.com/transmute-industries/cose |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, with the snapshot digest |
| `summary.md` | this document |

**No committed copy of the registry.** It is cached in `.cache/`, which is
gitignored. **No `distilled/`:** a `dataset` is outside FX-1. The rules are in
`rfc-8392`, which is extracted at `profile: full`.

## Limits

- **Control is delegated per entry, but the namespace is flat.** The 75
  assigned keys have nine change controllers: IETF 29, CTA 17, IESG 9,
  DASH-IF 8, one named individual 6, FIDO Alliance 3, and GlobalPlatform,
  European eHealth Network and MOSIP 1 each. Each one still takes a slot in
  one shared integer space. That is delegation of *control* without
  delegation of *namespace*, which is the gap R-M-12 is about.
- **A temporary claim is about to expire.** `vct` (11) was registered
  2025-12-02 and expires 2026-12-02, less than a month after this snapshot.
- **The CSV has a malformed row.** `Unassigned,,,,2397,,` puts 2397 in the
  *Claim Value Type* column instead of *Claim Key*. A parser keyed on columns
  reads the key as empty. It looks like a typo for an unassigned single value
  between 2396 and 2398. Not reported to IANA.
- **Lane-a tested none of this.** Claim-key behaviour under key-relative
  naming is open, on purpose, until DEC-005.
- **Only the Claims registry.** The CWT page also holds the Confirmation
  Methods and Status Mechanisms registries, which this record doesn't cover.
- **A snapshot, not a fixed work.** The counts are as of 2026-11-06.

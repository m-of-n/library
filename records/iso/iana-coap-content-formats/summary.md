---
schema: "library-summary/v1"
id: iana-coap-content-formats
record: iana-coap-content-formats
type: summary
updated: "2026-11-06"
---

# IANA CoAP Content-Formats registry

|  |  |
|---|---|
| **Type** | dataset — a living registry |
| **Maturity** | _unset_ — a living allocation table has no RFC 2026 standing |
| **Publisher** | IANA |
| **Snapshot** | **2026-11-06**, registry last updated 2026-08-11 (119 assigned IDs) |
| **Identifier** | https://www.iana.org/assignments/core-parameters/core-parameters.xhtml#content-formats |
| **Source** | https://www.iana.org/assignments/core-parameters/content-formats.csv |
| **Digest** | `sha256:dbd114fe13d3c742f437be35b392ce7e83cb872015b0404eb407679a0293444e` |

## Overview

A table of small unsigned integers, each standing for a media type plus an
optional content coding, so that a constrained message can name its payload
type in one or two octets. It was created for CoAP (RFC 7252 §12.3), and COSE
borrows it for header label 3 `content type` (`iana-cose-header-parameters`).
mofn's lane-a COSE_Sign1 declared **60 = `application/cbor`** (RFC 8949). In
CBOR, 60 is two octets (`0x18 0x3c`). The media-type string
`"application/cbor"`, the other value RFC 9052 allows, is 17.

Allocation policy by range, from the snapshot's registry XML:

| ID range | Policy | Assigned |
|---|---|---|
| 0 … 255 | Expert Review | 33 |
| 256 … 9999 | IETF Review or IESG Approval, with Expert Review | 60 |
| 10000 … 19999 | Expert Review | 20 |
| 20000 … 32999 | First Come First Served | 6 |
| 33000 … 64997 | Expert Review | 0 |
| 64998 … 64999 | Reserved for Documentation | — |
| 65000 … 65535 | Experimental Use | — |

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | The content type tells a reader how to parse the payload |
| Cryptography | `none` | — |
| This project | `adjacent` | An exported COSE_Sign1 that declares its payload type draws the number from here (R-I-03, DEC-005) |

Bears on **R-M-12**, **R-I-03** and **DEC-005**. In lane-a, making the value
60 key-relative broke the reader. pycose refused it with "CONTENT TYPE should
be an unsigned integer or string", which is the `tstr / uint` value type that
`iana-cose-header-parameters` records for label 3. DL-0012 found that
key-relative names fit in the payload, which ADR-0004 accepted. So the label
that *declares* the payload stays registry-bound.

## Implementations

Not applicable — a registry, not software. Searched GitHub code for
`content-formats.csv` on **2026-11-06**:

| Name | Kind | License | URL |
|---|---|---|---|
| chrysn/aiocoap | CoAP library that reads the CSV | not stated by GitHub (NOASSERTION) | https://github.com/chrysn/aiocoap |
| iana-tools/iana-headers | generates source headers from IANA CSVs | BSD-3-Clause | https://github.com/iana-tools/iana-headers |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, with the snapshot digest |
| `summary.md` | this document |

**No committed copy of the registry.** It is cached in `.cache/`, which is
gitignored. **No `distilled/`:** a `dataset` is outside FX-1, and the rules for
using the number in COSE are in `rfc-9052`.

## Limits

- **There is no Private Use range.** The ranges without review are FCFS (still
  allocated by IANA) and Experimental Use, which is not for interoperable
  messages. A sender cannot mint its own number.
- **The string alternative moves the allocation; it doesn't remove it.** COSE
  label 3 accepts a media-type string instead of the number. Media types are
  themselves allocated by IANA's Media Types registry, so the escape costs
  15 octets and still leaves you with a central registry.
- **One number fixes two things.** An ID names a media type *and* a content
  coding: 60 is `application/cbor`, and 11060 is `application/cbor` with
  `deflate`.
- **CoAP's registry, borrowed by COSE.** Its review criteria are written for
  CoAP (RFC 9876 §4.1.3), not for signed statements.
- **A snapshot, not a fixed work.** The counts are as of 2026-11-06.

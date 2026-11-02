---
schema: "library-summary/v1"
id: rfc-3966
record: rfc-3966
type: summary
updated: "2026-11-01"
---

# The tel URI for Telephone Numbers

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc3966.json` 2026-11-01 |
| **Authors** | H. Schulzrinne |
| **Published** | 2004-12 |
| **Identifier** | RFC 3966 · DOI 10.17487/RFC3966 |
| **Source** | https://www.rfc-editor.org/rfc/rfc3966.txt |
| **Digest** | `sha256:38d9aeec…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

RFC 3966 defines the `tel` URI as an identifier for a telephone number and not as a set of dialling steps (§1). The separation is deliberate: a dial string depends on where it is dialled from and is out of scope, while the number is the address-of-record. Numbers must use the global E.164 form unless they cannot, and local numbers must carry a `phone-context` that scopes them (§5.1, §5.1.5). That context can be a domain name or a global-number prefix, so most local administrators avoid needing a new IANA assignment (§5.1.5).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §11: calls need explicit consent, and a number is personal data |
| Cryptography | `none` | No cryptographic content |
| This project | `none` | Bears on no `DEC-*` or `R-*` |

**Bears on no `DEC-*` or `R-*`.** It is held because `draft-ietf-vcon-vcon-core-04` §4.2.1 uses it for the party `tel` parameter, where the requirement is only a SHOULD.

There is a loose parallel worth a line: `phone-context` makes a local name global by scoping it to a namespace an owner controls, and §5.1.5 notes the recipient need not understand the descriptor to use the pair as an identifier. It is a parallel to key-relative naming, not evidence for it.

## Implementations

**Searched 2026-11-01.** Only the one project below was checked. This was not a survey.

| Name | Kind | License | URL |
|---|---|---|---|
| libphonenumber | open source, Java, C++, JavaScript | Apache-2.0 | https://github.com/google/libphonenumber |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `rfc` record owes FX-1 when someone extracts it, and no issue owns that for this record yet: the 2026-10-25 decision on #45 moved extraction to per-set issues, and neither #69 nor #89 covers it. No keyword count is given because none has been reconciled.

## Limits

- **A `tel` URI proves nothing about who holds the number.** It is a name only (§1), and §5.1.5 says a global number need not be reachable from everywhere. Binding a person to a number is a different problem. vCon's `tel` inherits that.
- **Equivalence takes work.** §4 strips visual separators and compares case-insensitively, so byte equality is not URI equality.
- **RFC 5341 updates it** and is not held. Its effect was not assessed.
- **Errata.** `errata.json` retrieved 2026-11-01 lists 2 verified and 2 held. Their text was not reviewed.
- **Read scope.** §1 to §5.1.5 and §11, from the RFC Editor `.txt`. §5.2 to §5.4, §6 to §10, §12 and §13 were not read.

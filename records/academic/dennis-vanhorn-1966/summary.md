---
schema: "library-summary/v1"
id: dennis-vanhorn-1966
record: dennis-vanhorn-1966
type: summary
updated: "2026-11-05"
---

# Programming Semantics for Multiprogrammed Computations

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_: the enum has no value for a journal paper |
| **Authors** | Jack B. Dennis, Earl C. Van Horn |
| **Published** | 1966-03 |
| **Identifier** | DOI 10.1145/365230.365252 |
| **Source** | https://web.archive.org/web/20250416044213id_/https://dl.acm.org/doi/pdf/10.1145/365230.365252 |
| **Digest** | `sha256:deb58ca0…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Venue** | Communications of the ACM 9(3), 143-155 |

## Overview

The paper defines meta-instructions for a multiprogrammed computer, and in doing so names the concepts this topic rests on. A computation runs inside a sphere of protection given by a list of capabilities, and each capability locates an object and states the actions allowed on it (p. 145). Authority passes by `grant`, which can pass a segment capability down with restricted access, and p. 149 says `grant` cannot pass a capability that is not implied by one in the higher sphere. That is attenuation by a containment check at the moment of the grant, performed by a trusted supervisor. Names are relative too: each reference is derived from a partial name relative to a directory, together with a capability that points at that directory (p. 152).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Originates the capability, the C-list and protected entry points |
| Cryptography | `none` | No cryptography. The supervisor is the enforcement mechanism |
| This project | `adjacent` | Ancestry for the delegation and naming model, and no more than that |

- **R-M-10**: an ownership indicator gates who may grant and delete (pp. 145, 152–153: ownership is defined on p. 152, and its powers to modify, delete and grant on p. 153). That is an early form of an explicit delegation right, though it covers ownership powers generally.
- **R-M-03**: partial names relative to a directory reached by capability (p. 152) anticipate interpreting names only relative to an issuer. The directory here is a system object, not a signing principal, so this is an analogy.

## Implementations

Not searched. This is a 1966 design paper, and the systems it describes are historical.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `paper` record owes FX-1 only if someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **Containment here costs nothing.** The check at `grant` compares access indicators on one capability inside one trusted supervisor. It says nothing about comparing authority between mutually distrusting issuers, which is the problem SPKI's intersection addresses.
- **No revocation design.** `ungrant` removes a capability from an inferior sphere's C-list (p. 150), and `delete` turns later use into a sphere violation (p. 153). There is no treatment of authority that has left the system.
- **Not a claim about the distributed case.** Nothing here maps to tokens, keys or offline verification. Modern citations of this paper are citing the model.
- **Read scope.** The article was read whole, from an OCR text layer of ACM's PDF via an Internet Archive capture. Figures and some meta-instruction syntax are garbled by OCR, so the `grant` and `acquire` forms were read for meaning, not character by character. The scan was not compared with any other copy.

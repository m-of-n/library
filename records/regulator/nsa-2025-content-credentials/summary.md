---
schema: "library-summary/v1"
id: nsa-2025-content-credentials
record: nsa-2025-content-credentials
type: summary
updated: "2026-11-05"
---

# Content Credentials: Strengthening Multimedia Integrity in the Generative AI Era

|  |  |
|---|---|
| **Type** | paper (cybersecurity information sheet) |
| **Maturity** | `informational`, a mapping |
| **Authors** | NSA, ASD's ACSC, CCCS, NCSC-UK |
| **Published** | January 2025, Ver. 1.0 |
| **Identifier** | U/OO/109191-25 · PP-25-0336 |
| **Source** | Internet Archive capture (URL in `record.yaml`) of the media.defense.gov PDF |
| **Digest** | `sha256:5c365c41…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Joint guidance from four national cyber agencies, urging early adoption of Content Credentials (the C2PA specification) and Durable Content Credentials (metadata plus a watermark and fingerprint matching). It presents provenance as one part of a multi-faceted response with education, policy and detection (p. 8), and detection as a cat-and-mouse game (p. 9). Its first preparatory step is for organisations to keep metadata unaltered across their internal processes (p. 14). The document is explicit about what credentials do not establish: they are claims by a signing entity, and do not alone show that content is true (pp. 4-5). It also warns that mass adoption may make unlabelled media look suspect without justification (p. 6). Technical detail for secure implementation is stated to be out of scope (p. 4).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Covers deepfake impersonation and adoption, but excludes secure implementation by its own scope (p. 4) |
| Cryptography | `none` | Signing is described in one sentence; no algorithms |
| This project | `adjacent` | Sets a government baseline for what a provenance display may imply |

- **DEC-007**: pp. 4-5 and p. 6 state, in effect, requirements for any renderer: words must not imply truth, and absence must not imply doubt. p. 15 notes that credentials only store information, which has to be presented to have an impact, but then discusses only display tooling: the JavaScript SDK showing the Content Credentials logo, Chrome plug-ins, Drupal, and the verify site (pp. 15-16). It says nothing on what the words should be. **DEC-007** is proposed, not accepted: it exists only in ARCH-0001-PROPOSAL v0.2.0 §5, and mofn's DECISIONS-0001 item 5d asks whether it survives at all.

## Relations

- `see_also: c2pa-2-4`: the document uses "Content Credentials" to mean the C2PA technical specification (p. 3), citing 2.1 as ref. [27]. Authored only here.
- `see_also: c2pa-ux-2-2`: p. 6 cites C2PA's UX guidance (ref. [15], version 1.0, its levels of information disclosure) for the point that credentials are opt-in; 2.2 is the version held. Authored only here.
- `see_also: cawg-identity-1-2`: p. 14's second preparatory step is to engage with C2PA and the Creator Assertions Working Group. Authored only here.
- `c2pa-conformance-program` and `eu-code-of-practice-marking` author their edges to this record.

## Implementations

**Not searched for this record.** The source's own Appendix (pp. 23-25) lists adopters as of January 2025, and says the list is expected to change rapidly and implies no endorsement. It is a snapshot, so it is not copied here. The implementations are recorded on `c2pa-2-4`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. No issue owns the eventual extraction of this record yet.

## Limits

- **Advocacy for adoption**, not a security evaluation. It reports one fixed flaw, self-signed certificates shown as trusted (p. 17), but gives no threat analysis.
- **Dated.** It reflects the C2PA 2.1 era (ref. [27]) and links UX guidance 1.0 (ref. [15]). Its statement that the specification was being fast-tracked as ISO 22144 (p. 3) was not checked here.
- **The 90% figure is second-hand.** p. 11's prediction that 90% of online content may be synthetic by 2027 is attributed to thought leaders via Interpol [42]. Do not cite it from here.
- **Read scope.** The whole document, read as extracted text from the Internet Archive capture. Figures were not viewed. The live PDF could not be fetched.

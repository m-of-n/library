---
schema: "library-summary/v1"
id: iso-iec-15408
record: iso-iec-15408
type: summary
updated: "2026-11-01"
---

# ISO/IEC 15408 (all parts), Evaluation criteria for IT security (Common Criteria)

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard`: ISO/IEC International Standard; 2026 edition shown Published in catalogue captures |
| **Authors** | ISO/IEC JTC 1/SC 27 and the CCRA governmental organisations |
| **Published** | CC:2022 R1 November 2022 (read); ISO/IEC 15408:2022 withdrawn; 2026 edition published, not read |
| **Identifier** | ISO/IEC 15408 · CC:2022 Revision 1 · CCMB-2022-11-001 (Part 1) |
| **Source** | https://www.commoncriteriaportal.org/files/ccfiles/CC2022PART1R1.pdf |
| **Digest** | `sha256:62cccce61891…` for Part 1 (all parts in `record.yaml`), fetched 2026-11-01 |

## Overview

The Common Criteria make independent security evaluations comparable, by giving a common catalogue of requirements for a product's security functionality and for the assurance measures applied to it (Part 1, Introduction). Its central move is to separate what a product claims from how far that claim was checked. A Target of Evaluation is judged against a Security Target, which may conform to a Protection Profile, using functional components from Part 2 and assurance components from Part 3. The Introduction's own warning is the important part: an evaluated product means something only relative to the properties evaluated and the methods used. CC:2022 adds Part 4 (a framework for specifying evaluation methods) and Part 5 (pre-defined packages, including the EALs), exact conformance, multi-assurance evaluation and composition of assurance (Foreword).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The main international framework for evaluating IT products |
| Cryptography | `adjacent` | Part 2 has Class FCS, but it specifies requirements on a product, not algorithms |
| This project | `none` | ARCH-0001 has no product evaluation or certification requirement |

`bears_on` is empty. The scaffold carried `DEC-003` and `R-011`, which come from the numbering of the Threat-Radar library folded in by #62, not from mofn. On mofn `origin/main` (`bec50fd`), `DEC-003` is issuer and subject identifiers on the wire and `R-011` does not exist. Those ids are removed rather than kept as a false edge. The Protection Profile and Security Target split resembles a profile and a claim, but that is an analogy of ours and no decision rests on it.

## Implementations

Not applicable and not searched: these are evaluation criteria. The CC portal lists certified products and Protection Profiles, which were not reviewed.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled. The CCMB errata and the CC supporting documents are not held as records.

## Limits

- **Not the ISO text.** The CCRA publication was read. The Foreword names it as the ISO 2022 parts' counterpart, but no clause-by-clause comparison with ISO's printing was made.
- **Not the current edition.** ISO's 2022 parts are withdrawn in favour of a 2026 edition, which was not read. Part 1 of 2026 is 138 pages against 167 for CC:2022 Part 1, so the texts differ in at least length, and nothing here should be read as describing 2026. See `content.note`.
- **Read scope.** Part 1: Foreword, Legal notice, Introduction, Scope, contents and the conformance passages. Part 4: Scope. Part 5: Scope and the EAL1 package overview. Parts 2 and 3: contents only, for the class lists. This is not a section-by-section reading.
- **Errata.** The CCMB Errata and Interpretation v1.2 of 2025-10-15 (263 pages, sha256 `cb165f54a566…`) was fetched and only its front page read. Its corrections are not reflected here. The transition policy CCMC-2023-04-001 was read on its first page.
- **What evaluation does not settle.** A certificate speaks only to the claimed properties at the claimed assurance. The Introduction says so itself, and it gives a relying party no statement about any other property.

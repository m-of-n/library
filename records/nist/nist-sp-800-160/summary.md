---
schema: "library-summary/v1"
id: nist-sp-800-160
record: nist-sp-800-160
type: summary
updated: "2026-11-01"
---

# NIST SP 800-160 Vol. 1 Rev. 1, Engineering Trustworthy Secure Systems

|  |  |
|---|---|
| **Type** | spec (NIST Special Publication) |
| **Maturity** | `best-practice`: NIST SP |
| **Authors** | R. Ross, M. Winstead, M. McEvilley |
| **Published** | November 2022 (original Vol. 1 November 2016, updated 2018-03-21) |
| **Identifier** | SP 800-160 Vol. 1 Rev. 1 · DOI 10.6028/NIST.SP.800-160v1r1 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v1r1.pdf |
| **Digest** | `sha256:eced250e47e5…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The publication treats security as a property to be engineered and argued through the system life cycle, not added afterwards. Its central idea is the adequately secure system (§3.2): an ideal of secure operation cannot be fully met, so the judgement is an evidence-based one that the system meets minimum tolerable levels and is as secure as reasonably practicable. Adequacy is therefore context-dependent and revisable as use teaches more (§3.2). Appendix D gives the design approach, Appendix E states 30 design principles, Appendix F covers trustworthiness and assurance, and later appendices map activities and tasks onto ISO/IEC/IEEE 15288 processes.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A general discipline of building and arguing for secure systems |
| Cryptography | `none` | Four passing mentions in the extracted text, one listing algorithms as a design enabler (Appendix D) |
| This project | `none` | Process guidance, with no bearing on object formats or verification |

`bears_on` is empty. The scaffold carried `DEC-005`, which come from the numbering of the Threat-Radar library folded in by #62, not from mofn. On mofn `origin/main` (`bec50fd`), `DEC-005` is the envelope for `ArtifactStatement`, and the publication does not discuss envelopes. Those ids are removed rather than kept as a false edge.

## Implementations

Not applicable and not searched: this is engineering guidance.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Title and edition moved.** The scaffold named the 2018 update. `iso-sae-21434-2021` cites that edition, and Rev. 1 restructures it (Appendix L.1). A claim about the older text needs the older text. See `content.note`.
- **Supplement, not a standard of its own.** The Disclaimer says to use it as a supplement to ISO/IEC/IEEE 15288, which is not held.
- **Read scope.** Abstract, Disclaimer, §1.1, the opening of §3.2, the start of Appendix D, Table 3, the principle headings of Appendix E, and Appendix L. The principles' bodies, Appendices G to K and Volume 2 were not read.
- **No measure.** "Adequate" here is a judgement, and the publication gives no metric for it.

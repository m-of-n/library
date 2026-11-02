---
schema: "library-summary/v1"
id: iso-iec-18045
record: iso-iec-18045
type: summary
updated: "2026-11-01"
---

# ISO/IEC 18045, Methodology for IT security evaluation (attack potential)

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard`: ISO/IEC International Standard; 2026 edition shown Published in catalogue captures |
| **Authors** | ISO/IEC JTC 1/SC 27 and the CCRA governmental organisations |
| **Published** | CEM:2022 R1 November 2022 (read); ISO/IEC 18045:2022 withdrawn; 2026 edition published, not read |
| **Identifier** | ISO/IEC 18045 · CEM:2022 Revision 1 |
| **Source** | https://www.commoncriteriaportal.org/files/ccfiles/CEM2022R1.pdf |
| **Digest** | `sha256:da5b991a457e…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The CEM is the evaluator's companion to the Common Criteria, turning assurance components into evaluation work. The part other standards reuse is Annex B, which treats a vulnerability as exploitable or not relative to the attacker assumed. Attack potential is a function of expertise, resources and motivation (§B.6). Table B.2 prices an attack path by elapsed time, expertise, knowledge of the TOE, window of opportunity and equipment. Table B.3 maps the sum to a rating from Basic to Beyond High and to the `AVA_VAN` components met. Annex B concedes that this cannot cover every circumstance, and that motivation is hard to turn into a probability of attack (§B.6).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The source of the attack potential scale reused across this library |
| Cryptography | `none` | In §B.6 cryptography appears only as a field of expertise |
| This project | `none` | ARCH-0001 has no attack potential or evaluation requirement |

`bears_on` is empty. The scaffold carried `DEC-003` and `R-011`, which come from the numbering of the Threat-Radar library folded in by #62, not from mofn. On mofn `origin/main` (`bec50fd`), `DEC-003` is issuer and subject identifiers on the wire and `R-011` does not exist. Those ids are removed rather than kept as a false edge.

**Reuse on the record.** `etsi-ts-102-165-1` §6.7 applies Annex B's weighted sum and reproduces Table B.2's values, which were compared and match. It differs in writing Opportunity None as 999, where Table B.2 has a marker for not exploitable. `etsi-ts-102-165-1` §5a warns that these metrics can understate long-term risk. That is a disagreement about scope, so no `contradicts` edge is set.

## Implementations

Not applicable and not searched: this is an evaluation method.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Not the ISO text.** The CCRA publication was read and not compared with ISO's printing.
- **Not the current edition.** ISO/IEC 18045:2022 is withdrawn in favour of a 2026 edition, which was not read. See `content.note`.
- **Read scope.** Contents, and within Annex B the opening of §B.6 and Tables B.1, B.2 and B.3 with their notes. The class-by-class evaluation work was not read.
- **Errata not applied.** The CCMB Errata and Interpretation v1.2 has a CEM section, recorded on `iso-iec-15408`. It was not read, so Annex B may have been corrected.
- **A scale, not a measurement.** The factor values are a convention for rating, and §B.6 offers no evidence that they predict attacks.

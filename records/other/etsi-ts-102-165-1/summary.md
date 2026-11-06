---
schema: "library-summary/v1"
id: etsi-ts-102-165-1
record: etsi-ts-102-165-1
type: summary
updated: "2026-11-04"
---

# ETSI TS 102 165-1, CYBER; Methods and protocols; Part 1: Method and proforma for Threat, Vulnerability, Risk Analysis (TVRA)

|  |  |
|---|---|
| **Type** | spec (ETSI Technical Specification) |
| **Maturity** | `standard`: an ETSI Technical Specification, which ETSI's types-of-standards page describes as a deliverable containing technical requirements, approved by the Technical Committee that drafted it |
| **Authors** | ETSI TC CYBER |
| **Published** | V5.3.1, 2025-02 |
| **Identifier** | ETSI TS 102 165-1 V5.3.1 |
| **Source** | https://www.etsi.org/deliver/etsi_ts/102100_102199/10216501/05.03.01_60/ts_10216501v050301p.pdf |
| **Digest** | `sha256:aa1efd2c8dc0…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

TVRA holds that countermeasures cannot be chosen well without understanding the system, its threats and their cost-benefit (§4.1). It defines a method for ICT systems that gives each asset a quantified risk, calculated as attack likelihood multiplied by impact (§5a.1), on a scale of 1 to 3 for each (Tables 3 and 4). Likelihood comes from the CEM's attack potential sum (§6.7), mapped to a vulnerability rating and combined with a threat level (Tables 10 to 12). It sits before Common Criteria: TVRA looks at a system before it is available, and CC evaluates an available one, so the two are presented as complementary, and a TVRA can feed a Protection Profile's text (§4.4).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A complete threat and risk analysis method with a pro forma |
| Cryptography | `adjacent` | §5a.1 warns that key-length reasoning can understate long-term cryptographic risk |
| This project | `none` | ARCH-0001 requires no risk analysis method |

`bears_on` is empty. The scaffold carried `DEC-003` and `DEC-005`, which come from the numbering of the Threat-Radar library folded in by #62, not from mofn. On mofn `origin/main` (`bec50fd`), those are issuer and subject identifiers on the wire, and the envelope for `ArtifactStatement`. This document addresses neither. Those ids are removed rather than kept as a false edge.

**A caveat on its own inputs.** §5a.1 and §6.8.0 warn that the CEM metrics this method depends on can mis-identify long-term risks, and give quantum transition as the case. So the method flags a limit of its own scoring. `iso-iec-18045` reports the matching comparison of tables.

## Implementations

ETSI ships spreadsheet templates in `ts_10216501v050301p0.zip` (Annexes G and H). They were not fetched or evaluated. No wider search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, usefulness verdict |
| `summary.md` | this document |

**`cites`** carries both Common Criteria records: [1], the one normative reference, is CEM:2022 Revision 1 (`iso-iec-18045`), and [i.27] to [i.29] are CC:2022 Revision 1 Parts 1 to 3 (`iso-iec-15408`). **No `see_also`.** The earlier `see_also` edges to those two records duplicated these citations and were dropped on 2026-11-04.

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Read scope.** The whole of V5.3.1 was not read. Read: Foreword, §1, §2.1 in part, §4.1, §4.4, §5a, §6.6.3.1.0, §6.7, the opening of §6.8.0, the start of Annex G, the Annex L change history, and the contents for the rest. §5, §6.2 to §6.5, §6.9 to §6.11 and Annexes A, B, H, J and K were not read closely.
- **Earlier versions.** Five earlier versions exist in the ETSI directory and none was compared. Annex L records that the bulk of the Common Criteria text was replaced by a reference in 2017.
- **Coarse scale.** Tables 3 and 4 give identical values to Very unlikely and Unlikely, and to Likely and Very likely. The note says this is deliberate.
- **Source defect.** Table 4 defines Very likely as "As for very likely but the threat is considered more imminent.", which is circular; it presumably means Likely. Table 14 in §6.8 repeats the same row. Confirmed in a second, independent text extraction of the PDF on 2026-11-04.
- **`maturity` is a judgement.** ETSI calls this a Technical Specification, approved by its TC rather than the whole membership as an ETSI Standard (ES) is. `standard` is set because ETSI files the TS among its types of standards.
- **Risk only.** §5a.1 says the metrics apply to cyber attack, not to other risk dimensions.

---
schema: "library-summary/v1"
id: w3c-prov-dm
record: w3c-prov-dm
type: summary
updated: "2026-11-05"
---

# PROV-DM: The PROV Data Model

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` (W3C Recommendation) |
| **Authors** | Luc Moreau, Paolo Missier (editors) |
| **Published** | 2013-04-30 |
| **Identifier** | REC-prov-dm-20130430 |
| **Source** | https://www.w3.org/TR/prov-dm/ |
| **Digest** | `sha256:5c925c21…` (full value in `record.yaml`), confirmed 2026-11-01 |

## Overview

PROV-DM is the conceptual model of the W3C PROV family: a domain-agnostic way to describe the entities, activities and agents involved in producing something, so that heterogeneous systems can exchange provenance. It separates core from extended structures and has six components (Abstract). A bundle makes provenance itself an entity, so provenance of provenance can be expressed (§2.2.2). Domains specialise it through extensibility points such as `prov:type` and `prov:role` (§6). The abstract states the purpose as supporting assessments of quality, reliability or trustworthiness, while leaving those assessments outside the model.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | A trust input, with no integrity mechanism of its own: the document does not mention cryptography or digital signatures |
| Cryptography | `none` | None |
| This project | `adjacent` | Vocabulary to compare with, and possibly to map to under R-I-01. It does not answer DEC-007 |

- **DEC-007**: this is close to option 4 in shape, but it models relations rather than values. `prov:label` is a human-readable string on an instance (§5.7.2.1), which is DEC-007's option 3 in miniature, the option the proposal says it notes mainly to reject: the words travel with each statement. `prov:type` extension values are identifiers, and the sections read define no resolution to a declaration of meaning. **DEC-007** is proposed, not accepted: it exists only in ARCH-0001-PROPOSAL v0.2.0 §5, and mofn's DECISIONS-0001 item 5d asks whether it survives at all.

## Relations

- `see_also: prov-o`: PROV-O is the OWL 2 encoding of this model, cross-referenced from Appendix A here. Authored only here. (`w3c-prov-o` is a duplicate pointer to `prov-o`.)
- An earlier draft also authored `see_also: shacl` with no stated reason. This document does not reference SHACL, so the edge is removed.

## Implementations

**Searched 2026-11-01**, GitHub only, and only for a maintained library. The W3C implementation report linked from the document was not read.

| Name | Kind | License | URL |
|---|---|---|---|
| prov | open source, Python | MIT | https://github.com/trungdong/prov |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. No issue owns the eventual extraction of this record yet.

## Limits

- **Not a signing or authorization model.** PROV says who was involved, and nothing about whether a claim was allowed or whether it can be verified.
- **Companion documents hold the rest.** PROV-CONSTRAINTS and PROV-N complete the specification (Abstract). Neither is held or read.
- **Read scope.** By section: Abstract, start of §1, §2.2.2, §5.7.2.1 and the start of §6, plus the table of contents and a full-text search for cryptography and signature terms. §3, §4, §5 otherwise, and §7 were not read.

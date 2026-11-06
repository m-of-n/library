---
schema: "library-summary/v1"
id: powder-description-resources
record: powder-description-resources
type: summary
updated: "2026-11-05"
---

# POWDER: Description Resources

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` (W3C Recommendation); obsolescence proposal open |
| **Authors** | Phil Archer, Kevin Smith, Andrea Perego (editors) |
| **Published** | 2009-09-01 |
| **Identifier** | REC-powder-dr-20090901 |
| **Source** | https://www.w3.org/TR/powder-dr/ |
| **Digest** | `sha256:ea32851b…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

POWDER lets anyone publish machine-readable claims about a group of web resources. A Description Resource (DR) has attribution, a scope, and descriptors. Every valid document must say who issued it (§2.1, §5), and that one requirement is presented as the inherent trust model: it is always clear whom to ask. It resolves the human-versus-machine tension with an operational XML dialect and formal semantics reached through a GRDDL transform to RDF/OWL (§1.1). Descriptors come from RDF vocabularies, and §2.6 strongly advises RDF vocabularies or OWL ontologies in preference to POWDER descriptor sets with no restriction on where they apply. `displaytext` and `displayicon` carry a summary for end users (§2.1). Trust is a human judgment, so §5 offers discoverable mechanisms, third-party certification and supporting evidence, and prescribes none.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Attribution and optional certification, with authentication left open (§5.1, §5.6) |
| Cryptography | `none` | Mentions digital signature and XML Signature as options, specifying neither (§5.2, §5.6) |
| This project | `adjacent` | The closest thing to DEC-007 option 4, built on RDF, plus an uptake warning |

- **DEC-007**: this is option 4 tried in standards form. Meaning is pushed out to dereferenceable RDF terms, so a renderer needs an RDF stack, and a vocabulary's words are not fixed by the issuer. §5.5 relies on terms being defined by IRI. Publishers are strongly advised to use one `displaytext` per DR, apart from `xml:lang` variants (§2.1, §2.8.4), so the human rendering is attached to the description and not to each value. That is close to option 3. **DEC-007** is proposed, not accepted: it exists only in ARCH-0001-PROPOSAL v0.2.0 §5, and mofn's DECISIONS-0001 item 5d asks whether it survives at all.
- **R-M-12** (proposed text; relocated to ARCH-0002 P1 and accepted by ADR-0001): attribution via `issuedby` names an IRI describing an entity, not a key. §5.4 goes further: trust can equal the trustworthiness of the host. That is the model R-M-12 rejects.

## Relations

- `see_also: pics-1-1-services`: W3C retired PICS as superseded by POWDER (`w3-org-pics`); this is the PICS successor for describing content. Authored only here; `pics-1-1-services` no longer repeats it.
- `see_also: w3c-tag-obsolete-powder`: the TAG proposal to obsolete this Recommendation (w3c/transitions issue 86, in `content.note`). That record does not author an edge back, so it is authored here.
- `see_also: c2pa-2-4`: both attach attributed, machine-readable claims to content. POWDER pushes meaning out to RDF vocabularies (§2.6, §5.5); C2PA keeps label meaning in its specification (§6.2.2 there). Those are the two ends DEC-007 weighs. Authored only here; `c2pa-2-4` no longer repeats it.
- `pics-1-1-labels`, `pics-dsig-1-0` and `w3-org-pics` author their edges to this record, so they are not repeated here.

## Implementations

**Searched 2026-11-01**, web. No maintained library was found. W3C's primer lists a validator and Perl and PHP processors, and W3C's wiki has a PHP processor page marked as under development, last edited December 2009. Their licences and status were not checked, so none is listed as usable.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. No issue owns the eventual extraction of this record yet.

## Limits

- **It shows nothing about uptake.** That POWDER saw little use is a claim from mofn's report §6.2 and `w3c-tag-obsolete-powder`, not this document.
- **Mutable claims.** §5.4 says the document stays under the reviewer's control and may change or disappear, subject to a valid-until date. There is no content addressing.
- **One of a set.** Grouping of Resources and Formal Semantics are normative companions and are not held here.
- **Errata exist** and may include normative corrections, per the document; they were not read.
- **Read scope.** By section: Abstract, §1, §1.1, part of §2.1, the start of §2.6, the start of §2.8.4, §5 intro, §5.1, the start of §5.2, §5.4, §5.5 (start) and §5.6, plus the table of contents. §2.2 to §2.5, §2.7, §3, §4, §5.3 and the appendices were not read.

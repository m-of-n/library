---
schema: "library-summary/v1"
id: pics-1-1-services
record: pics-1-1-services
type: summary
updated: "2026-11-01"
---

# PICS 1.1 Rating Services and Rating Systems and Their Machine Readable Descriptions

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `historic`: W3C Recommendation, retired 2009-11-24 |
| **Authors** | Jim Miller (editor), Paul Resnick, David Singer |
| **Published** | 1996-10-31 |
| **Identifier** | REC-PICS-services-961031 |
| **Source** | https://www.w3.org/TR/REC-PICS-services-961031 |
| **Digest** | `sha256:504318e3…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

PICS separates a rating system (dimensions, scales, criteria) from a rating service (who applies them), and defines `application/pics-service`, a machine-readable document describing both. Software reads this description to interpret labels and build its interface, so that one UI does not have to fit every service (*What is a rating service?*). Each category has a language-independent transmission name, plus optional names, descriptions and icons; a value can carry a name, description and icon. Constraints cover min, max, integer, label-only, multivalue and unordered, and `unordered` is expressly a hint to UI designers (*Explanation of Sample Rating Service*). A label therefore carries only values, and a client resolves meaning from a separate document.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `none` | Filtering by labels; this document has no integrity or authentication mechanism |
| Cryptography | `none` | None; signing is `pics-dsig-1-0` |
| This project | `core` | The separation mofn's DEC-007 proposes to generalise |

- **DEC-007**: this is the mechanism option 2 cites, and it checks out against the text: categories, permitted values, scales and per-value words are all declared outside the label. Two details matter. The stated purpose is to generate a *configuration* UI for selection software, not to render a statement to a reader. And the document says an incompatible change should be made by creating a new service URL (*What is a rating service?*), a versioning rule DEC-007 could reuse. **DEC-007** is proposed, not accepted: it exists only in ARCH-0001-PROPOSAL v0.2.0 §5, and mofn's DECISIONS-0001 item 5d asks whether it survives at all.
- **R-M-12** (proposed text; relocated to ARCH-0002 P1 and accepted by ADR-0001): identity is a URL. Uniqueness comes from URL validity and meaning from whatever that URL serves, so there is no signature or digest in the description. That is exactly what a key-relative form replaces.

## Implementations

**Searched 2026-11-01**, web. No current implementation was found. W3C's own 1990s reference code came up: a Java library with a parser usable alone (https://www.w3.org/PICS/refcode/Parser) and an older C library. Neither was tested, and their licences were not checked.

| Name | Kind | License | URL |
|---|---|---|---|
| W3C PICS parser | open source, Java, historical | not checked | https://www.w3.org/PICS/refcode/Parser |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. No issue owns the eventual extraction of this record yet.

## Limits

- **Nothing binds a label to the description it was read against.** A label names a service URL; the description is fetched and cached, and no digest ties them. A changed description silently changes what old labels mean, which the new-URL rule only asks authors to avoid.
- **Discovery is unspecified.** The document says it does not state how a description is first located.
- **Ordinal scales are numeric.** Meaning sits on a number line, and fractions are the stated fix for inserting a value. DEC-007 need not inherit that.
- **One language per file.** Multiple languages are left to separate documents and negotiation; transmission names stay fixed.
- **The examples rate adult and violent content,** which is the domain that drew the censorship objections. This document does not discuss them; `pics-censorship-faq` is the record for that.
- **Read scope.** The whole document, including all three appendices, as extracted text.

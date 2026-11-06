---
schema: "library-summary/v1"
id: iso-iec-5962-2021
record: iso-iec-5962-2021
type: summary
updated: "2026-11-03"
---

# Information technology — SPDX Specification V2.2.1

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` — published ISO/IEC international standard |
| **Authors** | ISO/IEC JTC 1/SC 7 |
| **Published** | 2021-08 |
| **Identifier** | ISO/IEC 5962:2021 (carries SPDX 2.2.1) |
| **Source** | https://www.iso.org/standard/81870.html |
| **Digest** | none — the ISO text was not fetched; see the note at the end |
| **Read instead** | SPDX 2.2.1 source, https://github.com/spdx/spdx-spec/tree/v2.2.1-ISO-final, commit `96e7beab922a3afe2d2b334da2d999d9890fa36d` (CC-BY-3.0) |

## Overview

**The ISO text was not read.** The note at the end says why: the blocker is ISO's licence, not the price. What follows comes from the SPDX 2.2.1 source that the SPDX project tagged `v2.2.1-ISO-final` and publishes under CC-BY-3.0. Clause numbers below are that text's; that they match the ISO PDF is likely but not verified.

SPDX 2.2.1 defines *"a standard data format for communicating the component and metadata information associated with software packages"* (Clause 1). A document describes packages, files and snippets in sections for creation information, packages, files, snippets, other licensing information, relationships and annotations (Clauses 6–12). It can be serialised as tag:value, RDF/XML, JSON, YAML or spreadsheet, and Clause 4.4 says SPDX defines how to translate a valid document *"without loss to each other supported format"*. The Foreword says the Joint Development Foundation prepared it and JTC 1 adopted it under the PAS procedure; the differences annex (headed I.1 in the source) says V2.2.1 has *"no technical differences"* from V2.2 and is V2.2 reformatted for ISO. It is the only SBOM format with ISO ratification, and `spdx-3-0-1` supersedes it as the current SPDX line.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | An SBOM format: supply-chain transparency, not a security mechanism. Clause 5.3 excludes how a recipient uses the data |
| Cryptography | `adjacent` | Digests only: file checksums require SHA-1 (8.4, Table 39), package checksums allow MD2–MD6 and SHA-1/SHA-2 (7.10, Table 22). No signatures |
| This project | `adjacent` | One of the two SBOM syntaxes R-I-07 names; mofn would use 3.0.1 for new work |

**Bears on:**

- **R-I-07** (C): *"Emit SPDX or CycloneDX inside an `ArtifactStatement` predicate"*. This is the ISO edition of SPDX, so it is one of the formats that requirement names.
- **R-M-07** (M): artifact statements bind at least one content digest. SPDX 2.2.1 carries its own digests, but the one it requires per file is SHA-1 (8.4) and the package verification code is a 160-bit value (7.9). An SPDX 2.2.1 predicate's checksums therefore cannot be what satisfies R-M-07 for us; the statement must bind its own digest.

`R-M-11` was removed from `bears_on`: it is proposed in ARCH-0001-PROPOSAL-v0.2.0 and is not in ARCH-0001 §5.

## Implementations

Searched 2026-11-03, briefly. SPDX 2.x tooling (for example the `spdx/tools-java` and `spdx/tools-python` libraries) is tracked on `spdx-3-0-1`, the SPDX record we work from; it targets the SPDX text, not the ISO edition, so none is listed here.

| Name | Kind | License | URL |
|---|---|---|---|
| _see `spdx-3-0-1`_ | | | |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; `content.note` says what was read instead of the ISO text |
| `summary.md` | this document |

**No digest and no `distilled/`.** The ISO PDF was not fetched, and the SPDX source is a different artifact, so hashing it would misattribute the digest (see the comment in `record.yaml`). No FX-1 extraction: this PR summarises and does not extract, and an extraction of the ISO text would first need the licence question below settled. `spdx-3-0-1` carries the `supersedes` edge to this record.

## Limits

- **ISO text unread.** Everything above is from the SPDX 2.2.1 source. ISO may have edited it, and the clause numbers are unverified against the PDF.
- **The source contradicts itself on annex letters.** Clause 4.1 sends the reader to Annex J for differences from earlier editions. The annex file itself is headed "Annex I", and both the SPDX Lite annex and the CC-BY-3.0 annex are headed "Annex G". Table I.1 maps SPDX Lite to Annex G and leaves the licence annex out (`[omitted]`). Which letters the ISO edition uses cannot be inferred from this source, so this summary cites only clause numbers, which are consistent.
- **A required field with optional cardinality.** Table 21 marks the package verification code `Required: Yes` but gives cardinality `0..1` when `FilesAnalyzed` (7.8) is `true` or omitted, and `0..0` when it is `false`. The source does not say when a value may be absent with `FilesAnalyzed` true.
- **Weak digests.** SHA-1 is the mandatory file checksum and MD5 is permitted. That is a property of SPDX 2.2.1, not a defect in this record, and a reason to prefer 3.0.1.

## Note — why this record is unread (2026-11-01)

The ISO text was not read, so `status` stays `queued`. The sections above were
written on 2026-11-03 from the SPDX 2.2.1 source instead, labelled as such.

The September record called this paywalled. That is wrong. Internet Archive captures
were used because iso.org refuses scripted clients: the catalogue page captured
2026-10-23 lists the PDF at CHF 0, 145 pages, edition 1, stage 90.92 (to be revised)
since 2026-01-07. `standards.iso.org/ittf/PubliclyAvailableStandards/` now says that
site is closed and points to the ISO and IEC webstores, at no charge. Its old `.zip`
path only returns a licence page, and returned the same page for a made-up filename,
so that page proves nothing about this document.

The blocker is the licence, not the price. The download requires accepting the ISO
Customer Licence Agreement. In the capture of 2026-10-23, clause 7(b) bars access or
processing "for or related to any machine learning, artificial intelligence (AI), or
analogous computational purposes" without a separate licence, and names summarising.
The licence was not accepted and the text was not fetched. Whether to obtain it is a
human decision, as is how to read it if so.

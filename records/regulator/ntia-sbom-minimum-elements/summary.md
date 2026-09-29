---
schema: "library-summary/v1"
id: ntia-sbom-minimum-elements
record: ntia-sbom-minimum-elements
type: summary
updated: "2026-09-27"
---

# The Minimum Elements For a Software Bill of Materials (SBOM)

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `best-practice` — a Department of Commerce report issued under EO 14028 §4(f). It sets a floor for federal procurement, and says in §III that it creates no new federal requirement |
| **Authors** | National Telecommunications and Information Administration |
| **Published** | 2021-07-12 |
| **Identifier** | EO 14028 §4(f) · US Dept. of Commerce |
| **Source** | https://www.ntia.gov/sites/default/files/publications/sbom_minimum_elements_report_0.pdf |
| **Digest** | `sha256:b0fbbe5e3c5773977df1f402eceb845c4d5715a02cde4d967e54aef51856b716` |

## Overview

Defines the floor for what an SBOM must contain, in three interlocking parts:
**data fields**, **automation support**, and **practices and processes**. The
seven minimum data fields are Supplier Name, Component Name, Version of the
Component, Other Unique Identifiers, Dependency Relationship, Author of SBOM
Data, and Timestamp (§IV). Automation support names three acceptable formats —
SPDX, CycloneDX, and SWID tags — and requires that an SBOM crossing an
organisational boundary be conveyed in one of them.

**The decisive fact for this library is what the minimum does not include.** A
cryptographic hash of the component is *not* a minimum field. It appears in §V,
"Beyond Minimum Elements", among the *recommended* fields, where the report
argues its own case against itself: "A hash is a key foundation for using SBOM
to have trust in the software supply chain." Component identity at the minimum
tier is therefore carried entirely by **names and namespace identifiers** —
supplier string, component string, version string, and optionally CPE, SWID or
PURL — none of which binds to bytes.

The report is equally explicit that **"Author of SBOM Data" is not the author of
the software**: it is "just the source of the descriptive data", and may be the
supplier, an upstream supplier, or a third-party analysis tool. Two of the three
practice elements then limit what any SBOM asserts at all. **Known Unknowns**
requires that "the default interpretation of the data should be that the data is
incomplete", with completeness affirmatively stated when it holds.
**Accommodation of Mistakes** asks consumers to be "explicitly tolerant of the
occasional incidental error."

§V's "SBOM Integrity and Authenticity" treats signing as desirable and
unspecified: suppliers "are encouraged to explore options to both sign SBOMs and
verify tamper-detection", with no mechanism, envelope or key-binding named.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Sets the floor that every downstream SBOM mandate inherits, including what that floor omits |
| Cryptography | `adjacent` | Names hashes and signatures as valuable; specifies neither algorithm, encoding, nor binding |
| This project | `adjacent` | Evidence about a gap, not a mechanism we conform to |

`bears_on: R-M-07` — R-M-07 requires at least one content digest. This document
is the evidence that the federal SBOM floor **does not**, which makes the
requirement a real constraint rather than a restatement of common practice.

`bears_on: R-M-11` — R-M-11's `ArtifactId` admits a structured description of an
artifact's composition as one identification mode. The seven minimum fields are
precisely that mode at its weakest: a name-and-version description with no
digest, authored by a party that may be neither the producer nor the supplier.

`see_also: sp-800-161r1` — not a generic relation. SP 800-161r1 is the
enterprise C-SCRM process that *consumes* SBOM data and supplies the
institutional vocabulary this report writes into procurement; it is also the
record whose orphaning opened this topic. Neither document specifies a
mechanism, and reading either as though it does is the mistake both invite.

## Implementations

Not searched. This is a policy report, not a specification with implementations
— the implementations belong to the format records (`spdx-3-0-1`,
`cyclonedx-1-7`), where `implementations.searched` is still empty.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled/`. We conform to no clause here; §5.1 of `docs/requirements.md`
is the test, and this fails it. The requirements worth extracting in this topic
are CISA's maturity levels, not these.

## Limits

- **It defines a floor, not a proof.** Every field is a *description* supplied
  by an author who may have no relationship to the software. Nothing in the
  minimum elements makes an SBOM checkable against the artifact it describes.
- **No digest at the minimum tier.** Component identity rests on strings the
  report itself concedes are unstable — §IV notes that "corporate mergers and
  open source forking will make ubiquitous and permanent solutions on this basis
  unlikely."
- **Signing is gestured at, not specified.** §V asks for signatures and names no
  envelope, algorithm or key-binding. It also asks that a mechanism "allow the
  signing of each component" — a per-component signing model that no minimum
  field supports, since components carry no digest to sign over.
- **Superseded in practice on the hash question.** CISA's 2024 third edition
  moves the cryptographic hash to *Minimum Expected*. Citing this report in 2026
  as the current statement of the SBOM floor would be wrong; see
  `cisa-framing-software-component-transparency`.
- **It is US federal procurement policy.** §III disclaims creating new federal
  requirements and excludes hardware and regulatory questions from scope. It
  carries no weight as a technical specification.

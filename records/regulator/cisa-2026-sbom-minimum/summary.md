---
schema: "library-summary/v1"
id: cisa-2026-sbom-minimum
record: cisa-2026-sbom-minimum
type: summary
updated: "2026-11-04"
---

# 2026 Minimum Elements for a Software Bill of Materials (SBOM)

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | best-practice |
| **Authors** | Cybersecurity and Infrastructure Security Agency, NSA, FBI, and fifteen international co-authoring organizations named in the document |
| **Published** | 2026-07-29, Cybersecurity and Infrastructure Security Agency (CISA) |
| **Identifier** | https://www.cisa.gov/resources-tools/resources/2026-minimum-elements-software-bill-materials-sbom |
| **Source** | https://www.cisa.gov/sites/default/files/2026-07/2026_cisa_sbom_minimum_elements_508c.pdf |
| **Digest** | `sha256:b42046c4…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

A joint update of the 2021 NTIA baseline, led by CISA with NSA, the FBI and fifteen international partners. It says tooling has moved far enough that recipients can demand more. New data fields include SBOM Author Signature, Component Hash Value and Algorithm, Component License, Generation Context, and format and tool identity. Practices tighten too: Coverage replaces Depth and includes transitive dependencies with no minimum depth, and an SBOM author should state explicitly whether missing information is unknown or withheld (*Explicitly Identifying Unknown Information*). SWID drops out of the named formats, leaving SPDX and CycloneDX. The document creates no new requirements, by its own statement in *Scope*.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Hash and author signature make an SBOM checkable. Accuracy and completeness remain open (*Validation*) |
| Cryptography | `adjacent` | Names approved-algorithm expectations for hashes and signatures, nothing more |
| This project | `adjacent` | R-I-07 means carrying a format that must meet this list, not defining one |

- **R-I-07**: we emit SPDX or CycloneDX inside an `ArtifactStatement`. This is the baseline those documents get measured against.
- **R-M-07**: Component Hash Value is now minimum data. It is defined over the executable component artifact, and is reported as unknown if the author lacks that artifact.
- **R-M-11**: Component Identifiers is a separate element from Component Hash Value. It asks for common identifiers such as CPE and PURL, and also allows UUIDs, commit hashes and intrinsic identifiers (OmniBOR, SWHID). That is close to our locator and digest split, but not clean, since intrinsic identifiers are themselves content-derived. CISA defines identifiers as "used to identify a component or serve as a look-up key", which does not take R-M-11's position that a locator is non-authoritative evidence. R-M-11 is proposed text (ARCH-0001-PROPOSAL-v0.2.0).
- *SBOM Author Signature* asks for a signature, but not for a mechanism. *Validation* says to use existing software signing infrastructure.

## Implementations

**Searched 2026-11-01.** The two formats the document names, plus common generators, checked against GitHub. Conformance to these elements was not tested.

| Name | Kind | License | URL |
|---|---|---|---|
| syft | open source, generator | Apache-2.0 | https://github.com/anchore/syft |
| trivy | open source, scanner and generator | Apache-2.0 | https://github.com/aquasecurity/trivy |
| spdx/tools-python | open source, library | Apache-2.0 | https://github.com/spdx/tools-python |
| cyclonedx-cli | open source, CLI | Apache-2.0 | https://github.com/CycloneDX/cyclonedx-cli |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

**Relations.** `supersedes: ntia-sbom-minimum-elements`, on the document's own statement that it "updates and replaces" the NTIA report (Introduction, p. 4). No `see_also`. The CRA, CycloneDX (ECMA-424) and ISO/IEC 5962:2021 are cited, so they sit under `cites`. `omb-m-26-05` and `eu-cra-2024-2847` author their own edges to this record. SPDX 3.0.1 is not linked: the document cites spdx.dev and ISO/IEC 5962:2021, which is SPDX 2.2.1.

## Limits

- **A signature is not accuracy.** *Validation* separates integrity from accuracy, coverage and completeness, and leaves the latter open.
- **Author identity is a string.** SBOM Author is a name. SBOM Author Signature is defined only as "attributable to the SBOM author", with no link defined between the name and the signing key.
- **The Coverage test is strong, and not easily met.** The recipient should be able to conclude a vulnerability does not affect them from absence. That holds only for a complete SBOM, which nothing here verifies.
- **AI and SaaS are deferred** to *Discussion* and the separate G7 guidance, which is not held here.
- **Duplicate noted.** `ntia-2021-sbom-minimum` is a stub pointer to `ntia-sbom-minimum-elements`. The comment in that target's `record.yaml` that the 2021 report "has not been withdrawn" was written at the September 2026 SBOM-lane ingest (library#25, committed 2026-09-28), after this document was published, but it addresses only the 2024 CISA framing. It does not account for this document's statement (Introduction, p. 4) that it "updates and replaces" the NTIA report.
- **Read scope.** All 23 pages read through text extraction, including Appendix A, the References list and all of Appendix B, plus the PDF's link annotations (source check 2026-11-04, same bytes as the recorded digest). The resource page was read at ingest. The CISA site refused a direct fetch on 2026-11-04 (see `content.note`).

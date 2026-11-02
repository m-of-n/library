---
schema: "library-summary/v1"
id: cisa-2026-sbom-minimum
record: cisa-2026-sbom-minimum
type: summary
updated: "2026-11-01"
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

A joint update of the 2021 NTIA baseline, led by CISA with NSA, the FBI and fifteen international partners. It says tooling has moved far enough that recipients can demand more. New data fields include SBOM Author Signature, Component Hash Value and Algorithm, Component License, Generation Context, and format and tool identity. Practices tighten too: Coverage replaces Depth and includes transitive dependencies with no minimum depth, and unknown data must be distinguished from data withheld. SWID drops out of the named formats, leaving SPDX and CycloneDX. The document creates no new requirements, by its own statement in *Scope*.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Hash and author signature make an SBOM checkable. Accuracy and completeness remain open (*Validation*) |
| Cryptography | `adjacent` | Names approved-algorithm expectations for hashes and signatures, nothing more |
| This project | `adjacent` | R-I-07 means carrying a format that must meet this list, not defining one |

- **R-I-07**: we emit SPDX or CycloneDX inside an `ArtifactStatement`. This is the baseline those documents get measured against.
- **R-M-07**: Component Hash Value is now minimum data. It is defined over the executable component artifact, and is reported as unknown if the author lacks that artifact.
- **R-M-11**: Component Identifiers keeps lookup identifiers (CPE, PURL, SWHID, OmniBOR) separate from the hash. That matches our locator and digest split in spirit. CISA treats a PURL as a look-up key, not as non-authoritative evidence, and R-M-11 is proposed text.
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

## Limits

- **A signature is not accuracy.** *Validation* separates integrity from accuracy, coverage and completeness, and leaves the latter open.
- **Author identity is a string.** SBOM Author is a name. The signature is required to be attributable, with no link defined between the two.
- **The Coverage test is strong, and not easily met.** The recipient should be able to conclude a vulnerability does not affect them from absence. That holds only for a complete SBOM, which nothing here verifies.
- **AI and SaaS are deferred** to *Discussion* and the separate G7 guidance, which is not held here.
- **Duplicate noted.** `ntia-2021-sbom-minimum` is a stub pointer to `ntia-sbom-minimum-elements`. The note in that target's `record.yaml` that the 2021 report has not been replaced predates this document.
- **Read scope.** Pages 1 to 15 and 20 to 22 of 23 were read through text extraction, plus the resource page. Appendix A, the reference list and the tail of Appendix B were not read closely.

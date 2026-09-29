---
schema: "library-summary/v1"
id: cisa-framing-software-component-transparency
record: cisa-framing-software-component-transparency
type: summary
updated: "2026-09-27"
---

# Framing Software Component Transparency: Establishing a Common Software Bill of Materials (SBOM)

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `best-practice` — working-group guidance hosted by CISA. It frames and clarifies; it confers no conformance claim and carries no procurement mandate of its own |
| **Authors** | CISA SBOM Tooling and Implementation Working Group |
| **Published** | 2024-09-03 (released October 2024) — Third Edition |
| **Identifier** | CISA, Third Edition |
| **Source** | https://www.cisa.gov/sites/default/files/2024-10/SBOM%20Framing%20Software%20Component%20Transparency%202024.pdf |
| **Digest** | `sha256:3a204b5f6f988b5f32e635132feabc885789efc436d0756294d388f148cb3397` |

## Overview

The third edition of the framing document that NTIA's 2021 minimum elements
were drawn from. It restates the SBOM baseline as **twelve Baseline
Attributes** — four of SBOM meta-information (Author Name, Timestamp, Type,
Primary Component) and eight per component — and grades each one across three
**data maturity levels**: *Minimum Expected*, *Recommended Practice*,
*Aspirational Goal*. That grading is the structural change: where NTIA gave a
flat list, this gives each attribute a floor and a direction.

**The consequential move is §2.2.2.5.** Cryptographic Hash becomes a *Minimum
Expected* component attribute — "provide a hash for any Component listed in the
SBOM for which the hash was provided or sufficient information is available to
generate the hash. If sufficient information is not available, indicate as
unknown." It requires the algorithm and the hashed object alongside the value
"to enable reproducibility", accepts MD5/SHA1/SHA2 at the minimum tier while
noting MD5 and SHA1 "will be formally discontinued in 2030", and requires SHA-2
(SHA-256 or higher) at *Recommended Practice*. §2.2.2.4 goes further and says
the hash "may also effectively function as a unique identifier", listing
content-derived identifiers — SWHID, OmniBOR artifact IDs — alongside CPE, PURL
and SWID.

**§2.2.2.6.4 is the part that constrains what an SBOM can assert.** Relationship
completeness is a four-valued supplemental attribute — *Unknown*, *None*,
*Partial*, *Known* — whose **default is `Unknown`**, and the document names the
reason: "this default value implies the open-world ontological assumption." An
SBOM is therefore, by construction, a statement that some components are
present, never a statement that others are absent, unless completeness is
affirmatively declared — and a `Known` declaration reaches only one level, since
a component marked `Known` may have a transitive dependency marked `Partial`.

§2.4 asks for signing as a *supplemental* capability: "authors must be able to
digitally sign SBOMs and Consumers must be able to verify signatures...
requires appropriate digital signature and public key infrastructure." As in
NTIA 2021, no envelope, algorithm or key-binding is named. §2.5's Table 1 maps
every baseline attribute onto ISO/IEC 5962:2021, SPDX 3.0 and CycloneDX v1.6
(ECMA-424) — the crosswalk that makes all three format records in this topic
comparable field by field.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The current statement of what an SBOM is expected to contain, superseding NTIA 2021 on the hash question |
| Cryptography | `adjacent` | Requires hashes and names acceptable algorithm families; specifies no signing mechanism |
| This project | `core` | §2.2.2.5 and §2.2.2.6.4 bear directly on both requirements this record is filed against |

`bears_on: R-M-07` — R-M-07 requires at least one content digest. §2.2.2.5 is
the closest thing in the SBOM literature to agreement with that requirement, and
the distance that remains is exactly measurable: CISA's hash is *best-effort*
("indicate as unknown"), admits MD5 and SHA1 at its floor, and is scoped by
whatever the author chose to call a Component.

`bears_on: R-M-11` — §2.2.2.4 treats a content hash as one identifier among CPE,
PURL, SWID, SWHID and OmniBOR, which is R-M-11's `ArtifactId` question posed in
another vocabulary: when is a name enough, and when must identity be derived
from bytes?

`updates: ntia-sbom-minimum-elements` — not `supersedes`. EO 14028 §4(f) names
the NTIA report and it has not been withdrawn, so both remain current; that is
the test for `updates` in `docs/references.md` §2. In practice, the hash
requirement has moved and citing NTIA alone on that point is now wrong.

## Implementations

Not searched. Guidance rather than a format; tooling belongs to the format
records (`spdx-3-0-1`, `cyclonedx-1-7`), where `implementations.searched`
is still empty.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled/` yet. This is the record in the topic most likely to earn one:
the twelve attributes × three maturity levels are already a requirements table
in prose, and `distilled/requirements.yaml` would make them externally
referenceable. Not done here — that is the `distil` skill's job.

## Limits

- **Maturity levels are not conformance.** Nothing defines who asserts which
  level was met, or how a consumer checks it. An SBOM does not carry its own
  maturity claim, so "Minimum Expected" describes an aspiration for authors, not
  a property a verifier can test.
- **The hash floor is weak in three ways at once.** It is conditional on
  availability, it accepts MD5 and SHA1 until 2030, and its scope is whatever
  the author chose to bound as a Component — "Suppliers and Authors choose how
  to define Components, which in turn defines the scope of the hash" (§2.2.2.5).
  Two SBOMs of the same artifact can both be conformant and share no hash.
- **Signing is deferred entirely.** §2.4 states the requirement — authors sign,
  consumers verify — and specifies nothing that would make two implementations
  interoperate. Compare `in-toto-attestation-v1` and
  `secure-systems-lab-dsse`, which specify precisely this and are not
  referenced.
- **The open-world default is correct and rarely honoured.** §2.2.2.6.4 gets the
  semantics right, but it is a *supplemental, optional* attribute. An SBOM that
  omits it defaults to `Unknown` — meaning the great majority of real SBOMs
  assert nothing about completeness while being read by consumers as though they
  do.
- **Table 1 is already dated.** It maps CycloneDX v1.6 / ECMA-424 1st edition;
  the line is now at 1.7 / ECMA-424 2nd edition (`cyclonedx-1-7`).

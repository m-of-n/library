---
schema: "library-summary/v1"
id: tcg-tpm-2-0-library-184
record: tcg-tpm-2-0-library-184
type: summary
updated: "2026-11-04"
---

# TPM 2.0 Library Specification, Parts 0-3, Version 184

|  |  |
|---|---|
| **Type** | spec (TCG) |
| **Maturity** | `standard`: marked TCG Published. Superseded by v185 |
| **Authors** | Trusted Computing Group, individual contributors not recorded here |
| **Published** | 2025-03-20 |
| **Identifier** | TPM 2.0 Library, Version 184, Parts 0 to 3 |
| **Source** | https://www.trustedcomputinggroup.org/resources/documents/tpm-library-specification |
| **Digest** | `sha256:822aa80f…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Part 0 sets out the trust model. The TPM holds Roots of Trust for Storage and Reporting, and the RTR's identity is a set of Endorsement Keys from one seed (§4.4.4.2). Attestation is a hierarchy of six types, in which external parties vouch for the TPM and the platform, an Attestation CA or the TPM itself then vouches for keys, the TPM quotes measurements, and a third party vouches for the software measured (§4.5.3.1). That reporting depends on a binding the TPM cannot prove alone, which a Platform Certificate supplies (§4.4.4.3). V184 deprecates TDES and SHA-1 (§3.1.1), and TPM2_CreateLoaded, TPM2_CertifyX509 and the AC commands (§3.1.2). It is the last version before `tcg-tpm-2-0-library-185`.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The defining account of a hardware root's trust structure |
| Cryptography | `adjacent` | Algorithm-agile. Adds no primitive here |
| This project | `adjacent` | Direct bearing on what a device-held key can claim |

- **R-M-02**: §4.4.4.4 says that unless an EK is certified by a trusted entity, its trust and privacy properties are no different from a key generated in software. That is this topic's answer from the source: a hardware root adds nothing a verifier can see until a third party vouches for it.
- **R-I-02**: the vouching parties in §4.5.3.1 are external authorities. Importing such evidence must not make them native roots.

**Relations.** `see_also: brickell-2004-daa`: the DAA paper is the answer to the Attestation CA's ability to correlate, the privacy problem this model leaves open (see Limits). The successor `tcg-tpm-2-0-library-185` is not authored here: `superseded_by` is derived. `tcg-tpm-1-2-main`, `tcg-tpm2-keys-device-identity` and `iso-iec-11889-2015` each author the symmetric `see_also` to this record, so it is not repeated.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Identity does not bind to a platform by itself** (§4.4.4.3).
- **The Attestation CA can correlate** in the privacy-preserving scheme, an issue covered by `brickell-2004-daa`. Privacy here is a matter of the EK's restricted use (§4.4.4.4).
- **Superseded.** Algorithms and commands changed in v185. The record is pinned to v184 because its id is.
- **Read scope.** Part 0 §1 headings, §3.1, §4.4 and §4.5.3 were read, re-checked 2026-11-04 against the same bytes (all five digests match). In Part 3, TPM2_Quote's general description was read. Part 1 and Part 2 were not read beyond their contents. Errata v1 was read by title of each entry. Text extracted from Parts 1 to 3 has lost word spacing. The change history §2 was not read past the opening.

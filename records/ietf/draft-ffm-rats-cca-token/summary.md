---
schema: "library-summary/v1"
id: draft-ffm-rats-cca-token
record: draft-ffm-rats-cca-token
type: summary
updated: "2026-11-01"
---

# Arm's Confidential Compute Architecture Reference Attestation Token

|  |  |
|---|---|
| **Type** | draft (individual submission, intended Informational) |
| **Maturity** | `draft`: not adopted. §1 calls it a vendor extension and not a standard |
| **Authors** | S. Frost, T. Fossati, G. Mandyam |
| **Published** | 2026-09-07 |
| **Identifier** | draft-ffm-rats-cca-token-04 |
| **Source** | https://www.ietf.org/archive/id/draft-ffm-rats-cca-token-04.txt |
| **Digest** | `sha256:5cba6143…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

This draft specifies the CCA attestation token as an EAT profile, in two attester models, direct and delegated (§3). Both are layered attesters with exactly two layers: the HES hardware root attests the platform, and the RMM attests the Realm (§3). The two claim sets are bound together (§4.10), and verifying the platform signature is what establishes trust in the Realm key (§7). The verifier's key comes from an authorized Endorser, or from an X.509 chain if the implementation certifies its platform key (§6, §7).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A concrete account of what a hardware root signs and how a verifier decides |
| Cryptography | `adjacent` | COSE_Sign1 profile. Algorithm choice is left open (§4.11.1) |
| This project | `adjacent` | Live evidence on CBOR profile divergence |

- **R-O-03 and DEC-002**: §4.11.1 says the reference profile is designed not to emit preferred serializations, and assumes a variation-tolerant CBOR decoder at the Verifier. `rfc-9711` §6.4 requires preferred serialization for its constrained profile. These are different profiles, so this is a divergence and not a contradiction, but a signed attestation token in production has no deterministic bytes to rely on.
- **R-I-02**: §7 has the verification key supplied by an Endorser, so the verifier chooses that trust relationship. It is not implied by the token.

## Implementations

**Not surveyed.** Licenses were read from each repository on 2026-11-01. No wider search was run.

| Name | Kind | License | URL |
|---|---|---|---|
| Trusted Firmware RMM | open source, named in §8 | BSD-3-Clause | https://github.com/TF-RMM/tf-RMM |
| Veraison | open source, named in §8 | Apache-2.0 | https://github.com/veraison/veraison |

veraison/veraison is archived on GitHub; current code location not checked.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `draft` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Not a standard**, by its own statement (§1).
- **Algorithms are unconstrained** (§4.11.1), so a verifier's policy decides.
- **A debug-state token may be only a contraindication, not a failure** (§7). Lifecycle handling is policy.
- **Tracking.** §9 notes tokens may single out a device, and requires deployments with privacy needs to act themselves.
- **Read scope.** §1, §3 opening, §4.11, §6, §7 and §8, §9 were read. Individual claim definitions in §4 and the CDDL in §5 were not read. Bindings in §4.10 were not read past their use in §7.

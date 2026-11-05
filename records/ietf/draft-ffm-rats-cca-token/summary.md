---
schema: "library-summary/v1"
id: draft-ffm-rats-cca-token
record: draft-ffm-rats-cca-token
type: summary
updated: "2026-11-04"
---

# Arm's Confidential Compute Architecture Reference Attestation Token

|  |  |
|---|---|
| **Type** | draft (individual Internet-Draft, intended Informational per its header) |
| **Maturity** | `draft`: an Active individual I-D per the datatracker. The abstract and §1 say it is not a standard |
| **Authors** | S. Frost, T. Fossati, G. Mandyam |
| **Published** | 2026-09-07 |
| **Identifier** | draft-ffm-rats-cca-token-04 |
| **Source** | https://www.ietf.org/archive/id/draft-ffm-rats-cca-token-04.txt |
| **Digest** | `sha256:5cba6143…` (full value in `record.yaml`), fetched 2026-11-01, re-checked 2026-11-04 |

## Overview

This draft specifies the CCA attestation token as an EAT profile, in two attester models, direct and delegated (§3). Both are layered attesters with exactly two layers: the HES hardware root attests the platform, and the RMM attests the Realm (§3). The two claim sets are bound by the platform token's nonce, which carries a hash of the Realm public key (delegated) or of the Realm claim set (direct) (§4.10). Primary trust comes from the platform token's signature, and checking the binding then establishes trust in the Realm key (§7). The verification key comes from an authorized Endorser, or from an X.509 chain to a trusted CA root if the implementation certifies its platform key (§6, §7).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A concrete account of what a hardware root signs and how a verifier decides |
| Cryptography | `adjacent` | COSE_Sign1 profile. The baseline imposes no strong algorithm requirement (§4.11.1) |
| This project | `adjacent` | Live evidence on CBOR profile divergence |

- **R-O-03 and DEC-002**: §4.11.1 says the reference profile is designed not to emit CBOR preferred serializations, and that the Verifier MUST be a variation-tolerant CBOR decoder; its Table 2 lists variant serialization as MAY. `rfc-9711` §6.4 makes preferred serialization a MUST for its Constrained Device Standard Profile. These are different profiles, so this is a divergence and not a contradiction, but it shows a deployed signed-CBOR profile whose bytes a verifier cannot expect to be in any canonical form. A CBOR choice under DEC-002 has to cite its own canonicalization rather than assume the ecosystem provides one.
- **R-I-02**: §7 has the verification key supplied to the Verifier by an authorized Endorser, or validated through an X.509 chain to a CA root the Verifier trusts. Either way the anchor is the Verifier's configuration, not something the token brings with it, which is the posture R-I-02 asks an importer to keep.

## Implementations

§8 names two, and both references were followed on 2026-11-04. Licences from GitHub. No wider search was run.

| Name | Kind | License | URL |
|---|---|---|---|
| Trusted Firmware-RMM | open source, [TF-RMM] in §8, attester side | BSD-3-Clause | https://github.com/TF-RMM/tf-rmm |
| Veraison ccatoken | open source, [Veraison] in §8, token library | Apache-2.0 | https://github.com/veraison/ccatoken |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites`, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**`cites`** lists the held records among §11's references: [CCA-ARCH] is `arm-cca-den0125` (the same issue 400), [EAT] is draft-ietf-rats-eat-31, the version published as `rfc-9711`, [RATS-CoRIM] is draft-ietf-rats-corim-11 of the line `draft-ietf-rats-corim` tracks, [COSE-X509] is `rfc-9360`, [STD94] is `rfc-8949`, [STD96] is `rfc-9052`, plus `rfc-8392`, `rfc-8610` and `rfc-9334`. References the library does not hold are not listed. **No `see_also`.** Every earlier edge pointed at something the draft already cites.

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `draft` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Not a standard**, by its own statement (abstract, §1). The abstract calls it an independent submission, but the datatracker shows no stream for it.
- **Algorithms are not constrained.** §4.11.1 imposes no strong requirement and RECOMMENDs [COSE-ALGS], but in -04 that reference reads "*** BROKEN REFERENCE ***" (§11.1), so the recommendation has no target. A verifier's policy decides.
- **Source defects in -04.** §4.3.3.6 and §4.3.3.9 carry the same profile heading, `tag:arm.com,2026:cca_platform#2.0.0;HESRAK`. §4.10 expands RAK as "Realm Attestation Token" where §3.2 has Realm Attestation Key. §4.11.1 says the CCA Platform claims-set is never carried in a Detached EAT bundle, while Table 2 says "The CCA Claims set SHOULD not be carried in a Detached EAT bundle", weaker and about a differently named set. §3.1, §3.2, §7.1 and §7.2 carry TODOs, and §7.2 still speaks of PSA claims.
- **Some lifecycle states may be a contraindication, not a failure** (§7). Two non-secured states, a debug state and a recoverable state, may be reported that way at the verifier's choice. Lifecycle handling is policy.
- **Tracking.** §9 notes tokens may single out a device, and says deployments with privacy requirements must take measures so the token is only used to provision anonymous or pseudonym keys.
- **Read scope.** Abstract, §1, §3 to §3.2, §4.3.3, §4.10, §4.11, §6 to §9 and §11 were read, against the archive text. Individual claim definitions in §4, the CDDL in §5, §10 and the Appendix A examples were not.

---
schema: "library-summary/v1"
id: in-toto-envelope-v1
record: in-toto-envelope-v1
type: summary
updated: "2026-11-03"
---

# in-toto Attestation Framework: Envelope layer specification

|  |  |
|---|---|
| **Type** | spec (one file of the in-toto Attestation Framework v1, `spec/v1/envelope.md`) |
| **Maturity** | _unset._ A CNCF-project specification with no ratification step that maps to RFC 2026; same judgement as `in-toto-attestation-v1` |
| **Authors** | No byline. in-toto Attestation Framework maintainers; the last change (#431) was the ITE-5 alignment commit |
| **Published** | 2026-03-11 (last commit touching the file, `7bfb269`); framework version v1.2 |
| **Identifier** | `in-toto/attestation` main @ `50bf01716982189898823e90586075f37cd9bb7d`; identical bytes at tag `v1.2.0` (`df02077`) |
| **Source** | https://raw.githubusercontent.com/in-toto/attestation/50bf01716982189898823e90586075f37cd9bb7d/spec/v1/envelope.md |
| **Digest** | `sha256:c02c6588…` (full value in `record.yaml`), fetched 2026-11-03. It matches the per-file digest `in-toto-attestation-v1` recorded at v1.2.0 |

## Overview

The envelope is the outermost of in-toto's three layers. It does serialization and authentication, and it deliberately specifies almost nothing itself. §Schema makes DSSE v1.0 the RECOMMENDED format. Any other envelope is acceptable if it meets the six-item ITE-5 list: multiple signatures (the only MUST), an authenticated payload type, no dependence on canonicalization, a key hint, no parsing of the payload before verification, and no requirement to carry the signing key's algorithm in the signature. §Alternative Envelope schemas applies that list. `COSE_Sign` passes. `COSE_Sign1` and the Sigstore Bundle fail, because each allows only one signer. §Fields and §Storage convention then pin the in-toto-specific parts: a `payloadType` media type, a base64 JSON Statement as `payload`, a `.json` file-naming convention, and a `+dsse` storage media type. Consumers are told to trust `predicateType` inside the verified Statement, not the media type.

**What it contributes to the post-quantum question** ("which attestation systems have a stated post-quantum path, and which have a gap"): **no stated path, by design.** The file never names an algorithm, a key type or a size limit. The ITE-5 item "SHOULD NOT require the inclusion of signing key algorithms in the signature" (§Schema) means a verifier learns the algorithm from its own key policy, keyed by `keyid`, and never from the envelope. So the envelope itself neither blocks ML-DSA or SLH-DSA nor helps with them. Migration happens wholly in the signer, the key distribution and the verifier policy, none of which the Attestation Framework specifies. **Our reading, not a stated path:** the one MUST, multiple signatures, is what lets a producer dual-sign one Statement with a classical and a PQ key during a transition. Nothing in the file says how a verifier should combine them. `docs/validation.md`, read under `in-toto-attestation-v1`, accepts any one recognised key. A dual-signed envelope therefore gives no more assurance than its weakest accepted signature unless the policy layer requires both.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Defines what an in-toto consumer must authenticate (payloadType with payload) and the verify-before-parse rule (§Schema, §Fields, §Storage convention) |
| Cryptography | `adjacent` | Algorithm-agnostic by explicit choice. No primitive, no algorithm identifier, no key format |
| This project | `core` | The in-toto side of DEC-005 and R-I-03's export target |

- **DEC-005** (envelope for ArtifactStatement: DSSE, COSE_Sign1, or both). §Alternative Envelope schemas rules that `COSE_Sign1` is *not* ITE-5 compliant, because it supports one signer only, and that `COSE_Sign` is. A "both" answer to DEC-005 that pairs DSSE with COSE_Sign1 therefore yields a COSE form that in-toto itself would not accept as an in-toto envelope. This is a constraint DEC-005 should record.
- **R-I-03** (export to in-toto Statement + DSSE, or COSE_Sign1 + CWT). An export conforming to this file must set `payloadType` to `application/vnd.in-toto+json` or `application/vnd.in-toto.<predicate>+json`, with `payload` a base64 JSON Statement (§Fields). See Limits for the two forms disagreeing.
- **R-O-05** (proposed in ARCH-0001 v0.2.0: signed payload verbatim, authenticated type indicator, verify before decoding, never canonicalize). The ITE-5 list in §Schema is close to the same rule set: an authenticated payload type, avoid depending on canonicalization, and don't require parsing the payload before verifying. Note the strength. ITE-5 has these as SHOULD or SHOULD NOT, while R-O-05 has them as SHALL. §Fields upgrades only the payload type to a MUST.
- Not claimed: R-M-06. Multiple signatures in one envelope is carriage, not a threshold principal. The *k*-of-*n* rule lives in policy, not here.

**Relations.** `part_of: in-toto-attestation-v1` (this file is one layer of that framework). `see_also` is kept to two edges: `secure-systems-lab-dsse` (the RECOMMENDED envelope format, §Schema) and `rfc-9052` (the current COSE text behind the stale RFC 8152 link, see Limits). RFC 8152 and the Sigstore Bundle are recorded under `cites`, which is what the file references.

## Implementations

**Searched 2026-11-03** (GitHub API for licence and activity; web search for PQ use).

| Name | Kind | License | URL |
|---|---|---|---|
| securesystemslib (DSSE) | open source, Python | MIT | https://github.com/secure-systems-lab/securesystemslib |
| in-toto-golang | open source, Go | API reports NOASSERTION; `in-toto-attestation-v1` records Apache-2.0 | https://github.com/in-toto/in-toto-golang |
| Sigstore cosign | open source, Go | Apache-2.0 | https://github.com/sigstore/cosign |
| witness | open source, Go | Apache-2.0 | https://github.com/in-toto/witness |
| AWS KMS ML-DSA walkthrough | commercial (blog) | — | https://aws.amazon.com/blogs/security/quantum-resistant-signing-on-aws-part-1-build-a-software-supply-chain-with-ml-dsa/ |

**PQ search result.** We found no in-toto or DSSE document that registers or profiles an ML-DSA `keyid` or algorithm. That is consistent with the envelope having no place for one. One vendor walkthrough (AWS, above) signs an in-toto Statement with ML-DSA. We did not check its envelope details. Cosign's Sigstore bundle carries a single signature, so it cannot hold a classical+PQ dual signature in one envelope. envelope.md itself flags this single-signature limit (§Alternative Envelope schemas, footnote 1).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations (`part_of: in-toto-attestation-v1`), `bears_on`, implementations survey |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed.** This is a `spec` record at the summary bar for issue #45's post-quantum calibration batch. A full extraction would be owed if one is wanted, and no issue owns it yet. The file is short: a raw grep finds 10 MUST, 15 SHOULD, 3 MAY, 1 REQUIRED and 1 RECOMMENDED (4 of the SHOULDs are SHOULD NOT). That is an unreconciled grep, not an FX-1 count. The same text is already read, and its defects recorded, under `in-toto-attestation-v1`, which holds the whole v1.2.0 tree. This record holds only the envelope file, pinned to a current commit. The `.cache/` copy is local and gitignored.

## Limits

- **Two internal contradictions, already recorded by `in-toto-attestation-v1` and confirmed here.**
  - §Schema's ITE-5 list makes an authenticated payload type a SHOULD, but §Fields makes it a MUST.
  - §Fields' general rule requires the form `application/vnd.in-toto+<encoding>`, yet its DSSE-specific rule also allows `application/vnd.in-toto.<predicate>+json`, which does not have that form.

  For export, take the stricter reading in both cases. Neither was fixed between v1.2.0 and main `50bf017`: the bytes are identical.
- **Stale COSE reference.** `[COSE_Sign]` links RFC 8152 §4.1. RFC 9052 obsoleted RFC 8152 in 2022. The ITE-5 judgement about COSE_Sign and COSE_Sign1 still holds under RFC 9052.
- **The media type is unauthenticated metadata, and the file says so.** §Fields and §Storage convention both tell consumers not to rely on `<predicate>` in the media type, and to verify, then read `predicateType`. That is correct. The consequence is that file naming (§File naming convention) and storage media types carry no security meaning.
- **Silent on algorithm, key size and payload size.** That is the PQ gap above. Large PQ signatures and keys are not a problem the envelope even mentions. Whether consumers cap envelope size is not addressed.
- **Trust is out of scope.** Who may sign which predicate, and how many signatures are needed, sit outside this file. `keyid` is only a hint (§Schema, §Fields).
- **Read scope.** The whole file was read. DSSE v1.0.2 itself was not re-read for this record; see `secure-systems-lab-dsse`. ITE-5 was not fetched.

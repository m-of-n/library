---
schema: "library-summary/v1"
id: rfc-9942
record: rfc-9942
type: summary
updated: "2026-09-28"
---

# CBOR Object Signing and Encryption (COSE) Receipts

|  |  |
|---|---|
| **Type** | rfc (IETF, Standards Track) |
| **Maturity** | `standard` — Standards Track, IESG-approved. **Not an STD** |
| **Authors** | O. Steele (Tradeverifyd), H. Birkholz (Fraunhofer SIT), A. Delignat-Lavaud, C. Fournet (Microsoft) |
| **Published** | 2026-06 |
| **Identifier** | RFC 9942 · DOI 10.17487/RFC9942 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9942.txt |
| **Digest** | `sha256:da8ed24e…` — full value in `record.yaml`, re-fetched and re-verified 2026-09-28 against the digest recorded 2026-09-22 |

## Overview

A Receipt is a `COSE_Sign1` carrying a proof about a Verifiable Data Structure — typically that an entry is in a log (inclusion) or that a log has only been appended to (consistency). The document's actual mechanism is three COSE header parameters (§2): `receipts` (394) holding an array of receipts, `vds` (395) naming the data-structure algorithm, and `vdp` (396) holding the proofs keyed by proof type. It then defines **exactly one** VDS — `RFC9162_SHA256`, value 1, a SHA-256 binary Merkle tree (§5) — with inclusion (`-1`) and consistency (`-2`) proofs given as CBOR arrays.

The lasting product is therefore not the one algorithm but the two IANA registries it opens under Specification Required (§8.2): COSE Verifiable Data Structure Algorithms, and COSE Verifiable Data Structure Proofs. Everything beyond Merkle/SHA-256 arrives by registration, not by revision. And the document is candid about the limit of that design: §4.2 states plainly that implementers **should not expect interoperability across** VDSs, and that a security analysis MUST precede migrating to a new one. The envelope is unified; the proof layer inside it is not.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | **`core`** | The verification-order rules and the detached-payload hazard (§4.4, §5.2.1, §5.3.1) are where receipts are got wrong |
| Cryptography | **`core`** | Defines the CBOR encodings of Merkle inclusion and consistency proofs and the procedure for checking them, plus signature/hash pairing guidance (§7.1) |
| This project | **`core`** | The half of the transparency story `rfc-9943` defers entirely |

- **DEC-005** — the existing edge, and it holds. Receipts **MUST** be tagged `COSE_Sign1` (§4.3); the whole design assumes a COSE envelope, so adopting receipts means adopting that envelope.
- **R-M-12** — added by this summary, and this is the library's strongest specimen of the pattern. The document does not merely consume registry identifiers, it **creates two registries** and burns three COSE header parameters (394, 395, 396) in the Specification Required range. §8.2.1 then writes the governance: assign the next positive integer, discourage point squatting, require a specification, forbid a structure registration without its matching proof registration and vice versa, and keep the change controller the same for both. If we want an argument about what registry-allocated identifiers cost and what governance they drag along, it is written out here in full.

## What it settles, and what it costs

RFC 9943 defers every proof and data-structure question to this document (§5.1.3, §9.4.1 there). This is what comes back.

**Settles.**

- **One parse for any receipt.** A verifier reads `vds` from the protected header and knows which proof structure to expect in `vdp` — without understanding the VDS itself.
- **Consistency proofs exist here, and only here.** RFC 9943 *requires* append-only and non-equivocation (§5.1.3) without defining how either is checked. The `-2` consistency proof (§5.3) is the mechanism, and it is what lets a relying party detect a log that forked rather than grew.
- **Offline verification, concretely.** For inclusion, the verifier recomputes the Merkle root from a candidate entry and the proof path; the recomputed root *becomes* the `COSE_Sign1` payload, and the signature is then checked over it (§5.2.1). No contact with the log is required.
- **A governed extension path**, per §8.2.1 above.

**Costs.** Five, four of them stated by the RFC itself:

1. **Cross-VDS interoperability is disclaimed, not merely unsolved** (§4.2). A relying party accepting receipts from two services on different VDSs needs two verifiers. The unified header hides a non-unified proof layer.
2. **Only one VDS is defined, and agility is by registration.** §4.4.1 requires a *separate* IANA registration per hash algorithm — `RFC9162_SHA3_256` would need its own entry and is not defined here. Changing hash function is a standards action, not a parameter.
3. **The safety property is a `SHOULD`.** §4.4 says profiles' payloads SHOULD be detached, because detaching "force[s] verifiers to recompute the root from the proof and protect[s] against implementation errors where the signature is verified but the payload is incompatible with the proof." That is precisely the attack a receipt must resist, and the mitigation is not mandatory.
4. **Verification order differs by proof type, and the RFC knows it is a hazard.** Inclusion verifies proof first, then signature (§5.2.1); consistency verifies signature first, then proof (§5.3.1). §5.3.1 then recommends implementations return a *single boolean* "to reduce the chance of accepting a valid signature over an invalid consistency proof." A specification recommending a coarse API to stop implementers misusing the fine one is an admission about how easy this is to get wrong.
5. **No freshness and no revocation.** Validity periods (§7.2) and status updates (§7.3) are both explicitly out of scope. Read against RFC 9943 §4 — where a receipt's key, algorithm, validity period and claims MAY change each time one is issued — **neither document says how a relying party learns that a receipt it holds is stale or withdrawn.** That gap spans both records and belongs to neither; it is the most consequential thing this pair leaves open.

Privacy has one concrete cost too: every inclusion proof carries `tree-size`, so a receipt leaks how large the log was when it was issued (§6.1). The RFC's own example is a log that stores only breach notices, where that number is the count of prior breaches.

## Implementations

**Searched 2026-09-28.** Several exist, all small and early; none is a well-known library, and none is vetted by us.

| Name | Kind | License | URL |
|---|---|---|---|
| `scitt-cose` (Action State Group) | open source, Python | not stated | https://pypi.org/project/scitt-cose/ |
| `vaaraio/vaara` (PR #775) | open source | not stated | https://github.com/vaaraio/vaara/pull/775 |
| `wilder-robotics/pask-workspace` | open source, Rust | not stated | https://github.com/wilder-robotics/pask-workspace |
| SCITT WG receipt-verification vectors | test vectors | not stated | https://github.com/troybrandonc-bit/machine-testimony/issues/89 |

Two observations:

- **`scitt-cose` is published by Action State Group** — the same organisation as S. Mih, author of `draft-mih-scitt-agent-action-capsule`, which this library also holds. Two of our SCITT records trace to one small org. That is concentration, not independent uptake, and it should temper any claim that the receipt model is widely implemented.
- One source reports cross-implementation vectors covering `vds=2` for Microsoft CCF, which would mean the registry has already grown past the single value this RFC defines. **Unverified** — recorded as a lead, since confirming it means reading the IANA registry we do not hold (see Limits).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled/`. The normative density here is real — §4.3, §4.4.1, §5.2.1 and §5.3.1 carry MUSTs a verifier implementation must satisfy — so this is a plausible future `distill` target if we ever build a receipt verifier. Nothing is built on it yet.

## Limits

- **RFC 9162 is not in the library, and here that is load-bearing.** The only VDS this document defines is a mapping onto Section 2.1 of RFC 9162, and §7 delegates its security considerations to RFC 9162 and RFC 9053. We hold a receipt specification whose sole concrete instantiation, and whose security analysis, live in a document we do not have. This is a higher-priority frontier gap than the same citation in `rfc-9943`.
- **The two registries this RFC creates are not held either.** We hold [`iana-cose-algorithms`] but not COSE Verifiable Data Structure Algorithms or COSE Verifiable Data Structure Proofs. Since the RFC defines only value 1 and everything else arrives by registration, the library cannot currently see the live state of the extension point this document exists to open.
- **It analyses none of its own cryptography.** §7 is three lines and two pointers. Claims about the security of these proofs must be sourced from RFC 9162, not from here.
- **Nothing about who signs a receipt.** The document specifies the proof and the envelope; which key a relying party should trust, and how it learns it, is RFC 9943's Transparency Service identity problem and is untouched here.
- **`status: summarized`, `confidence: medium`** — read end to end and digest verified by an agent; no human has reviewed this summary. The `usefulness` verdict in `record.yaml` is S1's from 2026-09-22 and is left as they wrote it.

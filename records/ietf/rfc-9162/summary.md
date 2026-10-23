---
schema: "library-summary/v1"
id: rfc-9162
record: rfc-9162
type: summary
updated: "2026-10-23"
---

# Certificate Transparency Version 2.0

|  |  |
|---|---|
| **Type** | rfc (IETF TRANS WG, from `draft-ietf-trans-rfc6962-bis-42`) |
| **Maturity** | `experimental`: Category Experimental on the title page and in the RFC Editor metadata, checked 2026-10-23. **Not Standards Track**, though RFC 9942 (Standards Track) depends on it normatively |
| **Authors** | B. Laurie, E. Messeri (Google), R. Stradling (Sectigo) |
| **Published** | 2021-12 |
| **Identifier** | RFC 9162 · DOI 10.17487/RFC9162 · Obsoletes RFC 6962 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9162.txt |
| **Digest** | `sha256:a0e432ce…` (full value in `record.yaml`), fetched 2026-10-23 |
| **Errata** | one, ID 8670, editorial, Held for Document Update: the reporter argues that the "or fn is 0" exit in §2.1.3.2 step 4.b.ii and §2.1.4.2 step 6.b.iii cannot occur. Wording only; the algorithms' results are unchanged |

## Overview

CT 2.0 makes a certificate authority's issuance publicly checkable by having logs append every submitted certificate to **one append-only Merkle tree per log** (§4) and sign two kinds of commitment. A Signed Certificate Timestamp (SCT, §4.8) promises to incorporate an entry within the Maximum Merge Delay. A Signed Tree Head (STH, §4.10) commits to the tree at a given size. Inclusion proofs show that an entry is under an STH's root, and consistency proofs show that a later STH extends an earlier one (§2.1.3, §2.1.4). Neither kind of proof is signed. Each one gets its authority from the signed STHs it connects (§5.3, §5.4).

The document does not claim the logs are trustworthy. §1 says plainly that a log showing *"different, inconsistent views of itself to different clients"* defeats the auditing mechanisms, and that *"it is necessary to treat each log as a trusted third party"*. The defence against such a log, comparing STHs among clients ("gossip"), is *"an active area of research and not defined here"* (§11.3). What CT 2.0 delivers is **detection by parties who see the same view**, plus signed evidence once they do (§8, §8.3).

For this library, the RFC matters for a narrow reason. It is where `rfc-9942`'s only Verifiable Data Structure, `RFC9162_SHA256`, is actually defined. RFC 9942 §5 maps "the data structure described in Section 2.1 of [RFC9162]" and §7 delegates its security considerations here.

## The proof layer, by locator

This section exists so that a report author (mofn R-0006 §2.4, `unverified.md` §6) can check each guarantee against the source rather than against RFC 9942's account of it.

**Tree hash, §2.1.1.** For an ordered list of entries D_n, the Merkle Tree Hash `MTH` is `HASH()` for the empty list. A single entry (the leaf hash) is `HASH(0x00 || d[0])`. For n > 1, `HASH(0x01 || MTH(D[0:k]) || MTH(D[k:n]))`, where k is the largest power of two smaller than n. The 0x00/0x01 split is the leaf/node domain separation, and the RFC states why it is there: *"this domain separation is required to give second preimage resistance"*. Trees need not be balanced, but *"its shape is uniquely determined by the number of leaves"*. HASH is a log parameter drawn from the §10.2.1 registry, whose only assigned value is SHA-256 (0x00). RFC 6962 (§2.1) hard-wired SHA-256 here, and this generalisation is 9162's only change to the construction.

**What a leaf is, §4.7.** A CT leaf is `HASH(0x00 || TransItem)`, where the TransItem has type `x509_entry_v2` or `precert_entry_v2` and wraps a timestamp, `issuer_key_hash`, the TBSCertificate and the SCT extensions. The leaf input is therefore a specific serialised byte string. Re-encoding it changes the leaf.

**Verifying a whole tree, §2.1.2.** A stack algorithm recomputes the root from a complete entry list. Monitors use it (§8.2 step 5).

**Inclusion proof, §2.1.3.** Generation is the recursive `PATH(m, D_n)` (§2.1.3.1). Verification (§2.1.3.2) takes `leaf_index`, `tree_size`, `root_hash`, the `inclusion_path` and **a hash**: the leaf hash, not the entry bytes. Step 1 fails if `leaf_index >= tree_size`. Step 4.a fails if `sn` reaches 0 while path elements remain. Otherwise the steps walk `fn`/`sn` (index and last index), combining with `HASH(0x01 || p || r)` or `HASH(0x01 || r || p)` according to whether `LSB(fn)` is set or `fn == sn`. Step 5 accepts only if `sn` is 0 **and** the computed root equals `root_hash`. On our reading, 4.a and the `sn == 0` test are what reject a path of the wrong length. The guarantee is stated as: *"If the root computed from the inclusion proof matches the true root, then the inclusion proof proves that the leaf exists in the tree"* (§2.1.3). That means the tree of **that size with that root**, i.e. under one STH. The proof says nothing about whether other clients were shown the same tree.

**Consistency proof, §2.1.4.** Generation is `PROOF(m, D_n) = SUBPROOF(m, D_n, true)` for 0 < m < n, the unique minimal proof, with at most ceil(log2(n)) + 1 nodes (§2.1.4.1). Verification (§2.1.4.2) takes **two tree heads**, `first_hash` at size `first` and `second_hash` at size `second` with 0 < first < second, plus the `consistency_path`. It fails on an empty path. It prepends `first_hash` when `first` is an exact power of two, then rebuilds both roots (`fr`, `sr`) in one pass and accepts only if `fr == first_hash`, `sr == second_hash` and `sn == 0`. The property proven is that *"the first m inputs D[0:m] are equal in both trees"* (§2.1.4), which is append-only growth **between two heads the verifier already holds**.

**Normative force.** All three verification algorithms are introduced with "the following algorithm may be used" (§2.1.2, §2.1.3.2, §2.1.4.2): lowercase, not BCP 14. §1.3 lists "Verification algorithms" as **new in 9162**. RFC 6962 defined the same `PATH`/`PROOF` generation (6962 §2.1.1, §2.1.2) and gave no step-by-step verifier. Worked examples for a 7-leaf tree are in §2.1.5.

**What is signed, §4.8 and §4.10.** Signatures use an algorithm from the §10.2.2 registry, a subset of TLS SignatureScheme (§2.2). Structures are defined and encoded in the TLS presentation language of RFC 8446 §3 (§1.2). That is a fixed binary layout with length-prefixed vectors, and the RFC defines **no canonicalisation step**. The only ordering rule is that extension vectors MUST be sorted by `extension_type` with no duplicates (§4.8, §4.9). For an STH, *"signature is computed over the tree_head field"* (§4.10), a `TreeHeadDataV2` of `timestamp`, `tree_size`, `root_hash` and `sth_extensions` (§4.9). Two consequences that should be read straight from the structs:

- **`tree_size` and `timestamp` are inside the signed bytes.** An STH commits to *this root at this size at this time*.
- **`log_id` is not inside the STH's signed bytes**: it sits beside `tree_head` in `SignedTreeHeadDataV2`. Neither is a type tag. RFC 6962's `TreeHeadSignature` signed `version` and `signature_type = tree_hash` along with the head (6962 §3.5). 9162 dropped both from the STH signature input. SCT signatures cover a `TransItem` (§4.8), which does begin with a type. We have not analysed whether the missing tag on STHs matters, and we record it as an observation for FX-1, not as a finding.

**Proofs are unsigned by design.** In the RFC's words, *"no signature is required for the inclusion output, as it is used to verify inclusion in the selected STH, which is signed"* (§5.4). The same applies to consistency output (§5.3, §5.5).

**What the RFC says the proofs do not give you.**

- **Split views.** The §1 passage quoted above. §8.3 lists "the consistency of the log view presented to all query sources" among the four properties auditors should check. It then defers how to check it to §11.3, which leaves gossip undefined.
- **Misissuance detection.** Logs do not detect misissuance (§11.2). An SCT means *"a log has committed to publishing the certificate"*, and *"A signed timestamp does not guarantee"* that anyone looked (§11).
- **A bound on exposure.** A misissued certificate can be used for up to twice the MMD before it is available for audit (§11.1).
- **Algorithm change.** A log cannot change its hash or signature algorithm mid-life. It must be frozen and a new log started (§9, §4.13).

**Who checks what, §8.** TLS clients SHOULD verify an inclusion proof against the STH supplied with it, and SHOULD check that STH's consistency with one they already know (§8.1.5). Monitors MUST inspect every new entry, and SHOULD verify each STH's signature and then either rebuild the tree or verify a consistency proof to the previous STH (§8.2). Auditing (§8.3) rests on the claim that a failed audit leaves the auditor *"in possession of signed proof of the log's misbehavior"*.

**Log IDs, §4.4 and §10.2.5.** A log is identified by an OID that it MUST NOT share with another log, carried as `opaque LogID<2..127>` (the DER value without its tag and length). The operator may allocate the OID under its own arc or request one from the IANA "Log IDs" registry (First Come First Served). The registry's stated purpose: *"The only advantage of the registry is that the DER encoding can be small."* RFC 6962 identified a log by the SHA-256 hash of its public key (6962 §3.2), and §1.3 lists the move to OIDs as a major change. §4.1 still requires that *"A log MUST NOT use the same keypair as any other log"*.

## Against RFC 9942's account of it

`rfc-9942` was checked here against its own source (`.cache/rfc-9942.txt`, digest matching that record). Where it describes 9162 accurately, it is not repeated. These are the places where it diverges or says less than a reader might assume.

1. **A 9942 receipt is not an STH.** In 9942, *"the payload is the Merkle Tree root that corresponds to the log at size tree-size"* (9942 §5.2.1). `tree-size` and `leaf-index` travel in the **unprotected** header inside `vdp` (9942 §5.2, §5.2.1 Fig. 5), and the protected header 9942 requires (Fig. 4) holds only `alg` and `vds` (other labels are permitted, none required). A 9162 STH signs `timestamp` and `tree_size` together with the root (§4.9, §4.10). The word "timestamp" does not occur in the 9942 source, so the §8.3 audit move ("verifying an SCT against any STH dated after the SCT timestamp + the Maximum Merge Delay") has no counterpart in a receipt. Time is optional, not absent: 9942 §7.2 says receipts MAY include validity periods, pointing to the CWT `iat`/`nbf`/`exp` claims, and puts the details out of scope. But **R-0006 §2.4's phrase "a COSE_Sign1 whose payload is a Merkle root" should not be read as "an STH in COSE"**: the signed bytes are different.
2. **The consistency check is described differently.** 9942 §5.3.1 says *"the consistency proof is checked by applying a previous inclusion proof to the consistency proof"*. 9162 §2.1.4.2 takes no inclusion proof. Its inputs are two root hashes and their sizes. A charitable reading is that the older root is the one recomputed from an earlier inclusion receipt. That works only if that receipt's `tree-size` equals the consistency proof's `tree-size-1`, and we found no such condition stated in 9942. The 9942 consistency receipt signs only the newer root (9942 §5.3.1), so the verifier must obtain the older root, at the right size, from somewhere 9942 does not name.
3. **Inclusion is verified from a leaf hash, not entry bytes.** 9942 §5.2.1 step 1: *"The verifier applies the inclusion proof to the bytes of a candidate entry."* 9162 §2.1.3.2 starts from a hash, and the leaf hash is `HASH(0x00 || entry)` (§2.1.1, §4.7). The 9942 source contains neither "0x00" nor "leaf hash". This is a specification gap, not an error. On our reading, an implementer who works only from 9942 and omits the domain-separation byte produces a verifier that fails to interoperate with any 9162 tree, rather than an insecure one. What a SCITT "entry" is (what d[m] is) is defined neither by 9942 nor by this RFC.
4. **The leaf_index condition is weaker at its source than in our extraction.** `rfc-9942/distilled/normative.md` (§5.2) treats the quoted *"If leaf_index is greater than or equal to tree_size, then fail the proof verification."* as an imported normative requirement. In 9162 it is step 1 of an algorithm that "may be used" (§2.1.3.2). 9942 quotes it accurately; the stronger force is our wording, not either RFC's. The quote also carries only step 1, not step 4.a or the step-5 `sn == 0` test.
5. **On R-0006 §2.4's guarantees, read directly.** R-0006 says an inclusion receipt "proves one thing: the entry's inclusion in the VDS". In 9162 terms this is inclusion in **the tree of the stated size under the signed root**, not in "the log" as seen by others (§2.1.3, §1). R-0006 says "a consistency proof shows the log is append-only between two sizes". That holds, and **only between two heads the verifier holds** (§2.1.4.2). R-0006's conclusion that transparency does not catch a dishonest log is **9162's own position**, made in §1 and §11.3, and no longer only the `scitt` topic's reading. One qualification: §11.3 says append-only violations can be detected "by multiple clients comparing their instances of the STHs". The detection mechanism exists in principle and is simply left undefined.

None of these is set as `contradicts`. 9942 and 9162 do not assert incompatible things. Items 1 to 3 are places where 9942 says less than, or differently from, the document it delegates to.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | **`core`** | States its own trust model (§1: logs are trusted third parties) and threat list (§11.3), which the SCITT stack inherits through `rfc-9942` §7 |
| Cryptography | **`core`** | Defines the tree hash with domain separation, both proofs and their verification algorithms (§2.1) |
| This project | `adjacent` | We consume it only through receipts, and R-O-04 keeps transparency at *Could* |

- **R-O-04**: the direct edge. A SCITT-like transparency service is a 9942 receipt over a 9162 tree. Any guarantee the optional registration provides is bounded by §2.1 and §11.3 here, including the explicit absence of split-view protection.
- **R-M-12**: a clean specimen in both directions. RFC 6962 named a log by the **hash of its key**, which is key-relative. 9162 replaced that with an **OID**, from an operator's own arc or an FCFS IANA registry whose only stated benefit is a shorter encoding (§4.4). 9162 also moves its algorithm identifiers into IANA registries (§1.3, §10.2.1, §10.2.2). It is a worked case of a protocol choosing registry-style identifiers over key-derived ones. The document gives no reason for the move beyond §1.3's list entry and §4.4's encoding-size remark.
- **DEC-002**: narrow. CT signs fixed-layout TLS-presentation-language structures, and the leaf is the hash of exact serialised bytes (§1.2, §4.7). It needs no canonicaliser because its only freedom is extension order, which §4.8 and §4.9 fix. That is prior art for "a fixed binary layout needs no canonicaliser", and it is not a DEC-002 option.

## Implementations

**Searched 2026-10-23** (web search, GitHub repository search for "RFC9162 / RFC 9162", and READMEs).

| Name | Kind | License | URL |
|---|---|---|---|
| `transparency-dev/merkle` | open source, Go: tree and proofs | Apache-2.0 | https://github.com/transparency-dev/merkle |
| `google/trillian` | open source, Go: verifiable log | Apache-2.0 | https://github.com/google/trillian |
| `google/certificate-transparency-go` | open source, Go: CT v1 stack | Apache-2.0 per LICENSE (GitHub: NOASSERTION) | https://github.com/google/certificate-transparency-go |
| `FiloSottile/sunlight` | open source, Go: static-ct-api log | ISC | https://github.com/FiloSottile/sunlight |
| `transmute-industries/rfc9162` | open source, TypeScript | Apache-2.0 | https://github.com/transmute-industries/rfc9162 |

**This search found no production CT v2 log.** The CT code bases found (Trillian, certificate-transparency-go) and the C2SP static-ct-api spec that Sunlight implements all cite RFC 6962. The search also found nothing showing the v2 wire formats (TransItem, OID log IDs, `transparency_info`) in deployed use. **This barely affects us.** The §2.1 tree and proof construction is the same as 6962's for SHA-256, so v1 proof libraries such as `transparency-dev/merkle` compute what `RFC9162_SHA256` needs. Other small GitHub hits naming RFC 9162 as a Merkle library (e.g. TrustBeat/merklon, faustbrian/go-merkle-tree) and the SCITT receipt implementations already listed on `rfc-9942` were seen and not vetted.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

**No `distilled/`.** This record is at the summary bar, written for library#87. RFC 9162 is an `rfc` record, so the FX-1 extraction (normative text, BCP 14 keywords reconciled, the TLS-presentation structs and the Appendix B ASN.1 module as schema, the §5 API as messages and protocol, the §2.1.5 trees as test vectors) is **owned by library#89**. That extraction should settle three items left open here: whether the untagged STH signature input (§4.10) matters; a precise statement of 9942 §5.3.1 against §2.1.4.2; and fixtures from the §2.1.5 example. No keyword count is given here: a raw `grep -w` over the source finds 136 uppercase keyword tokens, including §1.1's own list, and that number is not a reconciled count.

## Limits

- **It solves split views by assumption.** The single most important sentence for anyone relying on proofs is in §1: logs must be treated as trusted third parties because inconsistent views defeat auditing. Gossip is left undefined (§11.3). Every system that inherits these proofs, including SCITT through `rfc-9942`, inherits that gap unless it adds its own mechanism.
- **Experimental, and this search found no deployed v2.** Its standing is lower than that of `rfc-9942`, which normatively depends on it.
- **Log parameter distribution is out of scope.** §8 says the document *"does not describe how the parameters are obtained"* (keys, log IDs, MMD), pointing to browser policy as an example. This is the same TS-key-distribution gap `rfc-9943` leaves.
- **Proof guarantees are stated in prose, not proven.** Second-preimage resistance is asserted (§2.1.1) and the resemblance to the [CrosbyWallach] history tree is noted; no security proof is given. `rfc-8391` is 9162's pointer for Merkle background (§2.1). The Merkle papers held here (`merkle-1979-thesis`, `merkle-1989-certified`) are not cited by 9162 and are linked as `see_also` only.
- **Internal edge case.** §5.3 says a consistency proof between equal sizes MUST be empty, while §2.1.4.2 fails an empty path and requires first < second. Equal-size "consistency" is therefore served by the API and outside the verifier, so callers have to special-case it.
- **`rfc-6962` is still a stub.** The comparisons to 6962 above were made against its text, fetched to `.cache/rfc-6962.txt` (sha256 `08fdf31c…`) for this pass, at §2.1, §3.2 and §3.5 only. That record was not edited.

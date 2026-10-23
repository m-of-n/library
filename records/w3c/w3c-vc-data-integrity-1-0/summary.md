---
schema: "library-summary/v1"
id: w3c-vc-data-integrity-1-0
record: w3c-vc-data-integrity-1-0
type: summary
updated: "2026-10-23"
---

# Verifiable Credential Data Integrity 1.0

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` — W3C Recommendation, the W3C's terminal maturity level. The RFC 2026 ladder does not apply to W3C documents; this is a mapping, not a quotation. The header links an errata page; on 2026-10-23 it listed no recorded errata. |
| **Authors** | Authors: Dave Longley (Digital Bazaar), Manu Sporny (Digital Bazaar), Ivan Herman (W3C). Editors: Manu Sporny, Ted Thibodeau Jr (OpenLink Software), Ivan Herman, Dave Longley, Greg Bernstein (Invited Expert) |
| **Published** | 2025-05-15 (W3C Recommendation; this version `REC-vc-data-integrity-20250515`, Verifiable Credentials Working Group). The latest-version URL https://www.w3.org/TR/vc-data-integrity/ still resolved to this REC on 2026-10-23 |
| **Identifier** | https://www.w3.org/TR/2025/REC-vc-data-integrity-20250515/ |
| **Source** | https://www.w3.org/TR/2025/REC-vc-data-integrity-20250515/ |
| **Digest** | `ba5c4baf13fe3bab3ebd95ab6650d6fe83720e254b383bb444b4fbbae7bcf4fe` (re-verified 2026-10-23 against the cached bytes) |

## Overview

Data Integrity embeds a proof *inside* the JSON document it secures, under a
`proof` property, instead of wrapping the document in an envelope (§2.1,
§5.12). It is a framework, not a signature scheme. It fixes the proof's data
model (§2.1–§2.4), a generic Add Proof / Verify Proof wrapper (§4.2–§4.5) and
the obligations a **cryptosuite** specification must meet (§3). The actual
transformation, hashing, proof serialization and proof verification are left
to those suites. The argument is *serialization flexibility* (§1.2, §5.6):
what gets signed is a **transformed** form of the data — "The data that is
protected by any data integrity proof is the transformed data" (§5.7) — so one
proof can travel across JSON, CBOR or YAML representations "without the need
to regenerate the cryptographic proof" (§1.2). The cost of that choice is the
answer to the question this record was opened for.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | It specifies a verifier procedure (§4.4, §4.5), proof-purpose, domain and challenge binding (§2.1, §2.2, §5.11), and names the transformation attacks — non-injective canonicalisation, silently dropped data, dataset poisoning (§2.4.3, §5.6, §5.13). |
| Cryptography | adjacent | It defines no primitive and no hash. Every algorithm that touches bytes belongs to a cryptosuite (§3); §5.1–§5.4 are guidance on suite versioning and agility. |
| This project | adjacent | The securing route for **R-I-06** (*Could*: export a subset of `AuthzCert` as a W3C VC), and the counter-example to **R-O-05**. It is not, and cannot become, our native signing form. |

Bears on **R-I-06**, **R-O-05** and **R-O-03**. R-O-05 is *proposed* in
`ARCH-0001-PROPOSAL-v0.2.0` §7 (argued in §3.4, whose pointer to §6 is
stale: §6 there is subject identity) and is not in ARCH-0001 v0.1.2. The mofn
documents disagree on its standing: R-0006 `report.md` §2.3 calls it
"proposed, not accepted", while `ADR-0003` refers to "accepted ARCH-0001
R-O-05". Settling that belongs to mofn. This record treats R-O-05 as the
proposed text.

### The finding: Data Integrity canonicalises at verification, by construction

R-0006 (`unverified.md` §2, `report.md` §2.2–§2.3) left one VC cell open:
**does VC Data Integrity canonicalise at verification?** It does. It is built
to, it cannot avoid it, and it holds no signed bytes that a verifier could
check verbatim. The locators:

1. **What is signed is not transmitted.** A proof carries `proofValue`, a
   Multibase string whose contents are set by the cryptosuite (§2.1, §3.1). The
   protected data is "the transformed data" (§5.7). The secured document carries
   the *untransformed* data plus the proof (§4.2 steps 5–6: a copy of the input
   document with `proof` set). No field carries the byte string the signature
   covers.
2. **The verifier rebuilds the signed bytes.** §1.1 (non-normative) gives
   verification as Transformation, Hashing, Proof Verification: "During
   verification, the transformation and hashing steps are conceptually the same
   as described above." §3 makes it a MUST that every cryptosuite specification
   detail its transformation, hashing, proof-serialization and
   proof-verification algorithms, and define a `verifyProof` that takes the
   *secured document* (a map) as input.
3. **The input to that transformation is the received, unauthenticated
   document.** In §4.4 Verify Proof, step 1 parses `documentBytes` to an Infra
   value. Step 2 checks only that the result and its `proof` are maps. Steps
   4–7 read `proof.type`, `verificationMethod`, `proofPurpose`, `domain` and
   `challenge` out of that **unverified** parse. Step 8 passes the whole parsed
   `securedDocument` to `cryptosuite.verifyProof`. Nothing is authenticated
   until step 8, and step 8 is where the suite transforms the document.
4. **Which canonicaliser runs is the suite's choice, and Data Integrity names
   the two.** §5.3 and §5.7 name `eddsa-rdfc-2022` and `ecdsa-rdfc-2019`, which
   use RDF Dataset Canonicalization (`w3c-rdf-canon-1-0`) to N-Quads, and
   `eddsa-jcs-2022` and `ecdsa-jcs-2019`, which use JCS (`rfc-8785`). §6.2 names
   `bbs-2023` for selective disclosure without stating its transformation. Cited
   and not ingested: the EdDSA suite REC (https://www.w3.org/TR/vc-di-eddsa/,
   2025-05-15), read live on 2026-10-23, has a Verify Proof for each suite
   (§3.2.2 rdfc, §3.3.2 jcs). Each one strips `proof`, then `proofValue`, runs
   the suite's Transformation over the unsecured document, and hashes the
   canonical proof configuration and the canonical document. Its Hashing
   algorithm (§3.2.4 / §3.3.4) concatenates the two hashes. The BBS suite
   (https://www.w3.org/TR/vc-di-bbs/, a Candidate Recommendation Draft dated
   2026-09-10 when read) transforms with RDF-CANON (its §1, §3.3). The ECDSA
   suite (https://www.w3.org/TR/vc-di-ecdsa/) was not opened for this pass. Its
   suite names come from Data Integrity §5.3 and §5.7. Those suite locators
   were read through a fetch tool, not checked against cached bytes. Treat
   them as pointers, not quotations.
5. **Business logic touches the data before verification.** §4.1's consumer
   steps put schema validation of the incoming document (JSON Schema "or an
   equivalent mechanism") at step 2, before verification at step 3. Context
   validation comes after verification, as §2.4.1 requires.

So for R-O-05 the answer is the same as rfc-8785's, and for the same reason.
JCS is one of the two transformations Data Integrity adopts, and its Appendix F
already re-canonicalises at verification (`rfc-8785` Limits). Data Integrity
generalises that pattern into a framework. R-O-05's clauses ("verify the
signature before decoding", "SHALL NOT canonicalize input as part of
verification", "signed payload SHALL be the canonical encoding verbatim") are
each negated by items 1–3. That fills condition (3) of R-0006 §3.2 for the VC
row: **not met**. The Data Integrity route is on the SPKI/RFC 9804 side of the
§2.3 split, not on the DSSE/COSE side.

**What this does to R-I-06.** An export under R-I-06 using Data Integrity would
re-encode our verified statement into JSON(-LD) and have a *new* signer sign a
transformed form of it. The export is then a second, derived statement. It does
not carry our signature, and a VC verifier would canonicalise it. That is
acceptable for an export that is a *Could* and consumed by others. It is not
acceptable as a form we verify. VC-JOSE-COSE (`w3c-vc-jose-cose`) is the
envelope alternative, and §5.12 points readers at JWT and CWT itself. Which
route R-I-06 takes is a question for that record and for mofn, not one this
record settles.

### The other R-0006 ∅ cells

- **What is hashed and signed.** The suite's transformed document, hashed
  together with the proof's own options (the EdDSA suite's Hashing step, item 4
  above). Proof options are signed alongside the data, as the "protected
  declaration" of purpose in §1.4 suggests. Data Integrity itself never says
  what is hashed. It defers that to the suite (§3).
- **What a proof carries** (§2.1): `id` (optional, used for chains), `type`
  (MUST), `proofPurpose` (MUST), `verificationMethod` (a URL, OPTIONAL under
  §2.1 but treated as required by §4.2 step 2 and §4.4 step 4), `cryptosuite`
  (MUST when `type` is `DataIntegrityProof`, §3.1), `created`, `expires`,
  `domain`, `challenge`, `proofValue` (Multibase per CID §2.4; §2.1 lets a suite
  substitute another property), `previousProof`, `nonce`. `digestMultibase`
  (§2.3) lets any object with an `id` commit to an external resource by
  Multihash.
- **How a verifier proceeds.** §4.4: parse the bytes, check the required
  members, check `proofPurpose`, `domain` (set-equal) and `challenge` against
  the caller's expectations, then hand off to the suite. The result carries
  `verifiedDocument`, which per §3 is the secured document with the verified
  proofs *removed* (the parsed map, not the transformed bytes that were
  checked). §5.7 urges trusting only data "provided in a return value from a
  software library that has confirmed that all data returned has been
  successfully protected". Key binding is outside §4.4 and goes through the
  Controlled Identifiers algorithm: verification-method binding (§5.9) and
  verification-relationship validation (§5.10, pointing at CID §3.3).
  Context validation (§4.6) runs after.
- **Proof sets and chains.** A set is unordered (§2.1.1). Appendix A shows that
  any intermediary can remove a member and "the secured data document will
  still verify". A chain binds by `previousProof`: the later proof signs the
  document plus the referenced earlier proofs (§2.1.2, §4.3 step 6 and its
  note). Neither construct carries a threshold. That matches R-0006 `report.md`
  §2.5's "carries `n` and never `k`" reading of DSSE, with set-stripping on top.

## Implementations

Data Integrity has no conformance suite of its own. Its implementation report
(https://w3c.github.io/vc-data-integrity/implementations/) only links three
cryptosuite reports: ECDSA, EdDSA and BBS. Read 2026-10-23, the EdDSA and ECDSA
reports (both dated 2026-10-18) list the implementers below. The rows read show
**only the rdfc suites**. No jcs row appeared in the portion read, though both
report headers list them. Several rows show failures or timeouts, so a row
means *tested*, not *passing*.

| Name | Kind | License | URL |
|---|---|---|---|
| `@digitalbazaar/data-integrity` (Digital Bazaar) | open source, JavaScript | not checked | https://github.com/digitalbazaar/data-integrity |
| `@herculas/vc-data-integrity` | open source, TypeScript | not checked | https://jsr.io/@herculas/vc-data-integrity |
| SpruceID `ssi` | open source, Rust | not checked | https://github.com/spruceid/ssi |
| apicatalog.com (Iron Verifiable Credentials, Filip Kolarik) | open source, Java | not checked | https://github.com/filip26/iron-verifiable-credentials |
| Grotto Networking, LearnCard, Netis (verifier only), Procivis One Core, Trential, Trinsic, bovine | report rows (EdDSA) | not checked | https://w3c.github.io/vc-di-eddsa-test-suite/ |
| CredenceID, Gen Digital, MakoLab, plus most of the above | report rows (ECDSA) | not checked | https://w3c.github.io/vc-di-ecdsa-test-suite/ |

**Licences are deliberately unfilled rather than guessed.** The W3C reports
carry no licence field. We would use these as an export target, not as a
dependency, so opening each repository is not needed yet. Searched 2026-10-23.
As with RDFC, the editors' own house (Digital Bazaar) is one implementer among
roughly a dozen.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites` (the document's own references we hold, plus four gaps) and our relations |
| `summary.md` | this document |

**No `distilled/`, and none is owed by this pass.** This is library#87's pass,
and it claims the **summary bar**: the record is `summarized`, declares no
`distillation` block and adds nothing to `distilled/`, so FX-1 does not fire.
That is a scope judgement, not a verdict that the document is unimportant. As a
`spec` it will owe FX-1 when extracted, and that extraction is **owned by the
library#89**. **What would make it urgent** is a decision
that R-I-06 exports through Data Integrity rather than VC-JOSE-COSE. §4.2–§4.6
would then become code we implement and test, and would need
`requirements.yaml`, a `protocol` artifact for the verifier procedure, and the
W3C cryptosuite test suites as `examples/` fixtures. The extraction would also
have to pull in at least one cryptosuite spec and Controlled Identifiers v1.0,
because the algorithms that touch bytes are not in this document.

**No verbatim normative text here.** Under FX-1 it belongs in
`distilled/normative.md` with its locator. The quoted fragments above are short
and carry their locators by design.

## Limits

1. **It specifies none of the byte-level work.** Transformation, hashing,
   serialization and verification are all the cryptosuite's (§3). This document
   alone cannot tell you what is signed. Every byte-level claim in this summary
   rests on a suite spec cited, not held.
2. **No rejection of non-canonical input, and no way to have one.** The
   transmitted form is never the canonical form, so condition (2) has no
   object: there is nothing for a verifier to reject *as* non-canonical. This
   is a stronger absence than RFC 8949 §4.2's or RDFC-1.0's, where an encoder
   rule exists and the decoder obligation is unstated.
3. **Correctness of the transformation is pushed onto vetting.** §5.13 states
   the risk itself: "if a canonicalization algorithm converts two inputs that
   have different meanings into the same output, then the author's intentions
   can be misrepresented to a verifier". The mitigation is advice to use
   peer-reviewed, proven algorithms, not a mechanism. §2.4.3 adds the
   JSON-LD-specific case, where "undefined terms and relative URLs can be
   dropped silently". It answers with a MUST to throw on data loss and a MUST
   to null the base URL. Condition (1) is therefore delegated to RDFC-1.0 or
   JCS, not met here.
4. **Proof validity time is not checked by the verifier algorithm.** `created`
   and `expires` are defined in §2.1, and §2.6 says checking the proof's
   validity period is "important". §4.4 checks neither, and `nonce` is not
   checked anywhere. Freshness is left to the caller.
5. **Unauthenticated fields drive the pre-checks.** §4.4 steps 4–7 compare
   `proofPurpose`, `domain` and `challenge` from the unverified parse before
   step 8 authenticates them. This is safe only because the suite then signs
   over the same proof options. Data Integrity does not itself require that
   those members be covered by the signature. The cover comes from the suite's
   proof-configuration step.
6. **The algorithm text has defects, as printed in this REC.** (a) §4.5 step 5
   initialises `combinedVerificationResult.status` to true. Step 6.1 sets
   `.verified` to false on failure. Step 7 then tests `.status`, which as
   written never becomes false. (b) §4.5 step 3.3 builds `inputDocument` with
   `proof` set to `matchingProofs` (the *earlier* proofs), and step 3.4 runs
   §4.4 steps 4–8 "on inputDocument". The proof under verification is never
   placed in `inputDocument`, and §4.4 step 8 as written passes
   `securedDocument`, not `inputDocument`, to `cryptosuite.verifyProof`.
   (c) §4.4 step 2 requires `securedDocument.proof` to be a map, so a proof set
   or chain (a list, §2.1.1–§2.1.2) fails §4.4 and can only go through §4.5.
   (d) `PARSING_ERROR` (§4.4 step 2) and `DATA_LOSS_DETECTION_ERROR` (§2.4.3)
   are used but absent from §4.7's error list. (e) D.2 lists the EdDSA and ECDSA
   suites twice, once as Working Drafts ([DI-EDDSA], [DI-ECDSA]) and once as
   RECs ([VC-DI-EDDSA], [VC-DI-ECDSA]). The errata page listed nothing on
   2026-10-23. The GitHub issue tracker it defers to was not searched.
7. **Proof sets give no threshold and no integrity of membership.** Appendix A
   says so openly. A `Threshold` export (ARCH-0001 §4.1) cannot be expressed as
   a proof set without a holder being able to drop signers. A chain gives
   order, but each link only binds the proofs it names in `previousProof`.
8. **Not `contradicts` with `secure-systems-lab-dsse`, though they disagree.**
   DSSE argues against canonicalisation and against parsing before verifying.
   Data Integrity does both and argues the opposite benefit (§1.2, §5.6), and
   §5.12 concedes that envelope mechanisms that perform no transformations
   "have simplicity advantages in some use cases". Both state a trade-off, and
   neither claims the other is wrong, so `see_also`. The direct contradiction
   is with **R-O-05**, our proposed requirement and not a record, which is why
   no edge carries it. That is the same judgement rfc-8785 made.
9. **Relations, with reasons.** `w3c-rdf-canon-1-0` and `rfc-8785` are the two
   transformations the named suites use (§5.7, §5.12). `w3c-vc-data-model-2-0`
   is the data model Data Integrity secures (§2.6, §5.15). `w3c-vc-jose-cose`
   is the envelope alternative for the same credentials. `secure-systems-lab-dsse`
   is per Limit 8.
10. **Read scope.** This summary was written from the complete stripped source,
    §1–§7 and Appendices A–D. The cryptosuite specs were consulted only for the
    locators in finding item 4. Controlled Identifiers v1.0, which owns
    verification-method retrieval and Multibase, was not read.

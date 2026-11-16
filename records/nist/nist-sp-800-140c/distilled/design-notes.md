---
schema: "library-distilled/v1"
id: nist-sp-800-140c-design-notes
record: nist-sp-800-140c
type: design-notes
updated: "2026-11-15"
---

# NIST SP 800-140C (CMVP approved security functions, withdrawn): design notes for mofn and tmodel

This note covers how SP 800-140C bears on `tmodel:DEC-009`, the record's `bears_on`, and on mofn's cipher suites, which carry the most weight here and which no `bears_on` id names yet.

- **Withdrawn.** The cached PDF opens with NIST's withdrawal notice:

<!-- q L9-15 -->
> Series/Number NIST SP 800-140C Title CMVP Approved Security Functions: CMVP Validation Authority Updates to ISO/IEC 24759 Publication Date(s) March 2020 Withdrawal Date May 20, 2022 Withdrawal Note NIST SP 800-140C is superseded in its entirety by the publication of NIST SP 800-140Cr1.

<!-- q L19-24 -->
> Series/Number NIST SP 800-140Cr1 Title CMVP Approved Security Functions: CMVP Validation Authority Updates to ISO/IEC 24759 Author(s) Kim Schaffer; Alexander Calis Publication Date(s) May 2022 URL/DOI https://doi.org/10.6028/NIST.SP.800-140Cr1

- So the list below is the March 2020 list, withdrawn on 2022-05-20. The library has no record for SP 800-140Cr1 or any later revision (`ls records/nist`), and FIPS 140-3 §3.1 makes the latest revision the one that applies (`fips-140-3` notes). Every finding below is about this edition.
- **Read against** tmodel@ddac1b9 and mofn@10e357f (`SPEC-0002` v0.9.1), as the `fips-140-3` notes are. A tmodel id is written `tmodel:…`; a bare id is mofn's.
- **What it is.** The CMVP's list of approved security functions, which replaces ISO/IEC 19790 Annex C and ISO/IEC 24759 §6.15. Its binding content is the list: one transition document and five categories of functions, each a citation of the standard that specifies it. §6 (L302–L492) contains no verbal form at all, by the `directives` regex over those lines. Random bit generation, key generation and key derivation are not in it; they are SP 800-140D's (`nist-sp-800-140d` notes).
- **Source.** `.cache/nist-sp-800-140c.txt`, sha256 `8acd30094a322c665ac3ef91dbb96b1a42494d4049e564fe7ac141bb06178ccf`, the pinned `source_text_digest`. It renders the PDF whose sha256, `8edf4f1f64bbdf62660f7b1b19f10e95a2d9a5671533530b2eb1dfb9e10dd0f4`, equals `content.sha256` and the skeleton's `source_digest`. All three were recomputed in this pass.
- **Ids.** `R-NNNN` means `nist-sp-800-140c#R-NNNN`; sibling ids are written in full. A script emits every id from the named record's `requirements.yaml`: it selects the entry whose `source_lines` start on a given line, narrowed by a phrase of its text, and raises unless exactly one matches.

## What mofn uses, against this list

Each function mofn names was searched for in `.cache/nist-sp-800-140c.txt` (case-insensitive grep). `SPEC-0002` §6.2 and §12.4 to §12.5 give mofn's suites and digests.

| mofn uses | where | this list | evidence |
|---|---|---|---|
| Ed25519 (PureEdDSA) | suite 1, the default (`SPEC-0002` §6.3); every wallet must support it (`SPEC-0001` §5.2) | **absent**. 0 hits for EdDSA, Ed25519 or Edwards | §6.2.3 cites FIPS 186-4 only, for DSA, RSA and ECDSA (R-0038) |
| ECDSA P-256 | suite 2 and key algorithm 2, reserved and not specified (`SPEC-0002` §6.2, §12.4) | **present**, through FIPS 186-4 | P-256 is FIPS 186-4 D.1.2.3, in the library's verified copy of `fips-186-4` |
| ML-DSA-65 | suite 8, provisional (`SPEC-0002` §6.5) | **absent**. 0 hits for ML-DSA or FIPS 204 | none |
| SHA-256 | every `kid` (`ADR-0005`, DEC-003), statement digests, digest algorithm 1 (`SPEC-0002` §12.5) | **present** | §6.2.4, FIPS 180-4 (R-0039, R-0040) |
| SHA-384 and SHA-512 | digest algorithms 2 and 3; SHA-512 is also inside Ed25519 (`fips-186-5` §7.1) | **present** | §6.2.4, FIPS 180-4 |
| SLH-DSA, ML-KEM, LMS or XMSS | no suite uses them | **absent**. 0 hits for each | none |

<!-- q L406-412 -->
> 6.2.3 Digital Signatures (DSA, RSA and ECDSA) Digital Signature Standard (DSS) National Institute of Standards and Technology (2013) Digital Signature Standard (DSS). (U.S. Department of Commerce, Washington, DC), Federal Information Processing Standards Publication (FIPS) 186-4. https://doi.org/10.6028/NIST.FIPS.186-4

<!-- q L414-417 -->
> 6.2.4 Secure Hash Standard (SHS) Secure Hash Standard (SHS) (SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, and SHA-512/256)

## Adopt

### DEC-003's `kid` hash is on the list (mofn)

This bears on mofn's DEC-003, accepted by `ADR-0005` (`kid` = SHA-256 of the suite's public-key encoding).

- SHA-256 is an approved hash under §6.2.4, so every `kid` mofn computes uses an approved function, in every suite. Nothing changes if a deployment has to run in an approved mode.
- The same holds for statement digests and for target digests under codes 1 to 3. The open sub-question mofn's `ARCH-0001` §7 records under DEC-003 (`ADR-0005`), whether a future suite needs its code in the `kid` preimage, does not touch the hash.

### A statement under an unapproved suite is unverifiable, not invalid (mofn)

This bears on mofn's `SPEC-0002` §6.1.

- `SPEC-0002` §6.1 has a verifier report a statement under an unsupported suite as unverifiable, which is distinct from invalid. A verifier confined to approved functions is such a verifier: under this list it supports none of mofn's specified suites, and it reports suite 1 statements as unverifiable rather than wrong.
- So the verdict needs no change for a deployment restricted to approved functions. What such a deployment lacks is a suite it can verify (Adapt).

## Adapt

### No specified mofn suite is approved under this edition (mofn)

This bears on mofn's `SPEC-0001` §5.2, `SPEC-0002` §6.2 to §6.5, and `ARCH-0001` NG3 (algorithms are not frozen). No DEC decides the suites; the rules are in the SPECs.

- **What cuts against mofn.** `SPEC-0001` §5.2 requires every wallet to support suite 1. Under this list, a wallet confined to approved functions cannot: EdDSA is not here. Suite 8's ML-DSA is not here either. The one mofn key algorithm this list approves, ECDSA P-256, is suite 2, which `SPEC-0002` reserves and does not specify.
- **Three ways to close it:**
  - read FIPS 140-3 ¶10 item a as approving any function a FIPS specifies (FIPS 186-5 §7 for EdDSA, FIPS 204 for ML-DSA), which the `fips-140-3` notes leave open (question 4);
  - read the current revision of this annex, which the library does not hold, to see whether it lists FIPS 186-5 and FIPS 204;
  - specify suite 2 (`ksa-p256-sha256`) and let a wallet in an approved mode offer it instead of suite 1. That needs `SPEC-0001` §5.2 to allow a wallet whose required suite is unavailable in its mode.
- None of this is needed for mofn's targets today; the `fips-140-3` notes record why no validated deployment is open.

### Strict Ed25519 rules have to stay outside any module (mofn)

This bears on mofn's `SPEC-0002` §6.3 (strict key and signature rules, DL-0020).

- `SPEC-0002` §6.3 rejects small-order keys, keys outside the prime-order subgroup, non-canonical encodings and S ≥ L, because library verify functions disagree on exactly those cases.
- FIPS 186-5 §7.7 lets a verifier check either the cofactored equation or the cofactorless one, and treats the key's validity as an input. That was read in the library's `fips-186-5` PDF, fetched for this note, whose sha256 matched `content.sha256`. Two validated EdDSA implementations can therefore disagree on the torsion cases `SPEC-0002` §6.3 closes.
- So a validated module does not deliver §6.3. A wallet that signs or verifies through one must still run §6.3's key and signature checks itself. They need only public data, so they can run outside the module boundary.

### Approval changes over time; keep it out of the suite registry (mofn and tmodel)

This bears on mofn's `SPEC-0002` §6.1 (a suite entry is immutable once the specification leaves 0.x) and on `tmodel:DEC-009` (mitigation lifecycle) and `Evidence.fresh_until` (`tmodel:ADR-0013`).

<!-- q L316-320 -->
> Barker EB, Roginsky AL (2019) Transitioning the Use of Cryptographic Algorithms and Key Lengths. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-131A, Rev. 2. https://doi.org/10.6028/NIST.SP.800-131Ar2 ● Relevant Sections: 1, 2, 3, 9 and 10.

- The list approves functions subject to SP 800-131A Rev. 2 (R-0015, R-0016). That is where key-length and algorithm transitions live, and the restrictions on what §6.2.4 lists, SHA-1 included, are there and not here. The library holds no record for SP 800-131A.
- The list itself was withdrawn and replaced two years after it was published. Whether a function is approved is a property of a date and a revision, not of a suite.
- **mofn.** Do not record approved status in the `SPEC-0002` suite registry. An immutable entry cannot carry a property that changes.
- **tmodel.** A Mitigation such as using approved cryptography is complete only while the list still approves what it uses. Record the list's revision on the RequirementSource built from it (`version`; Evidence's `about_version` is the product's version) and set `fresh_until` from the transition date, where SP 800-131A gives one.

## Reject or hold

### Reject (tmodel): importing this record from its keyword sentences

This bears on the import from the library's requirement format (`tmodel:RPT-0017`, `tmodel:DEC-002`) and on `RequirementSource` (`tmodel:ADR-0013`).

- Every row of the list is binding and none carries a verbal form. The skeleton found one verbal form in the body, in R-0001, the sentence about marking modifications. A converter that keeps only keyword sentences gets that sentence and none of the list. tmodel's own converter (`tmodel:RPT-0017`) also skips an entry whose `normativity` has no tmodel equivalent, which `none` and `possibility` have not, so as written it imports none of this record's entries.
- The rows have to come in as entries without a verb. This record's `requirements.yaml` carries them that way: R-0039 is the SHS row, for example, and R-0035 the SKIPJACK note.
- A RequirementSource for this annex has to be built from the list itself: one member per approved function or category, each with the standard it cites. Each member is a technical Requirement whose text names the function.

### Hold: SKIPJACK

<!-- q L398-400 -->
> NOTE The use of SKIPJACK is approved for decryption only. The SKIPJACK algorithm has been documented in Federal Information Processing Standards Publication (FIPS) 185. This publication is obsolete and has been withdrawn.

- The list approves a function, SKIPJACK decryption, through a FIPS it calls obsolete and withdrawn. Its restriction to decryption is stated only in a NOTE. Neither project uses it; it is recorded because a tmodel import must keep that restriction, and a reader of the NOTE alone would not know it binds.

## Open questions and source defects

### 1. The scope claims evidence methods the document does not have

<!-- q L230-233 "This document also specifies" .. "6.15." -->
> This document also specifies the modification of methods for evidence that a vendor or testing laboratory provides to demonstrate conformity. The approved security functions specified in this document supersede those specified in ISO/IEC 19790 Annex C and ISO/IEC 24759 paragraph 6.15.

- The record contains no vendor-evidence or test-evidence item (0 `VE`/`TE` identifiers by grep). §1 promises modified evidence methods, and §5.2 describes how modifications to TEs and VEs would be marked. The same sentence is in §1 of SP 800-140E and 800-140F, which have no such items either.

### 2. Approval and testing are separate, and this list says nothing about testing

- The list names functions; it never mentions the CAVP. SP 800-140B's security policy template needs a CAVP certificate per approved algorithm, or a vendor affirmation where testing does not exist yet (`nist-sp-800-140b` notes). For mofn the practical question is not only whether EdDSA and ML-DSA are approved but whether the module it would use has a certificate for them.

### 3. Pass 3 joins: what our artifacts do not yet agree on

These are differences between our own artifacts, found by script in the cross-check. None is a source defect.

- `requirements.yaml` `field`: 61 entries. 10 stated entries name no structure, step or state and keep a descriptive `field`: what they constrain is real, but no message structure, flow step or state models it (the notation of §5.2, editions, definitions, and R-0058, the withdrawal status). The 2 inferred entries R-0060 and R-0061 keep a `field` (§6.2.2, §6.2.1) and no field cites them; each rests on stated entries in its `derived_from`.
- `messages.yaml`: 94 citations from 1 structure and 12 fields. 4 cite an entry whose lines overlap the field's, 12 one that overlaps the structure's, 22 one within 40 lines, and 56 were read: they are the per-function reference entries of §6.2.2 to §6.2.6, each in the clause its `group` names. 22 had no word in common with their field and were read too.
- The record has no protocol or state machine, so no work product, step or guard joins here.

---
schema: "library-distilled/v1"
id: nist-sp-800-140d-design-notes
record: nist-sp-800-140d
type: design-notes
updated: "2026-11-15"
---

# NIST SP 800-140D (CMVP approved SSP generation and establishment methods, withdrawn): design notes for mofn and tmodel

This note covers how SP 800-140D bears on `tmodel:DEC-009`, the record's `bears_on`, and on how mofn generates, derives and protects keys, which no `bears_on` id names yet.

- **Withdrawn.** The cached PDF opens with NIST's withdrawal notice:

<!-- q L9-15 -->
> Series/Number NIST SP 800-140D Title CMVP Approved Sensitive Parameter Generation and Establishment Methods: CMVP Validation Authority Updates to ISO/IEC 24759 Publication Date(s) March 2020 Withdrawal Date May 20, 2022 Withdrawal Note NIST SP 800-140D is superseded in its entirety by the publication of NIST SP 800-140Dr1

- So the list below is the March 2020 list, withdrawn on 2022-05-20 in favour of SP 800-140Dr1 (L19–L24). The library has no record for Revision 1 or any later revision (`ls records/nist`), and FIPS 140-3 §3.1 makes the latest revision the one that applies (`fips-140-3` notes).
- **Read against** tmodel@ddac1b9 and mofn@10e357f, as the `fips-140-3` notes are. A tmodel id is written `tmodel:…`; a bare id is mofn's.
- **What it is.** The CMVP's list of approved methods for generating and establishing sensitive security parameters (SSPs: keys and other secrets). It replaces ISO/IEC 19790 Annex D and ISO/IEC 24759 §6.16. Its binding content is the list, and §6 (L298–L396) contains no verbal form at all, by the `directives` regex over those lines.
- **Source.** `.cache/nist-sp-800-140d.txt`, sha256 `95ac95faa07ee2f149b7a7fdd0a7c16d38746695fc338b145e769c6ff73db7d2`, the pinned `source_text_digest`. It renders the PDF whose sha256, `23a9f6798c641653ca999b5a19838204f6e61ea58b42b21303bdfc00d2c20f0b`, equals `content.sha256` and the skeleton's `source_digest`. All three were recomputed in this pass.
- **Ids.** `R-NNNN` means `nist-sp-800-140d#R-NNNN`. A script emits every id from `requirements.yaml`: it selects the entry whose `source_lines` start on a given line, narrowed by a phrase of its text, and raises unless exactly one matches.

## The list is closed

<!-- q L303-305 -->
> This document identifies CMVP-approved sensitive security parameter generation and establishment methods. It precludes the use of all other sensitive security parameter generation and establishment methods.

Unlike SP 800-140C, which supersedes the annex it replaces, this list excludes everything it does not name: a method not on it is precluded, not merely unlisted. SP 800-140B's tables show where a precluded algorithm can still appear, in services outside the approved mode (SP 800-140B's Non-Approved Algorithms Not Allowed table in B.2.2 and its Non-Approved Services table in B.2.4). That makes the mofn items below stronger than their SP 800-140C counterparts.

## Adopt

Nothing. Neither project uses a method on this list as mofn specifies it today, and tmodel uses none of its own. Every item below is a cost or a change, so it is under Adapt or Reject or hold.

## Adapt

### Key generation: Ed25519 key pairs are not on the list (mofn)

This bears on mofn's `SPEC-0002` §6.3 (suite 1's keys), `SPEC-0001` §5.2 and `ARCH-0001` NG3. No DEC decides the suites.

<!-- q L319-323 -->
> 1. National Institute of Standards and Technology (2013) Digital Signature Standard (DSS). (U.S. Department of Commerce, Washington, DC), Federal Information Processing Standards Publication (FIPS) 186-4. https://doi.org/10.6028/NIST.FIPS.186-4 • DSA, RSA, and ECDSA.

<!-- q L331-333 -->
> Note. For the purposes of the key establishment techniques, the Digital Signature Standard is only used to define the domain parameters and the (private, public) key-pair generation.

- The list's key-pair generation is FIPS 186-4's, for DSA, RSA and ECDSA, plus key generation by SP 800-133 Rev. 1 and random bits by SP 800-90A Rev. 1 with SP 800-90B entropy sources (L377–L393). FIPS 186-4 has no EdDSA (`nist-sp-800-140c` notes).
- So under this edition a module in an approved mode cannot generate a suite 1 key, and §6.1 forbids it from using another method instead. This is the same gap as in SP 800-140C, on the generation side, and it closes the same ways.

### Protecting keys at rest: the list names one password-based derivation (mofn)

This bears on mofn's `PLAN-0004` §6.1 (proposed: each private key file is encrypted at rest with a passphrase-based key) and §6.2 (engine v0 does it with Argon2id and libsodium SecretBox). Neither is a DEC.

<!-- q L355-358 -->
> 5. Sönmez Turan M, Barker EB, Burr WE, Chen L (2010) Recommendation for Password-Based Key Derivation: Part 1: Storage Applications. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-132. https://doi.org/10.6028/NIST.SP.800-132

- SP 800-132 is the list's only password-based key derivation, and it is for storage applications, which is what a key file is. Argon2id is not on the list (0 hits), and §6.1 precludes methods not on it. The symmetric ciphers SP 800-140C lists are AES, TDEA and SKIPJACK. libsodium's SecretBox is XSalsa20 with Poly1305, and neither name occurs in SP 800-140C or this record (0 hits each).
- SP 800-140's TE09.30.04 accepts a plaintext SSP that is not zeroised only if it is encrypted with an approved algorithm or kept inside an embedded validated module (nist-sp-800-140#R-0126). Engine v0's key files would meet neither.
- **This does not cut against a decision.** `PLAN-0004` §6.1 picks no mechanism, and §6.2 records what engine v0 does. If an approved mode is ever a goal, the candidates narrow to SP 800-132 with an approved AES mode, wrapping by SP 800-38F (L373–L375) where a key is wrapped rather than encrypted. Until then nothing here asks mofn to change.

### Deriving keys from a seed (mofn)

This bears on mofn's `ARCH-0003` §3.3 (custody `derived(seed, path)`), `ARCH-0003` W-11 and `SPEC-0001` §5.3 (a separate key per protocol, derived from one seed where convenient).

<!-- q L351-353 -->
> 4. Chen L (2009) Recommendation for Key Derivation Using Pseudorandom Functions (Revised). (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-108, Revised. https://doi.org/10.6028/NIST.SP.800-108

- mofn specifies no derivation for `derived(seed, path)`. In an approved mode it would have to be one of the list's methods: SP 800-108's derivation from a pseudorandom function (quoted), or SP 800-133 Rev. 1's key generation (L377–L379). A scheme of mofn's own, or one from another ecosystem, would be precluded by §6.1.
- The choice is cheapest before `derived(seed, path)` is specified: changing it later changes every derived key.

### A key exchange, if mofn ever adds one (mofn)

This bears on mofn's `ARCH-0003` §3.3 (`CipherSuite.key_exchange` stays empty until a transport needs it) and `SPEC-0001` §8.2.

- The list's key establishment schemes are SP 800-56A Rev. 3 (discrete logarithm), SP 800-56B Rev. 2 (integer factorisation) and SP 800-56C's key derivation (L335–L371). HPKE and X25519, which mofn's cipher-suite research surveyed, do not appear (0 hits each), and mofn already names HPKE (RFC 9180) for the provisional wallet-to-wallet mailbox (`SPEC-0001` §8.2, `ARCH-0003`): that item is outside this list as written.
- Nothing to do now: the slot is empty by design. A transport that must run in an approved mode would have to fill it from this list.

### The list moves over time (tmodel)

This bears on `tmodel:DEC-009` (mitigation lifecycle), `RequirementSource.version` and `Evidence.fresh_until` (`tmodel:ADR-0013`).

<!-- q L311-315 -->
> Barker EB, Roginsky AL (2019) Transitioning the Use of Cryptographic Algorithms and Key Lengths. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-131A, Rev. 2. https://doi.org/10.6028/NIST.SP.800-131Ar2 ● Sections relevant to this Annex: 1, 5, 6, 7, and 8.

- As in SP 800-140C, the approved methods are subject to SP 800-131A Rev. 2, here sections 1 and 5 to 8, and the library holds no record for SP 800-131A.
- A RequirementSource for this annex is one member per listed method, each a technical Requirement citing its standard, pinned to the revision read. The list was replaced two years after it was published, so a Mitigation that rests on it needs Evidence with `fresh_until`.

## Reject or hold

### Reject (tmodel): importing this record from its keyword sentences

- Every listed method is binding and none carries a verbal form; the skeleton found one in the body, in R-0001, about how modifications are marked. A converter that keeps only keyword sentences gets that sentence and none of the list (as for SP 800-140C).

### Hold: nothing here asks mofn to change today

- `PLAN-0004` keeps keys as files with no keychain product and no cloud custody, and the `fips-140-3` notes record why no validated deployment is open. Every Adapt item above is the cost of one, written down so that a later decision can weigh it.

## Open questions and source defects

### 1. Two editions of SP 800-56C side by side

<!-- q L364-371 -->
> 7. Barker EB, Chen L, Davis R (2018) Recommendation for Key-Derivation Methods in Key-Establishment Schemes. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-56C, Rev. 1. https://doi.org/10.6028/NIST.SP.800-56Cr1 8. Chen L (2011) Recommendation for Key-Derivation through Extraction-then-Expansion. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-56C. https://doi.org/10.6028/NIST.SP.800-56C

- Item 7 is SP 800-56C Rev. 1 (2018) and item 8 the original SP 800-56C (2011). A revision normally replaces its predecessor; the list approves both. A RequirementSource has to keep both as members until the current revision says otherwise.

### 2. The heading covers half the list

- §6.2.2 is headed Key Establishment Techniques, but items 10 to 12 are key generation, random bit generation and entropy sources. The title of the document says generation and establishment; the heading keeps only the second.

### 3. A binding restriction in a note

- The Note under item 1 (L331–L333) limits FIPS 186-4 to domain parameters and key-pair generation. It is the only text that says so. A tmodel import must keep it with item 1.

### 4. The cover drops a word of the title

- The withdrawal notice calls the document Approved Sensitive Parameter Generation and Establishment Methods (L10), and its successor likewise (L20). The title page says Sensitive Security Parameter (L42–L44), as do the abstract and §1.

### 5. Pass 3 joins: what our artifacts do not yet agree on

These are differences between our own artifacts, found by script in the cross-check. None is a source defect.

- `requirements.yaml` `field`: 34 entries. 9 stated entries name no structure, step or state and keep a descriptive `field`: what they constrain is real, but no message structure, flow step or state models it (the notation of §5.2, editions, definitions, and R-0031, the withdrawal status). The 2 inferred entries R-0032 and R-0033 keep a `field` and no field cites them; each rests on stated entries in its `derived_from`.
- `messages.yaml`: 64 citations from 1 structure and 10 fields. 4 cite an entry whose lines overlap the field's, 12 one that overlaps the structure's, 16 one within 40 lines, and 32 were read: they are the numbered method entries of §6.2.2, cited by `ordinal` and `reference`, and §1 and §6.1 for the structure as a whole.
- The record has no protocol or state machine, so no work product, step or guard joins here.

---
record: rfc-9162
kind: design-notes
title: "rfc-9162 — bearing on our design"
extracted: "2026-11-08"
reviewed_by: ""
---

# RFC 9162 (Certificate Transparency 2.0) — bearing on our design

RFC 9162 is **Experimental** (front page, L8), December 2021, and obsoletes RFC
6962 (L7). Source: `.cache/rfc-9162.txt`, sha256
`a0e432ce7580c99fcc8faf0cf3f6191f9ce6b4864f949158e020d4ecb295081f`, equal to
`content.sha256` in `record.yaml` and recomputed from `.cache/` in this pass.
`bin/bcp14-count` finds 138 keywords; `bin/fx1-skeleton` wrote the sentences
carrying them into `requirements.yaml` as `rfc-9162#R-0001` to `R-0125`, the
only ids this file cites.

It defines a log as one append-only Merkle tree, the two proofs over it, the
signed objects a log emits (SCT, STH), the TLS-presentation-language structs
they are made of, an HTTPS/JSON client API, and how TLS servers, CAs and
clients carry the results. **It does not define** how a client learns a log's
parameters, how logs are trusted, or how views are compared between clients
(gossip). It names that last gap as the reason a log must still be trusted.

It reaches us in four ways.

1. **R-O-04** (Could): *"Optional registration of statements with a SCITT-like
   transparency service (RFC 9943)."* (`spec/ARCH-0001-authorization-attestation.md@bb005ed`
   §5.3). The library's `rfc-9942` record points its RFC9162_SHA256 tree at this
   document's §2.1; that tree and its two proofs are what a SCITT receipt
   verifier would run. mofn report R-0006 §2.4 says of them: *"Every claim about
   what a proof guarantees is therefore inherited from RFC 9162 and not checked
   here"* (`research/0006-mechanism/report.md@bb005ed`). §4 below checks them.
2. **R-M-12**, relocated to `ARCH-0002` P1 by `ADR-0001`. CT 2.0 replaced a
   key-hash log identifier with an OID from an IANA registry or a private arc.
   That is the kind of move P1 rejects for extension points, made by a
   deployed-lineage protocol, and the bytes show what the allocated name is and is not trusted for (§3, A-07, K-03).
3. **DEC-002, accepted by `ADR-0004` (option 5), and MD-3.** CT signs
   fixed-layout TLS presentation-language structs and runs no canonicaliser.
   That is evidence about the canonicality conditions, in both directions. §5
   gives it, including where it cuts against option 5.
4. **R-O-05 and `SPEC-0002` §6.4** (authenticated type indicator, domain
   separation). CT tags the signed input of an SCT and does not tag the signed
   input of an STH. §6 settles from the byte layouts whether that matters.

What it is not: a statement format, a delegation model, or a trust model.
Applied to us it is an interchange and evidence mechanism (`ARCH-0001` §6 row
*SCITT receipt*: import, could-export, *"evidence attached to an attestation"*).

## Things to hold while reading

1. **Our decisions are read from m-of-n at `bb005ed`**
   (`bb005ed9e94b7aa9936c9a82077829e7b85d3eae`, HEAD on 2026-11-08), with
   `git -C /Users/nfn/Projects/mofn show bb005ed:<path>`, never from the working
   tree. A quotation of ours is typed, italicised, and located `<path>@bb005ed`;
   every one was resolved by script against that blob. Pass 2 re-ran it over
   all 50: 39 resolve with whitespace collapsed, and the other 11 only once the
   blob's Markdown emphasis, backticks or blockquote markers are also removed
   (the words are exact in all 50; each sits in the section it is attributed to).

   | name | path at bb005ed | standing at bb005ed |
   |---|---|---|
   | ARCH-0001 v0.2.0 | `spec/ARCH-0001-authorization-attestation.md` | draft. §5 rows, §6 matrix, §7 decisions. NG4: *"Require a blockchain or any specific transparency log."* is a non-goal |
   | ARCH-0002 v0.10.0 | `spec/ARCH-0002-key-relative-naming.md` | draft. P1 accepted (`ADR-0001`); P2, P3, P5, P5.1, P5.2, P6 accepted (`ADR-0002`); P4, P7, P1.1 draft; DEC-008, DEC-009 open |
   | ADR-0001 | `spec/ADR-0001-key-relative-naming.md` | accepted; R-M-12 becomes `ARCH-0002` P1 |
   | ADR-0004 | `spec/ADR-0004-dec-002-encoding.md` | **accepted 2026-10-25**: DEC-002 is option 5. *"an accepted ADR changes only by superseding it"*; `reviewed: false` |
   | ADR-0005 | `spec/ADR-0005-dec-003-key-identifier.md` | accepted; `kid` is SHA-256 of the suite's public-key encoding |
   | SPEC-0002 v0.5.0 | `spec/SPEC-0002-ksa-core.md` | draft; governs where it and an ARCH differ (`ADR-0003`) |
   | MD-3 | `project/meetings/2026-09-28.md` | the 2026-09-28 narrowing to option 5. `ADR-0004`: *"MD-3's narrowing is closed by acceptance"* |
   | mofn report R-0006 v0.3.0 | `research/0006-mechanism/report.md` | draft, *"Evidence only — it decides nothing."* Pinned to `library@60b3284`, when this record was a stub |
   | PLAN-0001, BACKLOG-0001 | `project/PLAN-0001-project-plan.md`, `project/BACKLOG-0001.md` | transparency deferred: T-092 *"R-O-04 is `Could`; not in the demo floor"* |

   **`docs/extraction.md` is stale on one point**, as the `w3c-vc-jose-cose`
   design notes already recorded: it says no DEC-002 ADR exists. At `bb005ed`
   `ADR-0004` accepts DEC-002 for option 5. This file maps against `ADR-0004`,
   and still records where the source cuts against option 5, because an
   accepted ADR is superseded, not patched, and only evidence can supersede it.

2. **Numbering.** A bare `R-NNNN` is `rfc-9162#R-NNNN`; mofn's research report
   R-0006 is not `rfc-9162#R-0006` and is always written *mofn report R-0006*.
   Every id below was
   emitted from `requirements.yaml` by script and its text read beside the
   claim it supports (§9 lists the joins). `R-M-NN`, `R-I-NN`, `R-O-NN` are
   `ARCH-0001` §5. `P1` … `P7`, `P5.1`, `P5.2` are `ARCH-0002`. `V1` … `V9` are
   `SPEC-0002` §9.2. "Condition (n)" is one of the six conditions of mofn report
   R-0006 §3.2. `MD-n` are dated meeting decisions. Row ids here are `A-nn`
   adopt, `D-nn` adapt, `X-nn` reject, `C-nn` constrains, `K-nn` conflicts,
   `S-nn` silent.

3. **Quotation.** No word of RFC 9162 is typed here. Each quotation is a
   `<!-- q Lx-y -->` marker whose blockquote `bin/check-quotes --render` wrote.
   Elsewhere a source passage is cited as `§n Lx-y` and paraphrased, and a
   paraphrase is never set in quotation marks. RFC 6962 and RFC 5280 facts are
   stated with their section and are not quoted.

4. **Labels.** *(inferred)* marks a consequence the source does not state.
   **Ours** marks a proposal of this library. A number carries the method that
   produced it; the scripts are listed in §9.

---

## 1. Rows by verdict

31 rows: **8 adopt, 4 adapt, 4 reject, 7 constrains, 3 conflicts, 5 silent**.
*Adopt (confirms)* means the source does what an accepted decision of ours
already does, and is recorded as independent evidence for it, not as a new
commitment. Nothing here changes a decision; §10 says so.

| id | verdict | in RFC 9162 | where | ids | maps to | finding |
|---|---|---|---|---|---|---|
| A-01 | adopt | Merkle Tree Hash: leaf `HASH(0x00 ‖ d)`, node `HASH(0x01 ‖ l ‖ r)`, split at the largest power of two below n; the shape is fixed by n | §2.1.1 L329-362 | — | R-O-04; `ARCH-0001` §6 *SCITT receipt*; `SPEC-0002` §6.4 (the same separation, at the signature) | §4 check 7: without the two prefixes a 2-entry list forges a 4-entry root; with them it does not |
| A-02 | adopt | PATH and PROOF, and the verification algorithms of §2.1.2, §2.1.3.2, §2.1.4.2 | §2.1.2–§2.1.4 L364-578 | — | R-O-04 | §4: 8,515 inclusion and 8,385 consistency proofs (n ≤ 130) verify; the 7-leaf example reproduces |
| A-03 | adopt | Proofs are unsigned and verified against a signed head, whose size and root are signed together | §5.3 L1475-1476; §5.4 L1523-1524; §5.5 L1594-1596 | R-0115, R-0116 | R-O-04; R-O-05 (the verified bytes are the used bytes) | §4 checks 5, 5b, 9b, 9c: with the head's own size, no wrong index passes; with a size taken from anywhere else, wrong sizes and indices do. See S-04 |
| A-04 | adopt (confirms) | The log signs the exact bytes that become the leaf, and the leaf hash excludes the signature | §4.7 L1041-1046; §4.8 L1112-1115 | — | `SPEC-0002` §4.5, §5, §13.3 | the signed object and the identified object are one byte string in both designs |
| A-05 | adopt (confirms) | A type code names one immutable structure; a changed structure takes a new code | §4.5 L1012-1015; §10.2.3 L2297-2299 | — | `SPEC-0002` §12 (append-only registries); `ARCH-0003` W-12 | — |
| A-06 | adopt (confirms) | One signature and one hash algorithm per log, for life; deprecating one freezes the log and starts another | §9 L2115-2134; §4.13 L1232-1259 | R-0060, R-0122, R-0123 | `SPEC-0002` §6.1–§6.2, §8.8 `rotate`; `ADR-0005` item 3 | a new algorithm is a new key, as in KSA. CT puts no algorithm identifier in any signed object (X-04) |
| A-07 | adopt (confirms) | The key is the security identity: no signature covers `log_id`; one keypair per log is what makes that safe; the CA is bound inside the signed bytes by a key hash | §4.1 L829-830; §4.7 L1064-1071; §4.8 L1112-1115; §4.10 L1180-1181 | R-0028, R-0044 | `ADR-0005`; `ARCH-0002` P1.1, P5.2; R-O-01, R-M-02 | §3 |
| A-08 | adopt (confirms) | Without view comparison a log is a trusted third party, and a signed timestamp does not guarantee that anyone monitored | §1 L213-219; §11 L2554-2562 | — | `ARCH-0001` §6 *SCITT receipt*; R-I-02; NG4; mofn report R-0006 §2.4 | the source's own words for R-0006 §2.4's reading |
| D-01 | adapt | Extension vectors: no repeated type, ascending by type | §4.8 L1103-1106; §4.9 L1140-1143 | R-0045, R-0046, R-0050, R-0051 | condition (5); `ADR-0004` *Not decided here*; mofn report R-0006 §3.13; P5.1 | the rule's shape (distinct, totally ordered) is what `trusts`, `allow-keys` and `exclude-keys` lack. CT binds producers only and verifies the bytes as sent, so P5.1's rejection must be added |
| D-02 | adapt | An SCT is a signed promise to include within the MMD; inclusion is proved separately and later | §4 L792-806; §4.1 L834-836; §11.3 L2596-2600 | R-0024, R-0114, R-0115 | R-O-04; `ARCH-0001` §4.3 step 3; mofn report R-0006 §2.4 | two kinds of transparency evidence of different strength; a promise needs a later audit |
| D-03 | adapt | Signatures as a tracking channel: one SCT per submission and one STH per tree size, or deterministic signatures; a cap on STH rate | §4 L782-786; §4.10 L1153-1156; §11.3 L2611-2620 | R-0023, R-0056, R-0125 | `SPEC-0002` §14, §6.3, §6.5, §13.3 | `SPEC-0002` says nothing on signature determinism (open question 6) |
| D-04 | adapt | Four audit properties, checked apart from SCT validation | §8.3 L2074-2083 | R-0119, R-0120, R-0121 | R-O-06; `SPEC-0004` §10.4 | *(inferred)* transparency evidence would be its own verdict line, never folded into *acceptance* |
| X-01 | reject | Rebuild the signing input at verification: the TransItem from parts, the TBSCertificate from the final certificate | §8.1.2 L1919-1934; §8.1.3 L1938-1966 | R-0113 | R-O-05; condition (3); `SPEC-0002` §5, §13.1 | §5.3: CT needs it because an embedded SCT cannot carry the bytes it signs |
| X-02 | reject | An STH signature over an untagged struct | §4.9 L1121-1128; §4.10 L1180-1181 | — | R-O-05; condition (4); `SPEC-0002` §6.4 | §6: safe today by a numeric accident, not by construction |
| X-03 | reject | Certificate machinery: CMS precertificates, the TLS extension, the X.509v3 and OCSP extensions | §3.2; §6; §7; §8.1.1; §8.1.6 | R-0007–R-0021, R-0090–R-0112, R-0118 | R-M-01; NG1 | not ours to carry |
| X-04 | reject | No algorithm identifier in any signed object; algorithms live only in out-of-band log parameters | §4.1 L824-831; §4.8 L1112-1115 | R-0001 | `SPEC-0002` §6.1; R-O-05 | it works for CT only because a log's parameters are immutable and configured (C-01) |
| C-01 | constrains | Verifying any CT object needs the log's key, hash, signature algorithm and MMD from configuration | §8 L1899-1903; §4.1 L813-816 | R-0026 | `ARCH-0002` DEC-008; `ARCH-0001` §4.3; `SPEC-0004` §4 | a fixed floor, as DEC-008's proposed answer says (S-02) |
| C-02 | constrains | A consistency proof binds only the two heads its verifier holds | §2.1.4 L475-483; §8.3 L2108-2111 | R-0116 | R-O-04; NG4 | §4 check 9: two forks of one prefix both verify |
| C-03 | constrains | Equal sizes and the empty tree sit outside the consistency algorithm | §2.1.4.1 L487-489; §2.1.4.2 L535-542; §5.3 L1468-1470 | R-0076 | R-O-04 | §4 check 8: an empty path fails step 1, and §5.3 returns an empty path for equal sizes |
| C-04 | constrains | Freshness: the MMD has no bound in the document; a served STH may be an MMD old; a misissued certificate may go unaudited for twice the MMD | §4.1 L834-836; §4.10 L1151-1153; §11.1 L2575-2578 | R-0055 | R-M-09; R-O-02; `SPEC-0002` §7.3; mofn report R-0006 §2.4 | the age rule binds the log's own `get-sth`, not an STH relayed by someone else |
| C-05 | constrains | CT key hashes are SubjectPublicKeyInfo DER under the log's HASH | §4.7 L1064-1071 | R-0044 | `ADR-0005` items 3–4; P1; R-I-01 | the two alternatives `ADR-0005` rejected, in one field; a `kid` never equals one, so an importer recomputes (§3) |
| C-06 | constrains | Logging is irrevocable publication | §4 L777-778, L808-809; §11.5 L2630-2634 | R-0025 | R-O-04; `SPEC-0002` §14 | *(inferred)* registration has to stay optional per statement; R-O-04 makes it optional, not per statement |
| C-07 | constrains | Timestamps are uint64 milliseconds since 1970, leap seconds ignored | §4.7 L1057-1061 | — | `SPEC-0002` §4.4; R-I-01 | an import into KSA time drops the milliseconds and must take the day form at midnight |
| K-01 | conflicts | Ignore what is not understood: SCT and STH extensions, JSON fields, unknown TransItem types, non-v2 SCTs | §4.8 L1106-1110; §4.9 L1143-1146; §5 L1279-1281; §5.1 L1413-1416; §5.6 L1630-1637 | R-0047, R-0048, R-0052, R-0053, R-0061, R-0069, R-0079 | `ARCH-0002` P5, P5.2; `SPEC-0002` §13.5 | hashing an unknown leaf as opaque tree input is traversal, which P5's note allows; accepting an unknown extension is not |
| K-02 | conflicts | Registry-allocated extension points, four of the six registries with experimental and private-use ranges | §10.2.1–§10.2.4; §10.2.6 | — | `ARCH-0002` P1; `ADR-0004` item 3 | natively excluded; at an import boundary the CT registries join `ADR-0004` item 3's list |
| K-03 | conflicts | The Log ID became an OID, self-allocated under an arc or taken from an IANA First Come First Served registry, replacing v1's key hash | §1.3 L259-261; §4.4 L939-963; §10.2.5 L2399-2448 | R-0041, R-0042, R-0043, R-0124 | R-M-12 → `ARCH-0002` P1 (`ADR-0001`); `ADR-0005` | §3: the allocated name sits outside every signature; no security rests on it |
| S-01 | silent | Gossip: how clients compare STHs to detect split views and rate violations | §11.3 L2602-2609; §1 L213-219 | — | R-O-04; NG4 | the source names it as the residual trust in the log |
| S-02 | silent | How log parameters are distributed, updated, trusted and distrusted | §8 L1899-1903; §6.2 L1765-1767; §4.13 L1241-1243 | — | `ARCH-0002` DEC-008; `SPEC-0004` §4 | out of band throughout |
| S-03 | silent | A compromised log key: no revocation and no rotation; parameters are immutable and freezing is the only transition | §4.1 L813-816; §4.13 L1248-1254; §6.2 L1774-1779 | R-0026 | R-O-02; `SPEC-0002` §8.7 `revoke`, §8.8 `rotate` | *(inferred)* a compromised key can sign any head, and nothing in the protocol withdraws it |
| S-04 | silent | No client rule ties a proof's own `tree_size` and `log_id` to the head it is checked against | §2.1.3.2 L436-440; §4.11 L1189-1194; §4.12 L1212-1217 | — | R-O-04 | §4 checks 5 and 9b: what an implementer who trusts the proof's size gets |
| S-05 | silent | Which signed inputs must be distinguishable from which; no security consideration addresses signature confusion | §11 | — | R-O-05; `SPEC-0002` §13.2 | §6 |

---

## 2. Row details

Source passages are markers rendered by `bin/check-quotes`. Each row's
`finding` above is argued here or in the section it names.

### 2.1 Adopt

**A-01 — the tree hash and its domain separation.** The one sentence of
rationale the source gives for the prefixes:

<!-- q L354-355 -->
> Note that the hash calculations for leaves and nodes differ; this domain separation is required to give second preimage resistance.

and the property every proof relies on:

<!-- q L357-359 "Note that we do not require" .. "number of leaves." -->
> Note that we do not require the length of the input list to be a power of two. The resulting Merkle Tree may thus not be balanced; however, its shape is uniquely determined by the number of leaves.

Both checked in §4 (checks 6 and 7). Ours: `SPEC-0002` §3 property 2 makes the
same move one layer up, *"Every signature covers a label naming what is being
signed (§6.4), so a signature over a statement cannot be presented as a
signature over anything else."* (`spec/SPEC-0002-ksa-core.md@bb005ed`). CT
separates its two hash inputs and, §6 shows, not its two signature inputs.

**A-02 — the proof algorithms.** A receipt verifier for the RFC9162_SHA256
tree (R-O-04) runs §2.1.3.2 and §2.1.4.2 exactly as written. They contain no
BCP 14 keyword and each is introduced as a procedure a client can use, so an
implementation that verifies some other way conforms. **Ours:** if R-O-04 is
ever built, these two algorithms and the §2.1.5 example are its first fixtures.

**A-03 — unsigned proofs, signed heads.** The source is explicit that a proof
carries no signature because the head does:

<!-- q L1475-1476 -->
> Note that no signature is required for the consistency output, as it is used to verify the consistency between two signed STHs.

<!-- q L1523-1524 -->
> Note that no signature is required for the inclusion output, as it is used to verify inclusion in the selected STH, which is signed.

The head's signature covers `tree_size` and `root_hash` together (§4.9
L1123-1128, §4.10 L1180-1181). §4 shows that this pairing is the whole of the
binding: a proof checked against the head's own size cannot move a leaf, and a
proof checked against a size from anywhere else can (checks 5, 5b, 9b, 9c).
Every client rule that calls for checking a proof against a head is a SHOULD
or a MAY (R-0115, R-0116, R-0117; the monitor procedures of R-0120 and
R-0121). Ours: R-O-05's discipline, that what is verified is what is used,
applied to sizes.

**A-04 — sign the leaf.** The SCT's signature and the leaf hash are computed
over the same TransItem:

<!-- q L1112-1115 -->
> signature is computed over a TransItem structure of type x509_entry_v2 or precert_entry_v2 (see Section 4.7) using the signature algorithm declared in the log's parameters (see Section 4.1).

<!-- q L1044-1046 "Note" .. "parameters." -->
> Note that leaf hashes are calculated as HASH(0x00 || TransItem), where the hash algorithm is one of the log's parameters.

So the log's signature and the tree's identifier are computed over the same
TransItem bytes (the hash with its `0x00` prefix), and the identifier excludes
the signature. Ours: *"Statements are
content-addressed by the digest of their TBS, not of their signature, so
signature malleability cannot change a statement's identity"*
(`spec/SPEC-0002-ksa-core.md@bb005ed` §13.3).

**A-05 — immutable type codes.**

<!-- q L1012-1015 -->
> Future versions of this protocol may reuse VersionedTransType values defined in this document as long as the corresponding data structures are not modified and may add new VersionedTransType values for new or modified data structures.

Ours: *"A code or name, once assigned, MUST NOT be reassigned or reused"*
(`spec/SPEC-0002-ksa-core.md@bb005ed` §12), and `ARCH-0003` W-12, *"Definitions
are immutable; a change is a new `DefinitionId` linked by `supersedes` from the
same definer."* (`spec/ARCH-0003-wallet-object-model.md@bb005ed`). CT and KSA
version by new code, never by edit.

**A-06 — algorithm fixed per key; deprecation is a new key.**

<!-- q L2125-2128 -->
> Allowing multiple signature or hash algorithms for a log would require that all data structures support it and would significantly complicate client implementation, which is why it is not supported by this document.

<!-- q L2130-2132 "If it should" .. "be started." -->
> If it should become necessary to deprecate an algorithm used by a live log, then the log MUST be frozen, as specified in Section 4.13, and a new log SHOULD be started.

KSA reaches the same place by a different road: one suite per key
(`SPEC-0002` §6.1), a new algorithm is a new key and a new `kid`, and the old
key's statements stay verifiable. `ADR-0005` item 3 takes the same line for the
identifier's digest: *"Agility, when needed, comes from a new identifier
version, not from a per-suite choice."*
(`spec/ADR-0005-dec-003-key-identifier.md@bb005ed`). A frozen log's Final STH
(§4.1 L847-853, R-0029) seals what the old key signed, so that additions after
it are detectable. KSA's nearest counterpart, `rotate` (`SPEC-0002` §8.8), is
signed by the old key and names the new one; a frozen CT log names no
successor, and clients learn of the new log out of band (§4.13 L1241-1243).
The other difference is X-04.

**A-07 — the key is the identity.** Three facts from the bytes. No signature
CT defines covers `log_id`: the SCT signs a TransItem with no `log_id` field
(§4.7 L1050-1055, §4.8 L1112-1115), and the STH signs only `tree_head`:

<!-- q L1180-1181 -->
> signature is computed over the tree_head field using the signature algorithm declared in the log's parameters (see Section 4.1).

What makes that safe is a rule about keys, not about names:

<!-- q L829-830 -->
> Public Key: The public key used to verify signatures generated by the log. A log MUST NOT use the same keypair as any other log.

And where CT does need to bind an identity into the signed bytes, it uses a
key hash, not a name:

<!-- q L1064-1071 "issuer_key_hash is the HASH" .. "matches tbs_certificate." -->
> issuer_key_hash is the HASH of the public key of the CA that issued the certificate or precertificate, calculated over the DER encoding of the key represented as SubjectPublicKeyInfo [RFC5280]. This is needed to bind the CA to the certificate or precertificate, making it impossible for the corresponding SCT to be valid for any other certificate or precertificate whose TBSCertificate matches tbs_certificate.

Ours: `ADR-0005` (*"the key is the principal (R-M-02), whichever suite it signs
under"*, `spec/ADR-0005-dec-003-key-identifier.md@bb005ed`), and P1.1, *"the
principal travels in the payload, never in a foreign `kid`."*
(`spec/ARCH-0002-key-relative-naming.md@bb005ed`). §3 takes this further.

**A-08 — a log is trusted until views are compared.**

<!-- q L213-219 -->
> The log auditing mechanisms described in this document can be circumvented by a misbehaving log that shows different, inconsistent views of itself to different clients. Therefore, it is necessary to treat each log as a trusted third party. While mechanisms are being developed to address these shortcomings and thereby avoid the need to blindly trust logs, such mechanisms are outside the scope of this document.

<!-- q L2560-2562 -->
> A signed timestamp does not guarantee this, though, since appropriate monitors might not have checked the logs or the CA might have refused to revoke the certificate.

Ours: the §6 matrix row, *"Does not change meaning of statement"*, and R-I-02,
*"Import SHALL NOT require the foreign object to become a native trust
anchor."* (`spec/ARCH-0001-authorization-attestation.md@bb005ed`). mofn report
R-0006 §2.4 reached *"A receipt is evidence about a statement's publication,
never about its authority"* (`research/0006-mechanism/report.md@bb005ed`) from
RFC 9942 and RFC 9943; this is the same conclusion in CT's own words, and from
the older document.

### 2.2 Adapt

**D-01 — a canonical order for a set carried in an array.**

<!-- q L1103-1106 "sct_extensions is a vector" .. "smallest value first." -->
> sct_extensions is a vector of 0 or more SCT extensions. This vector MUST NOT include more than one extension with the same extension_type. The extensions in the vector MUST be ordered by the value of the extension_type field, smallest value first.

The STH twin is R-0050, R-0051 (L1140-1143). This is condition (5) answered for
CT's one set-valued field: distinct members, one total order, stated on the
key the members are compared by. `ADR-0004` left exactly this open: *"`SPEC-0002`'s
`trusts`, `allow-keys` and `exclude-keys` are arrays whose order is signed and
unstated, so two producers can emit one set as two byte strings."*
(`spec/ADR-0004-dec-002-encoding.md@bb005ed`), and mofn report R-0006 §3.13
counts the cost: *"One semantic trust statement has as many statement digests
as its member list has permutations."* (`research/0006-mechanism/report.md@bb005ed`).

What does not transfer. CT states the order as a producer MUST and no verifier
rule. The client copies `sct_extensions` from the SCT into the signing input
(§8.1.3 L1953), so verification never looks at the order, and a misordered
vector simply fails no check. Under P5.1 a misordered set is a rejection.
*(inferred)* The adaptation is therefore: the rule as CT words it (distinct,
ascending by the comparison key; for `kid`s, bytewise), plus a decoder
rejection. CT has no analogue of `SPEC-0004` §6.4's *identical*, so it says
nothing about set equality across statements.

**D-02 — promise and proof are different evidence.**

<!-- q L792-796 -->
> An SCT is the log's promise to append to its Merkle Tree an entry for the accepted submission. Upon producing an SCT, the log MUST fulfill this promise by performing the following actions within a fixed amount of time known as the Maximum Merge Delay (MMD), which is one of the log's parameters (see Section 4.1):

<!-- q L2596-2598 "Violation of the MMD" .. "observed SCT." -->
> Violation of the MMD contract is detected by log clients requesting a Merkle inclusion proof (Section 5.4) for each observed SCT.

An SCT is a log's signed promise; only an inclusion proof against a later head
shows the promise kept, and the MMD that bounds the wait has no limit in the
document (C-04).
*(inferred)* If R-O-04 is ever built, a registration receipt that is a
promise (SCT-like) and one that is an inclusion proof (RFC 9942-like) are two
kinds of evidence, and statement acceptance (`ARCH-0001` §4.3 step 3) treats
neither as authorization, as mofn report R-0006 §2.4 already requires.

**D-03 — fresh signatures are a tracking channel.**

<!-- q L2611-2620 -->
> Clients that report back SCTs can be tracked or traced if a log produces multiple STHs or SCTs with the same timestamp and data but different signatures. Logs SHOULD mitigate this risk by either: * using deterministic signature schemes or * producing no more than one SCT for each distinct submission and no more than one STH for each distinct tree_size. Each of these SCTs and STHs can be stored by the log and served to other clients that submit the same certificate or request the same STH.

KSA content-addresses a statement by its TBS (`SPEC-0002` §13.3), so a re-signature does
not change identity, but two signatures over one TBS are still two
distinguishable byte strings. Suite 1 is Ed25519 (`SPEC-0002` §6.3), whose
signatures are deterministic [RFC 8032, outside this source]. Suite 8
(ML-DSA-65, §6.5) does not say whether signing is deterministic or hedged, and
`SPEC-0002` §14 does not discuss signature linkability. Open question 6.

**D-04 — audit is its own result.**

<!-- q L2074-2083 -->
> In particular, there are four properties of log behavior that should be checked: * the Maximum Merge Delay (MMD) * the STH Frequency Count * the append-only property * the consistency of the log view presented to all query sources

These four are checked by monitors and clients, apart from validating an SCT
(§8.1.3) and apart from the certificate's own validation (L1965-1966).
*(inferred)* For us, transparency evidence would be one more line in a
`SPEC-0004` §10.4 verdict, never a condition of *acceptance*: R-O-06 already
keeps name resolution, authorization and acceptance apart.

### 2.3 Reject

**X-01 — rebuilding the signed bytes at verification.** The SCT carries
`log_id`, `timestamp`, `sct_extensions` and `signature` (§4.8 L1090-1095), not
the bytes it signs. The client builds them:

<!-- q L1941-1953 -->
> * Compute the signature input by constructing a TransItem of type x509_entry_v2 or precert_entry_v2, depending on the SCT's TransItem type. The TimestampedCertificateEntryDataV2 structure is constructed in the following manner: - timestamp is copied from the SCT. - tbs_certificate is the reconstructed TBSCertificate portion of the server certificate, as described in Section 8.1.2. - issuer_key_hash is computed as described in Section 4.7. - sct_extensions is copied from the SCT.

and, for a precertificate, first rebuilds the TBSCertificate by deleting
extensions from the final certificate's:

<!-- q L1925-1934 -->
> Before an SCT for a precertificate (where the type of the TransItem is precert_sct_v2) can be validated, the TBSCertificate component of the precertificate needs to be reconstructed from the TBSCertificate component of the certificate as follows: * Remove the Transparency Information extension (see Section 7.1). * Remove embedded v1 SCTs, identified by OID 1.3.6.1.4.1.11129.2.4.2 (see Section 3.3 of [RFC6962]). This allows embedded v1 and v2 SCTs to co-exist in a certificate (see Appendix A).

That is a second encoder whose output must equal the log's octet for octet, run
during verification on input not yet authenticated. Ours forbids it: *"A
verifier SHALL verify the signature before decoding and SHALL NOT canonicalize
input as part of verification."* (R-O-05, `spec/ARCH-0001-authorization-attestation.md@bb005ed`),
and `SPEC-0002` §5 gives the reason in these words: *"creating a second encoder
whose output must match the producer's byte for byte"*
(`spec/SPEC-0002-ksa-core.md@bb005ed`). §5.3 says why CT cannot avoid it and
what that is evidence for.

**X-02 — an untagged signing input.** Settled in §6. Ours: *"Every signature
covers a label naming what is being signed"* (§3) and *"each MUST register its
own label, and reusing another's is forbidden"* (§6.4), both
`spec/SPEC-0002-ksa-core.md@bb005ed`.

**X-03 — certificate machinery.** Precertificates (§3.2), the TLS extension
(§6), the X.509v3 and OCSP extensions (§7) and the TLS client rules (§8.1.1,
§8.1.6) exist to carry CT inside WebPKI. *"Native encoding SHALL NOT be X.509 /
PKIX."* (R-M-01) and NG1, *"Replace WebPKI for TLS server authentication."*
(`spec/ARCH-0001-authorization-attestation.md@bb005ed`), place all of it out of
scope. Nothing in them bears on a statement model.

**X-04 — no algorithm on the wire.** The signature field is opaque bytes
(§4.8 L1094, §4.10 L1167) and the algorithm is found only in configuration:

<!-- q L1955-1958 -->
> * Verify the SCT's signature against the computed signature input using the public key of the corresponding log, which is identified by the log_id. The required signature algorithm is one of the log's parameters.

That holds together because a log's parameters are immutable and every client
is configured with them (C-01). A KSA statement is verified by parties who
learned the key from other statements, possibly decades later, so the suite is
carried and signed: *"A statement's suite is inside its TBS and is therefore
covered by its signature."* (`spec/SPEC-0002-ksa-core.md@bb005ed` §6.1). CT
avoids algorithm substitution by never reading an algorithm from an artifact;
KSA avoids it by signing the suite and checking the envelope's hint against it
(V6). Both close the substitution route; only the second works for a key
learned in-band.

### 2.4 Constrains

**C-01 — configuration is the floor.**

<!-- q L1899-1903 -->
> All clients need various parameters in order to communicate with logs and verify their responses. These parameters are described in Section 4.1, but note that this document does not describe how the parameters are obtained, which is implementation dependent (for example, see [Chromium.Policy]).

*(inferred)* For R-O-04 a transparency service would enter as a per-context
anchor: `ARCH-0001` §4.3 already lists *"configured trust for artifact services
(which issuers may assert which PredicateTypes), held as per-context anchors"*
(`spec/ARCH-0001-authorization-attestation.md@bb005ed`, markup removed). It is
evidence for DEC-008's proposed answer, *"Key-local is wrong for the core."*
(`spec/ARCH-0002-key-relative-naming.md@bb005ed`): CT cannot bootstrap a log's
key, hash or MMD from anything the log signs either.

**C-02 — what consistency covers.**

<!-- q L475-479 "Merkle consistency proofs prove" .. "equal in both trees." -->
> Merkle consistency proofs prove the append-only property of the tree. A Merkle consistency proof for a Merkle Tree Hash MTH(D_n) and a previously advertised hash MTH(D[0:m]) of the first m leaves, m <= n, is the list of nodes in the Merkle Tree required to verify that the first m inputs D[0:m] are equal in both trees.

<!-- q L2108-2111 -->
> Checking of the consistency of the log view presented to all entities is more difficult to perform because it requires a way to share log responses among a set of CT-using entities and is discussed in Section 11.3.

Two different extensions of one prefix are each consistent with it (§4 check
9). Consistency is a relation between two heads one verifier holds; it says
nothing about heads another verifier holds. That is the split view of §1, and
S-01 is its missing remedy.

**C-03 — equal sizes and the empty tree.** PROOF is defined for 0 < m < n
(§2.1.4.1 L487-489) and the verification algorithm requires 0 < first <
second (L535-536), failing an empty path at step 1 (L541-542). The API returns
exactly that empty path when the two sizes are equal:

<!-- q L1468-1470 "If first and second" .. "zero elements)." -->
> If first and second are equal and correspond to a known STH, the returned consistency proof MUST be empty (a consistency_path array with zero elements).

So an implementation compares the two root hashes directly when the sizes are
equal, and treats an empty first tree as trivially consistent, outside the
algorithm. *(inferred)*; the source states neither.

**C-04 — freshness is a log parameter.**

<!-- q L834-836 -->
> Maximum Merge Delay: The MMD the log has committed to. This document deliberately does not specify any limits on the value to allow for experimentation.

<!-- q L2575-2578 "Since a log" .. "twice the MMD." -->
> Since a log is allowed to serve an STH of any age up to the MMD, the maximum period of time during which a misissued certificate can be used without being available for audit is twice the MMD.

The arithmetic holds: up to one MMD to incorporate (L793-803), and a served STH
may be up to one MMD old (R-0055), so an honest log can keep an entry out of
every head it serves for just under 2 × MMD. But R-0055 binds the log's own
`get-sth`; an STH that reaches a client in a TLS handshake (§6.4) or from a
third party carries only its timestamp, and no client rule bounds its age.
For R-M-09 (validity intersection) and R-O-02 (short-lived validity), CT-style
evidence supplies a timestamp and a per-log bound, never freshness by itself,
which is what mofn report R-0006 §2.4 found for receipts.

**C-05 — CT's key hashes cannot be compared with a `kid`.**

<!-- q L1064-1066 "issuer_key_hash is the HASH" .. "[RFC5280]." -->
> issuer_key_hash is the HASH of the public key of the CA that issued the certificate or precertificate, calculated over the DER encoding of the key represented as SubjectPublicKeyInfo [RFC5280].

A SubjectPublicKeyInfo carries an AlgorithmIdentifier, an OID, beside the key
[RFC 5280 §4.1.2.7, outside this source], and HASH is the log's parameter, not
a fixed function. RFC 6962's `key_id` was the same construction under SHA-256
(RFC 6962 §3.2). In kind, those are the two alternatives `ADR-0005` rejected: *"suite
code in the preimage"* (*"puts our own registry number into every
identifier"*) and *"per-suite digest"* (*"kids of one key would differ by
suite"*), `spec/ADR-0005-dec-003-key-identifier.md@bb005ed`, markup removed.
Consequence for R-I-01: an importer that meets a CT key hash recomputes it from
the key; it never compares it with a `kid`.

**C-06 — publication cannot be withdrawn.**

<!-- q L808-809 -->
> Log operators SHOULD NOT impose any conditions on retrieving or sharing data from the log.

<!-- q L2630-2634 -->
> Malicious monitors can use logs to learn about the existence of domain names that might not otherwise be easy to discover. Some subdomain labels may reveal information about the service and software for which the subdomain is used, which in turn might facilitate targeted attacks.

A log is append-only (§4 L777-778) and the operator should not restrict
reading it. A KSA statement registered with such a service is published for
the life of the log, with its names, keys and relationships: *"Trust statements
reveal relationships"* (`spec/SPEC-0002-ksa-core.md@bb005ed` §14). R-O-04
already makes registration optional; *(inferred)* it has to stay optional per
statement, decided by the speaker.

**C-07 — time.**

<!-- q L1057-1061 "timestamp is the date" .. "network byte order." -->
> timestamp is the date and time at which the certificate or precertificate was accepted by the log, in the form of a 64-bit unsigned number of milliseconds elapsed since the Unix Epoch (1 January 1970 00:00:00 UTC -- see [UNIXTIME]), ignoring leap seconds, in network byte order.

`SPEC-0002` §4.4 counts seconds since 2026-01-01 in two forms and *"Leap
seconds are not represented."* (`spec/SPEC-0002-ksa-core.md@bb005ed`). Both
ignore leap seconds, so an import maps CT milliseconds to KSA seconds by
truncation, loses the milliseconds, and must emit the day form for an instant
at midnight (an even `T` there is rejected). R-I-01 owes that line.

### 2.5 Conflicts

**K-01 — ignore versus reject.**

<!-- q L1106-1110 "All SCT" .. "it does understand." -->
> All SCT extensions are similar to noncritical X.509v3 extensions (i.e., the mustUnderstand field is not set), and a recipient SHOULD ignore any extension it does not understand. Furthermore, an implementation MAY choose to ignore any extension(s) that it does understand.

<!-- q L1632-1637 "All leaves" .. "input to the tree." -->
> All leaves MUST be v2. However, a compliant v2 client MUST NOT construe an unrecognized TransItem type as an error. This means it may be unable to parse some entries, but note that each client can inspect the entries it does recognize as well as verify the integrity of the data by treating unrecognized leaves as opaque input to the tree.

The STH twin is R-0052, R-0053 (L1143-1146); the API's is R-0061 (L1279-1281);
and a v2 client meeting a non-v2 SCT must not treat it as an error (R-0069,
L1413-1416). Ours: *"an unknown field in a signed payload is an error, not
something to skip."* (P5, `spec/ARCH-0002-key-relative-naming.md@bb005ed`) and *"A verifier MUST NOT skip what it does not
understand (ARCH-0002 P5)."* (`spec/SPEC-0002-ksa-core.md@bb005ed` §13.5). The P5 note draws the line
CT's §5.6 sits on: *"A verifier may traverse what it cannot interpret. A
verifier must never accept what it cannot interpret."*
(`spec/ARCH-0002-key-relative-naming.md@bb005ed`, markup removed). Hashing an
unrecognised leaf as opaque input to the tree is traversal, and compatible.
Accepting an SCT or STH whose signed extension is not understood is
acceptance, and is not. P5.2 sets the boundary rule for DSSE; *(inferred)* the
same asymmetry fits here: an importing verifier rejects a CT object carrying a
signed extension it does not understand, and an exporter emits none. Today it
costs nothing, because Table 15 registers no extension.

**K-02 — registry extension points.** CT has six registries of its own (§10.2:
Hash Algorithms, Signature Algorithms, VersionedTransTypes, Log Artifact
Extensions, Log IDs, Error Types); the first four reserve experimental and
private-use ranges (Tables 8, 10, 12, 14). P1: *"Private-use ranges are not the answer: they give escape from a
registry, not a namespace."* (`spec/ARCH-0002-key-relative-naming.md@bb005ed`,
markup removed). `ADR-0004` item 3 names the registries the native model does
not depend on; an R-O-04 import would add these six to the boundary list, and
none to the native model.

**K-03 — the Log ID became an allocated name.** §3.

### 2.6 Silent

**S-01 — gossip.**

<!-- q L2602-2605 "Violation of the append-only" .. "not defined here." -->
> Violation of the append-only property or the STH issuance rate limit can be detected by multiple clients comparing their instances of the STHs. This technique, known as "gossip", is an active area of research and not defined here.

The one mechanism that would remove the trusted-third-party assumption of A-08
is left undefined. Nothing in the source tells a verifier how to learn what
heads others have seen.

**S-02 — log parameters.**

<!-- q L1765-1767 "Note that client discovery" .. "of this document." -->
> Note that client discovery, trust, and distrust of logs are expected to be handled out of band and are out of scope of this document.

Discovery, trust, distrust, and even the notice that a log is frozen (§4.13
L1241-1243) are out of band.

**S-03 — a compromised log key.** The parameters, key included, are immutable
(§4.1 L813-816, R-0026). The only transition is freezing, after which:

<!-- q L1252-1254 "At this point" .. "can be destroyed." -->
> At this point, the log's private key is no longer needed and can be destroyed.

A compromised key is handled by clients ceasing to trust the log (§6.2
L1774-1779), out of band. *(inferred)* Such a key can sign a head for any tree
of any size, and nothing in the protocol revokes it. KSA at least has signed
succession (`rotate`, `SPEC-0002` §8.8) and statement withdrawal (`revoke`,
§8.7); CT has neither for a log key.

**S-04 — binding a proof to its head.** The verification algorithms take the
size and root as given:

<!-- q L436-440 -->
> When a client has received an inclusion proof (e.g., in a TransItem of type inclusion_proof_v2) and wishes to verify inclusion of an input hash for a given tree_size and root_hash, the following algorithm may be used to prove the hash was included in the root_hash:

The proof structures repeat `log_id` and their sizes (§4.11 L1189-1194, §4.12
L1212-1217), unsigned, and no requirement tells a client to check them against
the head. §4 shows what a client that takes the proof's own size can be made to
accept.

**S-05 — signature confusion.** §11 discusses misissuance, misbehaving logs,
tracking and DNS leakage. It never states which signed inputs must be
distinguishable from which, or why; the one separation between v2's two signed
inputs that exists is the one §6 finds, and it is not stated as a property.

---

## 3. Log identifiers: the key hash became an OID (R-M-12, P1, ADR-0005)

**What changed.** RFC 6962 identified a log by `key_id`, the SHA-256 of the
log's public key over its SubjectPublicKeyInfo DER (RFC 6962 §3.2, read from
`.cache/rfc-6962.txt`). RFC 9162 replaced it:

<!-- q L259-261 -->
> * Logs IDs: Each log is now identified by an OID rather than by the hash of its public key. OID allocations are available from an IANA registry.

The operator either allocates the OID under an arc it holds or requests one from
the Log IDs registry (R-0042, L941-943), which is First Come First Served
(L2403). The source's own account of what the registry adds:

<!-- q L946-950 "The only advantage" .. "out-of-band means.)" -->
> The only advantage of the registry is that the DER encoding can be small. (Recall that OID allocations do not require a central registration, although logs will most likely want to make themselves known to potential clients through out-of-band means.)

**Checked.** The size claims are exact (`oid.py`, §9): every OID from
1.3.101.8192 to 1.3.101.16383 has 4 content octets, and there are 8,192 of
them; under 1.3.101.80 exactly the 128 OIDs .0 to .127 have 4, and .128 has 5.
A log OID under a five-digit Private Enterprise Number, 1.3.6.1.4.1.N.1, has 9
when N ≥ 16384 and 8 when N is 10000 to 16383, where N fits two base-128
octets (pass 2, by encoding every five-digit N: 83,616 give 9, 6,384 give 8).
RFC 6962's `key_id` had 32. LogID's vector length and the DER length octet
coincide (L955-959) because R-0043 caps the content at 127 octets, the
short-form limit. So the advantage the source names is real: four or five
octets per occurrence against a five-digit PEN arc, and 27 against the v1 key
hash (28 content octets, but v1's `opaque key_id[32]` is a fixed array with no
length prefix, RFC 6962 §3.2, while v2's LogID carries one: 32 octets on the
wire against 1 + 4); CT repeats `log_id` in every SCT, STH and proof it emits.

**What the bytes trust the name with: nothing.** No CT signature covers
`log_id` (A-07). The SCT's signing input has no such field; the STH's signature
covers `tree_head` only; proofs are unsigned. The name selects a key, and the
key is checked:

<!-- q L1955-1957 "Verify the SCT's signature" .. "identified by the log_id." -->
> Verify the SCT's signature against the computed signature input using the public key of the corresponding log, which is identified by the log_id.

What lets an unsigned name select safely is that names and keys are one-to-one
for a log's life: one keypair per log (R-0028), the OID used by no other log
(R-0041), both immutable parameters (§4.1 L813-816), and IANA refuses to update
a registered Log ID or base URL (L2439-2441). *(inferred)* If two logs did claim
one OID, the bytes could not tell them apart; only a client's configured key
for each could, which is P1's objection to private ranges seen from the other
side: *"Two parties using the same private label collide, and nothing in the
encoding can disambiguate them because no principal is attached."*
(`spec/ARCH-0002-key-relative-naming.md@bb005ed`). In CT the principal is
attached, but only by configuration.

**Read against R-M-12 and P1.** CT 2.0 made the move P1 rejects for extension
points, from a key-derived identifier to an allocated global name in a
delegated hierarchy (the source gives no reason for the move, L259-261;
*(inferred)* size, the one advantage it names for its registry, L946-947), and in the same revision kept
every security-relevant identity key-derived and inside the signed bytes
(`issuer_key_hash`, C-05). That is evidence **for** P1 and P1.1 in the form that
matters: even a protocol that adopted a registry name did not let the name carry
security, and used it as the lookup handle P1.1 says a foreign `kid` is and
P5.2 says DSSE's `KEYID` is. It is also the honest cost of key-derived
identifiers, and it cuts **against** `ADR-0005` on size, not on soundness:
*(inferred)* CT judged 27 octets per occurrence worth an allocation scheme. KSA's answer is
already written: identifiers stay whole in signed bytes and may be abbreviated
in transport, *"provided the receiver reconstructs the full TBS before
verification"* (`spec/SPEC-0002-ksa-core.md@bb005ed` §4.5, §13.7). CT could not
use that answer for `log_id`, because `log_id` is in no signed bytes to
reconstruct.

**Scope.** A CT log ID is a principal identifier, closer to DEC-003 than to the
extension points R-M-12 governs, so K-03 is a conflict only if CT's allocation
were adopted natively. At an R-O-04 import boundary the log is identified by
its key and the OID is a hint, by the same rule as P1.1.

---

## 4. What the proofs guarantee, checked (R-O-04; mofn report R-0006 §2.4)

mofn report R-0006 §2.4 recorded that *"Every claim about what a proof
guarantees is therefore inherited from RFC 9162 and not checked here"*
(`research/0006-mechanism/report.md@bb005ed`, markup removed). This section
checks them at the level of the algorithms. `merkle.py` and `merkle2.py` (§9)
transcribe §2.1.1 to §2.1.4.2 (L329-578) with SHA-256, the only registered
hash (Table 9, L2202), and run:

| # | check | result |
|---|---|---|
| 1 | §2.1.2's stack algorithm against MTH | equal for every n from 1 to 130 |
| 2 | every PATH(m, D_n) verifies by §2.1.3.2 | 8,515 proofs, every m, n ≤ 130; none longer than ⌈log2 n⌉ |
| 3 | every PROOF(m, D_n) verifies by §2.1.4.2; the bound of L528-529 | 8,385 proofs, 0 < m < n ≤ 130; none longer than ⌈log2 n⌉ + 1, and 3,642 of them exactly that long, so the bound is tight |
| 4 | the 7-leaf example, §2.1.5 | every inclusion and consistency proof printed is what the definitions produce |
| 5 | one valid inclusion proof and its root, checked under other (index, size) pairs | over n ≤ 64 and n′ < 130: 41,664 pass under another size at the same index, 11,864 under another index |
| 5b | the same, but at the head's own size | 0 of 715,520 wrong-index trials pass (n < 130) |
| 6 | do two sizes ever share a root? | no: 300 distinct roots for n = 0 to 299 |
| 7 | the tree without its 0x00 and 0x01 prefixes | a 2-entry list whose entries are the 4-entry tree's inner-node preimages has the 4-entry root; with the prefixes it does not |
| 8 | first = second through §2.1.4.2 | fails: step 1 rejects the empty path that §5.3 returns |
| 9 | two different 10-entry extensions of one 5-entry prefix | both verify as consistent with the same first head; their roots differ |
| 9b | one consistency proof and its two hashes, under other (first, second) | 45,137 of 2,282,280 trials pass (n < 40, n′ < 80) |
| 9c | the same, keeping the true second size | 0 of 158,158 pass (n < 80) |

The verification loops were read as *repeat while neither LSB(fn) is set nor fn
is 0* (L459-460, L566-567). Under that reading every generated proof verifies.
`record.yaml` notes erratum 8670 (editorial, Held for Document Update) on that
loop wording; the erratum text was not read in this pass.

**What a passing inclusion proof establishes.** Given a size and root that come
from one signed head (A-03), and a leaf hash the verifier computed itself as
`HASH(0x00 ‖ TransItem)` (L1044-1046): that entry is leaf `leaf_index` of the
tree of `tree_size` leaves whose root the head signs. Checks 5b and 6 are why:
at the true size no other index passed, and no two sizes shared a root; in
general the second follows from the two prefixes and collision resistance. It does
**not** establish that the log showed this tree to anyone else (C-02), that the
entry is true or authorised (A-08), or anything about time beyond the head's
timestamp being no earlier than the entry's (R-0058, a rule on the log).

**What a passing consistency proof establishes.** Given two heads, each with its
own signed size, and 0 < first < second: the first tree's entries are the first
`first` entries of the second tree (L478-479). Check 9c is why this holds at the
true sizes, and check 9b why it holds only there. It does **not** establish
that no different second tree was shown to another verifier (check 9, S-01),
and it says nothing at equal sizes or from an empty tree (C-03).

**What the security rests on.** Collision resistance of HASH, which the Hash
Algorithms registry's expert review is told to require (L2216-2219), and the
two prefixes (check 7). Nothing else: the proofs are unsigned and inherit all
authority from the head.

**The example's prose misnames three nodes.** Check 4 confirms every proof
printed in §2.1.5, but its commentary calls c, d and j non-leaf nodes:

<!-- q L636-639 -->
> The consistency proof between hash0 and hash is PROOF(3, D[7]) = [c, d, g, l]. Non-leaf nodes c, g are used to verify hash0, and non-leaf nodes d, l are additionally used to show hash is consistent with hash0.

<!-- q L644-646 -->
> The consistency proof between hash2 and hash is PROOF(6, D[7]) = [i, j, k]. Non-leaf nodes k, i are used to verify hash2, and non-leaf node j is additionally used to show hash is consistent with hash2.

In the figure (L584-598) c, d and j sit directly above d2, d3 and d6, so they
are leaf hashes in §2.1.1's sense (L335-337). k, i, g and l are correctly
named. This is a wording defect, not an error in any proof; it is recorded as
`normative.md` SD-22, `protocol.yaml` SD-10 and in `examples/README.md`.

**What this does not check.** The minimality and uniqueness the source asserts
for its consistency proof (L483) were not tested beyond the length bound. How
RFC 9942 carries these proofs is outside this source: open question 2.

---

## 5. MD-3, ADR-0004 and DEC-002: fixed layouts and no canonicaliser

MD-3 narrowed DEC-002 to option 5 on 2026-09-28: *"CBOR data model, no IANA
tags, COSE as export only; type identity is (defining key, label) per P1"*
(`project/meetings/2026-09-28.md@bb005ed`, markup removed). `ADR-0004` accepted
option 5 on 2026-10-25 and closed the narrowing. CT is not a CBOR, COSE or
envelope document, so there is no header-by-header mapping to give; what it
offers is a deployed-lineage signing design that needs **no canonicaliser at
all**, which is evidence about the conditions DEC-002 was decided on.

### 5.1 What CT signs, and how it is encoded

<!-- q L231-232 -->
> Data structures are defined and encoded according to the conventions laid out in Section 3 of [RFC8446].

CT's signed objects and its log entries are built from the nine `struct`
definitions in that language (counted: 9 occurrences of `struct {` in the
source); the Merkle nodes hash concatenated hashes, and the key hashes hash
DER. Integers are
fixed width; each vector's length prefix has a width fixed by its declared
ceiling (one octet for `NodeHash<32..2^8-1>`, two for
`extension_data<0..2^16-1>`, three for `TBSCertificate<1..2^24-1>`); fields
appear in declared order; the one variant is a `select` keyed by a preceding
type field (§4.5 L984-995). There are no maps, no optional fields, no
floating point, no indefinite lengths and no alternative length forms [RFC 8446
§3, outside this source; the structs here use nothing else]. The word
*canonical* occurs once in the source, in the title of the X.690 reference
(L2749); *normali* never. **No canonicalisation rule exists because none is
needed:** *(inferred)* each value has exactly one encoding, and a length-prefixed
concatenation in fixed order is uniquely decodable.

### 5.2 Against the six conditions (mofn report R-0006 §3.2)

| condition | CT | how |
|---|---|---|
| (1) injective | **met per type, by construction** | fixed widths and length prefixes. Across types only where a tag is signed: the SCT's input is tagged, the STH's is not (§6) |
| (2) decoder rejects non-canonical | **vacuous for values** | *(inferred)* no value has a second encoding to reject. What remains is range checking, which the source states for the hash fields (R-0044, R-0049); it states no rule on trailing octets |
| (3) canonicalise once, never in verification | **violated in the letter for SCTs** | X-01: the client re-encodes the TransItem and, for a precertificate, re-encodes a DER TBSCertificate with two extensions deleted. Safe only because both encodings have one form per value: TLS's by construction, DER's by rule |
| (4) authenticated type indicator in the signed bytes | **SCT met, STH not** | the SCT input opens with `versioned_type` (0x0100 or 0x0101); the STH input opens with a timestamp (§6) |
| (5) canonical order for sets in arrays | **met for its one set** | D-01: extensions distinct and ascending, a producer rule |
| (6) Unicode normalisation | **not applicable** | no text in any signed or hashed CT struct; certificate strings travel inside opaque DER |

### 5.3 What it is evidence for

**(1) Grammar-level canonicality without self-description, which DEC-002 never
listed.** `ADR-0004` scored option 1 ahead of option 5 on exactly this ground
and accepted the cost: *"Option 1 wins governance and makes
smallest-form a property of the grammar, so a conforming reader cannot omit
the check. Under option 5 the same property is a rule an implementation must
state; one that omits it still parses every valid document"*
(`spec/ADR-0004-dec-002-encoding.md@bb005ed`). CT has that property in a
binary format: there is no length form to choose and no map to order, so a
reader cannot omit a canonicality check that does not exist. P5.1 counts the
price option 5 pays instead: `SPEC-0002` §4.3 *"has to enumerate seven
conditions where a grammar would have enumerated none"*
(`spec/ARCH-0002-key-relative-naming.md@bb005ed`). CT's grammar enumerates
none; its only decoder obligations are length ranges.

**(2) The cost of a fixed layout is extensibility, and CT pays it by hand.**
Every place CT expects growth is wrapped in an explicit opaque length: each
`Extension` (§4.6 L1023-1026) and each `SerializedTransItem` in a list:

<!-- q L1802-1807 -->
> Here, SerializedTransItem is an opaque byte string that contains the serialized TransItem structure. This encoding ensures that TLS clients can decode each TransItem individually (so, for example, if there is a version upgrade, out-of-date clients can still parse old TransItem structures while skipping over new TransItem structures whose versions they don't understand).

The ARCH-0002 CBOR note names what CBOR gives for nothing: *"a decoder can
determine the extent of any item without understanding its semantics"*
(`spec/ARCH-0002-key-relative-naming.md@bb005ed`, markup removed). CT
rebuilt that at every extension point, and once the extent was skippable it
made skipping the rule (K-01). A fixed layout also has no field names, so a
changed structure is a new type code (A-05), which is what KSA does with
definitions anyway (W-12).

**(3) A type tag is a choice, not a property of the encoding.** CT tags the
signed bytes of an SCT and not those of an STH; the format allowed both.
`SPEC-0002` puts `kind` inside the TBS and a DS label in front of it, which
is R-O-05's indicator twice over. §6 shows what the untagged case costs.

**(4) Reconstruction is what an embedded receipt forces.** An SCT embedded in a
certificate (§7.1.2) cannot contain the bytes it signs, because those bytes
would contain the SCT; so the log signs the precertificate's TBSCertificate
without the extension and every client deletes the extension again before
verifying (X-01). *(inferred)* Under R-O-05 that design is unavailable to
us whatever the encoding: it is canonicalisation during verification by
construction. `ARCH-0001` §6 already keeps a receipt as *"evidence attached
to an attestation"* (`spec/ARCH-0001-authorization-attestation.md@bb005ed`),
attached rather than embedded, which needs no reconstruction. CT is evidence
for keeping it that way, and against any later proposal to embed receipts in
the statements they cover.

### 5.4 Where it cuts against option 5

- **On two rows of `ADR-0004`'s scoring**, *order-only divergence detectable*
  and *canonical-encoding conditions*, a fixed-layout encoding sits with option
  1, not option 5: no map order exists and no length form can vary, so there
  is nothing for a rejecting decoder to enforce. None of options 1 to 5 is a
  fixed-layout encoding. This is evidence that DEC-002's option set was not
  exhaustive on the one axis where `ADR-0004` found option 1 ahead and accepted
  the cost. It is **not** evidence that option 5 is defective: `ADR-0004` gave
  option 1's losses as the data model and library availability, and KSA
  statements are maps with closed key sets (`SPEC-0002` §7, V7), a data model a
  fixed layout does not give.
- **Condition (5) is still open in option 5's profile**, and CT shows the
  missing rule is one sentence per set: distinct, ordered by the comparison
  key. `ADR-0004` deferred it to `SPEC-0002`. Not against the encoding (mofn report
  R-0006 §3.2: Group B is supplied above it), but against the profile as it stands.
- **Map-key order is a cost option 5 carries and CT does not.** Option 5 needs
  §4.2.1 bytewise key order because statements are maps; CT has no maps.
  Option 1's S-expressions are positional too, so on this point CT again sits
  with option 1.

### 5.5 Where it favours option 5 and `SPEC-0002`

- **Self-delimiting extents**: built into CBOR, hand-built in CT (5.3 (2)).
- **An authenticated type indicator**: `SPEC-0002` carries two; CT's STH input
  carries none (§6). A property of the profile, not the encoding, but
  `SPEC-0002` has it and CT does not.
- **Carry the signed bytes** (R-O-05): `SPEC-0002` §5 transmits `tbs`; CT
  reconstructs (X-01).
- **No registry native** (`ADR-0004` item 3): CT depends on six registries of
  its own at every extension point (K-02).

### 5.6 Not discriminators

JSON appears in CT only as the unsigned HTTP transport, with every signed
object carried base64-encoded inside it (§5 L1263-1269); CT never signs JSON.
That is consistent with option 3's withdrawal and adds no new ground. Library
availability and human debugging are not evidenced by this source.

### 5.7 Net, stated as evidence

Nothing here shows a defect in option 5 itself, which is what would supersede
`ADR-0004`. Three findings go to its reader: the option set omitted
fixed-layout encodings, which have the grammar-level canonicality `ADR-0004`
credited to option 1; CT's extension rule is a worked precedent for condition
(5), still owed by `SPEC-0002`; and CT shows, in its STH and its SCT
verification, what R-O-05 and `SPEC-0002` §6.4 exist to prevent.

---

## 6. The untagged STH signing input, settled from the bytes (R-O-05, `SPEC-0002` §6.4)

**The question.** An SCT's signature covers a TransItem whose first field is its
type (L1112-1115). An STH's signature covers `tree_head`, a TreeHeadDataV2,
which has no type field (L1121-1128, L1180-1181). Both are made with the log's
one key and one algorithm (L829-830; §4.1 L827), with nothing prepended. Can a
signature over one be presented as a signature over the other?

RFC 6962 did not ask this, because both of its signing inputs began with a
`SignatureType` octet, `certificate_timestamp(0)` or `tree_hash(1)` (RFC 6962
§3.2, §3.5, read from `.cache/rfc-6962.txt`). RFC 9162 kept a type at the head
of the SCT's input and dropped it from the STH's.

### 6.1 The two layouts (SHA-256 log, HASH_SIZE 32)

| octet | SCT input: TransItem `x509_entry_v2` / `precert_entry_v2` (§4.5, §4.7) | STH input: TreeHeadDataV2 (§4.9) |
|---|---|---|
| 0–1 | `versioned_type`: `01 00` or `01 01` | `timestamp`, high two octets |
| 2–7 | `timestamp`, high six octets | `timestamp`, low six octets |
| 8–9 | `timestamp`, low two octets | `tree_size`, high two octets |
| 10 | `issuer_key_hash` length, `20` (R-0044) | `tree_size`, third octet |
| 11–15 | `issuer_key_hash` octets 0–4 | `tree_size`, low five octets |
| 16 | `issuer_key_hash` octet 5 | `root_hash` length, `20` (R-0049) |
| 17–42 | `issuer_key_hash` octets 6–31 | `root_hash` octets 0–25 |
| 43–45 | `tbs_certificate` length L | `root_hash` octets 26–28 |
| 46–48 | `tbs_certificate` octets 0–2 | `root_hash` octets 29–31 |
| 49–50 | `tbs_certificate` octets 3–4 | `sth_extensions` length X |
| 51 … | rest of `tbs_certificate`, then `sct_extensions` length E and data | `sth_extensions`, X octets, to the end |

### 6.2 An STH signature presented as an SCT signature: closed

For an STH input to begin `01 00` or `01 01`, its timestamp must lie in
[2^56, 2^56 + 2^49) milliseconds, the years 2,285,384 to 2,303,223
(`layout.py`). An honest log stamps the present:

<!-- q L1132-1133 -->
> timestamp is the current date and time, using the format defined in Section 4.7.

On 2026-11-08 that is `0x000001a1b8746c00`, whose high two octets stay `00 00`
until 2^48 ms, in the year 10889 (years counted as 365.2425 days). And the attacker does not choose the SCT
input in any case: the verifier builds it from the certificate (§8.1.3). No
honest STH signature verifies as an SCT signature.

### 6.3 An SCT signature presented as an STH signature: open at the struct layer

Every SCT input, read as a TreeHeadDataV2, already has its first two octets
fixed to the type code, so its timestamp is in that same far-future range. The
rest must tile: octet 16, which is `issuer_key_hash` octet 5, must be `20`; the
extension length X lands on `tbs_certificate` octets 3–4; and the extension
list must end exactly where the TransItem ends. `layout.py` solves this for a
DER TBSCertificate (`30 82` and a two-octet length, then `A0` for the version
field) with no SCT extensions. That is the case for every log that emits none;
Table 15 registers none, but its experimental and private-use ranges
(0xE000-0xFFFF, Table 14) need no registration, and with E octets of SCT
extensions the equation below gains a term and admits other lengths:

- exactly **one** content length works with that prefix, `0x9F9F` (40,863
  octets, a 40,867-octet TBSCertificate). The tiling equation is
  256·`tbs[3]` + `tbs[4]` = C + 1 for content length C, so each value of the
  first content octet `tbs[4]` fixes one C: a version-less (v1)
  TBSCertificate, whose first content octet is `02` (serialNumber), has its own
  single length, `0x0101` (a 261-octet TBSCertificate, a 309-octet TransItem;
  pass 2, by enumerating every C and `tbs[4]`). A three-octet DER length admits
  none, a one-octet length after `A0 03` would need at least 40,708 octets of
  SCT extensions, and a short-form length (under 128 octets) is no real
  TBSCertificate;
- with that length, a 40,915-octet string was built that a strict parser
  (both hash lengths 32, extension types distinct and ascending, no trailing
  octets) accepts **both** as an `x509_entry_v2` TransItem and as a
  TreeHeadDataV2;
- read as a tree head it says: timestamp in the year 2,285,384, and
  `tree_size` 7,782,255,340,485,214,980. Octet 10 is always `20`, so every such
  head claims at least 2^45 entries.

In practice this needs a certificate the log accepts, of exactly the length its
first content octet fixes, whose TBSCertificate octets at the tiling offsets the attacker controls, from a
CA whose key hash has `20` at octet 5 (one key in 256 on average). Whether a
real CA-signed TBSCertificate can be made to tile was **not** tested; the
struct layer admits it.

### 6.4 Does it matter? Settled

**A usable forged head: no.** The head claims at least 2^45 entries and a
timestamp more than two million years out. By §4 a consistency proof binds
both sizes, so none connects it to a real head, and no monitor can fetch its
entries.

**Framing an honest log: the residual risk.** CT treats signed inconsistency
as proof:

<!-- q L1895-1897 "Any inconsistency" .. "misbehavior." -->
> Any inconsistency may be used as evidence that a log has not behaved correctly, and the signatures on the data structures prevent the log from denying that misbehavior.

A signed head more than two million years in the future makes every later
honest head look like a breach of R-0059 (each timestamp later than the previous), and
its entries can never be served, which a monitor is told to view as
misbehaviour (L2042-2045). The log can rebut it by exhibiting the TransItem
those octets are, but no rule makes an auditor reject the head first: §8
gives STH verifiers no plausibility check on timestamp or size.

**Verdict.** The untagged input does not matter for honest heads, and the
direction that remains open is closed only by a **numeric accident**: the
SCT's type code `0x01xx`, read as milliseconds, is absurd. The separation is
not by construction, it is not stated anywhere (S-05), and no requirement
makes a verifier act on the absurdity. *(inferred)* An R-O-04 importer of
CT-style heads would need its own plausibility rule, because the source
supplies none.

### 6.5 What it means for us

`SPEC-0002` makes this impossible by construction: *"A signature binds its DS
label (§6.4)."* (`spec/SPEC-0002-ksa-core.md@bb005ed` §13.2), and each signed
object registers its own label (§6.4).
CT is the counterexample that shows why the rule binds **within** one protocol
and one key, not only across protocols: two object types under one key, one of
them untagged. It also shows that the remedy CT used between its versions,
separation by key (one key per log, one version per log, R-0028, §4.1
L838-839), is not open to KSA, whose one key speaks every statement kind; the
`kind` inside the TBS and the DS label in front of it are the only separation
KSA has, and `SPEC-0002` has both. R-O-05's *"authenticated type indicator"*
(`spec/ARCH-0001-authorization-attestation.md@bb005ed`) is met by CT's SCT
input and not by its STH input.

---

## 7. Arithmetic, and every *only* and *uniquely*, checked

**The source's claims.**

| claim | where | verdict | how |
|---|---|---|---|
| the tree's shape is fixed by the number of leaves | L357-359 | true by construction | k depends on n alone (L339-340); §4 check 6: no two sizes share a root |
| the consistency proof is the unique minimal one | L483 | **not checked** | only the length bound was tested |
| a consistency proof has at most ⌈log2 n⌉ + 1 nodes | L528-529 | true, and tight | §4 check 3: 8,385 proofs, 3,642 at the bound |
| 1.3.101.8192 to 1.3.101.16383 are 8,192 OIDs of 4 encoded octets | L2422-2424 | true | `oid.py`. Every 1.3.101.N with 128 ≤ N ≤ 16383 has 4 octets; the registry set aside the upper 8,192 |
| only the 128 OIDs 1.3.101.80.0 to .127 have 4 octets | L2427-2430 | true | `oid.py`: .128 has 5 |
| the registry's only advantage is a small DER encoding | L946-947 | consistent | 4 octets against 8 or 9 under a five-digit PEN (9 once N ≥ 16384) and 32 for v1's key hash; the registry adds no security property, since FCFS allocation checks only a base URL and contact (R-0124) and `log_id` is signed nowhere (§3) |
| the DER length octet and the LogID vector length coincide | L955-959 | true | both are one octet because R-0043 caps the content at 127 |
| a misissued certificate can go unaudited for twice the MMD | L2575-2578 | true as an upper bound for an honest log, read from the log | C-04 |
| 0x0403 appears twice and verification is the same for both | L2235-2238 | true | deterministic ECDSA [RFC 6979, outside this source] emits ordinary ECDSA signatures. Consequence in open question 6: a client cannot see from the code point whether a log signs deterministically |
| the issuer key hash makes an SCT impossible to reuse for another issuer's TBSCertificate | L1067-1070 | true given collision resistance of HASH | the hash is inside the signed bytes (A-07) |

**One inconsistency in the source's type codes.** The submission API's `type`
is described as a VersionedTransType value but given as 1 and 2:

<!-- q L1361-1363 -->
> type: The VersionedTransType integer value that indicates the type of the submission: 1 for x509_entry_v2 or 2 for precert_entry_v2.

The same types are 0x0100 and 0x0101 in the enum (L972) and in Table 13
(L2323-2325), and 1 and 2 lie in the range reserved for v1 (L978, L2321).
`badType` repeats 1 and 2 (L1395-1396, L2485), and L1433 calls type 2
`precert_sct_v2`. `record.yaml`'s one erratum (8670) is on other text. It bears
on this file only as the one place where the source's type codes disagree
with themselves; open question 8.

**This file's own numbers** were produced by the scripts in §9 and are stated
with their scope: the proof counts with their n, the polyglot with its length,
the OID sizes with the OIDs encoded. *More than two million years* is the
2,285,384 of §6.2 stated as a lower bound. *One CA key in 256* is the
expectation for a uniformly distributed hash octet. Row counts were taken by `grep` over the table in §1.

---

## 8. Open questions

1. **Non-equivocation for R-O-04.** CT leaves gossip undefined (S-01) and a
   consistency proof cannot see a fork (C-02, §4 check 9). If R-O-04 is ever
   built, does a verifier rely on one service as a trusted third party (A-08),
   on its own retained heads, or on something this source does not define?
   Bears on R-O-04, NG4 and DEC-008.
2. **Do RFC 9942 receipts authenticate tree size and leaf index?** mofn report
   R-0006 §2.4 describes an inclusion receipt as a COSE_Sign1 whose payload is
   a Merkle root, with *"[tree-size, leaf-index, inclusion-path] in the
   unprotected header"* (`research/0006-mechanism/report.md@bb005ed`, markup
   removed). If the size and index are signed nowhere, §4 checks 5 and 5b say
   the receipt proves membership under the signed root but not position or
   size. Whether that matters for SCITT, and whether RFC 9942 binds them some
   other way, is for the `rfc-9942` record. Not checked here.
3. **An imported signed head: evidence or statement?** An STH is a key saying
   that a tree of some size has some root at some time, which is P2's form
   with the root as a digest target. `ARCH-0001` §6 keeps a receipt as attached
   evidence. Which import profile R-I-01 records is open; either way §6.4
   says the importer needs its own plausibility rule.
4. **Condition (5) for `trusts`, `allow-keys` and `exclude-keys`.** D-01 gives
   CT's rule shape. Whether `SPEC-0002` adopts the rule mofn report R-0006
   §3.13 finds in `SPEC-0003` kind 7 (distinct kids, sorted), with P5.1's
   rejection added, is owed to `SPEC-0002` by `ADR-0004`. This record adds a
   precedent, not a decision.
5. **Was DEC-002's option set exhaustive?** §5.4: a fixed-layout,
   schema-determined binary encoding has grammar-level canonicality and is
   none of options 1 to 5. `ADR-0004` is accepted and changes only by
   superseding; this is recorded for its reviewer (`reviewed: false`), not as
   a reason to reopen it.
6. **Signature determinism in `SPEC-0002`.** D-03: CT treats distinct
   signatures over identical data as a tracking channel. Suite 1 is
   deterministic; suite 8 does not say; §14 does not discuss signature
   linkability. CT's own registry hides the property: 0x0403 names both
   randomized and deterministic ECDSA (L2235-2238), so a client cannot tell
   which of R-0125's two mitigations a log uses. Does `SPEC-0002` §14 need a
   sentence, and does a suite registration need to state determinism?
   The source is itself inconsistent here: a log that re-signs an idle tree
   every MMD period (R-0057) issues a second STH for one tree_size, which R-0125's
   second mitigation forbids, so only deterministic signatures satisfy both
   (`normative.md` SD-12; `protocol.yaml` OI-10).
7. **Equal sizes and the empty tree** (C-03). The API returns the empty path the
   algorithm rejects. Is that a source gap the protocol lane should record, and
   what rule would an R-O-04 verifier state? This file infers: equal roots at
   equal sizes, and any tree consistent with the empty one.
8. **The submission `type` values** (§7). 1 and 2 against 0x0100 and 0x0101.
   Recorded by the protocol and messages lanes (`normative.md` SD-2,
   `messages.yaml` SD-01, `protocol.yaml` SD-02); the source does not say which
   is literal.
9. **For this library.** `docs/extraction.md` still says no DEC-002 ADR exists;
   at `bb005ed` `ADR-0004` does. Not edited here: this lane owns one file.
10. **`bears_on`.** The findings bear on R-O-05 (§6, X-01, X-02) and on DEC-003
    through `ADR-0005` (§3, C-05) at least as directly as on DEC-002.
    `record.yaml`'s owner may want to add both; not edited here.
11. **What a frozen log must still do** (A-06, S-03). R-0421 makes freezing
    mandatory when an algorithm is deprecated, "as specified in Section 4.13",
    whose four actions are all SHOULD (R-0060), so which of them bind is not
    determinable (`normative.md` SD-14). The permission to destroy the key after
    the final STH cannot be reconciled with the freshness rules of §4.10 (R-0055,
    R-0057), which the source does not suspend for a frozen log (SD-13). An
    importer that records a frozen log's final head has no source rule for how
    stale a served head may then be.

---

## 9. Method: how each claim here was produced

- **Our documents** were read only with `git show bb005ed:<path>` in
  `/Users/nfn/Projects/mofn`, whose HEAD was `bb005ed` throughout the pass.
- **The source** is `.cache/rfc-9162.txt`, 2961 lines, sha256 as in the
  header. `bin/bcp14-count` was re-run in this pass: 138.
- **Quotations of the source** are `<!-- q -->` markers only; the blockquotes
  were written by `bin/check-quotes --render --only` on this file, and
  `bin/check-quotes` verifies every one against its lines (§9 count below).
- **Quotations of our documents** were each resolved by script against the
  blob of the file named beside them, at `bb005ed`. The one relaxation channel:
  blockquote markers, `*` and backticks removed on both sides, whitespace
  collapsed. Each attribution was read, not only matched.
- **Unmarked source text.** Every 8-word window of this file's prose (rendered
  blockquotes and markers excluded, our quotations excluded) was searched for in
  the source; none occurs there.
- **Requirement ids** were emitted from `requirements.yaml` by script, read
  under both of the library's YAML readers, and each pair (id, text) was read
  beside the claim citing it. During this pass the requirements lane grew the
  file from 125 to several hundred entries; this file cites only the skeleton's
  stated ids R-0001 to R-0125, re-read after the growth, and, since pass 3, R-0421
  (a split child of R-0122, in open question 11).
- **Scripts** (scratch, not committed: this lane owns one file; each is
  specified closely enough here to rebuild):
  - `merkle.py`, `merkle2.py`: §2.1.1 to §2.1.4.2 transcribed with SHA-256 over
    entries `entry-0`, `entry-1`, …; checks 1 to 9c of §4.
  - `layout.py`: the two signing inputs of §6.1 with strict parsers (hash lengths
    32, extension list tiling exactly with distinct ascending types, no trailing
    octets); the closed-form solution for the tiling; the 40,915-octet polyglot.
  - `oid.py`: DER content lengths of the OIDs in §3 and §7.
  - `reqs.py`, `audit.py`: the id table, the joins, the quotation and window
    audits.

**Counts, measured on the final text of this file** (each states what was
examined; recount after any edit):

Pass 2 (verify, 2026-11-08) recounted after its edits: check-quotes 48 of 48, the 50 mofn quotations, and 47 distinct ids, all unchanged; the window count moved and is annotated in its row. Pass 3 (cross-check, 2026-11-08) edited open questions 6, 8 and 11 and recounted: 48 of 48, 50, 49 distinct ids (rows below), and a window re-run with its own tokenisation (9,830 windows over the edited prose, 0 found in the source).

| check | examined | result |
|---|---|---|
| `bin/check-quotes`, this file | 48 source quotations | 0 mismatched |
| our-document quotations | 50 | 0 unresolved, every attribution read |
| 8-word prose windows against the source | 9,702 (pass 1); pass 2 edited §1 item 1, §3, §6.3 and this table, and its own re-run over the edited text (markers, blockquotes and italic quotations removed, whole text) examined 9,919 | 0 found |
| requirement ids cited | 49 distinct, 88 occurrences (47 and 82 after pass 2; pass 3 added R-0057 and R-0421 and six occurrences in the open-question text); one, `rfc-9162#R-0006`, is named only to tell it apart from mofn report R-0006 | 0 unresolved, every pair read |
| rows in §1 | 31 | 8 adopt, 4 adapt, 4 reject, 7 constrains, 3 conflicts, 5 silent |

---

## 10. What this file decides

Nothing. It records evidence and maps it. No requirement is added, amended or
withdrawn; no DEC-* is opened, ranked or accepted; `ADR-0004` is not reopened
and `ADR-0005` is not amended; R-O-04 stays *Could*, and T-092 stays out of the
demo floor. Where a row says *adopt* or *adapt*, it says what this source would
contribute if the decision it maps to were taken, and the decision belongs to
an ADR (`ARCH-0001` §9, R-D-02).

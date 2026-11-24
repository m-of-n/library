---
record: draft-ietf-spki-cert-structure
kind: design-notes
title: "draft-ietf-spki-cert-structure — bearing on our design"
extracted: "2026-11-09"
reviewed_by: ""
---

# Simple Public Key Certificate (SPKI, -06) — bearing on our design

*Simple Public Key Certificate* is the Internet-Draft
`draft-ietf-spki-cert-structure-06` of 26 July 1999 (Ellison, Frantz, Lampson,
Rivest, Thomas, Ylonen), expired 31 January 2000 and never published as an RFC.
The bytes are the lead author's copy at `content.url`; `record.yaml` says why -06
and not -05. Source of record: `.cache/draft-ietf-spki-cert-structure.source.txt`,
sha256 `6d3332d77a3b0231748dea94a22fa5876c191b51f5f789589024bb64b7397d15`, equal to
`content.sha256` and recomputed in this pass. Every line number below is a line
of `.cache/draft-ietf-spki-cert-structure.txt` (sha256
`7542050ffd8658c90b22564b34e8ad1b452b125e396423b1e77b2af7f19f33de`), which
`distilled/render-source.py` derives by rewriting section headings only, with no
line added or removed. 2622 lines (`wc -l`).

It defines, as S-expressions in canonical form: keys, hashes and detached
signatures (§3.8); the authorization certificate (§4) and the name certificate
(§5); the ACL and the `sequence` a prover hands a verifier (§6); CRL, delta-CRL,
revalidation and one-time revalidation replies (§7); and the 5-tuple reduction a
verifier runs (§8). It is where SPKI's line specifies the certificate as bytes;
`rfc-2693` is the theory and `rfc-9804` the S-expression encoding without the
certificate (`record.yaml` `see_also`).

It reaches us in eight ways.

1. **DEC-002, accepted by ADR-0004, and MD-3.** SPKI signs canonical
   S-expressions: a canonical encoding fixed at the grammar level, used for a
   whole certificate system. ADR-0004 scores option 1 cell by cell; §5 tests those
   cells against what SPKI actually needed.
2. **Threshold subjects.** ARCH-0001 §1 item 4 names SPKI as the source of
   *k*-of-*n*, and G4 and R-M-06 ask for it; SPEC-0002 §8.6 and SPEC-0004 §6.4
   specify ours. §6.
3. **Delegation depth.** `(propagate)` is a boolean; DL-0025 chose an integer
   depth and R-M-10 now records SPKI's objection as a stated limit. Because every
   hop must lower a KSA depth, the flag maps onto it per chain, never per
   certificate. §7.
4. **Tag intersection.** R-M-08, DEC-004 (open; its option 1 takes SPKI's tag
   S-expressions unchanged), SPEC-0003 §6 and SPEC-0004 §6.3. §8.
5. **Local names and name reduction.** R-M-03, R-M-04, P6, and the compound
   names ARCH-0001 §5.5 says SPEC-0004 owes (mofn#143). §9.
6. **Validity and online tests.** R-M-09, R-O-02, ADR-0003 D5, SPEC-0004 §7.1,
   and ARCH-0001 §5.5's open `online_check`. §10.
7. **Key-as-principal, and hashes as principals.** R-M-02, R-O-01, ADR-0005, P1.
   §11.
8. **mofn report R-0006 and R-0007.** R-0006 §2.2 marks SPKI's to-be-signed
   construction **∅** and places it in this draft; R-0007 §3.5 takes its SPKI
   wire syntax from this draft. §12 fills and tests those cells, and §13
   drafts the ARCH-0001 §6 SPKI row's R-I-01 table that WP2 owes.

**Things to hold while reading.**

1. **What binds.** The draft states its intended status and recites RFC 2119
   (L32, L39–L41), then uses no BCP 14 keyword:
   `bin/bcp14-count` returns **0**. Every obligation is in lower case: *must* (21
   occurrences on 21 lines, counted by script), *should* (6), one *may not*
   (L779), or a grammar rule, and there is no normative/informative split. So
   nothing here is a requirement in the BCP 14 sense; where a row below is
   adopted, **we** make it normative in a SPEC or an ADR. The requirements lane
   extracted this record concurrently; §15 joins its ids to this file's
   quotations and locators, and records where the two lanes inferred the same
   rule.
2. **Quotations are by reference, never typed.** A quotation of the source is a
   `<!-- q Lx-y -->` marker rendered by `bin/check-quotes --render`. A quotation
   of one of our documents is a `<!-- qm PATH Lx-y -->` marker: `PATH` is a file
   of the m-of-n repository at commit **`bb005ed`** (2026-11-07), and the words are
   lines x to y of `git show bb005ed:PATH`, a blockquote margin dropped,
   whitespace collapsed; a pass script rendered each one and checked it against
   its own file only. A marker is an HTML comment and does not render, so the
   same script writes a visible line under each such quotation naming it as
   `PATH`@`bb005ed` with its lines (our documents' lines are written *lines n–m*,
   never `Lnnn`, which is reserved for the source). `bin/check-quotes` cannot
   see a `qm` marker. Optional anchors (`"starts" .. "ends"`) select a sub-span
   in both kinds. **No marker spans a page break**: `bin/_source_text` strips
   only an RFC's running header, so in this draft each page's running header
   line (the first is L59) would land inside the quotation. A sentence that
   crosses a page is quoted as two markers. Names in
   backticks (`(propagate)`, `k-of-n`, `<subj-thresh>`) are identifiers, not
   quotations. S-expressions marked *constructed* are ours.
3. **Locators.** `§n` is the draft's own section number; `Lnnn` is the line,
   which is exact. The draft has no §8.5 or §8.6: its §8.4 is followed by §8.7, in
   the text and in its table of contents (L246–L247, SI-13).
4. **Our decisions, and their standing at `bb005ed`.**

   | name | path at bb005ed | standing |
   |---|---|---|
   | ARCH-0001 v0.2.0 | `spec/ARCH-0001-authorization-attestation.md` | draft, updated 2026-11-07. §5 R-M, R-I, R-O rows (R-O-05 added 0.2.0); §5.5 gaps owed by the SPECs; §6 matrix; §7: DEC-001, DEC-002, DEC-003, DEC-007 accepted, DEC-004, DEC-005 open |
   | ARCH-0002 v0.10.0 | `spec/ARCH-0002-key-relative-naming.md` | P1 accepted (ADR-0001); P2, P3, P5 with P5.1 and P5.2, P6 accepted (ADR-0002); P1.1, P4, P7 draft; DEC-008, DEC-009 open |
   | ADR-0001, ADR-0002 | `spec/ADR-0001-key-relative-naming.md`, `spec/ADR-0002-provisional-principles.md` | accepted 2026-09-22 and 2026-11-06; ADR-0002 `reviewed: false` |
   | ADR-0003 | `spec/ADR-0003-ksa-core-decisions.md` | accepted 2026-10-14; D1–D5; where a SPEC and an ARCH differ the SPEC governs |
   | ADR-0004 | `spec/ADR-0004-dec-002-encoding.md` | accepted 2026-10-25, `reviewed: false`; DEC-002 option 5 |
   | ADR-0005 | `spec/ADR-0005-dec-003-key-identifier.md` | accepted 2026-10-25, `reviewed: false`; DEC-003 |
   | SPEC-0001 v0.1.0, SPEC-0002 v0.5.0, SPEC-0003 v0.1.3, SPEC-0004 v0.3.0 | `spec/SPEC-000n-*.md` | drafts; govern under ADR-0003 |
   | DECISIONS-0001 v0.6.0 | `project/DECISIONS-0001.md` | the register |
   | MD-3 | `project/meetings/2026-09-28.md` | dated narrowing of DEC-002, closed by ADR-0004 |
   | DL-0019, DL-0025, DL-0028 | `design-log/00nn-*/` | the threshold fixture; integer depth; ARCH-0001 v0.2.0 and SDSI names kept |
   | mofn report R-0006 v0.3.0 | `research/0006-mechanism/report.md` | draft; evidence, decides nothing; pinned to `library@60b3284` |
   | mofn report R-0007 v0.2.0 | `research/0007-delegation-models/report.md` | draft, evidence only; pinned to `library@a1aa258` |
   | CONTRIBUTING | `CONTRIBUTING.md` | process; §5 |

   **`docs/extraction.md` is stale on one point**, as the two W3C siblings found:
   it says no DEC-002 ADR exists, and ADR-0004 is that ADR. This file maps against
   ADR-0004 and still records where the source cuts against option 5, which is
   what that rule is for. `docs/` is not edited here.
5. **Labels.** *(inferred)* marks what the source implies rather than states,
   and every consequence drawn here. **Ours** marks the library's proposal.
   **[outside this source]** marks a statement resting on a document this file
   did not read; such a statement is never quoted from that document, and never
   the sole ground of a verdict. `rfc-2693` is quoted only through R-0007's own
   quotation of it, marked as such.
6. **Numbering.** `R-M-NN`, `R-I-NN`, `R-O-NN`, `G1`–`G7` and `WP2` are ARCH-0001.
   `P1`–`P7` are ARCH-0002. `MD-n` are dated meeting decisions; `DL-NNNN` are
   design-log entries. `D1`–`D5` are ADR-0003's. `V1`–`V9` are SPEC-0002 §9.2's
   steps and `TV-n`, `N-n` its Appendix A vectors. "Condition (n)" is one of mofn
   report R-0006 §3.2's six. A bare `R-0006` or `R-0007` is always the mofn
   report, never a requirement id of this record, which is written in full
   (`draft-ietf-spki-cert-structure#R-NNNN`). `SI-n` are the source
   inconsistencies of §14 below. Sections of this file are written "§6 below".

---

## 1. What we adopt

### A1. The key is the principal, and identity is optional

<!-- q L416-418 -->
> PRINCIPAL: a cryptographic key, capable of generating a digital signature. We deal with public-key signatures in this document but any digital signature method should apply.

<!-- q L89-93 "Establishing identity" .. "often unnecessary." -->
> Establishing identity, sometimes thought to be the only purpose of a certificate, is considered to be an optional step in this process but not the goal of the effort and often unnecessary.

Ours:

<!-- qm spec/SPEC-0004-ksa-trust-evaluation.md L93-98 "KSA's answers are" .. "makes it trusted." -->
> KSA's answers are: **a key is a principal** (SPEC-0001); **what it may say is delegated, narrowing at every hop** (§6); and **trust begins at anchors the relying party chose, in the context where it chose them** (§4). There is no global root, no default trust list, and no step at which merely discovering a key makes it trusted.

— `spec/SPEC-0004-ksa-trust-evaluation.md`@`bb005ed`, lines 93–98

<!-- qm spec/ARCH-0002-key-relative-naming.md L146-148 -->
> Per SDSI and SPKI, **the speaker is the key.** There is no separate notion of "who signed this" versus "who said it", and no authority above A that makes A's saying meaningful.

— `spec/ARCH-0002-key-relative-naming.md`@`bb005ed`, lines 146–148

Same position. KSA narrows *how* the key is written (one `kid` per key, A11 and
§11 below); it takes the position itself unchanged. Nothing in either document
needs a global name to authorise.

### A2. The relying party's own unsigned entry is the root of every chain

<!-- q L1156-1163 -->
> Because a certificate merely transfers authorizations, rather than creating them, the form we call ACL-entry is also defined below to inject authorizations into a chain of certificates. An ACL entry lives on the machine of the verifier, leading to the observation that all authorization flow is in a circuit -- from the verifying machine's ACL, possibly through certificates and then back to the verifying machine. Alternatively, one might say that the only root of an authorization certificate chain is the verifier.

<!-- q L1787-1792 -->
> An ACL is a list of assertions: certificate bodies which don't need issuer fields or signatures because they are being held in secure memory. Since the fields of the ACL are fields of a <cert>, we will not repeat those common field definitions here. Since an ACL is not communicated to others, developers are free to choose their own formats.

Ours:

<!-- qm spec/SPEC-0004-ksa-trust-evaluation.md L165-168 -->
> Anchors are a **local data structure**, not a wire format. They are never signed as anchors and MUST NOT be transmitted unless the persona that owns the context chooses to publish them, for example as a trust statement of its own (§4.3, §12).

— `spec/SPEC-0004-ksa-trust-evaluation.md`@`bb005ed`, lines 165–168

<!-- qm research/0006-mechanism/report.md L269-275 "SPKI does, and its root" .. "where the anchors belong to the log operator." -->
> SPKI does, and its root is the verifier's own unsigned ACL. **`ADR-0003` D3 and D4 put the KSA core close to that position** — anchors per context, local and possibly unsigned, accepted by a persona — and further from SCITT's, where the anchors belong to the log operator.

— `research/0006-mechanism/report.md`@`bb005ed`, lines 269–275

An SPKI ACL entry is an anchor: an unsigned `entry` with a subject, an optional
`(propagate)`, a tag, and an optional validity and comment (L1784–L1785), issued
implicitly by `self` (L2041–L2043). ADR-0003 D3 goes further than SPKI (adapt B1
below).

### A3. *k*-of-*n* sits on the subject side, and is most useful at the root

<!-- q L1296-1302 -->
> The actual intent is to insure that there are K distinct paths passing permission between the verifier's ACL and the prover's request. These multiple paths fork and join, so the k-of-n construct could theoretically be part of either the Subject or the Issuer. Since an ACL might want to specify these multiple paths (and an ACL has no Issuer) and since a certificate is signed by a single Issuer, we have chosen to specify the branching at the Subject.

<!-- q L439-446 -->
> THRESHOLD SUBJECT: a Subject for an ACL entry or certificate that specifies K of N other Subjects. Conceptually, the power being transmitted to the Subject by the ACL entry or certificate is transmitted in (1/K) amount to each listed subordinate Subject. K of those subordinate Subjects must agree (by delegating their shares along to the same object or key) for that power to be passed along. This mechanism introduces fault tolerance and is especially useful in an ACL entry, providing fault tolerance for "root keys".

Ours: the threshold form of `trust` puts the set in the subject position, with
`this` absent:

<!-- qm spec/SPEC-0002-ksa-core.md L538-542 -->
> The speaker extends trust to a key about a range of attributes. In the **threshold form**, `this` is absent, `trusts` lists two or more keys, and `threshold` is an integer `n` with 1 ≤ n ≤ the number of keys: the trust is extended to any `n` of them acting together (SPEC-0004 §6.4). Otherwise `this` MUST be present and `trusts` and `threshold` MUST be absent.

— `spec/SPEC-0002-ksa-core.md`@`bb005ed`, lines 538–542

and an anchor may be a threshold set:

<!-- qm spec/SPEC-0004-ksa-trust-evaluation.md L146-147 -->
> An anchor states that, in this context, a key — or a threshold set of keys — is trusted about a scope.

— `spec/SPEC-0004-ksa-trust-evaluation.md`@`bb005ed`, lines 146–147

SPKI's reason for the subject side, that a certificate has one issuer and an ACL
none, applies to ours unchanged: a KSA statement has one `says`, and an anchor
has none (inferred; no document of ours states a reason).
Neither document has an issuer-side threshold, that is, one statement carrying
*k* signatures (inferred). Where the two differ is §6 below.

### A4. An object named by its hash can be a subject

<!-- q L1261-1265 -->
> <obj-hash>:: "(" "object-hash" <hash> ")" ; This option for a (subject ) refers to an object other than a <principal>. One might use this form to assign attributes to an object (a file, a web page, an executable program, ...).

<!-- q L381-384 -->
> HASH: a cryptographically strong hash function, assumed to be collision resistant. In general, the hash of an object can be used wherever the object can appear. The hash serves as a name for the object from which it was computed.

Ours: target type 2:

<!-- qm spec/SPEC-0002-ksa-core.md L415 "| 2 digest |" .. "32 octets) |" -->
> | 2 digest | `[2, digest-alg, bytes]` | an object identified by its digest; `digest-alg` 1 = SHA-256 (32 octets) |

— `spec/SPEC-0002-ksa-core.md`@`bb005ed`, line 415

<!-- qm spec/SPEC-0002-ksa-core.md L421-422 -->
> Subjects are not limited to keys: a statement can concern a release, a record, a definition, or another statement.

— `spec/SPEC-0002-ksa-core.md`@`bb005ed`, lines 421–422

SPKI's `object-hash` subject is ARCH-0001 G5's artifact statement in 1999 form.
ARCH-0001 §3.3 records the historic gap as:

<!-- qm spec/ARCH-0001-authorization-attestation.md L198 -->
> 1. Historic gap: SPKI/SDSI never standardized a first-class **artifact statement** type; PICS did, without a strong principal/delegation model.

— `spec/ARCH-0001-authorization-attestation.md`@`bb005ed`, line 198

This draft gives that statement a shape, though not a first-class type: an
authorization or name certificate whose subject is a hash, with no predicate
vocabulary (inferred). The gap ARCH-0001 records survives, narrowed: there was
a form, but no type.

### A5. A withdrawn statement is named by the hash of its bytes

<!-- q L1919-1923 -->
> <crl>:: "(" "crl" <version>? <cancel-list> <valid-basic> ")" ; <cancel-list>:: "(" "canceled" <hash>* ")" ; <delta-crl>:: "(" "delta-crl" <version>? <hash-of-pred> <cancel-list> <valid-basic> ")" ; <hash-of-pred>:: <hash> ;

Ours:

<!-- qm spec/SPEC-0002-ksa-core.md L554-560 -->
> ``` body = { 1 revokes: statement-digest } ``` Withdraws the statement with that digest. **Only that statement's speaker may revoke it** (ADR-0003 D5); a `revoke` naming a statement by another speaker has no effect. Revocation takes effect at `valid.not-before`.

— `spec/SPEC-0002-ksa-core.md`@`bb005ed`, lines 554–560

Both name the revoked object by content digest, never by a serial number. **Who**
may revoke differs, and so does whether a verifier can know it has seen every
revocation: §10 below.

### A6. Names are the issuer's own, and any key may make them

<!-- q L1608-1610 -->
> Note that we do not include an <issuer-loc> option for a name certificate. The issuer needs no authorization in order to create names. Every issuer has that right.

<!-- q L1612-1618 -->
> Similarly, there is no "certification practice statement" for these name certificates. Nothing is implied by a name certificate about the principal(s) being named. A name can be an arbitrary byte string assigned by the issuer and is intended to be meaningful only to that issuer, although other parties may end up using it. A name is not required or expected necessarily to conform to any name string in the physical world or in any other issuer's name space.

Ours:

<!-- qm spec/ARCH-0001-authorization-attestation.md L332 "Names SHALL" .. "issuing principal." -->
> Names SHALL be interpreted only relative to an issuing principal.

— `spec/ARCH-0001-authorization-attestation.md`@`bb005ed`, line 332

<!-- qm spec/ARCH-0002-key-relative-naming.md L67-72 -->
> An extension point is a pair: **`(defining key, local label)`**. Key *K*'s `build-provenance` and key *K′*'s `build-provenance` are different types. They are distinguishable without coordination, and neither needs permission from a registry to exist. Compound reference follows SDSI name chaining exactly.

— `spec/ARCH-0002-key-relative-naming.md`@`bb005ed`, lines 67–72

### A7. The canonical bytes are what is transmitted, hashed and signed

<!-- q L545-548 -->
> All SPKI structures communicated from one machine to another must be in canonical form. If canonical S-expressions need to be transmitted over a 7-bit channel, there is a form defined for base64 encoding them.

<!-- q L675-680 -->
> The canonical S-expression is the form which is hashed for both generating and verifying signatures. These two processes can be thought of as the start and end of an SPKI object's useful life and both require canonical form. The implementer may wish to keep the canonical form around, alongside any parsed version, for convenience in the event memory is not overly limited.

Ours:

<!-- qm spec/ARCH-0001-authorization-attestation.md L363 "The signed payload SHALL" .. "verified canonical bytes." -->
> The signed payload SHALL be the canonical encoding verbatim, carried with an authenticated type indicator. A verifier SHALL verify the signature before decoding and SHALL NOT canonicalize input as part of verification. Any human-facing form SHALL be regenerated from verified canonical bytes.

— `spec/ARCH-0001-authorization-attestation.md`@`bb005ed`, line 363

R-O-05's first clause is SPKI §3.1 restated: one canonical form on the wire.
Its third is compatible with §3.6, where the human form (*advanced* in SPKI) is
a readable rendering converted from the canonical one (L697–L704), though SPKI
never requires a displayed form to be regenerated from verified bytes (C5). Its
second clause, verify before decoding, is **ours**: the draft orders no
verification step (inferred from §3.5, §6.2 and §8, which
describe what is hashed and reduced, never in what order a verifier parses,
hashes and checks). §12 below says what this does to R-0006's reading of the
lineage.

### A8. A missing bound is unbounded, and a result cannot outlive its inputs

<!-- q L1432-1434 "If either" .. "in that direction." -->
> If either is missing, then the certificate is assumed valid for all time in that direction.

<!-- q L2148-2153 "That certificate will have" .. "particular verifier." -->
> That certificate will have a validity period no larger that of any certificate in the loop which formed it, but during that validity period it can be used by the prover instead of the full chain, when speaking to that particular verifier.

Ours:

<!-- qm spec/SPEC-0002-ksa-core.md L430-432 -->
> A statement is **valid at time t** if and only if `not-before ≤ t` when `not-before` is present and `t < not-on-or-after` when `not-on-or-after` is present. A missing bound is unbounded on that side.

— `spec/SPEC-0002-ksa-core.md`@`bb005ed`, lines 430–432

and SPEC-0004 §6.3's `cap`, the earliest `not-on-or-after` met along the path,
which is SPKI's validity intersection (L2063) restricted to time (§10 below).

### A9. Prefer certificates that are short-lived and re-fetched

<!-- q L1500-1502 -->
> The new-cert form requests a new copy of the certificate in question. The assumption is that these certificates are short-lived and that the one triggering the new-cert fetch had expired.

Ours:

<!-- qm spec/ARCH-0001-authorization-attestation.md L360 "Short-lived validity" .. "still representable." -->
> Short-lived validity preferred over revocation-heavy design; revocation still representable.

— `spec/ARCH-0001-authorization-attestation.md`@`bb005ed`, line 360

SPKI's fourth threshold example makes the same move with two keys: a long-lived
off-line grant echoed by short-lived on-line ones (L1344–L1350; §6 below).

### A10. Several algorithms in one root, so that breaking one breaks nothing

<!-- q L1334-1342 -->
> 3. establishing a root key for a trusted service, via multiple algorithms. That is, one could have three root keys, using RSA, DSA and Elliptic Curve signature algorithms (for example), and require that two of them yield a valid chain. This way, if someone were to break an entire algorithm (find a way to invert the algorithm), much less if someone were to break one key in the set of three, the root remains securely established. At the same time, there is fault tolerance. In case one of the keys is revoked, the following certificates remain empowered.

**Ours (inferred), no document of ours says it:** a threshold anchor over keys of
different suites (SPEC-0004 §4.2 permits it; nothing restricts `keys` to one
suite) is this example, and it is the shape a post-quantum transition needs.
SPEC-0002 §6.5's ML-DSA suite is provisional:

<!-- qm spec/SPEC-0002-ksa-core.md L380-383 -->
> Provisional: no test vectors are published for it yet, and it MUST NOT be the only suite a wallet offers until they are. It is specified now because a statement verified decades after signing must survive the post-quantum transition (ARCH survey R-001 §10).

— `spec/SPEC-0002-ksa-core.md`@`bb005ed`, lines 380–383

KSA has two suites to mix where SPKI's example has three algorithms, and that
changes the arithmetic (checked by enumeration): an anchor survives either
algorithm failing only if neither suite holds `threshold` keys or more, so no
2-of-3 over the two suites does. The smallest set that survives either algorithm
failing and also the loss of any one key is 3-of-4, two keys per suite; below
four keys only *n*-of-*n* survives, which SPKI's own `K < N` forbids (C9). Open
question 15.

### A11. One identifier per key, so that principal equality is byte equality

Taken from SPKI by **contrast** (C4 below): SPKI admits several spellings of one
principal and compares them as keys; ours admits one, and compares bytes. Listed
here because the property adopted is SPKI's own goal, stated in its glossary:

<!-- q L377-379 -->
> GLOBAL IDENTIFIER: a globally unique byte string, associated with the keyholder. In SPKI this is the public key itself, a collision-free hash of the public key or a Fully Qualified Name.

Ours:

<!-- qm spec/SPEC-0002-ksa-core.md L841-843 -->
> `kid` is the hash of the full public key, so two keys cannot share a kid without a SHA-256 collision. Identifiers MUST NOT be truncated in signed or hashed bytes.

— `spec/SPEC-0002-ksa-core.md`@`bb005ed`, lines 841–843


## 2. What we adapt, and how

### B1. The root: SPKI's local ACL, widened to accepted signed statements

SPKI's ACL is local and never sent (A2). Its one signed route back into a
verifier's own authority is the *certificate result certificate*:

<!-- q L2144-2157 -->
> In cases where the verifier, Self, has access to a private key, once it has reduced a chain of certificate bodies down to the form: (Self,X,D,A,V) it can sign that generated body, using its private key, producing an SPKI certificate. That certificate will have a validity period no larger that of any certificate in the loop which formed it, but during that validity period it can be used by the prover instead of the full chain, when speaking to that particular verifier. It is good only at that verifier (or at another which trusts that verifier, Self, to delegate the authorization A). Therefore, one option by the verifier is to sign and return the result 5-tuple to the caller for this later use.

<!-- q L2159-2162 -->
> If it isn't important for any other verifier to accept this "result certificate", it can even be signed by a symmetric key (an HMAC with secret key private to the verifier), although such keys are not defined in this standard.

Ours: ADR-0003 D3,

<!-- qm spec/ADR-0003-ksa-core-decisions.md L49 "**Trust anchors may be signed or unsigned.**" .. "person or organisation.**" -->
> **Trust anchors may be signed or unsigned.** An anchor may be an unsigned local decision, the owner's own trust statement, or a trust statement signed by any key — including a third party — that has been **verified and then accepted** into a context's anchor list. **Acceptance is a local act by a persona whose controller is a person or organisation.**

— `spec/ADR-0003-ksa-core-decisions.md`@`bb005ed`, line 49

**The adaptation.** A KSA anchor may come from three sources (SPEC-0004 §4.3);
SPKI has the first only. SPKI's result certificate corresponds to the second,
`own statement` — a persona's own trust statement, anchored — with two
differences (inferred): it is computed from a reduced chain and so cannot outlive
any link (A8), while a KSA own statement carries whatever validity its signer
gives it; and it may be MACed, while KSA has no symmetric suite (SPEC-0002 §6.2).
Nor is it an anchor in SPKI: it is a certificate under the verifier's own key,
which grants nothing until the verifier's ACL treats that key as `self`, and the
draft leaves that step to the implementation (the requirements lane infers the
same, `draft-ietf-spki-cert-structure#R-0437`). The third source, a third
party's statement accepted by a human-controlled persona (SPEC-0004 §4.4), has
no SPKI counterpart. R-I-02, read with SPEC-0004 §4.3's rule that a signature
never makes an anchor, is SPKI's position kept: an imported object does not
become an anchor by arriving.

### B2. *k*-of-*n*: SPKI's construct, with its arithmetic and membership tightened

<!-- q L1287-1289 -->
> <subj-thresh>:: "(" "k-of-n" <k-val> <n-val> <subj-obj>* ")" ; where K < N, and there are N <subj-obj> subjects listed.

Ours:

<!-- qm spec/SPEC-0002-ksa-core.md L530-535 -->
> body = { 1 about: [+ attribute-range], ? 2 may-delegate: delegation-constraints, ? 3 trusts: [2* kid], ? 4 threshold: uint } delegation-constraints = { ? 1 depth: uint, ? 2 ranges: [+ attribute-range], ? 3 allow-keys: [+ kid], ? 4 exclude-keys: [+ kid], ? 5 not-on-or-after: time }

— `spec/SPEC-0002-ksa-core.md`@`bb005ed`, lines 530–535

<!-- qm spec/SPEC-0002-ksa-core.md L911-915 -->
> The threshold vectors use `ARCH-0001`'s letters: `k` is `threshold` (the `n` of §8.6) and `n` is the length of `trusts`. **V8 owns `1 ≤ k ≤ n`** (N-7, N-8). `n = len(members)` holds by construction, because §8.6 has no `n` field: `n` is the array head of `trusts`. Writing a disagreement takes a field the closed map refuses (N-9, V7) or a head the decoder refuses (N-10, V5).

— `spec/SPEC-0002-ksa-core.md`@`bb005ed`, lines 911–915

**The adaptation**, item by item in §6 below: members are keys only, never names,
hashes of objects or nested thresholds; `n` is not written, so it cannot
disagree with the list; the bound is `1 ≤ k ≤ n`, so *n*-of-*n* exists where
SPKI's `K < N` excludes it; distinctness is by `kid`; and coverage is defined for
attestations as well as for delegation onward.

### B3. Delegation: SPKI's boolean, generalised to a counted, width-limited grant

<!-- q L1379-1383 -->
> <deleg>:: "(" "propagate" ")" ; This optional field, if present, notes that the <subject> has not only the permission given in the <cert>'s <tag> field but also the permission to delegate that (or some portion of it) to others.

<!-- q L2059-2063 -->
> <i1,s1,d1,a1,v1> + <i2,s2,d2,a2,v2> yields <i1,s2,d2,a,v> if: s1 = i2 d1 = "t" a = the intersection of a1 and a2 v = the intersection of v1 and v2

Ours:

<!-- qm spec/ARCH-0001-authorization-attestation.md L339 "Delegation SHALL be explicit" .. "not intersected silently to empty." -->
> Delegation SHALL be explicit and bounded on the delegation statement: absent means one hop with no onward delegation; present, it SHALL state an integer `depth` and MAY state an onward scope allow-list (`ranges`), key allow/exclude lists, and a validity cap. Each hop's scope SHALL be within the previous hop's, and a widening SHALL be reported as such, not intersected silently to empty.

— `spec/ARCH-0001-authorization-attestation.md`@`bb005ed`, line 339

**The adaptation** (DL-0025): `(propagate)` absent is `may-delegate` absent,
exactly; `(propagate)` present becomes a `depth`, plus three width controls SPKI
has no field for (`ranges`, `allow-keys` and `exclude-keys`) and a validity cap.
Each SPKI issuer still controls its own subject's onward right, as each KSA
issuer sets or drops its own `may-delegate`. What KSA adds is a count, set at
the root, that every hop must lower by at least one (SPEC-0004 §6.3 item 6,
quoted in §7.2). SPKI's flag is the same at every hop and a count cannot be, so
a `(propagate)` certificate has no one depth that fits every chain it can sit in
(inferred). §7 below gives the mapping both ways and what it loses.

### B4. Tags: SPKI's algebra, typed, and checked by containment

<!-- q L1393-1400 -->
> The simplest tag is an S-expression with no *-forms. This is a specific permission which must be passed along and used intact. A tag with *-forms represents a set of specific permissions. Any subset of such a set of permissions may be delegated by a principal empowered to delegate. When one is reducing the 5-tuples from such certificates, one intersects the adjacent tag sets to find a resulting tag set.

Ours:

<!-- qm spec/SPEC-0003-ksa-definitions.md L247-253 "A type's base kind fixes" .. "safe to load from anyone." -->
> A type's base kind fixes, exactly, five things: what an **assignment** is, what a **range** is, when a value is **in** a range, when one range is **within** another, and what the **unbounded** range is. Every base kind is implemented by the verifier; a definition chooses one and may constrain it (§8), but cannot change its algebra. This is the fixed core of ARCH-0002 DEC-008: definitions are declarative, and processing they cannot alter is what makes them safe to load from anyone.

— `spec/SPEC-0003-ksa-definitions.md`@`bb005ed`, lines 247–253

**The adaptation.** SPKI's tags are untyped, positional S-expressions whose
meaning is the application's; KSA's scope is a list of attribute ranges, each
of a key-relative type whose base kind fixes membership and containment. SPKI
computes an intersection at every hop; KSA checks that each hop is **within**
the last and fails the path otherwise (C1). R-0006 §4.6 shows the two agree on
every path KSA accepts. §8 below finds that SPKI-06's own intersection rules are
incomplete and self-contradictory, which strengthens the case for the typed
form rather than weakening it.

### B5. An unknown version: SPKI ignores the certificate, we reject the statement

<!-- q L1171-1177 -->
> Version numbers are alphanumeric strings. If the <version> field is missing from an object, it is assumed to be (version "0"), which is the version of all objects in this draft. Elaboration of version numbers, possibly with multiple fields, are left for later to define. A certificate containing an unrecognized version number must be ignored.

Ours:

<!-- qm spec/SPEC-0002-ksa-core.md L847-849 -->
> An unknown suite is unverifiable, never silently accepted; an unknown kind or field is invalid. A verifier MUST NOT skip what it does not understand (ARCH-0002 P5).

— `spec/SPEC-0002-ksa-core.md`@`bb005ed`, lines 847–849

<!-- qm spec/ARCH-0002-key-relative-naming.md L394-396 -->
> Beyond the three: **an unknown field in a signed payload is an error, not something to skip.** The default is must-understand; skippability is opt-in and explicit, never the other way round.

— `spec/ARCH-0002-key-relative-naming.md`@`bb005ed`, lines 394–396

**The adaptation (inferred).** For an authorization certificate, *ignored* and
*invalid* have the same effect: nothing is granted. They differ in what is
reported, and P5's wording, as SPEC-0002 §13.5 states it above, is the opposite
of SPKI's. SPKI's tag rule gets P5's effect by construction: an added trailing
field narrows, and one a verifier cannot match grants nothing (L1405–L1408, §8
below). The ignore rule also names certificates only: a CRL, delta-CRL, reval
or ACL carries a `version` with no rule for an unknown value (inferred; §15.3). An
import of an SPKI object with an unrecognised version is rejected (ours).

### B6. Time: SPKI's fixed-width UTC strings, made decoder-enforced

<!-- q L1445-1454 -->
> A date field is an ASCII byte string of the form: YYYY-MM-DD_HH:MM:SS always UTC. For internal use, it is treated as a normal byte string. For example, "1997-07-26_23:15:10" is a valid date. So is "2001-01-01_00:00:00". <date> fields are compared as normal ASCII byte strings since one never needs to compute the size of a time interval to test validity -- only determine greater-than, less-than or equal.

Ours:

<!-- qm spec/SPEC-0002-ksa-core.md L237-239 "An even `T` whose `s` is a multiple of 86400 MUST be rejected" .. "Leap seconds are not represented." -->
> An even `T` whose `s` is a multiple of 86400 MUST be rejected, so every instant has exactly one encoding. Leap seconds are not represented.

— `spec/SPEC-0002-ksa-core.md`@`bb005ed`, lines 237–239

**The adaptation.** Same idea, a total order on a fixed form in UTC, with what
SPKI left unstated now stated: SPKI gives no rule for a malformed date, and a
`<date>` is a `<byte-string>` (L1443) and so may carry a display type, which
§3.2 makes unequal to the same bytes without one (inferred: such a date compares
unequal, or not at all). KSA's time has one encoding per instant and rejects
the rest. Whether SPKI's `not-after` instant is itself valid is not said: L1432
defines neither bound. Ours is half-open (§10 below).

### B7. Determinism: SPKI's freedom of algorithm, with the input order removed

<!-- q L108-111 -->
> The process of reducing SPKI sequences and an ACL to determine an authorization result is spelled out here, but an individual implementer is free to design new reduction algorithms as long as they are computationally equivalent to the one defined here.

<!-- q L1841-1844 -->
> A <sequence> is an ordered sequence of objects that the verifier is to consider when deciding to grant access. By reducing certificates in the sequence, the verifier will establish that the final subject (key or object) has been granted authority through the sequence.

Ours:

<!-- qm spec/ARCH-0001-authorization-attestation.md L334 "Authorization composition SHALL" .. "and ACL." -->
> Authorization composition SHALL be deterministic given an ordered cert set and ACL.

— `spec/ARCH-0001-authorization-attestation.md`@`bb005ed`, line 334

<!-- qm spec/SPEC-0004-ksa-trust-evaluation.md L130-133 -->
> An evaluator MUST produce the same answer for the same inputs: the anchors of one context, the statement set, the definitions, the key store, the ask and the evaluation time. Nothing else — no network, no clock other than the evaluation time, no ordering of inputs — may affect the result.

— `spec/SPEC-0004-ksa-trust-evaluation.md`@`bb005ed`, lines 130–133

**The adaptation.** SPKI fixes the result and frees the algorithm, over an
*ordered* sequence. R-M-05 keeps the ordered set; SPEC-0004 §3 forbids input
order from mattering at all, which is stronger than both. R-M-05's wording is
SPKI's (open question 13).

### B8. The human form: SPKI's advanced form, made one-to-one

<!-- q L697-704 -->
> [SEXP] includes a general purpose utility program for converting between canonical and advanced S-expression form. In the advanced form, individual byte strings may be expressed without length fields (if they are what most languages consider text tokens), may be written as quoted strings (under normal C string rules), or may be individually hex or base64 encoded. Also in the advanced form, white space between list elements is allowed for readability and ignored on conversion to canonical form.

Ours:

<!-- qm spec/SPEC-0002-ksa-core.md L662-667 -->
> A statement has exactly one **binary form** — its KSA-CBOR TBS, which is what is signed, hashed and transmitted — and one **human-review form**, written in YAML, which is what people read, write and review. The human form represents the binary form exactly: every field, every value, and the signature. A conforming tool converts between the two **one-to-one**, with the one exception of §11.3 (text that reads as bytes):

— `spec/SPEC-0002-ksa-core.md`@`bb005ed`, lines 662–667

**The adaptation.** SPKI's advanced form maps **many-to-one** onto the canonical
form: a byte string may be a token, a quoted string, hex or base64, and white
space is dropped (L711–L717). SPEC-0002 §11.3 fixes one spelling per value
(bytes only as `'0x…'`, integers decimal only). MD-3's wording sits between the
two (§5.4 below).

### B9. Principals: SPKI's preference for a hash of the key, made the only form

<!-- q L1204-1210 -->
> <issuer>:: "(" "issuer" <principal> ")" ; <principal>:: <pub-key> | <hash-of-key> ; <hash-of-key> might be the preferred <principal>, not merely for size but also in case one is using small RSA keys and protecting them from cryptanalysis by keeping them secret.

Ours: `says` is a `kid` (SPEC-0002 §7.1); the key itself travels only in a
`key-publish` or `self` body, or as the envelope's unauthenticated `pub` hint
(§5). ADR-0005:

<!-- qm spec/ADR-0005-dec-003-key-identifier.md L36-38 -->
> 1. **Form.** An issuer or subject key is identified on the wire by its **`kid`**: a 32-octet byte string, `SHA-256(public-key encoding)` (`SPEC-0002` §4.5). Text renderings are presentation only (`SPEC-0002` §11).

— `spec/ADR-0005-dec-003-key-identifier.md`@`bb005ed`, lines 36–38

**The adaptation.** SPKI lets a principal be the key or any hash of it; KSA
makes SPKI's preferred form the only one, under one fixed digest. §11 below
shows from SPKI's own test vector what the other forms cost.

## 3. What we reject, and why

### C1. Absorbing a widening by intersection

SPKI's top-level rule (B3's second quotation) takes the intersection of the two
tags and of the two validities, and continues. A hop that widens is narrowed
silently; only a pair whose intersection is `null` stops reduction:

<!-- q L2073-2082 -->
> The intersection of a1 and a2 is given below. In the most basic case, If a1 is (tag (*)), a = a2. If a2 is (tag (*)), a = a1. If a1 == a2, a = a2. Otherwise, a = "null" and the 5-tuple doesn't reduce.

Ours: R-M-10 (B3) and

<!-- qm spec/SPEC-0004-ksa-trust-evaluation.md L284-285 -->
> **Widening fails the path.** If any condition fails, `s` is not followed; no partial or repaired version of it is.

— `spec/SPEC-0004-ksa-trust-evaluation.md`@`bb005ed`, lines 284–285

Rejected because a widening is evidence of a mistake or an attack, and
intersecting it away hides both. R-0006 §4.6 states the consequence exactly:

<!-- qm research/0006-mechanism/report.md L1134-1138 "The paths that differ are those with a hop that widens" .. "a choice, not an omission." -->
> The paths that differ are those with a hop that widens: SPKI intersects and continues with the narrower result, and `SPEC-0004` rejects the path. The core chose to **fail closed** where SPKI repairs. That matches the reject-never-repair rule of `SPEC-0002` §4.3 and §13.1, and it is a choice, not an omission.

— `research/0006-mechanism/report.md`@`bb005ed`, lines 1134–1138

### C2. One signature form for certificates and for files

<!-- q L1014-1019 -->
> <signature>:: "(" "signature" <hash> <principal> <sig-val> ")" ; A signature object is typically used for a certificate body and typically follows that <cert> object in a <sequence>. One can also sign objects other than certificate bodies, of course. For example, one can form the signature of a file.

Ours:

<!-- qm spec/SPEC-0002-ksa-core.md L824-826 "A signature binds its DS label (§6.4)." .. "provided that protocol also domain-separates." -->
> A signature binds its DS label (§6.4). A key that is also used in another protocol cannot have a KSA signature replayed there, or a signature from there replayed as KSA, provided that protocol also domain-separates.

— `spec/SPEC-0002-ksa-core.md`@`bb005ed`, lines 824–826

Rejected. An SPKI `signature` carries the hash of whatever it signs and nothing
naming what kind of thing that is; the signed object's own first element is
its type indicator, and a file has none (inferred). A file whose bytes happen
to parse as a canonical `(cert …)` is, to a verifier, a signed certificate.
SPEC-0002 §6.4's labels exist to make that impossible.

### C3. A threshold that states its own *n*

`<n-val>` (B2's quotation) is a second statement of the list length, which a
verifier must check against the count. Ours, from the fixture that tested it:

<!-- qm design-log/0019-threshold-fixture/review.md L16-19 "needs an `n` field" .. "exists only to be checked." -->
> needs an `n` field, which is a signed-bytes change, and the model advises against one: a field that can disagree exists only to be checked.

— `design-log/0019-threshold-fixture/review.md`@`bb005ed`, lines 16–19

Rejected; SPEC-0002 §8.6 has no `n` field. On import an SPKI threshold whose `N`
disagrees with its list is rejected, never repaired (ours, under P5.1).

### C4. Several identifiers for one key

An SPKI principal may be the key, its md5 hash, its sha1 hash, or a hash under a
URI-named algorithm, each with or without `uris` (L999, L1206, L2289). The hash
is over the key's whole canonical S-expression, algorithm name included:
**reproduced in this pass**, md5 and sha1 of the canonical key decoded from
L826–L829 equal the values printed at L1004 and L1007. So one RSA key under
`rsa-pkcs1-md5` and under `rsa-pkcs1-sha1` is two principals (inferred from the
reproduction). Rejected by ADR-0005:

<!-- qm spec/ADR-0005-dec-003-key-identifier.md L75 -->
> | **per-suite digest** | `kid`s of one key would differ by suite, contradicting "the key is the principal" |

— `spec/ADR-0005-dec-003-key-identifier.md`@`bb005ed`, line 75

### C5. A signed display hint that verifiers ignore

<!-- q L1185-1192 -->
> This optional field gives a display hint for the entire certificate. This display parameter does not affect certificate chain reduction, but is provided to aid user-interface software in certificate display. At this time, we have no such hints defined. This field is up to developers to define as they see fit. For verifiers of certificates, this field is treated as a comment.

<!-- q L1552-1553 -->
> This optional field allows the issuer to attach comments meant to be ignored by any processing code but presumably to be read by a human.

Rejected as a source of what a person is shown. Both fields are inside the
certificate's canonical bytes and so are signed (A7), yet no check relates them
to the tag: a certificate may display one permission and grant another, and
nothing in reduction notices (inferred). R-O-05's third clause regenerates every
human-facing form from verified bytes (A7's quotation), and SPEC-0003 §10
renders a statement from its definitions; SPEC-0002 §11.3's annotations, the
nearest thing to a comment, are never signed at all.

### C6. A certificate whose fields may come in any order

<!-- q L775-782 -->
> The following are the definitions of the top level objects which a verifying program may encounter. Note that the main object, <cert>, is sub-type based so the parameter fields may be in any order, but the BNF suggests a fixed order. We use the BNF definition to indicate that there may not be more than one of each of the listed fields, and also to suggest (for readability) that the certificate parts be presented in the order given. This document will use that order.

Rejected. A reordered certificate is grammatical, canonical and differently
hashed (inferred from L553–L555 and L775–L782), so one certificate has as many
identities as orderings. KSA sorts map keys and rejects any other order
(SPEC-0002 §4.2 item 3, §4.3). §5.3 below takes this to ADR-0004's scoring.

### C7. Type and algorithm names from a global or registry namespace

<!-- q L723-733 -->
> Top level object names are defined in this document along with certain algorithm names. <tag> objects are user-defined, using a language for describing sets of permissions given here, and in the process, the defining user can choose any object names he or she wishes. For the definition of new algorithm names, it is our preference that this be taken on by IANA [RFC1780] for single-word standard names. In the interest of maximum flexibility we also permit users to define their own algorithm names via a normal URIs (which presumably point to descriptions of the algorithms or even to code).

<!-- q L759-765 -->
> It is standard SPKI/SDSI practice to use names starting with a lower case letter, followed by lower case letters, digits and hyphens for object types. SPKI/SDSI is case-sensitive, so the byte-string "RSA" is not the same as "rsa". Non-standard object types (i.e. <tag>s defined by an application developer) are unconstrained, may have display types and may even be URIs pointing to documentation of the object type.

Rejected for the native model by P1 and ADR-0004 item 3; kept for interchange.
SPKI's top-level types are fixed by the document, its algorithm names were to
come from IANA or from URIs, and its tag names are whatever the defining user
writes, with no key attached. P1's critique fits exactly:

<!-- qm spec/ARCH-0002-key-relative-naming.md L82-84 -->
> Private-use ranges are not the answer: they give **escape from a registry, not a namespace**. Two parties using the same private label collide, and nothing in the encoding can disambiguate them because no principal is attached.

— `spec/ARCH-0002-key-relative-naming.md`@`bb005ed`, lines 82–84

In SPKI a tag's meaning is fixed in practice by the verifier whose ACL roots the
chain (A2), which is a defining key left implicit (inferred). §8 below.

### C8. More than one encoding of an integer

<!-- q L609-615 -->
> The bytes of a binary integer are twos-complement, in network standard order (most significant byte first). On the assumption that they are signed, a leading 0x00 or 0xFF byte may need to be present, but redundant bytes of sign need not be. The integer value 0 is expressed as a 1-byte string holding the 0 byte, not as the empty string "".

Rejected. The rule permits redundant sign octets without requiring them, so one
integer has several canonical byte strings (inferred). Every integer field in
the draft's canonical key examples (14 fields across the RSA public key, the RSA
private key and the DSA public key, L826–L939, decoded in this pass) is
minimal, so the examples keep a rule the text never states.
KSA requires the shortest head (SPEC-0002 §4.2 item 1) and rejects a longer one
(§4.3). The `version` field shows the same gap twice over (SI-1).

### C9. A threshold bound that excludes *n*-of-*n*

`K < N` (B2's quotation). Rejected: SPEC-0002 §8.6 allows `k = n`, and TV-10 is
its positive vector. SPKI's own examples need it (SI-2, §6 below).

## 4. Mapping to our decisions

Verdicts, exactly six. **adopts**: we take the source's rule or position and the
two agree. **adapts**: we take the source's idea and change it, and the change
is stated. **rejects**: we deliberately do not take the source's rule, for a
stated reason. **constrains**: one side narrows what the other leaves open, or
the source narrows a claim of ours. **conflicts**: one object or implementation
cannot satisfy both. **silent**: one side does not reach the other's subject.
The source has no BCP 14 keyword, so its column gives locators, not levels. Our
documents are cited by id and section at `bb005ed` (paths in the standing table
above); the words are in the `qm` markers of §1 to §3 and §5 to §11.

| # | Ours | Source | Verdict |
|---|---|---|---|
| 1 | ARCH-0001 §1 items 2–4 and G3: local names, tag intersection, thresholds and SPKI-style reduction, each attributed to SDSI/SPKI; G4's *k*-of-*n*; ARCH-0002's correction note (SPKI contributes ideas; reproducing its formalism is no aim) | §4–§8 | **adopts**, as ideas. Every row below that adapts or rejects is consistent with the correction note |
| 2 | R-M-02; P2 (the speaker is the key); SPEC-0004 §1 | L416–L418, L89–L93, L1206 | **adopts** (A1) |
| 3 | R-M-03; P1's SDSI chaining | L1608–L1618, L1684–L1690 | **adopts** (A6) |
| 4 | R-M-04, read with ARCH-0001 §4.2's note and P6 | name and authorization certificates share the type `cert` and differ by issuer form and the absence of tag and `(propagate)` (L1636–L1648); separate procedures, 4-tuple and 5-tuple (L448–L453, §5.3, §8) | **constrains**. SPKI satisfies R-M-04 read as two functions with two procedures, the reading ARCH-0001 §4.2 now gives it, and not read literally as two object kinds (§9) |
| 5 | R-M-05 (deterministic given an ordered set); SPEC-0004 §3 (no input order may matter) | L108–L111, L1841–L1844 | **adapts** (B7) |
| 6 | R-M-06, G4; SPEC-0002 §8.6 threshold form; ADR-0004's threshold fixture | §4.5.3, §8.4 | **adapts** (B2, §6): keys only, no `n` field, `1 ≤ k ≤ n`, distinct by `kid` |
| 7 | R-M-08: *within* defined for every profile and type claimed | §8.3's six rules define no meet of two *-forms, and rule 2 contradicts §4.8 (SI-3, SI-4) | **constrains**. SPKI-06 as written does not meet R-M-08 for its own tag language (inferred). SPEC-0003 §6 defines *within* for ten of its eleven base kinds; the eleventh, `record`, has no range and cannot be delegated (§8) |
| 8 | R-M-09 (time ∩ optional online checks); ARCH-0001 §4.1 `Validity.online_check` and the §5.5 gap | §8.2 L2065–L2071 defines exactly this intersection; §4.9.2, §7 | **constrains**. R-M-09 is SPKI's rule; KSA specifies its time half only (SPEC-0004 §6.3 `cap`) and leaves the online half open (§10) |
| 9 | R-M-10 as rewritten by DL-0025; SPEC-0002 §8.6 `may-delegate`; SPEC-0004 §6.3 items 3, 6 | `(propagate)` L1379–L1383; reduction L2059–L2063 | **adapts** (B3, §7). The flag maps onto a depth per chain, not per certificate (§7.3) |
| 10 | R-M-10's last clause: a widening reported, not intersected away; SPEC-0004 §6.3 (C1's quotation) | §8.2 intersects tags and validities and continues | **rejects** (C1) |
| 11 | R-O-01: every signed object's issuer specifiable as `KeyId` | issuers are RSA or DSA keys or their md5/sha1 hashes (§3.8.1, L1206, L2289, L2325–L2326) | **conflicts**, for import. No KSA suite defines an RSA or DSA public-key encoding (SPEC-0002 §6.2 reserves 3–7, specifies none), and a SHA-256 `kid` cannot be computed from an md5 or sha1 hash. Every issuer in this draft's algorithms is unspecifiable as a KSA `KeyId` today (§11) |
| 12 | R-O-02 | `new-cert` L1500–L1502; example 4 L1344–L1350 | **adopts** (A9) |
| 13 | R-O-03 | the canonical form is [SEXP] with two stated restrictions (L522–L526) | **silent**. R-O-03 governs our encoding; SPKI shows the pattern it asks for, a cited base plus a stated profile (inferred) |
| 14 | R-O-05 | L545–L548, L675–L680; the object's type is its first element, inside the hashed bytes (L524–L526) | **adopts** clauses 1 and 3 (A7); clause 2, verification order, is ours. SPKI's type indicator is authenticated but its signature form is not domain-separated (row 30) |
| 15 | R-I-01; ARCH-0001 §6 SPKI row (I and E, no loss listed; quoted in §13); WP2 | the whole draft | **constrains**. The row owes at least the losses of §13, and its **I** is not realisable natively today (row 11) |
| 16 | R-I-02 | ACL local and unsent (L1787–L1792); the verifier is the only root (L1162–L1163) | **adopts** |
| 17 | ARCH-0001 §4.1 `Principal` (`Key`, `KeyId`, `Name`, `Threshold`, `Group`) and `Threshold.members: [Principal]`, against SPEC-0002 §8.6's `[2* kid]` | `<subj-obj>`: principal, name, object hash, keyholder or a nested threshold (L1232–L1233, L1287) | **constrains**. ARCH-0001's logical type is SPKI's; SPEC-0002 narrows it to flat key sets, as DL-0019 recorded (§6) |
| 18 | DEC-002, ADR-0004 item 1 (KSA-CBOR) | §3: canonical S-expressions | **constrains**. Under option 5 every SPKI object is a translation, never carried byte for byte (§5) |
| 19 | ADR-0004 item 2, the rejecting decoder | a canonical length has no leading zero and lists carry no white space, by grammar (L550–L553, L589–L594); no receiver rule stated | **adopts** the property; ours states it as an obligation, SPKI only as a grammar (§5) |
| 20 | ADR-0004 item 3 and MD-3's exclusion of IANA tags | display types are MIME types and part of a string's identity (L577–L585); algorithm names preferred from IANA (L729–L730) | **rejects**, for the native model (C7) |
| 21 | ADR-0004's scoring cells for option 1 on order-only divergence, namespace governance and SPKI fidelity, and its paragraph headed Why 5 over 1 (all quoted in §5.3) | L775–L782, L609–L612, L577–L585, L729–L730, §3.8.1 | **constrains** all four cells; none moves the decision, two move it further toward option 5 (§5.3) |
| 22 | ADR-0004's acceptance test; DL-0019; TV-10 (`k = n = 3`) | `K < N` (L1289) | **conflicts**, for export. TV-10 has no SPKI-06 form as printed (§6) |
| 23 | MD-3: YAML is the human form, with a canonical **one-way** mapping | the advanced form, many spellings per canonical value (L697–L704, L711–L717) | **constrains**. MD-3's wording admits SPKI's many-to-one design; SPEC-0002 §11 excludes it (row 33, §5.4) |
| 24 | MD-3 and P1 / ADR-0001: type identity is `(defining key, label)` | tag names chosen freely, object types fixed by the document or given as URIs (L723–L733, L759–L765) | **rejects** (C7) |
| 25 | P5; SPEC-0002 §13.5 | an unrecognised version is ignored (L1176–L1177) | **adapts** (B5) |
| 26 | P5.1: a non-canonical serialisation is a rejection | the grammar rejects a non-canonical length or list; it cannot see a reordered certificate (C6), a redundant sign octet (C8) or a spelled-out default (SI-1) | **constrains** (§5) |
| 27 | P5.1's note on an option-1 default display hint | no default display type exists in this draft (`default` occurs 0 times; L581–L585) | **constrains**. The crack P5.1 and R-0006 §3.5 found is RFC 9804's, not SPKI-06's (inferred, §5) |
| 28 | P6: a name is an attested string | a name certificate is an ordinary `cert` stating that a name in its issuer's space denotes its subject (L1636–L1650) | **adopts** in form; SPKI's names also pass authority through unchecked, which P6 does not say (§9) |
| 29 | DEC-004 option 1, SPKI tags unchanged; R-0006 §4.1 (`AIntersect` closed) | §8.3, §4.8 | **constrains**. Option 1 cannot be taken from this source unchanged: its meet is incomplete and self-contradictory (§8) |
| 30 | SPEC-0002 §6.4, §13.2: every signature binds a DS label | one `signature` form for certificates and files (L1016–L1019) | **rejects** (C2) |
| 31 | SPEC-0002 §4.2–§4.3, §7.1: sorted keys, shortest heads, absent fields omitted, closed maps | free `cert` order (L775–L782); optional sign octets (L611–L612); defaults written or omitted (L1171–L1173, L1647) | **rejects** (C6, C8, SI-1) |
| 32 | SPEC-0002 §4.4 time | §4.9.1 | **adapts** (B6) |
| 33 | SPEC-0002 §11 human-review form, one-to-one | §3.6 | **adapts** (B8) |
| 34 | SPEC-0002 §7.2 target type 2 | `object-hash` (L1261–L1265) | **adopts** (A4) |
| 35 | SPEC-0001 §3.2 controllers; SPEC-0004 §4.5 evidence about controllers | `keyholder`: statements about the holder, not the key (L1269–L1281) | **silent**. KSA has no syntactic split between a statement about a key and one about its holder (open question 14) |
| 36 | SPEC-0002 §8.7 `revoke`; ADR-0003 D5 | `canceled` names each withdrawn certificate by its hash (L1919–L1923) | **adopts** the digest (A5) |
| 37 | ADR-0003 D5: only the speaker may revoke | the CRL or reval is signed by the principal the certificate's online test names, who need not be its issuer (L1460–L1463, L1929–L1930, L1963–L1964) | **conflicts**, for import: an SPKI CRL from a designated third party has no KSA form (§10) |
| 38 | SPEC-0004 §7.1, count-reporting revocation; R-0007 P4 | non-overlapping instrument intervals (L1907–L1910) | **constrains**. The source is the deterministic alternative SPEC-0004 did not take; R-0007 P4 asks that the choice be recorded (§10) |
| 39 | ADR-0003 D3; SPEC-0004 §4.2–§4.4 | ACL (§6.1); result certificate (§8.7) | **adapts** (B1) |
| 40 | ADR-0005 items 1–4: one `kid`, fixed digest, suite not hashed | several spellings per principal; algorithm and `uris` inside the hashed key (§3.8.1–§3.8.2, reproduced) | **rejects** SPKI's form (C4); evidence on ADR-0005's open sub-question both ways (§11) |
| 41 | ADR-0005, interchange: a foreign identifier that disagrees with the computed `kid` is rejected | a hash principal names the key by md5 or sha1 of its S-expression | **constrains**. An SPKI hash principal can be checked only once its key is in hand and a suite encodes it (§11) |
| 42 | SPEC-0003 §5.4, §6 | `*`-forms `set`, `range`, `prefix` (L2358–L2363); orderings never defined (SI-15) | **adapts** (B4); import of `prefix` and of undefined orderings is lossy (§8, §13) |
| 43 | SPEC-0004 §6.4: coverage by *n* members with the same target, type and value; onward delegation with identical `about` and `may-delegate` | paths converge on one subject; how the joined 5-tuple's tag, validity and delegation combine is not said (L1304–L1317, L2128–L2134) | **constrains** (§6; open question 2) |
| 44 | SPEC-0004 §6.4 distinctness by `kid`; §11.5 | L1296 asks for distinct paths; no rule says the listed subjects must be distinct | **adapts**: KSA closes SPKI's gap (§6) |
| 45 | SPEC-0004 §6.5: at most 16 edges | no bound on chain length; name growth bounded only by the theory document (L1737–L1739) | **silent** on names; open question 6 |
| 46 | SPEC-0001 §5.3, the external statement | §6.2 `sequence` | **constrains**. It is the one native-compatible route for an SPKI-06 object, and it needs the speaker mapped to a `kid` (row 11) |
| 47 | ARCH-0001 §4.3 step 1 and §5.5: compound SDSI names, owed by SPEC-0004 (mofn#143, DL-0028) | §5.2–§5.3 | **constrains** (§9; open questions 4–6) |
| 48 | R-0007 §3.5: UC-5 written in SPKI with list-prefix tags | §8.3 rule 2 (L2096–L2097) | **conflicts**. A verifier that implements §8.3 as printed rejects R-0007's chain at its first hop (§8) |
| 49 | SPEC-0001 §8.1, presentation nonce | one-time revalidation nonce (L1493–L1498, L1977–L1979) | **silent**. Ours proves freshness of a presentation; SPKI's, of a validity answer |
| 50 | SPEC-0004 §4.2 threshold anchors with SPEC-0002 §6.5 | example 3, a 2-of-3 root across three algorithms (L1334–L1342) | **silent**. No document of ours names the pattern (A10; open question 15) |


## 5. MD-3, ADR-0004 and DEC-002

MD-3, the dated narrowing of 2026-09-28:

<!-- qm project/meetings/2026-09-28.md L51-54 -->
> **MD-3 · DEC-002 — narrow to option 5.** CBOR data model, no IANA tags, COSE as export only; type identity is `(defining key, label)` per P1; YAML is the human form with a canonical one-way mapping. Option 2 is retained only as the comparison fixture. D5 fixture package due **Oct 28**, then ADR.

— `project/meetings/2026-09-28.md`@`bb005ed`, lines 51–54

ADR-0004 accepted option 5 on 2026-10-25 and closed MD-3. Nothing here reopens
it; only an ADR accepts a decision:

<!-- qm CONTRIBUTING.md L107-108 "**Never mark" .. "accepts a decision." -->
> **Never mark a DEC-* accepted in a PR description, a Zoom note, or a commit message.** Only an ADR accepts a decision.

— `CONTRIBUTING.md`@`bb005ed`, lines 107–108

This section exists because ADR-0004 was taken without a second reader and an
extraction that can only confirm is not evidence. The draft is not a COSE or
CBOR document, so there is no header-by-header mapping to give; the analogue,
construct by construct, is §5.6. **The draft is evidence about option 1 in use**:
ADR-0004 scored option 1 from RFC 9804, which defines the encoding and no
certificate, and this draft is the certificate system that encoding was built
for.

### 5.1 What SPKI's canonical form is, and is not

**A canonical encoding fixed at the grammar level.** Every value is a byte
string or a list; a byte string carries its length in ASCII decimal with no
superfluous leading zero; a list is parenthesised, non-empty, unseparated, and
opens with a byte string, its type:

<!-- q L371-372 -->
> CANONICAL S-EXPRESSION: an encoding of an S-expression that does not permit equivalent representations and is designed for easy parsing.

<!-- q L550-555 -->
> A canonical S-expression is formed from binary byte strings, each prefixed by its length, plus the punctuation characters "()[]". The length of a byte string is a non-negative ASCII decimal number, with no unnecessary leading "0" digits, terminated by ":". The canonical form is a unique representation of an S-expression and is used as the input to all hash and signature functions.

<!-- q L589-594 -->
> <byte-string>:: <bytes> | <display-type> <bytes> ; <bytes>:: <decimal> ":" {binary byte string of that length} ; <decimal>:: <nzddigit> <ddigit>* | "0" ; <nzddigit>:: "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ; <ddigit>:: "0" | <nzddigit> ; <display-type>:: "[" <bytes> "]" ;

<!-- q L434-437 -->
> S-EXPRESSION: the data format chosen for SPKI/SDSI. This is a LISP-like parenthesized expression with the limitations that empty lists are not allowed and the first element in any S-expression must be a string, called the "type" of the expression.

**One encoding per S-expression, by construction.** The grammar has no
alternative: no white space, no optional length, one spelling of each length.
`03:abc` is not a `<bytes>`. All eight base64 canonical blocks in the draft
(L656–L657, L826–L829, L872–L887, L929–L939, L1005, L1008, L1704–L1707,
L1814–L1820) decode and parse under a strict reader of this grammar with no
octet left over (checked in this pass). And a hash is over those bytes: md5 and
sha1 of the canonical key at L826–L829 reproduce L1004 and L1007 exactly (C4).

**Display hints are part of the value.** A byte string may carry a display type
in square brackets, and the type takes part in equality and hashing:

<!-- q L577-585 -->
> A display type is assumed to be a MIME type giving optional instructions to any program wishing to display or use the byte string. For example, it might indicate that the string is in UNICODE, is a GIF or JPEG image, is an audio segment, is a biometric template from some particular manufacturer, etc. Although the display type of a byte string is optional, it is considered part of the string for any equality comparisons or hashing. That is, two strings with the same bytes will not be considered equal (or otherwise comparable) if they have unequal display types.

No default display type is defined anywhere in the draft: the word `default`
occurs 0 times in its 2622 lines. So `[10:text/plain]3:abc` and `3:abc`
(*constructed*) are two values, by the source's own rule, not one value with two
encodings (inferred).

**Text is bytes.** There is no text type and no character set:

<!-- q L564-566 -->
> All byte strings carry explicit lengths and are therefore not 0-terminated as in the C language. They are treated as binary even when they are ASCII, and can use any character set encoding desired.

**Not one encoding per value of the application's data.** The grammar is unique
over S-expressions. Three layers above it are not, and the draft writes no rule
that would make any of them unique:

1. *Order of a certificate's fields* is free (C6's quotation, L775–L782).
2. *Integers* may carry redundant sign octets (C8's quotation, L609–L615).
3. *Defaults* may be written or left out: an absent `version` means version 0
   (L1171–L1173); a name certificate's omitted tag means `(tag (*))` (L1647);
   a `not-before` at or before creation may be omitted (L1434–L1437). Version 0
   itself has two spellings, an ASCII `"0"` in the prose and a one-octet zero
   integer in the grammar (SI-1).

Each of the three yields two canonical S-expressions, hence two hashes and two
identities, for one certificate (inferred). That is R-0006's prediction for
option 1, observed:

<!-- qm research/0006-mechanism/report.md L595-601 -->
> **Two things stop that being a conclusion**, and both are named DEC-002 drivers. The data model is far poorer — octet-strings and lists only, no integers, maps, booleans or null — so **every** `ARCH-0001` §4 logical type needs an application-level mapping in which injectivity must be re-established by hand, field by field, with no help from the format. Option 1 *moves* the hard part rather than removing it. And **library availability is its weakest axis**, thin above the parser layer.

— `research/0006-mechanism/report.md`@`bb005ed`, lines 595–601

### 5.2 DEC-002's options, as ARCH-0001 states them

<!-- qm spec/ARCH-0001-authorization-attestation.md L432-439 -->
> 1. Canonical S-expressions (RFC 9804) as canonical; JSON as diagnostic. 2. CBOR + CDDL as canonical; COSE for signed form. 3. JSON + RFC 8785 JCS as canonical; DSSE for signed form. 4. Dual canonical (CBOR and JSON) with a documented bijection. 5. *(Added with `ADR-0004`; drafted in `ARCH-0001-PROPOSAL-v0.2.0` §3.3.)* CBOR data model under RFC 8949 §4.2.1, restricted and decoder-enforced, with no IANA registry native; COSE and DSSE as export envelopes only. Drivers: library availability, SCITT alignment, SPKI fidelity, human debug. Acceptance test: round-trip fixtures for NameCert, AuthzCert (including threshold subject), ArtifactStatement.

— `spec/ARCH-0001-authorization-attestation.md`@`bb005ed`, lines 432–439

### 5.3 ADR-0004's cells for option 1, tested against SPKI's use

<!-- qm spec/ADR-0004-dec-002-encoding.md L71 -->
> | order-only divergence detectable | in the grammar | §4.2.1 optional | RFC 8785 sorts keys | — | **stated rule + rejecting decoder** |

— `spec/ADR-0004-dec-002-encoding.md`@`bb005ed`, line 71

**Narrowed, toward option 5.** It holds for the bytes of a list: reorder its
elements and you have another S-expression, and no grammar accepts the two as
one. It does not hold for SPKI's certificate, whose field order the source
frees (C6). Both orders are grammatical and canonical, so the grammar cannot
see the divergence; it surfaces only as two digests for one certificate, on the
identity path, where R-0006 §3.1 says divergence is silent. Under option 5 the
same reordering of a statement map is a rejection at V5, which is ADR-0004's own
cell for option 5; SPEC-0002 §4.3 lists it among what the decoder MUST reject:

<!-- qm spec/SPEC-0002-ksa-core.md L218 -->
> - map keys not in sorted order, or a duplicated key;

— `spec/SPEC-0002-ksa-core.md`@`bb005ed`, line 218

On this driver SPKI-06 is evidence for option 5 beyond what ADR-0004 claimed.

<!-- qm spec/ADR-0004-dec-002-encoding.md L74-77 "**Why 5 over 1.**" .. "cut B)." -->
> **Why 5 over 1.** Option 1 wins governance and makes smallest-form a property of the grammar, so a conforming reader cannot omit the check. Under option 5 the same property is a rule an implementation must state; one that omits it still parses every valid document (`DECISIONS-0001` item 2; `rfc-8747` cut B).

— `spec/ADR-0004-dec-002-encoding.md`@`bb005ed`, lines 74–77

**Narrowed, toward option 5.** Smallest form is in SPKI's grammar for **length
prefixes** (L591). It is not there for **integer values**, which the grammar
sees as opaque byte strings and whose minimality §3.2.1 permits without
requiring (C8). A reader of SPKI's grammar therefore cannot omit the length
check, and cannot perform the integer check at all without knowing which byte
strings are integers. KSA-CBOR's shortest-head rule reaches both (SPEC-0002
§4.2 item 1, quoted in §5.5). Option 1's advantage on this criterion is real and
smaller than the paragraph says. P5.1 makes the same claim and is narrowed the
same way. Its example is a length prefix, which is where the claim holds:

<!-- qm spec/ARCH-0002-key-relative-naming.md L456-459 "Under RFC 9804 the equivalent of smallest-form" .. "cannot omit the check." -->
> Under RFC 9804 the equivalent of smallest-form is **in the grammar**: `03:abc` is ungrammatical, not non-canonical, so a conforming reader cannot omit the check.

— `spec/ARCH-0002-key-relative-naming.md`@`bb005ed`, lines 456–459

<!-- qm spec/ADR-0004-dec-002-encoding.md L70 "| namespace governance (P1) |" .. "(`ADR-0001`) |" -->
> | namespace governance (P1) | **wins** | **fails** as written (`ADR-0001`) |

— `spec/ADR-0004-dec-002-encoding.md`@`bb005ed`, line 70

**Narrowed.** Option 1 wins governance only under a profile that drops what
SPKI-06 itself uses: display types that are MIME types, part of every string's
identity (§5.1), algorithm names to come from IANA (L729–L730), and object
types that may be URIs (L762–L765). R-0006 §3.5's argument is about the
encoding; the certificate system built on it was not registry-free (inferred).
Neutral between options 1 and 5, both of which need the profile rule.

<!-- qm spec/ADR-0004-dec-002-encoding.md L68 -->
> | SPKI fidelity | highest | low | low | low | low; mapped by WP2 |

— `spec/ADR-0004-dec-002-encoding.md`@`bb005ed`, line 68

**Narrowed, toward neutral.** Option 1 would let KSA carry an SPKI-06 certificate
structurally, byte for byte. It would not let KSA verify one: the draft's
signature algorithms are `rsa-pkcs1-md5`, `rsa-pkcs1-sha1`, `rsa-pkcs1` and
`dsa-sha1` (L2325–L2326), none a KSA suite, and its hash principals are md5 or
sha1 (L2289). Under every option an SPKI-06 object is foreign to KSA's
verification (row 11); option 1 alone keeps its bytes as native bytes. The
cell's weight is smaller than its wording suggests (inferred).

<!-- qm spec/ADR-0004-dec-002-encoding.md L72 -->
> | canonical-encoding conditions | right side of all four grounds | — | **withdrawn**, four grounds | — | (1)–(4) met; (5) owed; (6) see below |

— `spec/ADR-0004-dec-002-encoding.md`@`bb005ed`, line 72

Read against SPKI-06, condition by condition (R-0006 §3.2):

| condition | SPKI-06 | effect on the cell |
|---|---|---|
| (1) injective | over S-expressions, yes; over certificates, no (§5.1 items 1–3) | narrower than the cell |
| (2) decoder rejects | a strict reader rejects by construction; no receiver obligation is written (inferred) | as R-0006 §3.5 found for RFC 9804 |
| (3) canonicalise once, at authoring | **met by profile**: structures pass between machines only in canonical form (A7), base64-wrapped where a channel needs it (L546–L548, L652–L657), and unwrapping is decoding, not canonicalising (inferred). The advanced form never travels | closer to R-O-05 than RFC 9804, which R-0006 found obliges acceptance of other transports; §12 |
| (4) authenticated type indicator | the object's first element, inside the hashed bytes; no domain separation (C2) | partly met |
| (5) canonical order for sets | not met: `k-of-n` members, `(* set …)`, `canceled` and `valid` hash lists carry no order rule (L1287, L2361, L2268, L2330) | not a discriminator, as R-0006 §3.5 finding 1 says |
| (6) Unicode normalisation | no rule; text is bytes, with an optional display type naming the charset | no place for a normaliser, as R-0006 found |

### 5.4 Where this source cuts against MD-3, ADR-0004 and option 5

1. **Every SPKI object is a translation under option 5. Names option 1.**
   SPKI-06's bytes can never be KSA-CBOR, so the ARCH-0001 §6 row that calls SPKI
   the closest peer pays a re-encoding and, where KSA must sign, a new signature
   for every object it maps. WP2 must keep the original bytes (SPEC-0001 §5.3)
   and map display types, positional parts and free field order, none of which
   has a KSA-CBOR form. ADR-0004 scored this low, to be mapped by WP2 (§5.3's
   quotation of its row); the source shows the mapping is wide (§13). **A cost,
   not a reason to reopen**: option 1 would still not verify SPKI-06's
   signatures (§5.3).
2. **Typed byte strings. Names option 1.** A display type is a native typed
   string in SPKI's model. Option 5 has no tags, so an imported display-typed
   string must become a structure, and its identity changes with it (inferred).
3. **MD-3's wording is SPKI's design, and SPKI shows its cost.** MD-3's
   mapping from the human form to the canonical one runs in one direction only.
   SPKI's advanced form is exactly that: many spellings per canonical value,
   white space dropped (B8's quotation, L711–L717). Two reviewers can hold
   different texts of one signed object, and a reviewer cannot tell from a text
   that it is the one the bytes would print (inferred). SPEC-0002 §11.1 departed
   from MD-3's wording and made the human form one-to-one, with one stated
   exception. **The SPEC, not MD-3, is
   the position this source supports.** MD-3 is closed; recorded so that no one
   restores the one-directional mapping from the minute.
4. **Smallest-form for lengths by grammar. Names option 1.** ADR-0004 priced it;
   §5.3 narrows it to lengths.

Searched and found **not** to cut against option 5:

- **Condition (5).** SPKI-06 leaves set order as open as SPEC-0002 does, so it
  is a data-model obligation under every option (ADR-0004's section headed Not
  decided here).
- **Canonicalisation at verification.** SPKI-06 transmits the canonical form;
  option 5 does the same (SPEC-0002 §5). Equal.
- **The type indicator.** SPKI gets one from its structure; option 5 builds one
  from `kind` in the TBS plus a DS label (SPEC-0002 §6.4), and adds the domain
  separation SPKI lacks (C2).

### 5.5 Where it favours option 5

1. **The object layer.** SPKI-06 needed, and never wrote, rules for field order,
   integer minimality and defaults (§5.1). KSA-CBOR states all three in the
   encoding profile:

<!-- qm spec/SPEC-0002-ksa-core.md L198-202 -->
> 1. every integer, length and count uses the shortest possible head (preferred serialization); 2. every array, map, byte string and text string has a definite length; 3. the keys of every map are sorted in bytewise lexicographic order of their deterministic encodings;

— `spec/SPEC-0002-ksa-core.md`@`bb005ed`, lines 198–202

<!-- qm spec/SPEC-0002-ksa-core.md L389-390 -->
> A statement is a KSA-CBOR map with these keys. Absent optional fields MUST be omitted; they MUST NOT be present with an empty or placeholder value.

— `spec/SPEC-0002-ksa-core.md`@`bb005ed`, lines 389–390

2. **Order-only divergence** (§5.3): detectable under option 5, not for
   SPKI-shaped objects under option 1.
3. **A data model with integers and booleans.** SPKI spells a boolean as the
   presence of `(propagate)` in a certificate and as the byte strings `t` and `f`
   in a 5-tuple (L1379, L2033); KSA has both types natively (SPEC-0002 §4.1).

### 5.6 Construct by construct, at the encoding layer

| SPKI-06 construct | KSA (SPEC-0002) | import | export |
|---|---|---|---|
| canonical S-expression of an object (§3.1) | the TBS, KSA-CBOR (§4) | re-encoded; original bytes kept as an external statement (SPEC-0001 §5.3) | a translation, signed again (inferred) |
| `<bytes>`, length-prefixed (L590) | byte string or text string | bytes stay bytes; text only where the target type is text (ours) | — |
| display type `[...]` (L594) | none; no tags (§4.1) | a structure, or refused (open question 12) | never emitted |
| `<integer>`, twos complement (§3.2.1) | integer, ±(2^53 − 1) (§4.1) | decoded to its value where it fits (`version`, `k-val`, `n-val`); a key component does not (the modulus at L826–L829 is 129 octets) and stays bytes inside the key's encoding; a non-minimal encoding refused under P5.1 (ours) | minimal |
| `<date>`, ASCII UTC (§4.9.1) | time (§4.4) | parsed; malformed refused (ours); `not-after` boundary owed (§10) | rendered in SPKI's form |
| positional parts, trailing omission (L767–L773) | closed maps with integer keys (§7.1) | by position, per object type | — |
| `cert`/`acl` fields in any order (L772–L773, L775–L782) | map keys sorted (§4.2) | accepted in any order, as the source allows; the external statement keeps the bytes as received | the order of SPKI's BNF (ours) |
| object type, the first element (L524–L526) | `kind` in the TBS plus a DS label (§6.4) | `cert` splits into `trust` or a naming `attestation` by its issuer form (§9) | — |
| `signature` object (§3.8.3) | envelope `[suite, says, tbs, sig, ? pub]` (§5) | not verifiable natively (row 11) | not producible (no suite) |
| advanced form (§3.6) | human-review form (§11) | — | — |
| base64 `{…}` transport (L652–L657) | none; §13.7's abbreviated forms are the analogue | decoded before anything else | — |

### 5.7 Each DEC-002 option, for and against

The draft bears on all five options of §5.2, unevenly. Every cell is inferred
from the section it cites, and no cell ranks the options.

| option | SPKI-06 is evidence for it | SPKI-06 is evidence against it |
|---|---|---|
| 1 canonical S-expressions | the encoding in its one certificate design: uniqueness by grammar for lengths and lists (§5.1), the canonical form as the transmitted form (A7), a type indicator inside the hashed bytes (§12), SPKI objects carried byte for byte (§5.3) | the object layer it leaves open: field order, sign octets and defaults (§5.1, C6, C8, SI-1); MIME display types and IANA algorithm names inside identity (§5.3); a boolean spelled as presence and as `t`/`f` (§5.5); no domain separation (C2), and RFC 9804 supplies no authenticated type indicator to build one on (§12's quotation of R-0006); a fidelity that stops at structure, since no SPKI-06 signature verifies under a KSA suite (§5.3) |
| 2 CBOR and CDDL, COSE signed form | SPKI-06 itself wanted IANA algorithm names (L729–L730), so the registry objection to option 2 is P1's (ADR-0001), not a lesson from SPKI; and C2's missing separation does not count against option 2, since COSE's signed form has one **[outside this source]** | a unique grammar over a free object layer gives one certificate two identities (C6), which is the gap ADR-0004's option-2 cell records as RFC 8949 §4.2.1 being optional |
| 3 JSON and JCS, DSSE signed form | as for option 2, C2 does not count against it: DSSE's signed form binds a payload type **[outside this source]** | none new: ADR-0004 withdrew option 3 on four grounds, and this draft adds a ground neither way |
| 4 dual canonical, with a bijection | — | SPKI kept one canonical form and made its second form many-to-one, for display and transport (B8, §5.4 item 3); it never needed a second canonical form and never wrote a bijection |
| 5 KSA-CBOR, ADR-0004's choice | §5.5: the object-layer rules SPKI needed and never wrote, order-only divergence rejected at V5, integers and booleans in the data model, DS labels for the separation SPKI lacks | §5.4: every SPKI object a translation, no native typed string, and a WP2 mapping that §13 shows to be wide |

### 5.8 Net, stated as evidence

On ADR-0004's own criteria SPKI-06 leans toward option 5, and further than the
ADR claimed. Two of its option-1 cells were too generous: order-only divergence
is undetectable for SPKI-shaped objects, and smallest form is in the grammar for
lengths only. Two more are narrower than written: namespace governance holds
only under a profile SPKI did not adopt, and SPKI fidelity is structural, since
nothing in SPKI-06 verifies under a KSA suite. What it costs option 5 is the
width of WP2's mapping, and the loss of a native typed string. Against MD-3 it
supports SPEC-0002 §11's one-to-one human form over the minute's one-directional
mapping.
**Nothing here decides DEC-002 again**, and ADR-0004's reviewer may take the
four narrowed cells as corrections to the scoring text rather than to the
decision.

## 6. Threshold subjects (*k*-of-*n*)

This is the source's part closest to the project's name. ARCH-0001 attributes
the construct to SPKI and asks for it in the native model:

<!-- qm spec/ARCH-0001-authorization-attestation.md L119 -->
> 4. **threshold subjects** (*k* of *n*) as first-class principals (SPKI);

— `spec/ARCH-0001-authorization-attestation.md`@`bb005ed`, line 119

<!-- qm spec/ARCH-0001-authorization-attestation.md L335 "Threshold principals SHALL" .. "CA hierarchy." -->
> Threshold principals SHALL be representable without encoding them as a CA hierarchy.

— `spec/ARCH-0001-authorization-attestation.md`@`bb005ed`, line 335

### 6.1 What SPKI-06 specifies

The syntax and its two side conditions are B2's quotation (L1287–L1289); the
intent and the subject-side placement are A3's (L1296–L1302, L439–L446). The
semantics, across a page break:

<!-- q L1304-1309 -->
> A certificate or ACL with a k-of-n Subject does not delegate permission to any of those subjects, alone. Rather, each of these subjects receives a share of the delegated permission. Only if at least K of the N subjects show certificate paths which converge on a single target Subject during reduction, is that permission

<!-- q L1316-1317 -->
> transmitted to the target. If fewer than K such paths can be shown, then the permission is not delegated.

<!-- q L1319-1321 -->
> This construct is far from simple. However, it is extremely useful. It has been demanded by a number of initial customers of SPKI certificates. It also solves a number of sticky political problems.

The five uses it gives:

<!-- q L1327-1328 -->
> 1. co-signing of electronic corporate checks or purchase orders above a certain amount

<!-- q L1344-1350 -->
> 4. using online and off-line issuers. One could have a permission established by an off-line key issuing a long-lived certificate and echoed by an online automated server, issuing short-lived certificates. The delegation of this permission could require both before the eventual subject gets the permission. This can be achieved through the use of (online ) tests in a long-lived certificate, but the K-of-N subject mechanism may be cleaner.

<!-- q L1352-1354 -->
> 5. ultra-secure applications. There are many applications which follow the nuclear weapons launch scenario. That is, multiple agreement is required before the permission is granted.

(Example 2, the DNSSEC root, is L1330–L1332; example 3, three algorithms, is
A10's quotation.) And the reduction, which is a sketch:

<!-- q L2128-2134 -->
> A separate document will give full algorithms for reduction of K-of-N threshold subjects. One general procedure is to make K copies of of the 5-tuple containing the K-of-N subject and indicate which of those subjects is being handled by that copy. One then reduces that copy as if it had a single subject. One can stop the separate reductions when all K of the reduced values have the same subject. At that point, the K reduced 5-tuples become a single 5-tuple.

<!-- q L2136-2138 -->
> The actual algorithm choices for doing this reduction depend on whether one wants to reduce left-to-right or right-to-left and how much storage a verifier has.

### 6.2 What ours specifies

The threshold form and the vectors' letters are A3's and B2's quotations
(SPEC-0002 §8.6, Appendix A). Evaluation:

<!-- qm spec/SPEC-0004-ksa-trust-evaluation.md L289-297 -->
> A threshold anchor or threshold trust statement trusts a set `M` of keys with threshold `n` about a scope. A statement is **covered through the threshold** when `n` distinct members of `M`, each reached as the start of a sub-path with that scope, have each made a statement that covers the ask (§10.3) with **the same target, type and value**. Delegation onward from a threshold set requires `n` distinct members each to have issued a trust statement to the same key with identical `about` and `may-delegate`; the resulting edge is followed as one. Distinctness is by kid. Keys that a rotation (§7.2) links count as one member.

— `spec/SPEC-0004-ksa-trust-evaluation.md`@`bb005ed`, lines 289–297

<!-- qm spec/SPEC-0004-ksa-trust-evaluation.md L483-485 -->
> A threshold counts distinct keys. A party controlling several keys is several members unless the party that set the threshold prevented it; SPEC-0005 §4.3 discusses panels.

— `spec/SPEC-0004-ksa-trust-evaluation.md`@`bb005ed`, lines 483–485

### 6.3 Side by side

| # | question | SPKI-06 | ours | verdict |
|---|---|---|---|---|
| T1 | bounds on *k* | `K < N`; no lower bound is stated, and `K` is an `<integer>`, so zero and negative values are encodable (L2302, §3.2.1) | `1 ≤ k ≤ n`; N-7 (`k = 0`) and N-8 (`k > n`) reject at V8; TV-10 (`k = n`) and TV-11 (`k = 1`, `n = 2`) verify | **adapts**; export of `k = n` **conflicts** (T11) |
| T2 | is *n* written? | yes, `<n-val>`, beside the *N* members it must count | no: `n` is the length of `trusts`, not a field | **rejects** (C3). Import checks *N* against the count and refuses a mismatch (ours) |
| T3 | what may a member be? | any `<subj-obj>`: a key or its hash, a name, an object hash, a keyholder, or a nested threshold (L1232–L1233) | a `kid`, two or more | **constrains**. Import refuses non-key members (T9) and nested thresholds, which cannot in general be flattened: 2-of-{A, B, 2-of-{C, D, E}} (*constructed*) is satisfied by {A, B} and not by {C, D, E}, and no single threshold over five equally counted members does both (inferred) |
| T4 | where does the set sit? | the subject, of a certificate or an ACL entry | the subject of a `trust` (`this` absent), or an anchor | **adopts** (A3) |
| T5 | when is it met? | *K* paths converge on one target subject during reduction (L1304–L1317); the glossary allows an object or a key as that target (L443–L444) | (a) *n* members each make a statement covering the ask with the same target, type and value; (b) *n* members each delegate to one common key | **adopts** SPKI's convergence as (b). (a) has an SPKI counterpart only as *K* certificates converging on the target itself, an `object-hash` subject for an object or the key for a key, each carrying the same tag; SPKI reads each of them as an authorization (inferred). Our model reaches attestation without a delegation step; SPKI's does not |
| T6 | what does the join grant? | the *K* reduced 5-tuples become one (L2133–L2134); how their tags, validities and delegation bits combine is not said | (b) requires identical `about` and `may-delegate`, and R-0006 §3.13 found `identical` undefined | **constrains** (open question 2). Applying §8.2 pairwise would give the intersection of the *K* tags and validities (inferred), which accepts *K* delegations with different scopes that ours rejects |
| T7 | distinct members? | distinct paths are the intent (L1296); nothing requires the listed subjects to be distinct, so a key listed twice could be counted twice under a count by subject (inferred) | distinct by `kid`; rotation-linked keys count as one; `trusts: [A, A]` verifies at V8 and can never be met (DL-0019) | **adapts**: ours closes SPKI's gap, failing closed. SPEC-0002 still owes the V8 rule (ARCH-0001 §7, quoted below) |
| T8 | algorithm | *K* copies, stop when they agree; full algorithms deferred to a separate document (L2128) | the condition (§6.4), a work bound (§6.5), determinism (§3) | **adapts**. SPKI's sketch is underdetermined: a reducer holding *K* copies must first choose which *K* of the *N* members to follow, and must try another when a chosen path fails, so the procedure as written needs either *N* copies or a search (inferred, SI-12) |
| T9 | names as members | allowed, so a member may be a group; distinctness after name resolution is not addressed | not applicable: keys only | **silent** today; owed if mofn#143 gives names a principal form |
| T10 | shares | each member holds a share of one *K*-th (L442) | none | **silent**: a conceptual gloss with no arithmetic in either |
| T11 | the uses | example 4 needs both of two issuers, a 2-of-2; examples 1 and 5 describe co-signing and multiple agreement, which commonly mean every named party (inferred) | `k = n` is valid (TV-10) | **conflicts** with SPKI's own `K < N` (SI-2): its examples need what its grammar's side condition forbids. Ours allows it |

SPEC-0002's distinctness gap, as ARCH-0001 records it:

<!-- qm spec/ARCH-0001-authorization-attestation.md L484-487 -->
> round-trips in `prototype/wallet/tests`. **Still owed:** `trusts: [A, A]` with `threshold: 2` passes V8, since `SPEC-0002` has no distinctness rule and `SPEC-0004` §6.4 counts distinct kids. It fails closed; it goes to `SPEC-0002` with condition (5).

— `spec/ARCH-0001-authorization-attestation.md`@`bb005ed`, lines 484–487

### 6.4 What this means for m-of-n

1. **The construct is SPKI's and the arithmetic is ours.** On the arithmetic,
   every flat SPKI threshold over distinct keys with `1 ≤ K < N` and `N` equal
   to the count imports exactly, and the reverse fails only at `k = n`, which
   SPKI's side condition excludes and SPKI's own examples need (inferred). The
   members are another matter: an SPKI member is an SPKI principal, which has
   no `kid` today (row 11), and a `kid`, which hashes a different preimage, is
   not an SPKI hash principal either (§13). An R-I-01 table must say which
   reading of `K < N` an export follows (open question 1).
2. **Our coverage has a mode SPKI lacks.** SPEC-0004 §6.4's route (a) lets *n*
   keys jointly attest without anyone delegating to a common key. In SPKI the
   nearest form is *K* certificates converging on the target itself, an
   `object-hash` subject or a key, which SPKI reads as authorizations of that
   target rather than attestations about it (inferred; T5). This is what R-M-06
   buys us beyond SPKI.
3. **SPKI's members are richer and its semantics thinner.** It allows names and
   nested thresholds and never says what the joined grant is (T6) or whether
   members must be distinct (T7). Ours allows less and says both, except that
   `identical` is still undefined (R-0006 §3.13).
4. **ADR-0004's text is stale on the fixture, and cannot change.** It still
   reads:

<!-- qm spec/ADR-0004-dec-002-encoding.md L96-99 "**Owed — the threshold fixture (T-031).**" .. "the check that owns it." -->
> **Owed — the threshold fixture (T-031).** No vector exercises `trust`'s threshold form. Per `ARCH-0001` §7 since v0.1.3, it carries the invariant as positive and negative cases (`k = 0`, `k > n`, `n ≠ len(members)`) and names `SPEC-0002` V8 as the check that owns it.

— `spec/ADR-0004-dec-002-encoding.md`@`bb005ed`, lines 96–99

   while ARCH-0001 §7 records that the fixture landed (TV-9…11, N-7…10;
   DL-0019). An accepted ADR changes only by being superseded (its own
   `version_policy`), so the stale line stays; recorded so that a reader of
   ADR-0004 does not take the threshold form as unvectored.

## 7. Delegation: `(propagate)` against an integer depth

### 7.1 What SPKI-06 specifies

`(propagate)` is present or absent (B3's quotation, L1379–L1383). An ACL entry
without it grants no onward right:

<!-- q L1794-1797 -->
> If all the optional fields are left out, the subject is given the permission specified in <tag>, without permission to delegate it, with no expiration date or condition (until the ACL is edited to remove the permission).

In a 5-tuple the flag is `t` or `f` (L2033), and reduction requires the left
tuple's flag and keeps the right one's (B3's quotation, L2059–L2063). So each
issuer decides only whether **its own subject** may pass the grant on, and
nothing set at the root bounds how long the chain becomes (inferred from
L2059–L2063). The draft gives no argument against an integer; R-0007 reports
that the theory document did:

<!-- qm research/0007-delegation-models/report.md L454-455 -->
> - Depth is a boolean (`propagate`). SPKI considered integer depth and rejected it (§4.1.4).

— `research/0007-delegation-models/report.md`@`bb005ed`, lines 454–455

### 7.2 What ours specifies

DL-0025 decided integer depth, and recorded the rejected position as not weak:

<!-- qm design-log/0025-delegation-depth/produced.md L13-14 -->
> - Boolean is a special case of integer depth: absent `may-delegate` means one hop, and depth ≥ 1 means delegate onward.

— `design-log/0025-delegation-depth/produced.md`@`bb005ed`, lines 13–14

<!-- qm design-log/0025-delegation-depth/review.md L14-20 -->
> - **1b, boolean.** Rejected. It supersedes part of `ADR-0003` and reverses SPEC-0002 §8.6, TV-5 and the wallet engine. What it buys over 1a is expressible in 1a anyway. **The rejected position is not weak**, and the R-M-10 rewrite must carry it: RFC 2693 §4.1.4 (depth is unpredictable, since one can always add a temporary key; depth does not bound width). The library's `rfc-2693` notes side with RFC 2693. That contradiction is now recorded against them, not resolved.

— `design-log/0025-delegation-depth/review.md`@`bb005ed`, lines 14–20

R-M-10 as rewritten is B3's quotation; SPEC-0004 §6.3 is normative:

<!-- qm spec/SPEC-0004-ksa-trust-evaluation.md L260 -->
> 3. `deleg` is present, and `deleg.depth ≥ 1` (an absent depth is 0);

— `spec/SPEC-0004-ksa-trust-evaluation.md`@`bb005ed`, line 260

<!-- qm spec/SPEC-0004-ksa-trust-evaluation.md L268-271 -->
> 6. if `s.may-delegate` is present, it does not widen `deleg`: its `depth` is at most `deleg.depth − 1`; each of its `ranges` is within a range of `deleg.ranges` (or of `s.about` if `deleg.ranges` is absent); its key lists do not admit a key the current lists forbid.

— `spec/SPEC-0004-ksa-trust-evaluation.md`@`bb005ed`, lines 268–271

and the new state, whose wording reads as a cap rather than a test (open
question 20):

<!-- qm spec/SPEC-0004-ksa-trust-evaluation.md L278 "`s.may-delegate`, with" .. "is absent" -->
> `s.may-delegate`, with `depth` reduced to at most `deleg.depth − 1`; none if `s.may-delegate` is absent

— `spec/SPEC-0004-ksa-trust-evaluation.md`@`bb005ed`, line 278

### 7.3 The mapping, both ways

| SPKI-06 | KSA | exact? |
|---|---|---|
| no `(propagate)` | no `may-delegate`: one hop | **yes** |
| `(propagate)` on an ACL entry | an anchor's `may-delegate` with `depth` *d* ≥ 1 | **within a bound.** SPKI's flag sets no limit; ours needs a number. A `depth` of 16 or more behaves as no limit, because SPEC-0004 §6.5 stops a path at 16 edges (inferred; §6.5 does not define an edge, and whether the anchor counts moves the least such depth by one) |
| `(propagate)` on a certificate | a trust statement's `may-delegate` with `depth` *d* | **per chain only.** SPEC-0004 §6.3 item 6 follows a statement only if its `depth` is at most the received `depth` − 1, and anything more is a widening that fails the path. SPKI's flag is the same at every hop and a depth cannot be: a chain's depths must fall by at least one per hop, so the entry at its root needs at least the chain's length. One constant depth, however large, fails at the first propagating certificate below the root, and a certificate that sits at different positions in two chains has no single depth that serves both (inferred) |
| each SPKI issuer re-decides its own subject's flag | each KSA issuer sets its own `may-delegate`, at least one below the one it received, or drops it (SPEC-0004 §6.3 item 6) | **yes for the choice, no for the value**: per-hop control survives, but the number a hop may write depends on where the hop sits |
| — | `depth` *d* ≥ 1 exported as `(propagate)` | **no: over-grants.** An SPKI verifier follows chains longer than *d* |
| — | `ranges`, `allow-keys`, `exclude-keys`, `not-on-or-after` | **no field in SPKI.** Dropped on export, each one over-grants (inferred) |

**On DL-0025's first argument (inferred).** The argument (§7.2's first
quotation) holds for the absent case, which is SPKI's `f` exactly, and it holds
one chain at a time: an ACL entry and *L* certificates flagged `t, t, …, t, f`
become the depths *L*, *L* − 1, …, 1 and then no `may-delegate`. It does not
hold certificate by certificate. An SPKI `t` is one object, the same in every
chain that uses it; a KSA depth is a position in one chain, because every hop
must lower it. So the review's line that 1b buys nothing 1a cannot express
(§7.2's second quotation) is true of a delegation written by an issuer who knows
where it sits, and not of SPKI's semantics, in which no issuer needs to know.
This is a cost at import, not in the native model: an R-I-01 table cannot
translate an SPKI certificate set one certificate at a time (open questions 10
and 20). It leaves the RFC 2693 §4.1.4 contradiction DL-0025 recorded against
the library's `rfc-2693` notes where it was.

### 7.4 Names pass under the depth bound

SPKI reduces names before 5-tuples, and a name certificate carries no
`(propagate)` and passes everything:

<!-- q L2013-2017 -->
> Name reduction is specified in section 5.3. Therefore, in what follows we assume all issuers and subjects are principals. We also assume that all principals are public keys. It is an implementation decision whether to store these as explicit keys, hashes of keys (used as pointers) or addresses pointing to keys.

<!-- q L1647-1650 -->
> In a name certificate, the (tag) field is omitted and (tag (*)) is assumed. There is also no <deleg> field. A name definition is like an extension cord, passing everything the name is granted through to the subject.

So a chain of name certificates of any length sits between two 5-tuples without
consuming any delegation, and a name's issuer may add members at will
(L1660–L1665). If KSA resolves compound names as a separate step before
reduction, as ARCH-0001 §4.3 step 1 keeps and mofn#143 owes, then neither
`depth` nor SPEC-0004 §6.5 counts name hops unless mofn#143 says they do, and
whoever controls a name in a chain holds an unbounded, unnarrowed grant
(inferred). Open question 4.

## 8. Tags and their intersection

### 8.1 What SPKI-06 specifies

A tag is `(tag (*))`, all permissions, or a tag expression (L1389–L1391); one
without `*`-forms is a single permission and one with them a set (B4's
quotation). Two further rules govern every tag:

<!-- q L1402-1408 -->
> All tags are assumed to be positional. That is, parameters in a tag have a meaning defined by their position. All tags are assumed to be extendable. That is, if one adds a field to the end of a tag definition, one is restricting the permission granted. [If the field added makes the tag invalid, then one has restricted the original permission to zero.]

The intersection rules, in full:

<!-- q L2088-2104 -->
> Two <tag> S-expressions intersect by the following rules. Note that in most cases, one of the two tag S-expressions will be free of *-forms. A developer is free to implement general purpose code that does set-to-set reductions, for example, but that is not likely to be necessary. 1. basic: if a1 == a2, then the result is a1. 2. basic: if a1 != a2 and neither has a *-form, then the result is "null". 3. (tag (*)): if a1 == (tag (*)), then the result is a2. If a2 == (tag (*)), then the result is a1. 4. (* set ...): if some <tag> S-expression contains a (* set ) construct, then one expands the set and does the intersection of the resulting simpler S-expressions.

<!-- q L2106 -->
> 5. (* range ...): if some <tag> field compares a (* range ) to a

<!-- q L2114-2121 -->
> <byte-string>, one does the specified range comparison and the resulting field is the explicit one tested. If the strings being compared have unequal display types, then the result is the empty set. 6. (* prefix ...): if some <tag> field compares a (* prefix ) to a <byte-string>, then the result is the explicit string if the test string is a prefix of it and otherwise "null".

The `*`-forms and the orderings a range may use:

<!-- q L2358-2363 -->
> <tag-prefix>:: "(" "*" "prefix" <byte-string> ")" ; <tag-range>:: "(" "*" "range" <range-ordering> <low-lim>? <up-lim>? ")" ; <tag-set>:: "(" "*" "set" <tag-expr>* ")" ; <tag-star>:: "(" "tag" "(*)" ")" ; <tag-string>:: <byte-string> | <tag-range> | <tag-prefix> ;

<!-- q L2327 -->
> <range-ordering>:: "alpha" | "numeric" | "time" | "binary" | "date" ;

### 8.2 Three defects in the rules as written

1. **No meet of two `*`-forms (SI-4).** Rules 5 and 6 compare a `*`-form with a
   byte string; rule 4 expands a set, whose members may themselves be
   `*`-forms. No rule intersects a range with a range, a prefix with a prefix,
   or a range with a prefix, and the draft says why: in most cases one side is
   free of `*`-forms (L2088–L2092). That suffices when every intersection is taken
   against a concrete request, reducing right to left (inferred). It does not
   suffice for §8.7's result certificate, which reduces a chain to
   `(Self,X,D,A,V)` with no request in it (L2144–L2147), or for any left-to-right
   reduction of two certificates that both carry `*`-forms (inferred). So the
   operation R-0006 §4.1 calls closed is not closed in this draft:

<!-- qm research/0006-mechanism/report.md L964-968 -->
> SPKI [@rfc-2693] does something no system in R-001's survey does. Its §6.3 reduction composes two 5-tuples into one, and `AIntersect` is a **closed binary operation on authorization tags** — the intersection of two authorizations is itself an authorization of the same kind, computed element-wise over `(*)`, `(* set …)`, `(* prefix …)`, `(* range …)` forms.

— `research/0006-mechanism/report.md`@`bb005ed`, lines 964–968

   R-0006 cites RFC 2693 for it, which this file did not read **[outside this
   source]**; what can be said is that SPKI-06's §8.3 does not supply it.
2. **The extension rule and rule 2 disagree (SI-3).** By §4.8, a tag with a
   field added at the end restricts the shorter one, so
   `(ftp db.acme.com)` ∩ `(ftp db.acme.com root)` (*constructed*) should be the
   longer tag. By rule 2 the two are unequal and neither has a `*`-form, so the
   result is `null`. R-0007 §3.5 writes UC-5 in SPKI with exactly that pattern,
   relying on a rule it quotes from RFC 2693, not from this draft:

<!-- qm research/0007-delegation-models/report.md L413-418 "SPKI's wildcards (§6.3.1) are" .. "(§6.3.1)." -->
> SPKI's wildcards (§6.3.1) are `(*)`, `(* set …)`, `(* prefix <byte-string>)` and `(* range …)`. There is **no suffix form**, so `*@foo.com` cannot be written as a string pattern. The encoding that works uses list-prefix semantics: *"If one list is longer than the other but match at all elements where both lists have elements, then the longer list is the result of the intersection"* (§6.3.1).

— `research/0007-delegation-models/report.md`@`bb005ed`, lines 413–418

   A verifier that implements this draft's §8.3 as printed reduces
   `(mailbox com foo)` with `(mailbox com foo eng)` to `null` at R-0007's first
   hop and rejects the chain R-0007 says reduces (inferred; row 48). R-0007's
   conclusion survives under RFC 2693's rule; it does not survive under
   SPKI-06's, which is the document R-0007 cites for SPKI's wire syntax.
3. **Five orderings, none defined (SI-15).** `alpha`, `numeric`, `time`,
   `binary` and `date` occur as ordering names at L2327 and nowhere else (each
   word checked by script). Nothing says how a `numeric` byte string encodes its
   number, or how `time` differs from `date`, or `alpha` from `binary`.

Two smaller points: unequal display types make a range comparison empty (rule
5), so a display type silently narrows a grant to nothing (inferred); and there
is no suffix and no exclusion form, which R-0007 §3.5 already records.

### 8.3 Against ours

SPEC-0003 §6 defines, for ten of its eleven base kinds, the range form,
membership and *within* (B4's quotation); the eleventh, `record`, has no range,
and a `record` type's `delegation` must be 0. SPEC-0004 §6.3 never computes a
meet: it checks *within* at each hop, which needs only the partial order.
R-0006 §4.6 states what follows:

<!-- qm research/0006-mechanism/report.md L1128-1130 "When `A₂` is within `A₁`" .. "over the same ranges." -->
> When `A₂` is within `A₁`, the meet `A₁ ⊓ A₂` is `A₂`. So **on every path `SPEC-0004` accepts, the final scope equals what SPKI's reduction would compute** over the same ranges.

— `research/0006-mechanism/report.md`@`bb005ed`, lines 1128–1130

Against SPKI-06 that holds wherever SPKI-06 defines the meet. Where it does not
(defect 1), SPKI-06 gives no result to compare with, and ours gives a definite
one (inferred). And the extension rule's case (defect 2) is a case ours handles
by typing: a narrower grant is a narrower range of the same type, never a longer
list.

**Consequences.**

- **R-M-08 (row 7).** SPKI-06 does not meet it for its own tag language; the
  typed form does, for every kind that has a range, which is how R-M-08's own
  0.2.0 note scopes the claim (the types SPEC-0003's base kinds cover).
- **DEC-004 option 1 (row 29).** SPKI's tags cannot be taken unchanged from this
  draft: the list-prefix rule must come from RFC 2693, the `*`-form meet from
  somewhere, and the orderings from nowhere yet. Whoever scores DEC-004 should
  score option 1 as RFC 2693 plus repairs, not as this draft.
- **P1 (C7).** SPKI's tag names carry no key. In practice the meaning is fixed by
  the verifier whose ACL roots the chain (A2), a defining key left implicit
  (inferred). An import names the type under a definition of the importer's, as
  ARCH-0001 §6 already does for X.509 names.

### 8.4 SPKI `*`-forms on import (ours, inferred throughout)

| SPKI-06 | SPEC-0003 base kind | note |
|---|---|---|
| `(tag (*))` | an attribute range with no `range`, for each type concerned | SPEC-0002 §8.6 forbids an empty `about`; SPKI's star tag has no single-type form |
| `(* set …)` of byte strings | enum, text, digest or key range | order discarded; ranges are sorted and distinct per kind |
| `(* range numeric …)` | integer `[lo, hi]` | only once the number encoding is fixed (defect 3); `g` and `l` become `lo + 1`, `hi − 1` |
| `(* range time …)`, `(* range date …)` | time `[not-before, not-on-or-after)` | an `le` upper bound becomes the next second |
| `(* range alpha …)`, `(* range binary …)` | none | text ranges are sets, not intervals: refused |
| `(* prefix …)` | none | dns-name and email patterns are suffix-shaped: refused |
| a positional list with nested structure | several attributes, one per type | a `record` type has `delegation 0` and cannot be delegated (SPEC-0003 §6) |
| an extended tag (§4.8) | a narrower range of the same type | no list-length semantics in ours |

## 9. Local names and name reduction

### 9.1 What SPKI-06 specifies

Names are for people, and are reduced to keys before any authorization is
computed:

<!-- q L1603-1606 -->
> Names are defined for human convenience. For actual trust engine computations, names must be reduced to keys. This section gives the form of a name, a name certificate and the rules for reducing name certificates to simple mappings from name to key.

A name certificate binds one name in its issuer's space:

<!-- q L1636-1645 -->
> <name-cert>:: "(" "cert" <version>? <cert-display>? <issuer-name> <subject> <valid>? <comment>? ")" ; <issuer-name>:: "(" "issuer" "(" "name" <principal> <byte-string> ")" ")" ; That form maps directly into the intermediate form needed for name string reduction. The name must be under the <principal> of the certificate issuer, and under this syntax the certificate issuer <principal> is taken from the (name..) structure.

<!-- q L1658-1665 -->
> The subject is unrestricted. It is what you are trying to name. If there is more than one name certificate for a given name, with different subjects, then that name is a group. More specifically, all name certificates define groups, many of which will have only one member. A multi-member group is like a multi-plug extension cord, passing everything the name is granted through to any and all of its subjects.

A name in a subject may be relative or fully qualified:

<!-- q L1684-1690 -->
> A relative name is defined only with respect to an issuer and should show up only in a certificate, borrowing the <principal> from the issuer of that certificate. For evaluation purposes, the relative name is translated into a fully-qualified name before reduction. Unlike the <issuer-name>, which is forced to be a name in the issuer's name space, the subject name can be in any name space.

Reduction rewrites the first name by the certificate that defines it, and
termination is left to another document:

<!-- q L1715-1726 -->
> the name (subject (name (hash md5 |Txoz1GxK/uBvJbx3prIhEw==|) fred sam george mary)) reduces to (subject (name (hash md5 |Z5pxCD64YwgS1IY4Rh61oA==|) sam george mary)) recursing until the name reduces to a principal. In non-pathological cases this is the only reduction rule needed.

<!-- q L1737-1739 -->
> in which case a naive reduction would grow without bound. This kind of boundless growth is not possible under the name reduction rules given in the theory document.

### 9.2 What ours specifies

<!-- qm spec/ARCH-0001-authorization-attestation.md L241 "| `Name` |" .. "TV-13) |" -->
> | `Name` | `{ issuer: Principal, labels: [string, ...] }` — SDSI compound name | **owed by `SPEC-0004`** (mofn#143). A one-label binding is an `attestation` about a key under a names definition (`ARCH-0002` P6; TV-13) |

— `spec/ARCH-0001-authorization-attestation.md`@`bb005ed`, line 241

<!-- qm spec/ARCH-0001-authorization-attestation.md L383 -->
> | SDSI names | §1 item 2, G1, R-M-03, §4.3 step 1: compound names resolve to a key | no `Name` principal, no compound names, no resolution step | `SPEC-0004` (and `SPEC-0002` if a form is needed) | mofn#143 |

— `spec/ARCH-0001-authorization-attestation.md`@`bb005ed`, line 383

<!-- qm spec/ARCH-0002-key-relative-naming.md L307-310 -->
> There is no distinct naming object. A name is a **statement whose predicate is a name**: *A says B has name "fred"*

— `spec/ARCH-0002-key-relative-naming.md`@`bb005ed`, lines 307–310

### 9.3 Findings

1. **P6 is SPKI's name certificate (row 28).** A certificate by K stating that
   K's name N denotes S, issued with no authority needed (A6), is P6's form as
   §9.2 quotes it, and TV-13 is that shape for a key. SPKI's own example binds
   `fred` (L1698–L1702).
2. **R-M-04 holds as functions, not as types (row 4).** Both certificates are
   `cert`; the issuer form and the missing tag and `(propagate)` tell them apart,
   and they feed different procedures (4-tuples and 5-tuples, L448–L453). That
   is ARCH-0001 §4.2's reading of R-M-04, not its literal wording.
3. **Every SPKI name is a group (L1660–L1665).** Two KSA naming attestations by
   one key with one value about two keys would, read as SPKI reads them, make a
   two-member group. ARCH-0001 §5.5 lists `Group` as having no form and no
   consumer. Open question 5.
4. **A name passes everything (L1647–L1650).** Authority granted to a name flows,
   unnarrowed in scope, to every current and future member and through name
   chains that consume no delegation (§7.4). Only the name certificates' own
   validity bounds it, which the draft's example implies and never states (the
   requirements lane infers it, `draft-ietf-spki-cert-structure#R-0416`). Open
   question 4.
5. **Termination is not in this draft (L1737–L1739).** The self-referential
   certificate at L1731–L1735 grows without bound under the one rule the draft
   gives. mofn#143 must state a bound of its own; SPEC-0004 §6.5's edge bound
   is the precedent. Open question 6.
6. **The subject of a name is unrestricted.** It may be a key, another name in
   any space, an object hash, a keyholder or a threshold (L1658, L1689–L1690,
   L1230–L1233). TV-13's target is a key; a KSA name for a threshold set or an
   object has no form.
7. **The draft's own example is outside its grammar (SI-5).** The name
   certificate at L1698–L1702, and its canonical form at L1704–L1707 (decoded in
   this pass), carry `(not-after …)` directly in `cert`; `<name-cert>` allows
   only `(valid …)` there (L1636–L1637, L2370). The template at L1630–L1634 also
   writes `<name>` where the rule writes `<byte-string>` (SI-6).
8. **Foreign names map into the local space (L1620–L1622).** A CA's names become
   SDSI names, which is the X.509 row of ARCH-0001 §6: a DN as labels under the
   importer's namespace, not the CA's. **adopts**.

## 10. Validity and online tests

### 10.1 What SPKI-06 specifies

A validity is a date window and any number of online tests (L1420). The window's
bounds are A8's quotation; omitting `not-before` is ordinary:

<!-- q L1434-1437 "For example" .. "documentation purposes." -->
> For example, one might omit the <not-before> field, if that date would be before or at the time of creation of the certificate, unless one wanted to note the creation time for documentation purposes.

An online test names who answers and where, and its answer narrows the window:

<!-- q L1460-1463 -->
> <online-test>:: "(" "online" <online-type> <uris> <principal> <online-id> <s-part>* ")" | "(" "online" "new-cert" <uris> ")" ; <online-type>:: "crl" | "reval" | "one-time" ; <online-id>:: "(" "id" <byte-string> ")" ;

<!-- q L1465-1475 -->
> The online test option allows a certificate to be backed up by finer grain validity testing. The online test specification, above, is present in a certificate and shows that the certificate has a finer-grain validity mechanism. The reply from an online test is a digitally signed object, validated by the <principal> given in the test specification. That object includes validity dates, so that once one has the online test response, its validity dates can be intersected with the parent certificate's validity dates to yield the current working validity dates for the certificate.

Three answers, and a fourth request:

<!-- q L1477-1479 -->
> The crl form tells the verifier (or prover, who fetches this information for the verifier, in our standard model), the current list of invalid certificates. If the present certificate is not on

<!-- q L1487 -->
> that list, then the certificate is presumed valid.

<!-- q L1489-1491 -->
> The re-validate form is the logical opposite of the crl. It tells the verifier a list of valid certificates or, more likely, just that the current certificate is valid.

<!-- q L1493-1498 -->
> The one-time form is a re-validate form without validity dates. It must be fetched by the verifier, rather than the prover, since it is valid only for the current verification step. [In effect, it has a validity period of just "now".] The process of getting this one-time revalidation involves sending a unique (and partly random) challenge which is returned as part of the signed response.

(The fourth, `new-cert`, is A9's quotation.) The replies, signed by the principal
the test names:

<!-- q L1929-1930 -->
> The <crl> or <delta-crl> must be signed by the principal indicated in the <online-test> field that directed the CRL to be fetched.

<!-- q L1955-1961 -->
> This construct is the logical opposite of a CRL. With a reval instrument, a certificate is valid if it is listed. There is no delta-reval. One does not need to search an entire list and demonstrate that a given certificate is missing. Therefore, if the certificate in question shows up on a currently valid reval list, then it is valid.

<!-- q L1977-1984 -->
> where the byte string inside <one-valid> is one provided by the caller, expected to be unique over time and unguessable -- e.g., a large random number or random number plus sequence number. This reply should be signed by the <principal> indicated in the (online..) field which directed it to be fetched. This result corresponds to a 0-length validity interval of "now", however the developer wishes to express that.

Who fetches, and the rule that keeps a holder current:

<!-- q L1899-1902 -->
> It is assumed that, except for the one-time test, the prover and not the verifier will fetch any online-test results and then provide those results in the <sequence> being handed to the verifier. A one-time test result must contain a nonce generated by the verifier.

<!-- q L1907-1910 -->
> Each of these instruments contains a <valid-basic> time interval. The instrument is valid only during that interval and a sequence of instruments must be issued for non-overlapping intervals, so that the user of the instrument knows when it has the current one.

And how validities combine during reduction, which R-M-09 restates:

<!-- q L2065-2071 -->
> Validity intersection involves normal intersection of date ranges, if there are not-before or not-after fields in v1 or v2, and union of online tests, if those are present in v1 or v2. Each online test includes a validity period, so there is a resulting validity interval in terms of dates. This can include the string "now", as the product of a one-time online test result. "now" intersects with any date range to yield either "now" or "null".

### 10.2 What ours specifies

<!-- qm spec/SPEC-0004-ksa-trust-evaluation.md L309-318 -->
> A statement `s` is **revoked** at time `t` if and only if the statement set holds a verified `revoke` `r` with `r.says = s.says`, `r.body.revokes` = the digest of `s`, `r` valid at `t`, and `r.valid.not-before ≤ t` (ADR-0003 D5). A `revoke` whose target was made by a different speaker has no effect. A `revoke` that targets a `revoke` has no effect: revocation is permanent. An evaluator decides with the revocations it holds. It cannot know of one it has not received; the answer's reasons MUST state how many revocation statements were considered, and wallets SHOULD obtain current revocations before a high-stakes evaluation. Short validity windows remain RECOMMENDED.

— `spec/SPEC-0004-ksa-trust-evaluation.md`@`bb005ed`, lines 309–318

<!-- qm spec/ADR-0003-ksa-core-decisions.md L51 -->
> | **D5** | **Issuer revocation**: a `revoke` statement by the issuer, naming the revoked statement's digest, effective from its `not before`. | Short validity remains recommended; revocation distribution is not solved here. |

— `spec/ADR-0003-ksa-core-decisions.md`@`bb005ed`, line 51

<!-- qm spec/ARCH-0001-authorization-attestation.md L387 -->
> | Online validity check | §4.1 `Validity.online_check`, R-M-09 | none; `valid` is time only | open; R-O-02 prefers short validity | — |

— `spec/ARCH-0001-authorization-attestation.md`@`bb005ed`, line 387

<!-- qm research/0007-delegation-models/report.md L579-583 "1. SPEC-0004 §7.1 is the" .. "(§8, P4)." -->
> 1. SPEC-0004 §7.1 is the "wandering anti-matter" model SPKI ruled out (RFC 2693 §5.1, *"this process is non-deterministic"*). SPEC-0004 knows this and mitigates it by *reporting* the count rather than by SPKI's non-overlap rule. That is a defensible choice, but it should be recorded as a choice (§8, P4).

— `research/0007-delegation-models/report.md`@`bb005ed`, lines 579–583

### 10.3 Findings

1. **Two revocation models, and SPKI's is the deterministic one (row 38).**
   SPKI-06 puts the revocation route **in the certificate**: the issuer names
   the principal who answers and where to ask. A certificate without an online
   test can only expire (inferred from §4.9.2 and §7.1–§7.2, where every reply
   is fetched through and signed under a test); one with a test cannot be relied
   on without a current reply, and non-overlapping intervals tell a holder when
   it has the current one. KSA puts no route in the statement: any statement can
   be revoked by its speaker, and an evaluator cannot know whether a revocation
   exists that it has not received (SPEC-0004 §11.3). Ours needs no online party;
   SPKI's gives an answer that does not depend on what happens to have arrived.
   R-0007 P4 asks that SPEC-0004 §7.1 record the choice and why; the source
   supplies the wire form of the alternative (§7.1–§7.3 of the draft).
2. **A third party may revoke in SPKI, not in ours (row 37).** The answering
   principal need not be the certificate's issuer (L1460–L1463, L1929–L1930).
   ADR-0003 D5 lets only the speaker revoke. An imported SPKI CRL signed by a
   designated third party has no KSA form; R-0007 P5's escrowed `revoke`, signed
   in advance by the speaker and held by someone else, is the nearest native
   shape (inferred).
3. **Revocation by hash inherits the identity gap (inferred).** A CRL names a
   certificate by the hash of its canonical form (A5); a certificate re-serialised
   in another field order (C6) has another hash and is not on the list. R-0006
   §3.13 found the same hazard in ours: a `revoke` names one permutation of a
   statement's `trusts`.
4. **The window's upper bound is not defined.** Whether a certificate is valid
   at its `not-after` instant is not said (L1432); ours is half-open,
   `t < not-on-or-after` (A8). An import must choose: `not-on-or-after =
   not-after` if SPKI's bound is exclusive, the next second if inclusive (ours,
   open question 9).
5. **Freshness by challenge.** A one-time revalidation is fetched by the
   verifier, carries the verifier's nonce, and is valid only `now`, which
   intersects a window to `now` or `null` (L1493–L1498, L1977–L1984,
   L2069–L2071). KSA's nonce, in SPEC-0001 §8.1, proves a presentation fresh,
   not a statement current (row 49). If ARCH-0001 §5.5's online check is ever
   specified, this is its reference design (inferred).
6. **The reply is not bound to the test that asked for it.** §4.9.2 gives a test
   an `<online-id>` (L1463), §9.2's rule drops it (L2318–L2319), and no reply
   format carries one; the draft's own editorial note asks the question
   (L1888–L1889). A CRL is tied to the test that directed it only by its signer,
   the principal the test names (inferred, SI-7, SI-18).
7. **R-M-09 is SPKI's rule (row 8).** Date ranges intersect, online tests unite,
   and a one-time answer yields `now`. KSA keeps the date half as SPEC-0004
   §6.3's `cap` and has no online half.

## 11. Principals, and hashes as principals

### 11.1 What SPKI-06 specifies

A principal is a key or a hash of one (B9's quotation, L1204–L1210). A hash
names its algorithm and may carry locations; a key may carry locations too:

<!-- q L999-1002 -->
> <hash>:: "(" "hash" <hash-alg-name> <hash-value> <uris>? ")" ; A <hash> object gives the hash of some other object. For example, the public key given above has the following hashes:

<!-- q L791-793 -->
> A public key definition gives everything the user needs to employ the key for checking signatures. The <uri>s, if present, give locations where one might find certificates empowering that public key.

Equality during reduction is equality of keys, however they are written:

<!-- q L2013-2017 -->
> Name reduction is specified in section 5.3. Therefore, in what follows we assume all issuers and subjects are principals. We also assume that all principals are public keys. It is an implementation decision whether to store these as explicit keys, hashes of keys (used as pointers) or addresses pointing to keys.

### 11.2 Findings

1. **One key, many principals (C4).** A key, its md5 hash, its sha1 hash and a
   hash under any URI-named algorithm all denote it, each with or without
   `uris`, and reduction must resolve them to keys before `s1 = i2` (L2060) can
   be tested. Ours has one `kid` per key, so equality is byte equality (A11).
   SPKI's design is the identity-path hazard R-0006 §3.1 names: one value, two
   names, and a comparison that fails silently when an implementation compares
   bytes (inferred).
2. **The algorithm is inside the hash (reproduced).** md5 and sha1 of the
   179-octet canonical key decoded from L826–L829 give exactly the values printed
   at L1004 and L1007, and that key's canonical form opens
   `(10:public-key(13:rsa-pkcs1-md5`. So SPKI's hash principal covers the signature
   algorithm, and a key with `uris` hashes differently from the same key without
   them (inferred from §3.8.1's grammar). This is evidence on ADR-0005's open
   sub-question, **both ways**:

<!-- qm spec/ARCH-0001-authorization-attestation.md L518-522 -->
> - **The inverse question, which RFC 9679 does not reach.** Its AKP defect is an algorithm *inside* the preimage; `SPEC-0002`'s `kid` has none, so identical key octets under two suites yield one `kid`. Today's suites cannot collide (32 against 1952 octets). Whether a future suite with an equal-length encoding needs the suite in the preimage is for this ADR; not answered here.

— `spec/ARCH-0001-authorization-attestation.md`@`bb005ed`, lines 518–522

   *For* putting the suite in the preimage: SPKI does, as OpenPGP v6 does
   (ARCH-0001 §3.4), and no cross-algorithm collision of key encodings can then
   merge two keys. *Against*: SPKI shows the cost ADR-0005 named when it
   rejected a per-suite digest, one key becoming several principals, and adds a
   second cost ADR-0005 avoids by hashing raw key octets only, location hints
   changing identity. ADR-0005 item 4 meets the first with a registry rule:

<!-- qm spec/ADR-0005-dec-003-key-identifier.md L48-53 -->
> 4. **Collisions across key algorithms are prevented by the registry, not the preimage.** The suite code is not hashed. Instead `SPEC-0002` §12.3 gains a rule: a suite whose key algorithm differs from a registered suite's MUST NOT be registered if a valid public-key encoding under it can equal one under the registered suite. Suites that **share** a key algorithm share `kid`s: the key is the principal (R-M-02), whichever suite it signs under.

— `spec/ADR-0005-dec-003-key-identifier.md`@`bb005ed`, lines 48–53

3. **No SPKI-06 issuer is a KSA `KeyId` today (row 11).** The draft defines
   `rsa-pkcs1-md5`, `rsa-pkcs1-sha1`, `rsa-pkcs1` and `dsa-sha1`
   (L2325–L2326), and its elliptic-curve section is a placeholder (L987–L993). No
   KSA suite defines an RSA or DSA public-key encoding, so no `kid` exists for
   such a key; and a `kid` cannot be computed from an md5 or sha1 hash at all.
   R-O-01 therefore fails for every SPKI-06 object under the draft's own
   algorithms until a classical suite is registered (SPEC-0002 §6.2 reserves
   codes 3–7), and SPEC-0001 §5.3's external statement cannot map its speaker in
   the meantime (row 46). Both of the draft's hash algorithms are also broken
   for collision resistance, which its glossary assumes (L381–L382) **[outside
   this source]**.
4. **An object hash may use a digest we have no code for.** `object-hash` takes
   any `<hash>`, md5 and sha1 included; SPEC-0002 §12.5 registers SHA-256,
   SHA-384 and SHA-512 only. Such a subject is refused on import (ours).
5. **SPKI's reason to prefer the hash is partly secrecy** (L1208–L1210): a small
   RSA key kept secret behind its hash. KSA publishes keys (`key-publish`) and
   relies on the suite's strength, not on concealment (inferred). **silent**.
6. **A fully qualified name is a global identifier in SPKI** (A11's quotation,
   L377–L379); in ours names are not globally unique identifiers (ARCH-0001 G1),
   and the identifier of a principal is its `kid`.

## 12. What this fills in mofn report R-0006, and what it corrects in R-0006 and R-0007

**R-0006 §2.2's SPKI row** marks the to-be-signed construction **∅**:

<!-- qm research/0006-mechanism/report.md L230 -->
> | **SPKI/SDSI S-expression cert** | keys and objects may be named by hash; *"a collision-free hash of the public key is also a globally unique identifier"* [@rfc-2693] | **yes — and the canonical form is what is signed.** *"This canonical representation is used for digital signature purposes"* [@rfc-9804] §6.2. No parse-then-verify procedure is stated | the certificate; the exact to-be-signed construction lived in `draft-ietf-spki-cert-structure`, which never published — **∅** | the 5-tuple ⟨Issuer, Subject, Delegation, Tag, Validity⟩ and the name 4-tuple [@rfc-2693]. Authenticated/unauthenticated split **∅**; RFC 9804 has *"no authenticated type indicator"* |

— `research/0006-mechanism/report.md`@`bb005ed`, line 230

Filled from the source:

- **What is hashed:** the canonical S-expression of the signed object, every
  field included: `display`, `comment`, `version`, `uris` (A7; §5.1's
  reproduction shows a hash is over those bytes).
- **What is signed:** the draft says the canonical form feeds every hash and
  every signature function (L553–L555, L675–L676), and the detached
  `signature` names the object's hash, the signer and the value (§3.8.3). It
  never fixes the octets the signature primitive receives: `[PKCS1]` is listed
  among the references (L2459) and cited nowhere in the body (checked by
  search). So the cell can be filled only to *the canonical bytes, by
  hash-then-sign, primitive input unstated* (inferred). The §3.8.3.2 samples
  fit that reading and rule out the other: the DSA sample verifies with the
  printed hash value as its digest and not with the hash of the `(hash ...)`
  object, and the RSA sample's recovered block ends in the printed hash value
  (`examples/reproduce.py`; `draft-ietf-spki-cert-structure#R-0398`).
- **Authenticated and not:** authenticated, the whole signed object;
  unauthenticated, the `signature` object's own fields (its `<hash>` checked by
  recomputing, its `<principal>` by the signature verifying), the order of the
  `sequence`, its `(do hash …)` operations (L1847–L1856) and any base64 wrapping
  (inferred).
- **Type indicator:** the object's first element is inside the hashed bytes
  (L524–L526, L748–L751), which is the convention R-0006 §3.5 proposed for
  option 1. SPKI-06 uses it; it does not domain-separate (C2).
- **Parse before verify:** nothing is ordered (A7). Hashing needs the object's
  exact extent, so a verifier parses the `sequence`'s framing before checking
  any signature, as SPEC-0002's V1 parses the envelope (inferred).

**R-0006 §2.3 on the lineage:**

<!-- qm research/0006-mechanism/report.md L251-256 "SPKI, the system" .. "canonical form instead [@rfc-9804]." -->
> SPKI, the system `ARCH-0001` §6 calls the *"closest peer"*, signs a canonical form. That is a reversal inside SPKI's own lineage: RFC 2692 asked that *"a certificate should be signed exactly as it is transmitted. There should be no reformatting"* [@rfc-2692], and RFC 9804 resolved the tension by signing the canonical form instead [@rfc-9804].

— `research/0006-mechanism/report.md`@`bb005ed`, lines 251–256

**Narrowed.** SPKI-06 itself requires the canonical form between machines
(A7), so RFC 2692's request is kept in the certificate draft, apart from a
base64 wrapping it permits (L652–L657); the reversal R-0006 describes is RFC
9804's, which obliges an implementation to accept other transports (R-0006
§3.5). R-0006's conclusion, that R-O-05 needs a profile transmitting the
canonical form, is unchanged, and SPKI-06 is nearly that profile: it keeps the
advanced form off the wire and does not say whether a receiver must accept the
wrapping (inferred).

**R-0006 §2.3, third finding** (that SPKI outlined threshold subjects without
specifying them): **confirmed** by §8.4's sketch (§6 above). The same finding's
revocation clause is **contradicted**:

<!-- qm research/0006-mechanism/report.md L281 -->
> Revocation: SCITT and SPKI both leave it out; `ADR-0003` D5 adopts it.

— `research/0006-mechanism/report.md`@`bb005ed`, line 281

SPKI-06 §7 specifies CRLs, delta-CRLs, revalidations and one-time
revalidations, each with a grammar and each signed by the principal the
certificate's online test names (§10 above), and R-0007 §5.4 already records
SPKI's revocation rules from RFC 2693. What this draft leaves out is the online
protocol (L1517–L1520), not revocation.

**R-0006 §4.1** (`AIntersect` closed): **not supported by this draft** (§8.2,
defect 1).

**R-0007 §3.5:** its UC-5 chain fails under this draft's §8.3 (§8.2, defect 2).
Its example also writes `(hash sha256 …)`. SPKI-06's `<hash-alg-name>` does not
name `sha256`; it parses only through the `<uri>` alternative, whose rule is any
byte string (L2289, L2366) (inferred; R-0007 marks the tags as its own, not the
hashes). **R-0007 §5.4**'s SPKI row cites RFC 2693 for three revocation
rules; this draft states the non-overlap rule in its own words (L1907–L1910)
and gives the instruments' wire form (§10).

**R-0006 §8's ingest item** names this record as a stub behind a ∅ cell; this
extraction is that item.

## 13. ARCH-0001 §6's SPKI row: the R-I-01 table WP2 owes (draft)

The row as it stands:

<!-- qm spec/ARCH-0001-authorization-attestation.md L397 -->
> | SPKI/SDSI S-exp cert (RFC 2693 / 9804) | I | E | NameCert, AuthzCert, Threshold | Closest peer; preferred reference mapping |

— `spec/ARCH-0001-authorization-attestation.md`@`bb005ed`, line 397

Every cell below is **ours** and *(inferred)*: the source defines no mapping to
anything. Import keeps the original bytes as an external statement (SPEC-0001
§5.3) in every case; *refused* means no native form is produced.

| SPKI-06 | KSA form | import | export |
|---|---|---|---|
| `cert`, `(issuer <principal>)`, with a tag | `trust` (5): `says`, `this = [1, kid]`, `about`, `may-delegate`, `valid` | translated, never verified natively (row 11) | a `cert` only under a URI-named algorithm (L731–L733), which no SPKI-06 verifier knows |
| `cert`, `(issuer (name K N))`: a name certificate | an `attestation` (4) about a key, assigning N under the importer's names definition (TV-13's shape) | one label, subject a key; a name with several subjects is a group (open question 5) | the same shape, one label |
| subject `object-hash` | target `[2, alg, bytes]` | SHA-256, -384, -512 only; md5 and sha1 refused (§11.2 item 4) | `(object-hash (hash …))` under a URI-named algorithm |
| subject a name | none yet (mofn#143) | refused | — |
| subject `keyholder` | none | refused (open question 14) | — |
| subject `k-of-n` | the threshold form of `trust` | keys only, flat, `K ≥ 1`, `N` equal to the count, members distinct, each a key some suite encodes (row 11); anything else refused (§6) | `k < n` only; `k = n` has no form (open question 1) |
| `(propagate)` | `may-delegate.depth` | per chain: depths that fall by one per hop, the root entry's at least the chain's length (§7.3); one constant depth fails at the first propagating certificate | over-grants; `ranges`, key lists and the cap are lost (open question 10) |
| `tag` | `about` | §8.4: sets, numeric and time ranges map; `prefix`, `alpha`, `binary` refused | ranges as `(* set …)` or `(* range …)` |
| `not-before`, `not-after` | `valid.not-before`, `valid.not-on-or-after` | boundary rule owed (open question 9) | `not-on-or-after` minus one second, if SPKI's bound is inclusive |
| online tests | none (ARCH-0001 §5.5) | refused unless a current reply is presented, then the window is cut to the reply's (§10) | never emitted |
| `display`, `comment` | none; annotations are never signed | dropped, never rendered (C5) | never emitted |
| `version` | none | version 0 only, in either spelling (SI-1); any other refused (B5) | omitted |
| `issuer-info`, `subject-info`, `uris` | none | dropped as hints | — |
| `signature` | envelope (SPEC-0002 §5) | kept as evidence; not verifiable natively | not producible |
| `public-key`, RSA or DSA | `public-key {alg, pub}` | no key-algorithm code (SPEC-0002 §12.4): refused | — |
| ACL entry | anchor (SPEC-0004 §4.2) | never transmitted (A2); a copy becomes an anchor only by acceptance (ADR-0003 D3, R-I-02) | an anchor is never sent unless published as a statement |
| `sequence`, `(do hash …)` | a presentation (SPEC-0001 §8.1) | structure not carried | — |
| `crl`, `delta-crl`, `reval` | `revoke` (speaker only) | refused: the CRL's signer may not be the issuer (§10.3 item 2), and it names the SPKI hash, not the digest of our translation | none: our statements name no online test |
| result certificate (§8.7) | the verifier's own `trust`, anchored (`own statement`) | — | — |

## 14. Source inconsistencies

Found in this pass by reading and by script. The script audited every
`<name>::` definition and every `<name>` reference in the 2622 lines, a name
broken across a line end joined and a name that starts with a digit
(`<5-tuple>`) included: 154 definition sites for 92 names (58 defined twice,
mostly once in the text and once in §9.2; 2 three times, `<subj-obj>`, whose
second site is §4.5's principals-only restriction at L1237, and `<reval>`; 32
once), and 95 names referenced, the three extra being the undefined names of
SI-11. Line numbers are the source's.

| id | inconsistency | lines |
|---|---|---|
| SI-1 | `version` is an `<integer>` in both grammars, while the prose calls versions alphanumeric strings and spells version 0 as a quoted `"0"`, an ASCII digit, where the integer 0 is one zero octet; version 0 thus has two spellings and two hashes | L1169, L1171–L1173, L2371; L614–L615 |
| SI-2 | `K < N` excludes *n*-of-*n*; example 4 requires both of two issuers | L1289; L1344–L1350 |
| SI-3 | §4.8: an added trailing field restricts a tag; §8.3 rule 2: unequal tags without `*`-forms intersect to `null` | L1405–L1408; L2096–L2097 |
| SI-4 | §8.3 defines no intersection of two `*`-forms; §8.7's result certificate reduces with no request to intersect against | L2088–L2092; L2144–L2147 |
| SI-5 | the name-certificate example, in advanced and canonical form, carries `not-after` directly in `cert`; `<name-cert>` admits it only inside `(valid …)` | L1698–L1707; L1636–L1637, L2370 |
| SI-6 | §5.1's template writes `<name>` where `<issuer-name>` has a `<byte-string>` | L1630–L1634; L1639–L1640 |
| SI-7 | `<online-test>` has an `<online-id>` and a `new-cert` alternative in §4.9.2, neither in §9.2 | L1460–L1463; L2318–L2319 |
| SI-8 | `<reval>` is defined three times: with `<reval-list>` (§7.2), with `<subj-hash> <one-valid>` (§7.3), and with `<reval-hash-list> <reval-body>` (§9.2), the last carrying a hash list where §7.3 carries `(cert <hash>)` | L1952–L1953; L1973–L1975; L2329–L2331, L2348 |
| SI-9 | `<crl>` uses `<cancel-list>` in §7.1 and `<crl-hash-list>` in §9.2; `<delta-crl>` uses `<hash-of-pred>` and `<hash-of-crl>`; §9.2 also defines `<hash-list>`, which no rule references | L1919–L1923; L2267–L2268, L2274–L2275, L2290–L2291 |
| SI-10 | `<seq-ent>` lacks `<name-cert>` in §6.2 and has it in §9.2 | L1832–L1833; L2334, L2342 |
| SI-11 | referenced, never defined: `<threshold-subj>` and `<tag-body>` (§8.1), `<fq-name5>` (§9.2) | L2031, L2039, L2353 |
| SI-12 | §8.4's heading names `(subject (threshold ..))` where the syntax is `k-of-n`, and its procedure of copying the tuple *K* times cannot know which *K* of *N* to copy (inferred) | L2126, L1287; L2129–L2134 |
| SI-13 | section numbering runs §8.4 to §8.7, in the text and the table of contents | L2126, L2142; L246–L247 |
| SI-14 | `<dsa-sig-val>` uses `dsa-sha1-sig` and is referenced by no rule; the sample DSA signature follows `<sig-val>` with `dsa-sha1` | L2277, L2285; L1095–L1097 |
| SI-15 | the range orderings `alpha`, `numeric`, `time`, `binary`, `date` are named once and defined nowhere | L2327 |
| SI-16 | editorial residue: the elliptic-curve placeholder, the open question about CRL identity, a doubled *of* | L987–L993; L1888–L1889; L2129 |
| SI-17 | `<pub-sig-alg-id>` includes `rsa-pkcs1` with no hash named and no text describing it (inferred) | L2325 |
| SI-18 | a reply carries no field naming the test or certificate it answers; only its signer ties it to a test (inferred) | L1919–L1923, L1952–L1953; L1888–L1889 |
| SI-19 | §6.2 describes the one defined opcode twice: first as hashing the most recent key or certificate in the sequence, then as hashing the immediately preceding item, whatever it is; the two differ when that item is a CRL, a reval, a signature or another op (inferred) | L1838–L1839; L1848–L1850 |

Not inconsistencies, but gaps the draft states as intended: the online-test
protocol (L1517–L1520), the 5-tuple's data structure (L2009–L2011), threshold
reduction (L2128) and name-reduction termination (L1737–L1739) are each deferred
to another document.

## 15. Requirement ids

The requirements lane wrote `requirements.yaml` concurrently, append-only, and
finished its own pass before this section was generated. Every id below was
emitted **by script** from that file, never typed. At generation it held 461
ids: 402 with `source_lines` and a verbatim text (56 of them `split_of`
children), and 59 inferred, in its own words; both of the library's YAML readers
return the same text, lines and `repeated_in` for every id. Ids are written in
full so that `bin/check-id-joins --resolve` sees them and none can be read as
mofn report R-0006 or R-0007. An id appended after this pass is not reflected;
the join is the test, and a later pass re-runs it.

### 15.1 Quotations

For each of this file's 83 source quotations, every stated requirement whose
lines overlap the quotation's and whose text lies inside it, or contains it: 221
pairs over 76 quotations, each printed and read. *Partly* names a requirement
whose sentence runs past the quotation's edge, which here is always a sentence
that crosses a page and that this file quotes as two markers (*Things to hold*
item 2); 4 such pairs. 7 quotations are carried by no requirement: A1 L89–L93,
A10 L1334–L1342, §6.1 L1319–L1321, §6.1 L1327–L1328, §6.1 L1344–L1350, §6.1
L1352–L1354, §10.1 L1434–L1437. They are the abstract, the threshold commentary
and examples, and the `not-before` example; none states a rule.

4 of the ids below cross a page, and their texts hold the draft's running header
line between the two halves of the sentence:
`draft-ietf-spki-cert-structure#R-0150`,
`draft-ietf-spki-cert-structure#R-0182`,
`draft-ietf-spki-cert-structure#R-0235`,
`draft-ietf-spki-cert-structure#R-0329`. They are the source's own bytes and
`bin/check-quotes` verifies them; `requirements.yaml` names every such entry (9)
in its `extraction_notes` and marks each with `running_header_line`.

| this file | source lines | requirement ids |
|---|---|---|
| A1 | L416–L418 | `draft-ietf-spki-cert-structure#R-0442` |
| A1 | L89–L93 | none carries these words |
| A2 | L1156–L1163 | `draft-ietf-spki-cert-structure#R-0112`, `draft-ietf-spki-cert-structure#R-0113`, `draft-ietf-spki-cert-structure#R-0114` |
| A2 | L1787–L1792 | `draft-ietf-spki-cert-structure#R-0244`, `draft-ietf-spki-cert-structure#R-0245`, `draft-ietf-spki-cert-structure#R-0246` |
| A3 | L1296–L1302 | `draft-ietf-spki-cert-structure#R-0147`, `draft-ietf-spki-cert-structure#R-0451` |
| A3 | L439–L446 | `draft-ietf-spki-cert-structure#R-0020`, `draft-ietf-spki-cert-structure#R-0021`, `draft-ietf-spki-cert-structure#R-0446` |
| A4 | L1261–L1265 | `draft-ietf-spki-cert-structure#R-0137`, `draft-ietf-spki-cert-structure#R-0138` |
| A4 | L381–L384 | `draft-ietf-spki-cert-structure#R-0009`, `draft-ietf-spki-cert-structure#R-0010`, `draft-ietf-spki-cert-structure#R-0011` |
| A5 | L1919–L1923 | `draft-ietf-spki-cert-structure#R-0272`, `draft-ietf-spki-cert-structure#R-0273`, `draft-ietf-spki-cert-structure#R-0274`, `draft-ietf-spki-cert-structure#R-0275` |
| A6 | L1608–L1610 | `draft-ietf-spki-cert-structure#R-0205`, `draft-ietf-spki-cert-structure#R-0206` |
| A6 | L1612–L1618 | `draft-ietf-spki-cert-structure#R-0207`, `draft-ietf-spki-cert-structure#R-0208`, `draft-ietf-spki-cert-structure#R-0209`, `draft-ietf-spki-cert-structure#R-0452` |
| A7 | L545–L548 | `draft-ietf-spki-cert-structure#R-0034`, `draft-ietf-spki-cert-structure#R-0035` |
| A7 | L675–L680 | `draft-ietf-spki-cert-structure#R-0064` |
| A8 | L1432–L1434 | `draft-ietf-spki-cert-structure#R-0170` |
| A8 | L2148–L2153 | `draft-ietf-spki-cert-structure#R-0338`, `draft-ietf-spki-cert-structure#R-0339`, `draft-ietf-spki-cert-structure#R-0340` |
| A9 | L1500–L1502 | `draft-ietf-spki-cert-structure#R-0189` |
| A10 | L1334–L1342 | none carries these words |
| A11 | L377–L379 | `draft-ietf-spki-cert-structure#R-0008` |
| B1 | L2144–L2157 | `draft-ietf-spki-cert-structure#R-0337`, `draft-ietf-spki-cert-structure#R-0338`, `draft-ietf-spki-cert-structure#R-0339`, `draft-ietf-spki-cert-structure#R-0340`, `draft-ietf-spki-cert-structure#R-0341`, `draft-ietf-spki-cert-structure#R-0342` |
| B1 | L2159–L2162 | `draft-ietf-spki-cert-structure#R-0343` |
| B2 | L1287–L1289 | `draft-ietf-spki-cert-structure#R-0142`, `draft-ietf-spki-cert-structure#R-0143`, `draft-ietf-spki-cert-structure#R-0144`, `draft-ietf-spki-cert-structure#R-0145` |
| B3 | L1379–L1383 | `draft-ietf-spki-cert-structure#R-0154`, `draft-ietf-spki-cert-structure#R-0155` |
| B3 | L2059–L2063 | `draft-ietf-spki-cert-structure#R-0308`, `draft-ietf-spki-cert-structure#R-0309`, `draft-ietf-spki-cert-structure#R-0310`, `draft-ietf-spki-cert-structure#R-0311`, `draft-ietf-spki-cert-structure#R-0312` |
| B4 | L1393–L1400 | `draft-ietf-spki-cert-structure#R-0158`, `draft-ietf-spki-cert-structure#R-0159`, `draft-ietf-spki-cert-structure#R-0160`, `draft-ietf-spki-cert-structure#R-0161` |
| B5 | L1171–L1177 | `draft-ietf-spki-cert-structure#R-0116`, `draft-ietf-spki-cert-structure#R-0117`, `draft-ietf-spki-cert-structure#R-0118` |
| B6 | L1445–L1454 | `draft-ietf-spki-cert-structure#R-0172`, `draft-ietf-spki-cert-structure#R-0173`, `draft-ietf-spki-cert-structure#R-0174` |
| B7 | L108–L111 | `draft-ietf-spki-cert-structure#R-0002` |
| B7 | L1841–L1844 | `draft-ietf-spki-cert-structure#R-0254`, `draft-ietf-spki-cert-structure#R-0255` |
| B8 | L697–L704 | `draft-ietf-spki-cert-structure#R-0065`, `draft-ietf-spki-cert-structure#R-0066`, `draft-ietf-spki-cert-structure#R-0067`, `draft-ietf-spki-cert-structure#R-0068`, `draft-ietf-spki-cert-structure#R-0069` |
| B9 | L1204–L1210 | `draft-ietf-spki-cert-structure#R-0124`, `draft-ietf-spki-cert-structure#R-0125`, `draft-ietf-spki-cert-structure#R-0126` |
| C1 | L2073–L2082 | `draft-ietf-spki-cert-structure#R-0317`, `draft-ietf-spki-cert-structure#R-0318`, `draft-ietf-spki-cert-structure#R-0319`, `draft-ietf-spki-cert-structure#R-0320`, `draft-ietf-spki-cert-structure#R-0321` |
| C2 | L1014–L1019 | `draft-ietf-spki-cert-structure#R-0101`, `draft-ietf-spki-cert-structure#R-0102`, `draft-ietf-spki-cert-structure#R-0103` |
| C5 | L1185–L1192 | `draft-ietf-spki-cert-structure#R-0120`, `draft-ietf-spki-cert-structure#R-0121`, `draft-ietf-spki-cert-structure#R-0122`, `draft-ietf-spki-cert-structure#R-0123`, `draft-ietf-spki-cert-structure#R-0461` |
| C5 | L1552–L1553 | `draft-ietf-spki-cert-structure#R-0203` |
| C6 | L775–L782 | `draft-ietf-spki-cert-structure#R-0084`, `draft-ietf-spki-cert-structure#R-0085`, `draft-ietf-spki-cert-structure#R-0086`, `draft-ietf-spki-cert-structure#R-0087`, `draft-ietf-spki-cert-structure#R-0088`, `draft-ietf-spki-cert-structure#R-0089` |
| C7 | L723–L733 | `draft-ietf-spki-cert-structure#R-0072`, `draft-ietf-spki-cert-structure#R-0073`, `draft-ietf-spki-cert-structure#R-0074` |
| C7 | L759–L765 | `draft-ietf-spki-cert-structure#R-0077`, `draft-ietf-spki-cert-structure#R-0078`, `draft-ietf-spki-cert-structure#R-0079` |
| C8 | L609–L615 | `draft-ietf-spki-cert-structure#R-0056`, `draft-ietf-spki-cert-structure#R-0057`, `draft-ietf-spki-cert-structure#R-0058` |
| §5.1 | L371–L372 | `draft-ietf-spki-cert-structure#R-0006` |
| §5.1 | L550–L555 | `draft-ietf-spki-cert-structure#R-0036`, `draft-ietf-spki-cert-structure#R-0037`, `draft-ietf-spki-cert-structure#R-0038`, `draft-ietf-spki-cert-structure#R-0039`, `draft-ietf-spki-cert-structure#R-0040` |
| §5.1 | L589–L594 | `draft-ietf-spki-cert-structure#R-0047`, `draft-ietf-spki-cert-structure#R-0048`, `draft-ietf-spki-cert-structure#R-0049`, `draft-ietf-spki-cert-structure#R-0050`, `draft-ietf-spki-cert-structure#R-0051`, `draft-ietf-spki-cert-structure#R-0052` |
| §5.1 | L434–L437 | `draft-ietf-spki-cert-structure#R-0017`, `draft-ietf-spki-cert-structure#R-0018`, `draft-ietf-spki-cert-structure#R-0019`, `draft-ietf-spki-cert-structure#R-0445` |
| §5.1 | L577–L585 | `draft-ietf-spki-cert-structure#R-0044`, `draft-ietf-spki-cert-structure#R-0045`, `draft-ietf-spki-cert-structure#R-0046` |
| §5.1 | L564–L566 | `draft-ietf-spki-cert-structure#R-0042`, `draft-ietf-spki-cert-structure#R-0043` |
| §6.1 | L1304–L1309 | `draft-ietf-spki-cert-structure#R-0148`, `draft-ietf-spki-cert-structure#R-0149`; partly: `draft-ietf-spki-cert-structure#R-0150` |
| §6.1 | L1316–L1317 | `draft-ietf-spki-cert-structure#R-0151`; partly: `draft-ietf-spki-cert-structure#R-0150` |
| §6.1 | L1319–L1321 | none carries these words |
| §6.1 | L1327–L1328 | none carries these words |
| §6.1 | L1344–L1350 | none carries these words |
| §6.1 | L1352–L1354 | none carries these words |
| §6.1 | L2128–L2134 | `draft-ietf-spki-cert-structure#R-0332`, `draft-ietf-spki-cert-structure#R-0333`, `draft-ietf-spki-cert-structure#R-0334`, `draft-ietf-spki-cert-structure#R-0335` |
| §6.1 | L2136–L2138 | `draft-ietf-spki-cert-structure#R-0336` |
| §7.1 | L1794–L1797 | `draft-ietf-spki-cert-structure#R-0247` |
| §7.4 | L2013–L2017 | `draft-ietf-spki-cert-structure#R-0295`, `draft-ietf-spki-cert-structure#R-0296`, `draft-ietf-spki-cert-structure#R-0297` |
| §7.4 | L1647–L1650 | `draft-ietf-spki-cert-structure#R-0216`, `draft-ietf-spki-cert-structure#R-0217`, `draft-ietf-spki-cert-structure#R-0218`, `draft-ietf-spki-cert-structure#R-0219` |
| §8.1 | L1402–L1408 | `draft-ietf-spki-cert-structure#R-0162`, `draft-ietf-spki-cert-structure#R-0163`, `draft-ietf-spki-cert-structure#R-0164`, `draft-ietf-spki-cert-structure#R-0165` |
| §8.1 | L2088–L2104 | `draft-ietf-spki-cert-structure#R-0322`, `draft-ietf-spki-cert-structure#R-0323`, `draft-ietf-spki-cert-structure#R-0324`, `draft-ietf-spki-cert-structure#R-0325`, `draft-ietf-spki-cert-structure#R-0326`, `draft-ietf-spki-cert-structure#R-0327`, `draft-ietf-spki-cert-structure#R-0328` |
| §8.1 | L2106 | `draft-ietf-spki-cert-structure#R-0329` (contains the quotation) |
| §8.1 | L2114–L2121 | `draft-ietf-spki-cert-structure#R-0330`, `draft-ietf-spki-cert-structure#R-0331`; partly: `draft-ietf-spki-cert-structure#R-0329` |
| §8.1 | L2358–L2363 | `draft-ietf-spki-cert-structure#R-0375`, `draft-ietf-spki-cert-structure#R-0376`, `draft-ietf-spki-cert-structure#R-0377`, `draft-ietf-spki-cert-structure#R-0378`, `draft-ietf-spki-cert-structure#R-0379` |
| §8.1 | L2327 | `draft-ietf-spki-cert-structure#R-0365` |
| §9.1 | L1603–L1606 | `draft-ietf-spki-cert-structure#R-0204` |
| §9.1 | L1636–L1645 | `draft-ietf-spki-cert-structure#R-0211`, `draft-ietf-spki-cert-structure#R-0212`, `draft-ietf-spki-cert-structure#R-0213`, `draft-ietf-spki-cert-structure#R-0214`, `draft-ietf-spki-cert-structure#R-0215` |
| §9.1 | L1658–L1665 | `draft-ietf-spki-cert-structure#R-0220`, `draft-ietf-spki-cert-structure#R-0221`, `draft-ietf-spki-cert-structure#R-0222`, `draft-ietf-spki-cert-structure#R-0223` |
| §9.1 | L1684–L1690 | `draft-ietf-spki-cert-structure#R-0229`, `draft-ietf-spki-cert-structure#R-0230`, `draft-ietf-spki-cert-structure#R-0231`, `draft-ietf-spki-cert-structure#R-0232`, `draft-ietf-spki-cert-structure#R-0233`, `draft-ietf-spki-cert-structure#R-0234` |
| §9.1 | L1715–L1726 | `draft-ietf-spki-cert-structure#R-0235` (contains the quotation), `draft-ietf-spki-cert-structure#R-0236`, `draft-ietf-spki-cert-structure#R-0237` |
| §9.1 | L1737–L1739 | `draft-ietf-spki-cert-structure#R-0238` (contains the quotation), `draft-ietf-spki-cert-structure#R-0239`, `draft-ietf-spki-cert-structure#R-0240` |
| §10.1 | L1434–L1437 | none carries these words |
| §10.1 | L1460–L1463 | `draft-ietf-spki-cert-structure#R-0175`, `draft-ietf-spki-cert-structure#R-0176`, `draft-ietf-spki-cert-structure#R-0177` |
| §10.1 | L1465–L1475 | `draft-ietf-spki-cert-structure#R-0178`, `draft-ietf-spki-cert-structure#R-0179`, `draft-ietf-spki-cert-structure#R-0180` |
| §10.1 | L1477–L1479 | `draft-ietf-spki-cert-structure#R-0181`; partly: `draft-ietf-spki-cert-structure#R-0182` |
| §10.1 | L1487 | `draft-ietf-spki-cert-structure#R-0182` (contains the quotation) |
| §10.1 | L1489–L1491 | `draft-ietf-spki-cert-structure#R-0183` |
| §10.1 | L1493–L1498 | `draft-ietf-spki-cert-structure#R-0184`, `draft-ietf-spki-cert-structure#R-0185`, `draft-ietf-spki-cert-structure#R-0186`, `draft-ietf-spki-cert-structure#R-0187`, `draft-ietf-spki-cert-structure#R-0188` |
| §10.1 | L1929–L1930 | `draft-ietf-spki-cert-structure#R-0278` |
| §10.1 | L1955–L1961 | `draft-ietf-spki-cert-structure#R-0283`, `draft-ietf-spki-cert-structure#R-0284`, `draft-ietf-spki-cert-structure#R-0285` |
| §10.1 | L1977–L1984 | `draft-ietf-spki-cert-structure#R-0290`, `draft-ietf-spki-cert-structure#R-0291`, `draft-ietf-spki-cert-structure#R-0292` |
| §10.1 | L1899–L1902 | `draft-ietf-spki-cert-structure#R-0264`, `draft-ietf-spki-cert-structure#R-0265` |
| §10.1 | L1907–L1910 | `draft-ietf-spki-cert-structure#R-0267`, `draft-ietf-spki-cert-structure#R-0268`, `draft-ietf-spki-cert-structure#R-0269`, `draft-ietf-spki-cert-structure#R-0270` |
| §10.1 | L2065–L2071 | `draft-ietf-spki-cert-structure#R-0313`, `draft-ietf-spki-cert-structure#R-0314`, `draft-ietf-spki-cert-structure#R-0315`, `draft-ietf-spki-cert-structure#R-0316` |
| §11.1 | L999–L1002 | `draft-ietf-spki-cert-structure#R-0099`, `draft-ietf-spki-cert-structure#R-0100` |
| §11.1 | L791–L793 | `draft-ietf-spki-cert-structure#R-0091`, `draft-ietf-spki-cert-structure#R-0092` |
| §11.1 | L2013–L2017 | `draft-ietf-spki-cert-structure#R-0295`, `draft-ietf-spki-cert-structure#R-0296`, `draft-ietf-spki-cert-structure#R-0297` |

### 15.2 Locators cited without a quotation

For every source locator this file cites outside a quotation, in prose or a
table (249 occurrences, 170 distinct), the stated requirements whose
`source_lines` lie inside it or contain it, or whose `repeated_in` lines do: a
§9.2 production identical to an earlier one is carried by the earlier entry.
*Cited at* names the place: an entry (A1–C9), a row of §4, a `T` row of §6.3, an
`SI` row of §14, or a section. 144 locators have ids (292 pairs, each printed
and read). 26 have none: L32, L39–L41, L59, L89–L93, L246–L247, L656–L657,
L826–L829, L872–L887, L929–L939, L987–L993, L1004, L1005, L1007, L1008,
L1095–L1097, L1330–L1332, L1334–L1342, L1344–L1350, L1434–L1437, L1620–L1622,
L1814–L1820, L1888–L1889, L2009–L2011, L2126, L2142, L2459. They are front
matter, a running header, the abstract, the table of contents, two headings,
encoded samples and hash values, examples, editorial notes, a deferral, a remark
on CA names and a reference entry; none states a rule.

| source lines | cited at | requirement ids |
|---|---|---|
| L32 | intro | none |
| L39–L41 | intro | none |
| L59 | intro | none |
| L89–L93 | row 2 | none |
| L108–L111 | row 5 | `draft-ietf-spki-cert-structure#R-0002` |
| L246–L247 | intro, SI-13 | none |
| L377–L379 | §11.2 | `draft-ietf-spki-cert-structure#R-0008` |
| L381–L382 | §11.2 | `draft-ietf-spki-cert-structure#R-0009` |
| L416–L418 | row 2 | `draft-ietf-spki-cert-structure#R-0442` |
| L439–L446 | §6.1 | `draft-ietf-spki-cert-structure#R-0020`, `draft-ietf-spki-cert-structure#R-0021`, `draft-ietf-spki-cert-structure#R-0446` |
| L442 | T10 | `draft-ietf-spki-cert-structure#R-0020`, `draft-ietf-spki-cert-structure#R-0021` |
| L443–L444 | T5 | `draft-ietf-spki-cert-structure#R-0021` |
| L448–L453 | row 4, §9.3 | `draft-ietf-spki-cert-structure#R-0022`, `draft-ietf-spki-cert-structure#R-0447` |
| L522–L526 | row 13 | `draft-ietf-spki-cert-structure#R-0027`, `draft-ietf-spki-cert-structure#R-0028`, `draft-ietf-spki-cert-structure#R-0029`, `draft-ietf-spki-cert-structure#R-0030` |
| L524–L526 | row 14, §5.6, §12 | `draft-ietf-spki-cert-structure#R-0029`, `draft-ietf-spki-cert-structure#R-0030` |
| L545–L548 | row 14 | `draft-ietf-spki-cert-structure#R-0034`, `draft-ietf-spki-cert-structure#R-0035` |
| L546–L548 | §5.3 | `draft-ietf-spki-cert-structure#R-0035` |
| L550–L553 | row 19 | `draft-ietf-spki-cert-structure#R-0036`, `draft-ietf-spki-cert-structure#R-0037` |
| L553–L555 | C6, §12 | `draft-ietf-spki-cert-structure#R-0038`, `draft-ietf-spki-cert-structure#R-0039`, `draft-ietf-spki-cert-structure#R-0040` |
| L577–L585 | row 20, row 21 | `draft-ietf-spki-cert-structure#R-0044`, `draft-ietf-spki-cert-structure#R-0045`, `draft-ietf-spki-cert-structure#R-0046` |
| L581–L585 | row 27 | `draft-ietf-spki-cert-structure#R-0045`, `draft-ietf-spki-cert-structure#R-0046` |
| L589–L594 | row 19 | `draft-ietf-spki-cert-structure#R-0047`, `draft-ietf-spki-cert-structure#R-0048`, `draft-ietf-spki-cert-structure#R-0049`, `draft-ietf-spki-cert-structure#R-0050`, `draft-ietf-spki-cert-structure#R-0051`, `draft-ietf-spki-cert-structure#R-0052` |
| L590 | §5.6 | `draft-ietf-spki-cert-structure#R-0048` |
| L591 | §5.3 | `draft-ietf-spki-cert-structure#R-0049` |
| L594 | §5.6 | `draft-ietf-spki-cert-structure#R-0052` |
| L609–L612 | row 21 | `draft-ietf-spki-cert-structure#R-0056`, `draft-ietf-spki-cert-structure#R-0057` |
| L609–L615 | §5.1 | `draft-ietf-spki-cert-structure#R-0056`, `draft-ietf-spki-cert-structure#R-0057`, `draft-ietf-spki-cert-structure#R-0058` |
| L611–L612 | row 31 | `draft-ietf-spki-cert-structure#R-0057` |
| L614–L615 | SI-1 | `draft-ietf-spki-cert-structure#R-0058` |
| L652–L657 | §5.3, §5.6, §12 | `draft-ietf-spki-cert-structure#R-0063` |
| L656–L657 | §5.1 | none |
| L675–L676 | §12 | `draft-ietf-spki-cert-structure#R-0064` |
| L675–L680 | row 14 | `draft-ietf-spki-cert-structure#R-0064` |
| L697–L704 | A7, row 23 | `draft-ietf-spki-cert-structure#R-0065`, `draft-ietf-spki-cert-structure#R-0066`, `draft-ietf-spki-cert-structure#R-0067`, `draft-ietf-spki-cert-structure#R-0068`, `draft-ietf-spki-cert-structure#R-0069` |
| L711–L717 | B8, row 23, §5.4 | `draft-ietf-spki-cert-structure#R-0070`, `draft-ietf-spki-cert-structure#R-0071` |
| L723–L733 | row 24 | `draft-ietf-spki-cert-structure#R-0072`, `draft-ietf-spki-cert-structure#R-0073`, `draft-ietf-spki-cert-structure#R-0074` |
| L729–L730 | row 20, row 21, §5.3, §5.7 | `draft-ietf-spki-cert-structure#R-0073` |
| L731–L733 | §13 | `draft-ietf-spki-cert-structure#R-0074` |
| L748–L751 | §12 | `draft-ietf-spki-cert-structure#R-0075`, `draft-ietf-spki-cert-structure#R-0450` |
| L759–L765 | row 24 | `draft-ietf-spki-cert-structure#R-0077`, `draft-ietf-spki-cert-structure#R-0078`, `draft-ietf-spki-cert-structure#R-0079` |
| L762–L765 | §5.3 | `draft-ietf-spki-cert-structure#R-0079` |
| L767–L773 | §5.6 | `draft-ietf-spki-cert-structure#R-0080`, `draft-ietf-spki-cert-structure#R-0081`, `draft-ietf-spki-cert-structure#R-0082`, `draft-ietf-spki-cert-structure#R-0083` |
| L772–L773 | §5.6 | `draft-ietf-spki-cert-structure#R-0083` |
| L775–L782 | C6, row 21, row 31, §5.1, §5.6 | `draft-ietf-spki-cert-structure#R-0084`, `draft-ietf-spki-cert-structure#R-0085`, `draft-ietf-spki-cert-structure#R-0086`, `draft-ietf-spki-cert-structure#R-0087`, `draft-ietf-spki-cert-structure#R-0088`, `draft-ietf-spki-cert-structure#R-0089` |
| L779 | intro | `draft-ietf-spki-cert-structure#R-0087`, `draft-ietf-spki-cert-structure#R-0088` |
| L826–L829 | C4, §5.1, §5.6, §11.2 | none |
| L826–L939 | C8 | `draft-ietf-spki-cert-structure#R-0095`, `draft-ietf-spki-cert-structure#R-0096` |
| L872–L887 | §5.1 | none |
| L929–L939 | §5.1 | none |
| L987–L993 | §11.2, SI-16 | none |
| L999 | C4 | `draft-ietf-spki-cert-structure#R-0099` |
| L1004 | C4, §5.1, §11.2 | none |
| L1005 | §5.1 | none |
| L1007 | C4, §5.1, §11.2 | none |
| L1008 | §5.1 | none |
| L1016–L1019 | row 30 | `draft-ietf-spki-cert-structure#R-0102`, `draft-ietf-spki-cert-structure#R-0103` |
| L1095–L1097 | SI-14 | none |
| L1162–L1163 | row 16 | `draft-ietf-spki-cert-structure#R-0114` |
| L1169 | SI-1 | `draft-ietf-spki-cert-structure#R-0115` |
| L1171–L1173 | row 31, §5.1, SI-1 | `draft-ietf-spki-cert-structure#R-0116`, `draft-ietf-spki-cert-structure#R-0117` |
| L1176–L1177 | row 25 | `draft-ietf-spki-cert-structure#R-0118` |
| L1204–L1210 | §11.1 | `draft-ietf-spki-cert-structure#R-0124`, `draft-ietf-spki-cert-structure#R-0125`, `draft-ietf-spki-cert-structure#R-0126` |
| L1206 | C4, row 2, row 11 | `draft-ietf-spki-cert-structure#R-0125` |
| L1208–L1210 | §11.2 | `draft-ietf-spki-cert-structure#R-0126` |
| L1230–L1233 | §9.3 | `draft-ietf-spki-cert-structure#R-0130`, `draft-ietf-spki-cert-structure#R-0131` |
| L1232–L1233 | row 17, T3 | `draft-ietf-spki-cert-structure#R-0131` |
| L1237 | §14 | `draft-ietf-spki-cert-structure#R-0132`, `draft-ietf-spki-cert-structure#R-0133` |
| L1261–L1265 | row 34 | `draft-ietf-spki-cert-structure#R-0137`, `draft-ietf-spki-cert-structure#R-0138` |
| L1269–L1281 | row 35 | `draft-ietf-spki-cert-structure#R-0139`, `draft-ietf-spki-cert-structure#R-0140`, `draft-ietf-spki-cert-structure#R-0141` |
| L1287 | row 17, §5.3, SI-12 | `draft-ietf-spki-cert-structure#R-0142` |
| L1287–L1289 | §6.1 | `draft-ietf-spki-cert-structure#R-0142`, `draft-ietf-spki-cert-structure#R-0143`, `draft-ietf-spki-cert-structure#R-0144`, `draft-ietf-spki-cert-structure#R-0145` |
| L1289 | row 22, SI-2 | `draft-ietf-spki-cert-structure#R-0143`, `draft-ietf-spki-cert-structure#R-0144`, `draft-ietf-spki-cert-structure#R-0145` |
| L1296 | row 44, T7 | `draft-ietf-spki-cert-structure#R-0147` |
| L1296–L1302 | §6.1 | `draft-ietf-spki-cert-structure#R-0147`, `draft-ietf-spki-cert-structure#R-0451` |
| L1304–L1317 | row 43, T5 | `draft-ietf-spki-cert-structure#R-0148`, `draft-ietf-spki-cert-structure#R-0149`, `draft-ietf-spki-cert-structure#R-0150`, `draft-ietf-spki-cert-structure#R-0151` |
| L1330–L1332 | §6.1 | none |
| L1334–L1342 | row 50 | none |
| L1344–L1350 | A9, row 12, SI-2 | none |
| L1379 | §5.5 | `draft-ietf-spki-cert-structure#R-0154` |
| L1379–L1383 | row 9, §7.1 | `draft-ietf-spki-cert-structure#R-0154`, `draft-ietf-spki-cert-structure#R-0155` |
| L1389–L1391 | §8.1 | `draft-ietf-spki-cert-structure#R-0156`, `draft-ietf-spki-cert-structure#R-0157` |
| L1405–L1408 | B5, SI-3 | `draft-ietf-spki-cert-structure#R-0163`, `draft-ietf-spki-cert-structure#R-0164`, `draft-ietf-spki-cert-structure#R-0165` |
| L1420 | §10.1 | `draft-ietf-spki-cert-structure#R-0167` |
| L1432 | B6, §10.3 | `draft-ietf-spki-cert-structure#R-0170` |
| L1434–L1437 | §5.1 | none |
| L1443 | B6 | `draft-ietf-spki-cert-structure#R-0171` |
| L1460–L1463 | row 37, §10.3, SI-7 | `draft-ietf-spki-cert-structure#R-0175`, `draft-ietf-spki-cert-structure#R-0176`, `draft-ietf-spki-cert-structure#R-0177` |
| L1463 | §10.3 | `draft-ietf-spki-cert-structure#R-0177` |
| L1493–L1498 | row 49, §10.3 | `draft-ietf-spki-cert-structure#R-0184`, `draft-ietf-spki-cert-structure#R-0185`, `draft-ietf-spki-cert-structure#R-0186`, `draft-ietf-spki-cert-structure#R-0187`, `draft-ietf-spki-cert-structure#R-0188` |
| L1500–L1502 | row 12 | `draft-ietf-spki-cert-structure#R-0189` |
| L1517–L1520 | §12, §14 | `draft-ietf-spki-cert-structure#R-0192`, `draft-ietf-spki-cert-structure#R-0193`, `draft-ietf-spki-cert-structure#R-0194` |
| L1608–L1618 | row 3 | `draft-ietf-spki-cert-structure#R-0205`, `draft-ietf-spki-cert-structure#R-0206`, `draft-ietf-spki-cert-structure#R-0207`, `draft-ietf-spki-cert-structure#R-0208`, `draft-ietf-spki-cert-structure#R-0209`, `draft-ietf-spki-cert-structure#R-0452` |
| L1620–L1622 | §9.3 | none |
| L1630–L1634 | §9.3, SI-6 | `draft-ietf-spki-cert-structure#R-0210` |
| L1636–L1637 | §9.3, SI-5 | `draft-ietf-spki-cert-structure#R-0211` |
| L1636–L1648 | row 4 | `draft-ietf-spki-cert-structure#R-0211`, `draft-ietf-spki-cert-structure#R-0212`, `draft-ietf-spki-cert-structure#R-0213`, `draft-ietf-spki-cert-structure#R-0214`, `draft-ietf-spki-cert-structure#R-0215`, `draft-ietf-spki-cert-structure#R-0216`, `draft-ietf-spki-cert-structure#R-0217`, `draft-ietf-spki-cert-structure#R-0218` |
| L1636–L1650 | row 28 | `draft-ietf-spki-cert-structure#R-0211`, `draft-ietf-spki-cert-structure#R-0212`, `draft-ietf-spki-cert-structure#R-0213`, `draft-ietf-spki-cert-structure#R-0214`, `draft-ietf-spki-cert-structure#R-0215`, `draft-ietf-spki-cert-structure#R-0216`, `draft-ietf-spki-cert-structure#R-0217`, `draft-ietf-spki-cert-structure#R-0218`, `draft-ietf-spki-cert-structure#R-0219` |
| L1639–L1640 | SI-6 | `draft-ietf-spki-cert-structure#R-0212` |
| L1647 | row 31, §5.1 | `draft-ietf-spki-cert-structure#R-0216`, `draft-ietf-spki-cert-structure#R-0217` |
| L1647–L1650 | §9.3 | `draft-ietf-spki-cert-structure#R-0216`, `draft-ietf-spki-cert-structure#R-0217`, `draft-ietf-spki-cert-structure#R-0218`, `draft-ietf-spki-cert-structure#R-0219` |
| L1658 | §9.3 | `draft-ietf-spki-cert-structure#R-0220` |
| L1660–L1665 | §7.4, §9.3, §16 | `draft-ietf-spki-cert-structure#R-0221`, `draft-ietf-spki-cert-structure#R-0222`, `draft-ietf-spki-cert-structure#R-0223` |
| L1684–L1690 | row 3 | `draft-ietf-spki-cert-structure#R-0229`, `draft-ietf-spki-cert-structure#R-0230`, `draft-ietf-spki-cert-structure#R-0231`, `draft-ietf-spki-cert-structure#R-0232`, `draft-ietf-spki-cert-structure#R-0233`, `draft-ietf-spki-cert-structure#R-0234` |
| L1689–L1690 | §9.3 | `draft-ietf-spki-cert-structure#R-0234` |
| L1698–L1702 | §9.3 | `draft-ietf-spki-cert-structure#R-0235` |
| L1698–L1707 | SI-5 | `draft-ietf-spki-cert-structure#R-0235` |
| L1704–L1707 | §5.1, §9.3 | `draft-ietf-spki-cert-structure#R-0235` |
| L1731–L1735 | §9.3 | `draft-ietf-spki-cert-structure#R-0238` |
| L1737–L1739 | row 45, §9.3, §14, §16 | `draft-ietf-spki-cert-structure#R-0238`, `draft-ietf-spki-cert-structure#R-0239`, `draft-ietf-spki-cert-structure#R-0240` |
| L1784–L1785 | A2 | `draft-ietf-spki-cert-structure#R-0243` |
| L1787–L1792 | row 16 | `draft-ietf-spki-cert-structure#R-0244`, `draft-ietf-spki-cert-structure#R-0245`, `draft-ietf-spki-cert-structure#R-0246` |
| L1814–L1820 | §5.1 | none |
| L1832–L1833 | SI-10 | `draft-ietf-spki-cert-structure#R-0249` |
| L1838–L1839 | SI-19 | `draft-ietf-spki-cert-structure#R-0253` |
| L1841–L1844 | row 5 | `draft-ietf-spki-cert-structure#R-0254`, `draft-ietf-spki-cert-structure#R-0255` |
| L1847–L1856 | §12 | `draft-ietf-spki-cert-structure#R-0256`, `draft-ietf-spki-cert-structure#R-0257`, `draft-ietf-spki-cert-structure#R-0258`, `draft-ietf-spki-cert-structure#R-0259`, `draft-ietf-spki-cert-structure#R-0260` |
| L1848–L1850 | SI-19 | `draft-ietf-spki-cert-structure#R-0257` |
| L1888–L1889 | §10.3, SI-16, SI-18 | none |
| L1907–L1910 | row 38, §12 | `draft-ietf-spki-cert-structure#R-0267`, `draft-ietf-spki-cert-structure#R-0268`, `draft-ietf-spki-cert-structure#R-0269`, `draft-ietf-spki-cert-structure#R-0270` |
| L1919–L1923 | row 36, SI-9, SI-18 | `draft-ietf-spki-cert-structure#R-0272`, `draft-ietf-spki-cert-structure#R-0273`, `draft-ietf-spki-cert-structure#R-0274`, `draft-ietf-spki-cert-structure#R-0275` |
| L1929–L1930 | row 37, §10.3 | `draft-ietf-spki-cert-structure#R-0278` |
| L1952–L1953 | SI-8, SI-18 | `draft-ietf-spki-cert-structure#R-0281`, `draft-ietf-spki-cert-structure#R-0282` |
| L1963–L1964 | row 37 | `draft-ietf-spki-cert-structure#R-0286` |
| L1973–L1975 | SI-8 | `draft-ietf-spki-cert-structure#R-0288`, `draft-ietf-spki-cert-structure#R-0289` |
| L1977–L1979 | row 49 | `draft-ietf-spki-cert-structure#R-0290` |
| L1977–L1984 | §10.3 | `draft-ietf-spki-cert-structure#R-0290`, `draft-ietf-spki-cert-structure#R-0291`, `draft-ietf-spki-cert-structure#R-0292` |
| L2009–L2011 | §14 | none |
| L2031 | SI-11 | `draft-ietf-spki-cert-structure#R-0301` |
| L2033 | §5.5, §7.1 | `draft-ietf-spki-cert-structure#R-0302` |
| L2039 | SI-11 | `draft-ietf-spki-cert-structure#R-0305` |
| L2041–L2043 | A2 | `draft-ietf-spki-cert-structure#R-0306` |
| L2059–L2063 | row 9, §7.1 | `draft-ietf-spki-cert-structure#R-0308`, `draft-ietf-spki-cert-structure#R-0309`, `draft-ietf-spki-cert-structure#R-0310`, `draft-ietf-spki-cert-structure#R-0311`, `draft-ietf-spki-cert-structure#R-0312` |
| L2060 | §11.2 | `draft-ietf-spki-cert-structure#R-0308`, `draft-ietf-spki-cert-structure#R-0309` |
| L2063 | A8 | `draft-ietf-spki-cert-structure#R-0308`, `draft-ietf-spki-cert-structure#R-0312` |
| L2065–L2071 | row 8 | `draft-ietf-spki-cert-structure#R-0313`, `draft-ietf-spki-cert-structure#R-0314`, `draft-ietf-spki-cert-structure#R-0315`, `draft-ietf-spki-cert-structure#R-0316` |
| L2069–L2071 | §10.3 | `draft-ietf-spki-cert-structure#R-0315`, `draft-ietf-spki-cert-structure#R-0316` |
| L2088–L2092 | §8.2, SI-4 | `draft-ietf-spki-cert-structure#R-0322`, `draft-ietf-spki-cert-structure#R-0323` |
| L2096–L2097 | row 48, SI-3 | `draft-ietf-spki-cert-structure#R-0325` |
| L2126 | SI-12, SI-13 | none |
| L2128 | T8, §14 | `draft-ietf-spki-cert-structure#R-0332` |
| L2128–L2134 | row 43 | `draft-ietf-spki-cert-structure#R-0332`, `draft-ietf-spki-cert-structure#R-0333`, `draft-ietf-spki-cert-structure#R-0334`, `draft-ietf-spki-cert-structure#R-0335` |
| L2129 | SI-16 | `draft-ietf-spki-cert-structure#R-0332`, `draft-ietf-spki-cert-structure#R-0333` |
| L2129–L2134 | SI-12 | `draft-ietf-spki-cert-structure#R-0333`, `draft-ietf-spki-cert-structure#R-0334`, `draft-ietf-spki-cert-structure#R-0335` |
| L2133–L2134 | T6 | `draft-ietf-spki-cert-structure#R-0335` |
| L2142 | SI-13 | none |
| L2144–L2147 | §8.2, SI-4 | `draft-ietf-spki-cert-structure#R-0337` |
| L2267–L2268 | SI-9 | `draft-ietf-spki-cert-structure#R-0349`, `draft-ietf-spki-cert-structure#R-0350` |
| L2268 | §5.3 | `draft-ietf-spki-cert-structure#R-0350` |
| L2274–L2275 | SI-9 | `draft-ietf-spki-cert-structure#R-0351` |
| L2277 | SI-14 | `draft-ietf-spki-cert-structure#R-0352` |
| L2285 | SI-14 | `draft-ietf-spki-cert-structure#R-0352` |
| L2289 | C4, row 11, §5.3, §12 | `draft-ietf-spki-cert-structure#R-0354` |
| L2290–L2291 | SI-9 | `draft-ietf-spki-cert-structure#R-0355`, `draft-ietf-spki-cert-structure#R-0356` |
| L2302 | T1 | `draft-ietf-spki-cert-structure#R-0359` |
| L2318–L2319 | §10.3, SI-7 | `draft-ietf-spki-cert-structure#R-0363` |
| L2325 | SI-17 | `draft-ietf-spki-cert-structure#R-0364` |
| L2325–L2326 | row 11, §5.3, §11.2 | `draft-ietf-spki-cert-structure#R-0364` |
| L2327 | §8.2, SI-15 | `draft-ietf-spki-cert-structure#R-0365` |
| L2329–L2331 | SI-8 | `draft-ietf-spki-cert-structure#R-0366`, `draft-ietf-spki-cert-structure#R-0367`, `draft-ietf-spki-cert-structure#R-0368` |
| L2330 | §5.3 | `draft-ietf-spki-cert-structure#R-0367` |
| L2334 | SI-10 | `draft-ietf-spki-cert-structure#R-0369` |
| L2342 | SI-10 | `draft-ietf-spki-cert-structure#R-0369` |
| L2348 | SI-8 | `draft-ietf-spki-cert-structure#R-0371` |
| L2353 | SI-11 | `draft-ietf-spki-cert-structure#R-0372` |
| L2358–L2363 | row 42 | `draft-ietf-spki-cert-structure#R-0375`, `draft-ietf-spki-cert-structure#R-0376`, `draft-ietf-spki-cert-structure#R-0377`, `draft-ietf-spki-cert-structure#R-0378`, `draft-ietf-spki-cert-structure#R-0379` |
| L2361 | §5.3 | `draft-ietf-spki-cert-structure#R-0377` |
| L2366 | §12 | `draft-ietf-spki-cert-structure#R-0382` |
| L2370 | §9.3, SI-5 | `draft-ietf-spki-cert-structure#R-0385` |
| L2371 | SI-1 | `draft-ietf-spki-cert-structure#R-0115` (repeated_in) |
| L2459 | §12 | none |

### 15.3 Where the two lanes inferred the same rule

The requirements lane's inferred entries were read against this file's findings,
which were reached separately. 48 of its 59 bear on a finding here; each id was
selected by script from a unique substring of its text and the pair read.
*Agrees*: the same reading. *Adds*: the entry says something this file does not.
*Differs*: the two take different positions, and the open question named stays
open.

| this file | requirement id | the two lanes |
|---|---|---|
| C6, §5.1 item 1, §5.3 | `draft-ietf-spki-cert-structure#R-0392` | agrees: another field order is another canonical form, with another hash |
| C6 | `draft-ietf-spki-cert-structure#R-0394` | adds the parse rule a free order needs |
| C8, §5.1 item 2 | `draft-ietf-spki-cert-structure#R-0389` | agrees |
| SI-1, §5.1 item 3 | `draft-ietf-spki-cert-structure#R-0400` | agrees |
| B5 | `draft-ietf-spki-cert-structure#R-0401` | adds: a CRL, delta-CRL, reval or ACL carries a version no rule covers; B5 now carries the point |
| C5 | `draft-ietf-spki-cert-structure#R-0402` | agrees |
| B6 | `draft-ietf-spki-cert-structure#R-0408` | adds a rejection of a malformed date, which this file says the draft never states |
| §10.3 item 4, open question 9 | `draft-ietf-spki-cert-structure#R-0407` | **differs**: that lane takes the inclusive reading as its own; this file leaves the boundary open |
| T1, T2, SI-2, open question 1 | `draft-ietf-spki-cert-structure#R-0403` | agrees, including that `K = N` is unsettled |
| T7 | `draft-ietf-spki-cert-structure#R-0404` | agrees: the same gap, closed the way KSA closes it |
| T6, open question 2 | `draft-ietf-spki-cert-structure#R-0435` | agrees with T6's pairwise reading |
| T5, §6.4 item 2 | `draft-ietf-spki-cert-structure#R-0456` | agrees: an `object-hash` subject can only end a chain |
| SI-3, §8.2 defect 2 | `draft-ietf-spki-cert-structure#R-0405` | agrees |
| SI-4, §8.2 defect 1 | `draft-ietf-spki-cert-structure#R-0434` | adds: such an implementation answers `null`, never an operand |
| §8.2 defect 1 | `draft-ietf-spki-cert-structure#R-0453` | agrees: a request is a tag without `*`-forms, which is why the missing meet does not bite at a request |
| SI-15, §8.2 defect 3 | `draft-ietf-spki-cert-structure#R-0432` | agrees, and adds the undefined limit operators `g`, `ge`, `l`, `le` |
| §8.4 | `draft-ietf-spki-cert-structure#R-0430` | adds the element-wise recursion an import mapping needs |
| §8.4 | `draft-ietf-spki-cert-structure#R-0431` | adds how a set's results combine |
| §8.2 | `draft-ietf-spki-cert-structure#R-0433` | agrees: a display type can narrow a grant to nothing |
| §7.1 | `draft-ietf-spki-cert-structure#R-0424` | agrees |
| A2 | `draft-ietf-spki-cert-structure#R-0425` | agrees |
| §7.4, open question 4 | `draft-ietf-spki-cert-structure#R-0412` | agrees |
| §9.3 item 3, open question 5 | `draft-ietf-spki-cert-structure#R-0413` | agrees |
| §9.3 item 4 | `draft-ietf-spki-cert-structure#R-0416` | adds the validity bound, which §9.3 item 4 now carries |
| §9.3 item 5, open question 6 | `draft-ietf-spki-cert-structure#R-0417` | agrees |
| C4, §11.2 item 2 | `draft-ietf-spki-cert-structure#R-0396` | agrees: the same reproduction |
| §11.2 item 1 | `draft-ietf-spki-cert-structure#R-0454` | agrees |
| §11.2 item 1, row 41 | `draft-ietf-spki-cert-structure#R-0418` | agrees |
| §11.2 item 4 | `draft-ietf-spki-cert-structure#R-0459` | agrees |
| §13 | `draft-ietf-spki-cert-structure#R-0457` | agrees: a location is a hint, never a ground for trust |
| §12 | `draft-ietf-spki-cert-structure#R-0398` | agrees, names the three readings, and records that the samples settle them by example |
| A7, §12 | `draft-ietf-spki-cert-structure#R-0397` | consistent: it puts the signature check before reduction, not before parsing, and finds no section that states it |
| row 19 | `draft-ietf-spki-cert-structure#R-0386` | the receiver rule row 19 says the draft never states, inferred there |
| §5.3 condition (3) | `draft-ietf-spki-cert-structure#R-0387` | agrees |
| §5.1 | `draft-ietf-spki-cert-structure#R-0388` | agrees |
| §5.3 condition (6) | `draft-ietf-spki-cert-structure#R-0393` | agrees |
| A5, §10.3 item 3 | `draft-ietf-spki-cert-structure#R-0422` | adds: over which bytes is never said |
| §10.1 | `draft-ietf-spki-cert-structure#R-0426` | agrees |
| §10.3 item 5 | `draft-ietf-spki-cert-structure#R-0427` | agrees |
| C1 | `draft-ietf-spki-cert-structure#R-0428` | adds: a `null` validity stops reduction as a `null` tag does |
| SI-9 | `draft-ietf-spki-cert-structure#R-0423` | adds a gap this file did not list |
| §10 | `draft-ietf-spki-cert-structure#R-0421` | adds a gap this file did not list |
| SI-7, SI-18, §10.3 item 6 | `draft-ietf-spki-cert-structure#R-0411` | agrees |
| SI-19 | `draft-ietf-spki-cert-structure#R-0419` | agrees; found separately |
| §12 | `draft-ietf-spki-cert-structure#R-0455` | adds: an undefined op makes the sequence malformed |
| B1, A8 | `draft-ietf-spki-cert-structure#R-0436` | agrees |
| B1 | `draft-ietf-spki-cert-structure#R-0437` | adds: the verifier must treat its own key as `self`, which B1 now carries |
| B7 | `draft-ietf-spki-cert-structure#R-0429` | related: the order in which tuples combine, not the order of the input |

## 16. Open questions

Nothing here is decided; each names who would decide it.

1. **`K < N` against `k ≤ n`.** Does an R-I-01 export of SPKI refuse
   *n*-of-*n* (TV-10), or read SPKI's `K < N` as a defect (SI-2) and emit
   `K = N` anyway? WP2's owner.
2. **What a threshold join grants.** SPEC-0004 §6.4 requires identical `about`
   and `may-delegate`; SPKI leaves the joined tuple undefined, and its pairwise
   rule would intersect. Is `identical` byte equality, set equality, or meant as
   a meet? R-0006 §3.13 raised it; SPKI-06 does not answer it. SPEC-0004's
   decision makers.
3. **Threshold members.** ARCH-0001 §4.1's `Threshold.members` is
   `[Principal]` (names and nesting allowed, as in SPKI); SPEC-0002 §8.6 is
   `[2* kid]`. Is the narrowing the decision, so that §4.1 is corrected under
   ADR-0003, or is a richer form owed? DL-0019 left it open.
4. **Names and the depth bound.** When mofn#143 specifies compound-name
   resolution, do name hops count against `depth` and SPEC-0004 §6.5? SPKI says
   no and lets a name pass everything (§7.4).
5. **Is a KSA name a group?** In SPKI every name is (L1660–L1665). Two naming
   attestations with one value make a group under that reading; ARCH-0001 §5.5
   says `Group` has no form and no consumer.
6. **Termination of name resolution.** SPKI-06 defers it (L1737–L1739). Which
   bound does mofn#143 state?
7. **Online validity.** ARCH-0001 §5.5 leaves `online_check` open. If it is
   ever specified, SPKI-06's model (route in the certificate, signed replies,
   non-overlapping intervals, verifier nonce) is the reference. R-0007 P4 asks
   SPEC-0004 §7.1 to record why count-reporting was chosen instead.
8. **A revoker the issuer designates.** Is R-0007 P5's escrowed `revoke` the
   intended equivalent of SPKI's online-test principal, or is a designated
   revoker wanted?
9. **SPKI's `not-after` boundary.** Inclusive or exclusive on import? The
   requirements lane reads both bounds as inclusive, as its own reading
   (`draft-ietf-spki-cert-structure#R-0407`); ours is half-open, so under that
   reading an import's `not-on-or-after` is the next second.
10. **Mapping `may-delegate`.** Every export of `depth ≥ 1`, `ranges` or key
    lists to SPKI over-grants, and an import of `(propagate)` works per chain,
    not per certificate (§7.3). Should the R-I-01 table refuse, flag as lossy,
    or translate whole chains?
11. **Is the §6 row's import real?** No SPKI-06 issuer has a `kid` (row 11).
    Should the row read **P** until a classical suite exists, or does WP2 plan
    one? A suite for `rsa-pkcs1-md5` would register an algorithm built on a
    broken hash **[outside this source]**.
12. **Display types on import.** A structure, or refusal? Under option 5 no tag
    can carry one (§5.4 item 2).
13. **R-M-05's ordered set.** R-M-05 keeps SPKI's ordered sequence; SPEC-0004
    §3 forbids input order from mattering. Is R-M-05's wording to be corrected
    under ADR-0003?
14. **Statements about a key's holder.** SPKI separates them (`keyholder`); ours
    does not. Needed?
15. **A threshold anchor across suites.** SPKI's example 3 is a 2-of-3 root over
    three algorithms; with KSA's two suites the same guarantee needs 3-of-4, two
    keys per suite (A10). Should a UC or SPEC-0004 name the pattern for the
    post-quantum transition?
16. **ADR-0004's scoring text.** Four option-1 cells are narrowed here (§5.3),
    none changing the decision. For ADR-0004's second reader, who has not yet
    read it (`reviewed: false`).
17. **SPEC-0004 §6.5.** Does the anchor count as an edge? It moves by one the
    depth at which a `depth` stops mattering (§7.3).
18. **DEC-004 option 1.** Score it as RFC 2693's tags with repairs, since this
    draft's §8.3 cannot be used unchanged (§8.3)?
19. **R-0007 §3.5 and R-0006 §2.3.** R-0007's UC-5 chain fails under SPKI-06's
    rules and holds under RFC 2693's; R-0006 §2.3 says SPKI leaves revocation
    out, and this draft specifies it (§12). Notes in R-0006 and R-0007 are
    mofn's to write, not this library's.
20. **SPEC-0004 §6.3: a test or a cap?** Item 6 follows a statement only if its
    `depth` is below the received one, and the paragraph after the new-state
    table says a statement failing any condition is not followed (C1's
    quotation); the table's own wording (§7.2's last quotation) reads as a cap,
    and as written it never acts. Under
    a cap, an SPKI `(propagate)` would import as one constant depth; under the
    test, only per chain (§7.3). The depth-and-widening vector that DL-0025 and
    DL-0028 record as owed would pin the reading. SPEC-0004's decision makers.

## 17. What this file decides

Nothing. It records evidence against ARCH-0001, ARCH-0002, ADR-0003, ADR-0004,
ADR-0005, SPEC-0001 to SPEC-0004, MD-3, DL-0019, DL-0025, DL-0028 and mofn reports
R-0006 and R-0007, all read at `bb005ed`. No DEC-* is opened, ranked or accepted,
and no document of mofn's is edited.

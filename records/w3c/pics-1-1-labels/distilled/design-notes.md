---
record: pics-1-1-labels
kind: design-notes
title: "pics-1-1-labels — bearing on our design"
extracted: "2026-11-12"
reviewed_by: ""
---

# PICS 1.1 Label Distribution — bearing on our design

*PICS 1.1 Label Distribution: Label Syntax and Communication Protocols* is the
W3C Recommendation of 31 October 1996 (REC-PICS-labels-961031; `record.yaml`
gives `maturity: historic` and records its retirement on 2009-11-24). Source:
the HTML, sha256
`a1acf19869f6b8df9ab7387b6172fd0002960dd0f82983c82df614a0cbd8948d`, equal to
`content.sha256` in `record.yaml` and recomputed from `.cache/` in this pass;
every line number below counts in its `bin/render-w3c --ordinal` rendering,
`.cache/pics-1-1-labels.txt` (792 lines, sha256
`469de99e9845669cd4445879f7272d0513b8e94cd4760490ba3df408edba94f8`, recomputed).
`bin/bcp14-count` finds no BCP 14 keyword in it: its obligations are lowercase.

It defines the label: a list of service sections, each a rating service's URL,
options, and labels of options and ratings. It defines three ways to carry
labels: inside an HTML document, in an RFC-822 header beside the document (with
an HTTP extension to ask for them), and separately from a label bureau. And it
defines two security features: **MIC-md5**, an MD5 digest of the document with
its embedded labels removed, and **signature-RSA-MD5**, an RSA signature over the
MD5 of a *special form* of the label, which the client rebuilds from the label
it received. DSig 1.0 (`pics-dsig-1-0`) later replaced both.

It reaches us in seven ways (`record.yaml` `bears_on`: DEC-002, DEC-007, R-M-07,
R-I-01, R-O-03, R-O-05).

1. **R-O-05.** The special form is a verifier-rebuilt signing input (X-01,
   K-01, §4). In the same section the MIC makes the opposite choice for the
   content (A-01).
2. **R-M-07.** The MIC is a content digest, optional, MD5 only, and taken over
   a transformed document (A-02, C-01, C-03, D-01).
3. **DEC-007**, accepted by `ADR-0007`. The vocabulary is named by a URL that
   the signature does not even cover (X-03).
4. **R-I-01.** The `ARCH-0001` §6 PICS row's import profile (§5).
5. **DEC-002, accepted by `ADR-0004`, and MD-3.** §6, including where this
   source cuts against option 5.
6. **R-O-03.** The special form is a canonicalisation invented in prose, and
   underdetermined (SD-16, §9).
7. **mofn report R-0006** §2.2 and its `unverified.md` §1 ask whether and how a
   PICS 1.1 label binds content. §7 answers.

What it is not: a vocabulary format (that is *Rating Services and Rating
Systems*, `pics-1-1-services`, not read for this file), a trust model (the
client chooses its services), or a delegation model (it names the need and
declines it, A-06).

## Things to hold while reading

1. **Our decisions are read from m-of-n at `d7f7f89`** (origin/main), from the
   read-only snapshot this lane was given. Paths below are `<path>@d7f7f89`.

   | name | path | standing at d7f7f89 |
   |---|---|---|
   | ARCH-0001 v0.3.0 | `spec/ARCH-0001-authorization-attestation.md` | draft; §5 rows, §6 matrix, §7 decisions. **R-O-05 is a §5.3 requirement since v0.2.0** (`DECISIONS-0001` item 4); DEC-001, DEC-002, DEC-003, DEC-007 accepted; DEC-004, DEC-005 open |
   | ARCH-0002 v0.10.0 | `spec/ARCH-0002-key-relative-naming.md` | P1 accepted (`ADR-0001`); P2, P3, P5 with P5.1 and P5.2, P6 accepted (`ADR-0002`); P1.1, P4, P7 draft |
   | ADR-0003 | `spec/ADR-0003-ksa-core-decisions.md` | accepted; the SPECs govern where they differ from an ARCH |
   | ADR-0004 | `spec/ADR-0004-dec-002-encoding.md` | accepted 2026-10-25, `reviewed: false`; DEC-002 option 5 |
   | ADR-0007 | `spec/ADR-0007-dec-007-predicate-rendering.md` | accepted 2026-11-07, `reviewed: false`; DEC-007 option 2 |
   | SPEC-0001, SPEC-0002 v0.8.0, SPEC-0003 | `spec/SPEC-000{1,2,3}-*.md` | drafts; govern under `ADR-0003` |
   | DECISIONS-0001 v0.6.1 | `project/DECISIONS-0001.md` | the register |
   | MD-3 | `project/meetings/2026-09-28.md` | dated narrowing, closed by `ADR-0004` |
   | mofn report R-0006 v0.3.0 | `research/0006-mechanism/report.md` | draft; evidence, decides nothing |
   | CONTRIBUTING | `CONTRIBUTING.md` | process; §5 |

   **`docs/extraction.md` is stale on one point**: it says no DEC-002 ADR
   exists, and `ADR-0004` is that ADR. This file maps against `ADR-0004` and
   still records where the source cuts against option 5 (§6.3). `docs/` is not
   edited here.
2. **Quotation.** No word of PICS 1.1 is typed here. A quotation of it is a
   `<!-- q Lx-y -->` marker whose blockquote `bin/check-quotes --render` wrote
   from `.cache/pics-1-1-labels.txt`; optional anchors select a sub-span. A
   quotation of m-of-n is a `<!-- qm PATH Lx-y -->` marker: lines x to y of
   `PATH` in the `d7f7f89` snapshot, a leading blockquote margin dropped and
   whitespace collapsed, written and checked by the lane's `qm.py` and checked a
   second time by a fixed-string containment test (the brief's `grep -F`, on the
   whitespace-collapsed file). `bin/check-quotes` cannot see a `qm` marker.
   **DSig (`pics-dsig-1-0`) is cited by locator and line, never quoted here.**
   Names in backticks (`MIC-md5`, `for`) are identifiers, not quotations.
3. **Locators.** The source has no section numbers. A `§n` of the source is the
   renderer's structural ordinal and travels with its heading title or a line
   number, for example §13.1 (Signature Details) or §13.1 L414. `Lnnn` is a line
   of the `.txt` and is exact. A `§n` after another document's name
   (`SPEC-0002` §7.2) is that document's; a bare `§n` is a section of this
   file.
4. **Labels.** *(inferred)* marks what the source implies rather than states,
   and every consequence drawn here. **Ours** marks the library's proposal.
   **[outside this source]** marks a statement resting on a document the library
   does not hold for this record; it is never quoted and never the sole ground
   of a verdict.
5. **Numbering.** As in `pics-dsig-1-0`'s design notes: `R-M-NN`, `R-I-NN`,
   `R-O-NN` are `ARCH-0001` §5; `P1` to `P7`, `P5.1`, `P5.2` are `ARCH-0002`;
   `V1` to `V9` are `SPEC-0002` §9.2; *condition (n)* is mofn report R-0006
   §3.2's; row ids are `A-nn` adopt, `D-nn` adapt, `X-nn` reject, `C-nn`
   constrains, `K-nn` conflicts, `S-nn` silent; source defects are `SD-n` as `normative.md` numbers them. **No
   requirement id of this record is cited**: the requirements lane assigns them
   in this pass, and the verify pass joins quotations to ids.
6. **Levels.** The source's *must*, *should* and *may* are lowercase prose. A row
   reports them as printed and gives them no BCP 14 force.

---

## 1. Rows by verdict

30 rows: **8 adopt, 2 adapt, 7 reject, 7 constrains, 1 conflicts, 5 silent**.
*Adopt (confirms)* records the source as independent evidence for a decision we
already hold, not as a new commitment. **constrains**: one side narrows what the
other leaves open, so an implementation can satisfy both; **conflicts**: none
can.

| id | verdict | in PICS 1.1 | where | maps to | finding |
|---|---|---|---|---|---|
| A-01 | adopt (confirms) | The MIC hashes the document as delivered; email-style canonicalisation (MOSS) was declined as too complex | §13 (MICs and Digital Signatures) L398-400 | R-O-05's discipline, for content; `SPEC-0002` §5, §7.2 | the source rebuilds the label to verify it (X-01) and hashes the content as received: both sides of R-O-05 in one section |
| A-02 | adopt (confirms) | A label meant for exactly what was rated carries its digest, and a match all but proves the label belongs to the data | §13 L398; §14 (Glossary) L453 | R-M-07; `SPEC-0002` §7.2 | R-M-07 makes mandatory what PICS made optional (C-01) |
| A-03 | adopt (confirms) | A label carries values; the rating system that gives them meaning is published apart, under the service URL | §5 (General Format) L59; §7 (Detailed Syntax) L142 | `ARCH-0002` P3; `SPEC-0003` §1; `ADR-0007` | the separation P3 credits to PICS; the binding by URL is X-03 |
| A-04 | adopt (confirms) | An extension says whether it may be skipped; a mandatory one not understood means acting as though there were no label | §5 L103-105; §7 L175-176 | P5; `ARCH-0001` §3.4 (critical-bit row) | explicit opt-in skippability; our profile is stricter |
| A-05 | adopt (confirms) | The service signs its own labels with its private key, and a label has a lifetime | §13 L402-404; §5 L94-96 | `ARCH-0001` §4.2 (the PICS analogue); R-O-02 | `ARCH-0001`'s analogy fits PICS 1.1 exactly |
| A-06 | adopt (confirms `ARCH-0001` §3.3) | Labelling on a service's behalf, multi-party signing and key invalidation are named as needs, and declined | §13 L403, L406-407 | `ARCH-0001` §3.3 item 1; R-M-10; `ADR-0003` D5 | no principal or delegation model, in the source's own words |
| A-07 | adopt (confirms `SPEC-0002` §4.1) | Numbers are single-precision fractions, and implementers may keep them as ASCII strings | §7 L144 | `SPEC-0002` §4.1; mofn report R-0006 §3.4 | the source's own escape is the route an import takes (C-04) |
| A-08 | adopt (confirms) | Transmit-names and quoted strings are case-sensitive, and the wire format is US-ASCII | §7 L141-142; §14 L471 | `SPEC-0002` §4.1; condition (6) | DSig later folds transmit-name case (`pics-dsig-1-0` K-02) |
| D-01 | adapt | The MIC is computed after removing every embedded label and the whitespace after it | §13 L401 | R-M-07; `SPEC-0002` §7.2 | a digest inside what it hashes needs a removal rule; KSA never embeds a statement in its subject (open question 4) |
| D-02 | adapt | A document has many URLs; the one used to fetch it need not be the `for` URL | §5 L86 | R-M-11; `SPEC-0002` §7.2 | a locator rides as an attribute on a digest target, never as the target |
| X-01 | reject | A signature over a special form the client rebuilds from the label it received | §13 L404-405; §13.1 (Signature Details) L413-420 | R-O-05; `ADR-0003` (rejected: sign a re-encoded statement); `SPEC-0002` §5, §13.1; P5.1; condition (3) | §4: conflicts on every clause |
| X-02 | reject | The algorithm is named only by the option's name, which is never in what is signed; a new pair of algorithms is a new option | §13.1 L411, L414 | R-O-05; `SPEC-0002` §6.1, §6.2; condition (4) | the algorithm identifier is outside the signature |
| X-03 | reject | The special form has no service identifier: the signature does not cover which vocabulary the ratings are in | §13.1 L413-419; §8 (Semantics of PICS Labels and Label Lists) L224 | R-O-05; DEC-007 (`ADR-0007`); `SPEC-0003` §13.2; condition (4) | §3.3. DSig later signs the URL; KSA signs the hash |
| X-04 | reject (natively) | A label about a URL, or every URL under a prefix, stays valid while the content changes, and the source treats that as legitimate | §13 L392; §5 L73-74; §8 L226 | `SPEC-0002` §7.2, §13.10 | the reason KSA withdrew the locator target |
| X-05 | reject | An embedded or header label applies to the document it came with, whatever its `for` says | §10 (Embedding Labels in HyperText Markup Language (HTML)) L255; §11 (Using HTTP to Request Labels With A Document) L261 | R-M-11; `SPEC-0002` §7.2 | the delivery context is unsigned |
| X-06 | reject | Each service distributes its keys as it chooses, and no key is assumed ever to need invalidating | §13 L406 | `ADR-0003` D5; `SPEC-0002` §8.7, §8.8, §10; R-O-02 | — |
| X-07 | reject | A server may ignore the requested completeness, and an unknown value is read as *minimal* | §11.3 (Detailed Syntax of HTTP Requests for Labels With Document) L308-310 | P5; `SPEC-0002` §13.5 | a request for signed labels can be answered with unsigned ones and no error |
| C-01 | constrains | The MIC is optional and MD5 only, and signed labels commonly leave it out | §5 L79-81; §13.1 L414 | R-M-07; `SPEC-0002` §12.5; mofn report R-0006 §2.3 | no MIC is an accepted digest, and a signed label usually binds none |
| C-02 | constrains | A generic label names a URL prefix | §5 L73-74; §8 L226 | R-M-07; `SPEC-0002` §7.2, §13.10 | no target form satisfies both |
| C-03 | constrains | The MIC's hashed form is found by parsing the HTML | §13 L401 | condition (3), for content; `SPEC-0002` §13.6 | the verifier transforms untrusted input before hashing it *(inferred)* |
| C-04 | constrains | Ratings: fractions, multi-values and ranges | §7 L144-145, L197-198; §8 L227-232 | `SPEC-0002` §4.1, §7.4; `SPEC-0003` §6 | no base kind for a fraction; a multi-value is neither an assignment nor a scope |
| C-05 | constrains | Labels inherit service options, and transmitters abbreviate and compact | §6 (Example) L121-133; §7 L143 | `SPEC-0002` §4.5, §13.7 | §13.7 is the bounded version; R-O-05 forbids the rest |
| C-06 | constrains | Bureau responses match labels to URLs by position; `for` may be omitted (L379) and must be included (L386) | §12.3 (Response to Query for Labels Separate From Documents) L379, L386 | R-M-11; `SPEC-0002` §7.2 | a label without `for` is bound to its URL by its place in an unsigned list |
| C-07 | constrains | Dates to the minute, with an offset and `.` separators | §7 L179-196 | `SPEC-0002` §4.4 | an import converts to UTC seconds |
| K-01 | conflicts | No verifier can check the signature without rebuilding the special form from what it received | §13 L405; §13.1 L420 | R-O-05; P5.1, for an import verified by us | §4 |
| S-01 | silent | Labelling under a service's name by others, and co-signing, are left to commercial competition | §13 L403, L407 | R-M-10; `SPEC-0002` §8.6 | KSA's answer is delegation, not co-signature |
| S-02 | silent | The client chooses which services and bureaus to consult | §4 (Overview) L55; §12 (Requesting Labels Separately) L323-324 | `ADR-0003` D3, D4; mofn report R-0006 §2.3 | local trust, as in KSA |
| S-03 | silent | A label has no identity | none in the source | `SPEC-0002` §3, §8.7, §8.10 | nothing to revoke or review a label by |
| S-04 | silent | Delivery: the HTTP extension, the bureau query, Appendix A's bureau selection by DNS | §11 (Using HTTP to Request Labels With A Document) L259-320; §12 (Requesting Labels Separately) L321-386; §17 (Appendix A: An Algorithm for Locating a Label Bureau) L518-526 | R-I-01 | not modelled in this PR; §11 says what would need it |
| S-05 | silent | No domain separation: the service key signs the digest of a bare text string | §13 L404 | `SPEC-0002` §6.4, §13.2 | — |

---

## 2. Row details

### 2.1 Adopt

**A-01 — the content is hashed as delivered.** The source declines to
canonicalise the document:

<!-- q L399 "For use with electronic mail" .. "largely because of this complexity." -->
> For use with electronic mail, an elaborate technique is required to assure that the two message digests will match, since electronic mail gateways can modify the data before it is delivered (by wrapping lines, for example). We have chosen not to adopt MOSS directly for PICS, largely because of this complexity.

<!-- q L400 "Instead, we recommend the direct use of the MD5 algorithm" .. "conversion of the result to base64 encoding." -->
> Instead, we recommend the direct use of the MD5 algorithm on the source document and conversion of the result to base64 encoding.

Ours, the reason `SPEC-0002` carries the signed bytes:

<!-- qm spec/SPEC-0002-ksa-core.md L299-303 "Because otherwise a verifier" .. "(ARCH-0001 R-O-05)." -->
> Because otherwise a verifier would have to decode, remove the signature, and re-encode before it could check it — canonicalising during verification, exposing its decoder to unauthenticated input, and creating a second encoder whose output must match the producer's byte for byte. Carrying the signed bytes intact removes all three (ARCH-0001 R-O-05).

**Confirms the discipline, for content.** The same section that hashes the
document as received makes the client rebuild the label before checking its
signature (X-01). The authors applied R-O-05's reasoning to the object they
expected gateways to mangle and not to the one they wrote themselves
*(inferred)*. The exception, the removal of embedded labels, is D-01 and C-03.

**A-02 — a digest binds the label to the data.**

<!-- q L398 "If the label is intended to apply only to the data that was actually rated" .. "when the label is created." -->
> If the label is intended to apply only to the data that was actually rated, then a form of checksum (called a "message digest") can be applied to the data when the label is created.

<!-- q L453 "If they match, for all practical purposes" .. "has been retrieved." -->
> If they match, for all practical purposes, it is a proof that the label really belongs to the information that has been retrieved.

Ours:

<!-- qm spec/ARCH-0001-authorization-attestation.md L430 "Artifact statements SHALL bind" .. "content digest." -->
> Artifact statements SHALL bind at least one content digest.

`ARCH-0001` adds that a description digest satisfies R-M-07 and a locator
alone does not. **Confirms R-M-07's reason.** The source makes the digest a
choice, for a label meant only for the data that was rated; R-M-07 makes it a
requirement of every attestation (C-01).

**A-03 — values here, meaning elsewhere.**

<!-- q L59 "A label consists of a service identifier" .. "as its unique identifier." -->
> A label consists of a service identifier, label options, and a rating. The service identifier is the URL chosen by the rating service (see Rating Services and Rating Systems) as its unique identifier.

<!-- q L142 "The companion document" .. "other character sets." -->
> The companion document PICS Rating Services and Rating Systems describes how a client can map these transmit-names to descriptive strings using other character sets.

Ours, P3 and `SPEC-0003` §1:

<!-- qm spec/ARCH-0002-key-relative-naming.md L217-220 "**PICS is the early example.**" .. "is the generalisation." -->
> **PICS is the early example.** It published *rating systems* — categories, permitted values, scales, and the words a human reads — as machine-readable documents separate from the labels citing them. That separation is the idea, and bundling it into the type is the generalisation.

<!-- qm spec/SPEC-0003-ksa-definitions.md L81-89 "PICS (W3C, 1996)" .. "checked against the hash." -->
> PICS (W3C, 1996) published *rating systems* — categories, permitted values and the words a person reads — as documents separate from the labels that cited them, so that software meeting an unfamiliar vocabulary could fetch its description and render it correctly. That separation is the idea KSA keeps. Three things are added: 1. **Identity by hash.** A definition is identified by the SHA-256 of its canonical encoding, never by a URL. A locator is only a place to fetch it; what is fetched is checked against the hash.

**Confirms**; `SPEC-0003`'s first addition, identity by hash, is what X-03 shows
the source lacked.

**A-04 — skipping is declared, not assumed.**

<!-- q L105 "If the extension is optional" .. "as though no label had been supplied." -->
> If the extension is optional then software which does not understand the extension can simply ignore it; if the extension is mandatory then software which does not understand the extension should act as though no label had been supplied.

Ours, P5, and `ARCH-0001` §3.4's reading of the same split in OpenPGP:

<!-- qm spec/ARCH-0002-key-relative-naming.md L394-396 "Beyond the three:" .. "never the other way round." -->
> Beyond the three: **an unknown field in a signed payload is an error, not something to skip.** The default is must-understand; skippability is opt-in and explicit, never the other way round.

<!-- qm spec/ARCH-0001-authorization-attestation.md L308 "Our profile is" .. "not a field that old verifiers ignore." -->
> Our profile is **stricter**: every unknown field is rejected, so nothing is "non-critical". OpenPGP pays for its split: a verifier that ignores a non-critical field may not see a meaning the issuer intended. Under our profile a new field is a new definition (`ARCH-0003` W-12), not a field that old verifiers ignore.

**Confirms P5's shape, with our profile stricter.** PICS 1.1 has no default: the
grammar makes every extension say `optional` or `mandatory` (L175-176), which is
P5's explicit opt-in. Our importer rejects an extension it does not understand
even when it says `optional` (§5).

**A-05 — the service signs, and labels expire.**

<!-- q L404 "After creating a label" .. "to encrypt the digest." -->
> After creating a label, the service converts it to a special form specified below and computes the MD5 message digest of the label. It then uses the service's private key to encrypt the digest.

<!-- q L96 -->
> The date on which this rating expires.

Ours, `ARCH-0001` §4.2:

<!-- qm spec/ARCH-0001-authorization-attestation.md L384 "This is the PICS analogue" .. "is the definition (DEC-007)." -->
> This is the PICS analogue: issuer ≈ rating service; subjects ≈ labeled objects; predicate ≈ rating tuple; validity ≈ label lifetime; content binding is the artifact digest. The rating system, which v0.1 left out, is the definition (DEC-007).

**Confirms the analogy for PICS 1.1**: the issuer is the rating service, because
the service's key signs. Under DSig it is not (`pics-dsig-1-0` D-04). R-O-02's
preference for short validity has its precedent in `until`.

**A-06 — the gaps, in the source's words.**

<!-- q L403 "In order to sign a label" .. "on behalf of the service)" -->
> In order to sign a label, the rating service (or people authorized to generate labels on behalf of the service)

<!-- q L406 -->
> The problem of distributing these keys (and invalidating them in case the service's key is compromised) is an active area of commercial competition. Since there is no clearly established solution available today, PICS assumes that each service will distribute the public keys in some way it chooses. It also assumes that no keys will ever have to be invalidated. While this is clearly not a perfect solution, it seems to be the limit of what can be done today without committing to specific proprietary technology.

<!-- q L407 "If a rating service allows other people" .. "active commercial competition)." -->
> If a rating service allows other people to generate labels under its name (for example, a service that supports self-ratings by content producers) then the labels may need to be signed by both the service and the content producer. This can be done (each signs the label without the other's signature), but it becomes quite difficult to distribute the public keys needed to verify the signature. The PICS specification does not propose a solution to this problem (it, too, is part of active commercial competition).

Ours:

<!-- qm spec/ARCH-0001-authorization-attestation.md L292 "Historic gap:" .. "principal/delegation model." -->
> Historic gap: SPKI/SDSI never standardized a first-class **artifact statement** type; PICS did, without a strong principal/delegation model.

**Confirms `ARCH-0001` §3.3** from the primary source. What the source leaves
to commercial competition, KSA specifies: a service authorises a producer with a
`trust` statement carrying `may-delegate` (`SPEC-0002` §8.6), so a self-rating
needs one signature, the producer's, and a delegation the relying party can
reduce, not two signatures with two key-distribution problems. Key
invalidation is `revoke` and `rotate` (`SPEC-0002` §8.7, §8.8).

**A-07 — fractions, and the source's own escape.**

<!-- q L144 -->
> Numbers in PICS labels may be integers or fractions with no greater range or precision than that provided by IEEE single-precision floating point numbers. Implementors concerned about the vagaries of floating point comparisons may choose to represent numbers internally as ASCII strings.

Ours:

<!-- qm spec/SPEC-0002-ksa-core.md L202-204 "The following MUST NOT appear" .. "indefinite-length items." -->
> The following MUST NOT appear anywhere in a TBS or definition body: floating-point numbers, `null`, `undefined`, any other simple value, CBOR tags (major type 6), and indefinite-length items.

**Confirms the exclusion.** The special form asks for each value's shortest
spelling (L416) without saying whether that is the string's or the number's,
and a single-precision value has more than one decimal spelling *(inferred)*; the
source's suggestion, ASCII strings, removes the question, and it is what an
import would do (C-04).

**A-08 — byte-exact names, ASCII only.**

<!-- q L141 -->
> Transmit-names and quoted strings are case sensitive. Option names and other tokens in the BNF grammar are case insensitive.

<!-- q L142 "This specification is strictly about information carried over the wire" .. "requires the use of US-ASCII." -->
> This specification is strictly about information carried over the wire from the client to the server, and it requires the use of US-ASCII.

<!-- q L471 "URLs, while generally longer than desired" .. "case sensitive." -->
> URLs, while generally longer than desired, can be used as transmission names. Hence transmission names are case sensitive.

Ours:

<!-- qm spec/SPEC-0002-ksa-core.md L197 "valid UTF-8. Preserved byte-exact;" .. "by any producer or verifier" -->
> valid UTF-8. Preserved byte-exact; MUST NOT be normalised (no Unicode normalisation, no case folding, no whitespace trimming) by any producer or verifier

**Confirms.** US-ASCII leaves condition (6) nothing to normalise. DSig's
canonical form later lowercases every symbol, transmit-names included, which
this rule forbids (`pics-dsig-1-0` K-02, §8.1.2 L534).

### 2.2 Adapt

**D-01 — the digest sits inside what it hashes.**

<!-- q L401 -->
> Because PICS labels can be embedded inside of the documents they label, care must be taken to ensure that the message digest is computed excluding all PICS labels in the document. For HTML documents, this means that the digest must be computed after removing all META elements that include PICS labels (and any whitespace immediately following the end of each of these meta elements).

The removal is what lets a label carry a digest of the page that carries the
label. Ours: a KSA statement is never inside its subject; a digest target is
over the bytes a relying party holds (`SPEC-0002` §7.2). **Adapted, as a
condition on any future embedding:** if a KSA statement ever has to travel
inside the object it is about, the digest needs a removal rule that a verifier
can apply to bytes, without parsing untrusted markup; the source's rule needs
an HTML parse (C-03). Open question 4.

**D-02 — many URLs, one document.**

<!-- q L86 "Since a single document can have many URLs" .. "accompanies the document." -->
> Since a single document can have many URLs, the URL used to retrieve a document may differ from the URL in the for option of a label that accompanies the document.

Ours, R-M-11 and `SPEC-0002` §7.2:

<!-- qm spec/SPEC-0002-ksa-core.md L443-448 "**A locator is evidence, never a target.**" .. "defines (§7.4)." -->
> **A locator is evidence, never a target.** A URI, URN, ISBN, serial number or file path names a *place* or a *label*, not content: what it resolves to can change while the name stays the same. Where a statement needs to say where its subject can be found, it targets the subject by digest (type 2) or by description (type 6) and carries the locator as an attribute whose type a definition defines (§7.4).

**Adapted:** on import, `for` becomes a locator attribute, and the target, if
any, is the MIC's digest (C-01). Without a MIC there is no target (§5).

### 2.3 Reject

**X-01 — the client rebuilds what was signed.**

<!-- q L404 "the service converts it to a special form" .. "message digest of the label." -->
> the service converts it to a special form specified below and computes the MD5 message digest of the label.

<!-- q L405 "When the client receives a label" .. "originally signed." -->
> When the client receives a label and wants to verify the signature it takes the label it received and converts it back into the same special form in which it was originally signed.

The special form:

<!-- q L413-419 -->
> The special form of the label that is used for signatures is computed as follows: The service must decide which options it will include in the signed label when it is transmitted. Any options not transmitted with the signature cannot be used in the computation of the signature. We recommend that all options with known values be included with the exception of signature-rsa-md5. Any option may be omitted, but it will be common for the options mic-md5 (or md5) and full (or complete-label) to be omitted. The signature-rsa-md5 option is never included in the list of options. The selected options are sorted alphabetically by their shortest name (i.e. use full instead of complete-label). If a selected option has a default value and it is the same as the value to be used in the label, the option is omitted from this list. For each option in the list (in order), the short name is put into the label followed by a single space followed by the value of the option, followed by a space. The shortest form of a value is used, and strings are output in lower case if they are case insensitive. After all of the options has been output, output the characters "r (". Output the transmission names and their values, in alphabetical order by transmission name (using the US-ASCII character collating sequence for "alphabetical order"), separating the transmission name from the value by a single space. In outputting the value, no whitespace is permitted except for a single space used to separate items in a multi-value. Output a ")"

and the server's obligation that makes the rebuild possible:

<!-- q L420 -->
> When the client computes the special label format described above, it will use all options available to it: both those in the single-label and in the service-info. This implies a constraint on the server when it decides what options to include in the transmitted set. The transmitted set must include any options that the server ships as part of the service-info, unless either the value specified in the service-info or the value of the option for this label is the default value of the option.

Ours, `ADR-0003`'s rejected alternative and R-O-05:

<!-- qm spec/ADR-0003-ksa-core-decisions.md L62-63 "**Sign a re-encoded statement.**" .. "(R-O-05)." -->
> **Sign a re-encoded statement.** It makes the verifier canonicalise during verification and run its decoder on unauthenticated input (R-O-05).

<!-- qm spec/ARCH-0001-authorization-attestation.md L457 "The signed payload SHALL" .. "verified canonical bytes." -->
> The signed payload SHALL be the canonical encoding verbatim, carried with an authenticated type indicator. A verifier SHALL verify the signature before decoding and SHALL NOT canonicalize input as part of verification. Any human-facing form SHALL be regenerated from verified canonical bytes.

**Rejected natively, as `ADR-0003` did.** The verifier parses the received label
list, merges service and label options, drops defaults, sorts, shortens and
lowercases, and only then can hash and check. §4 scores it clause by clause; the
special form's own gaps are SD-16 and its item (a) (§9).

**X-02 — the algorithm outside the signature.**

<!-- q L411 -->
> PICS specifically requires the use of the RSA signature algorithm with the MD5 message digest. Should this system become outdated, the PICS specification can be easily updated to add a new label option that supports a different pair of algorithms.

<!-- q L414 "The signature-rsa-md5 option is" .. "list of options." -->
> The signature-rsa-md5 option is never included in the list of options.

The algorithm is identified by the option's name, and that option is excluded
from the special form; nothing signed names the algorithm *(inferred)*. One
option is one algorithm pair, so the identifier is not ambiguous today, but it
is not authenticated either. Ours:

<!-- qm spec/SPEC-0002-ksa-core.md L325 -->
> A statement's suite is inside its TBS and is therefore covered by its signature.

**Rejected.** The source's agility plan, a new option for a new pair, is a
registry by revision of the specification, as `SPEC-0002` §6.2 is; the
difference is that ours puts the code inside what is signed.

**X-03 — the vocabulary is not signed at all.** The service identifier is
required in every service section:

<!-- q L224 "The URL of each service must be specified" .. "(the serviceID)." -->
> The URL of each service must be specified (the serviceID).

and appears in none of the special form's six steps (L413-419, quoted under
X-01). So a PICS 1.1 signature covers the options and the ratings, and not the
name of the rating system in which `suds 0.5` means anything. §3.3 works out
the consequence. Ours, `SPEC-0003` §13.2, and the identity of a type:

<!-- qm spec/SPEC-0003-ksa-definitions.md L497-500 "Because statements cite definitions by hash" .. "after the fact." -->
> Because statements cite definitions by hash, an attacker cannot change what a value means after the fact.

<!-- qm spec/SPEC-0002-ksa-core.md L475-477 "A **type reference** names a type" .. "local to that definition." -->
> A **type reference** names a type by the hash of the definition that defines it and a label local to that definition.

**Rejected.** The progression across the two records is the argument in brief:
PICS 1.1 signs no vocabulary identifier; DSig signs the service URL
(`pics-dsig-1-0` §8.1.2 L535) and still not what it serves; KSA signs the
DefinitionId, which is the vocabulary's hash.

**X-04 — a label about a place.**

<!-- q L392 "While this can happen legitimately" .. "by an unauthorized party." -->
> While this can happen legitimately (as when Time-Warner updates the page containing the current issue of Time Magazine and believes that the label is still valid) it can also happen as a result of tampering with the document by an unauthorized party.

<!-- q L226 "A generic label implicitly rates every URL" .. "is a prefix." -->
> A generic label implicitly rates every URL for which the specified one is a prefix.

Ours:

<!-- qm spec/SPEC-0002-ksa-core.md L907-909 "A statement about a locator" .. "different days." -->
> A statement about a locator would be about whatever the locator resolves to when someone looks, so one signature could vouch for different content on different days.

**Rejected natively.** The source calls a label that outlives a page update
legitimate; KSA withdrew the locator target because one signature would then
vouch for different content on different days. A statement **about a name** is
still possible in KSA, as a description target, and `SPEC-0002` §13.10 warns
against the case a PICS label is (C-02).

**X-05 — the subject by delivery.**

<!-- q L255 "A specific (non-generic) label embedded in a document applies to that document" .. "to locate the document." -->
> A specific (non-generic) label embedded in a document applies to that document, regardless of what URL is used to locate the document.

<!-- q L261 "As with labels embedded in documents" .. "option of the label." -->
> As with labels embedded in documents, the client may assume that a label returned in the http header stream applies to the document requested, regardless of the URL specified in the "for" option of the label.

*(inferred)* A label with no MIC, delivered in a document or a header, is about
whatever it was delivered with. Anyone who can place it, by copying a `META`
element or a header, chooses its subject, and a signature over it is unaffected.
**Rejected:** a KSA target is inside the TBS. On import such a label has no
target (§5).

**X-06 — keys forever.** L406 (quoted under A-06) assumes no key will ever need
invalidating. **Rejected:** `ADR-0003` D5's issuer revocation, `SPEC-0002`
§8.7 and §8.8, and a key store that admits a key only from a verified
`key-publish` or an out-of-band import (`SPEC-0002` §10).

**X-07 — asking for signed labels guarantees nothing.**

<!-- q L310 "It is acceptable for a server to ignore the completeness" .. "as though minimal had been specified." -->
> It is acceptable for a server to ignore the completeness, either by delivering more or fewer options than requested. If the completeness is omitted, it should be treated as though minimal had been supplied. For future extensibility, any alphanumeric string may be used for a value of the completeness option. Servers which receive a value of completeness that they do not recognize must treat it as though minimal had been specified.

*(inferred)* A client that asks for `signed` and receives unsigned labels has no
error to see. Ours, the same principle for suites:

<!-- qm spec/SPEC-0002-ksa-core.md L878-880 "An unknown suite is unverifiable" .. "(ARCH-0002 P5)." -->
> An unknown suite is unverifiable, never silently accepted; an unknown kind or field is invalid. A verifier MUST NOT skip what it does not understand (ARCH-0002 P5).

**Rejected for any importer:** an unsigned answer to a signed request is no
answer. This is protocol behaviour, which this PR does not model (§11).

### 2.4 Constrains

**C-01 — a digest that is optional, MD5, and usually absent when signed.**

<!-- q L81 "A message integrity check (MIC) of the item being rated." .. "used to compute the MIC." -->
> A message integrity check (MIC) of the item being rated. The MD5 Message Digest Algorithm (see RFC1321) is used to compute the MIC.

<!-- q L414 "Any option may be omitted" .. "to be omitted." -->
> Any option may be omitted, but it will be common for the options mic-md5 (or md5) and full (or complete-label) to be omitted.

**Constrains import twice.** MD5 is not in `SPEC-0002` §12.5 (SHA-256, SHA-384,
SHA-512), and [outside this source] it is no longer collision-resistant, so no
PICS 1.1 MIC is an accepted R-M-07 digest; and the source expects signed labels
to omit the MIC, so a signed label usually binds no content at all. mofn report
R-0006 §2.3 asked any import to name the digest algorithms it accepts; for
PICS 1.1 that list cannot include the only algorithm the source offers.

**C-02 — a prefix is not a target.**

<!-- q L74 "A rating service may provide a generic label" .. "only one specific label for that URL." -->
> A rating service may provide a generic label for any or all prefixes of a given URL, but should provide only one specific label for that URL.

A generic label rates every URL with a given prefix, whatever those documents
are now or later (X-04). R-M-07 needs a digest, and `SPEC-0002` §13.10 asks
definers not to define a description type a reader would take for a statement
about the content at a locator:

<!-- qm spec/SPEC-0002-ksa-core.md L912-913 "A definer SHOULD NOT define a description type" .. "content at a locator." -->
> A definer SHOULD NOT define a description type that a reader would take for a statement about the content at a locator.

**Constrains import:** a generic label has no target that satisfies both. It is
dropped (§5).

**C-03 — hashing needs an HTML parse.** L401 (quoted under D-01) makes the
verifier find and remove every `META` element that includes a PICS label, and
the whitespace after it, before hashing. *(inferred)* That is a transformation
of untrusted input before any check, and its result depends on what a parser
takes a `META` element to be: one inside a comment, a malformed attribute, an
entity-escaped `content` (§10 L248-252). Two verifiers can compute two digests
of one document. Ours bounds work before V4 and never transforms a statement's
bytes:

<!-- qm spec/SPEC-0002-ksa-core.md L885-886 "It MUST bound the work" .. "before V4 succeeds." -->
> It MUST bound the work it performs on any input before V4 succeeds.

**Constrains:** condition (3)'s reasoning applies to the content digest too.
The whitespace rule is itself underdetermined (SD-24, §9).

**C-04 — ratings that KSA cannot spell as they are.**

<!-- q L145 -->
> The multi-value syntax must be used when there is more than one value for a particular category. This syntax may be used when there is exactly one value, but the more compact version may also be used in that case. When there is no value, the category may be omitted entirely or transmitted using the multi-value syntax.

<!-- q L232 "all subject values between 0.5 and 1.5" .. "as does the subject value 2." -->
> all subject values between 0.5 and 1.5 (including both endpoints) apply to the item, as does the subject value 2.

KSA's data model has no fraction (`SPEC-0002` §4.1, quoted under A-07), and
`SPEC-0003` §6's base kinds have none either: enum, integer, text, dns-name,
ip-prefix, digest, key, boolean, record, time, email. An attestation assigns a
value; a range is the scope of a trust statement, and `SPEC-0002` §7.4 keeps
them apart:

<!-- qm spec/SPEC-0002-ksa-core.md L484-485 "Supplying a range where an assignment is required" .. "is a type error." -->
> Supplying a range where an assignment is required, or the reverse, is a type error.

A PICS multi-value is a set of values and ranges asserted at once. **Constrains import:** values become enum texts or scaled
integers, as the source's ASCII-string suggestion already allows (A-07); a
multi-value becomes several attributes, or is dropped. Open question 3.

**C-05 — transmission compacts, inheritance factors.**

<!-- q L121 -->
> The same label list may be transmitted more compactly by converting all of the line breaks and subsequent indentation characters into a single space, and by replacing the word "labels" with "l", "ratings" with "r" and long option names with their abbreviations. It may be compressed for transmission purposes even further by removing all of the optional information to a separate document and referencing that document by a URL:

<!-- q L143 "An option that appears in the service-info" .. "applicable options." -->
> An option that appears in the service-info applies to all labels in that service-info unless overridden by an option in a specific label. That is, a label is effectively lexically nested within the enclosing service-info for the purpose of understanding the applicable options.

The special form is designed so that the compaction, the abbreviations and moving options into the service-info do not break a signature (L416, L420). Moving signed options out behind a `full` URL does: the verifier rebuilds from the options it received, and §11.3 (Detailed Syntax of HTTP Requests for Labels With Document) has a signed label carry its information directly (L309) [pass 2].
Ours allows one bounded case:

<!-- qm spec/SPEC-0002-ksa-core.md L890-892 "A transport that abbreviates identifiers" .. "simply fails V4." -->
> A transport that abbreviates identifiers (§4.5) MUST NOT be trusted to reconstruct them; the reconstructed TBS is verified in full, and an abbreviation that reconstructs to the wrong bytes simply fails V4.

**Constrains:** `SPEC-0002` §13.7 abbreviates identifiers only, and verifies the
rebuilt bytes in full. Anything more, R-O-05 forbids. §6.3 item 2 takes the
cost to ADR-0004.

**C-06 — bound by position.**

<!-- q L379 "Because order is preserved" .. "for which it requested a rating." -->
> Because order is preserved, it is acceptable (except where indicated below) to omit from the labels the "for" option which indicates the URL being rated. The client should match the label positionally with the URL for which it requested a rating.

<!-- q L386 "All labels produced in response to this query must include a for option." .. "for option." -->
> All labels produced in response to this query must include a for option.

The two sentences disagree, unless the query L386 speaks of is only the one
its `format=` paragraph describes (SD-12, §9). *(inferred)* A label without `for` is
bound to its URL by its place in an unsigned list; a signature over it covers no
URL, so reordering the list moves a signed rating from one URL to another.
**Constrains import:** a bureau-delivered label is imported only with `for` in
its signed set. Protocol behaviour; §11.

**C-07 — dates.** L179-196 fix one spelling: minutes, an offset, `.` separators.

<!-- q L192-196 -->
> Note: The ISO standard allows considerably greater flexibility than that described here. PICS requires precisely the syntax described here -- neither the time nor the time zone may be omitted, none of the alternate formats are permitted, and the punctuation must be as specified here.

`SPEC-0002` §4.4 counts seconds since 2026-01-01 in UTC with one encoding per
instant. **Constrains import:** convert the offset; the 1996-era dates are
negative times, which `SPEC-0002` §4.4 allows.

### 2.5 Conflicts

**K-01 — verification is a rebuild.** X-01 rejects the design for our
statements. K-01 is the conflict for an **import verified by us**: no PICS 1.1
signature can be checked without rebuilding the special form, so our verifier
would break R-O-05's clauses 3 and 4, and P5.1:

<!-- qm spec/ARCH-0002-key-relative-naming.md L412-415 "Where a profile declares a canonical encoding" .. "or repair it." -->
> Where a profile declares a canonical encoding, a decoder SHALL **reject** input that is not in that profile's canonical form. It SHALL NOT normalise it, re-encode it, or repair it.

**Conflicts.** It would be verified, if at all, outside the KSA verifier (§5).

### 2.6 Silent

**S-01 — delegation and co-signing.** L403 and L407 (quoted under A-06).
KSA's answer is delegation (`SPEC-0002` §8.6, `SPEC-0004` §6); the source has
none, and `ARCH-0001` §3.3 already says so.

**S-02 — the client chooses.**

<!-- q L323 "It is anticipated that there will be" .. "many rating services." -->
> It is anticipated that there will be "well-known" label bureaus which dispense (possibly for a fee) labels created by many rating services.

Ours: anchors per context, accepted locally (`ADR-0003` D3, D4). mofn report
R-0006 §2.3 reads PICS the same way: trust is placed outside the format.

**S-03 — no label identity.** Nothing names a label: there is no digest of a
label, no label id, and nothing to revoke or review it by. KSA's statement
digest is SHA-256 of the TBS (`SPEC-0002` §3, property 3).

**S-04 — delivery.** The HTTP extension (§11, L259-320), the bureau query (§12, L321-386) and
Appendix A's bureau selection, which rests on DNS:

<!-- q L523 "Our algorithm simply assumes that they exist and are equivalent" .. "in the usual manner." -->
> Our algorithm simply assumes that they exist and are equivalent, and that the network's Domain Name System (DNS) has records which map the single well-defined name for the label bureau to multiple Internet addresses, in the usual manner.

Not modelled in this PR (§11). *(inferred)* Appendix A selects among mirrors by
response time and trusts DNS for the set; a label's signature, where there is
one, is the only check on what a mirror serves.

**S-05 — no domain separation.** The service's RSA key signs the MD5 of a bare
text string (L404); nothing in it names the purpose. Ours: a DS label in every
signature input (`SPEC-0002` §6.4, §13.2).

---

## 3. What a PICS 1.1 label authenticates, and what it does not

### 3.1 The MIC

| | covered by the MIC? | where |
|---|---|---|
| the document's bytes, as delivered | yes | §13 L400 |
| the embedded PICS labels, and the whitespace after each | no: removed before hashing | §13 L401 |
| a transfer or character-set transformation on the way | not addressed: the source names only the document | §13 L400 |
| a non-HTML document carrying a label | no rule | — |
| who rated it | no: an unsigned label's MIC is anyone's claim | §13 L398 |

### 3.2 The signature

| part of a received label | covered by `signature-RSA-MD5`? | where |
|---|---|---|
| the transmitted options, service options merged in, defaults left out | yes | §13.1 L414-416, L420 |
| the ratings | yes | §13.1 L417-419 |
| the MIC | only if transmitted, and the source expects it usually is not | §13.1 L414 |
| the service identifier (which vocabulary) | **no** | §13.1 L413-419 |
| the format version (`PICS-1.1`) | no | §13.1 L413-419 |
| the algorithm | no: it is the option's name | §13.1 L411, L414 |
| the label's position in a bureau response, or its delivery channel | no | §12.3 L379; §10 L255; §11 L261 |
| what the ratings mean | no | §5 L59 |
| whether the key is still good | no: keys are assumed never to need invalidating | §13 L406 |

So a verified PICS 1.1 signature tells a client *(inferred)*: **some holder of
this service key signed these options and ratings, under some rating service
that key signs for, about the document that `for`, the MIC, the delivery
channel or the position in a list identifies — whichever of those the label
happens to have.** The source expects a key per service (L403, L406), so in
practice the key stands in for the service.

### 3.3 The missing service identifier, worked

*(inferred, from L224 and L413-419.)* Two service sections under one key — a
rating service that publishes two rating systems at two URLs, for instance
versions of one system — produce identical special forms for labels with equal
options and ratings. Moving a signed label from one section to the other leaves
its signature valid, and changes the vocabulary its transmit-names are read in.
The precondition is one key signing for both services; the source ties a key to
a service (L404, L406) and does not forbid one key for two. KSA's `type-ref` is
inside the TBS and names the definition by hash (X-03), so the move is
impossible by construction. DSig added the service URL to what is signed
(`pics-dsig-1-0` §8.1.2 L535), which closes the move between URLs and not a
change of what one URL serves.

---

## 4. R-O-05, clause by clause

`ARCH-0001` §5.3, since v0.2.0 (quoted under X-01).

| R-O-05 clause | PICS 1.1 signature | verdict |
|---|---|---|
| the signed payload is the canonical encoding verbatim | the special form is never transmitted, and is not itself a label (L413-419) | **conflicts** |
| carried with an authenticated type indicator | none: no version, no service, no algorithm in the special form (§3.2) | **conflicts** |
| verify before decoding | the client parses the label list and merges service options first (L405, L420) | **conflicts** |
| no canonicalising during verification | the rebuild is a canonicalisation: sort, shorten, lowercase, drop defaults (L415-416) | **conflicts** |
| any human-facing form regenerated from the verified bytes | the client shows the label it received; every transmitted option but the signature and any at its default value is in the special form, but the service identifier, which decides what the ratings mean, is not (X-03) | **conflicts** |

**Five of five.** The MIC, by contrast, keeps the discipline for the content and
breaks it only to remove the labels (A-01, C-03). Ours:

<!-- qm spec/ARCH-0002-key-relative-naming.md L440-443 "R-O-05 requires canonicalisation" .. "the separation is cosmetic." -->
> R-O-05 requires canonicalisation to run once, at authoring, on trusted input, and never as part of verification. **Rejection is what makes that separation real.** If a verifier may repair what it receives, the canonicaliser is back inside the verifier and the separation is cosmetic.

---

## 5. R-I-01: the PICS row's import profile, for a PICS 1.1 label (draft)

<!-- qm spec/ARCH-0001-authorization-attestation.md L441 "Publish a mapping table" .. "dropped, or inferred." -->
> Publish a mapping table for each supported foreign format: what is preserved, dropped, or inferred.

<!-- qm spec/ARCH-0001-authorization-attestation.md L500 "PICS label |" .. "import profile only if needed" -->
> PICS label | I | — | ArtifactStatement | Historic; import profile only if needed

Every row is *(inferred)*: the source defines no import. The route would be
`SPEC-0001` §5.3's external statement:

<!-- qm spec/SPEC-0001-ksa-architecture.md L229-232 "A wallet MAY import a signed object" .. "the same evaluation." -->
> A wallet MAY import a signed object from another protocol as an **external statement**, keeping its original bytes and mapping its speaker, subject and claims through an interchange profile (ARCH-0001 §6), so that it can be reasoned about by the same evaluation.

DSig's own rows (sigblock, resinfo) are in `pics-dsig-1-0`'s design notes, §5.

| PICS 1.1 construct | on import | |
|---|---|---|
| the service identifier | no DefinitionId. The importer mints a definition from a description it fetches, and becomes its definer; what the rater meant on the day is not recoverable (X-03) | **inferred** |
| ratings | attributes under that definition; fractions and multi-values have no base kind (C-04) | **lossy** |
| `by` | an attribute: a claimed creator, never the speaker (`ARCH-0002` P2) | **respelled** |
| `for` on a specific label | a locator attribute, never the target (D-02) | **respelled** |
| `generic` with `for` | no target (C-02) | **dropped** |
| `MIC-md5` | not an R-M-07 digest (C-01); an importer that fetches the document and binds it by SHA-256 makes that binding its own statement | **dropped**; **inferred** if re-bound |
| a label with no MIC | no target satisfying R-M-07 | **dropped** |
| `at` | an attribute at most: the document's modification date as the rater saw it | **inferred** |
| `on` | the date the rating was issued (L91). It becomes `valid.issued` only if the importer asserts that the signer signed then, which the source does not say | **inferred** |
| `until` / `exp` | `valid.not-on-or-after`, converted to UTC (C-07) | **preserved** |
| `comment` | nothing | **dropped** |
| `complete-label` / `full` | a locator; the label it fetches is a separate object | **dropped** |
| an extension | rejected unless the profile defines it, `optional` or not (A-04) | **dropped**, by rule |
| `signature-RSA-MD5` | no KSA suite: unverifiable natively (`SPEC-0002` §6.1, V2); verified, if at all, outside the KSA verifier; it covers no service, version or algorithm (§3.2) | **not carried natively** |
| the delivery channel, or a position in a bureau response | nothing (X-05, C-06) | **dropped** |
| `error` entries | nothing | **dropped** |

**Net.** Only a specific label that carries a MIC has anything to target, and
then only once the importer re-binds the document under an accepted digest; the
vocabulary is re-authored by the importer; the signature cannot be checked by a
KSA verifier. The row's *"import profile only if needed"* is right, and the row's
*Maps to native* cell (ArtifactStatement) holds for that one case only (open
question 2).

---

## 6. MD-3, ADR-0004 and DEC-002

MD-3 reads:

<!-- qm project/meetings/2026-09-28.md L51-53 "CBOR data model" .. "one-way mapping." -->
> CBOR data model, no IANA tags, COSE as export only; type identity is `(defining key, label)` per P1; YAML is the human form with a canonical one-way mapping.

`ADR-0004` accepted DEC-002 for option 5 on 2026-10-25, and:

<!-- qm spec/ADR-0004-dec-002-encoding.md L132 "MD-3's narrowing is closed by acceptance" .. "acceptance" -->
> MD-3's narrowing is closed by acceptance

Nothing here reopens it:

<!-- qm CONTRIBUTING.md L107-108 "Only an ADR" .. "decision." -->
> Only an ADR accepts a decision.

PICS 1.1 is a label format with a signature option, not a CBOR, COSE or envelope
document, so the mapping is of what is signed and hashed (§3), not header by
header. The section exists because an extraction that can only confirm is not
evidence.

### 6.1 What PICS 1.1 signs and hashes

The signature covers a text string the client builds: each transmitted option
as short name, space, value, space, sorted by short name, defaults dropped;
then `r (`; then the ratings sorted by transmit-name; then `)` (L413-419). The
MIC covers the document's bytes minus its embedded labels (L400-401). Neither is
carried: the client builds both. DSig's later canonical form is a different
algorithm for the same syntax (`pics-dsig-1-0` §6.1 compares the two).

### 6.2 Against the six conditions (mofn report R-0006 §3.2)

| condition | PICS 1.1 | how |
|---|---|---|
| (1) injective | **no, across services; unproven within one** | the special form omits the service (§3.3). L418 states no separator between rating pairs, and under the reading with none, `{0: 1, 2x: 5}` and `{0: 12, x: 5}` share one form (§8 check 1); with a space they do not |
| (2) the decoder rejects non-canonical input | **no** | labels are free-form on the wire (L109, L121, L140) and the client normalises |
| (3) canonicalise once, at authoring | **violated** for the signature (X-01); **kept** for the MIC except the label removal (A-01, C-03) | |
| (4) authenticated type indicator | **none** | no version, service or algorithm in the special form (§3.2) |
| (5) canonical order for sets | **partly** | options and ratings ordered; repeated `extension` and `comment` options (L146) and multi-value items not |
| (6) Unicode normalisation | **not applicable** | US-ASCII (L142); case folded only where the grammar is case-insensitive (L141, L416) |

### 6.3 Where PICS 1.1 cuts against option 5 and MD-3

1. **No floating point, against fractional ratings: weak, a cost of the
   profile.** `ADR-0004` item 1 excludes floating-point values, and
   `SPEC-0003` §6 has no fractional kind, so PICS-style ratings (`0.5`, ranges
   `0.5:1.5`) import as text or scaled integers (C-04). Options 2 and 3 would
   carry them as numbers, with the comparison and spelling hazards the source
   itself warns of (L144) and mofn report R-0006 §3.4 found in JCS; option 3 is
   withdrawn and option 2 rejected on P1. The source's own escape is strings,
   which is option 5's route. Not a reason to reopen.
2. **Compaction by intermediaries: a driver `ADR-0004` never scored.** PICS 1.1
   lets a transmitter abbreviate, compress whitespace, move options into a
   service section and push optional information behind a URL, and designs its
   signature to survive all of it but the last, which a signed label is not to
   use (L121, L143, L309, L420). A KSA signature survives
   none. **This names no DEC-002 option**: under R-O-05 every option pays it, and
   `SPEC-0002` §13.7 keeps the bounded case (C-05). Recorded as a cost R-O-05
   carries.
3. **Condition (5), against the profile as it stands.** The special form leaves
   repeated options and multi-value items unordered (6.2). `ADR-0004` left
   condition (5) owed, and at `d7f7f89` it still is (`ARCH-0001` §7, the
   *Still owed* paragraph; `pics-dsig-1-0` §6.3 quotes both). Against the
   profile, not the encoding.
4. **Legibility in text channels: weak, toward option 3, which is withdrawn.**
   A label is US-ASCII made to sit in an HTML `META` element and an RFC-822
   header (§9 (RFC-822 Headers) L236-240; §10, L244-255). `ADR-0004` scored *human debug* through `SPEC-0002` §11; this
   adds only the channel.

**What the special form does not show.** It is not evidence for option 1. It is
not a parseable label at all, it carries no lengths, and its weaknesses (no
service, an unstated separator, undefined defaults) are omissions of content,
which no grammar supplies *(inferred)*.

### 6.4 Where it favours option 5 and `SPEC-0002`

- **The MIC is R-O-05's discipline, found independently in 1996** (A-01), and
  its one exception, label removal, is the hazard (C-03).
- **An authenticated type indicator.** `SPEC-0002` puts `kind`, `suite` and every
  `type-ref` in the TBS (§7.1, §7.4) and a DS label in front (§6.4); the special
  form has none of the three (§3.2).
- **No numbers with two spellings.** KSA has integers only (§4.1); the special
  form's shortest-spelling rule is ambiguous for a single-precision number
  (A-07).
- **A closed option set.** PICS 1.1's options are a closed grammar, and new
  meaning goes in a declared extension (L161-178); `SPEC-0002` §7.1's closed
  maps and P5's rejection of the unknown are the same instinct, made strict.

### 6.5 DEC-005: detached and attached labels

<!-- qm spec/ARCH-0001-authorization-attestation.md L634 -->
> Options: DSSE (in-toto world), COSE_Sign1 (SCITT world), both with a single unsigned payload schema.

PICS 1.1 carries one label format three ways (§2 L26-29): in the document, with
it, and separately. Only the third is a detached statement in DEC-005's sense,
and all three bind the subject by context unless `for` or a MIC is present
(X-05, C-06). **Corroborates the attestation shape DEC-005's options wrap — a
statement apart from its subject, the subject named inside it — and is silent
between DSSE and COSE_Sign1**: PICS 1.1 has no envelope; its signature is an
option inside the label (§5 L92-93).

### 6.6 Net, stated as evidence

Nothing here shows a defect in option 5. Its findings go to the cost of R-O-05
under every option (6.3 item 2), to condition (5) (6.3 item 3), and to a
data-model cost of the profile for fractional values (6.3 item 1). Its weight
falls **outside DEC-002**: on R-O-05 (§4), on DEC-007 (X-03), on R-M-07 (A-02,
C-01, C-03), and on R-I-01's PICS row (§5).

---

## 7. mofn report R-0006: the PICS 1.1 cell, answered

R-0006's `unverified.md` asked:

<!-- qm research/0006-mechanism/unverified.md L40 "whether and how a PICS 1.1 label binds the content it labels" .. "(a hash option on the label?)" -->
> whether and how a PICS 1.1 label binds the content it labels (a hash option on the label?)

**Yes, by an option, and optionally.** `MIC-md5` (or `md5`) carries the base64
MD5 of the document, computed after removing every embedded label and the
whitespace after it (L79-81, L398-401). Without it, a label is bound to its
subject by `for` (a URL or, for a generic label, a prefix) or by where it was
delivered (X-05, C-06). The source expects signed labels to omit the MIC
(L414).

For R-0006 §2.2's columns (not edited here): **what is hashed** — the document,
by the MIC, optionally, and the special form, by the signature; **canonicalised,
and when** — the label, at signing and at verification; **what is signed** —
the MD5 of the special form, by RSA [the padding is outside this source; it
names RSAREF, L404]; **what the verifier does** — stated, unlike DSig's: rebuild
the special form, rehash, decrypt the signature with the service's public key,
compare (L405); **where trust is placed** — the client's choice of services,
and keys distributed by each service as it chooses (S-02, X-06).

---

## 8. Arithmetic and blanket claims, checked

| # | claim | how checked | result |
|---|---|---|---|
| 1 | under the reading of L418 with no separator between rating pairs, two rating sets share a special form | `pics_special.py`: names checked against the grammar (L199, L204-L207) and values against L200; sets sorted as L418 requires | `r (0 12x 5)` for both `{0: 1, 2x: 5}` and `{0: 12, x: 5}`; with a space, `r (0 1 2x 5)` and `r (0 12 x 5)` |
| 2 | the special form contains no service identifier | L413-419 read step by step | none of the six steps outputs it; the word *service* occurs in L414 as the signer and in L420 as `service-info` |
| 3 | no label option's default value is stated | `grep -i default` over the `.txt` | 8 occurrences on 5 lines (L73, L324, L386, L415, L420); none states the default of a label option |
| 4 | 30 rows in §1 | counted by script from the table | 8, 2, 7, 7, 1, 5 |
| 5 | the MIC hashes the document as delivered, the labels removed | L400 and L401 read together | the only transformation stated is the removal |

**Every *only*, *never*, *no* and *every* in this file's own prose was re-read**
against its row; each is scoped to the source as printed. That the source
expects signed labels to omit the MIC rests on L414's wording, which states an
expectation, not a rule.

---

## 9. Source defects met while mapping

Recorded, not repaired; each was re-read in the `.txt`, and SD-12 in the HTML. Each item carries the id `normative.md` gives the same defect [pass 2: this list first numbered itself SD-1 to SD-9, which named different defects than the same ids in `normative.md` and `requirements.yaml`; SD-24 was added to `normative.md` for the one it lacked].

- **SD-12. `for` may be omitted, and must be included.** L379 permits omitting
  `for`, with exceptions stated further on; the last item of the same list
  ends:

<!-- q L386 "Servers which receive a value of completeness" .. "must include a for option." -->
> Servers which receive a value of completeness that they do not recognize must treat it as though the default, full, had been specified. All labels produced in response to this query must include a for option.

  Read as covering every bureau query, it removes the permission; read as
  covering only queries that carry `format=`, the two coexist. The HTML puts the
  sentence inside the `format=` list item. The same sentence also ends the
  `opt=tree` and `opt=generic+tree` items (L383, L384), where it plainly covers
  those queries alone.
- **SD-16. The special form is underdetermined.** L418 states the separator between
  a transmit-name and its value, not between pairs (§8 check 1); L416 does not
  say whether a quoted value keeps its quotes, or what the shortest form of a
  quoted string or of an extension's data is.
- **SD-16 (a). Defaults that are never defined.** The special form drops an option
  equal to its default (L415), and L420 relies on defaults again, but no label
  option's default is stated (§8 check 3). DSig states one, `generic` false
  (`pics-dsig-1-0` §6.2 L153); PICS 1.1 does not.
- **SD-24. The whitespace removed with a label.** L401's rule for the whitespace
  after each removed element does not say which characters count, or whether a
  run ends at the first non-space.
- **SD-7. `by` cannot hold what it is offered for.**

<!-- q L84 "This may be human readable" .. "verify the signature on the label." -->
> This may be human readable, or it may be used to contain a (base-64 encoded) set of certificates and other information used to verify the signature on the label.

  `by` takes a quotedname (L163), whose characters (L203, L205-211) exclude
  `/`, which base64 uses [the alphabet is RFC 1521's, outside this source]. Only
  `%2F` escapes would carry it, and nothing says to undo them before decoding.
  DSig makes the same point about its own data (`pics-dsig-1-0` §7.4.2 L437).
- **SD-2. A message name the grammar lacks.**

<!-- q L382 "If no such generic label is available" .. "rather than sending back a specific label." -->
> If no such generic label is available, the server should include the "no-label" message rather than sending back a specific label.

  The grammar has `not-labeled` and `no-ratings` (L218, L152), no `no-label`.
- **SD-E (line 256). A prefix example that is not a prefix.**

<!-- q L256 "it may check further up the hierarchy" .. "or even at" -->
> it may check further up the hierarchy, in "http://www.greatdoc.com/foo/" or even at

  The page in question is under `www.greatdocs.com`; `greatdoc` drops the `s`,
  and ancestry is case-sensitive string matching (L380).
- **SD-13. Appendix B's queries put the separator inside the value.** Each `u=` and
  `s=` value but the last ends with `&` inside its quotes, and the first `u=`
  adds a `+` (L562-566, and the same in §18.2 to §18.4), where the grammar makes
  `&` a separator outside the value (L360-364).
- **SD-E (line 417). Text**, as printed:

<!-- q L417 "After all of the options has been output" .. "has been output" -->
> After all of the options has been output


---

## 10. Our documents: claims this source tests

Three passages say DSig *added* signatures to PICS (R-001 §6.1 L744-746,
R-0005 §5.4 L472-473, R-0006 §2.2 L231; `pics-dsig-1-0`'s design notes quote
them, in §10 and §7). This source shows PICS 1.1 had them in 1996:

<!-- q L93 "An RSA digital signature encompassing the label." .. "by the rating service that issued the label." -->
> An RSA digital signature encompassing the label. The signature is computed using the MD5 algorithm by the rating service that issued the label.

and the MIC as well (L79-81). DSig *replaced* both, about nineteen months later (573 days). R-001's
taxonomy row for PICS is consistent with this source on authority and on the
absence of delegation:

<!-- qm research/0001-signatures-and-attestation/report.md L1649 "**PICS** | a document (URL)" .. "client's chosen bureau" -->
> **PICS** | a document (URL) | **separately published, dereferenceable vocabulary** | any rating service; client chooses | n/a (no delegation) | client's chosen bureau

and incomplete on the subject: a document by URL, by URL prefix (a generic
label), or by digest (the MIC). `ARCH-0001` §3.1's PICS row matches the source:

<!-- qm spec/ARCH-0001-authorization-attestation.md L261 "Signed labels; checksum of content; client chooses services" .. "client chooses services" -->
> Signed labels; checksum of content; client chooses services

Recorded for their owners; m-of-n is not edited here.

---

## 11. Scope: the kinds this PR does not cover

The lead's scope gives `protocol` and `state-machine` as **not covered**
(`profile: partial`, `profile_reason` in `record.yaml`), not as not applicable:
the source defines an exchange and, in Appendix A, client state.
**This reading agrees, with one stated limit.** The design conclusions above do
not need a protocol model: our import binds a subject only by a signed digest,
so whatever the channel says is dropped (§5). But four rows rest on delivery
behaviour: X-05 (the subject of a header or embedded label), X-07 (the
completeness downgrade), C-06 (positional binding in bureau responses) and S-04
(bureau selection). **If R-I-01's PICS import is ever built for header- or
bureau-delivered labels, it needs this record's `protocol` kind, which this PR
does not cover** (open questions 6 and 8). L405 states a verification procedure,
an ordered local one, which is requirements and messages content, not a state
machine; label expiry is a validity rule. The one state the source defines is
Appendix A's bureau selection (primary, secondary, timer, threshold), part of
the uncovered protocol; S-04 is the only row that touches it, and it is silent.

## 12. Method

- **Our documents** were read only from the `d7f7f89` snapshot. Every m-of-n id
  this file cites was checked to occur there by a fixed-string search
  (`grep -rF`), by script over every id-shaped token in this file.
- **The source** is `.cache/pics-1-1-labels.txt`, with the HTML
  `.cache/pics-1-1-labels.bin` for SD-12, both sha256-checked against the brief and
  `record.yaml` in this pass. `bin/bcp14-count`: 0.
- **Quotations of the source** are `<!-- q -->` markers only, written by
  `bin/check-quotes --render --only` on this file and verified by
  `bin/check-quotes`.
- **Quotations of m-of-n** are `<!-- qm -->` markers, written and checked by
  `qm.py`, and re-checked by fixed-string containment in the
  whitespace-collapsed file.
- **Quotations of `pics-dsig-1-0`**: none. It is cited by locator.
- **Unmarked source text.** Every 8-word window of this file's prose
  (blockquotes, marker lines and backtick spans removed) was searched in
  both sources' `.txt`: 7647 windows examined; every hit is a heading title [pass 2 re-ran it with its own tokenizer after its edits to this file: 7155 windows, no run outside a heading title]
  quoted as a locator, as the locator rule requires.
- **Scripts** (lane scratch, not committed): `pics_special.py`, the special form
  of L413-419 from its text, with the pair separator as a parameter and the
  grammar of L199-207 as a check on the names.

## 13. What this file decides

Nothing. It records evidence and maps it. No requirement is added, amended or
withdrawn; no DEC-* is opened, ranked or accepted; `ADR-0004` and `ADR-0007` are
not reopened; the PICS row of `ARCH-0001` §6 keeps its priority.

## 14. Open questions

1. **Does R-I-01's PICS row ever need its profile?** §5 says what it would be:
   evidence, mostly dropped, the vocabulary re-authored by the importer, the
   signature unverifiable natively. Settle in the R-I-01 table for PICS, if one
   is ever written. Shared with `pics-dsig-1-0`'s open question 1.
2. **The row's *Maps to native* cell.** *ArtifactStatement* holds only for a
   specific label with a MIC, re-bound by the importer (§5). Most labels — generic,
   context-bound, MIC-less, or signed without a MIC as the source expects — have
   no target. Say so in the row when R-I-01 is written.
3. **Fractional and multi-valued ratings.** Does `SPEC-0003` need a decimal or
   rational base kind, or is enum-over-text the rule for imported scales (A-07,
   C-04)? And may an attestation carry several attributes of one type, which is
   how a multi-value would import? Settle in `SPEC-0003` if an import is built.
4. **Embedding a statement in its subject.** If a KSA statement ever has to
   travel inside the object it describes, the digest needs a removal rule a
   verifier can apply to bytes without parsing markup (D-01, C-03). Forbid
   embedding, as `SPEC-0002` does today by not providing it, or specify such a
   rule? Settle in `SPEC-0002` if a transport ever embeds.
5. **The missing service identifier.** Any import must record that a PICS 1.1
   signature does not authenticate the service (§3.3). State it in the R-I-01
   table for PICS.
6. **The completeness downgrade** (X-07). An importer that asks a bureau for
   signed labels must treat an unsigned answer as no answer. Protocol behaviour;
   settle with this record's `protocol` kind if a bureau import is built.
7. **Our documents' wording.** R-001 §6.1, R-0005 §5.4 and R-0006 §2.2 say DSig
   added signatures; R-001 §11.1's PICS subject cell omits the prefix and the
   digest (§10). Correct them when those reports are next revised; they are
   drafts and their owners decide.
8. **Positional binding** (C-06). If bureau-delivered labels are ever imported,
   require `for` in the signed set, and settle SD-12's two readings first. Protocol
   behaviour, as question 6.
9. **Condition (5).** Repeated extensions and multi-value items are unordered in
   the special form (6.2). `SPEC-0002` still owes the rule for its own sets;
   shared with `pics-dsig-1-0`'s open question 4. Settle in `SPEC-0002`.
10. **`bears_on`.** All six ids stand. Warranted additions, within the field's
    vocabulary: R-M-11 (D-02, X-04, X-05), R-M-10 (A-06, S-01), R-O-02 (A-05,
    X-06), DEC-005 (§6.5). P3 and P5, which this record presses, are outside it.
    `record.yaml` is not edited here.

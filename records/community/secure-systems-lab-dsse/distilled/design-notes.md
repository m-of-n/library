---
record: secure-systems-lab-dsse
kind: design-notes
title: "secure-systems-lab-dsse — bearing on our design"
extracted: "2026-11-22"
reviewed_by: ""
---

# DSSE — bearing on our design

The source is the DSSE specification at commit `1d3370f` (record.yaml:14,
:46): `protocol.md`, `envelope.md`, `envelope.proto`, `background.md` and the
attack notebook, rendered by `distilled/render-source.py` to
`.cache/secure-systems-lab-dsse.txt` (1145 lines, sha256
`b5fe6fb26be4eb9f3ac26391e376e0d677fbb041ede59397a8dabc1734913247`, equal to
`requirements.yaml`'s `source_digest`). The archive's sha256
`88fc65fd66d7250445dc08a65a2cb68c942fb88517152246f859a70d6dac3ac1` equals
`content.sha256` (record.yaml:15) and was recomputed from
`.cache/secure-systems-lab-dsse.tar.gz` in this pass; retrieved 2026-10-03
(record.yaml:16). `Lnnn` is a line of the rendering; *§1.2* is a section of the
source as the rendering numbers it (§1 `protocol.md`, §2 `envelope.md`, §3
`envelope.proto`, §4 `background.md`, §5 the notebook). The text names its own
version:

<!-- q L6-8 -->
> May 10, 2024 Version 1.0.2

**Which DSSE this is.** By the GitHub API (tags, compare and contents
endpoints, read again 2026-11-22; the responses are kept outside the
repository), tag `v1.0.2` is commit `4409013` (2024-05-28), and `1d3370f` is 21
commits after it and none behind. At the tag, `protocol.md`, `envelope.md`,
`envelope.proto` and the notebook hash to exactly the four sha256 values
`render-source.py` pins; `background.md` differs, in three link targets only.
So the normative text we hold **is** v1.0.2. The three earlier tags are not.
`v0.1.0` (`55b006c`, 2021-03-05) predates the five files: its text is one
`specification.md`. `v1.0.0` (`cacf247`, 2021-06-21) has no §1.3, and its `envelope.proto` comment
describes a different, little-endian length-prefixed PAE; `v1.0.1` (`fba27e4`,
2024-05-13) adds §1.3 and today's proto comment. `v1.0.0` and `v1.0.1` both lack the
bytes-identity rule, R-0008 and R-0009, and all of
§2.3 (R-0097, R-0016,
R-0017), which v1.0.2 added. That matters for anyone who reads
in-toto's label *DSSE v1.0* rather than its link (Part 6, CC-01).

It reaches us in seven ways (record.yaml:28-36 lists the `bears_on`):

1. **T-051 / `MAP-0002`** (BACKLOG-0001:188), the in-toto Statement ↔
   `ArtifactStatement` mapping, which must pin the exact signed bytes
   (library#152): those are DSSE's PAE. Part 1.
2. **R-O-05** (ARCH-0001:467). PLAN-0001:378-382 proposed it to keep the
   project clear of DSSE's canonicalisation critique; background §4.4 is the
   argument it must survive. Part 3.
3. **DEC-002**, accepted for option 5 by ADR-0004 (ADR-0004:36-56), whose item
   4 makes COSE_Sign1 and DSSE export envelopes only (:51-52). Option 3 had
   named DSSE as the signed form (ARCH-0001:539). Part 2 maps MD-3 field by
   field and says where DSSE cuts against it.
4. **DEC-005**, open (ARCH-0001:71-73, :643-645; DECISIONS-0001:308), and
   **R-I-03** (ARCH-0001:453). Part 4.
5. **R-M-06** (ARCH-0001:439) through §1.3's `(t, n)`-ENVELOPE. Part 4.
6. **R-M-02 and DEC-003** (ARCH-0001:435, :594-596) through `KEYID`, and
   **R-M-12 / P1** (ARCH-0001:445; ARCH-0002:65-87) through `PAYLOAD_TYPE`;
   with `Sign()`, the algorithm questions of Part 5.
7. **P5 and P5.2** (ARCH-0002:381-403, :485-537), which mofn reasoned from this
   source (DL-0013 review:85-92). Not in `bears_on`; record.yaml is not this
   lane's to edit (Q-16).

Part 6 cross-checks the in-toto envelope extraction, which profiles this source.

## Things to hold while reading

1. **Our decisions are read from m-of-n at `656bac0`**
   (`656bac0668d771e221fcbf02ff556cbcc6622b29`, origin/main head, committed
   2026-11-17) with `git -C ~/Projects/mofn show 656bac0:<path>`, never the
   working tree. `DOC:n` or `DOC:n-m` is a line range of that blob and a bare
   `:n` continues the document just named. The documents and their standing:

   | name | path | standing at `656bac0` |
   |---|---|---|
   | ARCH-0001 v0.3.2 | `spec/ARCH-0001-authorization-attestation.md` | draft. DEC-002 accepted (:533), DEC-003 accepted (:596), **DEC-005 open** (:71-73, :643-645) |
   | ARCH-0002 v0.10.0 | `spec/ARCH-0002-key-relative-naming.md` | P1, P2, P5 with P5.1 and P5.2 accepted; P1.1 draft |
   | ADR-0002 1.0.0 | `spec/ADR-0002-provisional-principles.md` | accepted 2026-11-06; owes the R-I-01 DSSE row (:180) |
   | ADR-0003 1.0.1 | `spec/ADR-0003-ksa-core-decisions.md` | accepted; D1 type identity, D2 one canonical encoding |
   | ADR-0004 1.0.0 | `spec/ADR-0004-dec-002-encoding.md` | **accepted 2026-10-25, `reviewed: false`** (:20, :29-32): DEC-002 is option 5 |
   | ADR-0005 1.0.0 | `spec/ADR-0005-dec-003-key-identifier.md` | accepted 2026-10-25, `reviewed: false`: `kid` = SHA-256 of the suite's key encoding |
   | SPEC-0001 0.1.0, SPEC-0002 0.10.1, SPEC-0004 0.6.2 | `spec/SPEC-000{1,2,4}-*.md` | draft; govern where an ARCH document differs (ADR-0003) |
   | MD-3 | `project/meetings/2026-09-28.md:51-54` | the 2026-09-28 narrowing, closed by ADR-0004's acceptance (ADR-0004:132-133) |
   | DECISIONS-0001 0.8.0, BACKLOG-0001 0.16.0, PLAN-0001 0.7.1 | `project/…` | register, backlog, plan |
   | DL-0006, DL-0013 | `design-log/0006-canonical-encoding-close/review.md` and its `produced.md`; `design-log/0013-p5-serialisation-clause/review.md` (two directories are numbered 0013 at `656bac0`; `0013-publish-research-reports` is not cited) | where mofn recorded its earlier reading of DSSE |
   | mofn report R-0006 v0.3.0, mofn report R-0005 v0.1.1, mofn survey R-0001 v0.2.0 | `research/0006-mechanism/report.md`, `research/0005-context/report.md`, `research/0001-signatures-and-attestation/report.md` | draft, evidence only |
   | decode spike | `prototype/statements/DECODE-FINDINGS.md` | decides nothing (:3-5); its falsifier names DSSE (:13-17) |
   | lane-a | `prototype/lane-a/` | a throwaway that decides nothing (lane-a/README.md:3); mofn's only DSSE code |

   **`docs/extraction.md` is stale on one point**: it says no DEC-002 ADR
   exists (docs/extraction.md:128-131). At `656bac0` ADR-0004 accepts DEC-002
   for option 5; the in-toto-envelope-v1 extraction found the same at
   `7c3c731`. This file maps against ADR-0004 and still records where the
   source cuts against option 5 and MD-3, which is what docs/extraction.md:133-135
   asks for, and its findings go to ADR-0004's owed second reader (ADR-0004:29-32)
   rather than to an ADR not yet written. DECISIONS-0001's own front matter still
   says DEC-002 is open (DECISIONS-0001:47-51) while its table says decided (:77).

2. **Ids.** A bare `R-NNNN` is this record's, `secure-systems-lab-dsse#R-NNNN`:
   R-0001 to R-0033 are the skeleton's BCP 14 sentences, R-0034 to R-0103 pass
   1's keyword-less additions (promoted candidates, hunted text and split
   children), R-0104 to R-0110 inferred, in the requirements lane's words. A
   candidate id `C-NNNN` from `inferred-candidates.yaml` is cited only where the
   candidate was rejected (rationale, motivation, the notebook); a promoted one
   is always cited by its R-id. Lines with no id (the vector L149, L155, L161,
   its key L167-171 and envelope L177-179) are cited by line. Every id cited here was
   emitted by script from a line-range selector and its resolved text read
   (Method); the six range bounds above describe the layout and cite nothing. `SD-n` is a defect in normative.md's canonical list (SD-1 to
   SD-20); `DN-SD-n` is a candidate this file offered for that list (Part 7):
   DN-SD-1 is SD-18, and DN-SD-2 was taken in by pass 2 as SD-19.
   Row ids: `A` adopt, `D` adapt, `X` reject, `C` constrains, `K` conflicts,
   `S` silent; `CC-nn` the cross-check findings of Part 6; `Q-nn` open
   questions. **The in-toto record's ids are never written bare**, because its
   R-, SD- and Q-numbers collide with ours: its requirements are cited by its
   source line, *in-toto L14*, resolved by script to a requirement carrying that
   line, except two lines cited as lines: one carrying two requirements and a
   link definition carrying none (Method); its rows, defects and questions as *in-toto D-03*,
   *in-toto SD-12*, *in-toto Q-09*; its files by name and line on
   `origin/fx1-in-toto-envelope-136` at `23c0d40` (*in-toto
   design-notes.md:141*).

3. **Quotation.** No word of the source is typed here. A quotation of DSSE is a
   `<!-- q Lx-y -->` marker whose blockquote `bin/check-quotes --render`
   wrote, whitespace-collapsed. A quotation of mofn, of the in-toto record or of
   this record's pre-FX-1 notes (*old design-notes.md*, at `212d336`, Part 7.1) is *foreign*: short, in double quotes, cited by
   line, and checked by script against that document alone (Method).

4. **Two export products.** Following in-toto K-01 (*in-toto
   design-notes.md:442-460*), **E1** is a DSSE envelope whose payload is the KSA
   TBS under a `payloadType` of our own; **E2** is an in-toto Statement in DSSE,
   which R-I-03 names. *(inferred)* marks a consequence the source does not
   state. Nothing here is a proposal unless it says so; the last part says what
   this file decides, which is nothing.

---

## Rows by verdict

**40 rows: 10 adopt, 5 adapt, 4 reject, 10 constrains, 3 conflicts, 8 silent** (counted by script from the table below).
*Adopt (confirms)* means DSSE does what an accepted decision of ours already
does: evidence, not a new commitment. *Reject (native)* means the native model
declines the mechanism; nothing stops it at the boundary. *Adapt (option)*
names a path DSSE opens that no decision of ours has taken.

| id | verdict | in the source | where | ids | maps to | finding |
|---|---|---|---|---|---|---|
| A-01 | adopt (confirms) | PAE authenticates the type together with the body; `KEYID` is outside it | L19; L24-28; L60-68 | R-0035, R-0036, R-0044, R-0045, R-0020 | R-O-05 (ARCH-0001:467); condition (4) (DECISIONS-0001:109-111); SPEC-0002 §6.4 (:395-407) | the authenticated type indicator R-O-05 asks for. DSSE transmits it and lets the application choose it; KSA fixes it per object class in a DS label that is never sent, with `kind` inside the TBS |
| A-02 | adopt (confirms) | sign the serialised bytes, send them as signed, verify before parsing, depend on no canonicalisation | L87-89; L100-104; L368; L370; L403-404 | R-0056, R-0057, R-0063, R-0066, R-0026, R-0028, R-0101 | R-O-05 clauses 1-2; PLAN-0001:378-382; SPEC-0002 §3 (:203-210), §5 (:312-328), V4-V5 (:696-697) | KSA's signature path is DSSE's here, and R-0101 is the sentence R-O-05 restates. DSSE prefers the order and never makes it binding (C-07) |
| A-03 | adopt (confirms) | verified bytes and delivered bytes are one; no second parse of the envelope | L109-113; L273-277 | R-0008, R-0009, R-0016, R-0017 | R-O-05 clause 3, by extension; SPEC-0002 §5 (:312-321), V5 (:697), V9 (:701) | met natively: V5 decodes the very `tbs` V4 verified. Owed by every importer (MAP-0002). The rule names the body only (S-08). New in v1.0.2 |
| A-04 | adopt (confirms) | an unsupported type is rejected, after the signature check | L102; L137 | R-0065, R-0080 | P5 (ARCH-0002:381-403); P5.2 (:500); SPEC-0002 V2 (:694), §13.5 (:918-922) | DSSE is reject-unknown for types, as P5.2 records. KSA checks its suite before the signature and DSSE its type after; both reject |
| A-05 | adopt | the type is opaque and case-sensitive, names encoding and schema, and SHOULD be application-specific, never generic | L32-34; L40-44 | R-0038, R-0039, R-0002, C-0010 | P3 (ARCH-0002:199); condition (1) over the pair, not the bytes (Part 3.3) | E1's type names the KSA statement schema, never a generic CBOR type; that is what keeps A-09's polyglot shut at the boundary. Comparison is byte for byte |
| A-06 | adopt (confirms) | `KEYID` is optional, unauthenticated, and never a security input; it only narrows the keys tried | L28; L52-56; L99; L314-316 | R-0036, R-0042, R-0006, R-0062, R-0022 | P5.2 (ARCH-0002:525-530); P1.1 (:117-119); R-M-02 (ARCH-0001:435); ADR-0005 (:36-38); SPEC-0002 §5 (:308), V6 (:698) | the pre-FX-1 notes' finding 4, now mofn's rule: the principal travels in the payload. KSA's envelope `says` is a hint too, but V6 checks it; nothing checks a `keyid` |
| A-07 | adopt (confirms) | the signature is over raw bytes; base64 is there only because JSON has no bytes | L429-438; L556 | C-0081, C-0083, C-0084, C-0087, C-0124 | SPEC-0002 §5 (:302, :309); T-051 (BACKLOG-0001:188) | KSA's CBOR envelope carries `tbs` as a byte string with no base64, as DSSE says a bytes-capable format should. MAP-0002 pins decoded bytes, never base64 text |
| A-08 | adopt (confirms) | detached signing by digest: the payload names outside bytes by their hash | L374-376 | R-0029, R-0100 | R-M-07 (ARCH-0001:440); SPEC-0002 §7.2 target 2 (:454) | an attestation about a digest target is DSSE's detached pattern. DSSE never omits the payload (CC-06) |
| A-09 | adopt (confirms) | the notebook's attack needs an unauthenticated type **and** a victim decoder that skips unknown fields | L519; L554; L592-595; L1072-1073; L1097 | C-0122, C-0133, C-0148, C-0151 | R-O-05; P5 (ARCH-0002:394-402); condition (4) | evidence for two rules, not one: authenticate the type, and never skip the unknown. Either alone stops this exploit (Part 3.4) |
| A-10 | adopt (confirms) | two different payloads may share one canonical encoding, and canonicalisation schemes have been broken | L393-398 | C-0073, C-0074, C-0075 | condition (1), which R-O-05 assumes rather than delivers (DECISIONS-0001:109-111); ADR-0004 scoring (:72); SPEC-0002 §4.1-§4.3 (:216-266), §11.1 (:727-748) | the condition stated as an attack. KSA never canonicalises during verification, its encoding gives one value one byte string, and the human form converts one-to-one. Over the (type, bytes) pair it needs the DS label (Part 3.3) |
| D-01 | adapt | either base64 alphabet; a verifier takes both; padding unstated | L106-107; L223-225 | R-0068, R-0007, R-0089, R-0090 | P5.1 (ARCH-0002:405-414); P5.2 (:502-510); SPEC-0001 §6.2 (:257); R-I-01 (ARCH-0001:451) | import accepts both alphabets, so P5.1 has no canonical exterior to enforce; export emits one spelling. lane-a's verifier would fail this MUST (Part 1.3) |
| D-02 | adapt | a multi-signature envelope counts as so many one-signature envelopes | L229-230 | R-0010, R-0092 | SPEC-0001 §5.3 (:229-232); SPEC-0004 §6.4 (:423-431); R-I-02 (ARCH-0001:452) | import: each verified signature becomes one external statement, the shape SPEC-0004 §6.4 counts. §1.3 strains the equivalence for `t` ≥ 2 (SD-18, Part 4.4) |
| D-03 | adapt | the type SHOULD be a media type or URI; another encoding may omit it or code it shorter | L34-50; L257-263 | R-0001, R-0002, R-0003, R-0004, R-0005, R-0096, R-0110 | P1 (ARCH-0002:65-87); ADR-0003 D1 (:47); ADR-0004 item 3 (:46-50); R-M-12 (ARCH-0001:445) | natively never; at the boundary one string, chosen once and inside every E1 signature. L262-263 compresses how the type is sent, not what is signed: the pre-FX-1 finding 2 half withdrawn (Part 2.4) |
| D-04 | adapt | `Sign()` is arbitrary and agreed out of band; no algorithm field exists; `KEYID` only hints at one | L52-53; L71-73; L366-367 | R-0042, R-0051, R-0052, R-0053, R-0025 | SPEC-0002 §6.1 (:350), §6.2 (:354-365); SPEC-0001 §5.1 (:204) | MAP-0002 states `Sign()` per suite: algorithm, input (PAE, no DS label), ML-DSA context, signature encoding. E1 keeps the signed `suite` in the payload; E2 drops it unless the Statement carries it (Part 5) |
| D-05 | adapt (option) | another data structure may carry the signed message, in CBOR or protobuf, with a default or coded type, provided the signature stays valid | L257-263 | R-0093, R-0094, R-0095, R-0096, R-0110 | ADR-0004 item 4 (:51-52); SPEC-0002 §5 (:298-321), §6.3-§6.4 (:367-407); DEC-005 (ARCH-0001:643-645) | the KSA envelope would be a DSSE structure of this kind if its signing input were PAE over the TBS: every native signature would then verify as a DSSE one, and E1 would need no new signature. No decision of ours takes it (Part 2.5, Q-03) |
| X-01 | reject (native; import deviation) | unknown fields: producers and later versions may add them, consumers skip them | L252-253 | R-0014, R-0015 | P5 (ARCH-0002:394-402); P5.2 (:485-537); ADR-0002:180 | the pre-FX-1 finding 3, now P5.2: import rejects unknown exterior fields, export emits none. Unknown members *inside* a `signatures` element fall under R-0015 and are named by nothing of ours (Q-05) |
| X-02 | reject (native) | more than one signature per envelope | L229-230; L377 | R-0030, R-0010 | P2 (ARCH-0002:132-148); SPEC-0002 §5 (:302, :310) | one speaker and one `sig` per KSA statement; a co-signature has no native form. Nothing is lost at the boundary, where DSSE supplies it |
| X-03 | reject (native) | no canonical form anywhere | L398; L368 | C-0075, R-0026 | ADR-0003 D1-D2 (:47-48); ADR-0004 (:36-45); SPEC-0002 §3 (:209-210), §4.5 (:284-294) | KSA canonicalises once, at authoring, for identity; DSSE derives no identifier from content. Its strong form lies outside DEC-002's options (Part 2.4, Part 3.5) |
| X-04 | reject (native) | the algorithm is fixed by the key, out of band; nothing signed names it | L52-53; L71-73; L366-367 | R-0042, R-0043, R-0053, R-0025 | SPEC-0002 §6.1 (:350), V2 (:694); SPEC-0001 §5.1 (:204); mofn survey R-0001 §10.4 (:1597-1608) | KSA signs the suite inside the TBS and binds each key to one suite. DSSE avoids algorithm confusion only where the verifier takes the algorithm with the key, which it never says (SD-13); the survey's charge holds for that gap and for thresholds, not for the silence as such (Part 5.4) |
| C-01 | constrains | what is signed is PAE(UTF8(type), body) | L19; L64-68; L75-76; L161 | R-0035, R-0045, R-0054, R-0020 | T-051 / MAP-0002 (BACKLOG-0001:188); R-I-03 (ARCH-0001:453) | MAP-0002 pins the type's UTF-8 bytes exactly, the decoded body, decimal byte lengths and nothing after the body (Part 1) |
| C-02 | constrains | `KEYID`, the JSON object, member order, whitespace and the base64 spelling are outside the signature | L24-28; L64; L106-107 | R-0036, R-0046, R-0007, R-0105 | R-I-01 (ARCH-0001:451); SPEC-0001 §6.2 (:257); SPEC-0002 §4.5 (:288-290) | one signed message has many envelope byte strings; an export's or an import's identity is over (type, body), never the envelope text |
| C-03 | constrains | the signer is not in the signed bytes | L24-28; L64 | R-0036, R-0046 | R-O-01 (ARCH-0001:463); P2 (ARCH-0002:146-148); SPEC-0002 §13.4 (:912-916), V6 (:698); P5.2 (ARCH-0002:525-530) | E1 keeps `says` inside the TBS. In E2 the speaker is whichever key verifies, unless the Statement carries it (Part 2.2, Q-08) |
| C-04 | constrains | the envelope carries no public key | L207-219; L250 | R-0087, R-0088, R-0012 | SPEC-0002 §5 (:311, :314-317), V3 (:695) | `pub` has no DSSE home and P5.2 forbids adding one, so the bootstrap kinds lose verify-before-decode under DSSE (Q-07) |
| C-05 | constrains | the threshold is the application's: neither `t` nor `n` is in the envelope | L121-123; L125-139 | R-0070, R-0077, R-0079 | R-M-06 (ARCH-0001:439); ARCH-0001 §4.1 (:346); SPEC-0002 §8.6 (:606-609) | the pre-FX-1 finding 1, amended: the envelope carries neither; `k` and the members travel in the payload (Part 4.3) |
| C-06 | constrains | JSON is the one recommended encoding and no other is standardised | L204-205; L207-208; L265 | R-0085, R-0086, R-0087, C-0057 | MD-3 (meetings/2026-09-28.md:51-54); ADR-0004 items 1 and 4 (:38-42, :51-52); ARCH-0001 §3.2 (:290) | every DSSE export leaves KSA-CBOR at the envelope for JSON and base64, with a PAE beside them: a cost option 5 pays and option 3, whose signed form DSSE was, does not (Part 2.5) |
| C-07 | constrains | the steps are listed verify-then-parse, but no sentence makes the order binding on a verifier | L96-104; L370; L403-404 | R-0060, R-0063, R-0066, R-0028, R-0101, R-0107 | R-O-05 clause 2 (ARCH-0001:467); SPEC-0002 §9.2 (:688-689) | R-O-05 and V1-V9 make the order a SHALL; DSSE makes it a preference and a design SHOULD NOT. A parse-first DSSE verifier conforms, so our importer imposes the order; lane-a sample 3 parses first (Part 3.1) |
| C-08 | constrains | the payload is any bytes under any type the parties agree | L30; L82-83; L365 | R-0037, R-0055, R-0024 | DEC-005 (ARCH-0001:643-645); R-I-03 (:453) | DSSE carries E1 as readily as E2. DEC-005's single unsigned payload schema is met by E1 alone, while R-I-03's DSSE branch names E2, an in-toto Statement (Part 4.1) |
| C-09 | constrains | parallel signatures over one payload verify independently, and any of them can be dropped | L117-119; L229-230; L131-136 | R-0069, R-0092, R-0076, R-0105 | SPEC-0001 §5.2 (:214-217), §11 (:415-421); SPEC-0002 §6.5 (:409-422); SPEC-0004 §6.4 (:431) | a classical and a post-quantum signature can ride together, but the pair is a hybrid only if the verifier demands the post-quantum key: the envelope cannot (Part 5.3) |
| C-10 | constrains | the in-toto profile narrows the type, the payload, `keyid` and the signature count, and adds storage names | L32-50; L30; L250; L229 | R-0001, R-0037, R-0012, R-0091 | R-I-03 (ARCH-0001:453); T-051 (BACKLOG-0001:188); R-I-01 (ARCH-0001:451) | E2 has to satisfy both documents at once, and neither record's schema alone checks that: in-toto's does not require DSSE's `payload` or `sig` (Part 6, CC-06, CC-07) |
| K-01 | conflicts | each format signs its own input, so a KSA signature never verifies as a DSSE one | L19; L64-67 | R-0035, R-0046, R-0049 | R-I-03; SPEC-0002 §6.3 (:372-373), §13.2 (:895-901); SPEC-0001 §5.3 (:226-227); ADR-0004 item 4 (:51-52) | every DSSE export signs again, and SPEC-0001 asks for a separate key (Q-02). DSSE §2.2 opens a way out: PAE as KSA's signing input (D-05, Part 2.5, Q-03) |
| K-02 | conflicts | `(t, n)` counts unique keys over one byte-identical payload | L121-139 | R-0070, R-0077, R-0078 | R-M-06; SPEC-0004 §6.4 (:423-431), §7.2 (:455-476), ask 17 (:840) | a mapping that reads a KSA threshold as DSSE's `(t, n)` counts Bob and bob2 twice where SPEC-0004 counts once, and cannot count separate statements that agree (Part 4.4) |
| K-03 | conflicts (terminology) | `n` is the number of unique trusted keys, `t` the threshold | L121-123 | R-0070 | R-M-06 (ARCH-0001:439); ARCH-0001 §4.1 (:346); SPEC-0002 §8.6 (:606-608); SPEC-0004 §6.4 (:423-428) | DSSE's `n` and ARCH-0001's `n` count keys, while SPEC-0002 §8.6 and SPEC-0004 §6.4 write the threshold itself as `n`. A table that maps `n` to `n` maps a threshold to a member count (Part 4.3, Q-11) |
| S-01 | silent | duplicate member names, JSON `null`, member order | L207-219 | R-0087, R-0088 | P5.2 (ARCH-0002:498-501); SPEC-0002 V1 (:693) | two parsers can read two payloads, or two types, from one envelope; the bytes-identity rule (R-0008, R-0009; again in §2.3, R-0016, R-0017) is DSSE's only defence, and it names the payload only (S-08), and P5.2 does not name the case (Q-05) |
| S-02 | silent | base64 padding, mixed alphabets, non-zero trailing bits, whitespace | L106-107; L223-225 | R-0007, R-0090 | P5.1 (ARCH-0002:405-414) | which spellings our importer rejects is open (Q-05) |
| S-03 | silent, and inconsistent | bounds on `t` and `n`; whether `signatures` may be empty | L121-123; L248-249; L305 | R-0070, R-0011, R-0020 | ARCH-0001 §4.1 (:346), §7 (:577-581); SPEC-0002 §8.6 (:606-607) | KSA has 1 ≤ k ≤ n and negative vectors (T-031); DSSE states no bound, `t` = 0 passes an envelope none of whose signatures verifies (SD-10), and SD-2 leaves the empty array both legal and not |
| S-04 | silent | post-quantum: algorithm, sizes, context strings, hybrids | L71-73 | R-0053 | SPEC-0002 §6.5 (:409-422); SPEC-0001 §5.2 (:212-217), §11 (:415-421) | Part 5 |
| S-05 | silent | `KEYID`'s format and how it maps to a key | L52-56 | R-0042, R-0043, R-0006 | ADR-0005 (:36-38); SPEC-0002 §4.5 (:288) | the spelling is MAP-0002's (Q-04) |
| S-06 | silent | validity, revocation, time, replay | — | — | SPEC-0002 §7.3 (:488-501), §8.7 (:619-627), §13.8 (:936-940) | E1 carries `valid` signed inside the TBS; E2 drops it at this layer |
| S-07 | silent | an object carrying both `payload` and `signed` | L484-487 | R-0103 | P5.2 (ARCH-0002:509) | DSSE tells old from new by which field is present and never says what both mean (SD-11); P5.2's import rule rejects the extra `signed` |
| S-08 | silent | which `PAYLOAD_TYPE` reaches the application: the bytes-identity rule names the body only | L109-113; L273-277 | R-0008, R-0016, R-0108 | R-O-05 clause 3 (ARCH-0001:467); P5.2 (ARCH-0002:498-510); SPEC-0002 §6.4 (:397-398) | natively moot: the DS label is fixed and `kind` is in the TBS. An importer takes the type from the verification step and rejects a duplicated `payloadType` (Part 3.2, SD-19) |

---

## 1. T-051 / MAP-0002: exactly which bytes are signed

T-051 is WP3's `MAP-0002`, in-toto Statement ↔ `ArtifactStatement`
(BACKLOG-0001:188). It names in-toto-envelope-v1 and in-toto-attestation-v1 as
its inputs, not this record; it reaches DSSE because the in-toto envelope layer
RECOMMENDS DSSE and leaves the signing input to it (in-toto S-01, *in-toto
design-notes.md:155*). library#152 asks this record to pin those bytes.

### 1.1 The definition

<!-- q L16 -->
> A signature is defined as:

<!-- q L19 -->
> SIGNATURE = Sign(PAE(UTF8(PAYLOAD_TYPE), SERIALIZED_BODY))

<!-- q L60-61 -->
> * PAE() is the "Pre-Authentication Encoding", where parameters `type` and `body` are byte sequences:

<!-- q L64-68 -->
> PAE(type, body) = "DSSEv1" + SP + LEN(type) + SP + type + SP + LEN(body) + SP + body + = concatenation SP = ASCII space [0x20] "DSSEv1" = ASCII [0x44, 0x53, 0x53, 0x45, 0x76, 0x31] LEN(s) = ASCII decimal encoding of the byte length of s, with no leading zeros

<!-- q L75-76 -->
> * UTF8() is [UTF-8 encoding](https://tools.ietf.org/html/rfc3629), transforming a unicode string to a byte sequence.

The authenticated parameters are exactly two; the table at L24-28 gives `KEYID`
*Authenticated: No* (R-0036), and the signature is the
output, absent from the table (SD-4). The proto comment restates the same PAE
with `payload` for `body` (R-0020; SD-5 on the naming).
The requirements lane's R-0105 draws the
consequence: nothing else in an envelope is authenticated.

### 1.2 The vector, byte by byte

§1.4 gives one vector: a body, a type, the PAE, an ECDSA P-256 key and the
signed envelope.

<!-- q L149 -->
> hello world

<!-- q L155 -->
> http://example.com/HelloWorld

<!-- q L161 -->
> DSSEv1 29 http://example.com/HelloWorld 11 hello world

Recomputed by this lane's build from L149 and L155 and asserted equal to L161
before the table was written (derived; the same layout is
`messages.yaml` → *PAE (Pre-Authentication Encoding)* → `layout_vector`):

| field | offset | octets | hex |
|---|---|---|---|
| `"DSSEv1"` | 0 | 6 | `445353457631` |
| SP | 6 | 1 | `20` |
| LEN(type) | 7 | 2 | `3239` |
| SP | 9 | 1 | `20` |
| type = UTF8(PAYLOAD_TYPE) | 10 | 29 | `687474703a2f2f6578616d706c652e636f6d2f48656c6c6f576f726c64` |
| SP | 39 | 1 | `20` |
| LEN(body) | 40 | 2 | `3131` |
| SP | 42 | 1 | `20` |
| body = SERIALIZED_BODY | 43 | 11 | `68656c6c6f20776f726c64` |
| **PAE** | 0 | **54** | sha256 `217751fac2c4f14edb2c9297fbc34abcb016ba88e74757e875ec4ac16fb6b6a1` |

The envelope the vector produces:

<!-- q L177-179 -->
> {"payload": "aGVsbG8gd29ybGQ=", "payloadType": "http://example.com/HelloWorld", "signatures": [{"sig": "A3JqsQGtVsJ2O2xqrI5IcnXip5GToJ3F+FnZ+O88SjtR6rDAajabZKciJTfUiHqJPcIAriEGAHTVeCUjW2JIZA=="}]}

`examples/` recomputes all of it (`python3 -I -B
distilled/examples/reproduce.py`, run in this pass: `reproduce: ok`): the PAE
two ways, equal to the printed line byte for byte
(`examples/pae.verbatim.txt`, `examples/pae-section-1-4.derived.hex`); the key
on P-256 with d·G = (X, Y); the `sig` as 64 octets r‖s that verifies over the
PAE and equals the RFC 6979 signature recomputed from d; the payload decoding to
the 11-octet body; and the negatives — the bare body, a changed type, a body
with a trailing newline, the PAE of the base64 text, type and body swapped,
`DSSEv2`, and others — all failing. `examples/pae-vectors.derived.json` adds 17
build vectors (empty type and body, multi-byte UTF-8 types, lengths 9, 10, 99,
100, 1000, a space inside the type, a binary body) and 19 strings the grammar
`schema/pae.derived.abnf` must reject; `schema/check-pae.derived.py` checks
them. *Observations, not source claims* (examples/README.md): the printed
signature is low-s, and its base64 is the standard alphabet, padded. The one
vector is ECDSA P-256, an algorithm KSA reserves and has not specified (suite 2,
SPEC-0002:360), so it tests MAP-0002's bytes and none of its keys (Part 5.2).

### 1.3 What a mapping must pin

1. **The type's bytes, exactly.** PAE takes UTF8(PAYLOAD_TYPE) of the string
   as sent. The string is opaque and case-sensitive (R-0038), so a
   mapping compares and signs it byte for byte: no case folding, no
   normalisation. R-0003 and R-0005 advise the
   producer; they license no consumer to fold. That is SPEC-0002 §4.1's stance
   on text, byte-exact and never normalised (SPEC-0002:222). Because the type is
   inside PAE, choosing it *is* choosing signed bytes; the in-toto extraction
   measured 11 octets between its two admissible values (in-toto D-03 and its
   §8 check 2, *in-toto design-notes.md:141, :795-797*).
2. **The body's bytes, decoded.** The signature is over SERIALIZED_BODY, never
   over its base64 text:

<!-- q L434-438 -->
> - Why sign raw bytes rather than base64 encoded bytes (as per JWS)? - Because it's simpler. Base64 is only needed for putting binary data in a text field, such as JSON. In other formats, such as protobuf or CBOR, base64 isn't needed at all.

   `reproduce.py` checks that the PAE of the base64 text fails.
3. **The lengths.** ASCII decimal of the *byte* length with no leading zeros
   (L68). A KSA TBS at SPEC-0002 §13.6's floor of 65,536 octets has a
   five-digit LEN. How zero is written the source does not say; the
   requirements lane reads it as the single digit `0`
   (R-0104, inferred), as `messages.yaml` does.
   It matters: R-0011 lets an envelope carry an empty
   payload or type.
4. **Nothing after the body.** No terminator and no newline: the vector's body
   is 11 octets and its LEN is 11 (L149, L161). `reproduce.py` check e proves
   the no-newline reading, because the printed signature verifies over that
   PAE and over no variant with a newline.
5. **What is not signed**, and so is no part of any identity: `KEYID`
   (R-0036), the envelope's JSON (member names, order,
   whitespace), the base64 alphabet and padding, and any extra member
   (R-0014, R-0015). One
   signed message therefore has many envelope byte strings (C-02). An export's
   or an import's identity is computed over (type, body), as in-toto Q-13
   inferred (*in-toto design-notes.md:910-916*); DSSE's PAE supports the
   inference (R-0105).
6. **The base64 spelling.** Either alphabet is allowed:

<!-- q L106-107 -->
> Either standard or URL-safe base64 encodings are allowed. Signers may use either, and verifiers **MUST** accept either.

<!-- q L223-225 -->
> Base64() is [Base64 encoding](https://tools.ietf.org/html/rfc4648), transforming a byte sequence to a unicode string. Either standard or URL-safe encoding is allowed.

   *(inferred)* An export emits one spelling and says which; the vector's
   (standard, padded) is the obvious pin (Q-05). An importer accepts both,
   which is a MUST (R-0007). **mofn's lane-a verifier
   would fail it.** It decodes `payload` and `sig` with Python's
   `base64.b64decode` (lane-a/02_dsse_intoto.py:78, :81;
   lane-a/03_slsa_provenance.py:93, :119), which reads only the standard
   alphabet: it drops every `-` and `_` and then raises, unless what remains is
   a length the padding completes, in which case it returns other bytes without
   error. Over 14,610 seeded random strings whose two spellings differ it raised
   on 9,230 and returned wrong bytes on 5,380, never the right ones; the
   vector's own `sig` (L179), re-spelled URL-safe, decodes to 63 octets instead
   of 64 (Method). `base64.urlsafe_b64decode` decodes either spelling of that
   `sig` to the same 64 octets. The signature then fails, so the failure is
   closed, but it breaks R-0007, and two components
   that decoded one envelope with the two functions would hand on different
   bytes, the divergence R-0008 forbids within one
   implementation.
7. **A new signature.** The native signature cannot be carried (K-01): PAE
   begins with the octet `0x44` (L67), a suite-1 signing input with the DS label
   `KSA-STMT-SIG-v1\0`, whose first octet is `0x4b` (SPEC-0002:372-373), and a
   TBS with a CBOR map head, `0xa0`…`0xbf` (in-toto §8 check 3 made the same
   count, *in-toto design-notes.md:798-808*). No byte string is both. So
   MAP-0002 also states what `Sign()` is for each suite (D-04, Part 5).
8. **Pin from `protocol.md`, and test against the vector.** At our pin the proto
   comment and §1.1 agree (R-0020). At v1.0.0 they did not:
   the proto comment described a little-endian length-prefixed PAE while
   `protocol.md` already printed today's vector (Which DSSE this is, above). A
   mapping that had copied the proto comment then would have signed other bytes.

### 1.4 What that means for an export of our statement

| | **E1**: the KSA TBS in DSSE | **E2**: an in-toto Statement in DSSE |
|---|---|---|
| SERIALIZED_BODY | the TBS, byte for byte (SPEC-0002:309, :319-321) | a JSON Statement, whatever bytes MAP-0002's serialiser writes; there is no canonical form (in-toto L14 asks a format not to depend on one), and if MAP-0002 fixes one, R-O-03 asks it to cite the algorithm (ARCH-0001:465) |
| PAYLOAD_TYPE | one string of ours, open (Q-01); it SHOULD be application-specific (R-0002) | `application/vnd.in-toto+json` (in-toto L45-46), the only value for a KSA-defined type (in-toto D-03, *in-toto design-notes.md:288-291*) |
| what is signed | PAE(T, TBS), under a new signature | PAE(`application/vnd.in-toto+json`, Statement), under a new signature |
| the KSA statement digest | survives: SHA-256 of the decoded payload is SHA-256(`tbs`) (SPEC-0002:701) | lost: the Statement has its own bytes and digest (in-toto K-01) |
| R-O-05's first clause | holds: the canonical encoding verbatim, under a type PAE authenticates | does not hold: a second object is signed |
| who reads it | any DSSE consumer told T and the key out of band | the in-toto world |

*(inferred)* E1 is the only export in which DSSE carries our canonical bytes;
E2 is the only one R-I-03 names. MAP-0002 is E2, so for T-051 the bytes to pin
are the PAE of a JSON Statement, whose serialisation MAP-0002 itself has to fix
before any vector can be written.

---

## 2. MD-3, ADR-0004 and DEC-002, field by field

MD-3 narrowed DEC-002 to option 5 on 2026-09-28: the CBOR data model, no IANA
tags, "COSE as export only", type identity as (defining key, label) per
P1, and YAML as the human form by a "canonical one-way mapping"
(meetings/2026-09-28.md:51-54). ADR-0004 accepted option 5 on 2026-10-25,
closing the narrowing (ADR-0004:132-133), and made COSE_Sign1 and DSSE the
export envelopes (:51-52), as option 5's own text already had (ARCH-0001:541;
PLAN-0001:365-368). DSSE is an envelope document, so docs/extraction.md:123-126
asks for the mapping below and :128-135 for 2.5, the part that can disagree.

### 2.1 Our signed statement against DSSE's fields

The KSA side is SPEC-0002 §5's envelope `[suite, says, tbs, sig, ? pub]`
(SPEC-0002:298-311) and §7.1's TBS fields (:428-438). E1 and E2 are the two
export products (Things to hold, item 4).

| KSA | DSSE | E1: the TBS in DSSE | E2: an in-toto Statement in DSSE | import |
|---|---|---|---|---|
| `tbs`, element 2, the TBS exactly as signed (SPEC-0002:309) | `payload`, Base64(SERIALIZED_BODY) (R-0088), any bytes (R-0037) | the TBS, byte for byte; base64 only in the JSON text | a JSON Statement MAP-0002 writes from the TBS: a second object | kept as received (SPEC-0001:229-232) |
| `kind`, TBS key 1 (SPEC-0002:433), and the DS label, never sent (:397-398) | `payloadType`, inside PAE (R-0035, R-0038) | one string T for every kind (Q-01); `kind` stays in the TBS | `application/vnd.in-toto+json` (in-toto L45-46); the kind's meaning moves into the Statement | compared byte for byte, taken from the verification step (S-08) |
| `suite`: element 0 a hint (SPEC-0002:307), TBS key 2 signed (:350) | nothing: no algorithm field (R-0053); `KEYID` hints at one (R-0042) | signed inside the TBS; nothing outside it | dropped unless the Statement carries it | from the key, agreed out of band (R-0055) |
| `says`: element 1 a hint checked at V6 (SPEC-0002:308, :698), TBS key 3 signed | `signatures[].keyid`, an unauthenticated hint (R-0006, R-0022) | the kid may go in `keyid` as a hint; the principal stays in the TBS (P5.2, ARCH-0002:525-530) | `keyid` as a hint; the speaker is whichever key verifies unless the Statement names it (2.2) | never a principal: the kid is computed from the key that verified |
| `sig`, element 3, over `DS ‖ tbs` (SPEC-0002:310) | `signatures[].sig`, Base64(Sign(PAE(type, body))) (R-0088) | a new signature (K-01) | a new signature (K-01) | each signature verified alone (D-02) |
| a second speaker: a separate statement (X-02) | another element of `signatures` (R-0010) | none: a signature by a key the TBS does not name has no native meaning *(inferred)* | any number of co-signers over one Statement | one external statement per verified signer (D-02) |
| `pub`, element 4, optional, checked at V3 (SPEC-0002:311, :695) | nothing | dropped; P5.2 forbids an added member (C-04, Q-07) | dropped | the key comes from the verifier's own set (R-0106) |
| `this`, `valid`, `body`, TBS keys 4-6 (SPEC-0002:436-438) | inside SERIALIZED_BODY | signed inside the TBS | MAP-0002's Statement fields; `valid` has no place at this layer (S-06) | the Statement layer's (library#134) |
| the envelope itself: a KSA-CBOR array (SPEC-0002:298-303) | a JSON object (R-0086, R-0087); other encodings allowed, none standardised (R-0094, C-0057) | JSON with base64 (C-06); the §2.2 path is D-05 | JSON with base64 | JSON parsed under P5.2's exterior rule |
| the statement digest, SHA-256 of `tbs` (SPEC-0002:701) | none: DSSE derives no identifier | SHA-256 of the decoded payload, so it survives | lost | over (type, body), plus the verifying kid for the speaker (2.2) |
| closed maps: an unknown field is an error (SPEC-0002:440-444) | producers may add members, consumers ignore them (R-0014, R-0015) | none emitted (P5.2, ARCH-0002:510) | none emitted | unknown exterior members rejected (ARCH-0002:509); inside a signature element, open (Q-05) |

### 2.2 The speaker, which DSSE never signs

PAE takes the type and the body and nothing else
(R-0105); a signer is known only as the
key a signature verifies under (R-0106).
In E1 the TBS names its speaker in `says`, so an importer can rebuild V6's
check, the verifying key's kid against the signed `says` (SPEC-0002:698), and
treat a signature by any other key as saying nothing *(inferred)*. In E2 the
speaker is the verifying key unless MAP-0002 puts a kid inside the Statement,
which is the Statement layer's question (in-toto-attestation-v1, library#134,
not read here). That is still P2's speaker, since the speaker is the key
(ARCH-0002:146-148), and R-O-01's kid is computable from it (ARCH-0001:463). What
E2 loses is the speaker *in the signed bytes*: two keys signing one Statement
make two statements with one payload digest, where two KSA speakers' TBSs always
differ in `says`. *(inferred)* So an import keys an external statement on the
verifying kid as well as on (type, body), or two speakers' statements collide
(Q-08).

### 2.3 What an export deliberately does not carry

- no member beyond `payload`, `payloadType` and `signatures` (P5.2,
  ARCH-0002:510), and *(inferred)* none inside a signature element beyond `sig`
  and `keyid`, which P5.2, written for the exterior (ARCH-0002:498-499), does not
  name (Q-05);
- no principal in `keyid` (P5.2, :530), and no `pub` (C-04);
- no threshold as a signature count (C-05, Part 4.3);
- not the native signature, which does not verify under PAE (K-01);
- in E1, no signature by a key other than the one `says` names (2.2);
- in E2, *(inferred)* not the signed `suite`, the native digest, `valid` or
  `pub` (D-04, S-06, Part 1.4).

### 2.4 MD-3, clause by clause

| MD-3 clause, quoted (meetings/2026-09-28.md:51-54) | what DSSE does | finding |
|---|---|---|
| "CBOR data model" | the payload is any bytes (R-0037), so E1 carries KSA-CBOR verbatim; the envelope is JSON, and other encodings are permitted but not standardised (R-0086, R-0095, C-0057) | the data model holds inside E1's payload and nowhere outside it (C-06) |
| "no IANA tags" | no CBOR at the envelope, so no tags; but the first form R-0001 recommends for the type is a media type, linked to the IANA registry (R-0040) | ADR-0004 item 3 names the registries option 5 keeps out of the native model (ADR-0004:46-50), as ARCH-0001:566-567 asked it to, and Media Types is not among them. E1 takes the URI form (R-0041), departs from the SHOULD, or adds the registry to item 3's boundary list (Q-01) |
| "COSE as export only" | DSSE is one of the two envelopes ADR-0004 item 4 names | MD-3's words name COSE alone; DSSE entered with option 5's text (PLAN-0001:365-368; ARCH-0001:541) and ADR-0004:51-52. §2.2 lets an envelope of ours be a DSSE structure (D-05), which *export only* would then not describe |
| "type identity is `(defining key, label)` per P1" | the type SHOULD be a media type or a URI (R-0001): global names | natively never (the DS label and `kind`; ADR-0003 D1, :47). At the boundary one string, chosen once and inside every E1 signature (D-03). The pre-FX-1 finding 2 is half withdrawn, below |
| "YAML is the human form with a canonical one-way mapping" | no human form; §4.4's first theoretical problem is two payloads under one canonical encoding (L393-398) | a one-way mapping read literally is many-to-one, the hazard DSSE names (A-10). SPEC-0002 §11.1 made it one-to-one (:733, :743-748) and §11.3 rejects YAML that two parsers read two ways (:787-791) |
| "Option 2 is retained only as the comparison fixture" | — | no bearing: DSSE is no part of option 2 |

The minute's last sentence schedules the D5 fixture package and then the ADR,
which is ADR-0004; it has no bearing here.

**The pre-FX-1 finding 2, half withdrawn.** The old notes held that DSSE
licenses a non-global type, because R-0001 is a
SHOULD and because §2.2 lets an application send the type in a shorter coded
form, so that "a locally-scoped type indicator is still fully authenticated"
(old design-notes.md:81-84). The first half stands: a type that is neither a
media type nor a URI departs from a SHOULD and from nothing stronger. The second
does not. §2.2 permits other encodings only without invalidating the signature
(R-0094), and what is signed is
UTF8(PAYLOAD_TYPE) (R-0035). A code that stood in PAE in
place of the string would invalidate every signature made over the string, so
the code is a transmission spelling, restored to the full string before PAE is
computed (R-0110, inferred); its mapping lies outside
every signature (protocol.md OI-08). What PAE authenticates is the full string,
which R-0001 governs. So option 3's fourth ground
(DECISIONS-0001:116-119; ADR-0004:121-124; enumerated, as a global type
identifier R-M-12 excludes, at `topics/canonical-encoding.yaml:134-137` and
DL-0006 review:39-40) is weakened by the SHOULD alone. The
withdrawn half, that the code is what PAE authenticates, also stands in
DL-0006 review:41-45, mofn report R-0006:1233-1239 and the library's own
`topics/canonical-encoding.yaml:353-358`, each as "which PAE authenticates just as well".
Their owners correct them; this file edits none of them (Q-12).

### 2.5 Where DSSE cuts against MD-3 and option 5

1. **Option 3 shared DSSE; option 5 pays twice at this boundary.** Under option
   3 the native form was JSON with RFC 8785 and DSSE was the signed form
   (ARCH-0001:539), so a native signature was a DSSE signature and E1 was the
   native object itself. Under option 5 every DSSE export needs a JSON
   serialiser, a base64 codec and a PAE beside KSA-CBOR (C-06), and a second
   signature (K-01). That is a cost option 5 pays and option 3 does not. E2
   re-signs under every option, since no native form is an in-toto Statement.
   Option 3 is withdrawn on four grounds (ADR-0004:121-124;
   DECISIONS-0001:116-119); DSSE bears on the fourth only, and weakens it only
   by a SHOULD (2.4). Evidence recorded, not a reopening.
2. **PAE as KSA's signing input (option named: a suite whose signature input is
   PAE(T, TBS)).** Nothing in ADR-0004 fixes the signing input: `DS ‖ TBS` is
   SPEC-0002 §6's (:345, :372-374). A suite that signed PAE(T, TBS) for a fixed
   string T would make every native signature a DSSE one, E1 a re-encoding of
   the native object under the same `sig`, and the KSA array itself a DSSE
   structure of §2.2's kind: CBOR, the type defaulted, extra members ignored
   (R-0094, R-0096,
   R-0014). *(inferred)* Its costs: domain
   separation moves from a label no other protocol uses (SPEC-0002:397-404) to a
   type string inside DSSE's framing, so a KSA signature would verify in the
   DSSE world by design and SPEC-0002 §13.2's separation (:897-899) would hold
   against other protocols and other DSSE types only; ML-DSA's context still has
   to be fixed, which DSSE leaves open (Part 5.2); and ADR-0004 item 4's *export
   envelopes only* would no longer describe DSSE. It changes no byte of the TBS,
   so it is not a DEC-002 option; it is DEC-005's and SPEC-0002 §6's (Q-03). It
   is named because docs/extraction.md:133-135 asks for it, not proposed.
3. **The registry list.** ADR-0004 item 3 states option 5's no-registry property
   as a list (ADR-0004:46-50), as ARCH-0001:561-567 asked, and DSSE's recommended
   type form is a registry that list omits (2.4).
4. **MD-3's "one-way".** Read literally, the minute's mapping is the many-to-one
   map §4.4 warns about; SPEC-0002 §11 is the stronger text and should be what
   ADR-0004's reader takes MD-3 to mean (2.4, A-10).

**Not discriminators.** Re-signing for E2 (every option). The one-signature
envelope (X-02), which is SPEC-0002 §5's under any encoding. The `keyid` and
principal collision (A-06), which is DEC-003's and P5.2's. The pre-FX-1 finding
5's hazard for option 4, a polyglot across two live profiles: option 4 is
rejected (ADR-0004:125-126), and under option 5 two profiles meet only at the
boundary, E1's CBOR and E2's JSON, told apart by a type PAE authenticates (A-05,
Part 3.3).

**Where DSSE favours option 5 and SPEC-0002.** It signs raw bytes, so the TBS
travels verbatim (A-07). KSA's DS label keeps a KSA signature and a DSSE one
apart in both directions (Part 1.3 item 7). KSA's binding of algorithm to key
is stronger than DSSE's: it signs the suite (X-04). And KSA already verifies
before it decodes (A-02, A-03).

---

## 3. R-O-05: verify before parse, never re-parse, and §4.4's critique

R-O-05 has three sentences (ARCH-0001:467): the signed payload is the
canonical encoding verbatim with an authenticated type indicator; a verifier
verifies before decoding and never canonicalises as part of verification; a
human-facing form is regenerated from verified canonical bytes. PLAN-0001
proposed it to keep the project clear of DSSE's critique (PLAN-0001:378-382),
and mofn's decode spike wrote the falsifier down: had canonicality been
uncheckable without re-encoding, DSSE would have been right and canonical form
abandoned (DECODE-FINDINGS.md:13-17). It did not fire (:25-26, :140-144).
This part reads R-O-05 against what DSSE actually requires.

### 3.1 Verify before parse, step by step

| # | DSSE §1.2, one signature | DSSE §1.3, `(t, n)` | KSA, SPEC-0002 §9.2 (:688-701) | finding |
|---|---|---|---|---|
| 1 | decode the four values; reject if that fails (R-0060, R-0061) | the same, with SIGNATURES (R-0071) | V1: the envelope array under the rejecting decoder | both decode the *envelope* first; R-O-05's decoding is the payload's (SPEC-0002:195-199) *(inferred)* |
| 2 | optionally narrow the keys by `KEYID` (R-0062) | per signature (R-0074) | V2 suite, V3 key by (`suite`, `says`) | KSA's hints are checked later (V6); a `keyid` never is (A-06) |
| 3 | verify over PAE; reject on failure (R-0063, R-0064) | verify; skip a failure; count unique keys against `t` (R-0076, R-0079) | V4 over `DS ‖ tbs` as received | the type is inside both signed inputs (A-01) |
| 4 | reject an unsupported type (R-0065) | the same (R-0080) | V2 before V4 for the suite; `kind` at V7 after V5 | both reject the unknown; KSA's class is fixed by the DS label (A-04) |
| 5 | parse; reject on failure (R-0066, R-0067) | the same (R-0081) | V5 rejecting decode of the very `tbs` V4 verified | the order R-O-05 asks for, in both |
| 6 | hand on the verified bytes; never re-parse the envelope (R-0008, R-0009) | not restated in §1.3; §2.3 makes it general (R-0097) | V5's input is V4's; V9 digests the same `tbs` | 3.2 |

The rows agree, and in DSSE they are only a list. No sentence makes the order
binding on a verifier: it is asked of the design
(R-0028) and preferred
(R-0101), and the requirements lane infers it for
the steps (R-0107; protocol.md OI-05). KSA's
procedure is a MUST in this order (SPEC-0002:688-689), and R-O-05 a SHALL. So a
DSSE verifier that parses first breaks no sentence of DSSE's, and **our
importer has to impose R-O-05's order itself** (C-07). mofn's lane-a sample 3
is such a verifier: it decodes and parses the payload
(lane-a/03_slsa_provenance.py:93-94, :155-156) before it verifies
(:119-123), and it verifies `signatures[0]` alone (:119), where §1.3 would skip
a failing signature and try the next (R-0076). It is a
throwaway (lane-a/README.md:3); in-toto C-01 recorded the same so that T-052
does not inherit it (*in-toto design-notes.md:355-365*).

### 3.2 The re-parse MUST NOT, and the type it does not name

<!-- q L270-271 -->
> The following advisories are relevant to all envelope formats, not just the standard JSON envelope.

<!-- q L273-277 -->
> **Important:** Implementations MUST ensure that the same payload bytes that are verified are the ones sent to the application layer. In particular, implementations MUST NOT re-parse the envelope after verification to pull out the payload. Failure to adhere to this requirement can lead to security vulnerabilities.

KSA meets it by construction: V5 decodes the `tbs` V4 verified, and nothing
reads the envelope again (SPEC-0002:313-315, :696-697). An importer has to
state it: the parser MAP-0002 runs on an import takes the bytes the
verification step produced, never a fresh read of the JSON *(inferred)*. R-O-05
does not say this in its own words; its third sentence regenerates a
human-facing form from verified bytes, which is the same rule seen from the
display (A-03).

The rule names the payload, in both places (R-0008,
R-0016), and **not the type**. JSON lets an envelope carry
a member twice, and DSSE is silent on duplicates (S-01). A verifier whose
parser keeps the first `payloadType` verifies PAE over it; an application that
reads the envelope again for the type, which no sentence forbids, may get the
last. The signature then authenticated one type and the application acts on
another: the notebook's confusion, rebuilt from a parser differential
*(inferred)*. The requirements lane closes it with an inferred rule, the type
handed on is the type verified (R-0108);
this file offered it to normative.md as a source-defect candidate, DN-SD-2,
which pass 2 took in as SD-19 (Part 7). Natively it is moot: the DS label is fixed, never sent
(SPEC-0002:397-398), and `kind` is inside the TBS. At import, the type comes
from the verification step, and a duplicated member is rejected (Q-05).

### 3.3 Background §4.4, problem by problem

<!-- q L387-388 -->
> First, the signature scheme depends on [Canonical JSON], which has one practical problem and two theoretical ones:

1. **The practical problem**, that the payload has to be JSON or be turned into
   JSON (L390-392; its normative form is R-0024). DSSE's
   answer is what lets E1 carry KSA-CBOR verbatim (C-08). Nothing to answer.
2. **The first theoretical problem**, condition (1) stated as an attack:

<!-- q L393-398 -->
> 1. Theoretical problem 1: Two semantically different payloads could have the same canonical encoding. Although there are currently no known attacks on Canonical JSON, there have been attacks in the past on other canonicalization schemes ([example](https://latacora.micro.blog/2019/07/24/how-not-to.html#canonicalization)). It is safer to avoid canonicalization altogether.

   DECISIONS-0001 records that R-O-05 *assumes* condition (1) and condition (2)
   and delivers (3) and (4) (DECISIONS-0001:109-111). KSA answers DSSE here
   without abandoning canonical form. On the signature path nothing is
   canonicalised: the bytes verified are the bytes decoded (SPEC-0002:203-205),
   so no two payloads ever meet under one canonical encoding there. On the
   identity path, statement digests and DefinitionIds (SPEC-0002:288-290), the
   encoding gives each value one byte string and the rejecting decoder each
   accepted byte string one value (:231-266), text is never normalised (:222),
   and the YAML form converts one-to-one (:733, :743-748). ADR-0004 scores
   (1) to (4) as met (ADR-0004:72) (A-10).

   **Over the pair, not the bytes.** The pre-FX-1 finding 5, carried: the
   notebook's payload is a polyglot (L593), a valid CBOR link and a valid
   protobuf link in one byte string. Each encoding is injective alone; the pair
   (type, bytes) is not, unless the type is authenticated. Condition (1) has to
   hold over that pair (old design-notes.md:170-176). DSSE puts the type in
   PAE (R-0035); KSA fixes the class in the DS label, the
   kind in the TBS, and one encoding for every signed object (ADR-0003 D2,
   :48). At the boundary E1 and E2 are two profiles in one envelope format,
   told apart by a type PAE authenticates (A-05).
3. **The second theoretical problem**, parsing before verifying (L399-401; its
   normative form is R-0028): R-O-05's second sentence,
   met by V4 before V5, so the rejecting decoder runs on authenticated bytes
   only. The spike's own conclusion is that R-O-05's ordering answers this
   objection (DECODE-FINDINGS.md:140-144) (A-02).

§4.4's second concern, the missing authenticated context (L407-415), is R-O-05's
authenticated type indicator (A-01).

### 3.4 The notebook's attack needs two failures

<!-- q L592-595 -->
> 1. Construct a target payload T in protobuf format that we want the victim to consume. 2. Send a carefully crafted build request that results CI/CD returning a signed CBOR-type link file, such that the payload is interpreted as P when type is CBOR but T when type is protobuf. 3. Modify the `payloadType` field to say `Protobuf` instead of `CBOR`. This does not invalidate the signature because the `payloadType` is unauthenticated. 4. Send the modified link file to the victim. They will interpret the payload as T, even though the CI/CD system intended it to be interpreted as P.

The exploit works only because the type sits outside the signature
(L554, L594) **and** the victim's protobuf decoder skips what it does not know:
the fixed bytes of the CBOR map head and of `command` parse as fields 1652 and
12, which the link schema lacks and the library ignores (L1072-1073), and a
dummy field 15 swallows the tail (L1097; SD-12 on its characters). Either rule
alone stops this exploit: PAE turns step 3's change into a signature failure,
and a must-understand decoder (P5, ARCH-0002:394-402) rejects fields 1652, 12
and 15. Only the first closes the class: a polyglot built from fields the
victim knows passes a must-understand decoder *(inferred)*. KSA has both, the
DS label and `kind`, and closed maps under a rejecting decoder
(SPEC-0002:440-444, :251-266) (A-09).

### 3.5 Where DSSE cuts against R-O-05

1. **R-O-05 is stricter than DSSE on order** (3.1). Not a cut against R-O-05: a
   cost at every DSSE import, which C-07 records.
2. **DSSE's strong form lies outside DEC-002's options** (option named: no
   canonical form at all). §4.4 ends by advising against canonicalisation of any
   kind (L398, C-0075), and the spike's falsifier named the
   same option for us: sign received bytes and identify by content digest only
   (DECODE-FINDINGS.md:15-17). Every DEC-002 option has a canonical form, so
   DSSE's position scores against none of them. KSA already signs and digests
   the received bytes (SPEC-0002:289); its canonical form earns its cost where
   an identifier is computed rather than received, a DefinitionId (:290) or a
   description target whose canonical encoding is its identity (:458), and
   conditions (5) and (6) live there (DECISIONS-0001:109-115). DSSE derives no
   identifier and says nothing about that path (X-03).
3. **R-O-05's first sentence and E2.** An in-toto export signs a JSON
   Statement, not the canonical encoding (Part 1.4). Whether R-O-05 governs an
   export at all is not written down (Q-06).
4. **The bytes-identity rule is DSSE's, not R-O-05's** (3.2). The library's
   topic answer said so at the time (`topics/canonical-encoding.yaml:59-62`);
   SPEC-0002 meets it, and R-O-05 still does not state it.

---

## 4. DEC-005, R-I-03 and the threshold

### 4.1 DEC-005, read against DSSE

DEC-005's options are "DSSE (in-toto world), COSE_Sign1 (SCITT world), both with a single unsigned payload schema" (ARCH-0001:645). mofn report R-0006 §5.2 found
two readings once SPEC-0002 §5 gave KSA a native envelope, the native envelope
or the export one, and could not choose (mofn report R-0006:1254-1266);
ADR-0004 item 4 took the second (ADR-0004:51-52, :112). ARCH-0001 still uses no
export envelope (ARCH-0001:174-176).

| option | what DSSE brings | E1 | E2 | finding |
|---|---|---|---|---|
| DSSE | any bytes under any type the parties agree (R-0037, R-0055); meant for any signature use, not only in-toto (L327) | carries the TBS verbatim (Part 1.4) | in-toto's profile of it (Part 6) | DEC-005's *in-toto world* is a profile's label; DSSE is generic |
| COSE_Sign1 | outside this source | — | in-toto does not accept it as an envelope (in-toto L23-24) | the in-toto extraction's C-03 (*in-toto design-notes.md:377-389*) |
| both, one unsigned payload schema | the payload is opaque bytes, so the TBS can be both envelopes' payload | **meets it**: one TBS, two envelopes | does not: an in-toto Statement is E2's payload, and CWT claims R-I-03's COSE branch | R-I-03 names two payload schemas (ARCH-0001:453); DEC-005's third option has one. Only E1 satisfies both texts (C-08, Q-10) |
| not listed: the KSA envelope as a DSSE structure | §2.2's other encodings (R-0094) | E1 becomes a re-encoding, with no new signature | unchanged | needs a PAE suite (D-05, Part 2.5, Q-03) |

### 4.2 R-I-03: what an export to DSSE, and an import from it, has to do

R-I-03 asks for at least one export envelope in v1 (ARCH-0001:453). From Parts
1 to 3, an exporter:

1. pins the PAE exactly (Part 1.3), with a type of its own for E1 (Q-01) or
   in-toto's for E2 (in-toto L45-46);
2. emits one base64 spelling (Q-05), no member beyond the three, `keyid` only as
   a hint (2.3);
3. signs again, with a key SPEC-0001 would rather were separate (K-01, Q-02);
4. puts a threshold's `k` and members in the payload, never in the envelope
   (4.3).

And an importer:

1. accepts both alphabets (R-0007), which lane-a's
   decoder does not (Part 1.3 item 6);
2. verifies before it parses, which DSSE never makes binding (C-07);
3. hands on the verified bytes and the verified type (3.2, S-08);
4. verifies a several-signature envelope by §1.3, skipping a failing signature
   (R-0109; SD-9),
   and turns each verified signer into one external statement (D-02);
5. rejects unknown exterior members (P5.2) and, *(inferred)*, duplicated ones
   (Q-05).

### 4.3 The threshold: the envelope carries neither `t` nor `n`

<!-- q L121-123 -->
> A `(t, n)`-ENVELOPE is valid if the enclosed signatures pass the verification against at least `t` of `n` unique trusted public keys where `t` is application-specific.

<!-- q L133-136 -->
> - Add the accepted public key to the set ACCEPTED_KEYS. - Break if the number of unique keys in ACCEPTED_KEYS is greater or equal to `t`. - Reject if the unique keys in ACCEPTED_KEYS is less than `t`.

`t` is the application's; `n` counts the verifier's unique trusted public
keys. The count uses nothing from the envelope but its signatures, and `n`
appears in no step (messages.yaml, *(t, n)-ENVELOPE*: neither travels in the
envelope). §1.3 is new in v1.0.1; v1.0.0 has no threshold procedure at all (Which
DSSE this is).

**The pre-FX-1 finding 1, carried with its own correction amended.** The old
notes withdrew the claim that the envelope carries threshold semantics, and
said instead that it "carries `n`. It cannot carry `k`"
(old design-notes.md:47-48). Re-checked against the source:

- *carried*: `t` is no field, and `k` with the member set has to travel inside
  the signed payload (old design-notes.md:55-59). In KSA it does: a threshold
  `trust` carries `threshold` and `trusts` in its body (SPEC-0002:594-609), so
  E1 carries them signed and E2 only if MAP-0002's Statement does;
- *amended*: the envelope does not carry `n` either. `n` is the count of
  trusted keys on the verifier's side (R-0070);
  what the envelope carries is a list of signatures, and its length is neither:
  signatures by untrusted keys, failing ones and repeats by one key all sit in
  the list and count toward nothing (R-0076,
  R-0077; SD-14);
- *carried and strengthened*: a signature count is unsafe to read as `k`
  (old design-notes.md:61-65). DSSE authenticates only the type and the body,
  so anyone can drop a signature or move one between envelopes over the same
  type and body (R-0105); and the
  equivalence the old note leaned on is itself strained for `t` ≥ 2 (SD-18,
  4.4).

The *n* half of the old wording also stands in mofn and in this library:
DL-0006 review:24 and produced.md:68, mofn report R-0006:278, :342 and :1225,
mofn report R-0005:559 ("carries `n` and cannot carry `k`" or close
variants), `topics/canonical-encoding.yaml:346-347`, and this record's
`summary.md:104`. Their owners correct them (Q-12).

**The letters cross (K-03).** DSSE writes the threshold `t` and the key count
`n`; ARCH-0001 §4.1 writes `k` and `n` = the number of members (ARCH-0001:346).
SPEC-0002 §8.6 writes the threshold itself as `n`, an integer with 1 ≤ `n` ≤
the number of keys (SPEC-0002:606-608), and SPEC-0004 §6.4 counts `n` distinct
members (SPEC-0004:423-428); ARCH-0001 notes that §8.6 spells `k` as the field
`threshold` (ARCH-0001:574-575). So DSSE's `n` is ARCH-0001's `n` and not
SPEC-0002's, and a mapping table that carries `n` across unchanged maps a
threshold onto a member count. MAP-0002 names the field `threshold`, never a
letter (Q-11).

### 4.4 Where DSSE's count and SPEC-0004's count part

Read as the same thing, DSSE's `(t, n)` and SPEC-0004 §6.4's threshold differ in
three ways (K-02):

1. **What counts as one key.** DSSE counts unique keys and never says when two
   keys are the same (SD-14). SPEC-0004 counts distinct kids and counts two
   keys a rotation links as one member (SPEC-0004:431); in asks 17 and 18
   Bob and bob2 both attest, and a threshold of two is met only once Dave does
   too (SPEC-0004:840-841).
   A DSSE verifier that trusts both of Bob's keys counts two.
   And one signature can count for two trusted keys where the signature
   scheme lacks exclusive ownership and a key was admitted without proof that
   its holder signs with it (SD-15); a KSA statement names its speaker in the
   TBS (`says`, item 2), so there one signature cannot stand for a second
   member *(inferred)*.
2. **What is counted over.** DSSE counts signatures over one byte-identical
   PAE. SPEC-0004 counts separate statements that agree in target, type and
   value (SPEC-0004:424-427). Two KSA speakers' statements always differ in
   their TBS (`says`), so no DSSE envelope can hold two members' native
   statements as signatures over one payload *(inferred)*: a KSA threshold
   is never a DSSE `(t, n)`-ENVELOPE over E1. Over E2 it can be, since an
   in-toto Statement need not name its speaker (2.2), but then the threshold
   rule itself is in no signed byte.
3. **Separate envelopes.** DSSE makes a several-signature envelope equivalent
   to separate one-signature envelopes (R-0092) but
   counts `t` inside one envelope only (R-0070):
   for `t` ≥ 2, two separate envelopes each fall short where one envelope
   holding both signatures passes (SD-18, from this lane's pass-1 notes). An
   importer that turns each verified signature into an external statement
   (D-02) and counts by SPEC-0004 §6.4 sees the same answer either way, which
   is the reason to import that way rather than to count DSSE's way
   *(inferred)*.

The bounds differ too (S-03): KSA has 1 ≤ `k` ≤ `n` with negative vectors N-7
and N-8 (ARCH-0001:577-578), DSSE no bound at all, and `t` = 0 passes an
envelope none of whose signatures verifies (SD-10). ARCH-0001 records that
`trusts: [A, A]` with `threshold: 2` passes V8 and fails closed in SPEC-0004
(ARCH-0001:589-592), DSSE's SD-14 on the native side.

R-M-06 asks only that a threshold principal be representable without a CA
hierarchy (ARCH-0001:439). Natively it is, as `trust`'s threshold form. DSSE
neither helps nor hinders: it carries the threshold statement as a payload like
any other, and its own `(t, n)` is a verifier policy, not a principal.

---

## 5. Post-quantum and algorithm agility: an envelope that names no algorithm

### 5.1 What DSSE fixes, and what it leaves to the agreement

<!-- q L71-73 -->
> * Sign() is an arbitrary digital signature format. Details are agreed upon out-of-band by the signer and verifier. This specification places no restriction on the signature algorithm or format.

<!-- q L52-56 -->
> * KEYID: Optional, unauthenticated hint indicating what key and algorithm was used to sign the message. As with Sign(), details are agreed upon out-of-band by the signer and verifier. It **MUST NOT** be used for security decisions; it may only be used to narrow the selection of possible keys to try.

The signed bytes do not depend on the algorithm: PAE has no input for one
(R-0035), so one PAE can carry signatures by keys of several
algorithms, side by side (R-0010). The
design asks for any primitive, library and key store
(R-0025). Nothing authenticated names the
algorithm: not the envelope, not the signature. `KEYID` hints at key *and*
algorithm (R-0042) while the proto comment says key
only (R-0022) and may decide nothing
(R-0006). Whether a verifier may let `KEYID` choose the algorithm
is not said (SD-13); the reading taken by the requirements lane, which this file
follows, is that the algorithm comes with the key from the agreement
(R-0055, R-0106).
The signature *encoding* is out of band too: the one vector says r‖s in a
library's binary form (L167-168), where DER would be another spelling of the
same signature.

### 5.2 What MAP-0002 states for each suite

KSA's suite table already holds every item DSSE leaves open (SPEC-0002 §6.1,
:337-348): algorithm, key encoding, signature input, signature encoding,
verification rules. Under DSSE only the signature input changes (D-04).

| suite (SPEC-0002 §6.2, :354-365) | under DSSE, signed over | context | `sig` | base64 in JSON |
|---|---|---|---|---|
| 1, Ed25519 (SPEC-0002:367-393) | PAE(T, body), no DS label | none: Ed25519 has none | 64 octets R‖S | 88 characters |
| 8, ML-DSA-65, provisional (SPEC-0002:409-422) | PAE(T, body) | unspecified by DSSE; KSA passes `KSA-STMT-SIG-v1` for statements (:414-415) | 3309 octets | 4412 characters |
| 2, P-256, reserved and unspecified (SPEC-0002:360) | PAE(type, body), as in the source's one vector (L167-168) and the real provenance lane-a verifies (lane-a/03_slsa_provenance.py:121-123) | none | 64 octets r‖s in the vector | 88 characters |

*(inferred)* Two consequences. KSA's strict Ed25519 rules (SPEC-0002:377-393)
bind a KSA verifier, not a DSSE one, so MAP-0002 says whether an importer
applies them to an imported signature; an exporter's signatures pass them
anyway, being honest. And with suite 2 unspecified, the DSSE vector tests
MAP-0002's bytes but none of its keys, and an import of real provenance has no
suite to name its signer by (in-toto C-06, *in-toto design-notes.md:422-430*).

### 5.3 Post-quantum, item by item

1. **It fits.** No length is bounded: LEN has no upper bound
   (R-0050) and no base64 string has a maximum. An
   ML-DSA-65 `sig` is 4412 characters; its 1952-octet key (SPEC-0002:412) does
   not travel. A DSSE importer bounds its own work before verifying, as KSA's
   verifier must before V4 (SPEC-0002:926-928), because DSSE sets no bound
   *(inferred)*.
2. **The context string.** A DSSE signature under ML-DSA takes whatever context
   its signer passes, and DSSE names none. Two implementations that differ,
   empty against non-empty, make signatures neither verifies for the other
   *(inferred)*. Replay against KSA stays closed either way (Part 1.3 item 7;
   in-toto §8 check 3). Q-14.
3. **Hybrids are policy, not envelope.** A classical and a post-quantum
   signature can ride in one envelope over one PAE, and each verifies alone
   (R-0076). Every signature is outside every other's signed
   bytes, so any of them can be dropped in transit
   (R-0105), and `t` counts keys, not
   algorithms (R-0070). The pair gives post-quantum
   assurance only to a verifier that demands the post-quantum key; with `t` = 1
   over both keys it is as strong as the classical one (C-09). mofn's survey
   puts it as an envelope that cannot say that at least N threshold signatures
   are quantum-resistant (mofn survey R-0001:1604-1608). KSA is in the same
   place one level up: SPEC-0004 §6.4 counts members distinct by kid and puts no
   condition on their suites (SPEC-0004:431), so the property is a relying
   party's choice of members in both.
4. **Long-lived statements.** SPEC-0001 asks a statement that must verify for
   decades for a post-quantum suite or an external timestamp (SPEC-0001:214-217,
   :415-421). DSSE carries no time (S-06). E1 carries `valid.issued` signed,
   which is the speaker's claim and not such evidence (SPEC-0001:421-422).

### 5.4 Where this cuts, and two readings it corrects

- **mofn's survey, partly.** It calls DSSE's silence agility by omission, which
  permits algorithm confusion (mofn survey R-0001:1597-1608). DSSE's own
  background charges JWS with exactly that confusion, an `alg` not checked
  against the key (L345-349), and its answer is to carry no `alg` at all, so
  there is nothing to mismatch. Confusion comes back only if a verifier lets
  something unauthenticated pick the algorithm, and the one hint the envelope
  names is `KEYID`, which the MUST NOT on security decisions arguably covers
  and the text never names (SD-13). So the
  charge holds for that gap and for thresholds (5.3 item 3), not for the silence
  as such (X-04).
- **The library's `rfc-9964` design notes, narrowed.** Their Cut D finds that
  for a post-quantum `ArtifactStatement` only COSE_Sign1 among DEC-005's
  options has a standardised algorithm identifier, which costs the DSSE and
  *both* options (`records/ietf/rfc-9964/distilled/design-notes.md:519-533`).
  True of DSSE's envelope. E1 still names its algorithm, signed, as `suite`
  inside the TBS (SPEC-0002:350, :434), with no IANA allocation, which is what
  ADR-0004 item 3 wants native (ADR-0004:46-50); only a KSA-aware reader can use
  it. E2 names none unless the Statement carries one. So the cut holds for every
  consumer that does not read the payload, and E1 is not algorithm-silent.
- **Not a DEC-002 discriminator.** Every option exports to DSSE with the same
  silence; under option 3 the native object would have been a DSSE envelope and
  could have named its algorithm only in its payload, as E1 does. Algorithm
  binding is SPEC-0002 §6's and DEC-003's (ADR-0005), not the encoding's.
- **Where KSA is stronger** (X-04): it signs the suite (SPEC-0002:350), binds
  each key to one suite (SPEC-0001:204), and forbids registering a suite whose
  key encodings could equal another's, because `kid` does not hash the suite
  (SPEC-0002:831-838).

---

## 6. Cross-check against in-toto-envelope-v1

The in-toto envelope extraction (library#141, branch
`origin/fx1-in-toto-envelope-136` at `23c0d40`, read file by file with `git
show`) profiles DSSE: its source recommends *DSSE v1.0* (in-toto L8)
and links `envelope.md` at the tag `v1.0.2` (in-toto L102; *in-toto
normative.md:251-252*). That record did not read DSSE and labelled every DSSE
fact *mofn's reading of DSSE* (*in-toto design-notes.md:113-117*). This record
holds DSSE, so it can check those readings against the source. Each item gives
in-toto's evidence, then ours; the in-toto record's ids are written as in
Things to hold, item 2.

### 6.1 Shared DSSE facts

| id | the fact | in-toto-envelope-v1 says | DSSE says | verdict | finding |
|---|---|---|---|---|---|
| CC-01 | which DSSE | label v1.0, link v1.0.2 (in-toto L8, in-toto L102; in-toto SD-12, *in-toto normative.md:420-430*); whether the library's DSSE text is v1.0.2 *was not checked* (*in-toto design-notes.md:113-117*) | L6-8 names v1.0.2; four of the five files are byte-identical at the tag and at our pin, and `background.md` differs in three links (Which DSSE this is) | answers | one text behind the link and our pin. No tag is named v1.0. Read as `v1.0.0`, the label names a tag whose proto comment describes another PAE, with no §1.3 and no bytes-identity rule; `v1.0.1` has §1.3 and still no rule. The link names `envelope.md` only; the signing input is defined in `protocol.md` (R-0035, R-0045), which `envelope.md` links (L200, L221) |
| CC-02 | the type is signed | `payloadType` MUST be signed with the payload (in-toto L38); in-toto A-01 (*in-toto design-notes.md:134*) | PAE takes the type (R-0035, R-0036) | agree | DSSE is the mechanism in-toto's rule presumes |
| CC-03 | `keyid` is unauthenticated | its source never says so; the word is DSSE's *in mofn's reading* (in-toto D-01 and in-toto Q-09, *in-toto design-notes.md:240-251, :896-900*) | the table (L28), the definition and its MUST NOT (R-0042, R-0006) and the proto comment (R-0022) | answers | in-toto Q-09 is answered for a DSSE envelope by DSSE's own text, not by mofn's report. For COSE_Sign it stays open |
| CC-04 | several signatures, and what they mean | a format must carry several (in-toto L12); how many must verify is silent, and *in mofn's reading* DSSE leaves the threshold to the application (in-toto S-05 and in-toto Q-03, *in-toto design-notes.md:159, :509-512, :867-869*) | §1.3: `t` of `n` unique trusted keys, `t` the application's (R-0070); a failing signature is skipped (R-0076; R-0109); the empty array has two readings (SD-2) | answers in part | in-toto Q-03 has an answer under the link (v1.0.2) and none under the label (v1.0.0 has no §1.3). DSSE fixes the procedure; what it leaves open is `t`, its bounds (SD-10), key equality (SD-14), a `KEYID` filter that leaves no key or several (SD-15), and which procedure a several-signature envelope gets (SD-9) |
| CC-05 | one envelope or several | DSSE makes them equivalent, so an importer of n signatures loses nothing DSSE recognises (in-toto D-04, *in-toto design-notes.md:295-310*); an intermediary may split or merge (in-toto C-02, *:367-375*) | the equivalence (R-0092) and a threshold counted inside one envelope (R-0070); nothing but type and body is authenticated (R-0105) | agree, qualified | true signature by signature; for `t` ≥ 2 the equivalence and §1.3 disagree (SD-18). Splitting is always possible, merging only over an identical type and body. in-toto's import shape stands (D-02) |
| CC-06 | the payload is present | `payload` SHOULD be included (in-toto L36-37); a detached payload has no rule (in-toto SD-14, *in-toto normative.md:439-447*); its schema leaves `payload` optional in a DSSE envelope (*in-toto schema/envelope.derived.schema.json:86-97*) | `payload` REQUIRED and set (R-0011); the design includes the message (R-0029); detachment is by digest inside it (R-0100) | answers | for a DSSE envelope in-toto SD-14 cannot arise: the payload is always there (A-08). A validator built from in-toto's schema alone accepts a DSSE envelope DSSE rejects |
| CC-07 | the signature element | its schema types `sig` and `keyid` and requires neither, DSSE's rules being outside its source (*in-toto schema/envelope.derived.schema.json:59-66*, x-open :10) | `sig` REQUIRED in each element, read through SD-1 (R-0011; SD-1) | agree on scope | its schema and ours bind different halves of one E2: in-toto's misses DSSE's presence rules, ours in-toto's type and payload rules. E2 is both at once (C-10) |
| CC-08 | the envelope is JSON | never said by its source; inferred from `.json` and the member names (*in-toto messages.yaml:131-133*) | JSON is the one recommended encoding (R-0086, R-0087), others allowed (R-0095) | confirms | in-toto's inference holds; DSSE's permission for other encodings is closed off by in-toto's base64 payload (6.2) |
| CC-09 | base64 | alphabet and padding unstated (in-toto SIL-04, *in-toto messages.yaml:529-533*); its schema takes both alphabets, optional padding, and refuses a mixed string (*in-toto schema/envelope.derived.schema.json:11, :50*) | either alphabet, and a verifier MUST accept either (R-0007); padding and mixing are silences (S-02) | agree | both records' schemas read the silences the same way (ours: `schema/envelope.derived.schema.json` x-open, Base64Text). Both readings are the library's, not DSSE's |
| CC-10 | unknown and duplicated members | DSSE's to define; P5.2 rejects unknown exterior members and, *(inferred)*, does not reach a duplicated `payload` or `payloadType` (in-toto S-06, *in-toto design-notes.md:514-521*) | producers may add, consumers ignore (R-0014, R-0015); duplicates unaddressed (S-01); no re-parse for the payload (R-0009) | agree | the duplicate-member differential in-toto inferred is DSSE's gap too: closed for the payload by DSSE's MUST NOT, open for the type (S-08, SD-19) |
| CC-11 | parse and verify | its consumer rule names parsing before verifying, against its own format criterion (in-toto SD-3, *in-toto normative.md:329-337*; in-toto L54-55, in-toto L16) | the verification steps list verify before parse (R-0063, R-0066), never made binding (C-07) | resolves, weakly | in-toto defers format *and protocol* to DSSE (in-toto L8), so for a DSSE envelope DSSE's order applies, and it is only a list order. Our importer imposes it either way |
| CC-12 | the signing input | the framing, from lane-a's code (lane-a/common.py:72-75), and a first octet `0x44` (in-toto §3.1 and §8 check 3, *in-toto design-notes.md:540, :798-808*) | L64-68 (R-0045); `0x44` at L67 (R-0049) | confirms | lane-a's `pae()` writes LEN with `%d`, so it writes zero as `0`, the reading of R-0104. Their 28-octet generic type gives `LEN(type)` = `28` |
| CC-13 | the algorithm | DSSE restricts neither algorithm nor format *in mofn's reading* (in-toto §6 item 2, *in-toto design-notes.md:723-727*); a format should not need the algorithm in the signature (in-toto L17) | R-0053; nothing names the algorithm (Part 5.1) | confirms | from the source. DSSE meets that format criterion by having no algorithm field at all |
| CC-14 | the format criteria themselves | six ITE-5 criteria (in-toto L12 to in-toto L17) | the design requirements of §4.3 (L363-381) | agree | two are DSSE's words verbatim (in-toto L14 is R-0026; in-toto L16 is R-0028), one adds a gloss (in-toto L15 to R-0033), one rewords (in-toto L12, R-0030), and two have no DSSE line: an authenticated type (in-toto L13; DSSE's nearest, R-0023) and no algorithm in the signature (in-toto L17). DSSE, as a format, meets all six |

### 6.2 Where in-toto narrows DSSE

| what | DSSE | in-toto's profile | finding |
|---|---|---|---|
| `payloadType` | any string; SHOULD be a media type or URI, application-specific, lowercase (R-0001, R-0002, R-0003) | MUST be one of two values (in-toto L45-46), which its general form admits only one of (in-toto SD-1) | E2's type is fixed; E1's is ours (Q-01). The generic value names the Statement schema and leaves the predicate to `_type` and `predicateType` inside the payload (in-toto L46-47, in-toto L52-53): the type stated more than once, the cost §4.5 named in a `_type` design (L469-471). All three are signed, so it costs nothing in security |
| payload | any bytes (R-0037) | a base64-encoded JSON Statement (in-toto L58) | E2 only; E1 is outside in-toto's profile, as a DSSE envelope of another type |
| envelope encoding | JSON recommended, others allowed, none standardised (R-0086, R-0094) | JSON: a base64 payload and a `.json` file (in-toto L58, in-toto L62-63) | the §2.2 path (D-05) does not reach the in-toto world |
| `keyid` | OPTIONAL (R-0012, R-0022) | SHOULD, one per signing key (in-toto L34) | E2 carries one per signature; its spelling is MAP-0002's (Q-04) |
| signature count | MAY be several (R-0091); none, by envelope.md's reading, or at least one, by the proto's (SD-2) | REQUIRED array (in-toto L31-32); a format MUST support several (in-toto L12); no minimum (in-toto SIL-02) | neither fixes a minimum both ways; with `t` ≥ 1, §1.3 rejects an empty array whatever a schema accepts (R-0079) |
| storage media type | none: DSSE names no media type for an envelope, and `+dsse` occurs nowhere in it (Method) | `application/vnd.in-toto.<predicate>+dsse` (in-toto L78-79) | the suffix is in-toto's coinage; whether it is registered DSSE cannot say (in-toto Q-08) |
| file names | none | `.json`, a step name, a truncated KEYID (in-toto L62-63, in-toto L71-74) | storage hints outside every signed byte (in-toto D-02) |

### 6.3 What this changes for MAP-0002

- An E2 envelope must satisfy DSSE and in-toto's profile together; the two
  derived schemas each bind one half (CC-07), so a MAP-0002 check runs both, or
  one schema written for E2 (C-10).
- in-toto Q-03 and in-toto Q-09 have answers for DSSE envelopes (CC-03,
  CC-04), and in-toto D-04 needs SD-18's qualification (CC-05). Those are the
  in-toto record's to take up; nothing here edits it.
- in-toto's ARCH-0001 citations are at `7c3c731`, where ARCH-0001 was v0.3.1;
  ours are at `656bac0`, v0.3.2, and the lines moved by ten: R-I-03 is line 443
  there and 453 here, R-O-05 457 and 467, DEC-005 633-635 and 643-645. A reader
  joining the two records maps by commit.

---

## 7. The pre-FX-1 findings, a source-defect candidate, and open questions

Source defects are normative.md's to number; this file states the questions
they raise and offered one candidate, now normative.md's SD-19. The questions are mapping, decision and
correction questions for their owners (Part 9); this file answers none of them.

### 7.1 The pre-FX-1 notes, re-checked

The notes this file replaces (dated 2026-10-08) are in this repository's history,
last changed in `e5f5387` and unchanged at `212d336` (`git show
212d336:records/community/secure-systems-lab-dsse/distilled/design-notes.md`;
cited throughout as *old design-notes.md*). They made five findings, two of them corrections of the record's earlier summary,
and one minor note. Each was re-checked against the source before it was
carried.

| pre-FX-1 finding | re-checked against | fate | here |
|---|---|---|---|
| 1, CORRECTION: the `(t, n)` envelope carries `n`, not `t` (old design-notes.md:24-65) | L121-139; messages.yaml *(t, n)-ENVELOPE* | carried, amended: it carries neither; `k` and the members travel in the payload; a signature count is unsafe to read as `k` | Part 4.3, C-05, K-03 |
| 2, CORRECTION: DSSE licenses a non-global type (old design-notes.md:67-92) | L34-35, L257-263 | half carried: the type form is a SHOULD. Half dropped: §2.2's coded type is a transmission spelling, and PAE authenticates the full string | Part 2.4, D-03 |
| 3: ignore-unknown collides with P5 (old design-notes.md:94-118) | L252-253 | carried, now accepted as P5.2; an unknown member inside a signature element is added, which P5.2 does not reach | X-01, Q-05 |
| 4: `KEYID` is no principal (old design-notes.md:120-142) | L28, L52-56, L314-317 | carried, now P5.2's `KEYID` row | A-06, S-05 |
| 5: injectivity by framing; condition (1) over the pair (old design-notes.md:144-179) | L64-68, L593; `examples/` injectivity checks | carried; its option-4 hazard is recorded as not a DEC-002 discriminator, option 4 being rejected | Part 3.3, Part 2.5, A-05, A-09 |
| minor: `signature` against `signatures` (old design-notes.md:183-190) | L248-250 | carried, now normative.md's SD-1 | CC-07 |

### 7.2 DN-SD-2, now SD-19 — §1.2 and §2.3: the bytes-identity rule names the payload, not the type

Offered to normative.md's Source defects, and taken in by pass 2 as SD-19,
whose wording there is the canonical one. R-0008
and R-0016 require the bytes the application receives to
be the bytes verified, and R-0009 and R-0017
forbid parsing the envelope again for the payload. No sentence says the
same of PAYLOAD_TYPE, which the application also needs to interpret the body.
An envelope carrying `payloadType` twice, which JSON permits and DSSE does not
address (messages.yaml `source_silences`), lets a verifier check PAE under one
type while an application that reads the envelope again for the type gets the
other: the confusion PAE exists to stop, reopened by a parser differential
(Part 3.2). The requirements lane reads the rule as covering the type
(R-0108, inferred); this candidate records
that the source does not. A gap a verifier must decide, like SD-8 and SD-13.
Requirements affected: R-0008,
R-0009, R-0016, R-0017,
R-0108. (DN-SD-1 is already SD-18.)

### 7.3 Questions

- **Q-01 — E1's type string.** One string for every kind, since `kind` is in
  the TBS. A URI of ours (R-0041, which SHOULD resolve to a description,
  R-0004); a vendor media type (R-0040,
  lowercase, R-0003), which brings the Media Types registry into
  ADR-0004 item 3's boundary list; or a string that departs from the SHOULD,
  such as the DS label's text (Part 2.4, Part 2.5 item 3).
- **Q-02 — the export's signing key.** The speaker's key, against SPEC-0001
  §5.3's SHOULD and with its MUST to record the use (SPEC-0001:226-227), or a
  separate key that nothing published links to the speaker (K-01; in-toto Q-11
  asks the same for E2).
- **Q-03 — PAE as a suite's signing input.** Keep `DS ‖ TBS` and sign every DSSE
  export again, or define a suite whose input is PAE(T, TBS), so that native
  signatures are DSSE signatures and E1 needs no new one (D-05, Part 2.5 item
  2)? DEC-005's and SPEC-0002 §6's question, not DEC-002's.
- **Q-04 — the `keyid` spelling.** A hex kid, lane-a's `SHA256:` plus base64
  (lane-a/02_dsse_intoto.py:58), or none; an importer never reads it as a
  principal either way (A-06, S-05).
- **Q-05 — the importer's exterior rules.** Which of these it rejects as
  documented deviations, P5.2's way: a duplicated member (S-01, SD-19), JSON
  `null`, an unknown member *inside* a signature element (X-01, which P5.2's
  sibling rule does not reach, ARCH-0002:498-499), a mixed alphabet, wrong
  padding or non-zero trailing bits (S-02). Both alphabets it must accept
  (R-0007). And which spelling an export emits: the
  vector's standard, padded base64 is the obvious pin (Part 1.3 item 6).
- **Q-06 — does R-O-05 govern an export?** E1 can meet its first sentence; E2,
  an in-toto Statement, cannot (Part 1.4, Part 3.5 item 3).
- **Q-07 — the bootstrap kinds under DSSE.** `key-publish`, and `self` with a
  key, need `pub` to be verified before decoding (SPEC-0002:315-317); DSSE has
  no place for it and P5.2 forbids adding one. Decode first, require the key out
  of band, or export no bootstrap statement (C-04)?
- **Q-08 — an import's identity and its speaker.** Is an external statement
  keyed on the verifying kid as well as on (type, body), so that two signers of
  one in-toto Statement make two statements (Part 2.2)? And does MAP-0002 put
  the speaker's kid in the Statement (library#134's layer)?
- **Q-09 — which DSSE MAP-0002 cites.** The link's v1.0.2, with the vector at
  L161 as its test, rather than the label's v1.0, which, read as `v1.0.0`, has a proto comment
  describing another PAE (CC-01, Part 1.3 item 8).
- **Q-10 — DEC-005's single unsigned payload schema.** E1's TBS, which meets
  *both* (one TBS, two envelopes), or the in-toto Statement R-I-03 names, which
  does not (C-08, Part 4.1)?
- **Q-11 — the threshold's letters.** MAP-0002 and any R-I-01 table name the
  field `threshold` and the member list `trusts`, never `t`, `k` or `n`, which
  mean different things in DSSE, ARCH-0001 and SPEC-0002 (K-03, Part 4.3).
- **Q-12 — the claims this file corrects, where they still stand.** *Carries
  n*: DL-0006 review:24 and produced.md:68; mofn report R-0006:278, :342,
  :1225; mofn report R-0005:559; `topics/canonical-encoding.yaml:346-347`; this
  record's `summary.md:104` (Part 4.3). *Which PAE authenticates just as well*,
  of a coded type: DL-0006 review:41-45; mofn report R-0006:1233-1239;
  `topics/canonical-encoding.yaml:353-358`; `summary.md:117-118` (Part 2.4).
  The mofn files are read-only here, and the summary and the topic belong to
  other lanes.
- **Q-13 — does an importer ever count DSSE's way?** Verifying each signature
  and counting by SPEC-0004 §6.4 gives one answer however the signatures were
  packed; counting `t` inside one envelope does not (SD-18, Part 4.4). And
  which `t` does a verifier use that has set none (SD-9)?
- **Q-14 — the ML-DSA context of an exported DSSE signature.** Empty, or KSA's
  label text, and stated where (Part 5.3 item 2)?
- **Q-15 — suite 2.** The source's one vector and the real provenance lane-a
  verifies are ECDSA P-256 (Part 5.2), which SPEC-0002 reserves and has not
  specified (SPEC-0002:360). Is suite 2 owed before T-052 (in-toto Q-15 asks
  the same)?
- **Q-16 — `bears_on`.** P5 and P5.2 were reasoned from this source (DL-0013
  review:85-92) and Part 3 bears on them; record.yaml lists neither, and is not
  this lane's to edit.

---

## 8. Method

- **Ids.** Every id cited in this file (not the six range bounds of Things to hold,
  item 2, which describe the layout) was written as a selector, a line range and a
  fragment of the entry's own text (an empty range for an inferred entry, a
  leading `^` anchoring the fragment at the start of the entry's text where one
  entry's text lies inside another's on the same lines, as R-0092's
  does in R-0010's), and resolved by script
  against `requirements.yaml` (110 entries) and `inferred-candidates.yaml` (153),
  each read with both `bin/_yaml.py` and `bin/_record_yaml.py`, which agree on
  every key of every entry. A selector matching no entry or two stops the build,
  and so does a candidate selector that lands on a promoted candidate, so no
  `C-NNNN` is cited where an R-id exists. This file makes 310 id citations of 103 distinct ids (recounted by pass 2: 307
  from the pass-1 build, and three pass 2 added to row S-01 by the same kind of
  selector); every resolved pair, the
  id beside its full text, was printed and read. The in-toto lines were resolved
  the same way against that record's `requirements.yaml` (50 entries, both
  readers agreeing): 32 citations of 19 distinct in-toto lines by selector, and four
  by hand, counted by pass 2: in CC-01 the label line and the link definition
  (in-toto L8, in-toto L102), the same link definition in Part 6's opening, and in Part
  4.1 in-toto L23-24, which carries two requirements, where in-toto L102 carries
  none:
  36 citations of 21 distinct lines in the rows and Parts 1 to 7.
- **Quotations.** 22 markers, each rendered by
  `bin/check-quotes --render --only` on this file and checked by
  `bin/check-quotes`, which reports how many it examined. 14 foreign quotations, each
  checked, whitespace collapsed, against its own document only: the minute, the
  DL-0006 review, mofn report R-0006, ARCH-0001 (one, added by pass 2) and this record's pre-FX-1
  notes (at `212d336`, Part 7.1).
- **mofn citations.** Every `DOC:n` range was printed back from its blob at
  `656bac0` by script and read beside its claim; so were the library citations
  (`topics/canonical-encoding.yaml`, the `rfc-9964` design notes, this record's
  `summary.md` lines, located by grep for the claims Q-12 lists and not read as
  a source) and the in-toto file lines at `23c0d40`.
- **Which DSSE.** The GitHub API, read 2026-11-22: the tags (`v0.1.0`
  `55b006c`, `v1.0.0` `cacf247`, `v1.0.1` `fba27e4`, `v1.0.2` `4409013`; `v0.1.0` added
  by pass 2, which re-read the tags, the comparison and the files the same day), the comparison of `v1.0.2`
  with `1d3370f` (21 ahead, 0 behind; changed: `MAINTAINERS.md`, `README.md`,
  `background.md` and six new files under `governance/`), and the
  specification files at the tags (all five at `v1.0.0` and `v1.0.2`;
  `protocol.md`, `envelope.md` and `envelope.proto` at `v1.0.1`), hashed against
  `render-source.py`'s pins and diffed. At `v1.0.2` four files equal the pins
  and `background.md` differs in three link targets; `v1.0.1`'s
  `envelope.proto` equals the pin too.
- **lane-a's base64.** A seeded sweep (`random.Random(152)`, 200 byte strings at
  each length from 1 to 96 octets, Python 3.14.7) through
  `base64.b64decode`, lane-a's call: of 19,200 strings, 4,590 spell the same in
  both alphabets; of the other 14,610, 9,230 raised and 5,380 decoded to other
  bytes without error, and none to the right ones. The rule *raises unless the
  alphabet characters left after dropping `-` and `_` make a length the padding
  completes* predicted all 14,610 outcomes. The L179 `sig` re-spelled URL-safe
  has two `-` and decodes to 63 octets; `base64.urlsafe_b64decode` takes either
  spelling to the same 64.
- **Arithmetic.** The PAE table was built from L149 and L155 and asserted equal
  to L161 before it was written; its sha256 is of those 54 octets. Base64
  lengths are 4·⌈n/3⌉: 64 → 88, 3309 → 4412. `application/vnd.in-toto+json` is
  28 octets.
- **The silences Part 6 and Part 5 rest on.** A case-insensitive search of the
  rendering: `+dsse`, `.json`, `file name` and `filename` occur nowhere; *media
  type* only at L37, as a form of PAYLOAD_TYPE. Algorithm names occur only in
  the §1.4 vector (L167), in background's remarks on PASETO and ed25519ctx
  (L353, L449, and the ed25519ctx link target at L490) and in the notebook,
  under no rule: its code (L617-634, L668, L754) and the `sha256` digests of
  its link files (L570, L581, L587); *context* only for how a
  payload is interpreted (L407, L519, L533, L535) and for JSON-LD (L470), never
  for a signature; and no length limit is set outside the notebook's code.
- **Rows.** Counted by script from the table's id column. `reproduce.py` was run
  in this pass (`reproduce: ok`).
- **What has no id.** A line is cited bare where no requirement carries it:
  the vector (L149, L155, L161, L167-171, L177-179), the notebook, and
  background's motivation and rationale, whose candidates were rejected and are
  cited by `C-NNNN` only where a row rests on one.

---

## 9. What this file decides

Nothing. No DEC-* is opened, ranked, accepted or reopened: DEC-005 stays open,
and ADR-0004 stands as accepted. Where DSSE cuts against MD-3 and option 5
(Part 2.5, Part 3.5, Part 5.4), the finding is evidence for ADR-0004's owed
second reader and for whoever takes DEC-005, and the option it names is named,
not proposed. No mofn file, no in-toto file and no other file of this record was
edited; the claims this file corrects elsewhere are listed for their owners
(Q-12), and the source-defect candidate it offered, DN-SD-2, is normative.md's SD-19.
The questions belong to their owners: Q-01, Q-03 and Q-10 to DEC-005 and
SPEC-0002 §6; Q-02, Q-04, Q-05, Q-07, Q-08, Q-09, Q-11 and Q-13 to T-051 and
MAP-0002; Q-06 to R-O-05's owner, ARCH-0001; Q-14 and Q-15 to SPEC-0002 §6;
Q-12 to the owners of the files it lists; Q-16 to this record's owner.

---
record: in-toto-envelope-v1
kind: design-notes
title: "in-toto-envelope-v1 — bearing on our design"
extracted: "2026-11-16"
reviewed_by: ""
---

# in-toto Attestation Framework v1, Envelope layer — bearing on our design

The source is `spec/v1/envelope.md` of the in-toto Attestation Framework at
commit `50bf017` (record.yaml:11-14), 110 lines of Markdown. Its sha256
`c02c65880ccc117bbdecc6c916d5108541c1a864de67f8f9082efbaf15265d11` equals
`content.sha256` (record.yaml:15) and the digest `distilled/render-source.py`
pins, and was recomputed from `.cache/in-toto-envelope-v1.bin` in this pass
(retrieved 2026-11-03, record.yaml:16). The FX-1 tools read the rendering
`.cache/in-toto-envelope-v1.txt` (sha256
`d4bdf93f92f2d654a430896374bdc94c53a15576ffab44d3603e5ebd61659f42`, equal to
`requirements.yaml`'s `source_digest`): line N is line N of the Markdown and
only the ATX headings are renumbered (§1 Schema, §1.1 Alternative Envelope
schemas, §2 Fields, §3 File naming convention, §4 Storage convention, §4.1
Examples). `bin/bcp14-count` finds 30 keywords; `bin/fx1-skeleton` wrote the 29
sentences carrying them as `in-toto-envelope-v1#R-0001` to `R-0029`, the only
requirement ids pass 1 of this file cited; pass 2 wired the ids the requirements
lane gave the keyword-less sentences (R-0030 to R-0042) and the inferred R-0045
where a row rests on them (§10).

The source names DSSE v1.0.2 as the RECOMMENDED envelope and lists six
properties (ITE-5) for any other format, one a MUST, three SHOULDs and two
SHOULD NOTs (its §1); names one format it calls compliant, COSE_Sign, and two that do not, the Sigstore Bundle and
COSE_Sign1 (its §1.1); states the field rules every in-toto envelope follows
and the two `payloadType` values DSSE may carry (its §2); and gives a
file-naming convention (its §3) and a storage media type (its §4). **It does
not define** a signing input (DSSE does), a key format, key discovery, an
algorithm, what several signatures mean to a verifier, validity, revocation or
time.

It reaches us in four ways.

1. **DEC-005**, open (ARCH-0001:71-73, :633-635). ADR-0004 made COSE_Sign1 and
   DSSE export envelopes only and left the choice between them to DEC-005
   (ADR-0004:51-52). §1.1 of the source says which COSE structure the in-toto
   world accepts, and it is not the one DEC-005 lists (C-03, §4).
2. **R-I-03** (ARCH-0001:443) and **T-051**, `MAP-0002` in-toto Statement ↔
   `ArtifactStatement` (BACKLOG-0001:188). An export needs this layer to fix
   what is signed; §3.1 says what it fixes and what it leaves to DSSE and to
   the Statement layer.
3. **R-O-05** (ARCH-0001:457). The source agrees with the authenticated-type
   half of its first clause and with its second (A-01, A-02), is weaker on the
   order of verification (C-01, §5), and makes the rest of its first clause,
   the canonical encoding verbatim, unmeetable for an in-toto export (K-01).
4. **MD-3 and ADR-0004** (DEC-002, option 5). §3 gives the field-by-field
   mapping and where the source cuts against option 5.

And **T-053** (BACKLOG-0001:190; R-I-01): §7 lists what the envelope layer
preserves, drops and infers.

What it is not: the Statement layer. `_type`, `subject`, `predicateType` and
`predicate` are defined in `statement.md` (L106), which the library holds as
`in-toto-attestation-v1` (library#134) and which was not read for this file.
The in-toto row's existing losses (a `description` subject, `predicateType` ↔
`type-ref`, ARCH-0001:496) belong there.

## Things to hold while reading

1. **Our decisions are read from m-of-n at `7c3c731`**
   (`7c3c73165197e9c63152a65ba51345d65a268b89`, HEAD, committed 2026-11-15),
   with `git -C /Users/nfn/Projects/mofn show 7c3c731:<path>`, never the
   working tree. A citation `DOC:n` or `DOC:n-m` is a line range of that blob;
   a bare `:n` continues the document just named. **No mofn text is quoted**:
   every citation is a paraphrase, except §3.3's clause column, which names
   MD-3's clauses in the minute's own words, and §10 says how each cited range was read
   back beside its claim.

   | name | path at 7c3c731 | standing |
   |---|---|---|
   | ARCH-0001 v0.3.1 | `spec/ARCH-0001-authorization-attestation.md` | draft. R-I-03 :443, R-O-05 :457, §6 matrix :486-505. **DEC-005 open** (:71-73, :633-635) |
   | ARCH-0002 v0.10.0 | `spec/ARCH-0002-key-relative-naming.md` | P1 accepted (ADR-0001); P5 with P5.1 and P5.2 accepted (ADR-0002); P1.1 draft (ARCH-0002:54-57) |
   | ADR-0002 1.0.0 | `spec/ADR-0002-provisional-principles.md` | accepted |
   | ADR-0003 1.0.1 | `spec/ADR-0003-ksa-core-decisions.md` | accepted; D1 type identity, D2 one canonical encoding |
   | ADR-0004 1.0.0 | `spec/ADR-0004-dec-002-encoding.md` | **accepted 2026-10-25, `reviewed: false`**: DEC-002 is option 5; COSE_Sign1 and DSSE export envelopes only; DEC-005 not decided (:51-52, :112) |
   | SPEC-0001 0.1.0, SPEC-0002 0.10.1, SPEC-0004 0.6.2 | `spec/SPEC-000{1,2,4}-*.md` | draft; govern where an ARCH document differs (ADR-0003) |
   | MD-3 | `project/meetings/2026-09-28.md` | the 2026-09-28 narrowing, closed by ADR-0004's acceptance (ADR-0004:132-133) |
   | DECISIONS-0001 0.7.1, BACKLOG-0001 0.15.1, PLAN-0001 0.7.1, PLAN-0003 0.1.0 | `project/…` | register, backlog, plans. T-051…T-053 BACKLOG-0001:188-190; L-041 :267 |
   | DL-0006, DL-0013, DL-0047 | `design-log/0006-…`, `0013-p5-serialisation-clause/`, `0047-…` | design log. DL-0047 opened library#136 for this record |
   | mofn report R-0006 v0.3.0 | `research/0006-mechanism/report.md` | draft, evidence only, pinned `library@60b3284` |
   | mofn survey R-0001 v0.2.0 | `research/0001-signatures-and-attestation/report.md`, `mini-reports/H-post-quantum.md` | draft |
   | lane-a | `prototype/lane-a/` | a throwaway that decides nothing (lane-a/README.md:3); the only mofn code that builds DSSE envelopes (§8 check 10) |

   **`docs/extraction.md` is stale on one point**: it says no DEC-002 ADR
   exists (docs/extraction.md:128-131). At `7c3c731` ADR-0004 accepts DEC-002
   for option 5. This file maps against ADR-0004 and still records where the
   source cuts against option 5, as docs/extraction.md:133-135 asks.

2. **Numbering.** A bare `R-NNNN` is `in-toto-envelope-v1#R-NNNN`. mofn's
   research reports are never bare: *mofn report R-0006* and *mofn survey
   R-0001*. `R-M-`, `R-I-`, `R-O-` ids are ARCH-0001 §5; P1, P1.1, P5, P5.1,
   P5.2 are ARCH-0002; V1…V9 are SPEC-0002 §9.2; conditions (1)…(6) are mofn
   report R-0006 §3.2. Row ids: `A` adopt, `D` adapt, `X` reject, `C`
   constrains, `K` conflicts, `S` silent; `Q-nn` open questions. Three pairs of
   requirements share identical text across the source's §2 and §4
   (R-0017/R-0027, R-0018/R-0028, R-0019/R-0029,
   `bin/check-id-joins --surface`); every id here was emitted by script from a
   line-range selector, never typed (§10). **Section signs:** a bare §n in
   running text is a section of this file; a section of the source is written
   *the source's §n* (or *its §n*) or carries a line locator, as in §2 L38; a
   mofn section always names its document.

3. **Quotation.** No word of the source is typed here. A quotation is a
   `<!-- q Lx-y -->` marker whose blockquote `bin/check-quotes --render` wrote;
   it shows the source's Markdown as written, link labels in brackets and
   backticks included. Elsewhere the source is cited by line and paraphrased.
   **DSSE is not this source.** A fact about DSSE is labelled *mofn's reading
   of DSSE* and cited where mofn records it; the library holds DSSE at commit
   `1d3370f` (secure-systems-lab-dsse/record.yaml:14), this source names the
   tag `v1.0.2` (L102), and whether the two texts agree was not checked. RFC
   9052 facts are stated with their section, outside this source, unquoted.

4. **Labels.** *(inferred)* marks a consequence the source does not state.
   Nothing here is a proposal for mofn unless it says so; §11 says what this
   file decides, which is nothing.

---

## 1. Rows by verdict

27 rows: **5 adopt, 4 adapt, 3 reject, 7 constrains, 2 conflicts, 6 silent.**
*Adopt (confirms)* means the source does what an accepted decision of ours
already does; it is evidence, not a new commitment. *Reject (native)* means the
native model declines the source's mechanism; nothing stops it at the boundary.

| id | verdict | in the source | where | ids | maps to | finding |
|---|---|---|---|---|---|---|
| A-01 | adopt (confirms) | `payloadType` is signed together with the payload; ITE-5 asks only that a format should authenticate a type | §2 L38; §1 L13 | R-0013, R-0004 | R-O-05 (ARCH-0001:457); condition (4) (mofn report R-0006:391-392, :428-432); SPEC-0002 §6.4 (:397-404) | the authenticated type indicator R-O-05 asks for. Here it is transmitted and takes one of two values; in KSA it is a DS label, fixed per object class and never transmitted. the source's §2 turns the ITE-5 SHOULD into a MUST for every in-toto envelope |
| A-02 | adopt (confirms) | no security dependence on canonicalisation; no parsing before verification | §1 L14, L16 | R-0005, R-0007 | R-O-05; SPEC-0002 §3 (:195-205), §4.3 (:264-266), §13.1 (:890-893); ADR-0003:53-58; PLAN-0001:378-382 | KSA's signature path meets both. Both are SHOULDs on a format, weaker than R-O-05's SHALLs on our verifier (C-01) |
| A-03 | adopt | the media type is no reliable sign of predicate type; `predicateType` is; authenticated predicate information comes from the verified payload | §2 L51-55; §4 L84-88 | R-0017, R-0018, R-0019, R-0027, R-0028, R-0029 | R-O-05's last sentence; P1.1 (ARCH-0002:89-119); SPEC-0002 §7.2 (:479-486) | the source denies its own registry-shaped names any authority over type, P1.1's stance on foreign identifiers. An import's human form comes from the verified Statement, never from a media type or a file name |
| A-04 | adopt (confirms) | DSSE is RECOMMENDED; COSE_Sign1 is not an in-toto envelope | §1 L8; §1.1 L23-24 | R-0001, R-0033 | R-I-03 (ARCH-0001:443); §6 rows (:496-498) | R-I-03 pairs in-toto with DSSE and COSE_Sign1 with CWT claims. It never pairs in-toto with COSE_Sign1, the pairing the source excludes |
| A-05 | adopt (confirms) | the envelope is the attestation's outer layer and the Statement sits inside it | L3-4 (no id); §2 L36-37 | R-0012 | ARCH-0001 §3.3 (:294); §6 DSSE row (:497); mofn report R-0006 §2.1 (:180-185) | the framework keeps envelope and statement apart, as ARCH-0001 keeps the envelope out of the information model. L3-4 also gives the envelope serialisation, the fusion mofn report R-0006:189-197 names |
| D-01 | adapt | a hint naming the signing key, one per key, which a format may nest in the signature array | §1 L15; §2 L34-35 | R-0006, R-0010, R-0011 | P5.2 (ARCH-0002:525-530); P1.1 (:117-119); SPEC-0002 §5 (:308), §9.2 (:698); mofn report R-0006:1268-1274 | KSA's envelope `says` is also a hint, but V6 checks it against the signed `says`; nothing checks a `keyid`. An export may carry the kid there as a hint; the principal travels in the payload. The source never says a `keyid` is unauthenticated (Q-09) |
| D-02 | adapt | file names: a `.json` suffix, a step name, an agreed name, a truncated KEYID | §3 L62-74 | R-0021, R-0022, R-0023, R-0024 | SPEC-0001 §6.2 (:257); SPEC-0002 §3 (:209-210), §4.5 (:292-294), §7.2 (:479-486), §13.4 (:914-916) | a storage hint, never identity. `<keyid[0:8]>` from a hex kid takes 2^32 values; from lane-a's spelling it takes 64, and the chance that some two of ten functionaries share one is 0.52 (§8 check 4) |
| D-03 | adapt | DSSE's `payloadType` is the predicate-specific or the generic in-toto media type | §2 L39-50 | R-0015, R-0016, R-0014 | R-O-05; P1 (ARCH-0002:65-87); ADR-0004 item 3 (:46-50); T-051 | the choice is part of the signed bytes: the predicate-specific form for SLSA provenance makes them 11 octets longer (§8 check 2). A KSA-defined type has only the generic form, which is also the only value R-0014 and R-0015 both admit when read literally (Q-01) |
| D-04 | adapt | several signatures over one payload | §1 L12; §2 L31-32 | R-0003, R-0009 | SPEC-0004 §6.4 (:423-431); SPEC-0001 §5.3 (:229-232); DL-0006 review:20-24 | *(inferred)* on import, n verified signatures become n external statements with one target, type and value, the shape SPEC-0004 §6.4 counts; in mofn's reading of DSSE nothing is lost, since DSSE declares the two equivalent |
| X-01 | reject (native) | a format must carry several signatures in one envelope | §1 L12 | R-0003 | SPEC-0002:56-57, :302, :696, :698; P2; mofn report R-0006:347 | the KSA envelope carries one `sig` over a TBS naming one speaker, so it cannot meet R-0003 and is never an ITE-5 envelope. ADR-0004:51-52 puts DSSE and COSE at the boundary, so nothing depends on it |
| X-02 | reject (native) | a format should not need the signing algorithm inside the signature | §1 L17 | R-0008 | SPEC-0002 §6.1 (:350), §5 (:307); SPEC-0001 §5.1 (:204); mofn survey R-0001:1597-1608; H-post-quantum.md:82 | KSA holds both the premise R-0008 rests on (a key belongs to one suite) and a signed suite. mofn's survey calls R-0008 a defect; the source argues neither way. The export loses the signed suite (§7) |
| X-03 | reject (native) | media types whose middle segment is a file name in in-toto's predicates directory | §2 L45-50; §4 L78-83, L92-96 | R-0015, R-0016, R-0025, R-0026 | P1 (ARCH-0002:65-87); ADR-0003 D1 (:47); ADR-0004 item 3 (:46-50) | two global namespaces, the media-type tree and one repository's file list. Natively excluded; *(inferred)* at the boundary they join ADR-0004 item 3's list, and A-03 means what is lost there is a hint |
| C-01 | constrains | the format-level order rule is a SHOULD NOT, and the consumer rule names parsing before verifying | §1 L16; §2 L54-55; §4 L87-88 | R-0007, R-0019, R-0029 | R-O-05; SPEC-0002 §9.2 (:688-701); lane-a/03_slsa_provenance.py:93-94, :119-123 | a format may still require parse-then-verify, and a parse-first consumer conforms; R-O-05's order has to be imposed by our importer. mofn's own lane-a sample 3 parses first and checks only `signatures[0]` (§5) |
| C-02 | constrains | several signatures, and no threshold | §1 L12; §2 L31-32 | R-0003, R-0009 | R-M-06 (ARCH-0001:429); SPEC-0002 §8.6 (:606-609); SPEC-0004 §6.4; mofn report R-0006:1225-1231 | a threshold `trust` cannot be exported as a signature count; `k` and the members travel in the payload, as mofn report R-0006 §5.1 concluded for DSSE |
| C-03 | constrains | COSE_Sign meets ITE-5; COSE_Sign1 does not | §1.1 L23-24, L101 | R-0032, R-0033 | DEC-005 (ARCH-0001:633-635); R-I-03; ARCH-0001 §3.2 (:281-283); P5.2 (ARCH-0002:522-523) | in the in-toto world DEC-005's COSE option is **COSE_Sign**, which DEC-005 does not list. The link is to RFC 8152, obsoleted (rfc-8152/record.yaml:21). *(inferred)* No one envelope among DSSE, COSE_Sign1 and COSE_Sign serves both the in-toto mapping and the SCITT row (§4) |
| C-04 | constrains | no canonical form; signatures over the exact payload bytes | §1 L14; §2 L58 | R-0005, R-0020 | SPEC-0001 §5.3 (:229-232), §6.2 (:257); SPEC-0002 §5 (:319-321); PLAN-0001:487; PLAN-0003:48 | an import keeps the payload, `payloadType` and signatures as received; re-serialising breaks the signature. *(inferred)* the I4 demo's round trip of a real SLSA attestation is byte-exact only by carrying those bytes |
| C-05 | constrains | the Sigstore Bundle does not meet ITE-5 | §1.1 L21-22, L98 | R-0030 | T-052 (BACKLOG-0001:189); PLAN-0001:487; lane-a/03_slsa_provenance.py:13, :152-153 | the real attestations T-052 and the I4 demo would import arrive in Sigstore bundles; the importer takes a one-signature DSSE envelope out of a container the source calls non-compliant (Q-06) |
| C-06 | constrains | the algorithm comes from outside the signature | §1 L17; §2 L32-33 | R-0008, R-0037 | R-O-01 (ARCH-0001:453); SPEC-0002 §4.5 (:288), §6.2 (:360), §12.4 (:845); lane-a/03_slsa_provenance.py:121-123 | lane-a verifies real provenance as ECDSA with SHA-256; KSA has no ECDSA suite, so *(inferred)* the signer has no kid, and R-O-01 cannot name it, if R-O-01 reaches imports, until suite 2 is specified |
| C-07 | constrains | each field rule admits an equivalent field, and any ITE-5 format may be used | §1 L9-10; §2 L31-40 | R-0002, R-0009, R-0010, R-0012, R-0013 | R-I-01 (ARCH-0001:441); ADR-0002:180; P5.2 acceptance test (ARCH-0002:532-535) | at the envelope layer in-toto is not one format, so an R-I-01 table for it is one block per envelope format; P5.2's owed rows are DSSE's |
| K-01 | conflicts | in DSSE the payload is a base64 JSON Statement and `payloadType` is in-toto's | §2 L45-46, L58 | R-0015, R-0020 | R-O-05's first sentence (ARCH-0001:457); §6 DSSE row (:497); ARCH-0001 §3.3 (:294) | an in-toto DSSE export cannot sign the canonical encoding verbatim: it signs a JSON Statement, a second object with its own bytes and digest. Not a DEC-002 discriminator, except against option 3 (§3.4) |
| K-02 | conflicts | each format signs its own input (PAE, under DSSE) | §1 L8; §2 L38 | R-0001, R-0013 | R-I-03; SPEC-0001 §5.3 (:221-227); SPEC-0002 §6.3 (:372-374), §13.2 (:897-901) | the native signature never verifies as a DSSE one (§8 check 3), so an export signs again: with the speaker's key, against SPEC-0001's SHOULD, or with a key nothing in KSA links to the speaker (Q-11) |
| S-01 | silent | the signing input | §1 L8-10; §2 L32-33; L102 | R-0001, R-0002, R-0037 | T-051; lane-a/common.py:72-75 | DSSE defines it; this source fixes only what goes into it (§3.1). The reference's label says v1.0 and its URL pins v1.0.2 |
| S-02 | silent | where keys and their algorithms come from; who may sign | §1 L15; §2 L54-55 | R-0006, R-0019 | R-I-02 (ARCH-0001:442); SPEC-0002 V3 (:695); SPEC-0004 §4 | verifying against the signatures presumes keys; the source offers a hint and nothing else |
| S-03 | silent | post-quantum: no algorithm, size, context string or hybrid rule | §1 L17; §2 L32-33 | R-0008, R-0037 | SPEC-0002 §6.4-§6.5 (:406-422); SPEC-0001 §5.2 (:214-217); SPEC-0004 (:431); mofn survey R-0001:1604-1608 | an ML-DSA-65 signature fits; the context string a DSSE ML-DSA signature uses is unspecified (§6) |
| S-04 | silent | validity, revocation, time | — | — | SPEC-0002 §7.3 (:491-501), §8.7 (:621-627); SPEC-0001 §5.2 (:215-217) | nothing at this layer; a native `revoke` names a digest the export does not share (§7) |
| S-05 | silent | what several signatures mean to a verifier: all, any, or k; none at all; one failing among good ones | §1 L12; §2 L31-32, L54-55 | R-0003, R-0009, R-0019, R-0045 | SPEC-0004 §6.4; mofn report R-0006:238 | policy, out of band (Q-03) |
| S-06 | silent | envelope serialisation: duplicate members, base64 alphabet and padding, unknown fields | §2 L58 | R-0020 | P5.2 (ARCH-0002:498-510); SPEC-0002 §13.6 (:928) | DSSE's, not this source's; P5.2 covers unknown exterior fields and *(inferred)* nothing else of these |

---

## 2. Row details

### 2.1 Adopt

**A-01 — the payload type is inside the signature.**

<!-- q L38 "`payloadType`" .. "`payload`." -->
> `payloadType` (or equivalent) MUST be signed along with the `payload`.

The ITE-5 list asks only that a format SHOULD authenticate a payload type
(R-0004). The source's §2 rules apply to an Envelope as such (L28-29, R-0034), whatever
its format, so for in-toto the SHOULD becomes a MUST. That is the
authenticated-type requirement of R-O-05's first clause, and condition (4) (mofn report R-0006:391-392), which that report made
load-bearing after the polyglot attack in the notebook attached to DSSE
(:422-432). The difference is where the indicator lives: here it travels in the
envelope and takes one of two values (D-03); in KSA it is a DS label, fixed per
object class and never transmitted (SPEC-0002:397-404). §8 check 1 shows the
type inside the bytes lane-a signed.

**A-02 — canonicalisation and parsing stay out of verification.**

<!-- q L14 "SHOULD avoid" .. "security" -->
> SHOULD avoid depending on canonicalization for security

<!-- q L16 "SHOULD NOT" .. "verifying" -->
> SHOULD NOT require the verifier to parse the payload before verifying

These restate, as properties of a format, the DSSE critique R-O-05 was proposed
to stay clear of (PLAN-0001:378-382). KSA's signature path meets both: V4
checks the received TBS before V5 decodes it (SPEC-0002:696-697), the verifier
never re-encodes, and a non-canonical TBS is rejected rather than repaired
(:203-205, :264-266, :890-893; ADR-0003:53-58). Both are SHOULDs that bind a
format, where R-O-05's SHALLs bind our verifier (C-01).

**A-03 — the media type hints; the Statement decides.**

<!-- q L51-53 "Consumers SHOULD NOT" .. "layer." -->
> Consumers SHOULD NOT rely upon the media type for individual attestations as faithful indicators of predicate type. Consumer SHOULD only rely on the `predicateType` field in the [Statement] layer.

<!-- q L54-55 "To obtain" .. "`signatures`." -->
> To obtain predicate information that is authenticated, consumers MUST parse the Envelope's `payload`, and verify it against its `signatures`.

The source's §4 repeats all three sentences for the storage media type (R-0027,
R-0028, R-0029). The source denies its own registry-shaped name any authority
over type: the stance P1.1 takes on a foreign `kid` (ARCH-0002:117-119) and
SPEC-0002 takes on a locator, evidence and never the thing (SPEC-0002:479-486).
For an import it fixes where the human form comes from. R-O-05's last sentence
requires that form to be regenerated from verified bytes, and here the verified
bytes are the payload, not `payloadType`, a storage label or a file name.

**A-04 — R-I-03's pairing is the source's.**

<!-- q L23-24 "The [COSE_Sign]" .. "NOT compliant." -->
> The [COSE_Sign] structure is [ITE-5] compliant, whereas the `COSE_Sign1` format that supports only one signer is NOT compliant.

DSSE is the RECOMMENDED format (R-0001). R-I-03 pairs an in-toto Statement with
DSSE and COSE_Sign1 with CWT claims (ARCH-0001:443), and the §6 matrix keeps
those rows apart (:496-498). It never pairs in-toto with COSE_Sign1, which is
the pairing the source excludes. DEC-005 does list COSE_Sign1; C-03 takes the
consequence.

**A-05 — the envelope wraps a Statement.** L3-4 (no id) makes the envelope the
attestation's outer layer and R-0012 puts the Statement inside it. That is
ARCH-0001's layering: the envelope is interchange, not the information model
(ARCH-0001:294), and the §6 DSSE row is wire only (:497). L3-4 also hands the
envelope the serialisation, the fusion of envelope and encoding that mofn
report R-0006 found in DSSE and found undone by PAE's length-prefixed framing
(mofn report R-0006:189-197).

### 2.2 Adapt

**D-01 — `keyid` is a hint; the principal is in the payload.**

<!-- q L34-35 "A `keyid`" .. "array." -->
> A `keyid` (or equivalent) SHOULD be included for each signing key used. The envelope schema MAY nest this field within the signature array.

R-0006 calls it a hint, and the source says nothing more: never that it is
unauthenticated, never what it is computed from. KSA's envelope `says` is a
hint too (SPEC-0002:308), but V6 checks it against the signed `says` inside the
TBS (:698); nothing checks a DSSE `keyid`. P5.2 already holds the rule this
needs, that the principal travels in the payload and never in
`signatures[].keyid` (ARCH-0002:525-530), and P1.1 lets an export put the KSA
kid in a COSE `kid` as a hint (:117-119). lane-a's sample puts Bob's kid in
`keyid` as `SHA256:` plus its base64 (lane-a/02_dsse_intoto.py:56-58; the seed
is Bob's, SPEC-0002 Appendix A) and carries no kid in the Statement at all
(lane-a/02_dsse_intoto.py:26-48), the shape P5.2 forbids relying on. The
spelling a mapping uses is open (Q-04); the word unauthenticated is DSSE's, in
mofn's reading (mofn report R-0006:1268-1274), not the in-toto layer's (Q-09).

**D-02 — file names are storage hints.**

<!-- q L71-74 "If multiple" .. "`<step/env-name>.<keyid[0:8]>.json`." -->
> If multiple Envelopes are produced for the same step by different [functionaries] uniquely identified by a public key, an Envelope name SHOULD include the truncated [KEYID] of the public key `<keyid[0:8]>` of the signing functionary: `<step/env-name>.<keyid[0:8]>.json`.

A wallet keeps every statement as its exact envelope bytes (SPEC-0001:257) and
refers to it by the SHA-256 of its TBS (SPEC-0002:209-210). A name the producer
and consumer agree on (R-0023) is a locator, the kind of name SPEC-0002
withdrew as a target because what it names can change (:479-486). So the
convention serves exported files and never identity. The truncation is allowed
where it is used: SPEC-0002 forbids truncating identifiers in signed or hashed
bytes (:914-916) and lets a transport abbreviate them (:292-294); a file name
is neither signed nor hashed. What it yields depends on a spelling the source
does not fix (Q-04). From a hex kid, `<keyid[0:8]>` takes 2^32 values. From
lane-a's spelling it takes 64, because seven of its eight characters are the
`SHA256:` prefix, and the chance that some two of ten functionaries share one
is 0.52 (§8 check 4). That spelling also puts a colon in the name, which
Windows file names do not allow, and one time in 64 a `/`.

**D-03 — choosing `payloadType` is choosing signed bytes.**

<!-- q L45-48 "`payloadType` MUST" .. "requirements apply:" -->
> `payloadType` MUST be set to `application/vnd.in-toto.<predicate>+json` or to `application/vnd.in-toto+json`. This indicates that the Envelope contains a JSON object with a `_type` field specifying its schema. If the predicate-specific media type is used, the following requirements apply:

<!-- q L49-50 "`<predicate>` MUST" .. "extension." -->
> `<predicate>` MUST match the [predicate specification filename] without the file extension.

Against the source's general rule for every envelope (§2 L39-40):

<!-- q L39-40 "It MUST" .. "format." -->
> It MUST take the form `application/vnd.in-toto+<encoding>` to indicate an in-toto [Statement] payload and its serialized `<encoding>` format.

For a mapping this is not a label: `payloadType` is inside the signed bytes
(A-01), and the predicate-specific form for SLSA provenance makes them 11
octets longer than the generic form (§8 check 2), so the two are different
signatures over one Statement. *(inferred)* A KSA-defined type is not an
in-toto predicate specification (a `type-ref` is a definition hash and a label,
SPEC-0002:506), so it has only the generic form. The generic form is also the
only value both R-0014 and R-0015 admit when read literally (§8 check 6, Q-01).
The SLSA, SPDX and VSA predicates do have in-toto names (L92-96), so MAP-0002
decides per predicate, and whichever it picks is signed.

**D-04 — co-signatures become separate statements.**

<!-- q L12 "MUST support" .. "envelope" -->
> MUST support the inclusion of multiple signatures in a single envelope

KSA has no co-signature: a statement is made by one key about one target
(SPEC-0002:56-57) and its envelope carries one `sig` (:302). Its threshold is
met by n distinct members each having made a statement with the same target,
type and value (SPEC-0004:423-427). *(inferred)* An importer that turns an
envelope's n verified signatures into n external statements over one payload
(SPEC-0001:229-232) produces exactly that shape, and loses nothing DSSE itself
recognises: in mofn's reading of DSSE, a multi-signature envelope is equivalent
to separate one-signature envelopes (DL-0006 review:20-24; mofn report
R-0006:1221-1223). Whether such external statements count toward a native
threshold is an import-profile question under R-I-02 (ARCH-0001:442), not
answered here.

### 2.3 Reject (native)

**X-01 — several signatures in one envelope.** (L12, quoted under D-04.) The
KSA envelope cannot meet R-0003: it carries one `sig` (SPEC-0002:302), and a
second key's signature over a TBS that names another speaker fails at V4 under
the named speaker's key, or at V6 under its own (:696, :698). So the KSA
envelope is never an ITE-5 envelope, which is also why the §6 matrix has no row
for it (mofn report R-0006:347). It costs a property, not a meaning (D-04), and
ADR-0004:51-52 keeps the property at the boundary, where DSSE and COSE have it.

**X-02 — no algorithm in the signature.**

<!-- q L17 "SHOULD NOT" .. "signature" -->
> SHOULD NOT require the inclusion of signing key algorithms in the signature

KSA does both things the source separates. It holds the premise R-0008 rests
on, that a key belongs to exactly one suite (SPEC-0001:204), with the key store
keyed by suite and kid (SPEC-0002:695). And it signs the suite inside the TBS
(:350), repeating it in the envelope as a hint checked at V6 (:307). mofn's
survey calls R-0008 a defect, agility by omission that permits algorithm
confusion (mofn survey R-0001:1597-1608; H-post-quantum.md:82). The source
gives no rationale either way; *(inferred)* an algorithm fixed by the key is
how its position closes the same attack. Whether a suite inside the signed
payload is in the signature, in R-0008's sense, the source does not say; read
either way, the KSA envelope is not an in-toto envelope (X-01). On export the
signed suite is lost (§7).

**X-03 — media types named by in-toto's predicates directory.**

<!-- q L78-79 -->
> The media type `application/vnd.in-toto.<predicate>+dsse` SHOULD be used to denote an individual attestation in arbitrary storage systems.

`<predicate>` is a file name in one repository (R-0016, R-0026; the link, L109)
inside the IANA vendor tree. P1 rejects that shape for extension points
(ARCH-0002:65-87), ADR-0003 D1 rules out URN identifiers and namespaced
extensions (ADR-0003:47), and ADR-0004 item 3 keeps registries at the boundary
(ADR-0004:46-50). *(inferred)* At an export boundary the media-type tree and
in-toto's predicate names join item 3's list, beside the registry identifiers
lane-a found DSSE and in-toto using (lane-a/README.md:36). Because of A-03,
what an export loses by not carrying them is a hint.

### 2.4 Constrains

**C-01 — the source's order is weaker than R-O-05's.** (L16, L54-55, quoted
above.) R-0007 only discourages a format from requiring parsing before
verification, so one that does is still admissible; and the consumer rule names
the two acts, parse then verify, without saying which runs first (R-0019,
R-0029). R-O-05 is a SHALL on our verifier (ARCH-0001:457; SPEC-0002:688-701).
So our importer has to impose the order; nothing in this source would flag a
parse-first consumer. mofn's own lane-a sample 3 is one: it base64-decodes and
parses the payload (lane-a/03_slsa_provenance.py:93-94) before checking the
signature (:119-123), and checks only the first signature (:119). It is a
throwaway (lane-a/README.md:3); it is recorded so T-052 does not inherit the
order. §5 maps the steps.

**C-02 — a threshold is not a signature count.** The source requires a format
to carry several signatures (R-0003) and `signatures` to be an array (R-0009),
and says nothing of how many must verify (S-05). With DSSE's equivalence of one
multi-signature envelope to separate ones, in mofn's reading, an intermediary
may split or merge envelopes, so a count is unsafe to read as `k` (mofn report
R-0006:1225-1231). A threshold `trust` (SPEC-0002:606-609) therefore cannot be
exported as signatures on one envelope: `k` and the members travel in the
payload, which mofn report R-0006 §5.1 already concluded. R-M-06
(ARCH-0001:429) is untouched natively.

**C-03 — in the in-toto world, COSE means COSE_Sign.** (L23-24, quoted under
A-04.) DEC-005 offers DSSE, COSE_Sign1, or both (ARCH-0001:635). The source
admits COSE_Sign and rejects COSE_Sign1 for in-toto, so the COSE structure that
would carry an in-toto attestation is one DEC-005 does not list, and it is
named here as docs/extraction.md:133-135 asks: **COSE_Sign**. Three caveats:
the link is to RFC 8152 §4.1 (L101), which RFC 9052 and RFC 9053 obsolete
(rfc-8152/record.yaml:21); the compliance is asserted, not shown against R-0008
(Q-05); and P5.2's analysis is owed again against COSE `crit` if COSE is chosen
(ARCH-0002:522-523). *(inferred)* ARCH-0001 §3.2 records SCITT signed
statements as COSE_Sign1 whose payload may be in-toto (ARCH-0001:281-283),
which by L23-24 is not an in-toto envelope. So no single envelope among DSSE,
COSE_Sign1 and COSE_Sign serves both the in-toto mapping that MD-1 keeps
(meetings/2026-09-28.md:40) and the SCITT row (§4).

**C-04 — an import keeps the bytes it verified.**

<!-- q L58 "`payload` MUST" .. "[Statement]." -->
> `payload` MUST be a base64-encoded JSON [Statement].

There is no canonical form (R-0005), and in DSSE the signature covers the exact
payload bytes (lane-a/common.py:72-75). So an imported attestation is the bytes
received, and re-serialising it breaks its signature. SPEC-0001 already says an
import keeps its original bytes (:229-232) and a wallet keeps statements as
their exact envelope bytes (:257); the KSA digest is likewise over `tbs`, never
the envelope (SPEC-0002:319-321). *(inferred)* The I4 demo's round trip of a
real SLSA attestation (PLAN-0001:487; PLAN-0003:48) is byte-exact only if the
export of an import re-emits the payload, `payloadType` and signatures
received; an `ArtifactStatement` re-serialised to JSON cannot carry a signature
by a key mofn does not hold, which is lane-a's own reason for never changing
the real provenance (lane-a/README.md:62). Q-13 asks what an import's identity
is computed over.

**C-05 — the attestations to import arrive in a container the source calls
non-compliant.**

<!-- q L21-22 "The [Sigstore Bundle]" .. "envelope." -->
> The [Sigstore Bundle], while [supporting DSSE], is not currently [ITE-5] compliant because it requires a _single signature_ in the envelope.

lane-a sample 3 fetches real provenance as Sigstore bundles wrapping DSSE
envelopes (lane-a/03_slsa_provenance.py:13) and skips bundles without one
(:152-153). These are what T-052 and the I4 demo would import
(BACKLOG-0001:189; PLAN-0001:487). The source does not say whether a DSSE
envelope taken out of such a bundle is a conforming in-toto envelope, and its
footnote points at an open discussion with no outcome (L98). Q-06.

**C-06 — the algorithm comes from the key, and KSA has no suite for the keys in
use.** Under R-0008 a verifier learns the algorithm from the key, and the
format decides how signature bytes are encoded (L32-33, R-0037). lane-a sample 3
verifies real provenance as ECDSA with SHA-256 under the leaf certificate's key
(lane-a/03_slsa_provenance.py:121-123). SPEC-0002 has no ECDSA suite: P-256 is
reserved and unspecified (SPEC-0002:360, :845), and a kid is defined only under
a suite (:288). *(inferred)* So the signer of a real attestation has no KSA kid
until suite 2 is specified, and R-O-01's issuer-as-`KeyId` (ARCH-0001:453)
cannot be met for it, if R-O-01 is read as reaching imported objects. Q-15.

**C-07 — one in-toto mapping table is several.** Each field rule admits an
equivalent field (R-0009, R-0010, R-0012, R-0013), and any ITE-5 format may be
used (R-0002). R-I-01 asks for a table per supported foreign format
(ARCH-0001:441). At the envelope layer in-toto is not one format, and P5.2's
owed rows and negative fixture are DSSE's (ARCH-0002:532-535; ADR-0002:180).
*(inferred)* An importer states which envelope formats it accepts, and the
R-I-01 table carries a block for each.

### 2.5 Conflicts

**K-01 — R-O-05's first clause cannot hold for an in-toto export.** (L45-48 and
L58, quoted above.) An in-toto DSSE envelope signs a JSON Statement under an
in-toto `payloadType`. R-O-05 requires the signed payload to be the canonical
encoding verbatim (ARCH-0001:457), and the canonical encoding is KSA-CBOR
(SPEC-0002:245-247; ADR-0004:38-42). One envelope cannot do both. *(inferred)*
Two export products exist, and this source governs only the second:

- **E1**, a DSSE envelope whose payload is the KSA TBS under a `payloadType` of
  our own. R-O-05 holds; no in-toto consumer reads it; this source does not
  apply. That is what the §6 DSSE row's *wire only* describes (ARCH-0001:497).
- **E2**, an in-toto Statement in DSSE, which R-I-03 asks for (ARCH-0001:443).
  This source applies and R-O-05's first clause does not: what is signed is a
  second object, with its own bytes and digest, made from the native statement
  by MAP-0002.

Neither carries the native signature (K-02). E2 re-signs under every DEC-002
option unless the native statement were itself an in-toto Statement, which P1
and the §6 matrix's lossy `predicateType` mapping rule out (:496). It is
therefore not a DEC-002 discriminator, with the one exception §3.4 names.

**K-02 — the export signs again, and SPEC-0001 says not with the same key.** A
DSSE signature is over PAE(`payloadType`, payload) (lane-a/common.py:72-75); a
KSA suite-1 signature is over the DS label followed by the TBS
(SPEC-0002:372-374). No byte string is both (§8 check 3), so the native
signature never verifies as a DSSE one, and every export, E1 or E2, needs a new
signature. SPEC-0001 §5.3 recommends a separate key per protocol and requires
any use outside KSA to be recorded on the key (SPEC-0001:221-227); SPEC-0002
§13.2 repeats the recommendation (SPEC-0002:900-901). *(inferred)* An in-toto consumer
attributes an attestation to whichever key signs the envelope. So an R-I-03
export is signed either with the speaker's key, against that recommendation
(a SHOULD) and with the requirement (a MUST) to record it, or with an export key that nothing published links to
the speaker: no kind in SPEC-0002 §8.1 (:527-539) and no usage code in §12.7
(:860-864) says one key exports for another. Q-11. Replay itself is closed by
the prefixes (§8 check 3), the condition SPEC-0002 §13.2 sets (:897-899).

### 2.6 Silent

**S-01 — the signing input.**

<!-- q L8 -->
> The RECOMMENDED format and protocol for Envelopes are defined per [DSSE v1.0].

<!-- q L32-33 "The encoding" .. "schema." -->
> The encoding of the signature bytes is determined by the envelope schema.

The source defines no signing input, and any ITE-5 format may be used instead
(R-0002). Under the RECOMMENDED format the signed bytes are DSSE's PAE over
this source's `payloadType` and payload (§3.1). The reference's label says v1.0
and its URL pins v1.0.2 (L102); ITE-5 itself is linked at a moving branch
(L103; Q-07).

**S-02 — keys, algorithms and who may sign.** Verifying a payload against its
signatures (R-0019) presumes keys; the source offers a hint (R-0006) and
nothing on where keys come from or whose they are. That fits R-I-02, under
which an import never makes a foreign object a native anchor (ARCH-0001:442),
and V3's *unverifiable* for an unknown key (SPEC-0002:695); whose a key is, is
SPEC-0004 §4's question.

**S-03 — post-quantum.** §6.

**S-04 — validity, revocation, time.** None at this layer; the words do not
occur (§8 check 8). A KSA validity window and a `revoke` by digest
(SPEC-0002:491-501, :621-627) do not reach an export, whose digest differs
(K-01). SPEC-0001 asks statements that must last decades for a post-quantum
suite or an external timestamp (SPEC-0001:215-217), and the envelope carries no
time.

**S-05 — what several signatures mean to a verifier.** All, any, or k; whether
`signatures` may be empty; what one failing signature among good ones does. In
mofn's reading DSSE leaves the threshold to the application (mofn report
R-0006:238). Q-03.

**S-06 — envelope serialisation.** The JSON shape, the base64 alphabet and
padding, duplicate members and unknown fields are DSSE's to define; this source
says base64 and no more (R-0020). P5.2 makes our importer reject unknown
exterior fields (ARCH-0002:498-510). *(inferred)* It does not reach a
duplicated `payload` or `payloadType` member, where two JSON parsers can verify
one value and hand on another, nor two base64 spellings of one payload; and
SPEC-0002's bound on the work done before V4 (SPEC-0002:928) has no counterpart
here for the envelope's own decoding.

---

## 3. MD-3, ADR-0004 and DEC-002, field by field

MD-3 narrowed DEC-002 to option 5 on 2026-09-28: the CBOR data model, no IANA
tags, COSE as export only, type identity as (defining key, label) per P1, and
YAML as the human form (meetings/2026-09-28.md:51-54). ADR-0004 accepted option
5 on 2026-10-25, closing the narrowing (ADR-0004:132-133), and made COSE_Sign1
and DSSE the export envelopes (:51-52), as option 5's own text already had
(ARCH-0001:531; PLAN-0001:365-368). This source is an envelope document, so the
mapping below is the one docs/extraction.md:123-126 asks for, and §3.4 is the
part it insists on.

### 3.1 What this layer fixes in the signed bytes (T-051)

| part of the signed bytes | fixed by | for an in-toto export |
|---|---|---|
| the framing | DSSE, outside this source: the literal `DSSEv1`, the type's length, the type, the body's length, the body, space-separated (lane-a/common.py:72-75) | — |
| the type string | this source: it is signed (R-0013) and DSSE allows two values (R-0015) | `application/vnd.in-toto+json`, or the predicate-specific form where one exists (D-03) |
| the body | this source: a JSON Statement (R-0020); the Statement layer: its fields (library#134) | the exporter's JSON bytes |
| the JSON serialisation | nobody: there is no canonical form (R-0005) | MAP-0002's choice. *(inferred)* if it fixes one, R-O-03 asks it to cite the algorithm (ARCH-0001:455) |
| the key and its algorithm | nobody here (R-0008; S-02) | K-02, C-06 |

From the type string and the body alone, lane-a's signed input reproduces byte
for byte (§8 check 1). So T-051 can fix the signed bytes once it has chosen a
`payloadType` value and a JSON serialisation; the key adds only the signature.

### 3.2 Field by field

| field (this source) | rule here | DSSE, as lane-a builds it | COSE_Sign (RFC 9052, outside this source) | KSA signed statement (SPEC-0002 §5) | at the boundary |
|---|---|---|---|---|---|
| `signatures` | REQUIRED, an array (R-0009); a format must carry several (R-0003); signature bytes encoded as the format says (L32-33, R-0037) | `signatures`, a list of `{keyid, sig}`, `sig` in base64 (lane-a/02_dsse_intoto.py:64-68) | `signatures: [+ COSE_Signature]`, each `[Headers, signature: bstr]` (§4.1) | one `sig`, element 3, over the DS label and `tbs` (SPEC-0002:302, :310) | export: a new signature per exported object (K-02); import: each verified alone, never read as `k` (C-02, D-04) |
| `keyid` | SHOULD, one per signing key (R-0010); may sit in the signature array (R-0011); a hint (R-0006) | `signatures[].keyid`, a string; lane-a's is `SHA256:` plus base64 of the kid (lane-a/02_dsse_intoto.py:56-58) | `kid` (label 4) in each signature's protected or unprotected header (§3.1) | `says`, element 1: a hint V6 checks against the signed `says` (SPEC-0002:308, :698) | export: the kid may go here, as a hint; the principal goes in the payload (P5.2, P1.1). import: never a principal; the kid is computed from the key (ARCH-0002:113) |
| `payload` | SHOULD be present and hold the Statement that was signed (R-0012); in DSSE a base64 JSON Statement (R-0020) | base64 of the Statement octets; PAE covers the decoded octets (lane-a/common.py:72-75; lane-a/02_dsse_intoto.py:78) | `payload: bstr / nil`, nil when detached (§4.1) | `tbs`, element 2, exactly as signed, always present (SPEC-0002:309, :693) | export: a JSON Statement, never the TBS (K-01). import: kept as received (C-04) |
| `payloadType` | signed with the payload (R-0013); of R-0014's form (R-0014); in DSSE one of two values (R-0015) | a string inside PAE, which begins `DSSEv1 28 application/vnd.in-toto+json` (§8 check 1) | content type (label 3) in the body's protected header, which every signer's `Sig_structure` covers (§3.1, §4.4) *(inferred)* | nothing transmitted: the DS label, fixed per object class (SPEC-0002:397-404), and `kind` in the TBS (:433) | export: the generic form for a KSA-defined type (D-03). import: compared byte for byte (Q-13) |
| algorithm | not needed in the signature (R-0008) | none; it comes with the key | `alg` (label 1) in each signature's headers (§3.1) | `suite`, signed in the TBS (SPEC-0002:350) and hinted as element 0 (:307) | export: the signed suite is dropped (§7). import: from the key; there is no ECDSA suite (C-06) |
| public key | — | none | outside this comparison | `pub`, element 4, optional, checked against `says` at V3 (SPEC-0002:311, :695) | not carried at this layer |
| storage media type | `application/vnd.in-toto.<predicate>+dsse`, SHOULD (R-0025); `<predicate>` a predicate file name (R-0026); not a reliable type (R-0027) | outside the signed bytes | none given by this source | none | a label, never read as type (A-03) |
| file name | `.json` (R-0021); a step name (R-0022); an agreed name (R-0023); a truncated KEYID (R-0024) | outside the signed bytes | none given | none: envelope bytes are kept and addressed by digest (SPEC-0001:257; SPEC-0002:209-210) | a storage hint (D-02) |
| `_type` | the payload's schema (L46-47, R-0039) | inside the payload | inside the payload | `kind` in the TBS; *(inferred)* the `v1` of the DS label does the versioning | the Statement layer (library#134) |

### 3.3 MD-3, clause by clause

| MD-3 clause (meetings/2026-09-28.md:51-54) | what this source does | finding |
|---|---|---|
| the CBOR data model | an in-toto DSSE payload is JSON (R-0015, R-0020), and lane-a's envelope is JSON too; only R-0014's `<encoding>` slot admits other serialisations, which the source defines nowhere | an in-toto export leaves the CBOR data model (§3.4 item 1) |
| no IANA tags | an in-toto DSSE envelope carries no CBOR, so no tags; COSE_Sign's tag (98) is optional, as COSE_Sign1's is (RFC 9052 §2, outside this source) | nothing natively; ADR-0004 item 3 holds at the boundary |
| COSE as export only | DSSE RECOMMENDED; COSE_Sign admitted; COSE_Sign1 rejected (L8, L23-24) | MD-3's wording names an export the in-toto world rejects in its one-signer form; DSSE came with option 5's text and ADR-0004:51-52 (§3.4 item 3) |
| type identity is (defining key, label) per P1 | `payloadType` and storage media types, predicate file names (X-03); `predicateType` URIs in the Statement layer | every type name at this layer is global, and the source denies the media type authority (A-03) |
| YAML is the human form, by a canonical one-way mapping | no human form; authenticated information comes from the verified payload only (R-0019) | R-O-05's last sentence carries over: render from verified bytes (A-03) |
| option 2 retained only as the comparison fixture | COSE_Sign is option 2's kind of envelope | no effect: option 2 fell on P1, not on its envelope (ADR-0004:119-120) |

### 3.4 Where the source cuts against MD-3 and option 5

1. **The in-toto world is JSON, and option 3 is the DEC-002 option that would
   have shared it.** At this boundary option 5 pays for a JSON serialiser, a
   base64 codec and a PAE implementation beside KSA-CBOR and the KSA envelope.
   Under option 3 the native form was JSON with RFC 8785 and DSSE was the
   signed form (ARCH-0001:529), so an in-toto export would have shared the data
   model and the envelope code, though not the payload schema or the
   `payloadType` (K-01 would still re-sign). That is a cost option 5 pays and
   option 3 does not. Option 3 is withdrawn on four grounds (ADR-0004:121-124;
   DECISIONS-0001:116-119), none of which this source touches, so this is
   evidence recorded, not a reopening.
2. **R-0005 is about signatures; option 5's canonical form is bought for
   identity.** KSA's signature path needs no canonicalisation (A-02). Its
   identity path does: statement digests and DefinitionIds are hashes of
   canonical encodings (SPEC-0002:288-290), and reduction compares a
   `delegation: 1` hop's range with the delegator's by KSA-CBOR bytes alone
   (BACKLOG-0001:175). mofn report R-0006 puts conditions (5) and (6) on that
   path: an identifier has no received bytes to verify, because the digest is
   produced by canonicalising (mofn report R-0006:401-407). DSSE derives no
   identifier from content and needs none. Every DEC-002 option has a canonical
   form, so the source's position lies outside the option set and discriminates
   among none. What it shows is narrower: checking a signature needs no
   canonical form, so the rejecting decoder (SPEC-0002:251-266), whose omission
   DECISIONS-0001:136-139 records as option 5's difference in kind, earns its
   cost elsewhere, on the identity path and in making signed bytes decode one
   way, and this source addresses neither.
3. **MD-3's own wording would not have produced an in-toto export.** It names
   COSE only (meetings/2026-09-28.md:51-52), and the in-toto world RECOMMENDS
   DSSE and rejects COSE_Sign1. The DSSE half of the export rule came with
   option 5's text (PLAN-0001:365-368; ARCH-0001:531) and ADR-0004 item 4, not
   with the minute.
4. **R-0014 leaves a CBOR door the source never opens** (L39-40, quoted under
   D-03). That form admits an in-toto Statement serialised in something other
   than JSON, in a format other than DSSE such as COSE_Sign, which would sit
   nearer option 5's data model. The source defines no such serialisation and
   fixes DSSE to JSON (R-0015, R-0020); only the Statement layer could. Q-12.
   It does not revive option 2, which fell on P1 (ADR-0004:119-120).

### 3.5 Where it favours option 5 and SPEC-0002

- The signature-path properties of A-01 and A-02 hold natively, and the
  rejecting decoder runs after V4 (SPEC-0002:696-697), downstream of
  authentication, which is the order the source wants.
- The DS label makes cross-protocol replay with DSSE impossible in both
  directions, by its first octet for suite 1, and for suite 8 by the context
  string or, where the contexts agree, at V5 (§8 check 3): the condition
  SPEC-0002 §13.2 sets (:897-899).
- KSA's binding of algorithm to key is stronger than R-0008 asks: the premise
  and a signed suite (X-02).

### 3.6 Not discriminators

- Re-signing (K-01, K-02): every DEC-002 option re-signs for an in-toto export.
- The one-signature envelope (X-01): SPEC-0002 §5's, under any encoding.
- The `keyid` and principal collision (D-01): DEC-003's and P5.2's, not
  DEC-002's.
- File names and storage media types (D-02, X-03): outside every signed byte.

### 3.7 What an export deliberately does not carry

- no exterior field beyond `payload`, `payloadType` and `signatures` (P5.2,
  ARCH-0002:510);
- no principal in `keyid` (P5.2, :530);
- no threshold as a signature count (C-02);
- no predicate-specific `payloadType` for a KSA-defined type (D-03);
- not the native signature, which does not verify under PAE (K-02);
- no claim that a storage media type or a file name types the attestation
  (A-03, D-02);
- *(inferred)* not the signed suite, the native digest, the validity window or
  `pub` (§7).

---

## 4. DEC-005 and R-I-03, read against this source

DEC-005 offers DSSE, COSE_Sign1, or both with one unsigned payload schema
(ARCH-0001:635). Once SPEC-0002 §5 gave KSA a native envelope, mofn report
R-0006 §5.2 found two readings of DEC-005 and could not choose (mofn report
R-0006:1254-1266); ADR-0004 item 4 took the second, that DEC-005 chooses an
export envelope (ADR-0004:51-52, :112).

| option | as an in-toto envelope (this source) | as a SCITT signed statement (ARCH-0001:281-283) | notes |
|---|---|---|---|
| DSSE | RECOMMENDED (R-0001); meets ITE-5 | not SCITT's form | P5.2 is reasoned from it alone (DL-0013 review:85-92) |
| COSE_Sign1 | does not meet ITE-5 (L23-24) | SCITT's form | R-I-03's second branch, with CWT (ARCH-0001:443) |
| both, one unsigned payload schema | the DSSE side must carry a JSON Statement (R-0020) | the COSE_Sign1 side | which payload is the single schema is open (Q-10) |
| **COSE_Sign**, not listed | meets ITE-5, per L23-24 | not SCITT's form, per ARCH-0001:281 | asserted, not shown, against R-0008 (Q-05); P5.2 owed against `crit` (ARCH-0002:522-523) |
| the KSA envelope (SPEC-0002 §5) | cannot meet R-0003 (X-01) | — | not a DEC-005 candidate after ADR-0004:51-52 |

R-I-03 asks for at least one envelope in v1 (ARCH-0001:443). *(inferred)* If v1
ships one, this source decides which world it serves: DSSE serves in-toto and
COSE_Sign1 serves SCITT. Only the *both* option serves the two, and an in-toto
Statement registered with SCITT travels in two envelopes, not one (C-03). That
is the source's bearing on DEC-005; it selects nothing.

---

## 5. R-O-05: verify before parse, step by step

R-O-05 has three clauses (ARCH-0001:457): sign the canonical encoding verbatim
with an authenticated type; verify before decoding and never canonicalise
during verification; regenerate any human form from verified bytes. K-01 takes
the first; this section takes the second and third.

| # | KSA (SPEC-0002 §9.2) | in-toto in DSSE (mofn's reading of DSSE, and this source) | this source says |
|---|---|---|---|
| 1 | V1: decode the envelope, a KSA-CBOR array (SPEC-0002:693) | parse the JSON envelope; base64-decode `payload` and each `sig` | nothing; P5.2 has our importer reject unknown exterior fields (ARCH-0002:509) |
| 2 | V2: the suite is registered and supported (SPEC-0002:694) | nothing: there is no algorithm in the envelope | R-0008 |
| 3 | V3: the key, by suite and `says`, or from `pub` checked against `says` (SPEC-0002:695) | the key a `keyid` hints at, from elsewhere | R-0006, R-0010; where from, nothing (S-02) |
| 4 | V4: the signature over the DS label and the received `tbs` (SPEC-0002:696) | the signature over PAE(`payloadType`, payload) | R-0013: the type is inside it |
| 5 | — (the DS label is fixed) | reject an unsupported `payloadType` (mofn report R-0006:238) | R-0015 names the two values |
| 6 | V5: decode `tbs` with the rejecting decoder (SPEC-0002:697) | parse the JSON Statement; there is no canonical form to check | R-0005 |
| 7 | V6: the decoded `suite` and `says` equal the envelope's (SPEC-0002:698) | nothing authenticated to compare a `keyid` with | — |
| 8 | V7, V8: structure and kind rules (SPEC-0002:699-700) | `_type` (L46-47, R-0039), then the Statement layer | R-0017, R-0018: type from `predicateType` only |
| 9 | V9: the digest is SHA-256 of `tbs` (SPEC-0002:701) | none defined | nothing (Q-13) |

Where the orders differ, and where they only seem to:

- Step 1 decodes before anything is verified, in both. Base64 and JSON here are
  the envelope's transport, as V1's CBOR is in KSA; R-O-05's decoding is the
  payload's (SPEC-0002:195-199). *(inferred)*
- The source's consumer rule names parsing before verifying (R-0019, R-0029),
  and R-0007 only discourages a format that requires it. A consumer that
  follows the sentence in order runs step 6 before step 4. R-O-05 forbids that;
  the source does not (C-01).
- The source's §2 states the consumer rule under the predicate-specific case
  only (L47-48, R-0040), and its §4 as a bullet of the storage convention with
  no condition of its own (L87-88). Read narrowly, its §2 gives a DSSE envelope
  with the generic type no consumer rule at all, and its §4 none outside storage
  (Q-02, SD-11).
- The human form: R-O-05's third clause is A-03. What a person sees comes from
  step 6's output, never from step 5's type string, a storage media type or a
  file name.
- lane-a sample 3 runs step 6 before step 4 and checks one signature (C-01).

---

## 6. Post-quantum: an algorithm-silent envelope

The format decides how signature bytes are encoded (R-0037) and need not name
the algorithm (R-0008). There is no size limit, algorithm identifier, context
string or hybrid rule (§8 check 8).

1. **It fits.** Suite 8's ML-DSA-65 signature is 3309 octets (SPEC-0002:416),
   4412 base64 characters in a DSSE `sig`; suite 1's 64 octets are 88. Its
   1952-octet public key (:412) does not travel in the envelope. Nothing in the
   source bounds either.
2. **The context string is unspecified.** KSA passes `KSA-STMT-SIG-v1` (15
   octets) to ML-DSA as its context and prepends nothing (SPEC-0002:406-407,
   :414-415). A DSSE signature under ML-DSA takes whatever context its signer
   passes, and neither this source nor, in mofn's reading, DSSE says which:
   DSSE restricts neither algorithm nor format (mofn survey R-0001:1599-1602).
   *(inferred)* Two DSSE implementations that disagree, empty against
   non-empty, make signatures neither verifies for the other (Q-14). Replay
   against KSA stays closed either way (§8 check 3).
3. **Algorithm binding.** R-0008's premise is that the key fixes the algorithm.
   KSA states that premise (SPEC-0001:204) and also signs the suite
   (SPEC-0002:350). Its kid does not hash the suite, so it forbids registering
   a suite whose key encodings can equal another's (:831-838). mofn's survey
   counts R-0008 as agility by omission (mofn survey R-0001:1597-1608;
   H-post-quantum.md:82); the source does not argue the point (X-02).
4. **Quantum-resistant thresholds.** The survey adds that no envelope can say
   that at least N of a threshold's signatures are post-quantum (mofn survey
   R-0001:1604-1608). That holds here, where the envelope carries no `k` at all
   (C-02). *(inferred)* It holds equally for SPEC-0004 §6.4, which counts
   members distinct by kid and puts no condition on their suites
   (SPEC-0004:431). A relying party gets the property only by the members it
   chooses, so it is a property of policy in both, not of an envelope.
5. **Long-lived exports.** SPEC-0001 asks statements that must verify for
   decades for a post-quantum suite or an external timestamp
   (SPEC-0001:215-217). The envelope carries no time (S-04); a Sigstore
   bundle's timestamp and log entry sit in the container (C-05), outside this
   source.

---

## 7. Interchange losses at the envelope layer (T-053, R-I-01)

**Export**, an `ArtifactStatement` to an in-toto Statement in DSSE:

| native | at the envelope layer | kind |
|---|---|---|
| the TBS bytes and their digest | a JSON Statement with its own bytes and digest | dropped: identity (K-01) |
| the signature over the DS label and the TBS | a new signature over PAE | replaced (K-02) |
| the authenticated type (DS label, `kind`) | `payloadType`, authenticated | preserved in kind, changed in value (A-01) |
| `suite`, signed | nothing | dropped (X-02) |
| `says`, signed | a `keyid` hint, checked by nothing | dropped from the signed bytes unless the Statement carries it (D-01; Statement layer) |
| `pub` | nothing | dropped |
| `valid`, and revocation by digest | nothing | dropped; a native `revoke` names a digest the export does not have (S-04) |
| a threshold's `k` | nothing; a signature count is not `k` | dropped (C-02) |
| — | the `payloadType` value, the `keyid` spelling, a file name | inferred by the mapping (D-01, D-02, D-03) |

**Import**, an in-toto Statement in DSSE to an external statement:

| foreign | native | kind |
|---|---|---|
| `payload`, `payloadType`, `signatures`, as received | kept verbatim (SPEC-0001:229-232) | preserved (C-04) |
| each verified signature | one external statement per signer (D-04) | inferred |
| `keyid` | nothing; the kid is computed from the key (ARCH-0002:113) | dropped as a principal |
| the signer's algorithm | from the key; none for ECDSA (C-06) | inferred, sometimes impossible |
| storage media type, file name | nothing | dropped (A-03, D-02) |
| a Sigstore bundle's verification material | outside this source | not read here (C-05) |

These are the envelope-layer rows. The Statement-layer rows (subject digests,
`predicateType`, the `description` subject of ARCH-0001:496) belong to the
`in-toto-attestation-v1` extraction (library#134).

---

## 8. Checks, arithmetic, and the enumerated *only*s

1. **lane-a's signed bytes reproduce from the type string and the body.** A
   standard-library re-implementation of lane-a/common.py:72-75 and of the
   Statement in lane-a/02_dsse_intoto.py:26-48, with no key, against
   lane-a/out/SHA256SUMS at the pin: the Statement is 406 octets and its sha256
   equals lane-a/out/SHA256SUMS:17; the PAE is 449 octets and its sha256 equals
   lane-a/out/SHA256SUMS:4 (`b6e040f2…`). The signed input is a pure function
   of the `payloadType` this source governs and the JSON bytes the exporter
   writes.
2. **Two `payloadType` values, two signed inputs.** The generic form is 28
   octets and the predicate-specific form for `provenance` is 39; over the same
   Statement the PAE grows by 11 octets and differs. Same script.
3. **Replay between KSA and DSSE.** A PAE's first octet is `0x44` (`D`); a
   suite-1 signing input's is `0x4b` (`K`), the DS label being
   `4b53412d53544d542d5349472d763100`, equal to SPEC-0002:373; a KSA TBS is a
   map (SPEC-0002:428), whose head octet lies in `0xa0`…`0xbf`. So no PAE
   equals a suite-1 signing input or a TBS, and no TBS equals a PAE. For suite
   8, FIPS 204's message representative begins with a zero octet and the
   context's length, so a DSSE signature made with any other context differs
   from KSA's in the context-length octet or within the context bytes (at the
   second octet, 15 against, say, 0, for a context of another length); one made with KSA's own
   context signs a PAE, which fails V5 after V4 (SPEC-0002:696-697) because it
   is not a KSA-CBOR map. Closed in both directions for both suites.
4. **`<keyid[0:8]>`, under two spellings.** For Bob's key (SPEC-0002 Appendix
   A; its seed is lane-a's, lane-a/02_dsse_intoto.py:19-21): the hex kid gives
   `39f713d0`, one of 2^32 values, and two keys share one with probability 0.5
   first at 77,164 keys. lane-a's spelling gives `SHA256:O`, one of 64 values:
   two functionaries collide with probability 0.016, five with 0.148, ten with
   0.523, and 0.5 is first passed at ten. Method: the birthday product 1 − ∏(1
   − i/N), i < m.
5. **Base64 sizes**, 4·⌈n/3⌉: 64 octets → 88 characters, 3309 → 4412, 1952 →
   2604.
6. **R-0014 against R-0015, enumerated.** R-0015 admits two strings. The
   predicate-specific one has `.` where R-0014's template has `+` directly
   after `vnd.in-toto`, for every predicate name including an empty one, so
   exactly one string satisfies both as written:
   `application/vnd.in-toto+json`.
7. **Identical texts.** `bin/check-id-joins --surface`: 3 groups, 6
   requirements (R-0017/R-0027, R-0018/R-0028, R-0019/R-0029). Every citation
   of them here was selected by its own line range (§10).
8. **The silences.** A case-insensitive grep of the rendering for authentic,
   hint, canonical, algorithm, threshold, revoc, time, quantum, order and
   verify: `hint` only at L15, `algorithm` only at L17, `canonical` only at
   L14; threshold, revoc, time, quantum and order nowhere.
9. **Digests, three ways.** The `.bin` sha256 equals record.yaml:15 and
   `render-source.py`'s pinned digest; the `.txt` sha256 equals
   `requirements.yaml`'s `source_digest`; retrieved 2026-11-03
   (record.yaml:16).
10. **The *only*s that rest on an enumeration.** The generic form is the only value R-0014
    and R-0015 both admit (check 6), and the only form for a KSA-defined type
    (D-03, by R-0016). A KSA envelope has only one `sig` (SPEC-0002:302).
    lane-a is the only mofn code that builds DSSE envelopes: at the pin, a grep
    for `dsse`, `in-toto`, `intoto` and `payloadType` finds nothing in
    `prototype/wallet` or `src`, and `payloadType` or a PAE call only in five
    `prototype/lane-a` files. Pass 2 added two more, checked against the source:
    only R-0014's `<encoding>` admits a serialisation other than JSON (§3.3;
    R-0015, R-0020 and R-0039 fix JSON), and the storage media type exists only
    for DSSE (Q-08; R-0025's `+dsse`). Every other *only* here is a citation or
    a reading, beside its source.

---

## 9. Open questions

Source defects are recorded here and not repaired; the record's canonical list
is normative.md's Source defects, and each question below that states one
names it. Q-10 to Q-15 are mapping
questions for MAP-0002, T-053 and DEC-005; this file answers none of them.

- **Q-01 — R-0014 and R-0015 disagree as written (SD-1).** The source's general rule
  (§2 L39-40) requires the form `application/vnd.in-toto+<encoding>`; its DSSE
  rule also allows `application/vnd.in-toto.<predicate>+json`, which does not
  have that form (§8 check 6), and then states rules for using it (R-0016 to
  R-0019). Either the general rule means a pattern it does not write, or the
  predicate-specific form is never conformant. A mapping that wants to be safe
  under both readings has one value.
- **Q-02 — the consumer rule's order and scope (SD-3, SD-11).** R-0019 and R-0029 name
  parsing before verifying, against R-0007. The source's §2 states it under the
  predicate-specific case (R-0040), its §4 as a storage-convention bullet with no
  condition of its own (L87-88); does a
  consumer of a DSSE envelope with the generic type have the rule at all?
- **Q-03 — several signatures (S-05).** Must all verify, any, or a number the
  verifier chooses? May `signatures` be empty? Does one failing signature void
  the envelope or only itself?
- **Q-04 — which KEYID is truncated, and in which spelling (SD-9).** R-0024 links
  KEYID to in-toto v1.0's key formats (L104), while the `keyid` field itself is
  any value a format likes (R-0010). The naming also assumes one signing
  functionary per envelope, which a multi-signature envelope does not have.
  Under lane-a's spelling the slice is degenerate (§8 check 4, D-02).
- **Q-05 — COSE_Sign's compliance is asserted (SD-13).** L23-24 does not show it
  against R-0008, and a COSE signature conventionally carries `alg` in its
  headers (RFC 9052 §3.1, outside this source); whether RFC 9052 requires it
  there was not settled in this pass. The link is to the obsoleted RFC 8152
  (L101).
- **Q-06 — a DSSE envelope inside a Sigstore bundle (SD-4).** The bundle does not meet
  ITE-5 because it admits one signature (L21-22). Is the DSSE envelope it holds
  a conforming in-toto envelope? The footnote names an open discussion with no
  status (L98).
- **Q-07 — ITE-5 is unpinned (SD-12).** The six properties are restated here (L12-17),
  and ITE-5 is linked at a moving branch (L103). Compliance is tested against
  two texts, one of which can change.
- **Q-08 — the smaller gaps (SD-5, SD-6, SD-14).** A payload SHOULD be present (R-0012), yet
  consumers are told to parse the payload (R-0019): where does a detached
  payload come from? The storage media type exists only for DSSE (R-0025), not
  for COSE_Sign or the generic type, and the source does not say whether
  `+dsse` is a registered suffix. A stored envelope ends in `.json` (R-0021)
  while its media type ends in `+dsse`. The predicate's version is not in the
  media type (R-0041, R-0042), so `provenance` names every SLSA
  provenance version at once (lane-a found v1.0 and v1.1 sharing one
  `predicateType`, lane-a/README.md:52).
- **Q-09 — is a `keyid` authenticated?** The source never says. DSSE says not,
  in mofn's reading (mofn report R-0006:1268-1274); a COSE_Sign `kid` may sit
  in a protected header and be signed. P5.2's rule, the principal in the
  payload, holds either way, but its stated reason is DSSE's (DL-0013
  review:85-92).
- **Q-10 — DEC-005's single unsigned payload schema.** Is it the KSA TBS (E1,
  where R-O-05 holds and no in-toto consumer reads it) or an in-toto Statement
  (E2, where this source holds and R-O-05's first clause does not)? (K-01)
- **Q-11 — the export's signing key.** The speaker's key, against SPEC-0001
  §5.3's SHOULD and with its MUST to record the use (SPEC-0001:226-227), or a
  separate key that nothing published links to the speaker? (K-02)
- **Q-12 — a CBOR in-toto Statement (SD-15).** R-0014's `<encoding>` slot admits one in
  a non-DSSE format; the source defines none. Does the Statement layer? (§3.4
  item 4)
- **Q-13 — an import's identity.** *(inferred)* The SHA-256 of the decoded
  payload together with `payloadType`, never of the envelope text, which base64
  spellings and JSON whitespace can vary without touching the signature (S-06).
  Media types compare case-insensitively under RFC 6838 §4.2 (outside this
  source, not held in the library, not checked here); comparing `payloadType`
  in any way but byte for byte before PAE would be canonicalising inside
  verification, which R-O-05 forbids.
- **Q-14 — the ML-DSA context of an exported DSSE signature** (§6 item 2).
- **Q-15 — ECDSA signers.** Real provenance is signed with ECDSA (C-06); with
  suite 2 unspecified (SPEC-0002:360) its signer has no kid. Does R-O-01 reach
  imported objects, and if so is suite 2 owed before T-052?

---

## 10. Method, and what lacks an id

- **Ids.** Every requirement id was written as a selector, a line range and a
  fragment of the requirement's own text, and resolved by script against
  `requirements.yaml`, where both library readers agree on id, locator, lines,
  verb and text for all 29 skeleton entries. A selector that names a range no
  single requirement has, or a fragment its text lacks, stops the script. The
  resolved pairs, each id beside its full text, were then read. Selecting by
  line range is what keeps R-0017 from R-0027 and its two siblings (§8 check
  7).
- **mofn and library citations.** Every `DOC:n` range was printed back from its
  blob at `7c3c731` (or from the library worktree) by script and read beside
  its claim.
- **Quotations.** Each marker was rendered by
  `bin/check-quotes --render --only` on this file and then checked by
  `bin/check-quotes`, which reports how many it examined. No other quotation of
  the source appears here.
- **Keyword-less lines.** Pass 1 cited these by line, having only the
  skeleton's ids; pass 2 wired the ids the requirements lane gave them, each
  resolved by script and read: L21-22 R-0030, L23-24 R-0032 and R-0033 (the
  halves of R-0031), L32-33 R-0037, L46-47 R-0039, L47-48 R-0040, L56-57 R-0041
  and L82-83 R-0042, and L28-29 R-0034 (A-01). Still cited by
  line, having no id: L3-4 (the envelope as outer layer), L92-96 (examples),
  L98 (the footnote) and L101-L110 (link targets).
- **R-0009** carries two keywords, REQUIRED and MUST; this file cites it whole,
  not any split of it.

## 11. What this file decides

Nothing. No DEC-* is opened, ranked, accepted or reopened: DEC-005 stays open,
and ADR-0004 stands as accepted. No mofn file was edited. Every consequence for
mofn is marked *(inferred)* or posed as a question, and the questions belong to
their owners: Q-10, Q-11 and the §4 table to whoever takes DEC-005; Q-13 to
Q-15, §3.1 and §7 to T-051 and T-053 (BACKLOG-0001:188-190).

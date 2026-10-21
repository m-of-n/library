---
record: rfc-8392
kind: index
title: "rfc-8392 — distilled artifacts"
extracted: "2026-10-20"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what it
does not.

**State: passes 1 and 2 of 3 complete. NO `profile` IS CLAIMED.** Extract ran
2026-10-20 at effort max, one agent for the whole artifact set, reading only
`.cache/rfc-8392.txt` — never `summary.md` and never another record's
artifacts. **Verify ran 2026-10-20 at effort max**, by an independent agent that
did not extract, over all three records of the lane at once. **Pass 3
(cross-check) has not run**, and every `reviewed_by` in this directory is empty,
deliberately: under `docs/extraction.md` an unfinished extraction has no profile
at all, and that is the state of this record. The artifacts are readable and
citable; they are not buildable-on.

RFC 8392 is the base document of library#39 Tier 2's CWT envelope lane
(`rfc-8392` → `rfc-9597` → `rfc-9596`), and much the largest: 25 pages, seven
claim definitions, four IANA registrations, two numbered procedures and five
complete worked CWTs.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | every normative statement of §1–§9 and Appendix A's four presentation rules, as **37 exact runs of source lines** with per-region `sha256`, in the document's own section order. Includes all of §4's Table 1, §6's Figure 1, §9.1.1's registration template and the five registry-contents blocks. **Four sections are quoted as two or three adjacent regions** because the source's 25 five-line page breaks fall inside them (§6, §7.1, §7.2, §9.1.2); each break is declared in place and **nothing is welded across a gap.** Built with `split("\n")`, never `splitlines()`, which splits on the 25 form feeds |
| requirements | `requirements.yaml` | **110 entries, R-0001 to R-0110, in source order with no gaps: 9 `stated`, 101 `inferred`.** Counts reconcile **9 = 9** and a 4.4 kB reconciliation is written anyway, because 110 entries against 9 keywords needs explaining. All 110 texts **verified mechanically** as contiguous substrings of the whitespace-normalised source, 0 failures. The §2 BCP 14 recital is deliberately never quoted here |
| schema | `schema/` | **RFC 8392 ships no grammar** — `CDDL`, `ABNF`, `ASN.1`, `JSON Schema`, `schema` and `grammar` each occur **zero** times. One verbatim file carries the four places the document renders a structure itself (9 regions, each with its line range and digest); four derived files carry the claims set as CDDL, the envelope and its tag layers as CDDL, a JSON-projection schema for fixtures, and §9.1.1's four allocation tiers **priced in octets** from RFC 8949 §3 |
| messages | `messages.yaml` | **5 structures, 23 fields**, with the actual code points and octet-level layouts, every layout produced by decoding Appendix A rather than by reading the prose. `constrained_by` **is wired** — 55 of the 110 requirements cited, 0 dangling — which this pass could do because one agent wrote both files. The 8 empty `constrained_by` lists are a finding: every one belongs to RFC 9052 or RFC 9053 |
| protocol | `protocol.yaml`, `protocol.md` | **APPLICABLE, unlike the lane's other two records.** §7.1 and §7.2 are two numbered procedures and §9.1 is a third; all three are modelled, with a Mermaid diagram each, 24 requirement ids wired and the boundary measured (`verifier` 0, `sender` 0, `exchange` 0, `protocol` 1 — and that one is someone else's) |
| state-machine | `state-machine.yaml` | **APPLICABLE and deliberately small.** No lifecycle exists — `state`, `lifecycle`, `revoke`, `rotate` and `expiry` each occur **zero** times — but §7.2 step 6 says *"return to Step 1"* and §7.1 step 5 says *"return to Step 3"*, so there are two real loops with **different re-entry points** and one terminal failure. Both machines written out with guards and the 15 requirements that constrain them |
| examples | `examples/` | **12 vectors, and all five of the document's CWTs verify cryptographically** — see below |
| design-notes | `design-notes.md` | the `DEC-003` decision this record forces, with the type evidence; the `R-O-01` proof; 5 adopts, 5 adaptations, 5 rejections; **MD-3 mapped header by header over 12 of our fields with the registry and option-5 verdict for each**, then **five cuts against MD-3**, each naming the DEC-002 option it costs and the option that does not pay it; `DEC-005`, `R-O-03`/`R-O-05` and all six `canonical-encoding` conditions scored; the summary's six findings tested one by one; **8 source defects**; 6 open questions. **27 quotations of RFC 8392, every one cut from the cache by line range by script and verified as a contiguous substring** |

## The one result

**RFC 8392 prints five complete CWTs and all five verify.** This pass closed the
cryptography rather than deferring it:

| vector | operation | result |
|---|---|---|
| A.3 signed, tag 18 | ECDSA P-256 / SHA-256 over a 99-octet `Sig_structure` | **signature verifies** |
| A.4 MACed, `61(17(...))` | HMAC-SHA-256, 64-bit truncation | **tag reproduces** — `093101ef6d789200` |
| A.5 encrypted, tag 16 | AES-128-CCM, 13-octet nonce, 8-octet tag | **decrypts, CCM tag valid**, plaintext = A.1 |
| A.6 nested | decrypt, then verify the inner signature | **decrypts to the A.3 object byte for byte**, inner signature verifies |
| A.7 float `iat`, tag 17 | HMAC-SHA-256, 64-bit truncation | **tag reproduces** — `b8816f34c0542892` |

ECDSA P-256 arithmetic, HMAC and AES-128-CCM were **implemented for this pass**
over `hashlib` alone. **No CBOR, COSE, CWT, elliptic-curve or AES library was
used**, so a shared library bug cannot hide in the result, and the AES core was
gated on FIPS 197 C.1 (`69c4e0d86a7b0430d8cdb78070b4c55a`) before use. The
A.2.3 private key was also checked to be **the** private key for its printed
public point (`d*G == (x, y)`), and that point to be on the curve.

## What this pass corrected in the record's own summary

Two narrowings, both of them making the finding sharper, and neither of them
edited away in `summary.md` — the falsified wording is recorded in place, as
this library's convention requires.

1. **"Two of the five Appendix A CWTs are not reproducible from the printed
   key" is refuted in its stronger half.** Both MAC tags reproduce from
   Figure 6's own 32 octets of `k`. The two errata concern the key's **`kid`
   label** and **`alg` value** — metadata no HMAC computation reads. So A.2.2 is
   a **working** fixture that **fails a conformance check on its own `alg`
   declaration**. The advice to prefer A.2.3 + Figure 10 stands, because that
   fixture is self-consistent as well as working.
2. **The §9.1.1 policy-tier table's Expert Review row was flattened.** It is 5
   octets for an integer and **4 and up** for a text string; the Expert Review
   and Private Use integer rows also become **9** octets beyond ±2³². The 5×
   headline and the 35-vs-7 arithmetic survive unchanged.

## A source defect no erratum covers, found in this pass

**A.6's prose describes a header parameter the figure does not carry.** The
section says *"The content type is set to CWT to indicate that there are
multiple layers of COSE protection before finding the CWT Claims Set."*
Decoded, the object's protected bucket is `{1: 10}` and its unprotected bucket
is `{4: kid, 5: iv}` — **RFC 9052 label 3, content type, is in neither.** So the
multi-layer signal in the document's one nested example is §7.2 step 6's tag
check and nothing else. Eight defects in all are listed in `design-notes.md`
§11, including three diagnostic-notation figures that do not parse.

## Two measurements that bear on DEC-002 and were not in the summary

- **All five printed CWTs and the printed claims set are already in RFC 8949
  §4.2.1 deterministic map order.** Each re-encodes byte-identically under a
  §4.2.1 encoder, so adopting §4.2.1 costs nothing against the standard's own
  vectors.
- **None of the three printed `COSE_Key`s is.** Their keys run `-1, 1, 2, 3`
  where §4.2.1 sorts `1, 2, 3, -1`. That is a `DEC-003` trap rather than a
  `DEC-002` one: a thumbprint over the printed bytes differs from one over the
  §4.2.1 re-encoding. RFC 7049 §3.9's canonical order, which is the rule
  RFC 8392 could have cited, sorts them the same way, so the split does not come
  from the vintage of the rule.

## This pass's own quote audit

Built because the lane that wrote these summaries ran one and caught **five
transcription defects in its own prose** — an ellipsis-spliced quotation, two
silently healed line breaks, a terminal colon turned into a full stop, and an
inserted word. The audit here pulls every **unambiguously delimited** quotation
out of every artifact in all three records of the lane — markdown blockquote
runs and `*"..."*` spans, whose delimiters survive the nested `"` that RFC
sentences are full of — and probes each one against every cached source and
every library file, normalising both sides the same way.

**178 quotations audited, 169 resolved as contiguous substrings, 0 splices.**
For any fragment that did not resolve whole, the probe found its longest
matching prefix and then tested whether the remainder matched *elsewhere* — the
signature of two non-adjacent quotes welded into one. **No fragment in these
three records has that shape.**

**It found four defects in this pass's own prose, and each is corrected in
place with the falsified wording recorded:**

1. **An inserted word.** `rfc-9052`'s design notes read *"No tags" and "no
   registry dependence" are different rules, and MD-3 states the first.* All
   three of this lane's design notes quoted it with **`only` inserted**. The
   word is now added in our own voice, marked `[analysis]`, and the three
   summaries carry the same correction.
2. **An ellipsis splice**, in `rfc-9597`'s design notes. The elided clause was
   *"made based on previously unverified information"* — the most load-bearing
   part of the sentence. Now quoted whole.
3. **A silently healed line break**, in `rfc-9596`'s `examples/README.md`:
   *"CoAP Content-Formats"* written as one token where the source breaks it
   across lines 116/117. The one place in this lane that healed a break was in
   the record that declares three times that it does not.
4. **A case change** in a quotation of our own `messages.yaml`.

The nine residuals are each accounted for: three are the **superseded summary
wordings** this pass quotes in order to record them, three are the audit
regex over-running past a closing `**` into our own following sentence, one is
the ellipsis form **deliberately preserved** inside the `[correction]` note that
identifies it, and two are our own `[...]`-labelled notes set as blockquotes.

## What pass 2 should attack hardest

1. **The 110 requirement texts, one by one, against the cache.** They were
   verified mechanically here as contiguous substrings, but the `after=` /
   `upto=` spans that cut them were chosen by hand, so a span can be *verbatim*
   and still start or end in the wrong place. Three such over-runs were caught
   by a terminator check during this pass; a fourth may have survived it.
2. **The locator of every entry**, which no check in this pass tested: a text
   can be a true substring of the source and still be filed under the wrong §.
3. **The `Sig_structure` and `MAC_structure` reconstructions**, which are RFC
   9052's definitions as this pass read them, not RFC 8392's. They are the one
   place where an error would make a verified signature a false positive — so
   re-derive them from `records/ietf/rfc-9052`'s own artifacts rather than from
   this file.
4. **The AES-CCM parameterisation.** L=2, a 13-octet nonce and an 8-octet tag
   were taken from the name `AES-CCM-16-64-128`; a wrong reading would have
   failed the tag check, so this is corroborated rather than assumed — but it is
   worth re-deriving from RFC 9053 §4.2 directly.
5. **The claim-key cost table**, recomputed from RFC 8949 §3 rather than from
   `schema/claim-key-policy.derived.yaml`. One cell of its predecessor was
   already wrong.

---

## What pass 2 did, and what it found (2026-10-20, independent, effort max)

Pass 2 answered all five, in order.

**1. The 110 texts, re-derived.** All 110 are contiguous verbatim spans of the
whitespace-normalised source — re-derived, not inherited. A tightened
terminator check over all 110 found **no fourth over-run**. Three suspects
remain and all three are legitimate: `R-0022` is the one deliberate
mid-sentence start and is declared in its own `note`; `R-0101` and `R-0105` are
complete IANA registry templates that end at their last field
(*"Provisional registration? No"*, *"Point of Contact: …"*), confirmed against
§9.2.1 and §9.4.1.

**2. Every locator — and under a stricter rule than the tool applies.**
`bin/check-locators` permits a text that really lives in §3.1.4 to be filed
under §3. Pass 2 computed the **innermost** containing section for every entry
and compared: **0 misfiled, 0 imprecise, 0 unresolvable.** The two
*unresolvable* rows `bin/check-locators` reports for `Appendix A.1` and
`Appendix A.2` are a **gap in the tool, not a defect in this record**: an RFC
`.txt` rendering prints sub-appendix headings bare (`A.2.1.  128-Bit Symmetric
Key`), and the tool's `APPENDIX` pattern requires the literal `Appendix`
prefix, so every locator naming a sub-appendix goes unchecked library-wide.
Pass 2's own scan resolves all 41 of this document's headings and finds both
locators correct.

**3. `Sig_structure` and `MAC_structure` — re-derived from `rfc-9052`, not from
here.** Both were rebuilt from `records/ietf/rfc-9052/distilled/schema/cose.cddl`
(§4.4 and §6.3) and its `normative.md`, and `Enc_structure` from §5.3. They
agree with what this record used. **The structures are now printed beside every
outcome**, and **eleven negative controls were added** — a `"Signature"`
context for `"Signature1"`, a wrongly included `sign_protected` field,
`external_aad` and `payload` transposed, the unprotected map folded in as a
fifth field, the payload signed bare, and the analogous wrong
`MAC_structure`s and `Enc_structure` AADs. **All eleven correctly fail.** So
the A.3 result is not a false positive, and the unprotected bucket is
**provably** not a signature input — which is the mechanical proof of
`rfc-9597`'s headline, obtained here rather than asserted there.

**4. AES-CCM, re-derived from RFC 9053 §4.2 rather than from the name.** §4.2's
own prose fixes L and Table 6 fixes the rest: **L = 16 bits (2 octets), M = 64
bits (8-octet tag), 13-byte nonce, 128-bit key.** Confirmed. Pass 2 also added
an external **CCM** known-answer test pass 1 did not report using — RFC 3610
packet vector #1 — because FIPS 197 C.1 gates the block cipher but says nothing
about the mode.

**5. The claim-key cost table, recomputed by encoding.** Ten of eleven cells
confirmed; **one corrected.** The Expert Review text row read *"1 + length
thereafter"* with no bound, but an RFC 8949 text head is 1 octet only to length
23, so a 24-character key costs **26** octets, not 25. The 5× headline, the
35-vs-7 arithmetic and the absence of any Private Use range for text keys all
survive. That row has now been wrong twice in two successive passes.

**The five-CWT result is independently reproduced.** A second crypto stack
sharing no code with pass 1's — SHA-256, HMAC, AES-128 with the S-box derived
from its GF(2⁸) definition rather than tabulated, CCM, P-256, ECDSA and a CBOR
codec, all from scratch — reproduces every one. 23 primitive gates pass first
(FIPS 180-4 B.1, RFC 4231 TC1/TC2, FIPS 197 C.1 and A.1, RFC 3610 vector #1,
RFC 8949 Appendix A, and two independent scalar-multiplication routines
required to agree). 52 CWT checks run and 50 pass; the two failures are pass 2's
own assertions written from **Figure 7's diagnostic notation**, and they
re-confirm defect **D-1** from the hex side — Figure 6's bytes put `kid` at
label 2 and `alg` at 10, exactly as `design-notes.md` says.

**The A.2.2 refutation is confirmed.** Both MAC tags reproduce from Figure 6's
own 32 octets of `k`, and pass 2 added the control that makes it sharp: the same
tags do **not** reproduce from A.2.1's 128-bit key, so `k` is load-bearing and
the metadata is not.

**All 37 `normative.md` regions and all 9 schema regions re-verified** — digest
**and** printed block byte-identical to the cache, which a digest check alone
would not catch. **Body source-line coverage was computed**: the only uncovered
lines in §1–§9 are the section headings themselves, so no statement is dropped.

**Two defects pass 2 found that pass 1 did not look for.**

1. **Two of this record's eight artifacts did not parse.**
   `bin/_record_yaml.py` rejected `protocol.yaml` and `state-machine.yaml`
   outright, so the reader `bin/check-locators` imports could not read the
   protocol model or the state machine at all — while `bin/validate` reported
   nothing, because it checks only that an artifact's **path exists**. The cause
   was eight wrapped double-quoted sequence items and three unescaped inner
   quotes, including four inside the very `absent:` list that sits one file away
   from this directory's own warning about the hazard. All fixed; all 17 YAML
   artifacts in the lane now parse with **both** readers, and 2918 leaf paths
   were compared value by value with **0 key-set mismatches**.
2. **A double-escaped apostrophe.** `requirements.yaml` R-0022's note read
   `ENTRY''''''S`, which a single-quoted YAML scalar decodes to `ENTRY'''S`. A
   sweep of the whole class across all 17 artifacts found it as the **only**
   instance.

### Pass 2's own lane-wide audits

Run over the lane, not per record, because a per-record audit fixes one of
three and never suspects a pattern — which is exactly how pass 1's inserted
`only` reached all three design notes and all three summaries.

**Quote audit: 291 delimited quotations across all 48 files of the lane; 289
resolve whole as contiguous substrings; 2 unresolved and both are our own
`[...]`-labelled notes set as blockquotes, not quotations. Zero splices.** The
discriminator pass 2 added is a **named-relaxation channel**: any fragment that
did not resolve whole was retried under four named relaxations — terminal
punctuation swapped, a hyphenation break healed, a line break healed into one
token, case folded — so the defect class would be *reported* rather than
masked. **Zero fragments needed any relaxation.** That is the positive result:
none of the four transcription-defect classes this lane's audits were built to
catch survives anywhere in it. Pass 1's `only` correction was verified as
correctly applied in all six places, and pass 2 traced the word's provenance —
it is `rfc-9053`'s design notes restating the point **in their own lowercase
voice**, where `only` is legitimate, so nothing in `rfc-9053` is defective
either and the attribution was the only error.

**Id join audit: every id emitted from the three requirements tables by script,
then 456 references resolved and printed beside their requirement's own text
for reading. 0 dangling, and 0 resolving to the wrong statement.** The sibling
lane's 30 wrong-but-resolvable ids came from one record's layout being in
working memory and another's not, so pass 2 also flagged every **bare**
reference whose number exists in a sibling record — 70 of them — and checked
each in context. All 70 are inside their own record's files, where the bare form
correctly means the owning record.

**YAML reader audit: all 17 YAML artifacts in the lane parsed with both
`bin/_record_yaml.py` and `bin/_yaml.py`, flattened to leaf paths, and compared
value by value — 2918 leaf paths, 0 key-set mismatches.** The detector was
proved non-blind on synthetic positive controls first, because a clean result
from an untested detector is worthless. **No inline flow map exists anywhere in
the lane** and **no wrapped flow collection remains**: all 27 flow collections
are empty `[]` and close on their own line. The 178 remaining value differences
are all `int`/`bool` versus `str` typing — a difference between the two readers,
not a mangling of our data.

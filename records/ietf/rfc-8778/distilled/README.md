---
record: rfc-8778
kind: index
title: "rfc-8778 — distilled artifacts"
extracted: "2026-10-20"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what it
does not.

**State: PASSES 1–3 COMPLETE. `distillation.standard: FX-1`, and whether a
`profile` is declared is the record owner's call on this report** — an
unfinished extraction is neither `full` nor `partial` and the gate says so
(`docs/extraction.md`, *`profile: partial` is a terminal state*). Extract ran
2026-10-20, one agent, alone, at effort `max`, reading only
`.cache/rfc-8778.txt`; **verify** 2026-10-21, adversarial and independent
(*Defects pass 2 found*); **cross-check** 2026-10-21 (*Defects pass 3 found*).
**No human has reviewed any of it** — every `reviewed_by` in this directory is
empty, and pass 4 is that review.
*(Corrected 2026-10-21, FX-1 pass 3: this block read "PASS 1 OF 3 COMPLETE …
No verify pass and no cross-check pass has run" in the same file as a
*Defects pass 2 found* section. The identical stale sentence stood in
`record.yaml`, `requirements.yaml`'s `note` and `summary.md` — one correction
that reached nothing, in four files at once.)*

RFC 8778 is a 772-line binding with **9 BCP 14 keywords**, and its substance is
in the two sections that carry none of them: §2 specifies the public-key octets
that RFC 9679 §4.5 requires and does not cite, and §5 describes a namespace root
with a counted lifetime and, deliberately, no private-key serialisation at all.
This extraction's job was to make both measurable rather than argued.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | every normative sentence of the Abstract, §1–§6 and Appendix A with its locator, plus **25 byte-exact fenced runs of source lines** for every bullet list, concatenation rendering, registration template and the whole of §4's state paragraph and §5. Four line-break severances declared and not healed. Nine source observations. |
| requirements | `requirements.yaml` | **135 entries, all 9 BCP 14 keywords, counts reconciled exactly** (8 MUST, 1 MAY; `source_keyword_count` = `extracted_keyword_count` = 9). 9 `stated`, 126 `inferred` with the carrier named in `field`. **Every `text` is verbatim and every locator resolves inside its section**: `bin/check-locators` reports 135 checked, 0 misfiled, 0 unresolvable. No derived quantity is in this file — see below. |
| schema | `schema/` | **RFC 8778 ships no grammar of any kind** — `ABNF` 0, `ASN.1` 0, `JSON Schema` 0, `CDDL` 1 (a reference title). One verbatim file carries the document's 20 structural renderings; the other six are the library's own and carry `.derived.`. 14 CDDL rules across three files (13 distinct), 21 ABNF rules, one JSON Schema, one parameter-set table. `schema/README.md` has the per-file table and the full width derivation. |
| messages | `messages.yaml` | **11 structures, 35 fields**, with offsets, encoded sizes and the CBOR head bytes: the 56-octet public key, the subordinate key, all three signature layers, both HSS signature forms, the `COSE_Key`, the RFC 9679 §4.5 thumbprint input, and both Appendix A envelopes. `constrained_by` **is wired**: 30 of 35 fields carry at least one `rfc-8778#R-NNNN`, 43 distinct ids cited, 0 dangling. The 5 empty lists are RFC 8152's fields and are a finding, not an omission. |
| protocol | `protocol.yaml`, `protocol.md` | **NOT APPLICABLE, with the measurement written out.** `protocol`, `exchange`, `verifier`, `sender`, `recipient`, `party`, `role`, `flow`, `step`, `procedure` each occur **0** times; `signer` 3 and `request` 1 (the masthead). No signing or verification algorithm is given — both are cited to `[HASHSIG]` by section — and the document never says where the signature octets go. `protocol.md` carries a Mermaid **state** diagram as a reading aid for `state-machine.yaml`, labelled as such. |
| state-machine | `state-machine.yaml` | **APPLICABLE, and it is the reason this record is useful.** Two machines — one LM-OTS leaf (4 states, 4 transitions) and the HSS key / trust anchor (5 states, 6 transitions) — with 2 error states, 2 `forbidden_transitions` and **5 explicitly `unspecified`** behaviours. The word-count measurement that would have supported declaring N/A is written out and rejected: `lifecycle`, `revoke`, `rotate`, `expire` and `exhaust` are all 0, and **eight requirements in six groups** define a lifecycle anyway. |
| examples | `examples/` | **11 vectors, 4 byte fixtures, and both of the document's stated sizes reproduced exactly** — 2560 and 2552 octets by re-encoding the printed diagnostic notation under RFC 8949. Both signatures parse to 2512 octets against the document's own renderings. **The u32str width, which no document in this library states, is measured here.** Plus two negative observations and one positive test of `R-0061` that passes. Two vectors are `source: template` because **no key is printed anywhere in RFC 8778**, so nothing was synthesised. |
| design-notes | `design-notes.md` | the three-leg reproduces/refutes/bounds result against `rfc-9964`; `DEC-003`'s sixth answer; `R-M-02`'s inverted size trade; `ARCH-0002` P1's counted namespace root; `R-O-01`'s per-object price; `DEC-005`; `R-M-12`, `R-O-03` and the `canonical-encoding` conditions (0) and (1)–(6) one by one; **six cuts against `MD-3`, each naming the `DEC-002` option it moves**; one marked `[inference]` about replicated signers; seven open questions; the sibling records re-derived; the nine source defects. |

## The one result

**RFC 8778 both reproduces and bounds `rfc-9964`'s headline finding, and it
refutes that record's escape clause.**

`rfc-9964` found an IANA allocation inside a post-quantum `KeyId` — COSE `alg`
−48/−49/−50 — and concluded that "An AKP `pub` is `alg`-independent", in a
sentence its own correction block records as having first read "A raw `pub` is
`alg`-independent, so" with no key type named. Here the allocation
is in the **key material**: §2.2 `R-0053` puts `u32str(lms_algorithm_type) ||
u32str(otstype)` at the front of the public key, and §2.2 `R-0046` and §2.3
`R-0077` say those index IANA registries. §2.1 `R-0024` makes that the HSS public
key too.

| leg | verdict |
|---|---|
| **reproduces** | yes, by a **different mechanism** — in the key octets, where no digest-input choice reaches it. `DEC-003` option 1 carries it, option 2 digests it, and `rfc-9964`'s `(kty, pub)` escape digests it too |
| **refutes** | yes — `alg`-independence of a raw `pub` is true for AKP and **false for HSS-LMS**. The immunity is a property of a key type's encoding, not of an option |
| **bounds** | yes, twice — COSE `alg` −46 is **not** in the preimage (§3 `R-0087` makes `alg` conditional; RFC 9679 §4.5 requires only `kty` and `pub`), and there is no "same key material under two algorithms" here because relabelling the parameter set changes `T[1]` with it |

`records/ietf/rfc-9964` and `records/ietf/rfc-9679` were **both narrowed on
2026-10-20 on the strength of exactly this, before this pass ran**. This pass
re-derived both narrowings from the source and they stand. **Neither record was
edited by it.**

## The 56 octets, and the one width no document this library holds states

| field | octets | provenance |
|---|---|---|
| `u32str(lms_algorithm_type)` | 4 | **measured** |
| `u32str(otstype)` | 4 | **measured** |
| `I` | 16 | **stated** — §3 `R-0092` |
| `T[1]` | 32 | **arithmetic** — §2.2 `R-0052` with `R-0039` |
| **total** | **56** | for all 20 parameter-set combinations RFC 8778 admits |

RFC 8778 never defines `u32str` — `R-0028` defers the notation to `[HASHSIG]`,
and `records/ietf/rfc-8554` is a **stub** with no digest and no cached bytes, so
the document the notation is deferred to is one this library holds a record for
and not the text of. *(Worded that way deliberately, 2026-10-21, FX-1 pass 3:
whether RFC 8554 states the width is itself unverifiable here. What is
verifiable is that **RFC 8778 does not**, and that is all the measurement
below needs.)* So the width was recovered from RFC 8778's own arithmetic
against its own printed bytes, in **two legs** — `2512 − 4u − 32` is divisible
by 32 for `u = 4` and for no other `u` in {1, 2, 8}, *and* octets 0–3 of both
signatures are `00000000` (§2.1 `R-0027`'s `u32str(0)`) with the two first
differing at octet 7, the leaf number `q`. `h = 10` and `p = 67` follow.
**[correction] 2026-10-21, FX-1 pass 2: six places in this record stated the
first leg as uniqueness ("the only width"). It is not — the congruence reduces
to `u ≡ 4 (mod 8)`, so 12, 20 and 28 also pass. The second leg is what pins it,
and the pass had measured it without using it.** **A normative structure
dimensioned by a non-normative appendix.**

And the consequences, measured: a 56-octet key is **24 octets larger than its own
SHA-256 thumbprint**; a minimal `COSE_Key` carrying it is **byte-identical** to
its RFC 9679 §4.5 thumbprint input (both 62 octets); and the signature is **2512
octets for a 20-octet payload**. `R-M-02`'s size trade inverts against
`rfc-9964`'s.

## Verification

**A CBOR encoder and decoder written for this pass** (RFC 8949 §3 and §4.2.1)
over the Python standard library alone. **No CBOR, COSE, CWT or HSS/LMS library
was used.**

- **Both stated example sizes reproduce exactly** — 2560 and 2552 octets — and
  both re-encoded messages decode fully to tag 98 and tag 18 with a 2512-octet
  signature byte-identical to a fresh cut from the source.
- **135/135 requirement texts** are contiguous spans of the whitespace-normalised
  source; **135/135 locators** resolve inside their stated section
  (`bin/check-locators`: 0 misfiled, 0 unresolvable).
- **The keyword count reconciles exactly**: `bin/bcp14-count` reports 9 (8 MUST,
  1 MAY) and the entry texts contain 9, recomputed the way `bin/validate` does.
- **A quote audit over every artifact in this directory**: pass 1 reported 225
  quotations against ten corpora, 0 not verbatim.
  **[correction] 2026-10-21, FX-1 pass 2: that breakdown does not sum, and the
  total is not reproducible from any method this record states.** It read
  "225 quotations ... 194 are RFC 8778's; 25 are the sibling records' ...; 5 are
  this library's own process documents; 1 is `topics/canonical-encoding.yaml`'s;
  and 8 are quotations of `mofn` documents this repository does not hold" —
  194 + 25 + 5 + 1 + 8 = **233**. The `mofn` 8 are also, by construction, not
  checkable here at all, so "0 not verbatim in any of them" cannot cover them.
  Pass 2 re-ran the audit as whole spans, longest first, attribution-aware, over
  every file in this record: **396 spans of ≥30 normalised characters resolve
  exactly, 20 do not, and of those 20 exactly one is a quotation defect** (see
  *Defects pass 2 found* below). All but that one are JSON `description` strings
  and front-matter titles that the extractor treats as quoted spans, or this
  record's own superseded wording quoted inside a declared `[correction]` block.
  **[correction] 2026-10-21, FX-1 pass 3: the 194/41/25 tallies are deleted, and
  so is any total.** They were the last unreproducible figures here, and no
  method reproduces them because a delimited-span count over this directory is
  dominated by YAML scalar *values* — `name:`, `encoding:`, `locator:` — that
  are not quotations at all. Pass 2's own 416/396/20 is the same shape: it
  counts whatever its extractor admitted, and it was measured over files pass 2
  then edited. `design-notes.md`'s opening block now states **three checks that
  recompute** instead: 135 of 135 requirement texts verbatim and each occurring
  exactly once; 11 of 11 markdown blockquotes verbatim; and every
  foreign-attributed span resolved against the document it names **with this
  record's own files excluded** — which is the audit that found two markup
  insertions pass 2 had left (*Defects pass 3 found*).
- **An id join audit** resolving every cited id to its requirement's text and
  reading the pairs: **0 dangling, 0 foreign-id collisions**, and pass 2 read
  all 30 `constrained_by` wirings in `messages.yaml` against the 43 requirement
  texts they name — every one resolves to the statement meant. Pass 1 measured
  **127 of 135** ids cited outside `requirements.yaml`; the 8 uncited were
  `R-0010`, `R-0011`, `R-0012` (§1.1 motivation) and `R-0042`, `R-0043`,
  `R-0044`, `R-0074`, `R-0075` (parameter-set-name rows).
  *(Corrected 2026-10-21: pass 1 gave the enclosing ranges `R-0041`…`R-0045`,
  `R-0073`…`R-0076` instead, which name nine ids of which four are cited.
  Naming the eight here is itself a citation of each, so **this metric is not
  stable under prose that discusses it** — the live figure is now 135 of 135,
  and the number worth keeping is the 0 dangling.)* Pass 2 also resolved every
  **bare** `R-NNNN` / `V-NNNN` / `S-NNNN` reference — the form
  `bin/check-id-joins` does not collect — by script: **0 dangling**, over 570-odd
  of them, with V-0001…V-0011 and S-0001…S-0011 all defined. No exact total is
  recorded on purpose: it counts references in prose that itself cites ids, so
  any edit to this directory changes it, and a number like that is a fossil
  waiting to happen.
- **`bin/check-id-joins`, both modes, which did not exist when this pass
  started.** `--resolve`: **469 citations, 0 dangling** (468 as pass 1 left it;
  pass 2's corrections added one). `--surface`: **0
  duplicate-text groups** — no two of the 135 requirements share identical text,
  so there is nowhere left in this record for a wrong id to resolve to a
  statement that happens to match the quoted words. That was the one residual
  risk the hand-rolled join audit could not close, and the tool closes it.
- **Every YAML artifact round-trips through BOTH of the library's readers**,
  `bin/_yaml.py` and `bin/_record_yaml.py`, which agree on every structure.

## Defects this pass found in its own work

Three, all caught by the mechanical checks rather than by eye, and recorded
because the checks are the point.

1. **`parameter-sets.derived.yaml` was unparseable by `bin/_record_yaml.py`** —
   flow maps spanning two lines. Caught by `bin/validate`'s warning — "An
   artifact no reader can read is not an artifact." — and it is block mappings
   now.
2. **A quotation spliced across two different documents.** `examples/README.md`
   and `examples/vectors.yaml` both quoted FX-1's examples requirement as
   — falsified wording, preserved as a code span so it cannot be mistaken for a
   quotation — `every example in the source as a fixture file ... hex for
   binary`. The first half is `docs/extraction.md`'s and the second is
   `.claude/skills/extract/SKILL.md`'s.
   The quote audit's longest-prefix test found it; both are now quoted separately
   and attributed separately. **This is the vCon failure mode (2026-09) occurring
   across two documents rather than two sections of one.**
3. **Two elided quotations of RFC 8778 marked with `...`.** One in
   `messages.yaml`, one in `schema/parameter-sets.derived.yaml`. Both now quote
   the whole clause. *(Corrected 2026-10-21: there is a **third**, in
   `summary.md`'s overview — "deliberately not defined… to avoid creating the
   ability to save the private key and state" elides ". It was not defined"
   behind a U+2026 ellipsis. It is visible rather than silent, and `R-0115` and
   `R-0116` carry the two sentences whole in `requirements.yaml`, so it is left
   in place and declared here instead of counted as fixed.)*

## Defects pass 2 found

Pass 2 (verify) ran 2026-10-21 at effort `max`, adversarially, reading only
`.cache/rfc-8778.txt` and the artifacts. **The keyword count, every locator,
every verbatim text, all 45 region digests, all 4 fixtures and the `protocol`
not-applicable verdict all held.** What did not:

1. **`record.yaml` still read `00000003` as `LMOTS_SHA256_N32_W8`** — the one
   claim `summary.md`, `examples/README.md` and `examples/vectors.yaml` had each
   already corrected. Pass 1 propagated the correction to three artifacts and
   left it standing in the fourth, inside a `bears_on` warrant. Fixed.
2. **`record.yaml` and `summary.md` quoted `rfc-9964` with a sentence that
   occurs in neither its current text nor its own record of the superseded
   text.** `record.yaml`'s version welded that record's retracted opening ("A
   raw `pub` is `alg`-independent, so") to its corrected tail with "for AKP
   keys" deleted, restoring the over-general claim the correction exists to
   retract. `distilled/README.md` and `design-notes.md` were right throughout.
   Both fixed.
3. **The `u32str` uniqueness argument was an over-claim in six places.** The
   divisibility test holds for every `u ≡ 4 (mod 8)`. Fixed, with the second
   leg (the printed leading octets) written out where the claim is made.
4. **Four count fossils**: "six `can be summarized as` renderings" (there are
   **five** — `source-renderings.txt`'s own "those eleven blocks" only sums with
   five); "the ten parameter-set names" (**nine**: five tree sizes, four LM-OTS
   variants); the 225-quotation breakdown above; and "the 11 `constrained_by`
   wirings in `messages.yaml` that cite more than one id" (**28** fields do,
   across 10 of the 11 structures).
   *(Corrected 2026-10-21, FX-1 pass 3: this item read "each fixed at every
   site", and the renderings fossil was not. `source-renderings.txt` carried
   "rendering 1 of 6" … "rendering 5 of 6" on its five block headers, plus
   "rendering 6 is 2.1's u32str(0) form" — which names rendering 1 a second
   time. The source has exactly five occurrences of `can be summarized as`, at
   lines 173, 181, 235, 258 and 308, and the five labelled blocks are exactly
   those five. The headers now read "of 5" and the phantom sixth is gone. The
   other three had in fact reached every site.)*
5. **`R-0132`–`R-0135` were filed at `Appendix A` when they live in A.1 and
   A.2**, which `bin/check-locators` passes because A contains A.1. `R-0133`'s
   note also claimed "the sentence appears twice in the document ... so the
   locator is the disambiguator": every one of the 135 texts occurs **exactly
   once** in the normalised source, and `Appendix A` was the locator on both
   anyway. Fixed.
6. **`normative.md` carried no §1.1 section at all** although `R-0010`–`R-0013`
   are §1.1 entries, while `record.yaml` claimed "every normative sentence of
   the Abstract, §1–§6 and Appendix A". Four of §1.1's eight sentences were in
   no artifact of this record. A sentence-level sweep of the Abstract, §1–§6 and
   Appendix A against every artifact resolved **137 of 143** units; §1.1 is now
   a section of `normative.md` carrying all eight sentences — four with their
   entries, four with none, like the Abstract and the §1.2 recital — and the
   sweep resolves **141 of 143**. The two residuals are the Appendix A
   diagnostic-notation blocks, which this record carries in pieces rather than
   as one span.
7. Two smaller ones: `schema/README.md` said `%x00-FF` was the ABNF's only
   terminal (`%x00.00.00.00` and `%x00.00.00.01` are terminals too), and Cut A
   gave one percentage, 1.6%, for two envelope overheads (48/2560 = 1.9%,
   40/2552 = 1.6%).

## What pass 3 was asked to attack hardest

Named by pass 2 so the cross-checker did not have to find them: whether every
`messages.yaml` field name appears in the schema files and vice versa (pass 2
read all 30 `constrained_by` wirings and every one resolves to the right
statement, but did not close the field↔schema direction); whether every
state-machine trigger is a defined event; the two `source: template` vectors,
the only places here where a structure is asserted with no value behind it;
and whether the corrections above reached **every** artifact stating the same
claim — that is the failure mode this record has already exhibited once.

## The four closures (FX-1 pass 3, 2026-10-21, effort `max`)

`docs/extraction.md` defines pass 3 as four closures. All four close.

**(a) Every field a requirement names exists in `messages.yaml` or
`distilled/schema/` — and the reverse, which pass 2 left open.**

*Forward.* Harvested by script from the 135 requirements' `object` and `field`
keys: **19 distinct field-level names** — `lms_algorithm_type`, `otstype`, `I`,
`T[1]`, `T[r]`, `C`, `y`, `q`, `ots_signature`, the LMS `type` code, `path`,
`Nspk`, `lms_signature`, `signed_public_key`, `pub`, `kty`, `alg`, `kid`,
`key_ops`. **18 of 19 are fields of `messages.yaml`**; the nineteenth, `T[r]`,
is not a wire field at all — it is `T[1]`'s generic form (`R-0050` defines the
node value, `R-0052` names the root instance), carried in `normative.md` and in
`source-renderings.txt`. **19 of 19 have a representation in
`distilled/schema/`.** Separately the requirements name **7 scalar parameters** —
`h`, `m`, `n`, `p`, `w`, `ls`, `H`. Five were rows in
`parameter-sets.derived.yaml`; `ls` and `H` were in `distilled/schema/` only as
the verbatim §2.3 block in `source-renderings.txt`, which satisfies the closure
by the letter while their siblings `n`, `w` and `p` had structured rows. `ls` is
**now a row on all four LM-OTS variants**, and `H` is named in that table's
header with the reason it is not one — it is SHA-256 for every variant, not a
per-row value. **26 of 26 closed** — `ls` and `H` only after this pass.

*Reverse.* `messages.yaml` carries **11 structures and 35 fields**, **24
distinct field names**. **All 24 have at least one counterpart in
`distilled/schema/`** — as a CDDL member key, as an ABNF rule (kebab-cased:
`ots-signature-p67` for `ots_signature`, `T1` for `T[1]`, the base rule
`path`/`y` for the indexed forms, `nspk-zero`/`nspk-one` for `Nspk`), or as a
JSON Schema property. The four RFC 8152 common parameters (`kty`, `alg`, `kid`,
`key_ops`) appear in `hss-lms-cose-key.derived.cddl` as their integer labels
with the name in the comment, which is the only form CDDL admits for a COSE
map. The 25th entry, S-0002's `(as S-0001)`, is a reference to S-0001's four
fields rather than a name of its own.
**0 field names in `messages.yaml` with no schema counterpart; 0 schema rules
with no field or structure behind them.** 14 CDDL rules across three files, 13
distinct (`hss-lms-pub` is defined identically in two); 21 ABNF rules, closed;
7 JSON Schema properties — every count as `schema/README.md` states it.

**(b) Every message in a protocol flow is defined in `messages.yaml` —
vacuous, and the `protocol` N/A verdict that makes it vacuous holds.** Pass 2
re-derived that verdict and every word count behind it; pass 3 **confirmed
rather than redid** it, re-measuring the counts as whole words over all 772
lines: 17 role/flow words at **0**, `signer` **3** (lines 91, 159, 394),
`request` **1** (line 6), `subject` **1** (line 41), `validation` **1** (line
325), `validate` **0**, `Sig_structure` / `header` / `tag` / `COSE_Key` **0**,
`kty` **1** (line 330), `pub` **1** (line 443). `roles`, `flows` and
`error_paths` are all empty lists, so there is no flow to close over.

**(c) Every state-machine trigger is a defined message or a named event.**
2 machines, 9 states, **10 transitions**, **5 distinct trigger events** —
`sign`, `publish_as_trust_anchor`, `establish_new_trust_anchor`,
`state_management_approach_sacrifices_the_node`, `tracking_data_integrity_loss`.
None is a message, correctly: the document defines none. **All 5 are named
events, each carrying `constrained_by` R-ids that resolve** (`sign` ←
`R-0101`/`R-0097`/`R-0111`; the others ← `R-0109`/`R-0100`/`R-0108`, `R-0110`,
`R-0113`/`R-0112`, `R-0098`/`R-0099`), and all 5 appear in `protocol.md`'s
diagram. Every transition endpoint is a declared state and every declared state
has a `state_meanings` entry — 9 of 9.

**(d) Every example validates against `distilled/schema/`.** Both printed
signatures parse against `hss-lms-octets.derived.abnf`'s
`hss-signature-standalone-p67-h10` with **2512 octets consumed and nothing left
over**; both whole messages decode against
`hss-lms-cose-envelopes.derived.cddl` to tag 98 and tag 18 with **0 trailing
octets**, the inner `signature` byte-identical to a fresh cut from the source;
`V-0007`'s two protected buckets round-trip; `V-0010`'s prefix `a20105205838`
is what an RFC 8949 §4.2.1 encoder emits for `{1: 5, -1: bstr(56)}`, 62 octets.
Re-encoded with an independent encoder written for this pass: **2560 and 2552**,
matching `R-0133` and `R-0135`. **The derived JSON Schema has no instance to
validate**, because `V-0009` is `source: template` and the document prints no
key — stated here rather than left as a silent gap.

## Defects pass 3 found

Nine, every one in this record's prose and none in the source, and
`bin/validate` reported none of them. **Five are the propagation failure pass 2
named**: a claim corrected in one artifact and left standing in another.

1. **The "six renderings → five" fossil had not reached its own file.**
   `schema/source-renderings.txt` line 18 carried pass 2's "five `can be
   summarized as` concatenation renderings" while its five **block headers**
   still read "rendering 1 of 6" … "rendering 5 of 6", the last adding
   "rendering 6 is 2.1's u32str(0) form" — which names rendering **1** a second
   time. The source has exactly five occurrences of `can be summarized as`, at
   lines 173, 181, 235, 258 and 308, and the five labelled blocks are exactly
   those five. Headers now read "of 5"; the phantom sixth is gone. *This file's
   own claim that the four fossils were "each fixed at every site" was the
   blanket claim that hid it.*
2. **The ninth u32str site.** Pass 2 corrected the uniqueness over-claim in
   eight places; `schema/hss-lms-public-key.derived.schema.json`'s
   `description` still read "the only u32str width that makes the printed
   2512-octet signature an integer number of 32-octet elements" — unscoped,
   with neither the `{1, 2, 8}` bound nor the second leg. Corrected, with both
   legs named. **A `description` string is where a correction goes to die:** no
   reader of the schema sees it and no grep for prose finds it.
3. **Four files still said the verify pass had not run**, each in the same file
   that records pass 2's work: `README.md` ("No verify pass and no cross-check
   pass has run", above a *Defects pass 2 found* section), `record.yaml` ("FX-1
   PASS 1 OF 3 ONLY … verify and cross-check have NOT run", above a `passes`
   list containing the verify pass), `requirements.yaml`'s `note` ("No pass 2
   and no pass 3 have run", above a `reconciliation` beginning "RE-MEASURED BY
   PASS 2"), and `summary.md`. All four corrected.
4. **`README.md` said "six requirements define a lifecycle"** where
   `state-machine.yaml` and `record.yaml` both carry pass 2's "**eight**
   requirements in six groups". Corrected.
5. **`requirements.yaml` said `state` and `statefulness` occur "all inside
   §4-§5"**, the wording `state-machine.yaml` had already corrected. Measured:
   all five occurrences are in **§5**, at lines 394, 397, 403, 405 and 406; §4
   (lines 344–382) has none — which is the sharper fact, since §4 states the
   one-time-use and tracking obligations without ever using the word.
6. **Two markup insertions inside foreign quotations**, found only by resolving
   each quotation against the document it names **with this record's own files
   excluded**. `design-notes.md` §8 quoted `MD-3` as "carried as **ordinary map
   entries**" and §7 quoted `DEC-005` as "Envelope for `` `ArtifactStatement` ``";
   both are plain in every other copy in the library (`rfc-9964` and
   `records/community/draft-mcnally-deterministic-cbor`), while the **same**
   `MD-3` sentence's own `**export**` bold *is* reproduced correctly. Both now
   plain, and the convention is stated in `design-notes.md`: **reproduce the
   quoted document's markup, add none** — a reader cannot tell an added emphasis
   from the source's own.
7. **Three `region_sha256` values did not digest the run their `locator`
   named.** `V-0006` carried a digest of lines 584–658 beside a locator naming
   **no** line range at all, although the vector compares A.1's *and* A.2's
   paths; `V-0007`'s digest is of lines 565–662 while its locator names
   571–573, 578–580 and 672–674 — the last of which that region does not
   contain; `V-0005` names three runs and digests the second. The file's own
   header says "`locator` gives … the exact line range … and the sha256 of that
   run of lines". Each now carries `region_sha256_covers` naming the run it
   digests and the digests of the runs it does not.
8. **The 194 / 41 / 25 quotation tallies are deleted**, not re-estimated. Pass 2
   found the breakdown they belong to sums to 233 against a stated 225 and left
   them with the flaw declared. No method reproduces them and none can: a
   delimited-span count over this directory is dominated by YAML scalar
   *values* that are not quotations. `design-notes.md` now carries three checks
   that recompute instead, each with its method.
9. **Three facts asserted about RFC 8554 were flagged at one site and asserted
   at five.** That Appendix B gives `p = 67` for `w = 4` and `p = 34` for
   `w = 8` — **load-bearing for the W8 refutation** — was unflagged in
   `summary.md`, `examples/README.md`, `examples/vectors.yaml` and
   `schema/parameter-sets.derived.yaml`; that Appendix F prints LMS public keys
   was unflagged in `examples/README.md`. All now flagged, with the split made
   explicit: **the refutation has a floor that needs no second document** —
   RFC 8778 prints no code point for any of its nine names, so `00000003`
   resolves to neither `W8` nor `W4` — and `p = 67` itself is measured from the
   printed bytes. Only the *naming* of 67 as the `w = 4` count depends on
   RFC 8554. `bin/fetch-source` cannot close it: `records/ietf/rfc-8554`'s
   `content.sha256` is empty, so there is no digest to verify fetched bytes
   against, and its `content.url` is the HTML page rather than the `.txt`.

**What pass 3 checked and found sound**, so a later pass need not redo it: all
45 region digests **and** every printed block byte-for-byte against its declared
line range (20 in `source-renderings.txt`, 25 in `normative.md`); all 4 fixtures,
including a fresh cut of both printed signatures; the whole structural parse
(`Nspk` 0, `q` 1/0, `otstype` 3, `C` identical, 67 `y` elements of which **0 of
67** match across the two, type code `00000006` at 2188, 10 path nodes from 2192
of which **9 of 10** match, a 288-octet common suffix = 9 × 32, 2180 / 2508 /
2512); every derived figure (56, 62, 32, 24, 30, 48, 40, 125.6×, 44.9×, 78.5×);
`bin/bcp14-count` 9 = 9 with the nine at lines 330/332/334/337/340 and
352/354/362/365; `bin/check-locators` 135/135, 0 misfiled; `bin/check-id-joins`
`--resolve` **469 citations, 0 dangling**, `--surface` 0 duplicate-text groups,
`--quote-join` **0 pairs to read**; **609 unqualified references** (568 bare
`R-`/`V-`/`S-` plus 41 short `#R-`), **0 dangling**, the form `--quote-join`
does not collect; 135 of 135 requirement texts verbatim and each occurring
**exactly once**; 11 of 11 blockquotes verbatim; the four declared severances
are the **only** four mid-token wraps in the body, the other two being URLs at
lines 479–480 and 523–524; the **6** literal `\n` escapes intact and unresolved under
both readers (this sentence’s own mention makes seven on disk, exactly as
pass 2’s note did); every YAML artifact parsing under **both** readers with **0** keys
missing on either side across 2424 leaf paths; and the cross-record RFC 9679
claims checked against `.cache/rfc-9679.txt` directly — §4.5 requires exactly
`kty` (1, int, 5) and `pub` (−1, bstr), §3 step 2 is RFC 8949 §4.2.1, §8
registers `ckt` as "COSE Key SHA-256 Thumbprint", and **`8778` and `8554` each
occur 0 times in it**.

*(One refinement to pass 2's wording, not a defect: its "only int/bool coercion
differing" between the readers is narrowly over-stated — 10 block-scalar values
in `messages.yaml` also differ by a trailing newline. No key or value is lost
either way.)*

## Source defects found

Nine, reported and never repaired. `normative.md`'s *Observations on the source*
has all of them with locators; `design-notes.md` has the three that cost a reader
something. The sharpest is that **§2.3's definition of `p` contradicts §2.3's own
layout** — `R-0070` defines `p` as the number of n-byte elements in an LM-OTS
signature and `R-0079` renders that signature with `p + 1` of them. Then **§3's
parseability claim is true of `[HASHSIG]` and not of this document**, because
RFC 8778 prints no code point for any of its nine named parameter sets. And
**both Appendix A signatures carry the same `C`**, which `R-0078` calls "an
n-byte random value".

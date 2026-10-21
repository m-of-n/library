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

**State: PASS 1 OF 3 COMPLETE. `distillation.standard: FX-1` with NO `profile`
declared, deliberately** — an unfinished extraction is neither `full` nor
`partial` and the gate says so (`docs/extraction.md`, *`profile: partial` is a
terminal state*). Extract ran 2026-10-20, one agent, alone, at effort `max`,
reading only `.cache/rfc-8778.txt`. **No verify pass and no cross-check pass has
run. No human has reviewed any of it** — every `reviewed_by` in this directory
is empty.

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
| state-machine | `state-machine.yaml` | **APPLICABLE, and it is the reason this record is useful.** Two machines — one LM-OTS leaf (4 states, 4 transitions) and the HSS key / trust anchor (5 states, 6 transitions) — with 2 error states, 2 `forbidden_transitions` and **5 explicitly `unspecified`** behaviours. The word-count measurement that would have supported declaring N/A is written out and rejected: `lifecycle`, `revoke`, `rotate`, `expire` and `exhaust` are all 0, and six requirements define a lifecycle anyway. |
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

## The 56 octets, and the one width nothing in this library states

| field | octets | provenance |
|---|---|---|
| `u32str(lms_algorithm_type)` | 4 | **measured** |
| `u32str(otstype)` | 4 | **measured** |
| `I` | 16 | **stated** — §3 `R-0092` |
| `T[1]` | 32 | **arithmetic** — §2.2 `R-0052` with `R-0039` |
| **total** | **56** | for all 20 parameter-set combinations RFC 8778 admits |

RFC 8778 never defines `u32str` — `R-0028` defers the notation to `[HASHSIG]`,
and `records/ietf/rfc-8554` is a **stub**. So the width was recovered from the
document's own arithmetic against its own printed bytes: a stand-alone-tree
signature is `4u + 32 + 32(p + h)` octets, both printed signatures measure 2512,
and `2512 − 4u − 32` is divisible by 32 for `u = 4` and for no other `u` in
{1, 2, 8}. `h = 10` and `p = 67` follow. **A normative structure dimensioned by a
non-normative appendix.**

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
- **A quote audit over every artifact in this directory**: 225 quotations
  checked against ten corpora, **0 not verbatim in any of them**. 194 are
  RFC 8778's; 25 are the sibling records' design notes or their cached sources
  (20 `rfc-9964`, 4 `rfc-9679`, 1 RFC 9679 itself); 5 are this library's own
  process documents (`docs/extraction.md`, the extract skill, `bin/validate`);
  1 is `topics/canonical-encoding.yaml`'s; and 8 are quotations of `mofn`
  documents this repository does not hold, which `design-notes.md` declares
  unverifiable here.
- **An id join audit** resolving every cited id to its requirement's text and
  reading the pairs: **127 of 135 ids cited outside `requirements.yaml`, 0
  dangling, 0 foreign-id collisions.** The 8 uncited are §1.1's three motivation
  sentences and five parameter-set-name rows that appear inside written ranges
  (`R-0041`…`R-0045`, `R-0073`…`R-0076`).
- **`bin/check-id-joins`, both modes, which did not exist when this pass
  started.** `--resolve`: **468 citations, 0 dangling.** `--surface`: **0
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
   the whole clause.

## What pass 2 should attack hardest

Named here so the verifier does not have to find them: the `u32str` width
derivation (the uniqueness argument, not just the arithmetic); the claim that 56
octets holds for all 20 admitted parameter sets; the four declared severances;
the 11 `constrained_by` wirings in `messages.yaml` that cite more than one id;
and the two `source: template` vectors, which are the only places in this
directory where a structure is asserted with no value behind it.

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

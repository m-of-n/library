---
record: rfc-8949
kind: index
title: "rfc-8949 — distilled artifacts"
extracted: "2026-09-30"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). Extracted from `.cache/rfc-8949.txt`, whose
sha-256 matches `content.sha256` in `record.yaml`
(`f1164a5b31a3…`) — so every locator below resolves against the exact bytes
this record commits to.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 165 verbatim statements + 36 verbatim blocks (Tables 1–7, §1.2 terminology and notation conventions in full, §3.1 major types, §4.2.1/§4.2.2/§4.2.3 in full, §5.3.1–§5.6.1, §6.1–§6.2, §7.1, §8 diagnostic-notation definition, §8.1, all five §9 registries, Appendix C Figures 1–2, Appendix F taxonomy + F.1). §1.2–§10 plus Appendices A, B, C, F. **Excludes** Appendix G (RFC 7049 changelog) and Appendices D/E (informative). |
| requirements | `requirements.yaml` | All 34 BCP 14 statements as `rfc-8949#R-0001`…`R-0034`, in source order. `extracted_keyword_count` 34 = `source_keyword_count` 34, so `reconciliation` is empty. §9.1–§9.4, §10 and Appendices A–G contain **zero** BCP 14 keywords — confirmed by regex sweep, so nothing was invented there. |
| schema | `schema/` | 2 verbatim + 2 derived. `well-formed.pseudocode.txt` (Appendix C, byte-identical) and `initial-byte-jump-table.txt` (Appendix B / Table 7, byte-identical); `cbor-data-model.derived.cddl` (44 rules, two roots — CDDL cannot express "any tag except these"); `cbor-head.derived.abnf` (head layer only, admits exactly the 229 well-formed initial bytes). **RFC 8949 contains no CDDL and no ABNF of its own** — §8 explicitly declines a formal definition. Neither derived file has been run through a real CDDL/ABNF parser; none is installed here. |
| messages | `messages.yaml` | 44 structures, 89 fields: the data-item head, 7 argument forms, major types 0–7, major type 7 in detail (simple values, three float widths, `break`), 4 indefinite-length forms, preferred/shortest-argument ranges, and the 16 tags of §3.4 with their exact head bytes, each head byte recomputed from its tag number in pass 3. `constrained_by` is **populated**: 75 of the 89 fields carry at least one `rfc-8949#R-NNNN`, 125 links in all. |
| examples | `examples/` | **232 vectors** — 131 well-formed, 101 not-well-formed. All 81 rows of Appendix A Table 6, plus §3.1–§3.4.6, §4.1, §4.2.1–§4.2.3, §5.2, §5.5, §8.1, Appendix E.5, and all 94 items of Appendix F.1 with the source's own error kind. **Not** transcribed: Appendix B jump table and Tables 1–5 (byte ranges, not items), and §8 byte-string literals with no CBOR encoding given — reasons in `examples/README.md`. Every not-well-formed vector carries a `violates` key naming the requirement or normative statement it breaks. |
| design-notes | `design-notes.md` | Adopt / adapt / reject against ARCH-0001, ARCH-0002 P1/P4/P5, ADR-0001 and **D-3** (option 5: CBOR data model, no IANA tags, COSE export only). Includes a 14-row table of what §4.2 leaves open with a negative fixture per row — direct input to the Oct 28 D5 package — and a per-tag table of what the no-tags rule costs. |

## Declared not applicable

| kind | reason |
|---|---|
| protocol | RFC 8949 defines a data format, not an exchange: no roles, no messages between parties, no error signalling. Its only procedural content is the single-item decode algorithm of Appendix C, captured verbatim in `schema/well-formed.pseudocode.txt` and as requirements. |
| state-machine | No lifecycle is defined. The one stateful process is the decode of a single data item, which has no persistent states, triggers or guards. |

## Known limits of this extraction

- **`constrained_by` in `messages.yaml` is populated as of pass 3** — 75 of the
  89 fields carry at least one requirement id, 125 links in all. 14 fields carry
  `[]` because no BCP 14 statement constrains them: five derived or free-content
  fields (`major-type-1`'s computed `value`, a byte string's `content`, the
  `elements` of both the definite- and the indefinite-length array, the generic
  `major-type-6-tag`'s `tag_content`), the `stop_code` of all four
  indefinite-length forms, an indefinite byte string's `chunks`, and the
  `tag_content` of tags 21, 22, 23 and 55799, whose content
  Table 5 gives as "(any)". 11 of the 34 requirements are referenced by no field:
  R-0006, R-0021, R-0022, R-0024, R-0025, R-0026, R-0027, R-0028, R-0032, R-0033
  and R-0034. That is the expected shape, not a hole — every one of them
  constrains a specification document, a protocol layer's behaviour, an
  application's security design or a media-type registration, none of which is a
  field of the encoding. Two requirements carry most of the weight: R-0012
  (arguments MUST be as short as possible) reaches every argument-valued field
  including each tag's exact head byte, and R-0023 (encoders MUST produce only
  valid items) reaches exactly the four validity classes §5.3.1 and §5.3.2
  enumerate — map entries, text-string content, and tag content. R-0003 and
  R-0004 are deliberately *not* spread across every field: they are blanket
  obligations over the whole format, so they are linked only to the three fields
  that encode nothing but a well-formedness verdict (reserved additional
  information, indefinite additional information, the `break` byte). Every
  not-well-formed vector cites R-0004 in its own `violates` key instead.
- **The two derived schema files are still unvalidated by a real CDDL or ABNF
  parser.** None is installed on this machine; first job for anyone with one.
  Pass 3 did the next best thing — transcribed the CDDL into a structural
  validator and ran it, with an Appendix C well-formedness checker, over all 232
  vectors: 131/131 well-formed validate against both roots, 101/101
  not-well-formed are refused, no defects. That tests what the rules *say*, not
  whether the files parse. `schema/README.md` and `examples/README.md` record
  the detail and the rules no vector reaches.
- **Lowercase obligations are included but not demoted.** §5, §6 and §4.2.2
  carry many "needs to"/"should" obligations with no uppercase BCP 14 keyword;
  §5 explicitly disclaims BCP 14 other than MAY and §6 calls itself
  non-normative. They are quoted verbatim in `normative.md` and labelled as the
  source labels them. A reviewer may want them demoted or split out.
- **Simple values 24–31 — resolved, not a source defect.** Pass 1 flagged Table 4's
  "(reserved)" as being in tension with §3.3, which forbids only two-byte `0xf8`
  sequences continuing with a byte below 0x20. Pass 2 showed there is no tension:
  major type 7's additional information 24–31 is already consumed (24 = one-byte
  extension, 25/26/27 = the three float widths, 28–30 = reserved, 31 = `break`),
  so values 24–31 have no immediate encoding, and §3.3 forbids the only other
  candidate. They are therefore unencodable, which is *why* Table 4 reserves
  them — and §9.1 confirms it by assigning registry entries only in 0–19 and
  32–255.

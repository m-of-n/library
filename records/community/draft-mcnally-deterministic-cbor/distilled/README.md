---
record: draft-mcnally-deterministic-cbor
kind: index
title: "draft-mcnally-deterministic-cbor — distilled artifacts"
extracted: "2026-10-16"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

**State: pass 1 of 3 complete.** The extract pass ran, at effort max, one
agent per artifact kind, each reading only `.cache/draft-mcnally-deterministic-cbor.txt`.
**The verify and cross-check passes have NOT run**, so this record carries no
`profile` — an unfinished extraction is neither `full` nor `partial`
(`docs/extraction.md`, "`profile: partial` is a terminal state, not a
failure"). It is readable; nothing may be built on it. library#39 owns
finishing it.

Source: *dCBOR: Deterministic CBOR*, `draft-mcnally-deterministic-cbor-18`,
10 August 2026, Standards Track, **expires 11 February 2027**.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 74 located statements and 14 verbatim fenced blocks across §1, §1.1, §2, §2.1–§2.7, §3, §5, §6, §7/§7.1/§7.2 and a restricted §8. Excludes §1's motivation, §4 Implementation Status (marked for removal before publication), §8.1–§8.6 rationale prose, references, acknowledgements and boilerplate. Mechanically verified: 74/74 bullets are contiguous substrings of the whitespace-normalised source, 14/14 fences are byte-exact source line runs |
| requirements | `requirements.yaml` | 38 entries, `R-0001`–`R-0038`, source order, no gaps: 18 `stated` carrying all 18 BCP 14 occurrences (16 MUST, 2 MUST NOT — the document uses no SHOULD, MAY, REQUIRED or OPTIONAL), 20 `inferred` carrying none and each declaring so. `source_keyword_count` and `extracted_keyword_count` both 18; `reconciliation` is written anyway because four of the count's details are invisible to a reader of the file alone |
| schema | `schema/` | 1 verbatim (`cddl-prelude-number.cddl`, the §3 prelude line) and 4 derived — a profile CDDL, a head-layer ABNF, and pseudocode for numeric reduction and for validation. The source ships almost no formal grammar of its own, so nearly every formal artifact here is ours and is named `.derived.` accordingly. See `schema/README.md` |
| messages | `messages.yaml` | 17 structures: the data item head and each major type's encoded layout as this profile narrows it, the numeric-reduction forms, and map key ordering. `constrained_by` is populated only where pass 1 was confident from the source's own section numbering — wiring it completely is a cross-check-pass job that has not run |
| examples | `examples/` | 72 vectors, `V-0001`–`V-0072`: 56 `valid`, 16 `invalid`, every invalid one carrying a `violates`. 62 hex strings are the source's own and were each confirmed to occur verbatim in it; 5 are our computation and say so in `notes`; 5 vectors state a case the source names without giving bytes. All 52 hex values in Tables 3 and 4 were decoded by hand against their stated values and agree. See `examples/README.md` for the source's own coverage holes |
| design-notes | `design-notes.md` | a 23-rule comparison of dCBOR against option 5 as drafted (same 3, stricter 3, looser 1, direct conflict 1, conditional conflict 1, **silent 14**), the R-O-03 question of whether option 5 can cite dCBOR rather than invent, and six places this document cuts against MD-3 with the favoured DEC-002 option named in each |

## Not applicable

Recorded in `record.yaml` under `distillation.not_applicable`, with reasons.
Both are findings, not omissions:

- **protocol** — dCBOR defines an encoding profile, not an exchange. Its only
  roles are codec roles ("dCBOR encoders:", "dCBOR decoders:"), §2 fixes its
  scope as processing rather than conversation, every failure is a local
  decoder verdict with no error code and no peer, and §8.6 expressly declines
  to specify even an API.
- **state-machine** — no lifecycle. dCBOR conformance is a per-data-item
  predicate defined recursively in §2. The only registration-like content is
  §6's one-time IANA action, which has no states or transitions.

## Source defects found

Reported in the artifacts, never repaired. The first is decision-relevant:

1. **A normative gap.** §7.2 Table 4 requires rejecting the 65-bit negative
   integers `3b8000000000000000` (−2^63−1) and `3bffffffffffffffff` (−2^64)
   as "65-bit negative integer value", but **no rule in the normative §2
   forbids them**. `DCBOR_INT` is introduced only inside §2.5, as the range
   within which *floating point* values are reduced to integers; these two
   encodings are the preferred serialization of their values, so §2.2 does not
   reach them either. Nine of eleven Table 4 rows trace to a §2 rule; these two
   do not. **The integer range cannot be inherited by citing §2.** Found
   independently by three agents.
2. §6 asks IANA to register "Table 1" into the CDDL Control Operators
   registry, but the operators are Table 2; Table 1 is the tag 201
   registration. The same section says Table 1 "has registered" while Table 2
   is still a request, and Table 1's Reference is the placeholder `[RFCXXXX]`.
3. §2.7 numbers its decoder rule "1." where §2.1–§2.6 all number it "2.", so
   §2.7 has two items numbered 1.
4. Two arithmetically wrong parentheticals in Table 3: `-127 (-2^8 - 1)`
   (−2^8−1 is −257; −127 is −(2^7−1)) and `-32768 (-2^16)` (−2^16 is −65536;
   −32768 is −2^15). Both hex encodings are correct; only the labels are wrong.
5. §2.7 does not say whether a conforming encoder rejects or rewrites non-NFC
   input, which is the whole of the identity risk it creates.
6. A tension the source itself acknowledges, and which a later pass must not
   "fix": §2 claims "The rules specified here do not "fork" CBOR" while the
   §2.5 aside concedes Numeric Reduction can turn a valid CBOR map into an
   invalid dCBOR map. The CBOR→dCBOR mapping is not total; the document puts
   the burden on applications rather than on the rules.

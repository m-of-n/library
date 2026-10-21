---
record: rfc-9921
kind: index
title: "rfc-9921 — distilled artifacts"
extracted: "2026-10-20"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). **Pass 1 (extract) only** — passes 2 (verify) and
3 (cross-check) have not run, no `profile` is declared in `record.yaml`, and
every `reviewed_by` is empty.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 29 verbatim regions covering the Abstract and §1–§7 and both appendices, in source order, each an exact run of source lines with its line range and its own sha256 (the region's lines joined by `\n`, no trailing newline). Includes §1.2's BCP 14 recital, both figures whole, §6's Table 1 whole and the whole reference list. **Measured coverage: every statement-bearing line of 17–23 and 79–1014 is inside a region except section headings, blank lines and the two 159-line hex blocks, which are declared with their digests and reproduced in `examples/` — 0 uncovered.** The two sentences a displayed byte block interrupts (§3.1.1, §3.1.2) are quoted as whole regions so the interruption is visible, and nothing is welded across a gap |
| requirements | `requirements.yaml` | 109 entries `R-0001`–`R-0109` in source order, no gaps, no duplicate ids: **11 stated and 98 inferred** — the 8 BCP 14 statements plus the three non-keyword spans whose force comes from an adjacent keyword in the same sentence (R-0042, R-0043, R-0058). `source_keyword_count` and `extracted_keyword_count` both **8** and agreeing, with a reconciliation written anyway. All 109 texts cut from the cache **by script** and verified as contiguous substrings of the whitespace-normalised source — 109/109, **0 relaxations needed** under terminal-punctuation swap, hyphenation heal, line-break heal or case fold. `source_lines` was read back off a per-character line map rather than typed. **Nine lower-case force words are entries with `verb: none`** and the carrier phrase named in `field` |
| schema | `schema/` | 1 verbatim file and 4 derived, plus a README. **RFC 9921 ships no grammar: `CDDL`, `ABNF`, `ASN.1`, `JSON Schema`, `schema` and `grammar` each occur ZERO times**, as do `canonical` and `deterministic`. `source-renderings.txt` is the only unmarked file and carries the twelve places the document renders a structure by printing it, as 12 regions with line ranges and digests. Derived: `cose-headers.derived.cddl` (the two labels, the opaque value, both bucket constraints, and all three imprint preimages written out octet by octet); `header-parameters.derived.yaml` (§6's rows as data, **reassembled** because the table is column-wrapped and no cell is a contiguous span); `timestamp-token.derived.outline.txt` (what the 5453 octets contain, produced by decoding, with four internal consistency checks); `cose-headers.derived.schema.json` with `$id: urn:library:rfc-9921:cose-headers.derived` |
| messages | `messages.yaml` | 13 structures with octet-level layouts: both header parameters, the three COSE instantiations the document prints, `MessageImprint`, `TimeStampReq`, `TimeStampResp`, `TimeStampToken`, `TSTInfo`, and **all three MessageImprint preimages as byte sequences**. Every layout produced by decoding, never by reading the prose, and every octet count re-derived by the generator at write time. `constrained_by` is wired and **no id was typed** — each was resolved by script from a fragment of the requirement's own text. **29 empty `constrained_by` lists across 48 fields**, every one belonging to RFC 9052, RFC 5652 or RFC 3161 |
| protocol | `protocol.yaml`, `protocol.md` | **APPLICABLE.** 4 roles, 4 flows (CTT assembly, TTC assembly, CTT verification, TTC verification), 20 steps, a Mermaid sequence diagram per flow. Every `message:` names a structure in `messages.yaml`. The two verification flows are marked step by step as `stated` or `reconstructed`, because **§5.1 asserts that each mode has its own verification algorithm and the document writes neither down**. `error_paths` separates the 3 the document states from the 6 it leaves `undefined_by_source` — including the failure branch of its own only machine-facing MUST |
| state-machine | `state-machine.yaml` | **APPLICABLE.** 5 machines, 28 states, 23 transitions, 10 error states. The two assembly orders (the document's entire subject), the two verification machines, and **the long-term-validity lifecycle the document exists for and never names** — `state`, `states`, `lifecycle`, `expire`, `expiry`, `expiration`, `revoke` and `rotate` each occur ZERO times. The finding it makes legible: in CTT verification the transition that *selects the machine* is guarded on an unauthenticated byte, and no state anywhere records that a timestamp was expected |
| examples | `examples/` | 15 vectors plus two 5453-octet `.hex` fixtures. **Four digests printed, three reproduce byte for byte and one does not** — the 207-candidate preimage sweep behind that claim is in `V-0011`. Two CMS internal consistency checks per token, both passing, plus every length and offset. Two derived censuses: where a CBOR head sits inside a third party's digest, and what the fixture's TSA actually is — a public demo TSA whose signing certificate **expired 2026-03-11**, one month after publication |
| design-notes | `design-notes.md` | The DEC-002 cut measured both ways, `R-M-12` from the value side, `R-O-05`'s one adopt and one hazard, all six `canonical-encoding` conditions scored, **MD-3 mapped header by header and then five cuts against it, each naming the DEC-002 option it affects**, the inverted modes verified leg by leg, 11 source defects, 7 open questions, and an adopt/adapt/reject table. 25 source quotations, every one cut from the cache by script and verified contiguous — **0 relaxations**. Every quotation of a `mofn` document is marked **unverifiable from this repository** (10 of them), following `records/ietf/rfc-9741` |

**`not_applicable`: none.** All eight artifact kinds are present, and the two
that are usually declined here — protocol and state machine — were each
measured before being kept; see `record.yaml` for the grounds.

## The three numbers to take away

- **5453 octets** of ASN.1 DER in one protected header parameter against a
  **20-octet** payload: **272.65 : 1**, and **98.09 %** of the whole tagged
  `COSE_Sign1`. 75.26 % of the token is a two-certificate X.509 chain.
- **`0x58 0x40`** — the two CBOR head octets that §3.1.1 puts inside the TSA's
  digest preimage, verified by reproducing the printed imprint exactly.
- **8** BCP 14 keywords (6 MUST, 2 SHOULD), against **nine** lower-case force
  words — two of which are the document's answers to its own stated attacks.

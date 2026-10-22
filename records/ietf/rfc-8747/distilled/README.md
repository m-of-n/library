---
record: rfc-8747
kind: index
title: "rfc-8747 — distilled artifacts"
extracted: "2026-10-21"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what it
does not.

**Pass 1 (extract) only.** Passes 2 and 3 have not run, so
`distillation.profile` is deliberately **unset** and every `reviewed_by` is
empty. Read every count below as pass 1's measurement, with the method stated.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | **28** byte-exact fenced regions covering **389** of the source's 683 lines, in document order, §1-§7.2.2 plus the masthead and Abstract; includes Table 1 and all four IANA blocks. Front matter, ToC, both reference lists, Acknowledgements and Authors' Addresses dropped and stated as dropped |
| requirements | `requirements.yaml` | **118** entries `R-0001`-`R-0118`, source order, no gaps: 111 `stated`, 7 `inferred`; 35 `testable: yes`, 12 `partial`, 71 `no`. Keyword counts **8 = 8**, bijection by source line |
| schema | `schema/` | **1** verbatim and **3** derived. The source ships **no** grammar, so every formal artifact is ours; the CDDL is shown to **bind**, 10 of 10 instances |
| messages | `messages.yaml` | **5** structures, **22** fields, **38** of the 118 requirements wired, every `constrained_by` non-empty except five RFC 8392 claims that carry an `unwired_reason` |
| protocol | `protocol.yaml`, `protocol.md` | **3** roles, **6** steps, **0** error paths. One step partly specified; five unspecified, two by explicit refusal. Mermaid diagram with every arrow dashed |
| state-machine | `state-machine.yaml` | **not applicable**, written out: thirteen lifecycle words at zero over 683 lines, four near misses each checked, and a ground none of the five sibling N/A records shares |
| examples | `examples/` | **6** vectors over the source's 4 printed examples and 1 printed scalar; 5 byte-exact fences. The one cryptographic computation **reproduces** |
| design-notes | `design-notes.md` | all four `bears_on` identifiers, the `MD-3` structure mapping and export mapping, **6** named cuts against `MD-3` each naming the `DEC-002` option it affects, plus a convergence note; the six canonical-encoding conditions as a measured negative; **6** source defects; **13** open questions; and a pass-2/3 attention map |

## What this extraction measured rather than asserted

Every number here was re-derived at write time by the generator that wrote the
file, and asserted against the printed value, so a stale count cannot survive
in the artifact that states it. Counts stated in a *different* file from the
artifact they describe are the likeliest fossils (`hazards.md` §6), so this
table's figures are read **off the files on disk** when this index is built.

| | |
|---|---|
| source | `.cache/rfc-8747.txt`, **683** newline-delimited lines, **0 form feeds** |
| digest | `9b695379f119f9675828d054f1b0e76014c06c9a59dccef8bb417e0420272dda` — matches `content.sha256` |
| maturity | **Standards Track**, quoted from source line 7 in `normative.md`, not inferred |
| BCP 14 keywords | **8**: 4 MUST, 2 MAY, 1 SHOULD, 1 MUST NOT — `bin/bcp14-count --by-keyword` |
| where they are | L172, L180 (§3.1); L227, L228, L231, L235 (§3.2); L357, L391 (§4). **None** in §1, §2, §3, §3.3, §3.4, §3.5, §5, §6, §7 |
| non-uppercase force words in the body | **25** on 25 lines — `may` 9, `should` 7, `must` 4, `required` 2, `Required` 1, `recommended` 1, `optional` 1 |
| line-end hyphens | **8**, three of them inside quoted requirement texts. **None healed** |
| §3.3 ciphertext | **authenticates** and reproduces all 48 octets — from entry order `3, 1, -1`, not from the printed `1, 3, -1` |
| §3.2 public key | **on P-256** |
| `cnf` sizes | **77** octets (`COSE_Key`), **73** (`Encrypted_COSE_Key`, untagged), **19** (`kid`) |
| tag cost | **1 octet** — 71 untagged against 72 tagged |

## Mechanical results, with the method

| check | result |
|---|---|
| requirement texts contiguous in the whitespace-normalised source | **118 of 118**, zero relaxations |
| `bin/check-locators` | **118 of 118** contained, 0 misfiled, 0 unresolvable |
| fenced regions byte- **and** digest-exact against their declared line range | **33 of 33** |
| both YAML readers agree on every artifact | **0** real value divergences; the only differences are `int` vs `str` on bare numbers |
| `bin/check-id-joins --surface` | **1** duplicate-text group, `R-0038`/`R-0052` — both `example-intro` sentences, byte-identical |
| `bin/check-id-joins --quote-join` | **31** pairs examined, **31** carried, 0 to read — re-measured after the check was fixed (below) |
| this pass's own exhaustive join audit | **38** pairs examined, **38** carried by their cited id |
| citation closure over `distilled/` | **118** distinct ids cited, **0** dangling |
| `bin/validate` | **0 errors**, nothing flagged on this record |

**Every cited id was emitted from the id table by a selector that raises on
zero or multiple matches.** None was typed or pattern-matched, which is the
only defence against the one defect class nothing automated catches — an id
that resolves to a real but different statement (`hazards.md` §4).

## Known gaps, named rather than left for pass 2 to find

1. **`--quote-join`'s coverage was this pass's finding, and it has since been
   fixed.** This pass reported that the check examined **25** pairs where its
   own audit finds 38, and diagnosed the window: `text[pos-1400:pos]` paired
   quote marks left to right from wherever the cut fell, so a cut landing
   inside a quotation offset the pairing and the span beside the citation went
   unrecognised. Reported rather than worked around, because `bin/` was not
   this pass's to change.

   The fix found that the window was real but **not** the binding constraint
   here. Two further causes dominated, and both were invisible until the
   rejections were tallied rather than reasoned about:

   - `_OPENS` did not list `'` as an opener-shaped predecessor, so **this
     record's commonest attributed shape was unreadable** — a `quoted_evidence`
     entry is a YAML single-quoted scalar opening on the quotation itself,
     `- '"…" (rfc-8747#R-0047)'`, where the `"` is preceded by `'` and nothing
     else;
   - a quotation carrying **more than one** interior mark pair was rejected,
     which §7.1's sentence does twice in one breath.

   Now **31 examined, 31 carried, 0 to read**. The remaining seven of this
   pass's 38 are excluded by design rather than by accident, and each class can
   be named: a `- id: 'rfc-8747#R-0017'` line **defines** an entry and does not
   cite one (the nearby mark is the previous entry's `text:`); `` `Specification
   Required` `` is a backticked code span, not a quotation; and §7.2.2's IANA
   registration block is a template of `* Change Controller:` lines, which is
   structure rather than prose. The 38 remain correct **by construction** —
   each quotation is the cited requirement's own `text`, emitted from the id
   table — but 31 is now a coverage figure determined by evidence, and the
   difference is accounted for instead of unexplained.
2. **The cut operator is inert on Confirmation Keys 1 and 2.** `schema/README.md`
   says so in its own words: RFC 8747 defines no `COSE_Key` or `COSE_Encrypt0`
   grammar, so those rules are sockets typed `any` and the whole constraint on
   those two labels is carried by `other-label`'s exclusion. The cut does real
   work on Confirmation Key 3 alone.
3. **`summary.md` heals a hyphen.** It quotes rfc-8747#R-0028 as
   `proof-of-possession` where the source breaks `proof-of-` / `possession`
   across lines 180-181. All seven `bears_on` quotations in `record.yaml`
   resolve **exact**; this one resolves only under a source-side hyphen heal.
   Not edited by this pass — see `design-notes.md` §7.
4. **`record.yaml`'s `bears_on` elides a qualifier.** Its §6 quotation runs
   `… within the lifetime of the CWTs... Failure to do so …`, eliding `, unless
   intentionally desired.` The ellipsis is visible, so the elision is declared
   rather than hidden — but what it removes is the clause that makes §6 a
   *qualified* uniqueness rule, and `design-notes.md` §4.2 treats that clause as
   a finding in its own right. rfc-8747#R-0091 carries
   the full sentence verbatim.
5. **Nothing here has been read by a human.** Every `reviewed_by` is empty and
   `profile` is unset.

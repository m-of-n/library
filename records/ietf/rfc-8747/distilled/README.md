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

`distillation.passes` is the pass record and this file deliberately does not
restate it, because such a restatement goes stale the moment the next pass
lands — as the line that stood here did. Every `reviewed_by` is empty, which is
pass 4 and not a precondition for `profile: full`. Each count below carries the
method that produced it.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | **28** byte-exact fenced regions covering **389** of the source's 683 lines, in document order, §1-§7.2.2 plus the masthead and Abstract; includes Table 1 and all four IANA blocks. Front matter, ToC, both reference lists, Acknowledgements and Authors' Addresses dropped and stated as dropped |
| requirements | `requirements.yaml` | **118** entries `R-0001`-`R-0118`, source order, no gaps: 110 `stated`, 8 `inferred` under the criterion that file now **declares**; 35 `testable: yes`, 12 `partial`, 71 `no`. Keyword counts **8 = 8**, bijection by source line. No entry's text runs into the next entry's opening — checked, 0 of 118 |
| schema | `schema/` | **1** verbatim and **3** derived. The source ships **no** grammar, so every formal artifact is ours; the CDDL is shown to **bind**, **36 of 36** instances (26 accept, 10 reject) with a vacuity probe in which a wildcard rendering wrongly accepts **10 of the 10** rejects. *This row said 10 of 10 — pass 1's figure, which pass 2's 30-case re-run and the cross-check pass's 36 both superseded without reaching here* |
| messages | `messages.yaml` | **5** structures, **20** fields, **38** of the 118 requirements wired, every `constrained_by` non-empty except **three** of the five RFC 8392 claims in the fragment — `aud`, `exp`, `iat` carry an `unwired_reason`; `iss` and `sub` are wired to §3 sentences |
| protocol | `protocol.yaml`, `protocol.md` | **3** roles, **6** steps, **0** error paths. One step partly specified; five unspecified, two by explicit refusal. Mermaid diagram with every arrow dashed |
| state-machine | `state-machine.yaml` | **not applicable**, written out: thirteen lifecycle words at zero over 683 lines, four near misses each checked, and §7's registration procedure confronted rather than dismissed. **16** of the lane's **25** FX-1 records declare this artifact N/A; **five** of those were read for their grounds and those five fall into **four** kinds, none of them this record's. *The four kinds are a property of the five that were read, not of all 15 others — `state-machine.yaml` corrected exactly that overstatement in its own field and this row kept it* |
| examples | `examples/` | **6** vectors over the source's 4 printed examples and 1 printed scalar; 5 byte-exact fences. The one cryptographic computation **reproduces** |
| design-notes | `design-notes.md` | all four `bears_on` identifiers, the `MD-3` structure mapping and export mapping, **6** named cuts against `MD-3` each naming the `DEC-002` option it affects, plus a convergence note; the six canonical-encoding conditions as a measured negative; **6** source defects; **6** open questions; and a pass-2/3 attention map |

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
| where they are | L172, L180 (§3.1); L227, L228, L231, L235 (§3.2); L357, L391 (§4). **None** in §1, §3, §3.3, §3.4, §3.5, §5, §6, §7 — nor in §2 **beyond its BCP 14 recital**, which holds 11 more uppercase keywords at L101–103 and is excluded as boilerplate by `bin/bcp14-count` |
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
| fenced regions byte- **and** digest-exact against their declared line range | **33 of 33** — 28 in `normative.md`, 5 in `examples/README.md`. `schema/source-renderings.txt` carries **4** more that are dash-delimited rather than fenced and are digested the same way, so **37 of 37** digested regions in all |
| whole-YAML-scalar verbatim spans (the blind spot a delimited audit cannot see) | **104**, every one exact and **none healed** — 83 are `requirements.yaml` `text:` fields, 21 are elsewhere (9 `protocol.yaml`, 8 `schema/confirmation-methods.derived.yaml`, 3 `examples/vectors.yaml`, 1 `record.yaml`'s `title`). Threshold ≥25 characters after whitespace normalisation |
| quotation spans resolving **only under relaxation** (hyphen heal, terminal-punctuation swap, case fold) | **0** in the ≥25-character band. In the 6–24 character band the audit reports exactly **one**, and it is not a quotation: the JSON Schema keyword `object` in `schema/cnf-claim.derived.schema.json`, which resolves case-folded against the source's prose. That band is the one the `"expected"` defect was found in, and it is now clean |
| both YAML readers compared, **values** not counts, over **1966** leaf paths of `distilled/` (the union of the two readers' key sets on the files both can parse; **1975** under `bin/_yaml.py` alone, which also parses the JSON Schema). *Scoped to `distilled/` deliberately: a figure that includes `record.yaml` cannot be stated anywhere without an edit to `record.yaml` falsifying it, which is `hazards.md` §6's advice to state a count outside the text it measures — it moved twice during the cross-check pass* | **1** real divergence — `content.local`, `'false'` under `bin/_yaml.py` against `False` under `bin/_record_yaml.py` — plus **46** `int`-vs-`str` differences on bare numbers, and **one file `_record_yaml.py` cannot parse at all**, `schema/cnf-claim.derived.schema.json`. *This row said "agree on every artifact, 0 real value divergences". Pass 2 withdrew that claim in `record.yaml` and it survived here, which is the propagation failure a cross-check pass exists to find* |
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
2. **The cut operator is inert on Confirmation Keys 1 and 2, and there is now an
   instance that proves it.** RFC 8747 defines no `COSE_Key` or `COSE_Encrypt0`
   grammar, so those rules are sockets typed `any` and the whole constraint on
   those two labels is carried by `other-label`'s exclusion; the cut does real
   work on Confirmation Key 3 alone. The cross-check pass added `{1: 42}` and
   `{2: "nonsense"}` to `schema/README.md`'s table — both **accept** — because a
   concession with no instance behind it is not testable, which is
   `hazards.md` §7 read the other way round. It also recorded that the nearby
   `{2: COSE_Encrypt0, 1: "nonsense"}` rejects for **co-presence**, not for the
   wrong type, so that row cannot be read as a type constraint on key 1.
3. **CLOSED by the cross-check pass: `summary.md`'s two quotation defects.**
   It had quoted rfc-8747#R-0028 as `proof-of-possession` where the source
   breaks `proof-of-` / `possession` across lines 180-181, so the quotation
   resolved only under a source-side hyphen heal; and it wrote collisions were
   to be `"expected"`, where §3.4 reads *implementers should expect collisions*
   — an inflection inside quote marks, and a word that occurs **0** times in
   the document. Both were reported twice without being decided. Now fixed:
   the hyphenation is written the way the source reads it, with the break
   named, which is the convention `requirements.yaml` and `normative.md`
   already keep; and the collision clause quotes the document's own words.
   Re-measured: the ≥25-character whole-span audit and the 6–24-character pass
   both now resolve every `summary.md` span, and the only remaining
   occurrences of `expected` in the record are the three places that name it as
   a word the document does not use.

   The claim that stood here, that **all seven** `bears_on` quotations in
   `record.yaml` resolve **exact**, was withdrawn by pass 2 as not reproducible,
   and the measurement has since moved again. Measured by taking every span ≥25
   characters from the joined comment block: there are **nine** quotations, of
   which **four** are m-of-n and unverifiable from this repository; of the
   remaining five, **all five now resolve EXACT** — because the cross-check pass
   removed both ellipses (known gap 4 below). The blanket wording was wrong when
   it was written and the narrower statement is now true, which is the order
   `hazards.md` §2 asks for: state the rule you actually keep.
4. **CLOSED by the cross-check pass: the two `bears_on` elisions.** The §6
   quotation ran `… within the lifetime of the CWTs... Failure to do so …`,
   eliding `, unless intentionally desired.` — declared, but it removed the
   clause that makes §6 a *qualified* uniqueness rule and that
   `design-notes.md` §4.2 treats as a finding in its own right. Attacking that
   elision turned up a **second and worse** one the earlier passes had not
   listed: the `ARCH-0002 P1` §3.4 quotation elided `When sending a COSE
   encrypted message with a shared key,` — the **antecedent** of the sentence
   this record is held for, so the elision dropped the condition under which
   the document says a Key ID may differ. Both restored. Each is now a
   contiguous substring of the source (lines 414-419 and 321-325) and resolves
   EXACT, so `record.yaml` carries no elision at all and the finding survives
   the restoration, because §3.4's first sentence is unconditional.
5. **Nothing here has been read by a human.** Every `reviewed_by` is empty.
   `profile` is `full` as of the cross-check pass; `reviewed_by` is pass 4 and
   is not a precondition for it.

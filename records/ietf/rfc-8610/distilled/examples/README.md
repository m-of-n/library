---
record: rfc-8610
kind: examples
title: "rfc-8610 — examples and test vectors"
extracted: "2026-10-18"
reviewed_by: ""
---

# Examples and test vectors

`vectors.yaml` — **98 vectors, `rfc-8610#V-0001` … `rfc-8610#V-0098`, in source
order with no gaps.** 92 `valid`, 5 `invalid`, 1 `indeterminate`. 20 carry a
concrete instance the source prints.

RFC 8610 is a document about a notation, so nearly every example in it is CDDL
text rather than bytes. The vectors are therefore schema fixtures first: each
one holds the CDDL (or ABNF, or EDN) **as the source prints it** and, where the
document gives one, the matching or non-matching data item.

## How a vector is built

- **`cddl`** — lifted from the cached source **by line range, by script, never
  retyped.** The only transformation is removal of the common left margin,
  which a YAML block scalar performs in any case; relative indentation inside a
  block, the RFC's own comments, and the RFC's own spelling (including the
  uppercase `F` in `h'63666F6FF6'`) are the source's. Six vectors join two
  non-adjacent source ranges — a page frame or an omitted line falls between
  them — and each says so in its `notes`.
- **`instance`** — the data item the source prints, again by line range. Where
  the source gives the instance inside running prose rather than as a block
  (`h''`, `10`, `1e1`), the vector carries it as a one-line scalar and the
  `notes` say where it came from.
- **`matches`** — what the schema admits, in one line.
- **`expect`** — `valid`, `invalid`, or `indeterminate` (one vector; see below).
- **`violates`** — on `invalid` vectors only: the rule broken, by section.
- **`notes`** — the source's own sentences in quotation marks; anything marked
  **OURS**, **CHECKED BY US** or **DECODED BY US** is this library's reading or
  arithmetic, not the document's.

**Double quotes around a CDDL fragment are often the source's own bytes**, not
part of the CDDL: §1.2 states the convention — "CDDL text in the running text
is in "typewriter", which is rendered in plain text as the CDDL text in double
quotes". Vectors lifted from running prose (`"bytes .cbor type1"`,
`"type1 .and type2"`, `"[Cc][Aa][Ss][Ee]"`) keep those quotes and say so.

## Why one vector is neither valid nor invalid

`rfc-8610#V-0037` (§3.5.3, `do-not-do-this` against `{3: 5, 4: 6}`) carries
`expect: indeterminate`. This is the document's one genuine ambiguity and it
**declines to resolve it**: "the first group entry might pick off the "3: 5",
leaving "4: 6" for matching the second one. Or it might pick off "4: 6",
leaving nothing for the second entry. […] At the time of writing, CDDL tools
cannot detect such cases automatically, and for the present version of the CDDL
specification, the specification writer is simply urged to not write
pathologically non-deterministic specifications." Forcing it into `valid` or
`invalid` would assert something RFC 8610 does not.

## The negative vectors

Five, and all five are the source's own, not constructions of ours:

| id | locator | what is wrong |
|---|---|---|
| `V-0013` | §2.2.2.1 | `BAD-range1 = 0..10.0` — the source's own comment is `; NOT DEFINED`. Parses; is not a type. |
| `V-0014` | §2.2.2.1 | `BAD-range2 = 0.0..10` — the mirror image. |
| `V-0041` | §3.5.4 | `{ "optional-key": "nonsense" }` against the map **with** the cut. The same instance against the same map **without** the cut (`V-0039`) matches. The pair is the whole argument for cuts; match vectors on id, never on the instance. |
| `V-0075` | Appendix A | `A = "a" / "a" "b"` — under PEG the second alternative is unreachable. |
| `V-0076` | Appendix A | `*a a` — occurrence indicators are greedy, so it can never match. |

Negative facts the document states **in prose without an example** are not
invented into vectors here. The two worth knowing: the prelude defines no
`string` (Appendix D), and a specification may not use a group as its root
(§2.2.4). Both are recorded in `../schema/grammar-gaps.derived.txt` (G-40,
G-04) rather than fabricated as CDDL.

## Coverage by section

Every CDDL, ABNF, EDN or instance example the document prints is here.

| source | vectors |
|---|---|
| §2.1 Figures 1–6 (groups and composition) | 6 |
| §2.2.2 choices and extension | 4 |
| §2.2.2.1 ranges, including both NOT DEFINED cases | 6 |
| §2.2.2.2 group→choice with `&` | 1 |
| §2.2.3 representation types | 1 |
| §3.1 comments and barewords | 1 |
| §3.2 occurrence, and the map collapse | 2 |
| §3.4 arrays, with all four printed instances | 5 |
| §3.5.1 structs, Figure 7 and its generated instance | 7 |
| §3.5.2 tables | 2 |
| §3.5.3 non-deterministic order | 2 |
| §3.5.4 cuts — all four spellings plus both instance outcomes | 6 |
| §3.6 tags | 3 |
| §3.7 unwrapping, with and without `~` | 2 |
| §3.8.1 Figures 8–9 (`.size`) | 2 |
| §3.8.2 Figure 10 (`.bits`), the ten generated instances, the three all-clear instances | 5 |
| §3.8.3 Figure 11 (`.regexp`) and its matching string | 2 |
| §3.8.3.1 the case-insensitivity workaround | 1 |
| §3.8.4 `.cbor`, `.cborseq` | 2 |
| §3.8.5 `.and`, `.within`, and the socket example | 3 |
| §3.8.6 `.ge`, `.default` | 2 |
| §3.9 socket/plug, including Figure 12 | 2 |
| §3.10 generics | 1 |
| §3.11 operator precedence, all five groups | 5 |
| Appendices A, E, G and H | 25 |
| **total** | **98** |

Three figures are **not** duplicated as vectors because they are schemas, not
examples, and are held verbatim next door: Figure 13 (the ABNF) as
`../schema/cddl.abnf`, Figure 14 (the prelude) as `../schema/prelude.cddl`,
Figure 15 (the JSON subset) as `../schema/prelude-json-subset.cddl`. Figure 16
(I-JSON types) is held **both** ways — as `../schema/ijson-types.cddl` and as
`rfc-8610#V-0082` — because the source presents it as a copyable snippet rather
than as part of any prelude.

## Things these vectors expose

- **The same instance bytes appear under two verdicts.** `V-0039` (valid) and
  `V-0041` (invalid) are `{ "optional-key": "nonsense" }` against maps that
  differ by one `^`. Any consumer must key on `id`.
- **Appendix H's generated instance does not satisfy its own schema** on a
  strict reading (`V-0098`): the schema says `rating: float16` and the instance
  carries `0.34133473256800795`, which is not representable in binary16. Under
  Appendix E that is exactly what a float precision means — "only to restrict
  the set of permissible values to those expressible with
  binary16/binary32/binary64". The document does not comment on it. Recorded,
  not repaired.
- **`0o` octal literals are EDN-only** (`V-0092`). Appendix G.5 admits them;
  CDDL's own `uint` production has `0x` and `0b` and no octal.
- **EDN admits byte-string prefixes CDDL does not** (`V-0085`): Appendix G.2
  names `h`, `b32`, `h32` and `b64`, where `bsqual = "h" / "b64"`.
- **The ten `.bits` instances were re-checked here**, not taken on trust: all
  ten set only bits in {0, 4…15} under the section's own rule
  `(str[n >> 3] & (1 << (n & 7))) != 0`, and none sets bit 1, 2 or 3.

## State

**Passes 1 and 2 of 3 complete.** Every `cddl` and `instance` block scalar was
verified by script against the cached source — **109 block scalars: 103 a single
unbroken source run, 1 spanning a page frame (`V-0096`), and 5 joining two
non-adjacent ranges across an omitted line (`V-0012`, `V-0023`…`V-0026`), each
declaring the omitted lines in its own `notes`.** So 104 are dedented contiguous
slices once the page decoration is removed, and the remaining 5 are the declared
compositions. A further 9 `instance` values are one-line prose-quoted scalars
rather than block scalars (`h''`, `10`, `1e1`, `{3: 5, 4: 6}`, …); each was
confirmed present in the source. Pass 2 re-derived all of this independently,
added the `instance` that `V-0037`'s `notes` already cited but the vector did
not carry (`{3: 5, 4: 6}`, source line 1275), and corrected pass 1's
arithmetic, which reported the single-range count (103) as the total and gave
the single-range figure as 97.

The file parses identically under both of the repository's YAML readers
(`bin/_record_yaml.py` and `bin/_yaml.py`) and under PyYAML `safe_load`: 98
vectors, identical ids, identical block text, zero differences. **No vector has
been run through a CDDL tool** — none is installed in this environment — so
every `expect` here rests on the source's own statement or on arithmetic that
the `notes` attribute to us.

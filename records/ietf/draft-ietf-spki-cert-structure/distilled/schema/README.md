---
record: draft-ietf-spki-cert-structure
kind: schema
title: "draft-ietf-spki-cert-structure — schemas"
extracted: "2026-11-09"
reviewed_by: ""
---

# Schema

The draft's schema language is BNF, written "in a familiar extension of BNF" with
`|`, `*`, `?`, `+` and quoted strings (section 3). It ships no CDDL, ASN.1 or JSON
Schema. So the schema artifacts are the draft's BNF **verbatim**, plus a library-made
executable reader for it.

## Verbatim (the draft's bytes)

A file with no `.derived.` in its name asserts verbatim bytes. Each holds blocks
`# @frag <section> L<first>-<last>` of source lines, byte for byte. Lines that start
`# ` are the library's header and block annotations. The only thing left out of a
block is page furniture (footer, running header, form feed, the blank runs round them),
recorded in a `# elided` line per block. `verbatim_files.derived.py --check` rebuilds each
file from the source and fails on any drift.

| file | what | lines |
|---|---|---|
| `bnf-s9-2-alphabetical.verbatim.bnf` | section 9.2, the whole alphabetical list (88 productions) | L2257-2371 |
| `bnf-fragments-s3-s8.verbatim.bnf` | every BNF production printed in sections 3, 4, 5, 6, 7 and 8.1 (66 productions, 64 names) | 38 blocks, see file |
| `bnf-s9-intro-s9-1.verbatim.txt` | section 9 introduction and 9.1 Top Level Objects (prose, no productions) | L2230-2232, L2238-2251 |

## Derived (written by this library; not the draft's)

| file | what |
|---|---|
| `spki_sexp.derived.py` | reader and writer for the canonical, advanced and `{base64}` transport forms of section 3 (stdlib). Byte strings with display types, integers (two's complement), dates |
| `spki_bnf.derived.py` | reads the verbatim BNF files and checks a parsed S-expression against any production. A memoised recogniser that also counts derivations (ambiguity). `semantic_issues` checks what the prose says and the BNF cannot: K < N, N listed, date shape, digest length |
| `test_spki.derived.py` | MUST-accept and MUST-reject cases for both, each citing the sentence that makes it a case, and `--mutate`, which shows the reject cases bind |
| `reject-reasons.derived.json` | the error text each reject case must produce (data for `test_spki.derived.py`) |
| `join_requirements.derived.py` | wires `constrained_by` in `../messages.yaml`: the production text rule, then a curated table read against every requirement; `--wire` prints the pairs, `--apply` rewrites the lists. Reports requirements, messages and fields examined beside what it wired, and fails if the list of requirements cited by nothing changes |
| `test_basis.derived.py` | joins every case table entry of `test_spki.derived.py` to the requirement ids that state its rule (`--list` prints each pair). Examined 342 table entries, all joined, 142 distinct ids, 0 dangling |
| `check_messages.derived.py` | checks `../messages.yaml` against the BNF: every minimal instance parses, round-trips and is accepted by its own production; every object's fields agree with 9.2 |
| `bnf_compare.derived.py` | compares every fragment production with its section 9.2 twin by script; writes `bnf-comparison.derived.txt` |
| `bnf-comparison.derived.txt` | that script's whole output |
| `verbatim_files.derived.py` | builds and checks the three verbatim files from the source |

```sh
python3 -I schema/test_spki.derived.py             # cases; exit 1 on a failure
python3 -I schema/test_spki.derived.py --mutate    # cases against mutants (slow: minutes)
python3 -I schema/spki_bnf.derived.py --rule cert FILE...
python3 -I schema/bnf_compare.derived.py --write
python3 -I schema/verbatim_files.derived.py --check
```

## Tests

Last run: `spki_sexp` 187 cases, `spki_bnf` 187 cases, 0 failed. By kind: 93 MUST-accept,
121 MUST-reject, 9 odd-accept (the BNF as printed accepts something the prose would
not; recorded so a change is noticed), 3 ambiguity probes (derivation counts).

Every case table entry is joined to the requirements that state its rule by
`test_basis.derived.py` (`python3 -I schema/test_basis.derived.py`; 342 entries examined: the case tables, the integer and date tables and eight inline checks listed in the script's `INLINE`;
342 joined, 142 distinct ids, 0 dangling). Roundtrip and API-edge checks inside `run_sexp` restate no rule and are not joined.

### Mutation

`--mutate` applies one mutation at a time and requires a case to fail (a mutant that
loops forever is killed after 3 s). Last run, after the second set of cases:

| target | mutants | killed | survived |
|---|---|---|---|
| `spki_sexp.derived.py` (AST: comparisons flipped, and/or swapped, raises removed, integer constants +1, `if` conditions negated) | 260 | 236 | 24 |
| section 9.2 grammar text (quantifier dropped, alternative dropped, literal changed) in rules reachable from a top-level object | 138 | 125 | 13 |

The first run of the first case set killed 189 of 260 and 89 of 138. Two changes closed most of
the gap. A reject case now binds to *why* an input is rejected: the error text must equal the one
in `reject-reasons.derived.json` (68 reasons, reviewed against each case's cited sentence;
`--write-reasons` rewrites it), because a mutant that removed a `raise` still rejected the
input through a later check. And rule-level cases test each production directly (`<tag-range>`,
`<tag-prefix>`, `<tag-set>`, `<tag-string>`, the enumerations, `<hash-op>`, `<online-test>`, and a
`<sequence>` with every kind of entry), because at the `<cert>` level a malformed star form still
parses as `<simple-tag>` (messages.yaml SD-13).

The 13 grammar survivors are equivalent mutants: `<hash-alg-name>` and `<pub-sig-alg-id>` end in
`<uri>`, which is any byte string, so the named algorithms constrain nothing and changing or
dropping one changes no verdict; and dropping `<hash-op>` from `<op>` changes nothing because
`<general-op>` accepts every `<hash-op>`. 29 more mutants sit in 10 rules no top-level object
reaches (`<5-tuple>` and its parts, `<dsa-sig-val>`, `<hash-list>`, `<subj-hash>`) and are not
counted. The 24 reader survivors were classified by category, not proven one by one (pass 2
re-derived each from its mutant number; the first count here had 17, 1 and 1 in the first, third
and fourth classes): 14 flip an end-of-input comparison, index against the length (lines 76, 81,
84, 225, 229, 239, 251, 253, 298, 310, 324, 328, 330, 362); 1 flips the not-found test `j < 0`
after `str.find`, where `j` is never 0 (line 273); 4 remove a `raise` (lines 99, 142, 165, 183);
2 turn an `or` into `and` (line 164, and the inner `or` of line 253); 2 raise an integer constant
(the `allow_atom` offset at line 144, and the 0 of `j < 0` at line 273); 1 flips an `is not None`
test (line 385). The reader's documented assumptions (A1 to A5 in the module docstring, A6 in
`check_date`) are where a different reader would legitimately differ.


## How the BNF is read (library choices, not the draft's)

- Section 3 says the examples and BNF "deal with advanced rather than canonical
  S-expressions" and section 9 says its BNF is canonical with lengths. They are one
  grammar read both ways: a quoted string means a byte string with exactly those bytes. The
  checker works on the parsed S-expression, so it is form-independent.
- `"(*)"` in `<tag-star>` is three tokens: `(`, the byte string `*`, `)`.
- A display type before a byte string is accepted wherever `<byte-string>` is, and
  never matches a quoted literal (a literal has no display type).
- `<cert>` fields are matched in BNF order (messages.yaml SD-09 records the prose disagreement).

Assumptions the draft leaves open, each flagged A1 to A5 in the docstring of
`spki_sexp.derived.py`: the token alphabet (A1), C string escapes (A2), whether the
advanced form accepts `N:bytes` (A3), display types in the advanced form (A4), and strict
base64 (A5). They affect advanced and transport input only, never canonical form. A6, in
the docstring of `check_date`, is the range check on each date field.

## BNF disagreements within the draft

`bnf-comparison.derived.txt` compares 66 fragment productions with section 9.2:
51 identical, 8 identical once a recorded alias or inline is applied, 6 different, 1 only
in a fragment. The aliases are the script's `ALIAS` table: `<cancel-list>` = `<crl-hash-list>`,
`<hash-of-pred>` = `<hash-of-crl>`, `<reval-list>` = `<reval-hash-list>`, `<tag-body>` =
`<tag-expr>` and `<threshold-subj>` = `<subj-thresh>`; the inlines are `<valid-basic>` and
`<tag-star>`. Each identical-after row of the comparison file names the ones it needed. One of
the eight, `<tag-body5>`, is equal only through an alias for a name the draft never defines
(`<tag-body>`), so it is also listed below as a difference; `<subject5>` stays different even
with `<threshold-subj>` aliased. The differences, reported as source defects (ids in
`messages.yaml`):

- `<online-test>`: 4.9.2 has `<online-id>` and a `new-cert` form, 9.2 has neither (SD-03).
- `<seq-ent>`: 6.2 omits `<name-cert>` (SD-04).
- `<reval>`: three right-hand sides in 7.2, 7.3 and 9.2 (SD-05).
- `<subject5>`: 9.2's `<fq-name5>` is defined nowhere; 8.1 names `<threshold-subj>` (SD-06).
- `<tag-body5>` refers to `<tag-body>`, defined nowhere (SD-07).
- `<subj-obj>` defined twice in 4.5, once as the minimal form (SD-12).
- Unused in 9.2: `<dsa-sig-val>` (which also says `dsa-sha1-sig` where the DSA sample says
  `dsa-sha1`), `<hash-list>`, `<subj-hash>` (SD-02, SD-11; §7.3's `<reval>` uses `<subj-hash>`).
- `(tag (*))` and `(tag (* set ...))` each match two productions (SD-13).

Laying the fragments over 9.2 changes the verdict of 8 of the 187 cases (listed at the end
of the comparison file), which is the measure of how much the disagreements matter.

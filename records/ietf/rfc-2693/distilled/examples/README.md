---
record: rfc-2693
kind: examples
title: "rfc-2693 — examples and test vectors"
extracted: "2026-10-11"
reviewed_by: ""
---

# RFC 2693 — examples and test vectors

`vectors.yaml` holds **94 vectors** in source order. **58** carry text RFC 2693
prints: every S-expression display, every other example display, and two
S-expressions printed inline in prose. **36** are **constructed**. Each one
tests a rule or a scenario outcome that the source states but prints no
literal for: the delegation, CRL and revalidation scenarios of §4 and §5, the
guard conditions of the 5-tuple rule, VIntersect cases, and threshold cases.
Pass 1 (extract), from the source only.

Every vector says how far it can be trusted, in two fields:

- **`fidelity`** describes the input. `verbatim` is the whole display, margin
  removed. `split` is part of a display or of a prose line, with every
  character still the source's. `constructed` was built for this file.
- **`expected_basis`** describes the expected value. `stated` means the source
  states this result for this input, and `expected` quotes it verbatim.
  `rule-quoted` means the source gives only the governing rule, and `expected`
  quotes that rule.

A top-level `result` or `outcome` appears **only** where the source states it.
Anything this extraction computed sits under `derived:` with
`in_source: false`, together with the rule applied. The file's header documents
these conventions and the others: the `notation` field, `input_lines` for
multi-line examples, margin stripping, quoting, and abstract time.

RFC 2693 contains no BCP 14 keyword; every `requirements.yaml` entry carries
verb `none`. Each vector's `constrains` lists the `rfc-2693#R-NNNN` entries
whose statements determine its expected or derived result. The cross-check
pass (pass 3) added the links; pass 1 extracted the file from the source alone.

## Coverage

| source section | from source | constructed | ids |
|---|---|---|---|
| §1.1 Glossary (S-EXPRESSION) | 0 | 2 | `SPKI-11-01`, `-02` |
| §2.6.1 Basic SDSI names | 1 | 0 | `SPKI-261-01` |
| §2.6.2 Compound SDSI names | 2 | 0 | `SPKI-262-01`, `-02` |
| §2.8 Fully qualified SDSI names | 1 | 0 | `SPKI-28-01` |
| §2.9 Fully qualified X.509 names | 2 | 0 | `SPKI-29-01`, `-02` |
| §2.10 Group names | 0 | 1 | `SPKI-210-01` |
| §3.1 Attribute certificates | 1 | 0 | `SPKI-31-01` |
| §3.2 X.509v3 extensions | 2 | 0 | `SPKI-32-01`, `-02` |
| §3.3 SPKI certificates | 4 | 0 | `SPKI-33-01` … `-04` |
| §4.1.2 Boolean control | 0 | 1 | `SPKI-412-01` |
| §4.2 A delegator exercising the permission | 0 | 1 | `SPKI-42-01` |
| §4.3 Delegation vs. ACLs (the firewall) | 0 | 1 | `SPKI-43-01` |
| §5.1 Anti-matter CRLs | 0 | 1 | `SPKI-51-01` |
| §5.2 Timed CRLs | 0 | 6 | `SPKI-52-01` … `-06` |
| §5.3 Timed revalidations | 0 | 1 | `SPKI-53-01` |
| §5.4 Setting the validity interval | 0 | 1 | `SPKI-54-01` |
| §5.5 One-time revalidations | 0 | 3 | `SPKI-55-01` … `-03` |
| §6.3 5-tuple reduction rules | 1 | 5 | `SPKI-63-01`; `-02` … `-06` |
| §6.3.1 AIntersect | 13 | 0 | `SPKI-631-01` … `-13` |
| §6.3.2 VIntersect | 1 | 4 | `SPKI-632-01`; `-02` … `-05` |
| §6.3.3 Threshold subjects | 1 | 3 | `SPKI-633-01`; `-02` … `-04` |
| §6.3.4 Certificate path discovery | 0 | 1 | `SPKI-634-01` |
| §6.4 4-tuple reduction | 4 | 1 | `SPKI-64-01` … `-04`; `-05` |
| §6.4.1 Threshold subject name reduction | 0 | 1 | `SPKI-641-01` |
| §6.4.2 4-tuple validity intersection | 0 | 1 | `SPKI-642-01` |
| §6.5.1 X.509v1 | 2 | 0 | `SPKI-651-01`, `-02` |
| §6.5.2 PGP | 1 | 0 | `SPKI-652-01` |
| §6.5.3 X.509v3 | 1 | 0 | `SPKI-653-01` |
| §6.5.7 SSL | 11 | 1 | `SPKI-657-01` … `-11`; `-12` |
| §7.3 Through `<name,key>` certificates | 3 | 0 | `SPKI-73-01` … `-03` |
| §7.5 One root per individual | 2 | 0 | `SPKI-75-01`, `-02` |
| §7.7 Threshold ACL subjects | 3 | 1 | `SPKI-77-01` … `-03`; `-04` |
| §8 Security considerations | 2 | 0 | `SPKI-8-01`, `-02` |
| **total** | **58** | **36** | **94** |

**How the 58 account for the source.**

- **Lines beginning "(".** 38 source lines start with "(" after the margin.
  - 34 are example displays, and every one is a vector input.
  - Lines 481, 1087 and 1167 are parenthetical asides in running prose.
  - Line 1502 is running prose that prints `(null)` inline, carried as split
    vector `SPKI-633-01`.
- **The other displays:**
  - 3 SDSI names
  - 9 arrow-notation mapping chains
  - the 5-tuple rule
  - 5 `AIntersect( … )` calls with their 4 printed results and "fails to
    intersect."
  - the VIntersect definition
  - 2 name-tuple classes and 2 name reductions
  - 3 translation tuples
  - 2 quoted names
- **The other inline S-expression** is `(tag (*))` in §6.5.3. The remaining
  parenthesised forms in running prose name forms the displays already carry,
  and are not values of their own: `(* set)` at lines 1757 and 1766, `(ssl)`,
  `(dns)` and `(us-crypto)` at 1767–1770, and `(acl-edit)` at 2030.
- **Displays that yield more than one vector.** Line 1764 prints two
  S-expressions, which become `SPKI-657-10` and `-11`. The ftp pair at 1373
  and 1379 also yields `SPKI-631-03`, for the intersection the source states
  between them.

**Every display-indented line accounted for.** The body (§1–§8, lines
145–2090) has 149 non-blank lines indented past the three-space prose margin,
page furniture excluded:

- **57** are carried as a vector input, operand, result or condition.
- **29** lie inside a verbatim quote: the star-form descriptions of §6.3.1
  (14), the §5.2 conditions (4), §6.1 item 1 and the infinity defaults of its
  item 5 (4), §6.2 item 2 and the infinity defaults of its item 4 (4), and §8
  item 1 (3).
- **63** are not carried. All of them are definitions or argument, not
  examples:
  - the three entity kinds and three processing stages of §6 (34)
  - the rest of the 5-tuple element list of §6.1 (11)
  - the rest of the 4-tuple element list of §6.2 (5)
  - the two question forms of §6.6 (4)
  - the second argument of §8 (9)

  They belong to the normative, messages and schema artifacts. Pass 1 counted
  128 = 56 + 24 + 48. That total leaves out the 21 lines indented exactly four
  spaces, which open numbered items, and its split did not reproduce; the
  figures above are pass 2's, re-derived by script.

## Sections with no vectors, and why

- **§1, §2 intro, §2.1–§2.5**: history and argument. No example is printed.
- **§2.6 intro, §2.7**: §2.7 argues that a public key, or its hash, is a
  global identifier, but prints none. The hash form first appears in §2.8.
- **§3 intro, §3.4 ACL entries**: §3.4 says a sample implementation "is
  documented, as a certificate body minus the issuer field" but prints none.
  ACL entries appear in the constructed vectors as `Self`-issued 5-tuples
  (§6.1, "the reserved word "Self"").
- **§4 intro, §4.1, §4.1.1, §4.1.3, §4.1.4**: arguments about depth control.
  SPKI has no depth field, so nothing is left to test. §4.1.4's laptop-key
  sentence is quoted in `SPKI-42-01`.
- **§5 intro**: quoted in `SPKI-53-01` (the certificate issuer names the
  issuer of validity confirmations).
- **§5.6**: one general claim ("always requires fewer signature
  verifications"), with no scenario.
- **§5.7, §5.7.1, §5.7.2**: alternatives the document does not adopt ("not
  reflected in the SPKI structure definition").
- **§6 intro, §6.1, §6.2**: definitions. Stage 1's VIntersect of on-line test
  results is applied in `SPKI-52-01` and `SPKI-53-01`, and the infinity
  defaults drive `SPKI-632-05`.
- **§6.5 intro, §6.5.4 X9.57, §6.5.5 SDSI 1.0, §6.5.6 SPKI**: statements of
  translation cardinality with no literal ("one or more 5-tuples", "one
  4-tuple", "one 4- or 5- tuple").
- **§6.6 Certificate Result Certificates**: the two question forms are
  definitions. `SPKI-657-12` exercises form 1, and the `derived.result` of
  every constructed reduction is a form-2 answer. No CRC is printed.
- **§7 intro, §7.1, §7.2, §7.4, §7.6**: key-management argument. §7.6 names a
  key inline by the base-64 of its hash (noted on `SPKI-75-02`).

## Source defects and ambiguities

These are recorded and not repaired. Each defect carries `source_issue` on its
vector.

1. **§6.5.1 contradicts §6.2 (`SPKI-651-01`, `SPKI-651-02`,
   definition-example-mismatch).** §6.2 defines the Name element of a name
   4-tuple as "a byte string". Both X.509v1 forms put an S-expression in that
   slot. The first, `(name <leaf-name>)`, fits only if it is read as notation
   for its one name, as §6.5.2 writes a bare `name`. The second puts a chain of
   k + 1 names there, `(name CA1 CA2 ... CAk <leaf-name>)`, and cannot be read
   that way. Every §6.4 4-tuple defines a single name `N` relative to its
   issuer. In §6.4 notation this tuple is
   `[(name Kroot CA1 … CAk <leaf-name>) -> K1]`, whose left side fits neither
   class. Read literally, both forms fail the schema's `four-tuple` (schema
   D-02).
2. **§5.2 condition 3 is ambiguous at a shared endpoint (`SPKI-52-04`,
   boundary-ambiguity).** "CRL validity date ranges must not intersect", and
   VIntersect's intervals are closed (it fails only "if Vmin > Vmax"). So the
   CRLs `[100, 200]` and `[200, 300]` intersect at 200 and break the first
   sentence. They meet the restatement, because the new CRL does not "take
   effect before the expiration" of the old one. No section says whether
   intervals are closed or half-open.
3. **§6.3.1's range template does not match its only example (`SPKI-631-08`,
   template-example-mismatch).** The template has bare
   `<lower-limit>? <upper-limit>?`, and the example writes `ge #30# le #39#`.
   The operators are never defined.
4. **§6.4.1 cites "[see 6.7]", and there is no §6.7.** Certificate Result
   Certificates are §6.6 (table of contents line 130, heading line 1780). This
   is not an example. It was noticed while reading, and is passed on for the
   normative and verify passes.

**Checked and not defective.** No parenthesis is unbalanced, in any of the 34
S-expression displays or any vector fragment. No example contradicts its stated
result: all six stated intersections and both name reductions reproduce
mechanically. §6.5.7's claim that `(dns (*))` "is equivalent to" `(dns)` holds,
but **only through the padding rule** of §6.3.1. On a strict reading of "all
lists that start with those elements", `(dns)` also contains the one-element
list `(dns)`, and `(dns (*))` does not.

**Underspecified, and recorded on the vectors that meet it:**

- **Numeric ordering.** The source never says how numeric ordering values a
  byte string (`SPKI-631-13`). The stated failure holds under all three
  plausible readings.
- **Encoding of K and N** (`SPKI-77-02`). The example writes them as binary
  octets (`#03#`), while the range example's limits `#30#`–`#39#` are exactly
  the ASCII codes of "0" and "9".
- **"delegation- intersected"** (`SPKI-633-02`).
- **The final decision rule** (`SPKI-657-12`): grant when the intersection
  succeeds, or only when it equals the request.
- **Template notation**: `*`, `?`, `...` and `<…>` (`SPKI-631-06`).
- **A verifier holding two overlapping CRLs**: what it must do is not stated
  (`SPKI-52-03`).

**Notation drift, not wrong.**

- Name 4-tuples have two notations. §6.4 writes `[(name K1 N) -> K2]`, with
  validity elided. §6.5 writes `[issuer, name, subject, validity]`.
- `<leaf name>` and `<CA(1)>` in §2.9 become `<leaf-name>` and `CA1` in §6.5.1.

## The vectors that earn their place

These ten, for a test harness built on this record.

1. **`SPKI-631-13`**: `(* range numeric ge #30# le #39# )` against `#26#`. This
   is the only failed intersection in the document. The failure holds whether
   the octets are read as integers, as ASCII digits or as raw bytes, so a
   harness can assert it without resolving what the source leaves open.
2. **`SPKI-631-10`**: set intersection. The printed result follows the first
   operand's order, and swapping the operands gives the same set in the other
   order. Compare `*-set` results as sets.
3. **`SPKI-631-11`**: the result is `(tag read)`, not `(tag (* set read))`.
   A singleton set collapses to its element, and an implementation can have
   the right set and the wrong representation.
4. **`SPKI-657-04` / `-05`**: the padding-rule pair. Their stated equivalence
   holds only because the shorter list is padded with `(*)`. Probed against
   nine tags, and the results agree up to `(dns)` against `(dns (*))`.
5. **`SPKI-632-04`**: `Vmin = Vmax` **succeeds**. One-time revalidation
   (`SPKI-55-02`) is a zero-length interval and depends on it. The same
   reading creates the §5.2 ambiguity (`SPKI-52-04`).
6. **`SPKI-75-01`** with **`SPKI-642-01`**: a name subject bypasses the
   delegation bit. The definer of a name can re-bind it at will even though
   delegation is FALSE everywhere, because name reduction (§6.4.2) has no
   delegation guard. The source presents this as the key-management feature.
   It is security-relevant, and a harness should pin it.
7. **`SPKI-52-02`**: fail closed. A certificate that is in date and was never
   listed **cannot be processed** without a valid CRL. This is the opposite of
   the anti-matter model (`SPKI-51-01`).
8. **`SPKI-633-04`**: a threshold needs K reductions **to the same subject**,
   not merely K reductions.
9. **`SPKI-64-05`**: a two-tuple naming loop. The unordered-pool safe rule
   applies class-1 tuples only, so it terminates without reaching a key.
10. **`SPKI-657-12`**: the SSL example end to end, built from the three
    printed tags (ACL, CA and leaf). It grants `(ssl)` and
    `(dns www.datafellows.com)` and denies `(us-crypto)`, exactly as the
    source states.

## Schema entry per vector

Inputs holding metavariables or placeholders are instantiated first: a key
symbol becomes a key, either a `public-key` list or a `hash`, with identical
results; a name symbol (`N`, `Na`, `...`) a `name-string`; an authorization
symbol a `tag`, or its binding where that is an S-expression; a validity
symbol its `[a, b]` binding as `{"not-before": a, "not-after": b}`, otherwise
`{}`; `[(name K N) -> S]` becomes `[K, N, S, {}]`; a `<placeholder>` a value
of the entry the schema README's *Template closure* names; prose scenarios
become the schema's records.

| entry | vectors | result |
|---|---|---|
| `s-expression` | SPKI-11-01, -02 | rejected, as §1.1 requires |
| `basic-sdsi-name` | `sexp` of SPKI-261-01, SPKI-262-01 | valid |
| `compound-sdsi-name` | `sexp` of SPKI-262-02 | valid |
| `fully-qualified-sdsi-name` | SPKI-28-01, SPKI-73-01, `sexp` of SPKI-73-03, SPKI-75-01; operand 1 and result of SPKI-64-03, -04 | valid |
| `fully-qualified-x509-name` | SPKI-29-01, -02 | valid |
| `hash` | SPKI-75-02 | valid |
| `name-string` | SPKI-73-02, inside its prose quotes | valid; not an `sdsi-name`, which is its `outcome: fails` |
| `tag` | SPKI-653-01, SPKI-657-01 … -11, SPKI-77-01; operands and results of SPKI-631-09 … -13 | valid |
| `tag-list` | SPKI-631-01, -02, -04; operands and result of SPKI-631-03 | valid; not `authorization` (D-11) |
| `star-all` | SPKI-631-05 | valid |
| `star-set`, `star-prefix` | SPKI-631-06, SPKI-631-07 | valid |
| `star-range` | SPKI-631-08 | example form valid; template read literally rejected (`source_issue`) |
| `tuple-validity` | bindings and results of SPKI-632-02 … -05 | valid |
| `null-subject` | SPKI-633-01 | valid; not a `subject` |
| `threshold-subject` | SPKI-77-02, -03 | valid; K and N in code (SC-01, SC-02) |
| `five-tuple` | the `<…>` tuples of SPKI-210-01, -412-01, -42-01, -43-01, -63-02 … -06, -633-02 … -04, -634-01, -641-01, -642-01, -657-12, -77-04, and derived tuples of these and of SPKI-75-01, -02 | valid |
| `four-tuple-defining-key` | SPKI-64-01; 4-tuples of SPKI-210-01, -641-01, -642-01, -652-01; derived 4-tuples of SPKI-262-02, -75-01 | valid |
| `four-tuple-defining-name` | SPKI-64-02, both 4-tuples of SPKI-64-05 | valid |
| `four-tuple` | operand 2 of SPKI-64-03, -04; SPKI-651-01, -02 | SPKI-651-01, -02 rejected read literally (`source_issue`, D-02) |
| `subordinate-five-tuple`, `threshold-subordinate-tuples` | derived intermediate form of SPKI-633-02, both `(null)` readings | valid |
| `authorization-certificate-body` | certificate C of SPKI-52-01, -02, -05, -06, SPKI-53-01, SPKI-55-02 | valid |
| `timed-crl` | CRLs of SPKI-52-01 … -05, -54-01, -55-01 | valid; SPKI-55-01 fails SC-08 in code |
| `timed-crl` | CRL of SPKI-52-06; anti-matter CRL of SPKI-51-01 | rejected |
| `current-crl` | full CRL of SPKI-52-01; anti-matter CRL of SPKI-51-01 | valid; SPKI-51-01 rejected |
| `timed-revalidation` | R of SPKI-53-01 | valid |
| `one-time-revalidation-request`, `one-time-revalidation` | SPKI-55-02, -03 | valid; SPKI-55-03 fails SC-11 in code |
| none: notation | SPKI-31-01 … -33-04, SPKI-8-01, -02; rule displays SPKI-63-01, SPKI-632-01 | checked by hand |

## What was checked, and how

Mechanically, by scripts kept outside the repository. Every result below is the
final run.

- **Both YAML readers agree.** PyYAML 6.0.1 `safe_load` and `bin/_yaml.py`
  `parse` give identical trees, value by value. `_yaml.py` returns every
  scalar as a string, so the 66 integer and boolean scalars are compared as
  strings. No block scalar, flow collection, anchor or alias is used, every
  free-text value is quoted, and the source holds no backslash, so no value
  does.
- **Ids.** 94, all unique. Each id's section digits match its locator, and the
  vectors are in source order.
- **Cross-links resolve.** All 89 `same_as` / `related` / `equivalent_to`
  links resolve. `same_as` and `equivalent_to` are reciprocal, and `same_as`
  pairs have identical inputs. Every `SPKI-…` id mentioned anywhere in the
  file is defined. The one cross-record link, rfc-9804 `SEXP-5-05`, resolves.
- **Verbatim, byte-exact.**
  - All 48 `verbatim` vectors equal whole source lines after margin removal.
    Multi-line ones match consecutive lines with relative indentation
    preserved; for example, the second operand of each `AIntersect` sits 12
    columns in, as printed.
  - In the 10 `split` vectors, every line is a byte-exact substring of one
    source line, and so are the 31 operand, result, condition and `sexp`
    fragments.
  - All 135 quotes (`expected` with basis `stated` or `rule-quoted`, plus
    `source_text`) are verbatim spans of the source. They are compared after
    whitespace normalisation: page header and footer removed, and a line-end
    hard hyphen rejoined.
  - The check found one pass-1 error, now fixed. `SPKI-641-01` had quoted
    "validity- intersection", but the source breaks "validity-intersection"
    at a hard hyphen.
- **Parentheses balanced** in all 122 fragments checked.
- **Lexing by notation.**
  - **Inputs that must lex.** These lex under the RFC 9804 token, hex and
    base-64 rules, and obey the §1.1 restrictions (no empty list; every list
    starts with a string):
    - 22 `sexp` inputs, every `sexp` vector but the two §1.1 counter-examples (23 strings: `SPKI-631-03` has two lines)
    - 10 `AIntersect` operands
    - 2 schematic `k-of-n` subjects
    - 4 embedded `sexp` fields
  - **Inputs that must be rejected.** Both §1.1 counter-examples fail the
    §1.1 restrictions. All 6 `sexp-template` and 9 `mapping-notation` inputs
    are rejected by the lexer, as their notation says.
- **Stated results reproduced** by an independent engine written from
  §6.3–§6.4 alone. All 6 stated intersections reproduce under each of the
  three readings of numeric ordering, and both name reductions reproduce.
- **Derived results recomputed.** 44 values, all agreeing:
  - the VIntersect cases
  - the five 5-tuple guards
  - the `AIntersect` derived cases
  - the SSL chain and its queries
  - the padding probes
  - the threshold result
  - interval arithmetic in §5
  - the key-hash facts: 20 octets (SHA-1 length), canonical base-64, hex
    `4cb0a03c…9d49`
  - the k-of-n facts: K = 3 and 5, N = 7, subordinate count 7, 0 < K ≤ N
- **Counts reconciled.** `vector_count`, `source_vector_count`,
  `constructed_vector_count` and every per-section figure in
  `count_reconciliation` match the file. The 38 lines beginning "(" and the
  149 display-indented lines are classified as above.
- **No unfinished-work marker** anywhere in `examples/`: the scaffold string `bin/validate` rejects under `profile: full` was scanned for and is absent.

**Pass 2 (verify, 2026-10-12).** An independent set of scripts re-derived
every check above from the cached source: the counts and per-section tallies,
every verbatim and split input and fragment, all 135 quotes with their
locators, the 89 cross-links, both YAML readers, and every stated and derived
result, recomputed by a separate engine written from §6.3–§6.4. Every concrete
S-expression input also validates against the entry of
`schema/spki-theory.derived.schema.json` it instantiates, as listed under
*Schema entry per vector*. No printed example
is missing. Fixed: the quote rule for line-end hyphens is now stated in the
file header; seven vectors gained `source_text_locator`, because a
`source_text` quote came from another section; `SPKI-631-13` no longer
presents inclusive range bounds as a finding; `SPKI-54-01`'s exposure window
and `SPKI-657-10`'s note were made exact; `SPKI-75-01` binds `Vn`; and the
display-line census above was re-derived.

**Pass 3 (cross-check, 2026-10-12).** Every vector was checked against the
schema entry listed under *Schema entry per vector*, with `jsonschema` 4.10.3
(Draft 2020-12): 255 checks over 83 vectors, 224 that must pass and 31 that
must fail, run once with keys as `public-key` lists and once as `hash` forms,
with identical results. The other 11 vectors are notation, not values, and
were checked by hand. Every stated and derived result was recomputed by an
engine written from the `aintersect`, `vintersect`, `five-tuple-reduction`,
`four-tuple-name-reduction`, `unordered-pool-name-reduction` and
`threshold-subject-reduction` steps of `protocol.yaml`: 115 checks over 74
vectors, all agreeing, and the 35 S-expressions inside `derived` blocks
validate. Fixed: `SPKI-63-02`, `-03`, `-04` and `-06` bound bare tag bodies as
5-tuple authorizations, which `five-tuple` rejects, and now wrap them in
`(tag …)`; `SPKI-651-01` carries `source_issue`; every vector carries
`constrains` (204 links to 126 distinct requirements).

**Not checked, because the document supports no such check.** There is no
reference implementation. The engine is this extraction's own, so agreement
shows the vectors are consistent with one careful reading of the rules, not
that they conform to any implementation. The public key behind
`|TLCgPLFlGTzgUbcaYLW8kGTEnUk=|` is never printed, so the hash can be checked
for shape only. No canonical forms are derived: RFC 2693 defines none, and the
definition lives in `rfc-9804`. The expected results of the 36 constructed
vectors are this extraction's application of the stated rules, and are marked
as such throughout.

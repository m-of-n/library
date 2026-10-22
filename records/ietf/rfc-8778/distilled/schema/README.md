---
record: rfc-8778
kind: schema
title: "rfc-8778 — schemas"
extracted: "2026-10-20"
reviewed_by: ""
---

# Schemas

<!-- The source's own CDDL / ASN.1 / JSON Schema, VERBATIM, in *.cddl or
*.schema.json, each file naming its source section. If the source has only
prose, write a machine-checkable schema and mark it `derived`. -->

**RFC 8778 ships no grammar of any kind, so six of the seven files here are the
library's own.** Measured over its 772 lines: `ABNF` 0, `ASN.1` 0,
`JSON Schema` 0, `CDDL` **1** — and that one occurrence is the title of the
RFC 8610 entry in §7.2's *Informative* references. There is no `COSE_Key`
anywhere (0 occurrences), `kty` occurs once and `pub` once as a word. What the
document does supply is **five concatenation renderings** in `[HASHSIG]`'s `||`
notation, **two lists of parameter-set names with no code points**, **one
checklist of five COSE-key conditions** and **three IANA registration
templates**. `source-renderings.txt` collects all of that verbatim; everything
else carries `.derived.` in its filename, per `docs/extraction.md`,
*Derived vs verbatim*.

| file | kind | what it is |
|---|---|---|
| `source-renderings.txt` | **verbatim** | 20 byte-exact runs of source lines — the Abstract, the BCP 14 recital, all five concatenation renderings, both name lists, §3's five checks, §4's state paragraph, §5's whole lifecycle, and all three registration templates. Each block carries its line range and the sha256 of the region's lines joined by `\n`. |
| `hss-lms-public-key.derived.cddl` | derived | the 56-octet `pub`, with every one of the four widths cited to an `R-id` and the u32str width's **measurement** written out. 3 rules. |
| `hss-lms-public-key.derived.schema.json` | derived | the same structure as a parsed object in hex, for a JSON test harness. `$id: urn:library:rfc-8778:hss-lms-public-key.derived`. |
| `hss-lms-cose-key.derived.cddl` | derived | the `kty: 5` `COSE_Key` assembled from §3's five checks and §6.2/§6.3's registrations, **plus RFC 9679 §4.5's thumbprint input over it** (cross-record, marked as such). 5 rules. |
| `hss-lms-cose-envelopes.derived.cddl` | derived | `COSE_Sign` (tag 98) and `COSE_Sign1` (tag 18) as Appendix A instantiates them. The document itself never says where the signature octets go. 6 rules. |
| `hss-lms-octets.derived.abnf` | derived | the flat byte layouts — public key, LM-OTS signature, LMS signature, both HSS signature forms — as RFC 5234 ABNF, so the **lengths** are machine-checkable. 21 rules. |
| `parameter-sets.derived.yaml` | derived | the nine parameter-set names, what RFC 8778 fixes about each (h, m, n, w, leaf count) and **what it does not**: no code point for any of the nine, and no value of `p` for three of the four LM-OTS variants. |

## What the renderings do not give you

Three gaps, and every derived file here is shaped by them.

1. **No width.** `u32str` and `||` are never defined. §2.1 (`R-0028`) says only
   "where the notation comes from [HASHSIG]". So the 4-octet width is
   **measured**, not cited — see below.
2. **No code point.** The five LMS tree sizes (`R-0041`…`R-0045`) and the four
   LM-OTS variants (`R-0073`…`R-0076`) appear as bare names. The document's own
   Appendix A then prints `00000003` and `00000006`, and **nothing in RFC 8778
   maps either number to any of the nine names.** Left open as a finding
   (`normative.md`, observation 8); `parameter-sets.derived.yaml` records it
   row by row.
3. **No value of `p`.** §2.3 (`R-0072`) defers every one to Appendix B of
   `[HASHSIG]`, so the length of an LM-OTS signature is not computable from
   RFC 8778. Partly closed by measurement: `p = 67` for the Appendix A fixtures.

## The 56 octets, and how each width was got

| field | octets | provenance |
|---|---|---|
| `u32str(lms_algorithm_type)` | 4 | **measured.** Not stated anywhere in RFC 8778 |
| `u32str(otstype)` | 4 | **measured**, same argument |
| `I` | 16 | **stated** — §3, `R-0092`, "it is the 16-byte identifier of the LMS public key for the tree" |
| `T[1]` | 32 | **arithmetic** — §2.2 `R-0052` ("T[1] is the m-byte string") with §2.2 `R-0039` ("supports only SHA-256 with m=32") |
| **total** | **56** | and §2.1 `R-0024` makes it the HSS public key as well as the LMS one |

**The u32str measurement, because "it is called u32" is not a citation.**
RFC 8778's own formulas give the signature length as
`4·u + n + n·p + m·h` octets, where `u` is the u32str width and the four
u32str fields are `Nspk` (§2.1 `R-0027`), `q` and the LMS type code (§2.2
`R-0062`) and `otstype` (§2.3 `R-0079`); `n = m = 32` by `R-0066` and `R-0039`.
Both printed signatures measure **2512** octets. Then:

| `u` | `2512 − 4u − 32` | `÷ 32` | |
|---|---|---|---|
| 1 | 2476 | 77.375 | impossible |
| 2 | 2472 | 77.25 | impossible |
| **4** | **2464** | **77** | **the only integer among these four** |
| 8 | 2448 | 76.5 | impossible |

**[correction] 2026-10-21, FX-1 pass 2 — the divisibility test does not give
uniqueness, and this file and five others said it did.** That last cell read
"the only integer". It is the only integer *in this table*. The congruence
`2512 − 4u − 32 ≡ 0 (mod 32)` reduces to `u ≡ 4 (mod 8)`, so **`u = 12`, `20`
and `28` satisfy it too** (with `p + h = 76`, `75`, `74`). The arithmetic alone
excludes 1, 2 and 8 and nothing wider.

**What does pin `u = 4` is the second leg, and it is in the printed octets.**
Octets 0–3 of **both** signatures are `00000000`, which is exactly §2.1
`R-0027`'s `u32str(0)` for a stand-alone tree, and the two signatures first
differ at octet **7** — the leaf number `q`, `00000001` in A.1 against
`00000000` in A.2. Under `u = 12` the first field would run to octet 11 and the
leaf number would begin at octet 12, where both signatures carry `91291de7…`;
under `u = 4` every one of the four `u32str` fields holds a small integer
(`0`, `1`/`0`, `3`, `6`) at the predicted offset. Taken together with the
congruence, `u = 4` is the only width consistent with the printed bytes.

Then `p + h = 77` falls out of it, and `h = 10` follows because only `p = 67`
puts a small integer (`00000006`) at the resulting type-code offset, 2188, with
exactly 10 trailing 32-octet path nodes as §2.2 `R-0060` requires — the other
four admitted `h` values put `bb1d8cc8`, `b0e99b2b`, `366c8ffe` and `352e20e0`
there. Independently: the two signatures share a **288-octet** common suffix,
which is 9 × 32, exactly the `path[1..9]` that `R-0061` predicts two sibling
leaves share.

**56 octets holds for all 20 parameter-set combinations RFC 8778 admits** — all
five tree sizes are `M32`, all four LM-OTS variants are `N32`, `I`'s width is
stated unconditionally, both type codes are `u32str`. It is **not** future-proof,
and that is the `DEC-002` point: `R-0046` and `R-0077` both say `[HASHSIG]`
establishes an IANA registry for additional hash functions, tree sizes and
parameter sets, so a registered `m ≠ 32` changes `T[1]` and the total.

## Verification

- **14 CDDL rules across three files; 13 distinct.** `hss-lms-pub` is defined in
  two files and the definition — `bstr .size 56` — is identical in both; the
  trailing comment differs. Every referenced rule is defined in its own file and
  nothing collides with the RFC 8610 prelude. A naive grep reports
  `protected`, `unprotected`, `payload`, `signature`, `signatures`,
  `lms_algorithm_type`, `otstype`, `I` and `T1` as unresolved; they are CDDL
  **member keys** inside arrays and maps, not rule references.
- **21 ABNF rules, closed.** Terminals: `%x00-FF` (the `OCTET` rule) and the
  two fixed `Nspk` values, `%x00.00.00.00` and `%x00.00.00.01`. *(Corrected
  2026-10-21: this said `%x00-FF` was the only terminal.)*
- **`parameter-sets.derived.yaml` round-trips through both of the library's YAML
  readers** — `bin/_yaml.py` and `bin/_record_yaml.py` — and they agree on all
  eight top-level keys. The file was first written with flow maps spanning two
  lines, which `_record_yaml` cannot parse; `bin/validate` caught it and it is
  block mappings now.
- **The JSON Schema parses** and its `$id` is the `urn:library:` form
  `docs/extraction.md` requires.
- **Both envelope shapes re-encode to the document's own stated sizes** — 2560
  and 2552 octets — which is the strongest check available on
  `hss-lms-cose-envelopes.derived.cddl`. See `../examples/README.md`.

## What no schema here can constrain

- **The private key.** §5 (`R-0115`) withholds the encoding deliberately, so
  there is nothing to write a grammar for. §6.3 registers one parameter for
  `kty: 5` and it is the public key.
- **A `kid`'s relation to `I`.** §3 (`R-0090`) permits a `kid` to be the
  16-octet `I` and nothing binds it, so no schema can check the two agree. The
  document's own examples use `'ItsBig'`.
- **Leaf-usage state.** `R-0097` requires it be kept and no format exists.
- **Determinism and map order.** `canonical` and `deterministic` each occur 0
  times in RFC 8778. The deterministic-encoding requirement on a thumbprint
  input comes from RFC 9679 §3 step 2, not from here.

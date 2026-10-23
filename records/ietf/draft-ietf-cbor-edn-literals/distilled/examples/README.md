---
record: draft-ietf-cbor-edn-literals
kind: examples
title: "draft-ietf-cbor-edn-literals — examples and test vectors"
extracted: "2026-10-19"
reviewed_by: ""
---

# draft-ietf-cbor-edn-literals — examples and test vectors

`vectors.yaml` holds **251 vectors** extracted from
`draft-ietf-cbor-edn-literals-27`, "Concise Diagnostic Notation (CDN)", in
source order. **242 are valid; 9 are invalid**, and every invalid one carries a
`violates` naming the rule it breaks and the section that states it.

A diagnostic-notation document is almost entirely examples, so this is the bulk
artifact of the record. The set is the complete inventory of CDN literals the
document prints — not a selection.

## Fields

| field | meaning |
| --- | --- |
| `id` | stable `draft-ietf-cbor-edn-literals#V-NNNN` handle, quoted because it contains `#` |
| `locator` | the section (or section + table) the literal is printed in |
| `edn` | the CDN text, **verbatim** from the source, as a `\|-` block scalar so no escaping intervenes |
| `hex` | the encoded CBOR, lowercase, no spaces; see *Provenance of every byte* below |
| `decoded` | what the literal denotes, in words |
| `expect` | `valid` or `invalid`; see *What `expect` means* |
| `violates` | invalid vectors only: the rule broken, by section, quoted |
| `notes` | provenance marker, the source's own framing, and any caveat |

Sibling vector sets in this library (`rfc-8949`, `draft-ietf-cbor-cde`,
`draft-ietf-cbor-serialization`, `draft-mcnally-deterministic-cbor`) call this
field `diagnostic`. Here it is `edn`, because in this record the notation is the
*subject* rather than a convenience. A tool joining across sets should treat
`edn` and `diagnostic` as the same column.

## Provenance of every byte

`notes` begins with one of three markers. This is the whole point of the
record, so it is machine-greppable:

| marker | count | meaning |
| --- | --- | --- |
| `SOURCE HEX.` | **52** | the document prints these bytes. This extraction **decoded them and confirmed they denote the `edn`**. |
| `SOURCE HEX CORRECTED.` | **1** | the document prints bytes that **do not** denote the `edn`. `hex` carries *our* corrected bytes; `notes` quotes the document's and shows the arithmetic. |
| `COMPUTED HEX.` | **173** | the document prints only the EDN. The bytes are this extraction's encoding of it, in RFC 8949 Preferred Serialization unless an encoding indicator says otherwise — which is the document's own assumption, `R-0222` (§4.1). |
| `NO HEX.` | **25** | no bytes, and the reason is stated — almost always an unassigned `CPA888`/`CPA999` tag number, occasionally a value the document declines to fix. **Seventeen carry `expect: valid`** and are the deliberate non-encodables; the other eight are eight of the nine `invalid`. |

**63 byte sequences printed by the document were independently re-encoded from
the EDN and compared; 61 matched and 2 did not** — the 2 are both cells of one
Table 6 row (below). The 63 are the 52 `SOURCE HEX.` vectors, the one
`SOURCE HEX CORRECTED.` vector, and the ten "ignoring e.i." cells of Table 6,
which are checked even though they are not vectors of their own. Every printed
byte sequence in the document is covered: Table 1 (8 cells), Table 2 (14),
§2.5's pretty dump, §3.6's five `ilbs` lines, §3.8's pretty dump,
Table 6 (10 rows × 2 columns), §4.2's `98 02 f4 f5` and §4.3's
`5f ff` / `7f ff`.

> Pass 1 put this at **61 compared, 59 matched**, having left §4.3's two out:
> `''_` and `""_` (`V-0212`, `V-0213`) were marked `COMPUTED HEX.` although
> §4.3 prints their bytes. Both agree, so only the arithmetic moved.

> A byte string this extraction derived is **never** presented as one the
> document printed. Where the two disagree, both appear and the disagreement is
> the finding.

> The cross-check pass moved one vector out of `NO HEX.`. `V-0238`
> (`987654321098765432310`) withheld its bytes because "the encoding REQUIRES
> major type 6 (tag 2), which is exactly what a no-IANA-tags profile forbids" —
> while `V-0239` carried `c249358a750438f380f5f6` for **the same value**, one
> line below, from the same sentence of §6.1 item 5: "E.g.,
> 987654321098765432310, which is equivalent to `2(h'35 8a 75 04 38 f3 80 f5
> f6')` in its Preferred Serialization". A vector set cannot refuse a value's
> bytes on one line and print them on the next, and the withheld side was the
> wrong one: the reason given was a statement about **our** tag profile, not
> about the document declining to fix the value, which it fixes in that very
> clause. `V-0238` now carries the bytes, with the profile caveat kept in
> `notes`. Provenance moved `172`/`26` → `173`/`25`; the `NO HEX.` class is now
> exactly the deliberate non-encodables and the invalid vectors, with nothing in
> it whose bytes the document states.

## The defect the round-trip found

**Table 6 (§4.1), major-type-3 row, is wrong in both of its hex columns.** The
source prints:

```
| 3  | "A"_1        | 79000161           | 6161          |
```

`0x79` is major type 3 with `ai=25`, so the two-byte length `0x0001` is followed
by the string's single content byte — and `"A"` is U+0041 = `0x41`. The correct
encodings are **`79000141`** and, ignoring the encoding indicator, **`6141`**.
`79000161` and `6161` encode `"a"`, not `"A"`.

The error is almost certainly copied from the row above it: for the
major-type-2 row `'A'_1 | 59000141 | 4141`, a one-byte byte string's head is
`0x41` and its content byte is also `0x41`, so head and content coincide. For
major type 3 the head is `0x61` and the content is still `0x41`, and the row was
written as though they coincided too. `V-0206` carries the corrected bytes and
quotes the document's. Every other cell of Table 6 was decoded and confirmed.

**Two vectors of our own were wrong, and the verify pass corrected them.**
`V-0131` (`dt'1969-07-21T02:56:16.0Z'`) and `V-0139` (`-14159024.0`) carried
`fbc16b019600000000`, the binary64 encoding. −14159024 is `0xD80CB0`, which
needs 20 significant bits, so binary32 holds −14159024.0 exactly and RFC 8949
Preferred Serialization — the convention this file states, and the one
§4.1 itself assumes for a literal with no encoding indicator (`R-0222`) —
requires the shortest form that preserves the value. Both now carry
**`facb580cb0`**. `V-0132`/`V-0140` (−14159023.5) need 25 significant bits and
keep binary64, which is why the error was easy to miss: the neighbouring rows
of the same table are right.

Two further source defects are recorded as vectors rather than fixed:

- **`b1<"Hello world">` (§3.5, `V-0174`)** uses single angle brackets where
  `app-sequence = app-prefix "<<" seq ">>"` (§6.1) requires doubled ones. The
  line is 20 characters long in a document whose longest line is 78, so it is
  not a margin truncation — it is a typographical error in draft-27, and a tool
  fed the document's examples verbatim will stop on it.
- **The `bytes_in_IRI` line of §5.2 (`V-0231`)** also ends in a single `>`, but
  that line *is* 78 characters, exactly the document's maximum, so it is almost
  certainly a right-margin truncation in the plain-text rendition rather than an
  error in the authored source. It is transcribed as we hold it and marked
  `invalid`, with the distinction spelled out in `notes`; a reader with the XML
  source should re-check it.

## Every vector against the grammar

**The cross-check pass (2026-10-19) ran all 251 `edn` values through the §6.1
grammar.** This is the check that had never been done: the vectors are CDN
*source text* and `../schema/cdn.abnf` is CDN's own ABNF, so "does this example
validate against the schema" means "does this `edn` parse". The instrument was an
RFC 5234 ABNF reader plus a memoised set-of-end-positions recogniser, reading
`cdn.abnf`'s own bytes — it strips the `;` headers and the three-column margin
itself, so the grammar under test is the verbatim artifact and not a
transcription. It is a backtracking recogniser, **not** a PEG: ABNF alternation
is unordered, so where §6's ordered choice is load-bearing it accepts the union
(`schema/grammar-gaps.derived.txt` G‑08).

**242 of 251 parse as held. 246 of 251 parse with the document's own line
terminator restored.** The verdict is identical from both candidate start
symbols and identical under both readings of the raw-string delimiter widths.

| vector | `expect` | why it does not parse |
| --- | --- | --- |
| `V-0014` `//` | invalid | `comment = … / eol-comment *non-lf %x0A` needs the terminating LF (G‑31). With the LF it parses under `seq` as an item-less sequence and not under `one-item` — the **only** input in the corpus where the start symbol matters |
| `V-0015` `/*foo/` | invalid | `ends-in-star` needs a `*`, and `non-slash-star` excludes both `*` and `/`, so neither the slash nor the C-style alternative can match |
| `V-0059`–`V-0061` | **valid** | each ends in a trailing `#` comment, which needs the LF the block scalar strips (G‑31). Valid CDN on the document's own line; the three are the only vectors affected |
| `V-0101` `[[][]]` | invalid | `MSC = ("," S) / (MS ["," S])` and both alternatives are non-empty, so the separator is **mandatory in the grammar**, not only in §2.4.1's prose |
| `V-0174` `b1<"Hello world">` | invalid | `app-sequence` doubles the angle brackets. All three of `b1<…>`, `b1<…>>` and `b1<<…>` are rejected; only `b1<<"Hello world">>` parses |
| `V-0220` `(_ )` | invalid | `streamstring = "(_" MS string *(MSC string) SOC ")"` requires at least one `string` |
| `V-0231` | invalid | the `bytes_in_IRI` line's single `>`. Restore it and the whole example parses, which is the evidence that the rest of the four-line literal is sound |

Three results worth stating because they are easy to assume the other way:

- **Six of the nine `invalid` vectors fail the GRAMMAR, not only the semantics.**
  Only `V-0044`, `V-0045` (`1.1_1`, `1.1_2` — encoding indicators too small) and
  `V-0102` (a duplicate map key) parse and then fail on meaning. The sibling
  `rfc-8610` record's invalid set is mostly the semantic kind; this one is not,
  because four of CDN's own error cases — the two repurposed comment forms, the
  mandatory separator and the chunkless `(_ )` — are written into Figure 1. Every
  one of the six carries a `violates` that already cited the §6.1 production, so
  the artifact and the parser agree.
- **All 17 deliberate non-encodables parse.** Ellipses, the CRI model, the
  unassigned `CPA888`/`CPA999` tags: those are reasons no *bytes* can be given,
  and none of them is a parse failure. 17 of 17.
- **`seq` versus `one-item` changes no verdict.** §6.1 names no root and
  `one-item` is referenced nowhere (G‑19), so the choice is undecided. On this
  corpus it is also inconsequential: the two differ only on item-less and
  multi-item input (`seq` admits the empty text, a comment-only text, several
  items and a trailing comma; `one-item` admits exactly one item and no trailing
  comma), and exactly one vector is of that shape — `V-0014`, and only once its
  newline is restored. The defect is real; the exposure here is one line.

## What `expect` means

CDN sits over two different notions of correctness, and the document itself
keeps them apart (§2: implementations "MAY support generation and possibly
ingestion of CDN for CBOR data items that are well-formed but not valid").
`expect` folds both into one verdict, and `violates` says which:

- **`valid`** — the text parses as CDN under the §6.1 grammar **and** the data
  item it denotes is valid CBOR.
- **`invalid`** — one of those two fails. Four of the nine are *syntax*
  (`//`, `/*foo/`, `[[][]]`, `(_ )`, plus the two bracket defects above); two
  are *encoding-indicator* errors the document itself prints as `(error)`
  (`1.1_1`, `1.1_2`); one is *CBOR validity* with perfectly good CDN syntax
  (`{1: "to", 1: "from"}`, a duplicate map key).

The nine: `V-0014`, `V-0015` (§2.1.1), `V-0044`, `V-0045` (§2.2 Table 2),
`V-0101` (§2.4.1), `V-0102` (§2.4.2), `V-0174` (§3.5), `V-0220` (§4.3),
`V-0231` (§5.2).

## What counts as a vector

A vector is **a complete CDN literal or document that the source prints**.
Applying that rule consistently:

- Where a table maps a literal to an equivalent (`dt` → plain CDN, `ip` → plain
  CDN, `hash` → digest), **each distinct literal in either column** is one
  vector, and the equivalence is recorded in `decoded`. Repeated right-hand
  values are not repeated as vectors.
- Notation named in prose (`h''`, `<<>>`, `b64''` in §1.3.2–§1.3.3) **is**
  vectored: those are complete literals with determinate values.
- **Fragments are not vectored.** Encoding-indicator spellings on their own
  (`_`, `_i`, `_3`, the reserved `_4`–`_7`), escape spellings on their own
  (`\r`, `\t`, `\u{NNN}`), bare prefix names (`h`, `b32`, `h32`, `b64`, `pragma`),
  ABNF rule names and registry rows are not literals. They belong to
  `normative.md`, `requirements.yaml` and `schema/`.
- The CDDL shown beside CDN in Appendix A is **not** CDN and is not vectored;
  it is analysed in `design-notes.md`.

## Where the vectors came from

| `locator` | ids | count |
| --- | --- | --- |
| `§1.2` | V-0001 – V-0004 | 4 |
| `§1.3.2` | V-0005 – V-0006 | 2 |
| `§1.3.3` | V-0007 – V-0008 | 2 |
| `§2.1` | V-0009 – V-0013 | 5 |
| `§2.1.1` | V-0014 – V-0017 | 4 |
| `§2.2` | V-0018 – V-0027 | 10 |
| `§2.2 Table 1` | V-0028 – V-0042 | 15 |
| `§2.2 Table 2` | V-0043 – V-0058 | 16 |
| `§2.3.1` | V-0059 – V-0061 | 3 |
| `§2.3.2` | V-0062 – V-0063 | 2 |
| `§2.3.3` | V-0064 – V-0070 | 7 |
| `§2.3.4` | V-0071 – V-0084 | 14 |
| `§2.4.1` | V-0085 – V-0101 | 17 |
| `§2.4.2` | V-0102 | 1 |
| `§2.5` | V-0103 – V-0105 | 3 |
| `§2.6` | V-0106 – V-0111 | 6 |
| `§3` | V-0112 – V-0114 | 3 |
| `§3.1` | V-0115 – V-0129 | 15 |
| `§3.2 Table 3` | V-0130 – V-0141 | 12 |
| `§3.3` | V-0142 – V-0147 | 6 |
| `§3.3 Table 4` | V-0148 – V-0160 | 13 |
| `§3.4 Table 5` | V-0161 – V-0168 | 8 |
| `§3.5` | V-0169 – V-0184 | 16 |
| `§3.6` | V-0185 – V-0189 | 5 |
| `§3.7` | V-0190 – V-0193 | 4 |
| `§3.8` | V-0194 – V-0201 | 8 |
| `§4.1 Table 6` | V-0202 – V-0211 | 10 |
| `§4.1` | V-0212 – V-0213 | 2 |
| `§4.2` | V-0214 – V-0217 | 4 |
| `§4.3` | V-0218 – V-0222 | 5 |
| `§5.1` | V-0223 – V-0226 | 4 |
| `§5.2` | V-0227 – V-0233 | 7 |
| `§6.1 item 3` | V-0234 – V-0237 | 4 |
| `§6.1 item 5` | V-0238 – V-0240 | 3 |
| `§6.2.1` | V-0241 – V-0244 | 4 |
| `Appendix A` | V-0245 – V-0251 | 7 |

A literal that recurs in a later section making a different point is kept as a
separate vector (`h''` at V-0006 and again at V-0241, where §6.2.1 covers it as
the empty case of the `app-string-h` grammar). `notes` says so when it happens.
**Match vectors on `id`, never on `edn` or `hex`:** 226 vectors carry a `hex`
and those take only 113 distinct values, so 177 of them share bytes with at
least one other — that is what an equivalence table is. Six `edn` strings
(`true`, `h''`, `<<>>`, `1.5_2`, `h'68656c6c6f20776f726c64'`, `'Hello world'`)
occur twice, always in two different sections making two different points.

## The arithmetic this extraction re-did

Everything the document asserts numerically was recomputed:

- `0x1267 = 0o11147 = 0b1001001100111 = 4711` (Table 1).
- `0x1.8p0 = 0x18p-4 = 0.15e1 = 15e-1 = 1.5`, and `f9 3e00` is binary16 1.5.
- **`1.1_1` and `1.1_2` really are errors**: binary16 of 1.1 is 1.099609375 and
  binary32 of 1.1 is 1.100000023841858. Neither is 1.1, so neither width can
  carry the item unchanged (§4.1). The only two `(error)` cells in the document.
- base64 `EjRWeA` → `12345678`; `Zm9v` → `foo`.
- The §3.1 "deliberately confusing" pair: stripping blank space and the `#`
  comment from `b64'/base64 not a comment/ but one follows # comment'` leaves
  `/base64notacomment/butonefollows`, which base64-decodes to exactly the 24
  bytes `h'FDB6AC 7BAE27A2D69CA2699E9EDFDBBADA2779FA25 968C2C'` prints. The
  `/bas` → `FDB6AC` and `lows` → `968C2C` sub-claims also hold.
- `dt'1969-07-21T02:56:16Z'` → epoch **-14159024** (Table 3).
- `IP'2001:db8::/64'` → `54([64,h'20010db8'])` — the RFC 9164 §4.2 truncation is
  applied correctly, and the address expansions in Table 4 are right.
- **SHA-256 and SHA-512 of `'foo'` match Table 5 digest for digest.** Those two
  rows are directly usable fixtures.
- `0x4711p+03 = 145544.0`, `fb4101c44000000000` is its binary64 and
  `fa480e2200` its binary32 (Table 6).
- `0x1.22102ap+15 = 37128.08203125 = fa47110815` (§3.8), and `float'fe00'` is a
  binary16 NaN with the sign bit set, whose binary32 image is `ffc00000`.
- **`h'358a750438f380f5f6'` is exactly `987654321098765432310`** (§6.1 item 5).
  The document's bignum arithmetic is correct.
- `<< {/alg/ 1: -7 /ECDSA 256/} >>` is `h'a10126'`, as the document's own
  comment claims (Appendix A). The only place the document prints an
  embedded-CBOR literal and its bytes together; they agree.

## What this set does **not** contain, and why

- **No `b32'…'` or `h32'…'` vector.** The document does not print one. §3.1 says
  base32 and base32hex "ha[ve] not been implemented widely and therefore [are]
  not directly included in this specification", while §7.1 Table 8 still
  *reserves* `b32` and `h32` with RFC 8949 as the reference. So they are
  syntactically well-formed `app-prefix`es (§6.1 `app-prefix = lcalpha *lcldh`)
  with no defined value, which under §5.1 is an error or a `CPA999` tag. The
  consequences for writing our vectors in EDN and validating them against CDDL
  are in `design-notes.md`; they are not representable as a vector here, because
  inventing the literal would be fabrication.
- **No `ilbs`/`ilts` registry entry.** §3.6 defines both and §4.3 makes them the
  replacement for the deprecated `streamstring`, but neither appears in §6.2
  Table 7 nor in §7.1 Table 8. The five §3.6 vectors are therefore written with
  prefixes that are, as draft-27 stands, unregistered. See `design-notes.md`.
- **No encoding for anything needing `CPA888` or `CPA999`.** Eight of the
  twenty-five `NO HEX.` vectors name one of those tag numbers outright. Those
  tag numbers are placeholders; §7.5's RFC-Editor note says to substitute what
  IANA assigns (suggested 888 and 999). Any byte string we invented would go
  stale at publication.
- **No digest for `hash<<"data", -44>>` (V-0225).** §3.4 says the input is "a
  (text or byte) string" but never says whether the bytes hashed are a text
  string's UTF-8 content or its CBOR encoding, and Table 5 uses only the byte
  string `'foo'`, so the text-string case is unexercised. A real gap in the
  document, recorded rather than guessed.
- **No expansion for `cri'https://example.com'` (V-0223).** The CRI data model
  lives in `I-D.ietf-core-href`, which this record does not hold, and §3.7's
  worked example does not fix what an empty path becomes.

## Verifying this file

```sh
python3 -c "import sys,pathlib;sys.path.insert(0,'bin');\
from _record_yaml import load_yaml;from _yaml import parse as m;\
p=pathlib.Path('records/ietf/draft-ietf-cbor-edn-literals/distilled/examples/vectors.yaml');\
a=load_yaml(p)['vectors'];b=m(p.read_text())['vectors'];\
print(len(a),len(b),len({x['id'] for x in a}))"
```

Expected: `251 251 251`. Both of the library's readers parse the file to the
same 251 records field for field; `edn` is always a `|-` block scalar and every
other string is single-quoted, because the two readers process backslash
escapes in double-quoted scalars differently and EDN is full of backslashes.

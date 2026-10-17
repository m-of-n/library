---
record: draft-mcnally-deterministic-cbor
kind: examples
title: "draft-mcnally-deterministic-cbor (dCBOR) — examples and test vectors"
extracted: "2026-10-16"
pass: 1
reviewed_by: ""
---

# dCBOR — examples and test vectors

`vectors.yaml` holds **72 vectors**: every example and test vector in
`draft-mcnally-deterministic-cbor-18` (1232 lines), in source order, with no
gaps in the id sequence.

| | count |
|---|---|
| `expect: valid` — the profile accepts these bytes | **56** |
| `expect: invalid` — well-formed CBOR this profile **forbids** | **16** |
| hex printed by the source | **62** |
| hex computed by this extraction (flagged `OUR COMPUTATION` in `notes`) | **5** |
| no hex — the source states the case but names no value (flagged in `notes`) | **5** |

No fixture files. The largest vector is 22 bytes, so everything sits inline.

The negative half matters as much as the positive half. dCBOR does not extend
CBOR, it narrows it: **every one of the 16 invalid vectors is well-formed,
and most are preferred-serialization, RFC 8949 CBOR that a stock decoder
accepts.** The source says so itself at §7.2 — "These are valid CBOR
encodings that MUST be rejected as invalid by a dCBOR-compliant decoder."
Each one carries a `violates` field naming the rule it breaks and the section
that states it.

## Fields

| field | meaning |
|---|---|
| `id` | `draft-mcnally-deterministic-cbor#V-NNNN`, source order, never reused |
| `locator` | the section, figure, rule number or table row the vector comes from |
| `diagnostic` | the value in CBOR diagnostic notation, as the source writes it |
| `hex` | the encoded bytes, lowercase, no separators. **Absent** when the source states a case without naming a value |
| `decoded` | what the bytes decode to, in words — including the integer a float reduces to |
| `expect` | `valid` or `invalid`. `invalid` means *this profile forbids it*, not that it is malformed CBOR |
| `violates` | on `invalid` vectors only: the rule broken, cited by section |
| `notes` | the source's own framing, in its words where it has them, plus provenance |

Ids are **quoted** in the YAML. `bin/_record_yaml.py` strips `#` to end of
line even mid-token, so an unquoted `…-cbor#V-0001` parses as `…-cbor`. Keep
the quotes.

### Provenance, and what it means

`notes` carries one of three provenance markers, or none:

- **nothing** — the source prints these bytes. 62 vectors. Every one was
  checked to occur verbatim in `.cache/draft-mcnally-deterministic-cbor.txt`,
  bare or as `0x…`.
- **`OUR COMPUTATION`** — the source prints diagnostic notation or a code
  point, and the bytes were derived here. 5 vectors: `V-0006`, `V-0007`
  (Figures 1 and 2), `V-0067`, `V-0068` (the `[1, NaN, 3]` array of §8.3),
  `V-0070` (`undefined`, from code point 23). Nothing in these five is
  presented as the source's own byte string.
- **`NO BYTES AND NO VALUE IN THE SOURCE`** — the source states the case in
  prose and names no instance, so `hex` is absent rather than guessed. 4
  vectors: `V-0064`, `V-0065` (the Tag 1 example of §8.1), `V-0071`,
  `V-0072` (the Tag 2/3 and Tag 80/81/82 escape hatches of §8.5). These are
  scope markers, not runnable cases: our suite supplies its own instances.

`V-0066` also has no `hex`, for a different reason — see the source issues
below.

## How to use it

Three checks, one vector at a time.

```python
for v in yaml["vectors"]:
    if "hex" not in v:                     # scope markers; nothing to run
        continue
    raw = bytes.fromhex(v["hex"])

    # 1. decoder acceptance — the check the whole profile turns on
    assert dcbor_decode_accepts(raw) == (v["expect"] == "valid"), v["id"]

    # 2. round trip — determinism, for the accepted ones
    if v["expect"] == "valid":
        assert dcbor_encode(dcbor_decode(raw)) == raw, v["id"]
```

The third check is the encoder side, and it is the one that catches Numeric
Reduction. Feed the **`diagnostic`** value to the encoder and require
`hex` back. 11 of the valid vectors are a float on the way in and an integer
on the way out (`42.0` → `182a`, `-0.0` → `00`, `65504.0` → `19ffe0`), so a
decode/re-encode loop alone will never exercise rule 1 of §2.5 — the
reduction has already happened before the bytes exist. `diagnostic` is the
input; `decoded` says what should come back.

Three vectors are classes rather than single values. `V-0050`, `V-0051` and
`V-0052` read `Infinity (any size)`, `-Infinity (any size)` and
`NaN (any size, any payload)`: the encoder must map **every** width and, for
NaN, every payload and sign onto the one printed encoding. Their decoder-side
counterparts are enumerated — `V-0057` to `V-0063`.

Nothing here needs a network or a fixture file. The suite is self-contained
in `vectors.yaml`.

### Recursion

§2 states that "A CBOR data item is considered to conform to dCBOR only if
every CBOR data item nested within it, recursively (including array elements,
map keys and values, and the contents of tagged data items), also conforms to
the narrowing rules". Every scalar vector is therefore also a test of the
container case: wrap any `invalid` vector in an array, a map value or a tag
and it must still be rejected. `V-0068` is the one worked instance of this in
the source's own material (a bad NaN inside an array), and `V-0065` the one
for tag content. The 12 scalar negatives — `V-0053` to `V-0063` and `V-0070`
— are worth re-running inside an array, a map key, a map value and a tag.

## Where the vectors come from

| source location | vectors | ids | valid / invalid |
|---|---|---|---|
| §2.5 intro — the `2` / `2.0` pair | 2 | `V-0001`–`V-0002` | 2 / 0 |
| §2.5 rule 1 — the three zeros | 3 | `V-0003`–`V-0005` | 3 / 0 |
| §2.5 Figures 1 and 2 — reduction turning a valid CBOR map invalid | 2 | `V-0006`–`V-0007` | 0 / 2 |
| §2.5 rule 2 — the canonical NaN | 1 | `V-0008` | 1 / 0 |
| §2.6 — the three permitted simple values | 3 | `V-0009`–`V-0011` | 3 / 0 |
| §7.1 Table 3 — dCBOR Numeric Encodings | 41 | `V-0012`–`V-0052` | 41 / 0 |
| §7.2 Table 4 — Invalid dCBOR Encodings | 11 | `V-0053`–`V-0063` | 0 / 11 |
| §8.1 — the Tag 1 epoch-time example, both arms | 2 | `V-0064`–`V-0065` | 1 / 1 |
| §8.3 — `1.0 / 0.0`, the `[1, NaN, 3]` array, the canonical NaN restated | 4 | `V-0066`–`V-0069` | 3 / 1 |
| §8.4 — `undefined`, code point 23 | 1 | `V-0070` | 0 / 1 |
| §8.5 — the Tag 2/3 and Tag 80/81/82 escape hatches | 2 | `V-0071`–`V-0072` | 2 / 0 |
| **total** | **72** | | **56 / 16** |

The 41 and 11 row counts were taken independently of the extraction, by
counting the row separators in each table: 41 and 11.

### Restatements

The source prints some byte strings more than once, and each occurrence is
its own vector with its own locator rather than being folded away:

- `00` for a zero: `V-0003` (§2.5 rule 1) and `V-0012` (Table 3 row 1);
  `-0.0` → `00` at `V-0005` and `V-0035`.
- `f97e00`, the canonical NaN, three times: `V-0008` (§2.5 rule 2),
  `V-0052` (Table 3 row 41), `V-0069` (§8.3).

One restatement is **not** given vectors of its own: §8.4 re-expresses
false, true and null as code points 20, 21 and 22, which `V-0009` to
`V-0011` already carry as bytes from §2.6. Only §8.4's fourth code point,
`undefined` (23), is new, and that is `V-0070`. The rule applied throughout
is **one vector per place the source exhibits a value together with an
encoding** — bytes printed, or bytes derivable from a value or code point
the source states.

## Source issues found (recorded, not repaired)

1. **§7.1 Table 3 row 13 — `-127 (-2^8 - 1)`.** -2^8-1 is -257, not -127.
   The decimal and the hex agree (`387e` decodes to -127); only the
   parenthetical is wrong. -127 is -(2^7 - 1). Recorded on `V-0024`.
2. **§7.1 Table 3 row 15 — `-32768 (-2^16)`.** -2^16 is -65536, not -32768.
   Again the decimal and the hex agree (`397fff` decodes to -32768); the
   parenthetical should read -2^15. Recorded on `V-0026`.
3. **§8.3 — `1.0 / 0.0` is not NaN.** "How to represent the result of a
   computation like 1.0 / 0.0 is another perennial question… The [IEEE754]
   floating point standard answers this question with the concept of 'Not a
   Number' (NaN)". Under IEEE 754, 1.0 / 0.0 is +Infinity; 0.0 / 0.0 is the
   NaN-producing division. The illustration is wrong, the rule it
   illustrates is not, and both candidate values are valid dCBOR, so nothing
   normative turns on it. Recorded on `V-0066`, which is why that vector has
   no `hex`.
4. **§7.2 rows 3 and 4 rest on an appendix, not on §2.** `3b8000000000000000`
   and `3bffffffffffffffff` are rejected for being "65-bit negative integer
   value"s, but no narrowing rule in §2 forbids a 65-bit negative *integer*.
   §2.5 rule 1 defines `DCBOR_INT = [-2^63, 2^64-1]` only as the range inside
   which *floating point* values are reduced, and rule 3 constrains floats.
   These bytes are well-formed, preferred-serialization CBOR for a value RFC
   8949 §3.1 permits, so §2.2 does not reach them either. The only normative
   statement that rejects them is §7.2's own "MUST be rejected as invalid by
   a dCBOR-compliant decoder", in an appendix the document introduces as
   "common and edge-case numeric test vectors". Recorded on `V-0055` and
   `V-0056`, whose `violates` cites §7.2 together with the §2.5 range rather
   than claiming a §2 rule that is not there.

Everything else checks out. All 41 Table 3 rows and all 11 Table 4 rows were
decoded by hand against their stated values: **every hex matches its value**,
every encoding consumes exactly its own bytes, and all 62 source-printed hex
strings occur verbatim in the source. The remaining parentheticals (2^8-1,
2^16-1, 2^16, 2^32-1, 2^32, 2^64-1, -2^7, -2^31, -2^63, -2^63-1, -2^64) are
all correct.

Two Table 3 value columns print a shortest round-trip decimal rather than the
exact double, which is conventional and not an error, but matters if the
column is parsed as a literal: row 33's `18446744073709550000.0` is exactly
18446744073709549568, and row 35's `-18446742974197924000.0` is exactly
-18446742974197923840. Noted on `V-0044` and `V-0046`. Row 34's
`18446744073709552000.0` is exactly 2^64, which is the point of the row.

## Rules with no worked example in the source

The source states these and prints nothing to test them with. They are gaps
in the source's own vector set, not gaps in this extraction, and our suite
has to supply its own cases:

- **§2.1 Definite Length Items.** No indefinite-length byte string, text
  string, array or map is printed anywhere in the document. The whole of
  §2.1 — arguably the profile's most basic rejection — has zero coverage in
  Table 4.
- **§2.2 Preferred Serialization**, beyond floats. Table 4 covers
  non-preferred *float* widths (rows 2, 5–8). It prints no non-preferred
  *integer* head, for example `1817` for 23 or `1a00000001` for 1, and no
  non-preferred byte-string, text-string, array or map length head.
- **§2.3 Ordered Map Keys.** No out-of-order map is printed. Figure 1's keys
  are already in bytewise lexicographic order (`0a` < `f94900`), so even the
  one map example in the document does not exercise §2.3.
- **§2.7 Strings.** No non-NFC text string is printed, and no NFC one.
  Nothing in the document names a Unicode sequence at all.
- **§2.6, the unassigned and reserved simple values.** §8.4 observes that the
  other 252 code points are "unassigned" or "reserved" but makes an example
  of none. `e0`–`f3` and the one-byte-argument form `f8xx` are untested.
- **Tag 201** (§3, §6 Table 1). Defined, registered, and never shown. The
  document prints no encoding of it, and no example of the "boundary marker"
  use it describes.
- **The tag-equality rule** (§2.5, last paragraph): "two tagged data items
  are equal in dCBOR only if both their tag numbers and their enclosed CBOR
  data items are equal, and no tagged data item is ever considered
  numerically equal to an untagged data item." No example. The testable
  consequence is that a map holding both `0` and `1(0)` as keys is **not** a
  duplicate-key map, which is exactly the kind of case a careless
  implementation of Figure 1's lesson would get wrong.

## What in the source is deliberately not a vector here

- **§3's CDDL** — `number = int / float` from the RFC 8610 prelude, and the
  `.dcbor` / `.dcborseq` control operators. Grammar, not an encoding; it
  belongs in `../schema/`.
- **§6 Tables 1 and 2** — the IANA registrations for tag 201 and the two
  control operators. Registry rows, with no data item printed.
- **§8 Table 5** — the variability-source-to-rule mapping. Its one
  parenthetical, "(e.g., 0, 0.0, -0.0)", restates §2.5 and is already
  `V-0003` to `V-0005`.
- **§4's implementation list** and the §8.1 block quote of RFC 8949 §3.4.2.
  The quote's content types are recorded in the `notes` of `V-0064`.

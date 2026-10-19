---
record: rfc-9679
kind: examples
title: "rfc-9679 — examples and test vectors"
extracted: "2026-10-18"
reviewed_by: ""
---

# RFC 9679 — examples and test vectors

`vectors.yaml` holds **13 vectors**, in source-locator order with no gaps.
**Five are the source's own printed examples (`V-0008`–`V-0012`); eight are
constructed by this extraction** (`V-0001`–`V-0007` and `V-0013`) for sections
that state a rule and print nothing. Those five printed vectors carry **six**
printed values between them, which is the count in the reproduction table
below — `V-0012` alone carries the reduced encoding, the digest and the
base64url form. *(Corrected by the verify pass: pass 1 wrote "six … seven",
conflating printed values with printed vectors. The enumerated list further
down was always right — it describes eight constructed vectors.)* Every vector
carries `source: printed` or `source: constructed`, and a constructed vector
also carries `constructed_why`. Nothing this pass computed is presented as a
value RFC 9679 printed.

RFC 9679 prints exactly **one** complete thumbprint computation — §6, one EC2
P-256 key — and every other printed value in the document descends from it. The
`kid` in §6's own full example, the `ckt` in §5.6's CWT claims set, the
base64url string in §5.7 and the URI in §5.7 are all the same 32 octets. That
makes the source's test surface very thin for a document whose entire purpose
is a digest, and it is why eight vectors here are ours.

## Reproduction — all six printed values reproduce exactly

Recomputed with an independent CBOR encoder written for this pass (RFC 8949
§4.2.1: shortest argument, definite lengths, map keys sorted by the bytewise
lexicographic order of their encoded forms) plus `hashlib.sha256`. **No CBOR or
COSE library was used**, so a shared library bug cannot hide behind a match.

| printed value | §ref | reproduced |
|---|---|---|
| full example COSE_Key, CBOR encoding | §6 | **yes** — byte-for-byte from the diagnostic notation |
| reduced COSE_Key (required parameters only), CBOR encoding | §6 | **yes** — byte-for-byte, and §4.2.1 sorting gives the same bytes |
| SHA-256 thumbprint | §6 | **yes** — `496bd8af…9da253ec` over those 75 octets |
| `kid` in the §6 full example | §6 | **yes** — equals the thumbprint |
| `ckt` in the §5.6 CWT confirmation claim | §5.6 | **yes** — equals the thumbprint |
| base64url of the thumbprint, and the full `urn:ietf:params:oauth:ckt:` URI | §5.7 | **yes** — 43 characters, unpadded, exact |

**Nothing failed to reproduce.** The document's one worked example is correct in
every printed form.

## Source defect found — §6's full example is not deterministically encoded

`V-0011`. §6 prints the full COSE_Key (with `kid`) and says "The example above
corresponds to the following CBOR encoding". That hex is a faithful encoding of
the diagnostic notation in the order printed — `kty`, `crv`, `x`, `y`, `kid` —
and it is **not** in RFC 8949 §4.2.1 deterministic order, which sorts `kid`
(label 2, encoded `0x02`) into second position:

```
printed    A5 0102 2001 215820 65EDA5…  225820 1E52ED…  025820 496BD8…
§4.2.1     A5 0102 025820 496BD8…  2001 215820 65EDA5…  225820 1E52ED…
```

The second line is this extraction's computation, not the document's.

The defect is **harmless for the thumbprint** — §3 step 2 applies to the step-1
reduction, and `kid` is dropped before step 2 ever runs, which is precisely what
§5.1 is about. It is still a defect: a determinism-dependent specification shows
an implementer a non-deterministic encoding and labels it "the following CBOR
encoding", with nothing in the surrounding text to say that this one is not
subject to step 2. The reduced encoding four paragraphs later *is* §4.2.1-ordered,
so the document switches regimes silently between two adjacent hex blocks.

Not in RFC 9679's errata as of the retrieval date (`2026-09-22`).

## A property of the source worth knowing before writing fixtures

**No thumbprint defined anywhere discriminates RFC 8949 §4.2.1 ordering from
§4.2.3 length-first ordering.** Checked mechanically over every required
parameter set in the document, plus the AKP set RFC 9964 §6 adds:

| key type | §ref | required labels | encoded | §4.2.1 == §4.2.3 |
|---|---|---|---|---|
| OKP | §4.1 | 1, −1, −2 | `01 20 21` | yes |
| EC2 | §4.2 | 1, −1, −2, −3 | `01 20 21 22` | yes |
| RSA | §4.3 | 1, −1, −2 | `01 20 21` | yes |
| Symmetric | §4.4 | 1, −1 | `01 20` | yes |
| HSS-LMS | §4.5 | 1, −1 | `01 20` | yes |
| AKP | §4.6 via RFC 9964 §6 | 1, 3, −1 | `01 03 20` | yes |

Every label lies in −24..23 and so encodes in a single octet, which makes the
length-first tiebreak degenerate. So RFC 9679's dependency on §4.2.1 bites only
on the **value** encodings — minimal-length `bstr` heads and minimal integer
arguments — and never on key order. A thumbprint implementation can get §4.2.1's
map-sorting rule wrong and still produce every correct answer in this document.
That changes with the first COSE Key Type Parameter allocated outside −24..23,
and nothing warns an implementer.

Consequence recorded for the D5 fixture package: **DEC-003 adds no rows to the
determinism table.** See `design-notes.md`.

## The eight constructed vectors, and why each exists

Each one covers a rule RFC 9679 states and does not demonstrate.

1. **`V-0001` — §4.2's compressed-point MUST, as a negative fixture.** The §6
   key with `y` as a sign bit (`false`, `0xF4`) instead of a 32-byte `bstr` —
   the compressed form RFC 9052/9053 also permit. A well-formed COSE_Key, a
   non-conforming thumbprint input, and a different digest for the same
   mathematical key. The conversion §4.2 requires happens **before** any CBOR
   encoding, so RFC 8949 §4.2.1 cannot catch its omission: both encodings are
   perfectly deterministic and they name different keys. The record's cheapest
   negative fixture.
2. **`V-0002` / `V-0003` — the RSA leading-octet ambiguity.** One integer
   modulus, spelled with and without a leading `0x00`. §4.3 types `n` as a
   `bstr` and states no leading-octet rule, so both satisfy every requirement in
   this document and yield different thumbprints. `expect: ambiguous` is
   deliberate: this is a gap in RFC 9679, not a conformance failure against it.
   Note that §4.1 and §4.2 both end "Further details are described in Section
   7.1 of [RFC9053]" while **§4.3, §4.4 and §4.5 cite no defining specification
   at all** — so for RSA, Symmetric and HSS-LMS keys, §7's precondition that "a
   single unambiguous COSE Key representation for that key is defined" is not
   met by anything this document names. **[verify pass]** It *is* met by a
   document RFC 9679 does not name: RFC 8230 §4 requires that numeric RSA key
   parameters be unsigned big-endian and that "The octet sequence MUST utilize
   the minimum number of octets needed to represent the value", which makes
   `V-0003`'s spelling non-conforming under RFC 8230 even though it conforms to
   everything RFC 9679 says. `expect: ambiguous` is therefore scoped to RFC 9679
   and is not a claim about COSE as a whole.
3. **`V-0004` / `V-0005` / `V-0006` — the `alg`-inside-the-digest hazard, as
   hex.** §4.6 delegates the required-parameter set to each key type's defining
   specification. RFC 9964 §6 is the one concrete exercise of that clause, and
   it requires `kty` (1), **`alg` (3)** and `pub` (−1). These three vectors hold
   one byte-identical `pub` under ML-DSA-44, -65 and -87 (`alg` −48, −49, −50)
   and produce three thumbprints that share no prefix. If a `KeyId` is a COSE
   Key Thumbprint over an AKP key, one key under two parameter sets is two
   principals. The `pub` is 32 zero octets and is **not** a valid ML-DSA public
   key; what is being tested is the parameter set, not the cryptography. RFC
   9964's own reproducible AKP thumbprints belong in the `rfc-9964` record.
4. **`V-0007` — the control that proves the set is per-key-type.** The §6 EC2
   key with `alg` (label 3, −7 = ES256) **added**. For EC2, §4.2 does not list
   `alg` as required, so §3 step 1 drops it and the thumbprint is unchanged —
   still `496bd8af…`. Same parameter, same label, same document: excluded for
   EC2, inside the digest for AKP. This vector and `V-0005` are the pair that
   settles "is the parameter set fixed or per-key-type?"
5. **`V-0013` — §7's modulus transformation.** §7 describes an attacker
   supplying modulus `3*N` and prints no key. `V-0013` is `V-0002`'s modulus
   times three. The thumbprint half of the claim is verified — the transformed
   key is a different key to every thumbprint comparison. The "works about 1/3
   of the time" half is **not** verified here: no RSA operation was performed and
   `V-0002`'s modulus is not a real one.

## The vectors that earn their place in a harness

- **`V-0012`** — the conformance anchor. The one complete end-to-end
  computation, reproduced three independent ways (re-encode in printed order;
  re-encode under §4.2.1 sorting; hash). Any implementation that fails this
  fails everything.
- **`V-0007` against `V-0005`** — the one-line regression test for "does our
  KeyId change when the algorithm does?" Run both; if the two digests move
  together, the parameter set is wrong.
- **`V-0001`** — catches a point-compression bug that no CBOR-level determinism
  check can catch.
- **`V-0002` against `V-0003`** — catches a bignum-to-bytes helper that emits a
  sign octet.

## What was checked, and how

- **Every `thumbprint_input_hex` re-hashed** and compared to its
  `thumbprint_hex`: 12 of 13 (the §5.6 claims set has no digest input of its
  own), all consistent.
- **`thumbprint_b64url` re-derived** from the digest octets for both vectors
  that carry one, and the §5.7 URI re-assembled from prefix, `sha-256` and the
  base64url string. Exact.
- **Ids are in source-locator order, contiguous `V-0001`…`V-0013`, unique**, and
  every `pair_with` target resolves to an id defined in the file.
- **Parsed under both readers** — `bin/_record_yaml.load_yaml` and
  `bin/_yaml.parse` return 13 vectors each.

Not checked, because the document supports no such check: no COSE or CBOR
library was run against these vectors, deliberately — the point of hand-encoding
was to be independent of one. No RSA, EC or ML-DSA key in a constructed vector
is a real key, and no signature operation was performed anywhere.

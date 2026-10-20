---
record: rfc-9964
kind: examples
title: "rfc-9964 — examples and test vectors"
extracted: "2026-10-19"
reviewed_by: ""
---

# RFC 9964 — examples and test vectors

**RFC 9964 prints real cryptographic test vectors, and they reproduce.** Six
complete worked examples — Appendix A, Figures 3–8: three JOSE and three COSE,
one per registered ML-DSA parameter set — each carrying a real FIPS 204 public
key of 1312, 1952 or 2592 octets, a real signature of 2420, 3309 or 4627
octets, the exact bytes that were signed, and a `kid` that this extraction
recomputed and matched byte for byte.

That is the opposite of the `rfc-9053` finding, where 43 registered code points
shipped with no cryptographic vector at all. **These are the library's first
post-quantum fixtures.**

12 vectors, in source order, ids quoted because they contain `#`.

| id | locator | source | what |
|---|---|---|---|
| `rfc-9964#V-0001` | §3 Fig. 1 | printed | the truncated ML-DSA-44 JWK — the document's own JOSE rendering |
| `rfc-9964#V-0002` | §3 Fig. 2 | printed | the truncated ML-DSA-44 COSE_Key — **carries a source defect** |
| `rfc-9964#V-0003` | §5 Table 1 | printed | the size table, and why its "Private Key" column is a trap |
| `rfc-9964#V-0004` | A.1 Fig. 3 | printed | ML-DSA-44 JOSE: JWK, JWS, signing input, signature, pub |
| `rfc-9964#V-0005` | A.1 Fig. 4 | printed | ML-DSA-65 JOSE, the same shape |
| `rfc-9964#V-0006` | A.1 Fig. 5 | printed | ML-DSA-87 JOSE, the same shape |
| `rfc-9964#V-0007` | A.2 Fig. 6 | printed | ML-DSA-44 COSE: COSE_Key, tag-18 COSE_Sign1, Sig_structure, signature, pub |
| `rfc-9964#V-0008` | A.2 Fig. 7 | printed | ML-DSA-65 COSE, the same shape |
| `rfc-9964#V-0009` | A.2 Fig. 8 | printed | ML-DSA-87 COSE, the same shape |
| `rfc-9964#V-0010` | §6 applied | **computed** | the Fig. 6 `pub` under `alg` −49 — a different digest from identical bytes |
| `rfc-9964#V-0011` | §6 applied | **computed** | the Fig. 6 `pub` under `alg` −50 — a third |
| `rfc-9964#V-0012` | A.1 vs A.2 | derived | one key, two thumbprints, both printed by the document as its `kid` |

No gaps. `source: printed` means every byte is the document's; `source:
computed` means at least one value is this extraction's and the vector names
every computed field; `source: derived` means every byte is printed but the
assertion is ours. **No computed value anywhere in `vectors.yaml` is presented
as printed.**

## The fixture this record was asked for

**Two different digests from one byte-identical `pub`, with one leg anchored on
a value RFC 9964 itself prints.** Produced, and better than hoped:

| `alg` | thumbprint of the *same* 1312-octet ML-DSA-44 `pub` | provenance |
|---|---|---|
| −48 (ML-DSA-44) | `b8969ab4b37da9f0684e42647eb8a0be8b5b661ebf5d76f0583bf5b8d3a8059a` | **printed by RFC 9964** as the `kid` of Figure 6 |
| −49 (ML-DSA-65) | `f507c41723160cdec5f245a8f6b6c0cd8144f1febae70df0c24fa4fcf187315d` | computed by this extraction |
| −50 (ML-DSA-87) | `de68d5ecb9465cd4c06dd1b246a20f50d0b928bdff52433e53e4d387e128f62b` | computed by this extraction |

The three inputs are 1322 octets each and differ in **exactly one octet** —
offset 5, which holds `2f`, `30`, `31`. They share no digest prefix.

> **[corrected by the verify pass, 2026-10-20.]** This previously read "differ
> in **exactly two octets** — `382f`, `3830`, `3831` at offset 4". The
> two-octet *span* at offsets 4–5 does read `382f` / `3830` / `3831`, but
> offset 4 is `0x38` in all three inputs and only offset 5 differs: −48, −49
> and −50 all encode as major type 1 with a one-byte argument, so they share
> the head `0x38` and differ only in the argument byte (`2f`, `30`, `31`).
> Re-derived: the three 1322-octet inputs begin `a3010703382f2059`,
> `a301070338302059`, `a301070338312059`. The correction makes the finding
> *stronger* — a **single octet** of algorithm identifier relocates the whole
> digest.

This is the fixture `rfc-9679`'s `V-0004`/`V-0005`/`V-0006` could not build.
Those used 32 zero octets as a stand-in `pub`, so all three legs of their
triple were constructed and nothing anchored the method. Here the `alg` −48 leg
**is the document's own printed `kid`** and reproduces exactly, which validates
the encoder and the parameter set *before* the other two legs are computed with
it. Checked: neither computed digest occurs anywhere in `.cache/rfc-9964.txt`.

`V-0010`'s `computed_why` records what the vector does *not* claim: a
1312-octet `pub` is the wrong length for ML-DSA-65, so this is not an assertion
that the key is usable at that parameter set. §6 types `alg` as a bare `int`
with nothing tying it to the key material, and §6 opens by saying AKP suits
"algorithms other than ML-DSA", so the thumbprint is well-formed and computable
before any such check runs. **The identity is computed first. That is the
hazard.**

## The second finding: the same key has two thumbprints

`V-0012`. For each algorithm the JOSE and COSE halves of Appendix A carry a
**byte-identical** `pub` — measured — and §6 defines a required set for each of
RFC 7638 and RFC 9679 over the same three parameters. The digests are
unrelated:

| algorithm | JWK Thumbprint (RFC 7638) | COSE Key Thumbprint (RFC 9679) |
|---|---|---|
| ML-DSA-44 | `4f8c65ef44bb…8d06bbaa` | `b8969ab4b37d…d3a8059a` |
| ML-DSA-65 | `4ae8aedbda9b…fd0a5d53` | `b788acf242f1…ab80cc02` |
| ML-DSA-87 | `b519f524d224…33ede575` | `d9bc439f97bd…166cb4fa` |

Shared prefix: zero octets in all three. All six digests are printed by this
document as that key's `kid`. Nothing here is computed — what is ours is the
assertion that these are six digests of *three* keys.

## Verification performed

A CBOR encoder/decoder written for this pass (RFC 8949 §4.2.1: shortest
argument, definite lengths, map keys sorted by the bytewise order of their
encoded forms) plus `hashlib.sha256` and `base64.urlsafe_b64encode`. **No CBOR,
COSE, JOSE or JWT library was used**, so a shared library bug cannot hide here.

1. **All three COSE Key Thumbprints reproduce.** `sha256(enc({1:7, 3:alg,
   -1:pub}))` equals the printed `kid` of Figures 6, 7 and 8. Inputs 1322, 1962
   and 2602 octets.
2. **All three JWK Thumbprints reproduce.** `sha256` of
   `{"alg":…,"kty":"AKP","pub":…}` in §6's stated order, base64url unpadded,
   equals the printed `kid` of Figures 3, 4 and 5. Inputs 1790, 2643 and 3496
   octets.
3. **Structural consistency, every figure.** `raw_public_key` equals the key's
   `pub`; `raw_signature` equals the JWS third part / the COSE_Sign1 fourth
   element; `raw_to_be_signed` equals `"header.payload"` as ASCII (JOSE, 171
   octets) and decodes to `["Signature1", bstr(39), bstr(0), bstr(29)]` (COSE,
   85 octets) with the same 39 protected octets the COSE_Sign1 carries.
4. **Every long value re-found in the source** with the RFC's line breaks
   removed, so no value in `vectors.yaml` is a transcription.
5. **The whole file round-trips.** `vectors.yaml` was re-read with the
   library's own `_record_yaml` and every digest recomputed *from what the file
   stores* rather than from the extraction's memory. 121 assertions, zero
   failures.
6. **Both YAML readers agree**: 12 vectors under `_record_yaml.load_yaml` and
   under `_yaml.parse`.

### The signature gap — closed by the verify pass, 2026-10-20

Pass 1 recorded that it could not verify the signatures, and said so on every
vector: no FIPS 204 implementation was available to it. **That gap is now
closed.** ML-DSA `KeyGen_internal` and `Verify_internal` were implemented from
FIPS 204 (August 2024) in pure Python over `hashlib`'s SHAKE128/256 — NTT with
ζ = 1753, `ExpandA`/`ExpandS` rejection sampling, `Power2Round`,
`SimpleBitPack`, `Decompose`, `UseHint`, `SampleInBall`, `sigDecode`.

**It was gated against NIST's own known answers before being pointed at this
document.** That order matters: a hand-rolled lattice implementation
disagreeing with an RFC is indistinguishable from a defect in the RFC, which is
the worst outcome available — reporting our own bug as the source's.

| gate | vectors | result |
|---|---|---|
| `ML-DSA-keyGen-FIPS204` (ACVP) | 75 (25 per parameter set) | **75/75 public keys reproduce exactly** |
| `ML-DSA-sigVer-FIPS204` (ACVP) | 90, of which **72 expected-reject** | **90/90 verdicts agree** |

The reject majority is the point: a verifier that always returned true would
score 18/90 on gate 2.

Both gates passed, and only then:

7. **All six printed public keys re-derive from the all-zeros seed.**
   `KeyGen_internal(0^32)` reproduces the 1312 / 1952 / 2592-octet `pub` of
   Figures 3–8 byte for byte. Pass 1 could only infer the seed-to-key relation
   from the two halves of Appendix A agreeing; it is now measured against
   FIPS 204 itself.
8. **All six printed signatures verify cryptographically.**
   `ML-DSA.Verify(pk, M, σ, ctx="")` accepts all six, with
   `M' = 0x00 ‖ 0x00 ‖ M` per FIPS 204 Algorithm 3 and the empty `ctx` that §5
   requires (`R-0034`) — which also makes `R-0034` the one requirement in this
   record whose *satisfaction* is now demonstrated rather than asserted.
   Flipping a single bit of each message is rejected, as a control.

`signature_verified: verified` now says so on all six vectors that carry a
signature. The six that carry none keep `n/a`.

The internal consistency check pass 1 relied on also holds: for each algorithm
the JOSE and COSE halves carry the same `pub` byte for byte — and the derivation
above now explains why, since both come from the same all-zeros seed.

## Source findings

### Figure 2's `pub` prefix does not match the key it illustrates

§3 line 147 prints:

```
      / pub  / -1: h'ba71f9f64e11baeb589...3830546b9dd8db0d',
```

The same key's `pub` in Appendix A — Figure 3's base64url and Figure 6's hex,
which agree with each other — begins `ba71f9f64e11baeb58fa…`. The first 18 hex
digits are identical; **the 19th is `9` in Figure 2 and `f` in the key.** The
suffix matches. `kid` and `priv` match at both ends, and Figure 1, the JWK
rendering of the same key in the same section, has no defect.

The prefix is also 19 hex digits, an odd number, so it is not a byte-aligned
cut — but the cut length is a display choice, whereas a differing character is
not. **Reported, not repaired** (`docs/extraction.md`). Nothing downstream
depends on it: the value is illustrative and truncated, the complete key is in
Appendix A, and §2 already warns that "Some examples in this specification are
truncated using "..." for readability."

Located mechanically, by comparing against the reassembled Appendix A JSON, not
by eye.

> **[verify pass, 2026-10-20] The defect is now confirmed against FIPS 204
> itself, not just against Appendix A.** Pass 1 could show only that Figure 2
> disagrees with the *other two renderings in the same document* — which,
> alone, leaves open the possibility that Figure 2 is right and Appendix A is
> wrong twice. `KeyGen_internal(0^32)` for ML-DSA-44 produces a `pub` beginning
> `ba71f9f64e11baeb58fa`, so the 19th hex digit is **`f`** in the real key and
> Figure 2's `9` is the error. Appendix A is correct; Figure 2 alone is wrong.

### The printed `COSE_Key` bytes are not in deterministic map order

All three Appendix A.2 `key` values encode the map as `kid`(2), `kty`(1),
`alg`(3), `pub`(−1), `priv`(−2) — label 2 before label 1 — where RFC 8949
§4.2.1 would give 1, 2, 3, −1, −2. The §3 Figure 2 diagnostic form has the same
order, so it is the document's consistent house style, not a diagram artefact.

**It is not a conformance defect.** §4.2.1 binds the *thumbprint input* (RFC
9679 §3 step 2), not the COSE_Key, and neither RFC 9964 nor RFC 9052 asks a
COSE_Key to be deterministically encoded.

**But here is the near-trap, and it was checked rather than assumed.** An
implementation that derives the thumbprint input by walking the printed
COSE_Key, keeping labels 1, 3 and −1 in the order it met them, and rewriting
only the map head gets exactly the right bytes — because the printed order is
2, 1, 3, −1, −2, and dropping 2 and −2 leaves 1, 3, −1, which *is* §4.2.1
order. Measured for all three figures: same bytes, same digest.

**That is an accident of this key shape, not a rule.** It holds only because
`kid` is the single out-of-order label and is one of the two that get dropped.
A key whose out-of-order label survived the subsetting would break it, and
break it silently — the digest would simply be a different 32 octets. Noted
because "it worked on the RFC's examples" is exactly the evidence that would
make an implementer skip the re-sort.

### §6 names no hash function

"The COSE Key Thumbprint is produced according to the process described in
Section 3 of [RFC9679]", and RFC 9679 §3 step 3 takes the hash function as a
*parameter*. The string `SHA-256` does not occur in RFC 9964 at all — checked
mechanically, zero occurrences. SHA-256 is established here by the Appendix A
`kid` values reproducing under it, which is an example rather than a normative
statement. Recorded in `../schema/akp-parameters.derived.json` as
`hash_function_named_by_this_document: null`.

### The two halves of Appendix A are not a matched pair

The JOSE examples sign `"It’s a dangerous business, Frodo, going out your
door."` (56 octets — 54 characters, because U+2019 encodes as `e2 80 99`); the
COSE examples sign `"hello post quantum signatures"` (29 octets).

> **[correction] 2026-10-20, cross-check pass.** The record carried this one
> 56-octet payload in **three different spellings**, and only one of them was
> right. `messages.yaml` had the character, U+2019. `vectors.yaml`'s three
> `jws_payload_utf8` fields had the YAML escape `"It’s …"` — and **neither
> of the library's two YAML readers decodes a `\u` + four-hex-digit escape** (`bin/_record_yaml.py`
> handles `\n`, `\t`, `\"`, `\\` and no more), so the fixture read back as a
> 59-character string with a literal backslash, not as the payload. This
> sentence and `design-notes.md`'s defect 5 quoted it with an **ASCII**
> apostrophe, which is 54 octets — in the same breath as asserting 56. All five
> now carry the character, so the quotation and `jws_payload_hex` agree under
> both readers. `jws_payload_hex` was correct throughout and remains the
> authority. Found by sweeping every artifact that states a value another
> artifact also states, which is how this class of defect surfaces. Same keys,
different payloads, so the signatures cannot be compared across the two halves
and a JOSE↔COSE round-trip fixture cannot be built from this document. Only the
keys are shared.

## What is carried in full, and what is not

Full and unaltered: every public key (hex and base64url), every signature, every
`COSE_Key`, every `COSE_Sign1`, every `Sig_structure`, every JWS, every `kid`,
every `priv` seed. The RFC hard-wraps JSON string literals at 72 columns with
no continuation marker; those line breaks are removed and nothing else is
altered.

Elided, and marked in place with the character count removed: the `key_diag`
and `sign1_diag` CBOR diagnostic strings, which run to thousands of characters
and are a human rendering of bytes carried here in full as `key_hex` and
`sign1_hex`. Nothing testable is lost — the hex is the authority, and
`vectors.yaml` says so.

> **[correction] 2026-10-20, cross-check pass.** The six counts were each **one
> too high** — 2632 / 4839, 3912 / 6617, 5192 / 9253 where the measured counts
> are 2631 / 4838, 3911 / 6616, 5191 / 9252 — and are corrected in
> `vectors.yaml`. In all six the kept prefix is the printed diagnostic's first
> **91** characters and the kept suffix its last **70**, so the marker replaces
> `len(printed) − 161`: for V-0007's `key_diag`, 2792 − 161 = **2631**. The old
> numbers describe a cut one character longer than the file exhibits. Stating
> the count removed is the whole content of this convention, so off-by-one
> falsified it. Also recorded there: the space before each marker's retained
> suffix is this extraction's separator, not a source character, and because the
> elided span ends inside the last entry's key (`-2`), `key_diagnostic_elided`
> is **not** parseable as CBOR diagnostic notation. `key_hex` is the authority.

The thumbprint inputs are carried as `thumbprint_input_head_hex` plus a
statement that the full input is that head concatenated with `pub_hex`, which
is already in the same vector. Verified as an identity rather than asserted.

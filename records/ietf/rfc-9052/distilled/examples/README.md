---
record: rfc-9052
kind: examples
title: "rfc-9052 — examples and test vectors"
extracted: "2026-09-30"
reviewed_by: ""
---

# Examples and test vectors

## What the source contains

RFC 9052 **does** carry examples, contrary to the common assumption that the
COSE examples were all moved out of the structures document. Appendix C
("Examples") and Appendix B together hold **17 complete, tagged COSE messages**
in the extended CBOR diagnostic notation of RFC 8610, each preceded by a
declared binary size:

| locator | vector | message |
|---|---|---|
| §B | V-0001 | triple-layer `COSE_Encrypt` (decomposed ECDH-ES+A128KW), 183 bytes |
| §C.1.1–C.1.3 | V-0002–V-0004 | `COSE_Sign`: single signer, multiple signers, `crit` marker |
| §C.2.1 | V-0005 | `COSE_Sign1`, ECDSA w/ SHA-256 |
| §C.3.1–C.3.3 | V-0006–V-0008 | `COSE_Encrypt`: direct ECDH, direct+KDF, external AAD |
| §C.4.1–C.4.2 | V-0009–V-0010 | `COSE_Encrypt0`: simple, partial IV |
| §C.5.1–C.5.4 | V-0011–V-0014 | `COSE_Mac`: direct, ECDH direct, wrapped, multi-recipient |
| §C.6.1 | V-0015 | `COSE_Mac0`, shared-secret direct MAC |
| §C.7.1–C.7.2 | V-0016–V-0017 | `COSE_KeySet`: 4 public keys; 7 private/symmetric keys |

Crucially, §C.7 supplies the **full public and private key material** —
including the `d` values and the raw shared secrets — for every preceding
example. Six further fragments (V-0018–V-0023) capture the partial material in
the body: the `h'a0'` zero-length-protected-bucket rule (§3), the minimal-length
integer encoding assertion (§9), the `Sig_structure` / `Enc_structure` /
`MAC_structure` CDDL shapes (§4.4, §5.3, §6.3), and the Context IV prefix for
the partial-IV example (§C.4.2).

## What the source does not contain

- **No hex dumps.** Every example is diagnostic notation plus a byte count.
  The `hex:` field is empty on all 23 records for this reason.
- **No populated `Sig_structure`, `Enc_structure` or `MAC_structure` instance,
  and no `ToBeSigned` / `ToBeMaced` / AAD byte string anywhere** — verified by
  exhaustive search. Only the CDDL shapes and the prose procedures are given.
  This is the single largest gap for a test harness: the signing-input
  construction, which is where implementations most often diverge, **cannot be
  tested from this document alone**. Not even §C.3.3, the one example that
  supplies an external AAD (`h'0011bbcc22dd44ee55ff660077'`), shows the
  resulting `Enc_structure`.
- **No algorithm definitions.** ECDSA, HMAC, AES-GCM, AES-CCM, AES-KW, HKDF and
  the ECDH variants are all defined in RFC 9053, so no fixture here supports
  cryptographic verification on its own.
- **No KDF context byte strings** for §C.3.2 or §C.5.2 (the context fields are
  given only as prose), and no derived keys or intermediate values.
- **No failure-test cases.** Every example here is a positive one.

## The gap list — what no fixture here exercises

This is the most useful output of the cross-check pass for whoever writes the
test suite. All 17 fixtures were parsed, encoded and validated against the
`cose.cddl` subset and against `messages.yaml` (element count, element order,
and which element is a `bstr`): **zero structural findings, all 17 sizes equal
the RFC's declared byte count, all 17 `derived_hex` values reproduce.** What
follows is therefore not a list of failures; it is the list of things the
17 positive examples cannot reach.

**Structures in `messages.yaml` that no fixture exercises (8 of 25).**
`COSE_Messages` (a choice rule, so it has no fields of its own); `Sig_structure`,
`ToBeSigned`; `Enc_structure`, `AAD`; `MAC_structure`, `ToBeMaced`; and `CBOR
encoding restrictions` as §9 scopes it. The other 17 structures are all
exercised, though not every field of each. Every structure in that list is an
*internal* type —
§1.4's `Internal_Types`, "used for security computations but are not emitted for
transport" — so no transported example can ever contain one. That is the shape
of the gap, not an oversight in the extraction.

**Fields no fixture populates (25 of 74).** Besides every field of the four
internal structures above: `COSE_message_identification`'s "by context",
`cose-type` media type parameter and CoAP Content-Format rows (all 15 tagged
fixtures use the CBOR tag, method 2, and nothing else); `Generic_Headers`
`content type` (label 3 appears in no example); and `COSE_Key`'s `alg`,
`key_ops` and `Base IV` (labels 3, 4 and 5 appear in neither key set, even
though §C.4.2 needs a Base IV to reconstruct its IV).

**`testable: yes` requirements no fixture covers (23 of 85).** Derived
mechanically: a requirement counts as covered when a fixture populates at least
one `messages.yaml` field whose `constrained_by` names it.

| ids | why no fixture reaches them |
|---|---|
| `R-0034`–`R-0042`, `R-0044` | the whole §4.4 `Sig_structure` / `ToBeSigned` construction |
| `R-0046`, `R-0049`, `R-0051`, `R-0052` | the §5.3 `AAD`, the §5.4 AE checks, the §6.3 `ToBeMaced` |
| `R-0089`, `R-0090` | §9's definite lengths and minimum-length arguments — the fixtures *do* round-trip minimally, but §9 scopes the rule to the three internal structures, and none is populated |
| `R-0004`, `R-0005` | the `cose-type` media type parameter, which needs a media type, not a CBOR object |
| `R-0024`, `R-0025` | `content type`, absent from every example |
| `R-0063`, `R-0064`, `R-0095` | `COSE_Key`'s `alg`, absent from both key sets |

Two cautions on reading that table. First, coverage here means **a fixture
populates a field the requirement constrains** — necessary, not sufficient. No
fixture in this record supports cryptographic verification at all, because the
algorithms are in RFC 9053, so a requirement such as `R-0066` ("content MUST NOT
be used if the decryption does not validate") counts as covered structurally and
is still untestable here. Second, the negative requirements — the `MUST NOT`s
about duplicate labels, non-`int`/non-`tstr` labels, `IV` and `Partial IV`
together — need *failure* fixtures, and **RFC 9052 contains none**; every
example in it is positive.

**The signing input cannot be tested from this source. Full stop.** There is no
populated `Sig_structure` and no `ToBeSigned` byte string anywhere in RFC 9052 —
and no populated `Enc_structure`/`AAD` or `MAC_structure`/`ToBeMaced` either.
Pass 2 searched exhaustively to falsify that and could not. So the one place
implementations most often diverge — the construction of the bytes that get
signed — has **no vector in this document**. Pull the cose-wg Examples JSON for
it; do not synthesise one and call it a fixture.

## Where the real vectors live

The Appendix C introduction defers explicitly to `[GitHub-Examples]`
(§13.2: "GitHub Examples of COSE", commit 3221310, 3 June 2020,
<https://github.com/cose-wg/Examples>), which holds "not only the examples
presented in this document, but a more complete set of testing examples as
well" — each a JSON file carrying the inputs, the intermediate debugging
values, and the output **both as a hex dump and in diagnostic notation**.
Failure-testing cases are marked as such in those JSON files, and the source
states that corrections are made there rather than in the RFC. Algorithm
specifics are in RFC 9053.

## Two discrepancies in the source, recorded deliberately

- **§C.5.4** prose says "HMAC w/ SHA-256, **128-bit** key", but the protected
  bucket carries `alg` 5, annotated in the same example as `HMAC 256//256`.
  Treat the encoded `alg` value as authoritative.
- **§C.3.3** writes the recipient protected bucket as a literal byte string
  `h'a101381f'` followed by a comment using backslash delimiters, instead of the
  `<< { ... } >>` embedded-map form every other example uses. The encoded bytes
  are unaffected (`a101381f` decodes to `{1: -32}`), but a diagnostic-notation
  parser must tolerate both spellings.

## How a harness should treat this today

1. **Treat `fixtures/*.diag` as authoritative**, not `derived_hex`. Each file is
   the example exactly as the source prints it, with two whitespace-only
   normalisations: hex literals that the RFC text formatter hard-wrapped across
   lines were rejoined, and the 3-space block indent was removed. No token was
   altered, added or reordered — this is checked byte-for-byte against the
   cached source, whitespace-insensitively.
2. **Canonical bytes come from `cbor-diag`**, as the source directs:
   `gem install cbor-diag` then `diag2cbor.rb < fixtures/V-0002-….diag`.
3. **`derived_hex` is a convenience and is NOT in the source.** It was produced
   by encoding each `.diag` file to deterministic CBOR (RFC 8949 §4.2.1, source
   map order preserved) and corroborated two independent ways: the encoded
   length equals the size the RFC declares, for all 17 messages; and all 22
   inline `protected h'…'` annotations in the source reproduce byte for byte.
   Both checks pass with zero mismatches. Re-derive with `diag2cbor.rb` before
   relying on it for anything load-bearing.
4. **Scope the assertions to `expect`.** `decode` means the fixture must decode
   to this structure and re-encode to `declared_size_bytes`; `encode` is a
   byte-level assertion the source states outright; `informative` is a shape or
   note with no executable assertion. Use these for structural, round-trip and
   canonical-encoding tests only.
5. **For signature/MAC/AEAD verification, and for any `Sig_structure`-level
   test, pull the cose-wg Examples JSON** and pair it with RFC 9053. Do not
   synthesise the missing intermediates locally: §C.4.2's Context IV, for one,
   is given only as a 10-byte prefix, and the IV length comes from RFC 9053, so
   the message IV is not reconstructible from this document.

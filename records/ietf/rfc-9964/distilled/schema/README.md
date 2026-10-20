---
record: rfc-9964
kind: schema
title: "rfc-9964 — schemas"
extracted: "2026-10-19"
reviewed_by: ""
---

# RFC 9964 — schemas

**RFC 9964 ships no formal grammar.** No CDDL, no ABNF, no ASN.1, no JSON
Schema, not one production. Checked mechanically against
`.cache/rfc-9964.txt`: `CDDL` occurs **zero** times, `ABNF` zero, `ASN.1`
zero, `JSON Schema` zero, and `bstr` occurs **three** times — two IANA
"CBOR Type: bstr" rows (§8.1.3.1, §8.1.3.2) and one bullet of §6. Its
structural content is prose (§3, §4, §5), one size table (§5 Table 1), two
truncated examples (Figures 1 and 2), two bullet lists of required parameters
(§6) and twelve IANA registration templates (§8.1).

So one file here is verbatim and it is not a grammar; everything formal is the
library's own and carries `.derived.` (`docs/extraction.md`, *Derived vs
verbatim*). This is the RFC 8785 / RFC 9679 case, not the RFC 9804 case.

| file | verbatim or derived | what it covers | what it deliberately does **not** constrain |
|---|---|---|---|
| `akp-source-renderings.txt` | **verbatim** | the four places the document renders a structure itself: Figure 1 (truncated ML-DSA-44 JWK), Figure 2 (truncated ML-DSA-44 COSE_Key), Table 1 (key and signature sizes with its own note), and §6's two required-parameter bullet lists. Byte-for-byte, the RFC's three-space margin included; each excerpt carries its source line range and its own sha256 | **nothing — it constrains nothing at all.** It is two examples, a table and two lists. It is in this directory because it is what the source offers in place of a grammar, and it must never be cited as one |
| `akp-key.derived.cddl` | derived | the AKP `COSE_Key`: `kty` 1, `alg` 3, `pub` −1, `priv` −2, public and private forms, plus six per-algorithm rules carrying Table 1's `pub` sizes and §4's 32-byte seed. 23 rules | map order (CDDL cannot); whether `pub` and `priv` agree (§7.4); the internals of `pub` (FIPS 204 §5.3 / pkEncode); the expanded private key (§4 excludes it); `ctx` (no label exists, so §5's MUST is unobservable from the wire); HashML-DSA (no code point) |
| `akp-thumbprint-input.derived.cddl` | derived | **the file the record exists for.** §6's two required-parameter sets as closed structures: the COSE Key Thumbprint input `{1 => 7, 3 => int, -1 => bstr}` with the three ML-DSA instances, and the JWK Thumbprint input with its `alg`, `kty`, `pub` order. 6 rules | byte order and encoding determinism — the properties that actually define a thumbprint input (RFC 8949 §4.2.1, required by RFC 9679 §3 step 2, inexpressible in CDDL); the hash function (**§6 names none**); whether `pub` is a valid key; the output encoding; and that the two inputs agree (**they do not, and both digests are printed as `kid`**) |
| `ml-dsa-cose-sign1.derived.cddl` | derived | the signature side as the Appendix A.2 figures instantiate it: protected header `{1 => alg, ? 4 => kid}`, the four-element `COSE_Sign1`, the `#6.18`-tagged form, the `Sig_structure`, and the JWS protected header. 16 rules | that the signature verifies; `ctx`; whether `kid` is a thumbprint (§6 only illustrates); tag presence (RFC 9052 permits either form, RFC 9964 exhibits only the tagged one) |
| `akp-parameters.derived.json` | derived | the registry data and the **measured byte layouts**: code points with their CBOR encodings, the six registries §8.1 touches, per-parameter thumbprint membership, and for each algorithm the thumbprint-input length, the octet-by-octet head before `pub`, the SHA-256, and whether this extraction reproduced the printed `kid`. `$id: urn:library:rfc-9964:akp-parameters.derived` | nothing structural — it is data, not a validator. `hash_function_named_by_this_document` is `null` on purpose |
| `akp-key.derived.schema.json` | derived | JSON Schema 2020-12 over the **fixture rendering**: the JWK form from §3/§4/§5 with per-algorithm base64url lengths, the COSE_Key fixture form with per-algorithm hex lengths, the bare thumbprint-input fixture (`additionalProperties: false`, which is §6's closed set), and a signature fixture by length. `$id: urn:library:rfc-9964:akp-key.derived` | the same five things the CDDL does not, listed in the file's own `$comment-does-not-constrain` |

The CDDL is the authoritative structural rendering; the JSON Schema exists
because our fixtures are carried as JSON, not CBOR. Where they could disagree,
the CDDL is right.

## The one thing to read if you read nothing else

`alg` (label 3) is **inside** the AKP COSE Key Thumbprint. For every key type
RFC 9679 §4.1–§4.5 defines it is outside. RFC 9964 §3 makes it REQUIRED — "The
alg JSON Web Key (JWK) parameter or COSE Key Common parameter is REQUIRED for
all AKP keys" — and §6 then states the thumbprint set outright, so no inference
is needed:

> *  "kty" (label: 1, data type: int, value: 7)
>
> *  "alg" (label: 3, data type: int, value: int)
>
> *  "pub" (label: -1, value: bstr)

Consequence, measured on the document's own 1312-byte ML-DSA-44 public key:
three digests from byte-identical `pub`, one of them the value RFC 9964 itself
prints. `../examples/vectors.yaml` V-0007, V-0010, V-0011; the design
consequence is in `../design-notes.md`.

## What §6 does not say, and nobody can supply

**No hash function.** §6 says "The COSE Key Thumbprint is produced according to
the process described in Section 3 of [RFC9679]" and RFC 9679 §3 step 3 takes
the hash function as a *parameter*. RFC 9964 never writes "SHA-256" anywhere.
The Appendix A `kid` values reproduce under SHA-256 and under nothing else we
tried, so SHA-256 is established by the examples rather than by the normative
text. Recorded in `akp-parameters.derived.json` as
`hash_function_named_by_this_document: null`.

## Verification performed in pass 1

Mechanical, not by reading. A CBOR encoder/decoder written for this pass
(RFC 8949 §4.2.1: shortest argument, definite lengths, map keys sorted by the
bytewise order of their encoded forms) plus `hashlib.sha256`. No CBOR, COSE or
JOSE library was used, so a shared library bug cannot hide here.

1. **All three COSE Key Thumbprints reproduce.** `sha256(enc({1:7, 3:alg,
   -1:pub}))` equals the `kid` printed in Figures 6, 7 and 8 exactly —
   `b8969ab4…d3a8059a`, `b788acf2…ab80cc02`, `d9bc439f…166cb4fa`. Inputs are
   1322, 1962 and 2602 bytes. This is independent confirmation of §6's
   parameter set against the document's own values, over real FIPS 204 keys.
2. **All three JWK Thumbprints reproduce.** `sha256` of
   `{"alg":"…","kty":"AKP","pub":"…"}` with members in §6's stated lexicographic
   order, base64url-encoded unpadded, equals the `kid` printed in Figures 3, 4
   and 5 exactly. Inputs are 1790, 2643 and 3496 bytes.
3. **Every length claim in both schemas was measured, not computed from Table
   1.** `pub` 1312/1952/2592 bytes = 1750/2603/3456 base64url chars =
   2624/3904/5184 hex chars; signatures 2420/3309/4627 bytes; `priv` 32 bytes =
   43 base64url chars. All six figures agree with Table 1.
4. **CDDL rule closure.** 45 rules across three files (23 + 6 + 16); no
   duplicate definition **within any one file**, no reference that is neither
   defined locally nor an RFC 8610 Appendix D prelude name, no name colliding
   with a prelude name (the RFC 8785 defect), braces, brackets and parens
   balanced. Prelude names used: `int`, `bstr`, `tstr`, `nil`, `any`.

   > **[clarified by the verify pass, 2026-10-20.]** This said "no duplicate
   > definition" without qualification, which a reader checking it across the
   > whole directory would falsify: 45 is the **sum of per-file counts** and
   > there are **36 distinct rule names**, because **nine** are defined in both
   > `akp-key.derived.cddl` and `ml-dsa-cose-sign1.derived.cddl` —
   > `ml-dsa-alg`, `ml-dsa-44`, `ml-dsa-65`, `ml-dsa-87`, `label`, `values`,
   > and the three `ML-DSA-nn-Signature` rules. That repetition is **required,
   > not sloppy**: a CDDL file must define every rule it references, so each
   > file standing alone has to carry them. Re-derived: all nine pairs are
   > **byte-identical** after comment and whitespace normalisation — zero
   > divergent definitions — and no file duplicates a rule internally. Also
   > re-checked: the seven bare names in `ml-dsa-cose-sign1.derived.cddl` that
   > look like dangling references (`protected`, `unprotected`, `payload`,
   > `signature`, `context`, `body_protected`, `external_aad`) are **member
   > keys of array groups**, written `name: type`, not rule references — RFC
   > 9052's own field names, carried so the array positions are readable.
5. **JSON Schema integrity.** Both `.json` files parse; six internal `$ref`s all
   resolve; both `$id`s are `urn:library:rfc-9964:*`.
6. **The verbatim excerpts re-cut.** Each excerpt in
   `akp-source-renderings.txt` was diffed against `sed -n 'a,bp'` on the cached
   source and is byte-identical.

## Two source findings this directory records

**Figure 2's `pub` prefix does not match the key it illustrates.** §3 line 147
prints `/ pub  / -1: h'ba71f9f64e11baeb589...3830546b9dd8db0d'`. The same key's
`pub` in Appendix A begins `ba71f9f64e11baeb58fa…` — the 19th hex digit is `9`
in Figure 2 and `f` in the key. The suffix matches, and `kid` and `priv` match
at both ends. Reported, not repaired; detail in `../examples/README.md`.

**The printed `COSE_Key` bytes are not in deterministic map order.** All three
Appendix A.2 `key` values encode the map as `kid`(2), `kty`(1), `alg`(3),
`pub`(−1), `priv`(−2) — label 2 before label 1 — where RFC 8949 §4.2.1 would
give 1, 2, 3, −1, −2. Nothing requires otherwise: §4.2.1 binds the *thumbprint
input*, not the key. It is recorded because the thumbprint input is derived from
this map, and the subsetting happens to come out right only because `kid` is the
single out-of-order label and is one of the two that get dropped. Measured in
`../examples/README.md`.

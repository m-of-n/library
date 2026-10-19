---
record: rfc-9679
kind: schema
title: "rfc-9679 — schemas"
extracted: "2026-10-18"
reviewed_by: ""
---

# RFC 9679 — schemas

**Every file here is derived. RFC 9679 ships no formal grammar of any kind** —
no CDDL, no ABNF, no JSON Schema, no ASN.1, not one production. Its structural
content is a three-step numbered procedure in prose (§3) and five bullet lists
of required parameters (§4.1–4.5), cross-checked by exactly one worked encoding
(§6). There is therefore nothing to copy verbatim into this directory, and
every filename carries `.derived.` accordingly (`docs/extraction.md`, *Derived
vs verbatim*). This is the RFC 8785 case, not the RFC 9804 case.

| file | what it is | derived from | start / shape |
|---|---|---|---|
| `cose-key-thumbprint-input.derived.cddl` | CDDL for the structure that is **hashed** — one rule per key type, maps closed so that "only the required parameters" is expressed, not just described | §3 step 1, §4.1–4.5; cross-checked against the §6 bytes | `COSE-Key-Thumbprint-Input`, 6 rules |
| `thumbprint-computation.derived.json` | the §3 **computation** as data: ordered steps with their requirement ids, the per-key-type label table with encoded label bytes and order index, the excluded labels, the hash-function rules, the §5.7 URI form, the §5.6/§8 `ckt` confirmation member, and the §6 worked example with its digest | §3, §4, §5.2, §5.6, §5.7, §6, §8 | JSON object, `$id: urn:library:rfc-9679:thumbprint-computation.derived` |
| `thumbprint-input.derived.schema.json` | JSON Schema over the **fixture rendering** of a thumbprint input (key type, parameters by decimal label, the encoded bytes, H, the digest). Its five `oneOf` branches are §4.1–4.5 made machine-checkable: each fixes the required labels and sets `additionalProperties: false`, which is §4's exclusion rule | §4.1–4.5, §5.7, §6 | JSON Schema 2020-12, `$id: urn:library:rfc-9679:thumbprint-input.derived` |

The CDDL is the authoritative structural rendering; the JSON Schema exists
because our tests carry fixtures as JSON, not CBOR. Where they could disagree,
the CDDL is right.

## What the CDDL deliberately does not say

CDDL describes a map as an unordered set of entries, and **this input is
defined by its byte order**. Two rules therefore live in
`thumbprint-computation.derived.json` and not in the grammar:

1. **Entry order.** RFC 8949 §4.2.1 sorts map keys by the bytewise
   lexicographic order of their encoded forms, which puts `kty` (label 1,
   encoded `0x01`) before every negative label and orders the rest `-1`
   (`0x20`), `-2` (`0x21`), `-3` (`0x22`).
2. **Encoding determinism.** Preferred serialization of every head, definite
   lengths only. Also RFC 8949 §4.2.1.

Validating a byte string against the CDDL alone therefore does **not**
establish that it is a well-formed thumbprint input. Both files say so.

## Verification performed in pass 1

Mechanical, not by reading:

1. **Worked example.** `sha256` of the §6 thumbprint-input bytes
   (`A40102200121...0084D19C`, 75 bytes) reproduces the §6 thumbprint
   `496bd8af…9da253ec` exactly, and its unpadded base64url reproduces the §5.7
   string `SWvYr63zB-WwjGSwQhv53AFSijRKQ72oj63RZp2iU-w` exactly. The example
   fixture embedded in the JSON Schema is the same bytes and was re-checked
   the same way.
2. **CDDL rule closure.** 6 rules defined, no duplicate definitions, no rule
   referenced that is neither defined here nor an RFC 8610 Appendix D prelude
   name, no defined name colliding with a prelude name (the RFC 8785 defect),
   and braces balanced. Prelude names used: `int`, `bstr`.
3. **Cross-reference integrity.** Every `rfc-9679#R-NNNN` cited in this
   directory exists in `../requirements.yaml`.

No CDDL tool is installed in this environment, so (2) is a closure and
collision check rather than a parse.

## Source defects recorded here — reported, never repaired

1. **§4.1 labels its own columns differently from §4.2–§4.5.** It prints
   `"crv" (label: -1, value: int)` and `"x" (label: -2, value: bstr)` where
   every other subsection prints `data type:`, and its own `kty` bullet prints
   both (`data type: int, value: 1`). Read as *data type*; the bullets are
   reproduced as printed in `../normative.md` (R-0014, R-0015).

2. **RSA `n` and `e` have no stated normalisation.** §4.3 gives both as bare
   `bstr` and the document says nothing about leading zero octets or fixed
   width. The exponent 65537 as `h'010001'` and as `h'00010001'` are different
   byte strings and hash to different thumbprints, as are a modulus with and
   without a leading `0x00`. §7 makes "a single unambiguous COSE Key
   representation for that key is defined and used" the precondition for a
   thumbprint identifying a key at all (R-0057) — and for RSA, §4 does not
   supply one. RFC 8230 §4 does not close this either: it requires only that
   the fields be encoded as byte strings. **An implementation that uses this
   as a key identifier must pin a normalisation of its own and say so.**

3. **The §6 full example key is not in deterministic-encoding order.** Its
   printed encoding is `A5 01 02 | 20 01 | 21 5820 … | 22 5820 … | 02 5820 …`
   — `kid` (label 2, encoded `0x02`) last, where RFC 8949 §4.2.1 would place it
   second, immediately after `kty`. Nothing requires the *input* key to be
   deterministically encoded, so this is not non-conformance; it is worth
   recording because it is the clearest demonstration that §3 step 1
   **re-encodes** rather than filtering a received encoding in place.

4. **The `ckt` registration pins SHA-256 while §3 does not.** §8 registers the
   description "COSE Key SHA-256 Thumbprint" (the registration is R-0065; the
   clash is recorded in the note on R-0067), but §3 requires only
   that SHA-256 be *supported* and permits other algorithms (R-0005, R-0006),
   and the `ckt` member is a bare binary string with nowhere to name H
   (R-0046). A `ckt` computed with SHA-384 is indistinguishable on the wire
   from one computed with SHA-256. Only the §5.7 URI form carries the
   algorithm.

5. **§5.5 misattributes both of its cross-references.** It cites "the ckt of a
   COSE Key, as described in Section 7 of [RFC9052]" — RFC 9052 §7 defines the
   `COSE_Key` structure and never mentions `ckt`, which *this* document defines
   (§5.6, §8) — and "the jkt of a JSON Web Key, as described in Section 4 of
   [RFC7517]", where RFC 7517 §4 lists JWK parameters and `jkt` is RFC 7638
   (used as a confirmation member in RFC 9449 §6). Recorded at R-0043.

## What is not here, and why

**No schema for the `COSE_Key` structure itself.** That is RFC 9052 §7 and
belongs to `records/ietf/rfc-9052`. This document constrains only the reduced
structure that is hashed, which is what the CDDL describes.

**No schema for the CWT or the `cnf` claim.** RFC 8392 and RFC 8747 define
those; this document adds one member to one registry. The member's label,
value type and claim are carried as data in
`thumbprint-computation.derived.json` and as a structure in
`../messages.yaml`.

**No grammar for the URI form.** §5.7 states it as prose over a fixed prefix
plus two colon-separated fields; the pattern is carried as a JSON Schema
`pattern` on the `uri` property rather than as a separate ABNF, which would add
a second thing to keep in sync and no checking power.

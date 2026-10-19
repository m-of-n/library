---
record: rfc-9053
kind: schema
title: "rfc-9053 — schemas"
extracted: "2026-10-19"
reviewed_by: ""
---

# Schemas

**RFC 9053 ships exactly one CDDL fragment in 2443 lines.** It is the
`PartyInfo` / `COSE_KDF_Context` pair in §5.2, introduced by the sentence "The
following CDDL fragment corresponds to the text above." Everything else this
document defines — four key types, three curve families, 43 algorithm code
points, nine algorithm-specific header parameters, two capability structures and
one signature encoding — is defined in **prose and tables only**.

The document says so itself, in §1.4:

> When COSE was originally written, the Concise Data Definition Language (CDDL)
> [RFC8610] had not yet been published in an RFC, so it could not be used as the
> data description language to normatively describe the CBOR data structures
> employed by COSE. For that reason, the CBOR data objects defined here are
> described in prose. Additional (non-normative) descriptions of the COSE data
> objects are provided in a subset of CDDL, described in [RFC9052].

Two consequences, and they govern how every file here may be cited. First, the
one fragment that exists is **non-normative by the document's own statement** —
`kdf-context.cddl` transcribes a non-normative rendering inside an Informational
document, and the normative statement of `COSE_KDF_Context` is the §5.2 prose.
Second, **no machine-checkable rendering of RFC 9053's structures exists
upstream**, so four of the five files here are ours. That is the `R-O-03`
situation RFC 8785 is the sharp case of: a directory where the library wrote
nearly all of the formal content, and where mistaking a derived file for the
standard's own grammar is the live failure.

The filename carries the distinction and `bin/validate` enforces it: a
`.derived.` infix is mandatory on anything this library wrote, and an unmarked
name asserts verbatim bytes (`docs/extraction.md`, "Derived vs verbatim — the
filename carries it"). Each file repeats the claim in its own header.

## Per-file

| file | claim | what it covers | what it does **not** constrain |
|---|---|---|---|
| `kdf-context.cddl` | **verbatim** | **§5.2 complete** — the document's only CDDL: `PartyInfo` (3 entries) and `COSE_KDF_Context` (5 fields incl. the nested `SuppPubInfo`), cached source lines 1168–1184, with the RFC's three-space page margin, its internal blank line and its spacing around `:` and `/` preserved | **it does not compile.** `empty_or_serialized_map` is used and never defined — it is RFC 9052 §3's rule. It is **non-normative** (§1.4), and it does not express: that `identity`/`nonce`/`other` are "set to nil" when unused rather than absent (§5.2 prose), that `keyDataLength` is "the number of bits of the desired output value", that `protected` is "a zero-length bstr" when the protected field is empty, or §9's requirement that this structure in particular be deterministically encoded |
| `algorithm-values.derived.cddl` | derived | every code point RFC 9053 assigns, as named CDDL value groups: 4 signature, 8 MAC, 12 content-encryption, 18 recipient, `IV-GENERATION`, 4 key types (Table 17), 7 curves split by key type (Table 18) | **the pairings**, which are the whole of §2–§7. A value group cannot say that ES256 requires `kty` EC2, that Ed25519 is "for use w/ EdDSA only", or that `alg` **MUST** match the key's `alg`. It is also deliberately **closed** to the RFC 9053 set, so it rejects every later registration; and `alg` on the wire is `int / tstr` (RFC 9052 §3.1), which these groups do not admit |
| `key-structures.derived.cddl` | derived | `COSE_Key` for the three key types RFC 9053 defines — EC2 (Table 19), OKP (Table 20), Symmetric (Table 21) — each split into the public and private required sets §7.1.1/§7.2/§7.3 state; plus the §2.1 ECDSA signature sizes | **the common parameters**, which are RFC 9052 §7, stubbed here and not defined. It cannot express "but they can be recomputed from the required elements, and omitting them saves on space", the SEC1 leading-zero rule, the sign-bit encoding of `y` as a CBOR `false`/`true`, or §7.1's cross-check obligation. The three `.size` values are **OURS**, computed from the RFC's formula; the RFC prints the formula and no size. `EdDSA_signature` is an unconstrained `bstr` because RFC 9053 gives no size |
| `algorithm-headers.derived.cddl` | derived | all **nine** algorithm-specific header parameters — Table 9 (`salt`, −20), Table 10 (the six context parameters, −21…−26), Table 15 (`ephemeral key` −1, `static key` −2, `static key id` −3) — with each table's own Algorithm column as the scope, plus composite per-family groups and the **empty** groups for every algorithm that has none | the algorithm→parameter binding itself: CDDL cannot condition a header map on the `alg` value in the same map. The salt/nonce disjunction is rendered, but the condition that it applies only to direct+KDF and Static-Static is in the rule *name*, not the notation. The composite groups are **OURS** — RFC 9053 never prints a per-algorithm header group |
| `capabilities.derived.cddl` | derived | §8's capability arrays: the §8.1 one-element algorithm capability, the empty `IV-GENERATION` capability (§10.2), all six §10.1 Table 22 key-type lists, and the §8.3 three-field advertisement element | **the registry**, which is the actual constraint — §8 makes a capability list fixed by its IANA registration, and no schema performs a lookup. The advertisement form is explicitly "one of many encodings that could be used". The immutability rule cannot be written down at all |
| `README.md` | — | this file | — |

**No JSON Schema.** Every structure in RFC 9053 is a CBOR array or a map with
negative integer labels and `bstr` values; a JSON Schema would have to invent a
JSON projection the document does not define, and `docs/extraction.md`'s
`$id` rule would then be attached to a rendering with no source. CDDL is the
notation the COSE documents use and the one RFC 9052 ships.

## What the schemas together cannot do

**1. Bind an algorithm to its key.** This is the document's single largest
category of requirement and none of it is expressible. §2.1, §2.2, §3.1, §3.2,
§4.1, §4.2, §4.3, §6.1.2, §6.2.1, §6.3.1 and §6.4.1 each carry the same
four-to-five bullet block — `kty` **MUST** be present and **MUST** be a named
value; `alg`, if present, **MUST** match; `key_ops`, if present, **MUST**
include a named operation — and CDDL can condition none of it on a value in a
*different* map (the key) from the one being validated (the message header).
`messages.yaml` carries these as data, per algorithm.

**2. Scope a negative label.** COSE labels are scoped to the map they appear in
*and* to the key type or algorithm in force, and nothing in the encoding carries
that scope. Three collisions in this document alone:

| label | meaning A | meaning B |
|---|---|---|
| `-1` | `crv` in a `COSE_Key` with `kty` 1 or 2 (Tables 19, 20) | `k` in a `COSE_Key` with `kty` 4 (Table 21); `ephemeral key` in a recipient header (Table 15) |
| `-2` | `x` in a `COSE_Key` (Tables 19, 20) | `static key` in a recipient header (Table 15) |
| `-25`, `-26` | `PartyV nonce`, `PartyV other` in a recipient header (Table 10) | the **values** ECDH-ES+HKDF-256, ECDH-ES+HKDF-512 of `alg` (Table 14) |

**3. Say what a code point is for.** `IV-GENERATION` (34) is registered in "COSE
Algorithms" but is never carried in an `alg` header: §6.1.2 says "If HKDF is
used for generating the IV, the algorithm identifier is set to 34
("IV-GENERATION")", which is the `AlgorithmID` field of `COSE_KDF_Context`. The
registry holds two different namespaces in one column and the schema cannot tell
them apart; `algorithm-values.derived.cddl` keeps it in a separate group so a
validator cannot admit it where an `alg` is expected.

## Defects and ambiguities in RFC 9053 itself

Recorded here, never repaired in the files.

- **Table 8 has no Value column.** §5.1's four HKDF algorithms — "HKDF SHA-256",
  "HKDF SHA-512", "HKDF AES-MAC-128", "HKDF AES-MAC-256" — are given a Name, a
  PRF and a Description and **no code point**. They are not independently
  addressable in COSE; they reach the wire only inside the compound identifiers
  −10…−13 (Table 12) and −25…−34 (Tables 14, 16). Table 8 is also the only
  algorithm table in the document missing the Value column §1.3 says the
  algorithm tables carry.
- **§9's scope bullet is ambiguous.** §9 says "It has been narrowed down to the
  following restrictions:" and then lists, as the first of three bullets, "The
  restriction applies to the encoding of the COSE_KDF_Context." Singular
  "restriction" against plural "restrictions". On the narrow reading the
  definite-length / minimum-argument rule binds only `COSE_KDF_Context`; on the
  wide reading it binds every structure. **The parallel text in RFC 9052 §9
  settles it**: identical wording, identical three bullets, with the scope
  bullet naming "the Sig_structure, the Enc_structure, and the MAC_structure"
  instead. Each document scopes the rule to its own structures, so the narrow
  reading is right — and the consequence is that **neither document requires the
  transmitted COSE bytes to be deterministically encoded.** `design-notes.md`
  carries what that costs us.
- **§1.4 points at a CDDL subset it does not reproduce.** "Additional
  (non-normative) descriptions of the COSE data objects are provided in a subset
  of CDDL, described in [RFC9052]" — but RFC 9052 describes the *subset of CDDL*,
  not the RFC 9053 structures. There is no CDDL anywhere for Tables 17–21. A
  reader following §1.4 to RFC 9052 finds `COSE_Key` and the common parameters,
  and no `crv`, `x`, `y`, `d` or `k`.
- **Table 15's `static key id` is a `bstr` with no stated relationship to
  `kid`.** §6.3.1 says a static key "can be identified by providing either the
  key ("static key") or a key identifier for the static key ("static key id")"
  and never says the identifier is a `kid` (RFC 9052 §3.1, label 4) or how it is
  computed.
- **§7 Table 17 lists `Reserved: 0` as a key type value.** The document says only
  "This value is reserved" and nowhere states what a recipient does on seeing it.
- **§2.1's curve/hash pairing is advice, not a requirement.** "In order to
  promote interoperability, it is suggested that SHA-256 be used only with curve
  P-256, SHA-384 be used only with curve P-384, and SHA-512 be used only with
  curve P-521." Lowercase "suggested", so ES256 over P-384 is conforming — while
  §2.1.1 admits that the curve-substitution attack has no mitigation "except to
  restrict the overall set of curves that can be used."

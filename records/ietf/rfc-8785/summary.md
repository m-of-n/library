---
schema: "library-summary/v1"
id: rfc-8785
record: rfc-8785
type: summary
updated: "2026-10-03"
---

# JSON Canonicalization Scheme (JCS)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | informational — Independent Submission stream, explicitly **not** IETF standards track (§2) |
| **Authors** | A. Rundgren, B. Jordan, S. Erdtman |
| **Published** | June 2020 |
| **Identifier** | RFC 8785 · DOI 10.17487/RFC8785 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8785.txt |
| **Digest** | `63d52294eb0e…` (sha-256 of the .txt, retrieved 2026-10-03) |

## Overview

JCS defines how to turn JSON into a unique byte string so that it can be hashed
and signed. Its method is to delegate rather than invent: primitive
serialisation is ECMAScript's (`JSON.stringify` semantics, with numbers per
ECMA-262 §7.1.12.1 including the "Note 2" enhancement), the input is constrained
to the I-JSON subset of RFC 7493, object properties are sorted recursively by
UTF-16 code unit, and the result is emitted as UTF-8 with no inter-token
whitespace. The stated design goal is that *"a JSON object remains a JSON object
even after being signed"* — data stays in its original form on the wire while
cryptographic operations run over its canonicalised counterpart. The authors
contrast this deliberately with JWS, which sidesteps canonicalisation by
base64url-encoding the payload, and with XML DSIG, whose canonicalisation rules
they regard as a cautionary tale.

The document is an Independent Submission and Informational. §2 concedes it *"is
not on the IETF standards track"* while asserting that a conformant
implementation is nonetheless *"supposed to adhere to the specified behavior for
security and interoperability reasons."*

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | It is a canonicalisation-before-signing scheme, and §5 plus Appendix F specify the order in which a verifier must act — which is exactly where the DSSE critique bites. |
| Cryptography | adjacent | Defines no primitives. It produces the byte string a signature is computed over. |
| This project | core | **DEC-002 option 3** names it directly ("JSON + RFC 8785 JCS as canonical; DSSE for signed form"). This record is the primary evidence for or against that option. |

Bears on **DEC-002**, **R-O-03** (cite the canonicalisation algorithm, do not
invent one) and **R-O-05** (sign canonical bytes verbatim; never canonicalise
during verification). The R-O-05 relationship is adversarial rather than
supporting, and it is the most consequential thing in this record — see Limits.

## Implementations

Appendix G, as listed by the source (2020); independently surveyed 2026-10-03.

| Name | Kind | License | URL |
|---|---|---|---|
| canonicalize (JS) | open source | — | https://www.npmjs.com/package/canonicalize |
| java-json-canonicalization | open source | — | https://github.com/erdtman/java-json-canonicalization |
| json-canonicalization (Go) | open source | — | https://github.com/cyberphone/json-canonicalization |
| json-canonicalization (.NET/C#) | open source | — | https://github.com/cyberphone/json-canonicalization |
| json-canonicalization (Python) | open source | — | https://github.com/cyberphone/json-canonicalization |

Two observations a build-on-it decision turns on:

- **Four of the five listed implementations live in one repository belonging to
  the specification's own first author.** The Java one belongs to its third
  author. That is a narrow independent-implementation base for something we
  would make load-bearing, and it is a different situation from RFC 8949's
  dozen-plus independently maintained libraries.
- **The hard part is delegated, not solved.** Number serialisation is the one
  genuinely difficult step and §3.2.2.3 declines to specify the algorithm,
  pointing instead at V8 and at Ryu. So a JCS implementation's correctness rests
  on whichever shortest-round-trip float printer the host platform ships.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata and typed relations |
| `summary.md` | this document |
| `distilled/` | the FX-1 artifact set — see `distilled/README.md` |

## Limits

- **§5 and Appendix F mandate the ordering R-O-05 forbids.** §5 requires an
  application to (1) parse and check I-JSON, (2) verify correctness and locate
  the signature property, and only then (3) verify the signature. Appendix F is
  more explicit still: its verification scheme parses the signed JSON, removes
  the signature property, **re-serialises the remainder, and re-canonicalises
  it** before comparing. That is canonicalisation performed as part of
  verification, over untrusted input, which R-O-05 prohibits in terms. This is
  not a tension to be managed; as JCS specifies its own use it is a direct
  contradiction, and it is the DSSE critique arriving with normative force.
- **Numbers are limited to IEEE 754 double precision** (§3.1). Anything outside
  that — integers past 2^53, high-precision decimals — *"MUST be wrapped using
  the JSON string type"* (Appendix D). The document's own example of the problem
  includes `int64Max`.
- **The canonical form is not stable across parser styles.** Appendix E shows
  that stream- and schema-based parsers substitute native subtypes on the fly,
  so `"055"` canonicalises to `"55"` and `"2019-01-28T07:45:10Z"` to
  `"2019-01-28T07:45:10.000Z"`, *"presumably making an application depending on
  JCS fail."* The mitigation is a discipline imposed on every application, not a
  property of the scheme.
- **It declines Unicode normalisation** (§3.1): all components *"MUST preserve
  Unicode string data 'as is'."* A deliberate, defensible choice, but it leaves
  normalisation-variant labels distinct — which matters wherever a label is
  load-bearing for identity.
- **Array element order MUST NOT be changed** (§3.2.3). Sorting reaches object
  properties recursively and stops there, so a logical set carried in an array
  has no canonical order.
- **Sorting is defined on UTF-16 code units**, and the source notes that sorting
  the same data as UTF-8 or UTF-32 yields a different and incompatible order.
- **No authenticated type indicator**, so option 3 must pair it with an envelope
  that supplies one.
- **Read scope:** this summary was written from the complete source text,
  §1–§6 and Appendices A–I. The FX-1 artifacts under `distilled/` were extracted
  independently from the same source and are the citable detail.

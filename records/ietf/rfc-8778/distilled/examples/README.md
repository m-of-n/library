---
record: rfc-8778
kind: examples
title: "rfc-8778 — examples and test vectors"
extracted: "2026-10-20"
reviewed_by: ""
---

# Examples and test vectors

<!-- Every example in the source as a fixture file (verbatim bytes or
text), with the expected verification result. These drive our tests. -->

**RFC 8778 prints two complete COSE messages and not one key.** Both messages
reproduce to the byte; no key, no `pub` value and therefore no `KeyId` exists
anywhere in the document. Those two sentences bound everything in
`vectors.yaml`, and the second is the more important one.

| | |
|---|---|
| **Vectors** | 11 — `V-0001` … `V-0011` |
| **Fixtures** | 4 byte blocks: both printed signatures (2512 octets each, verbatim) and both whole messages (2560 and 2552, re-encoded) |
| **Reproduced** | both stated file sizes, both protected buckets, both signature parses, the u32str width, the parameter set, the shared `C`, the shared authentication path |
| **Not reproducible, and why** | no cryptographic verification of either signature, and no thumbprint — the document prints no key |

## What reproduced

**Both stated sizes, exactly.** The document states only the size of each
example — "The size of binary file is 2560 bytes" (`R-0133`) and "2552 bytes"
(`R-0135`) — and prints the rest as extended CBOR diagnostic notation
(`R-0130`). Re-encoding that notation under RFC 8949 gives **2560** and
**2552**. `V-0001`, `V-0002`.

**Both protected buckets, round-tripped.** `h'a10300'` decodes to `{3: 0}` and
`h'a101382d'` to `{1: -46}`, and both re-encode byte-identically under
RFC 8949 §4.2.1. `V-0007`. Those four octets are **the only place in RFC 8778
where −46 appears as bytes**; §6.1 states the value, Appendix A encodes it.

**Both signatures parse cleanly against the document's own renderings** —
`u32str(0) || u32str(q) || u32str(otstype) || C || y[0..66] || u32str(type) ||
path[0..9]`, 2512 octets, nothing left over. `V-0003`, `V-0004`.

**The `u32str` width, which the document never states.** `R-0028` defers the
notation to `[HASHSIG]`, so 4 octets is **measured, not cited**: RFC 8778's own
formulas make the signature `4u + n + n·p + m·h` octets with `m = n = 32`
(`R-0039`, `R-0066`), and `2512 − 4u − 32` is divisible by 32 for `u = 4` and
for no other `u` in {1, 2, 8}. `h = 10` and `p = 67` follow. This is the one
place in the document from which the width is recoverable, and it is in a
non-normative appendix.

**The strongest internal consistency check the document admits, and it passes.**
`R-0061` fixes the authentication path's order — leaf sibling first, then the
sibling of the leaf's parent, and so on. A.1 is leaf `q = 1` and A.2 is leaf
`q = 0` of **one** tree, so leaves 0 and 1 are siblings and the rule *predicts*
that the two paths differ in `path[0]` and agree in `path[1..9]`. Measured:
**9 of 10 nodes byte-identical, index 0 differing.** 288 octets of Merkle
structure agreeing across two independently printed 2512-octet values, for a
reason the text states. `V-0006`.

## Two negative observations, both measured

**Both signatures carry the same `C`.** `R-0078` calls `C` "an n-byte random
value"; octets 12–43 of both printed signatures are the same 32 octets, across
two different `Sig_structure` contexts from two different leaves. Not a
violation of anything RFC 8778 states, and recorded because a reader treating
Appendix A as a demonstration of per-signature randomisation would be wrong, and
because a test suite built from these two fixtures gets **no coverage of `C`
varying**. `V-0005`, `normative.md` observation 9.

**The document's own `kid` ignores the document's own suggestion.** `R-0090`
says a `kid` MAY be used to identify the top of the HSS tree and `R-0092` says
that identifier is 16 octets. Both examples use `'ItsBig'` — **six ASCII
octets**. Conforming, because `R-0090` is a MAY and nothing binds a `kid` to the
key's actual `I`. So §3's `kid` suggestion, which is this record's whole
contribution to `DEC-003`, has **no worked instance anywhere in RFC 8778**.
`V-0008`.

## What cannot be reproduced, and exactly why

**No signature here is cryptographically verified, and none can be from this
document.** Verifying an LMS signature means recomputing a candidate root from
the signature and the message and comparing it against `T[1]`. Both steps need
the public key: `I` enters every hash input and `T[1]` is the thing compared
against. RFC 8778 prints neither, and an LMS signature does not carry them. This
is a hard limit of the source. Contrast `records/ietf/rfc-9964`, whose six
printed signatures its verify pass could check **because that document prints
its keys**.

**No HSS-LMS public key and no HSS-LMS `KeyId` is computable from any document
this library holds.** Measured over all 772 lines: `COSE_Key` **0**
occurrences, `kty` **1** (§3's checklist), `pub` **1** as a word (§6.3's
registration template), `thumbprint` **0**. No key, no `pub` value and no `I` or
`T[1]` value appears anywhere, in any notation.

`V-0009` and `V-0010` are therefore **templates, not vectors with elided
values** — there are no values to elide. `V-0009` gives the 56-octet layout with
its four field offsets; `V-0010` gives the exact six-octet prefix of RFC 9679
§4.5's thumbprint input, `a20105205838`, and the total, 62 octets. The structure
is exact. The digest is unavailable.

**Nothing was synthesised.** No key was invented to fill the gap, and no digest
appears in this directory that was computed over made-up bytes. That is the
whole of the discipline here, and it is why `source: template` exists as a third
provenance class alongside `printed` and `derived`.

**What would close it.** One `COSE_Key` for `kty: 5` from any source this
library can hash. The obvious candidate is RFC 8554's own test vectors —
`[HASHSIG]` Appendix F prints LMS public keys — and
`records/ietf/rfc-8554` is a **stub**. Extracting RFC 8554 would make every
template in this file a vector, and would also supply the parameter-set code
points RFC 8778 omits (see `../schema/parameter-sets.derived.yaml`). That is the
single highest-value follow-on this record identifies.

## Method

A CBOR encoder and decoder (RFC 8949 §3 and §4.2.1) written for this pass over
the Python standard library alone. **No CBOR, COSE, CWT or HSS/LMS library was
used**, so a shared library bug cannot hide here.

Checks run, all passing:

- the two fixture signature hexes are **byte-identical to a fresh cut from
  `.cache/rfc-8778.txt`** at lines 584–658 and 679–753;
- each fixture's declared `octets` matches its hex length, and each declared
  `sha256_of_bytes` matches a recomputation;
- both re-encoded whole messages **decode fully** — no trailing octets — to
  tag 98 and tag 18, payload `'This is the content.'`, and a 2512-octet
  signature **equal to the source cut**;
- `vectors.yaml` round-trips through **both** of the library's YAML readers,
  `bin/_yaml.py` and `bin/_record_yaml.py`, which agree on all 11 vectors and
  all 4 fixtures including the wrapped hex block scalars.

## Provenance convention

As `rfc-9964`'s and `rfc-8392`'s vectors use it, with one addition.

| `source:` | meaning |
|---|---|
| `printed` | every byte of the value appears in RFC 8778. `reproduced` says what this pass recomputed and whether it matched |
| `derived` | every byte is printed by the source, but the **assertion** is this extraction's — a parse, a measurement, a re-encoding |
| `template` | **new here.** The structure is specified by the source and **no value exists in it.** Not a fixture; a statement of what a fixture would have to contain |

`locator` gives the section, the exact line range in `.cache/rfc-8778.txt` and
the sha256 of that run of lines joined by `\n` with no trailing newline, so any
value can be re-cut from the source without trusting this file. The RFC
hard-wraps its hex blocks for display; the only transformation applied is
joining those lines. Page decoration falls inside none of the quoted ranges.

**Why the hex is committed at all.** FX-1's examples artifact is "every example
in the source as a fixture file, plus expected results; this is what drives our
tests" (`docs/extraction.md`), and the skill asks for it as "every example and
test vector as a fixture file, verbatim, with the expected result; hex for
binary" (`.claude/skills/extract/SKILL.md`). `records/ietf/rfc-9964` and
`records/ietf/rfc-8392` both carry their sources' printed vectors the same way. Two 2512-octet values
carried as fixtures with expected results is not a copy of a 772-line document:
the document is not in this repository and `.cache/` is gitignored.

## The sizes, in one place

`V-0011` collects every figure and recomputes them in one pass so the set is
internally consistent.

| quantity | octets |
|---|---|
| HSS-LMS public key (`pub`) | **56** |
| minimal `COSE_Key` `{1: 5, −1: pub}` | 62 |
| RFC 9679 §4.5 thumbprint input | 62 — **byte-identical** to the minimal key |
| `KeyId` (SHA-256) | 32 |
| **key − `KeyId`** | **+24** |
| signature | **2512** |
| LM-OTS signature within it | 2180 |
| LMS signature within it | 2508 |
| payload | 20 |
| `COSE_Sign` (tag 98) total | 2560 — envelope overhead 48 |
| `COSE_Sign1` (tag 18) total | 2552 — envelope overhead 40 |
| signature ÷ payload | 125.6× |
| signature ÷ public key | 44.9× |

**The trade inverts against `rfc-9964`.** There an ML-DSA public key is
1312–2592 octets against 32 for its thumbprint, so carrying the key costs 41–81
times as much. Here the key is 56 octets — **24 more than its own thumbprint, 30
more as a minimal `COSE_Key`** — so carrying it is nearly free, and the whole
expense has moved to the signature. `design-notes.md` under `R-M-02`.

**A sibling lane's reading is refuted by `V-0003`.** It read octets 8–11 of both
signatures — `00000003` — as `LMOTS_SHA256_N32_W8`. The structural arithmetic
gives `p = 67`, which is the `w = 4` parameter count; `w = 8` has `p = 34` and
would make the signature `1136 + 32h` octets, never 2512. So `00000003` cannot be
the W8 code point. What RFC 8778 itself supports is weaker and is the real
finding: **the document prints no code point for any of its nine named parameter
sets**, so neither `00000003` nor `00000006` is resolvable to a *name* from this
document at all. The parameters are recoverable; the names are not.

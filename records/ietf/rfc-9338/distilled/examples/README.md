---
record: rfc-9338
kind: examples
title: "rfc-9338 — examples and test vectors"
extracted: "2026-10-20"
reviewed_by: ""
---

# `examples/` — Appendix A, encoded and checked, plus the structures it omits

**14 vectors in `vectors.yaml`, 6 fixtures in `fixtures/`.** Every fixture is
an **exact run of source lines** with its range and its own sha256; every hex
string is **derived**, produced by encoding the document's own CBOR diagnostic
notation under RFC 8949 shortest-form heads with the written map key order
preserved.

## The six printed messages

| vector | § | target | stated | encoded | |
|---|---|---|---:|---:|---|
| `V-0001` | A.1.1 | `COSE_Sign` (tag 98) | 180 | **180** | ✓ |
| `V-0002` | A.2.1 | `COSE_Sign1` (tag 18) | 275 | **275** | ✓ |
| `V-0003` | A.3.1 | `COSE_Encrypt` (tag 96) | 326 | **326** | ✓ |
| `V-0004` | A.4.1 | `COSE_Encrypt0` (tag 16) | 136 | **136** | ✓ |
| `V-0005` | A.5.1 | `COSE_Mac` (tag 97) | 159 | **159** | ✓ |
| `V-0006` | A.6.1 | `COSE_Mac0` (tag 17) | 159 | **139** | **✗ source defect** |

**A.6.1's stated size is wrong by 20 bytes, and no erratum covers it.** A.6.1 is
a `COSE_Mac0` and A.5.1 a `COSE_Mac` with the same protected bucket, the same
countersignature, the same payload and a tag of the same width. The whole
difference between them is the tag head — two octets for 97, one for 17 — plus
A.5.1's 19-octet `recipients` array, which a `COSE_Mac0` does not have. That is
exactly 20. And **A.5.1's and A.6.1's preambles are byte-identical runs of
source text**, so the number was carried over from A.5.1.

**Five of six reproducing exactly is also what validates the encoder** — and so,
independently, is this: all **13** `<< … >>` embedded maps encode to
precisely the hex the document's own diagnostic comments claim for them
(`h'a10126'`, `h'A201260300'`, `h'A1013823'`, `h'a10101'`, `h'a1013823'`,
`h'A10101'`, `h'A10127'`, `h'A10105'`, and five repeats). **13 comments, 13 matches.**

## The eight derived to-be-signed structures — the point of this directory

RFC 9338 prints **no** `Countersign_structure`, which is the one thing an
implementer has to get byte-exact. `V-0007`–`V-0014` are those structures, built
from the document's own components.

| vector | target | `other_fields` | `context` | bytes | unique? |
|---|---|---|---|---:|---|
| `V-0007` | `COSE_Sign` | omitted | `CounterSignature` | 45 | **yes** — and it contains **no signature value** |
| `V-0008` | `COSE_Sign1` | `[signature]` | `CounterSignatureV2` | 120 | **yes** — the only one of the eight that binds a signature |
| `V-0009` | `COSE_Mac` | `[tag]` | `CounterSignatureV2` | 85 | yes — binds a **MAC tag** |
| `V-0010` | `COSE_Mac0` | `[tag]` | `CounterSignatureV2` | 85 | yes — binds a **MAC tag** |
| `V-0011` | `COSE_Encrypt` | omitted | `CounterSignature` | 66 | **no** — positional reading only |
| `V-0012` | `COSE_Encrypt0` | omitted | `CounterSignature` | 65 | **no** — positional reading only |
| `V-0013` | `COSE_Signature` | omitted | `CounterSignature` | 93 | the **positional** reading |
| `V-0014` | `COSE_Signature` | omitted | `CounterSignature` | 48 | the **semantic** reading |

**Two of the document's own six examples cannot be reduced to a unique
to-be-signed value.** A.3.1 and A.4.1 target structures with no `payload` field,
and §3.3 does not say what fills `Countersign_structure.payload` for them.
V-0011 and V-0012 are built under the positional reading and say so.

**`V-0013` and `V-0014` are the contested case built both ways**, which is the
measurement behind `../design-notes.md` §3.4 rather than an argument about it.
`vectors.yaml`'s `collisions` entry records the result: under the **semantic**
reading two signers over one payload with identical protected buckets produce
the **same** 48-byte structure, so a countersignature over one verifies
unchanged as one over the other; under the **positional** reading they differ.

## What cannot be reproduced, and why

**No signature verification, at all.** RFC 9338 prints no key material anywhere
— no `COSE_Key`, no `x`/`y`/`d`, no public key for any of the four `kid` values
it uses. So no signature in Appendix A can be verified from this document alone.
The three ECDSA examples (A.1.1, A.2.1, A.3.1) are randomised and could not be
*reproduced* even with the keys; the three EdDSA ones (A.4.1, A.5.1, A.6.1) are
deterministic and would be. What is reproduced here is the encoding, the sizes
and the structures.

**No tag-19 example, no label-12 example, no detached-payload example.** The
document prints none of the three. The last is the one that would have forced it
to say whether its `bstr` count is by type slot or by wire item.

## One thing to know before reusing these as encoding vectors

**A.3.1's recipient unprotected map is not in deterministic key order.** It is
written `{-1: …, 4: …}` and under RFC 8949 §4.2.1 bytewise ordering the encoded
keys are `0x20` and `0x04`, so `4` would come first. Nothing is violated — §4's
`MUST` binds the to-be-signed value, not the message — but it means **these are
countersignature fixtures and not deterministic-encoding fixtures.** Every other
map in the six examples is in deterministic order.

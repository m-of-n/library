---
record: rfc-9741
kind: examples
title: "rfc-9741 — examples and test vectors"
extracted: "2026-10-19"
reviewed_by: ""
---

# Examples and test vectors

`vectors.yaml` holds **8 vectors**, `V-0001`–`V-0008`, in source order with no
gaps, covering **every example RFC 9741 prints**: six CDDL fragments and four
instances (3 valid, 1 invalid).

| vector | § | construct | instance | expect |
|---|---|---|---|---|
| `V-0001` | §2.1 | `text .b64u` over `bytes .cbor COSE_Sign1` | — | valid |
| `V-0002` | §2.2 | `text .base10 (0..9223372036854775807)` | — | valid |
| `V-0003` | §2.3 | `hexlabel<19>` | `0x0013` | valid |
| `V-0004` | §2.3 | `hexlabel<1..20>` | `0x0013` | valid |
| `V-0005` | §2.3 | `hexlabel<1..20>` | `0x0001` | valid |
| `V-0006` | §2.3 | `hexlabel<1..20>` | `0x1234` | **invalid** |
| `V-0007` | §2.4 | `text .json claims` | — | valid |
| `V-0008` | §3.1 | Figure 1, `text .join` dotted-decimal IPv4 | — | valid |

`V-0004`–`V-0006` share one CDDL fragment because the source gives it three
instances in a single sentence: *"Here, any_alg matches the text strings
"0x0013" or "0x0001" but not "0x1234"."* The one negative is the source's own;
none is invented.

Each `cddl` block is lifted from the cache by line range, by script, never
retyped; the only transformation is removal of the common three-space left
margin. All eight were re-verified as dedented contiguous slices at their
declared `source_lines`, and each of the four `instance` values was confirmed
present in the source.

## The finding that matters most here

**This document prints not one instance of any base encoding it defines.**
Ten of its fourteen operators convert between text and byte strings, and there
is no base64, base64url, base32, base32hex, base16 or base45 test vector
anywhere in RFC 9741 — not a single `"aGVsbG8"` or `"68656c6c6f"`. Nor does it
print an instance for `.json` or `.join`. The only instances in the whole
document are the three hex labels in §2.3, and they are `.printf` output, not
a base encoding.

**Consequence for library#39.** The test-vector role cannot be fed from this
document for the ten operators we are most likely to use. Every fixture for
`.hexlc`, `.b64u` or `.b45` would be **ours**, and under `R-O-03` ours must be
cited as ours. The encodings themselves are citable — RFC 4648 §10 carries
test vectors and RFC 9285 carries its own — but the *CDDL matching behaviour*
of these operators has no published fixture at all. If we want to know that
two tools agree about `text .b64u bytes`, we have to write that agreement test
ourselves.

## What a fixture consumer should know

- **No instance is binary.** Every instance here is a short ASCII text string,
  so there is no hex-encoded fixture and nothing to decode.
- **`V-0001`'s `COSE_Sign1` is undefined.** The source names it and never
  defines it; the rule cannot be instantiated without RFC 9052. The vector is
  carried as printed, unresolved. It is also the closest thing in the document
  to our own export path — see `../design-notes.md` §2.1.
- **`V-0007` matches unboundedly many texts.** `.json` cannot constrain blank
  space or map-entry order (`rfc-9741#R-0040`), so `{"iss":"a","exp":"b"}` and
  `{ "exp" : "b" , "iss" : "a" }` both match. Any fixture we write for it
  therefore tests *our* serialization choice, not the document's.
- **`V-0003`'s lower-case hex digits are not stated.** `%x` gives lower case
  and `%X` upper, and for the value 19 both produce `0x0013`, so the example
  does not actually exercise the distinction. A fixture that did would be ours.
- **No vector exercises `.join`'s hard cases**: the empty controller array, a
  controller whose first element is a byte string, or an element that ends
  mid-UTF-8-sequence. Those are the three places `.join` can surprise an
  implementer, and the document illustrates none of them.

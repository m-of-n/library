---
record: rfc-9053
kind: examples
title: "rfc-9053 — examples and test vectors"
extracted: "2026-10-19"
reviewed_by: ""
---

# Examples and test vectors

## RFC 9053 prints no cryptographic test vectors

Not one. In 2443 lines assigning **43 algorithm code points** across four
signature algorithms, eight MACs, twelve content encryption algorithms and
eighteen content key distribution methods, the document prints no key, no
signature, no MAC tag, no ciphertext, no nonce, no derived key, no
`COSE_KDF_Context` and no `COSE_Key`. There is no appendix of examples and no
figure containing a cryptographic value.

**This absence is itself a finding**, and the strongest one this directory
carries. A document whose entire purpose is to assign code points to
cryptographic algorithms, and to state for each one the key type, curve, key
length, nonce length, tag length and signature encoding, ships nothing an
implementer can test against. The P-521 signature length is the sharp case:
§2.1 gives the formula `Signature = I2OSP(R, n) | I2OSP(S, n)` with
`n = ceiling(key_length / 8)` and prints no size, so the reader must work out
that an ES512 signature is 132 bytes and not 128 — and has no vector that would
catch the error.

### What the document does instead

§1.5, in full:

> A GitHub project has been created at [GitHub-Examples] that contains a set of
> testing examples. Each example is found in a JSON file that contains the
> inputs used to create the example, some of the intermediate values that can be
> used for debugging, and the output of the example. The results are encoded
> using both hexadecimal and CBOR diagnostic notation format.
>
> Some of the examples are designed to be failure-testing cases; these are
> clearly marked as such in the JSON file.

The reference is `[GitHub-Examples]`, `"GitHub Examples of COSE", commit
3221310, 3 June 2020, <https://github.com/cose-wg/Examples>`, listed under
**Informative** References.

Three things follow, and they are why this is recorded as a defect rather than
as a convenience.

1. **The corpus is informative, not normative.** Nothing in RFC 9053 requires an
   implementation to pass it, and §1.5 calls the content "testing examples"
   rather than test vectors.
2. **It is pinned to a commit that predates the RFC by more than two years.**
   Commit `3221310`, 3 June 2020, against publication in August 2022. The
   document does not say whether the corpus was regenerated for the final
   algorithm set, and `IV-GENERATION` (34), the one code point RFC 9053 newly
   allocates (§10.2, Table 23), postdates nothing in a 2020 corpus that we can
   check from the document.
3. **It is a repository, not an archived artifact.** A commit hash in a
   reference entry is better than a bare URL, but under this library's rules it
   is still a third-party document we do not hold — `content.sha256` for the
   corpus is not recorded anywhere, and the record for RFC 9053 does not claim
   it. An extraction cannot verify a single algorithm in this document against
   anything the document itself supplies.

**For our purposes** (library#39, the export path): the D5 fixture package due
Oct 28 cannot be built from RFC 9053. It can be built from RFC 9053 **plus** the
upstream primitives — RFC 6979 for deterministic ECDSA, RFC 8032 for EdDSA — and
the choice of which matters: §2.2.1 says "Signing and nonbatch signature
verification are deterministic operations and do not need random numbers of any
kind", so **EdDSA fixtures are byte-reproducible from the primitive alone**,
while ES256 fixtures are reproducible only if the signer uses RFC 6979, which
§2.1 states as a SHOULD and not a MUST.

## What is in `vectors.yaml`

**Six vectors, `rfc-9053#V-0001` … `rfc-9053#V-0006`, in source order with no
gaps.** Every concrete value the document prints, and nothing else.

| id | locator | what | bytes? |
|---|---|---|---|
| `V-0001` | §8.3 | algorithm capability for ES256 | `0x8102` |
| `V-0002` | §8.3 | key type capability, EC2 with P-256 | `0x820201` |
| `V-0003` | §8.3 | ECDH-ES+A256KW with X25519, the concatenated form | `0x8101820104` |
| `V-0004` | §8.3 | the four-element capability advertisement | **none printed** — diagnostic notation only |
| `V-0005` | §9 | the integer 1 as `0x01`, not `0x1801` | `0x01` valid / `0x1801` invalid |
| `V-0006` | §11 | the `"YES"` / `"NO "` padding illustration | **none** — text strings |

Three of the six are capability structures, which is to say that **the only
bytes RFC 9053 prints anywhere are five bytes of §8 capability encoding**, for a
feature that is advisory and that §8.3 itself describes as "one of many
encodings that could be used for that purpose."

## How a vector is built

- **`bytes`** — the document's own hex string, copied exactly, including its
  `0x` prefix. Where the document prints none, the field says so in words
  rather than carrying a value this library computed.
- **`diagnostic`** — the document's own annotation or notation. `V-0004`'s block
  is lifted from the cached source by line range (lines 1919–1948), by script,
  never retyped; the only transformation is removal of the common three-space
  page margin, which a YAML block scalar performs in any case. The irregular
  spacing inside the comments — `[1 /OKP/, 7 /Ed448 /]` against
  `[1 / OKP /, 6 / Ed25519 / ]` — is the document's.
- **`decodes_to`** — **OURS.** Every decoding in this file is this library's,
  performed under RFC 8949 §3.1. RFC 9053 decodes only `V-0004`, in the prose
  that follows it, and those sentences are quoted in that vector's `notes`.
- **`expect`** — `valid` throughout, with `V-0005` additionally carrying
  `counter_example_bytes` / `counter_example_expect`, the document's own
  invalid form.
- **`notes`** — the document's sentences in quotation marks; anything marked
  **(OURS)** is this library's reading or arithmetic.

## Findings in the examples themselves

**`V-0003` is a CBOR sequence and the document does not say so.** `0x8101820104`
is two data items — `0x8101` = `[1]`, `0x820104` = `[1, 4]` — not one array.
§8.3 calls it "the third example, which just concatenates the two capabilities
together" and §8 calls it a "cross product … between an array of algorithm
capabilities and key type capabilities", but neither gives the pair a containing
array and neither uses the words "CBOR sequence". A decoder asked for one data
item consumes two bytes, returns `[1]`, and leaves three bytes unread **with no
error** — the failure mode RFC 8742 exists to name. Anything that consumes COSE
capabilities needs to be told, out of band, how many items to read.

**§8 misspells the algorithm it points at.** "see the ECDH-ES+A25KW element" in
§8, against `ECDH-ES + A256KW` in Table 16 (−31) and "ECDH-ES + A256KW with an
X25519 curve:" in §8.3. One missing `6`. That quotation also *heals* a
hyphenation line break — the plain text reads `ECDH-` / `ES+A25KW` across
L1826/1827 — so it is verbatim against the RFC but not a contiguous substring
of the cached text; see `../README.md` defect 3 for the rule.

**Two annotation conventions, neither of them RFC 8949's.** `V-0001`–`V-0003`
annotate with `\ ... \` nested inside an outer `/ ... /`; `V-0004`, which is
notation rather than a comment on hex, uses `/ ... /` throughout. RFC 8949 §8
defines `/ ... /` for comments in diagnostic notation and defines no backslash
form. (OURS: the reading that the inner backslashes exist to avoid closing the
outer comment early. The document offers no explanation.)

**`V-0004`'s third element has a different shape from the first two.** Elements
one, two and four carry a *flat* algorithm capability (`[1 / OKP key type /]`);
element three carries a *nested array of arrays* (`[[ 2 /EC2/], [1 /OKP/ ]]`).
§8 licenses both as "one or more algorithm capabilities" and gives no rule for
distinguishing a single capability from a list of them — and since a capability
is itself an array of integers, `[[2],[1]]` and `[2, 1]` are both well-formed
readings of *the capabilities for this algorithm*. A parser cannot tell them apart
from the encoding.

**`V-0005` is the only valid/invalid pair in the document**, and its scope is
narrower than it looks. §9's first bullet is "The restriction applies to the
encoding of the COSE_KDF_Context", so the minimum-length rule it illustrates
binds that structure and, on the plain reading, nothing else RFC 9053 defines.
The identical §9 of RFC 9052 carries the identical rule scoped to "the
Sig_structure, the Enc_structure, and the MAC_structure". Taken together,
**neither document requires the transmitted COSE bytes to be deterministically
encoded** — only the inputs to the cryptographic computations. `design-notes.md`
carries what that costs an encoding decision that is premised on determinism.

---
record: rfc-9054
kind: examples
title: "rfc-9054 — examples and test vectors"
extracted: "2026-10-20"
reviewed_by: ""
---

# Examples and test vectors

**RFC 9054 prints not one digest value, for any of the eight algorithms it
registers — including the one it defines itself.** `Figure`, `Appendix`,
`vector` and "test vector" occur **zero** times in its 498 lines; there is no
hex and no base64 anywhere. For a document whose whole purpose is to name eight
hash functions so that two parties can agree on which one, there is nothing to
check an implementation against.

Its only examples of anything are §2.1's two CDDL fragments, and those are
carried here as V-0005 with mechanical parse verdicts. Everything else is this
extraction's computation, over one fixed input printed in the file so any value
can be recomputed from the file alone.

| vector | what it is | result |
|---|---|---|
| V-0001 | all eight identifiers as CBOR | **5 of 8 cost one octet**, against §4.1's "two-byte" rationale |
| V-0002 | all eight digests over one input | reference set; 7 of 8 checkable against FIPS |
| V-0003 | **the SHA-256/64 ambiguity** | both readings computed; **the document admits both** |
| V-0004 | SHA-512/256 vs truncated SHA-512 | **completely different**; Table 2's description says otherwise |
| V-0005 | §2.1's two structures, verbatim | `COSE_Hash_V` **parses** — as 24 entries; `COSE_Hash_Find` parses as intended |
| V-0006 | `COSE_Hash_Find` vs `COSE_CertHash` | **byte-identical for all eight algorithms** |
| V-0007 | §2.1's length rule executed | a **zero-work collision**, and the CBOR array that prevents it |
| V-0008 | census: what the source does not print | `collision` **15** here, **0** in `rfc-9360` |

## The three results to carry forward

**V-0003 — the hazard the document could have closed in one line.** §3.2's
NOTE is the whole of SHA-256/64's definition: *"SHA-256/64 is a simple
truncation of SHA-256 to 64 bits defined in this specification."* It does not
say which 64 bits, and no test vector pins it. Both candidates are computed
here and they differ, and **the document does not say which**, so two
implementations can both conform and never match. The analogous case is stated
one document away: `rfc-9053` §3.1 — *"When truncating, the leftmost tag-length
bits are kept and transmitted"* — about HMAC 256/64, the same truncation of the
same hash to the same length, in the same registry, by the same working group,
**and RFC 9054 does not cite it**. Our profile takes the leading reading and
cites `rfc-9053` §3.1 for it, which is `R-O-03` applied: the truncation rule
gets **cited**, because RFC 9054 supplies none.

**V-0006 — the two-field digest shape is arrived at twice, by coincidence.**
`COSE_Hash_Find = [ hashAlg : int / tstr, hashValue : bstr ]` and `rfc-9360`'s
`COSE_CertHash = [ hashAlg: (int / tstr), hashValue: bstr ]` differ by one pair
of parentheses that changes nothing, so the same (algorithm, digest) pair
encodes identically under both — verified for all eight algorithms. Same
working group, same author, six months apart, and **neither cites the other's
structure**.

**V-0007 — the one injectivity argument in the lane, and it works.** §2.1 says
additional data must be a fixed known size or carry the lengths of the hashed
pieces *"so that the resulting byte string has a unique interpretation"*, and
adds *"(Encoding as a CBOR array accomplishes this requirement.)"* The vector
exhibits the collision it prevents: `("AB","C")` and `("A","BC")` concatenate
to the same three octets and hash the same, while their CBOR array encodings
differ. That is `canonical-encoding` condition (1), argued in a parenthetical,
lower case, in an Informational RFC — and it is citable.

## What is not here, and why that is the right ceiling

No end-to-end digest-carrier fixture, because **there is no carrier**. §1 says
COSE defines no digested-object structure and that *"This omission was
intentional"*. The two structures §2.1 offers are declared examples, one of
them needs an erratum and a wrapper the document never supplies, and neither is
registered anywhere. A fixture for our own carrier belongs with our own
carrier, not here.

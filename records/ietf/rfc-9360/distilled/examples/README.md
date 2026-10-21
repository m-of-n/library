---
record: rfc-9360
kind: examples
title: "rfc-9360 — examples and test vectors"
extracted: "2026-10-20"
reviewed_by: ""
---

# Examples and test vectors

**RFC 9360 prints no example of any kind, and that is the first result in this
directory.** `Figure`, `Appendix`, `vector` and "test vector" occur **zero**
times in its 614 lines; there is no hex, no base64 and no diagnostic notation
anywhere. For a document whose entire content is wire format — four header
labels, two lines of CDDL, one media type — there is not one COSE object, not
one certificate and not one `x5t` value to take. `rfc-9338`, by the same author
in the same year, carries six figures.

So **every vector here is this extraction's computation**, marked
`source: computed` or `source: derived`, with its `computed_fields` named and
its purpose stated. Nothing is presented as printed.

| vector | what it is | result |
|---|---|---|
| V-0001 | all seven allocated labels, as CBOR | **all seven cost 2 octets**; 8 IANA allocations, 0 tags |
| V-0002 | `COSE_X509` shape conformance, 7 cases | the one-element array and the empty array are **invalid** |
| V-0003 | three framings of one certificate list | for **one** certificate the array and sequence framings are the **same bytes** |
| V-0004 | **filtering vs binding `x5t`** | **byte-identical, 25 octets** |
| V-0005 | `COSE_CertHash` with all eight registered hashes | 11 to 69 octets; the two cheapest are the two `Filter Only` ones |
| V-0006 | **F-3 executed**: the intermediary rewrite | the protected bucket's bytes are **unchanged** |
| V-0007 | census: what the source prints | 13 of 15 terms at **zero** |
| V-0008 | the `hashValue` length non-rule | `[-16, h'']` is **conforming** |

## The two results that are identities, not observations

**V-0004.** `COSE_CertHash` has exactly two fields. `rfc-9054` registers SHA-1
(−14) and SHA-256/64 (−15) as `Recommended: Filter Only`, defined there as
*"not to be used for purposes that require collision resistance"* — and
`Recommended` is a **registry column**, not a wire field. RFC 9360 restricts
`hashAlg` to no subset of the registry. So a sender filtering among
certificates the relying party already holds and a sender integrity-binding an
`x5chain` that arrived in a rewritable bucket emit **the same 25 octets**.
There is no third field in which the purpose could have travelled. That is not
an inference about implementations; it is an equality between two byte strings,
and it is why `../schema/x5t-hashalg-policy.derived.yaml` has to exist.

**V-0003.** A one-item CBOR sequence *is* the item, so for one certificate
`application/cose-x509` and a bare `COSE_X509` are indistinguishable. The only
thing that could disambiguate is the media type's `usage` parameter, which is
optional and whose absence means only *"no further information"*.

## What these fixtures can and cannot test

They test the CBOR layer exactly: shape conformance against the CDDL, the cost
of every code point, the three framings, and the two indistinguishability
results. **They test nothing about DER, path building or trust**, because the
document's own grammar stops where DER starts. §2 line 314: *"The contents of
"bstr" are the bytes of a DER-encoded certificate."* That boundary is the
`DEC-002` finding made concrete — a reduced-CBOR profile does not reach inside
a byte string — and it is why the certificates here are **placeholders that are
not valid X.509**. A fabricated certificate presented as a fixture would be
worse than no fixture: it would invite someone to parse it.

## What a later pass would have to build

A real end-to-end fixture needs a certificate, a key, a signature and a COSE
envelope — i.e. RFC 9052's machinery plus a PKI. The CWT lane in this same
effort did the equivalent for `rfc-8392` because RFC 8392 **printed five
objects to reproduce**. Here there is nothing to reproduce, so the honest
ceiling for pass 1 is conformance and cost, which is what is above. If we ever
accept certificates, the fixtures are ours to author from scratch, and
`../schema/x5-headers.derived.cddl`'s profile section is the specification they
would be written against.

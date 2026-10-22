---
record: rfc-9921
kind: examples
title: "rfc-9921 — examples and test vectors"
extracted: "2026-10-20"
reviewed_by: ""
---

# Examples and test vectors

| file | what it is |
|---|---|
| `vectors.yaml` | 15 vectors, `V-0001`–`V-0015`: every example and worked computation the document prints, plus two derived censuses |
| `a1-ttc-timestamp-token.hex` | Appendix A.1's TimeStampToken, 5453 octets, one line of lower-case hex. `xxd -r -p` gives the DER |
| `a2-ctt-timestamp-token.hex` | Appendix A.2's TimeStampToken, 5453 octets, same form |

## The headline: four digests printed, three reproduce

| vector | what | result |
|---|---|---|
| `V-0002` | §3.1.1, `sha256(0x58 0x40 ‖ signature)` | **reproduces** `44C2419D…` byte for byte |
| `V-0005` | §3.1.2, `sha256(signatures array, 77 octets)` | **reproduces** `803FADA2…` byte for byte |
| `V-0006` | Appendix A.1, `sha256('This is the content.')` | **reproduces** `09E638D4…`, and matches the imprint embedded in the token |
| `V-0011` | Appendix A.2, the CTT request | **does not reproduce.** 207 candidate preimages tried, 0 match |

**Everything that needs no key was verified; nothing that needs one could be.**
A CBOR codec and a DER parser were written for this pass over `hashlib` alone —
no CBOR, COSE, ASN.1, CMS, X.509 or cryptography library was used. Four message
digests, two CMS `messageDigest` attributes, two `ESSCertID` certificate hashes
and every length and offset in both tokens were checked. **Neither COSE
signature can be verified from this document** — the signer's public key appears
nowhere in RFC 9921 and `kid` is the two ASCII octets `'11'` — and **neither
token's RSA signature can be verified either**, because the chain needs a trust
anchor and RFC 5652's rules, and RFC 5652 and RFC 3161 are not in this library.

## Appendix A.2 is not a usable fixture, and the reason is in the bytes

`V-0011` and `V-0012`. A.2 says *the CBOR-encoded signature field is hashed
using SHA-256* and prints `DD 94 71 EF …`. The signature it prints is
byte-identical to §3.1.1's — three printings in the document, three different
hex wraps, one value, checked — and §3.1.1's own rule over that value gives
`44 C2 41 9D …`, which §3.1.1 prints and which reproduces exactly here. The
token A.2 prints **commits to `DD 94 71 EF …` in its own TSTInfo** and is
otherwise internally perfect: the CMS `messageDigest` attribute equals
`sha512` of its eContent, the `signingCertificate` hash equals `sha1` of its
signing certificate, every length is consistent, and the TSA signed it 7
minutes 14 seconds after A.1's with the next-but-one serial number. **So the
request that produced it carried the wrong imprint**, and no edit to the
printed hex can fix the appendix.

**Errata, stated as a result rather than an absence — and UNVERIFIABLE FROM
THIS REPOSITORY.** Pass 2 (2026-10-21) flags everything in this paragraph as
second-hand: the lookup was made from the network on 2026-10-20, no errata
listing is cached beside the source, and a validation run cannot reach
`errata.rfc-editor.org`. Treat the id, status, reporter, date, proposed value,
cause and the RFC 3161 control counts as a citation to re-check, the way
`design-notes.md` §0 treats quotations of `mofn` documents. The mismatch itself
needs no network and is verified above. As recorded:
`errata.rfc-editor.org/rfc9921` returns **one** erratum — **ID 9177, status
REPORTED (not Verified), type Technical, section A.2**, filed 2026-09-13 by
Florent Morselli — proposing `44 C2 41 9D …` and asking for a **newly issued**
token rather than an edit; its notes attribute the printed value to a generator
script hashing an error message after a folded line truncated the signature.
**Positive control:** the same endpoint returns **5** errata for RFC 3161
(1879, 2931, 2932 Verified; 844 Held for Document Update; 4042 Rejected), so an
empty result would have been a result and not a silent failure. The erratum's
*cause* is reported, not verified here. What this pass verifies independently is
that the printed imprint does not match and that `44 C2 41 9D …` does.

## These are not conformance vectors — say so before using them

`V-0015` measures what the two tokens actually are:

- a **public demonstration TSA**: `Free TSA`, `www.freetsa.org`, with a
  `freetsa.org` CPS URL and a CRL distribution point;
- a **placeholder policy OID**: `TSAPolicyId` is `1.2.3.4.1`, an example arc,
  not a real TSA policy;
- a **two-certificate chain that is 75.26 per cent of each token** (4104 of
  5453 octets), against 6.73 per cent for the timestamp assertion itself;
- and a **signing certificate valid 2016-03-13 to 2026-03-11 01:57:39Z**.

**The RFC published in February 2026, so the only fixture it ships had an
expired signing certificate within a month of publication**, and seven months
before this extraction. Nothing in the document flags this, and §5 says nothing
about a TSA certificate's own lifetime.

**What that means for a harness.** Use these bytes for **parsing** and **digest
agreement** — which is what `V-0002`, `V-0005`, `V-0006`, `V-0008` and `V-0012`
do, and all of those are time-independent and will hold forever. **Do not** use
them for path validation, revocation checking or an accept/reject decision:
those now fail for a reason that has nothing to do with RFC 9921, and a harness
that treats the failure as a conformance signal will be debugging 2016's
certificate rather than 2026's specification. A fixture for the acceptance path
has to be minted against a live TSA, and a corrected A.2 would carry a
different chain from A.1's.

## Conventions

- `source: printed` — every byte of every value appears in RFC 9921 itself;
  `reproduced` says what this pass recomputed and whether it matched.
  `source: derived` — every byte is printed by the source, but the **assertion**
  is this extraction's. **Nothing here is computed and presented as printed.**
- `locator` gives the section **and** the exact line range in
  `.cache/rfc-9921.txt`; `region_sha256` is the sha256 of that run of lines
  joined by `\n` with no trailing newline, so any value can be re-cut from the
  source without trusting this file.
- The RFC hard-wraps its hex for display. The only transformation applied is
  joining those lines.
- The source has **zero form feeds** and no running headers or footers, so no
  quoted range can contain page decoration.

---
record: rfc-8392
kind: examples
title: "rfc-8392 — examples and test vectors"
extracted: "2026-10-20"
reviewed_by: ""
---

# Examples and test vectors

**RFC 8392 prints five complete CWTs and all five verify cryptographically.**
That is the result of this pass, and it was closed here rather than deferred:
ECDSA P-256 verification, HMAC-SHA-256 truncated to 64 bits, and AES-128-CCM
with a 13-octet nonce and an 8-octet tag were all implemented for this
extraction over `hashlib` alone. **No CBOR, COSE, CWT, elliptic-curve or AES
library was used**, so a shared library bug cannot hide in the result, and the
AES core was gated on FIPS 197 C.1 (`69c4e0d86a7b0430d8cdb78070b4c55a`) before
it was used for anything.

| vector | what it is | expected result | reproduced? |
|---|---|---|---|
| V-0001 | A.1 claims set, 80 octets | decodes to 7 claims, no tags | yes, and byte-identical after §4.2.1 re-encoding |
| V-0002 | A.2.1 128-bit symmetric key | clean; `kid` 2, `alg` 10 | yes |
| V-0003 | A.2.2 256-bit symmetric key | **two defects**; both errata still *Reported* | yes, mechanically |
| V-0004 | A.2.3 ECDSA P-256 key | on-curve, and `d*G == (x,y)` | yes, both |
| V-0005 | A.3 signed CWT, tag 18 | **the signature verifies** | yes |
| V-0006 | A.4 MACed CWT, `61(17(...))` | **the MAC tag reproduces** | yes |
| V-0007 | A.5 encrypted CWT, tag 16 | **decrypts, CCM tag valid** | yes |
| V-0008 | A.6 nested CWT | **decrypts to the A.3 bytes exactly** | yes |
| V-0009 | A.7 float `iat` | **the MAC tag reproduces** | yes |
| V-0010 | derived: the tag census | 4 of 5 have no tag 61, 0 of 5 untagged | measured |
| V-0011 | derived: the determinism census | 6 of 6 CWT structures ordered, 0 of 3 keys | measured |
| V-0012 | derived: the diagnostic-notation defects | 3 of 9 figures do not parse | measured |

## The correction this directory owes the record's own summary

`summary.md` says *"two of the five Appendix A CWTs are not reproducible from
the printed key without applying two unverified errata"*. **They are
reproducible.** Both MAC tags — A.4's `093101ef6d789200` and A.7's
`b8816f34c0542892` — reproduce exactly from Figure 6's own 32 octets of `k`.

The two errata concern the key's **metadata**, not its key material: erratum
7982 is about the `kid` *label* and 8655 about the `alg` *value*, and nothing in
an HMAC computation reads either. So the finding is narrower and sharper than
the summary made it:

> **[analysis — this extraction's own finding, not a quotation]** A.2.2 is a
> **working** fixture that **fails a conformance check on its own `alg`
> declaration.** As the hex prints it the key declares `alg` 10
> (AES-CCM-16-64-128) and is then used to MAC two objects whose protected
> headers declare `alg` 4, which RFC 9053 §3.1 forbids.

The summary's practical advice stands — prefer A.2.3 and Figure 10 — because
that fixture is self-consistent **as well as** working. Recorded here rather
than edited away in the summary, per the library's convention of recording
falsified wording.

## A source defect this pass found that no erratum covers

**A.6's prose describes a header parameter the figure does not carry.** The
section says *"The content type is set to CWT to indicate that there are
multiple layers of COSE protection before finding the CWT Claims Set."*
Decoded, the object's protected bucket is `{1: 10}` and its unprotected bucket
is `{4: kid, 5: iv}`. **RFC 9052 label 3 — content type — is absent from
both.** So the multi-layer signal in the document's one nested example is
§7.2 step 6's tag check and nothing else. See V-0008 and
`../design-notes.md` defect D-4.

## How to re-cut any value here from the source

Every vector carries its section, its **exact line range** in
`.cache/rfc-8392.txt` and the **sha256 of that run of lines** (the region's
lines joined by `\n`, no trailing newline). The only transformation applied to
a hex block is joining its display line breaks, which A.2 authorises in terms:
*"Line breaks are for display purposes only."* Nothing else is altered, no
value is elided, and **nothing computed is presented as printed** — the three
`source: derived` vectors say so in their own `assertion` and `method` fields.

Page decoration is never inside a quoted range: the region machinery refuses a
range that touches one of the source's 25 five-line page breaks, so no hex run
here can contain a running footer.

## What is not here, and would have to be ours

- **An untagged CWT.** Permitted by §7.2 step 3, printed nowhere. V-0010.
- **An `aud` array.** Permitted by §3.1.3, printed nowhere, and contradicted by
  §4's Table 1 and the §9.1.2 registry entry.
- **A CWT with any claim outside 1-7**, so no fixture exercises §3's
  ignore-the-unknown rule or the Private Use range.
- **A `COSE_Sign` (multi-signature), `COSE_Mac` or `COSE_Encrypt`** — the
  appendix prints only the single-recipient `*0` and `*1` forms, though §7.1
  step 4 and §7.2 step 5 name all six.
- **Any negative fixture at all.** Not one invalid CWT is printed, so §7.2's
  single rejection path has no vector.

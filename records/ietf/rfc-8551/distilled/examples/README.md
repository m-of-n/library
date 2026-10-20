---
record: rfc-8551
kind: examples
title: "rfc-8551 — examples and test vectors"
extracted: "2026-10-19"
reviewed_by: ""
---

# RFC 8551 — examples and test vectors

Pass 1 (extract), examples agent, effort max, working from the source only
(`.cache/rfc-8551.txt`, sha256 `dac39f74…7ed884ae2`, 3531 lines).

`vectors.yaml` holds **47 vectors**:

- **16 in-source.** 7 printed displays, each a verbatim fixture, plus 9
  values printed in prose with a stated meaning.
- **31 constructed.** Each one tests a rule the source states but gives no
  literal for. Every one has a yes/no answer that needs no cryptography,
  and each quotes its rule verbatim and cites its R-ids.

## Fixtures (17)

| file | kind | source lines | what |
|---|---|---|---|
| `3.1.4-canonical-mime-entity.eml` | verbatim | 1409–1437 | §3.1.4 multipart/mixed canonical entity (the source says it is not S/MIME) |
| `3.3-enveloped-data.eml` | verbatim | 1611–1621 | §3.3 application/pkcs7-mime, enveloped-data |
| `3.4-authenveloped-data.eml` | verbatim | 1689–1713 | §3.4 authEnveloped-data |
| `3.5.2-signed-data.eml` | verbatim | 1801–1824 | §3.5.2 signed-data (encapsulated) |
| `3.5.3.3-multipart-signed.eml` | verbatim | 1969–1992 | §3.5.3.3 multipart/signed |
| `3.5.3.3-digested-content.hex` | verbatim | 1997–1998 | the printed digested bytes of the first part |
| `3.6-compressed-data.eml` | verbatim | 2035–2040 | §3.6 compressed-data |
| `3.1.4-image-jpeg-part.derived.hex` | derived | 1432–1435 | decoded image/jpeg part (152 octets) |
| `3.3-enveloped-data.derived.hex` / `.derived.dump.txt` | derived | 1616–1621 | decoded DER (290 octets) and its OpenSSL asn1parse dump |
| `3.4-authenveloped-data.derived.hex` / `.derived.dump.txt` | derived | 1694–1713 | decoded DER (861) and its dump |
| `3.5.2-signed-data.derived.hex` / `.derived.dump.txt` | derived | 1806–1824 | decoded DER (925) and its dump |
| `3.5.3.3-signature.derived.hex` / `.derived.dump.txt` | derived | 1984–1990 | decoded DER (298) and its dump |
| `3.6-compressed-data.derived.hex` | derived | 2040 | decoded body (34 octets; not DER, so no dump) |

An unmarked filename holds the source's own bytes. A `.derived.` filename
was computed by this extraction.

**What was stripped from the verbatim fixtures.** Only the RFC's 3-space
left margin, which every non-blank line of every display carries. Blank
lines are empty in the source. No display crosses a page break, and no
form feed, header, footer or trailing whitespace falls inside any range.
Folded header continuation lines keep the indent left after the margin
is removed. The files have **LF line ends, as printed**, and one LF after
the last line. The source says the real entity uses `<CR><LF>` (§3.1.4,
R-0089, R-0098), so a harness must convert LF to CRLF before parsing or
digesting. No CRLF copy is kept.

**Derived hex** is lowercase, 32 octets per line, made by `sed | cut -c4- |
base64 -d | od -An -tx1 -v -w32 | tr -d ' '`. **Dumps** are the output of `openssl
asn1parse -inform DER -i` (OpenSSL 3.0.13) with one edit: the raw CR LF that
OpenSSL prints inside the 3.5.2 eContent line is written as `\r\n`.

## Verification (mechanical, scratch scripts, not committed)

- All 7 verbatim fixtures are byte-identical to the source lines after
  margin removal. All 6 hex files equal the decoded base64. Every sha256 in
  `vectors.yaml` matches its file. `vectors.yaml` parses (PyYAML), the
  counts in its header match the entries, and the ids are unique.
- All 96 R-ids cited exist in `requirements.yaml`.
- Of the 53 distinct quotes, 52 are verbatim substrings of the
  line-normalised source. The remaining one is the `content-`/`encryption`
  line-break rejoin, the same exception `requirements.yaml` makes.
- Each `.eml`, after LF→CRLF, was parsed with Python `email`. It reported
  no defects, and every header, parameter and part check in the vectors
  holds.
- DER: a strict walker and `openssl asn1parse` agree on 25, 26, 78 and 28
  TLVs. All four bodies are complete DER whose outer length equals the
  decoded length.

Pass 2 (verify, independent) re-ran all of the above from the source: the
fixture diffs, the hex decodes, the four `asn1parse` dumps (identical apart
from the stated `\r\n` edit), `cms -verify` on §3.5.2 with its bit-flip
control, the §3.6 inflate, and the `email` parse. It fixed the key-size
table padding, the §3.2.2-C01 and §3.5.3.2-C02 locators, and the obligation
wording on SHOULD-level results, and it widened S-05.

Pass 3 (cross-check, 2026-10-19) ran every vector against the schema
artifacts and recorded the outcome as `xcheck` on each vector. For a
fixture, each `.eml` (LF→CRLF, Python `email`) is parsed into the JSON
Schema's instance shape and validated with `jsonschema` 4.10.3 at the
root, `#should` and `#identifies`. The raw multipart/signed Content-Type
is matched against the two ABNF rules, hand-translated to regular
expressions because no ABNF tool is installed. The derived hex is walked
as DER and its OIDs and algorithms are compared with the
`algorithm-requirements` sets and key-size rows. The four `asn1parse`
dumps regenerate identically, and `cms -verify -noverify` on §3.5.2
succeeds again. Constructed cases are built as instances where a schema
can express them. The two SMIMECapability encodings were checked against
the module's syntax, with the OID computed from the module's own arcs.
No ASN.1 compiler is installed. Every vector's R-ids exist, and every
`messages` entry exists and carries the vector's R-ids, except
EX-3.1.2-C01 and EX-3.10-C01, which cite no R-id.

Result: all 47 agree, 28 pass and 19 reject as expected. Before the fix
below it was 46 and 1. **EX-3.2.2-01** was the mismatch. A value built by
the source's own guidelines 1 and 3 (`enveloped-OID.2.16.840.1.101.3.4.1.2`)
was warned on by the JSON Schema's `#should`, because that level
restricted smime-type to the five defined values. The source states no
such SHOULD: R-0101 asks only that the parameter be included. The schema
was fixed. No new source defect was found. Every failing check on a source
sample is one of S-01 to S-10.

## Findings (recorded, not repaired)

| id | where | finding |
|---|---|---|
| S-01 | §3.6 | The body is a **bare zlib stream** (`78 da`), not a DER ContentInfo/CompressedData as Steps 2–4 require. It inflates to `This is some sample content.` with no CRLF and no header block. |
| S-02 | §3.5.3.3 | The **messageDigest** (`b1c29646…`) is not SHA-256 of the printed digested bytes (`17a0cf82…`), nor of 9 other readings of part 1. The signature cannot belong to the printed content. |
| S-03 | §3.5.3.3 | The printed digested bytes are text+CRLF. Under RFC 2046, part 1 as printed is CRLF+text (an empty header block, and the CRLF before the boundary belongs to the boundary). Marked ambiguous. |
| S-04 | §3.5.3.3 | SignerInfo **version 2** with an issuerAndSerialNumber sid. RFC 5652 requires 1. External rule. |
| S-05 | §3.5.3.3 | signedAttrs holds messageDigest only, with **no content-type**. RFC 5652 requires both (external rule). It also departs from §2.5's own SHOULDs (R-0027, R-0029: signing time, capabilities, key preference, digest, content type, signingCertificate). §3.5.2 has no signed attributes at all. |
| S-06 | §3.4 | GCMParameters omits aes-ICVlen (DEFAULT 12), but the **mac is 16 octets**. RFC 5084. |
| S-07 | §3.4 | rsaEncryption has **no NULL parameters**, while §3.3's has NULL. RFC 3370 requires NULL. |
| S-08 | §3.3–§3.5.3.3 | The samples use what this document no longer requires or has dropped: 1024-bit RSA, DES-EDE3-CBC, SHA-1, DSA-with-SHA1, 1024-bit DSA. Lines 3455–3457 say some examples were copied from RFC 4134. |
| S-09 | §3.1.4 | The "image/jpeg" part is an **OpenPGP v3 signature packet** (RSA/MD5), confirmed by `gpg --list-packets`. It is illustrative filler. |
| S-10 | §2.5.2 | The sha256WithRSAEncryption capability keeps a NULL that differentiates nothing, against R-0046's "MUST be omitted and MUST NOT be encoded as NULL". Not reconciled in the source. |

Signature results:

- **§3.5.2 verifies.** OpenSSL `cms -verify -noverify` accepts it under the
  included AliceDSS key and rejects a copy with one bit flipped. The chain
  to CarlDSS cannot be built.
- **§3.5.3.3 cannot be verified.** No signer certificate is printed, and
  the digest mismatch (S-02) would defeat it anyway.
- **§3.3 and §3.4 cannot be decrypted.** No private key is printed.

## Not made into vectors, and why

- **§5.1–§5.3 media-type templates and the smime-type registration** are
  IANA registrations. They define registry entries and print no message
  or value to test. Their contents (optional parameters, extension
  pointers) are exercised by `EX-3.2.1-C01` and `EX-3.2.2-C01`.
- **§1.x**: the "e.g." and "for example" uses (§1.1 HTTP/SIP, §1.6
  "e.g., 3.4.3.2", §1.6's note on the updated OID example) name things;
  they are not example values. §1.6 line 551 is cross-checked in
  `EX-3.2.2-01`.
- **§2.5 "e.g."** names attributes. **§3.1** (Subject/To/From/Cc),
  **§3.1.1** (text/plain vs audio/basic), **§3.1.2** (the trusted-gateway
  scenario) and **§6** (attack references, mail list servers) are
  scenarios or names, not values.
- **No case-folding vectors.** The source states no case rule for header
  parameters or smime-type values (that is RFC 2045's).
- **Appendix A** is the schema artifact. Its preferBinaryInside OID is
  used in `EX-2.5.2-C02`.

## Sections with no example

§1.2–§1.5, §2.1, §2.2, §2.4.2–§2.4.5, §2.5.3.1, §2.6, §2.7, §2.7.3, §3.1.2
(beyond C01), §3.7, §3.8 (the source prints no certs-only sample; see
`EX-3.8-C01`), §3.9, §4 and §4.1 (beyond C01), §6 (beyond C01), §7,
Appendix B.1, B.3, B.4, and Appendix C. Their rules are carried in
`requirements.yaml`. They are tested here only through the constructed
vectors listed in `vectors.yaml`.

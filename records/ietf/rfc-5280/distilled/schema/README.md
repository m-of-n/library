---
record: rfc-5280
kind: schema
title: "rfc-5280 — schemas"
extracted: "2026-10-13"
reviewed_by: ""
---

# RFC 5280 — schemas

**Every file here is verbatim.** RFC 5280 publishes its own ASN.1: two
complete modules in Appendix A and the same structures printed inline through
§4 and §5. Nothing in this directory is derived, inferred or written by this
project, except this README. Defects in the ASN.1 are recorded below as
findings. None is repaired in the files.

| file | kind | source | source lines | page breaks removed | lines · bytes | assignments | sha256 |
|---|---|---|---|---|---|---|---|
| `PKIX1Explicit88.asn1` | **verbatim** | Appendix A.1, "Explicitly Tagged Module, 1988 Syntax" | 6129–6954 | 15 | 640 · 23223 | 172 | `94c23a58d3e15a8690c082d5d2e650045b5776b95dd53f2c0bd022350278034d` |
| `PKIX1Implicit88.asn1` | **verbatim** | Appendix A.2, "Implicitly Tagged Module, 1988 Syntax" | 6958–7405 | 8 | 336 · 10804 | 85 | `7295ab9cac5e38eaa03a800196e44475908a663d41aea99fecfc33098d2ce70a` |
| `inline.verbatim.txt` | **verbatim** | the ASN.1 printed inline in §4.1–§5.3.3: 32 regions in 30 sections | see the region table | 3 | — | 114 | per region, below |

Source: `.cache/rfc-5280.txt`, sha256
`a2f2628c0a83b873fc4786abd921f9b2c02395954b655d190bf16b831633345d`, 8459 lines.
This is RFC 5280 as published in May 2008. Later RFCs that update it are not
applied here.

The two `.asn1` files hold **only** the extracted bytes, with no header added.
So `sha256sum` of the file is the digest of the extraction, and the file goes
to an ASN.1 tool unchanged. Each module runs from its module-identifier line
to its `END`. The appendix headings `A.1.` and `A.2.` are left out, because
they are RFC text, not module text. `inline.verbatim.txt` names its source in
its own header. Each region in it has an id (`I-01` … `I-32`), a section, a
line range and its own sha256, and sits between `---- BEGIN VERBATIM I-nn ----`
and `---- END VERBATIM I-nn ----`.

## What the modules are

### Module identifiers

From the module headers (A.1 lines 6129–6132, A.2 lines 6958–6961):

| module | module identifier, as printed | dotted | tag default |
|---|---|---|---|
| `PKIX1Explicit88` | `{ iso(1) identified-organization(3) dod(6) internet(1) security(5) mechanisms(5) pkix(7) id-mod(0) id-pkix1-explicit(18) }` | 1.3.6.1.5.5.7.0.18 | `DEFINITIONS EXPLICIT TAGS ::=` |
| `PKIX1Implicit88` | `{ iso(1) identified-organization(3) dod(6) internet(1) security(5) mechanisms(5) pkix(7) id-mod(0) id-pkix1-implicit(19) }` | 1.3.6.1.5.5.7.0.19 | `DEFINITIONS IMPLICIT TAGS ::=` |

The dotted form is ours, read off the printed arcs. A.1 says
`-- EXPORTS ALL --` and `-- IMPORTS NONE --`. A.2 says `-- EXPORTS ALL --` and
imports twelve names from `PKIX1Explicit88` (lines 6966–6974): `id-pe`,
`id-kp`, `id-qt-unotice`, `id-qt-cps`, `BMPString`, `UTF8String`, `ORAddress`,
`Name`, `RelativeDistinguishedName`, `CertificateSerialNumber`, `Attribute`
and `DirectoryString`. All twelve are defined in A.1, and A.2 uses all twelve.

### X.509 is the origin; these modules are a profile of it

The certificate and CRL formats are ITU-T's, and RFC 5280 profiles them. In
the RFC's own words (quotes are verbatim, with each line break and the indent
after it read as one space):

- §1, lines 196–197: “This specification is one part of a family of
  standards for the X.509 Public Key Infrastructure (PKI) for the Internet.”
- §1, lines 199–200: “This specification profiles the format and semantics of
  certificates and certificate revocation lists (CRLs) for the Internet PKI.”
- §1, lines 212–213: “Section 4 profiles the X.509 version 3 certificate, and
  Section 5 profiles the X.509 version 2 CRL.”
- §3.1, lines 514–516: “ITU-T X.509 (formerly CCITT X.509) or ISO/IEC 9594-8,
  which was first published in 1988 as part of the X.500 directory
  recommendations, defines a standard certificate format [X.509].”
- §4, lines 854–857: “This section presents a profile for public key
  certificates that will foster interoperability and a reusable PKI.  This
  section is based upon the X.509 v3 certificate format and the standard
  certificate extensions defined in [X.509].”
- §4.2.1, lines 1480–1482: “This section identifies standard certificate
  extensions defined in [X.509] for use in the Internet PKI.  Each extension
  is associated with an OID defined in [X.509].”

So these modules are **not** the definitive ASN.1 for X.509. That is the ITU-T
Recommendation, which uses later ASN.1. They are the IETF's 1988-syntax
rendering of the subset it profiles, plus the PKIX private extensions under
`id-pe`. **A citation note for later passes:** RFC 5280 lists `[X.509]` (ITU-T
Rec. X.509 (2005)) under **11.2 Informative References** (line 6068, under the
heading at 5949). The ASN.1 and encoding Recommendations it relies on,
`[X.680]` (5932) and `[X.690]` (5943), are under 11.1 Normative References.

### The 1988 ASN.1 syntax

The modules use the 1988 syntax, with the 1993 string types added, and the RFC
says that the result conforms to neither standard. **This is stated in
Appendix A's preamble and in §1 and §4, not in Appendix B.** Appendix B adds
only the history of UTF8String (quoted below).

- Appendix A, lines 6113–6125: “This appendix describes data objects used by
  conforming PKI components in an "ASN.1-like" syntax.  This syntax is a
  hybrid of the 1988 and 1993 ASN.1 syntaxes.  The 1988 ASN.1 syntax is
  augmented with 1993 UNIVERSAL Types UniversalString, BMPString, and
  UTF8String.” … “As a result, this module does not conform to either version
  of the ASN.1 standard.” … “This appendix may be converted into 1988 ASN.1 by
  replacing the definitions for the UNIVERSAL Types with the 1988 catch-all
  "ANY".”
- §1, lines 215–217: “The profiles are presented in the 1988 Abstract Syntax
  Notation One (ASN.1) rather than the 1997 ASN.1 syntax used in the most
  recent ISO/IEC/ITU-T standards.”
- §4, lines 857–860: “The ISO/IEC and ITU-T documents use the 1997 version of
  ASN.1; while this document uses the 1988 ASN.1 syntax, the encoded
  certificate and standard extensions are equivalent.”

Concretely, A.1 defines `UniversalString ::= [UNIVERSAL 28] IMPLICIT OCTET
STRING`, `BMPString ::= [UNIVERSAL 30] …` and `UTF8String ::= [UNIVERSAL 12] …`
(lines 6143–6151). A.2's IMPORTS clause carries the line `-- delete following
line if "new" types are supported --` before `BMPString, UTF8String,  -- end
"new" types --` (6968–6969). So the RFC expects a reader to edit the modules
for a compiler that knows these types. These are the source's own words. They
are recorded here because they bear on the compile check below.

## Inline regions

The ASN.1 printed inline in §4.1, §4.2.x, §5.1, §5.2.x and §5.3.x is also
normative. A region is a maximal run of ASN.1, from the first `::=` line to its
last ASN.1 or `--` comment line, that no prose interrupts. Regions were found
by script and every boundary was then read against the source. The digest
covers the bytes between the markers.

| id | section | source lines | definitions | sha256 |
|---|---|---|---|---|
| I-01 | §4.1 Basic Certificate Fields | 879–936 | Certificate, TBSCertificate, Version, CertificateSerialNumber, Validity, Time, UniqueIdentifier, SubjectPublicKeyInfo, Extensions, Extension | `2120ae1c97776c0a27170f3f3734681e6f5bd34d26d3686c873703ea42c7f525` |
| I-02 | §4.1.1.2 signatureAlgorithm | 976–978 | AlgorithmIdentifier | `6a8c166e8266e3f86a4ce25c5d4ddf4bcef34d34c3566c67e1fd8b5398f92efc` |
| I-03 | §4.1.2.4 Issuer | 1083–1104 | Name, RDNSequence, RelativeDistinguishedName, AttributeTypeAndValue, AttributeType, AttributeValue, DirectoryString | `dd1f28536af006bd5918f46357767873ad1037b4761b5d7d0fc3ed0ac5622b29` |
| I-04 | §4.2.1 Standard Extensions | 1485 | id-ce | `494f7e49f98fae99e457c43055b31b884ad934ef5929ca4cfbd7088d4e6be04a` |
| I-05 | §4.2.1.1 Authority Key Identifier | 1532–1539 | id-ce-authorityKeyIdentifier, AuthorityKeyIdentifier, KeyIdentifier | `3283ef74c12e2027dc200c663ccecc9b64c00ed84bcb5847c1b6d4aba8ce77ed` |
| I-06 | §4.2.1.2 Subject Key Identifier | 1604–1606 | id-ce-subjectKeyIdentifier, SubjectKeyIdentifier | `da08794533612dba2d89a2a62ad1c4216b9a401553c1a17786e9bca7103de2dd` |
| I-07 | §4.2.1.3 Key Usage | 1636–1648 | id-ce-keyUsage, KeyUsage | `39c2e3ecc101aee5cb31010839c3499024a0b90b2ac472a28dcc62e077f538e7` |
| I-08 | §4.2.1.4 Certificate Policies | 1855–1898 | id-ce-certificatePolicies, anyPolicy, certificatePolicies, PolicyInformation, CertPolicyId, PolicyQualifierInfo, id-qt, id-qt-cps, id-qt-unotice, PolicyQualifierId, Qualifier, CPSuri, UserNotice, NoticeReference, DisplayText | `605987dd9ed8f4b59f7661cfbc8a0f25fbbc9d4dbb821cc62dbd18c698221cf9` |
| I-09 | §4.2.1.5 Policy Mappings | 1947–1951 | id-ce-policyMappings, PolicyMappings | `37153e67fee4a668241fe3d9399c2fa13e592bad931ba0d68c2b667e827ea8e6` |
| I-10 | §4.2.1.6 Subject Alternative Name | 2087–2110 | id-ce-subjectAltName, SubjectAltName, GeneralNames, GeneralName, OtherName, EDIPartyName | `2e1ecc108615e9890b089349f35c9b8e1433d8fb94303a4cd981021fadd8c39a` |
| I-11 | §4.2.1.7 Issuer Alternative Name | 2124–2126 | id-ce-issuerAltName, IssuerAltName | `14e7191682bc30d72411d445cdfb59cbb82f3f46150acfe81fed5f48383753bf` |
| I-12 | §4.2.1.8 Subject Directory Attributes | 2142–2144 | id-ce-subjectDirectoryAttributes, SubjectDirectoryAttributes | `229963e40cc51723f8b567863c56c93637c3878617f86afb0a458418d10ccf2d` |
| I-13 | §4.2.1.9 Basic Constraints | 2198–2202 | id-ce-basicConstraints, BasicConstraints | `9b4fa7ae2cac3af44a0f7354ad6f2129136a1594b0f567f9a77918d4ab1cac29` |
| I-14 | §4.2.1.10 Name Constraints | 2343–2364 | id-ce-nameConstraints, NameConstraints, GeneralSubtrees, GeneralSubtree, BaseDistance | `64a8d2c411cdc240df41ab7e0b56e01d7a0cafb48672a37d0517b14245d48856` |
| I-15 | §4.2.1.11 Policy Constraints | 2415–2421 | id-ce-policyConstraints, PolicyConstraints, SkipCerts | `2ff4dca43a044122915c5dd24d0b1c56db5bc435de491f94ad09ff27ef036902` |
| I-16 | §4.2.1.12 Extended Key Usage | 2431–2435 | id-ce-extKeyUsage, ExtKeyUsageSyntax, KeyPurposeId | `da12647d9118a425b3aa936b5e831c305278da4735657d17cbbf6e7f41fb246d` |
| I-17 | §4.2.1.12 Extended Key Usage | 2480–2511 | anyExtendedKeyUsage, id-kp, id-kp-serverAuth, id-kp-clientAuth, id-kp-codeSigning, id-kp-emailProtection, id-kp-timeStamping, id-kp-OCSPSigning | `d92ba055997026bf2851289aa04fc5e7b5eddd6556b81a676fa5e994e27dcf0b` |
| I-18 | §4.2.1.13 CRL Distribution Points | 2609–2648 | id-ce-cRLDistributionPoints, CRLDistributionPoints, DistributionPoint, DistributionPointName, ReasonFlags | `39227e1a636e833006c2c2457342ef7bc649c72b654adb436366df4b41429b69` |
| I-19 | §4.2.1.14 Inhibit anyPolicy | 2665–2669 | id-ce-inhibitAnyPolicy, InhibitAnyPolicy, SkipCerts | `e06e87c559c58ac3d925a1ff266f5608e874bdcfca0d6362d641477e99834006` |
| I-20 | §4.2.1.15 Freshest CRL | 2681–2683 | id-ce-freshestCRL, FreshestCRL | `27cf4a688eed5ad62f53ae0e8e871e10182ba84fa8358d122e136da4bb26de62` |
| I-21 | §4.2.2 Private Internet Extensions | 2712–2716 | id-pkix, id-pe | `911bb62e8223b67b387928ba5ae8b9761496a437eb8e3b0816a88bb525a0970b` |
| I-22 | §4.2.2.1 Authority Information Access | 2729–2742 | id-pe-authorityInfoAccess, AuthorityInfoAccessSyntax, AccessDescription, id-ad, id-ad-caIssuers, id-ad-ocsp | `18e58940dc7803d57b9c8439bcb6f8f1bd04d7a70eeef156e8c5854ca428dea9` |
| I-23 | §4.2.2.2 Subject Information Access | 2867–2874 | id-pe-subjectInfoAccess, SubjectInfoAccessSyntax, AccessDescription | `8dcab0ee6134c03a31de31a84a5ed4c63941c7b7dc5fc4913696583001fac958` |
| I-24 | §4.2.2.2 Subject Information Access | 2978–2982 | id-ad, id-ad-caRepository, id-ad-timeStamping | `4a9732451bd8afee64a1020c770f7d46465c68b82f1d5a8363a081645d19e077` |
| I-25 | §5.1 CRL Fields | 3087–3112 | CertificateList, TBSCertList | `f0ac4a963256c61e6a9c5b2127ec26a38b8b0cf6f4a74d1997de545ebee03446` |
| I-26 | §5.2.3 CRL Number | 3408–3410 | id-ce-cRLNumber, CRLNumber | `e7937821975b0dd7a67f84824f43c27523f5d7dc093fc88280fd592d1ed90601` |
| I-27 | §5.2.4 Delta CRL Indicator | 3591–3593 | id-ce-deltaCRLIndicator, BaseCRLNumber | `fe3a8e3f76d1e48e8b9138cd809d06289c5baf0279d37f59330a544338e969cb` |
| I-28 | §5.2.5 Issuing Distribution Point | 3678–3689 | id-ce-issuingDistributionPoint, IssuingDistributionPoint | `1555867a9416527f56f4be72251471fb8a66cc8bad7fba1feecfb51cd75155e7` |
| I-29 | §5.2.6 Freshest CRL | 3724–3726 | id-ce-freshestCRL, FreshestCRL | `27cf4a688eed5ad62f53ae0e8e871e10182ba84fa8358d122e136da4bb26de62` |
| I-30 | §5.3.1 Reason Code | 3871–3886 | id-ce-cRLReasons, CRLReason | `e23bafa893b5847810911aaccccb52d430ddc407197b097586b0bae2b23aca02` |
| I-31 | §5.3.2 Invalidity Date | 3905–3907 | id-ce-invalidityDate, InvalidityDate | `4cc29637e6827a0608a46a2f011c5c953b185bd19b262f0cbfac2cd402b27394` |
| I-32 | §5.3.3 Certificate Issuer | 3931–3933 | id-ce-certificateIssuer, CertificateIssuer | `6da0e768c6219fd0d190f4d9e241c3859e14996bcf404cfac733d14e656e65fc` |

I-20 and I-29 have the same digest. Their bytes are identical, because §5.2.6
reprints §4.2.1.15's definition (finding F-06). I-01, I-14 and I-18 each
cross one page break (at 893/903, 2349/2359 and 2620/2639).

**Sections in that range that print no ASN.1:** §4.1.1, §4.1.1.1, §4.1.1.3,
§4.1.2 and §4.1.2.1–§4.1.2.3, §4.1.2.5–§4.1.2.9 (including §4.1.2.5.1 and
§4.1.2.5.2), §4.2, §5, §5.1.1–§5.1.2.7, §5.2, §5.2.1 (CRL authority key
identifier), §5.2.2 (CRL issuer alternative name), §5.2.7 (CRL authority
information access) and §5.3. The three CRL extensions in §5.2.1, §5.2.2 and
§5.2.7 reuse the certificate-extension syntax and print none of their own.
The `-- reasonCode ::= { CRLReason }` line in I-30 (3873) is an ASN.1 comment,
not an assignment.

## Reproducing the extraction

**The furniture rule.** Within a line range, remove three kinds of line:

- every page footer (`Cooper, et al. … Standards Track … [Page n]`);
- every form-feed line (a line that is exactly `\f`);
- every running header (`RFC 5280 … PKIX Certificate and CRL Profile … May 2008`);

and also every empty line that is contiguous with one of them. Insert nothing
in their place. Keep every other line exactly, with its leading spaces, and end
each line with LF. The source has no CR, no tab, no non-ASCII byte, no
whitespace-only line and no trailing whitespace, so nothing else needs
normalising.

**One consequence, stated so that nobody mistakes it for a transcription
error.** There are 26 page joins in the extracted ranges: 15 in A.1, 8 in
A.2, 3 inline. At each one the last line before the break directly abuts the
first line after it. For example, A.1 line 6157 `security(5) mechanisms(5)
pkix(7) }` is followed directly by 6167 `-- PKIX arcs`.

The paginated text does not record whether a blank line stood at a join. The
source pages run 55 lines with at most 48 lines of text, and a page that ends
early is padded with blank lines, so a separating blank line before a break
cannot be told apart from padding. Read by content:

- at **24** joins the break falls between two definitions, or between a
  definition and a comment block. Away from page breaks the modules put a
  blank line between such neighbours; only runs of one-line assignments
  (the `id-at-*`, `id-ad-*`, A.2 `id-kp-*` and `ub-*` lists) are packed
  without one, and no join falls in such a run. A separating blank line very
  probably stood at each of these joins and is not reproduced;
- at **2** joins the break falls inside one construct, so no blank line was
  lost: 893/903 (I-01) splits the TBSCertificate SEQUENCE between
  `issuerUniqueID` and `subjectUniqueID`, and 6942/6951 (A.1) splits one
  comment paragraph mid-sentence.

Restoring the 24 would insert bytes the source does not contain. So the rule
inserts nothing, and the files are verbatim to the source's printed lines.
ASN.1 treats blank lines as whitespace. Every comment here ends at its line
end or at a closing `--`, so no join splits a comment line and no definition
changes.

The joins, as last-line-before/first-line-after:

- A.1: 6157/6167, 6212/6223, 6259/6279, 6307/6335, 6375/6391, 6437/6447,
  6487/6503, 6545/6559, 6599/6615, 6659/6671, 6717/6727, 6774/6783,
  6829/6839, 6885/6895, 6942/6951;
- A.2: 6992/7007, 7051/7063, 7106/7119, 7157/7175, 7215/7231, 7273/7287,
  7327/7343, 7383/7399;
- inline: 893/903 (I-01), 2349/2359 (I-14), 2620/2639 (I-18).

**Script.** Run it from the library root:

```python
# python3 -I extract.py .cache/rfc-5280.txt 6129-6954 6958-7405 879-936 …
import hashlib, re, sys
src = open(sys.argv[1], 'rb').read().split(b'\n')
FURN = re.compile(rb'^(Cooper, et al\. +Standards Track +\[Page \d+\]|\x0c'
                  rb'|RFC 5280 +PKIX Certificate and CRL Profile +May 2008)$')
def extract(a, b):                       # 1-based, inclusive
    ls = src[a-1:b]
    drop = {i for i, l in enumerate(ls) if FURN.match(l)}
    for i in sorted(drop):
        for step in (-1, 1):             # and the blank lines either side
            j = i + step
            while 0 <= j < len(ls) and ls[j] == b'':
                drop.add(j); j += step
    return b''.join(l + b'\n' for i, l in enumerate(ls) if i not in drop)
for spec in sys.argv[2:]:
    a, b = map(int, spec.split('-'))
    print(spec, hashlib.sha256(extract(a, b)).hexdigest())
```

To check a module, compare `extract(6129, 6954)` byte for byte with
`PKIX1Explicit88.asn1`, and `extract(6958, 7405)` with `PKIX1Implicit88.asn1`.
`sha256sum *.asn1` must print the two digests in the file table. To check an
inline region, take the bytes between its markers and compare them with
`extract(a, b)` for the region's range.

**Run in this pass, 2026-10-13. All hold.**

1. The script prints the digests in both tables, for both modules and all 32
   regions, and `sha256sum` of the two `.asn1` files matches.
2. A separate checker, written apart from the extractor, re-derived each file
   and region. It confirmed four things for each: the extracted lines are an
   in-order subsequence of the source range; every source line left out is
   furniture, or an empty line joined to furniture through other removed
   lines; the first and last lines of the range are kept; and each region's
   section label matches the numbered heading above its first line. It
   counted 32 BEGIN markers and 32 END markers.
3. No file here contains a to-do marker (checked with `grep`).

## Cross-comparison: inline against Appendix A

**Method.** This step was mechanical, by script.

1. Strip comments. An ASN.1 comment runs from `--` to the next `--` or to the
   end of the line.
2. Split each text into assignments, one at each line that contains `::=`.
   The first token is the name, and any tokens between the name and `::=` are
   the type of a value assignment.
3. Tokenise the right-hand side and join the tokens with single spaces.
4. Group the assignments by name and compare.

Comments were then compared as a second pass. There are 257 appendix
assignments (172 in A.1, 85 in A.2) and 114 inline ones, giving 260 distinct
names. Two definitions in the two modules never share a name.

| outcome | names |
|---|---|
| inline and appendix agree, ignoring comments and whitespace | 101 |
| inline and appendix differ | 5 |
| inline only | 3 |
| appendix only | 151 |
| printed more than once inline (each also in the appendix) | 5 |

### Findings

Nothing below is repaired in any file. Line numbers are source lines.

**F-01 — The signature component has a different name (Certificate,
CertificateList).**
- Inline, §4.1 line 882 and §5.1 line 3090: `signatureValue       BIT STRING  }`.
- A.1, lines 6487 and 6564: `signature            BIT STRING  }`.

The component name does not appear in DER, so encodings are unaffected. It does
change value notation and any decoded field name. The prose follows the inline
form: §4.1.1.3 is headed `signatureValue` (988), and so is §5.1.1.3 (3155).
Field names in `messages.yaml` and in decoded fixtures should say which form
they use.

**F-02 — EXPLICIT is written inline but left to the module default in A.1
(TBSCertificate, TBSCertList).**
- Inline: `version [0] EXPLICIT Version DEFAULT v1` (885),
  `extensions [3] EXPLICIT Extensions OPTIONAL` (905) and
  `crlExtensions [0] EXPLICIT Extensions OPTIONAL` (3105).
- A.1 (6503–6516, 6566–6580): `[0] Version`, `[3] Extensions`, `[0] Extensions`.

In an `EXPLICIT TAGS` module these are equivalent. The inline text spells the
keyword out because it lives in no module (F-09). The `[1] IMPLICIT` and
`[2] IMPLICIT` on the unique identifiers appear in both.

**F-03 — OtherName and AnotherName (GeneralName).**
- Inline §4.2.1.6: `otherName [0] OtherName` (2094) and
  `OtherName ::= SEQUENCE {…}` (2104–2106).
- A.2: `otherName [0] AnotherName` (7120) and `AnotherName ::= SEQUENCE {…}`
  (7133–7135), with the comment “AnotherName replaces OTHER-NAME ::=
  TYPE-IDENTIFIER, as -- TYPE-IDENTIFIER is not supported in the '88 ASN.1
  syntax” (7130–7131).

The two SEQUENCE bodies are token-identical, so the difference is a rename.
`OtherName` is inline-only and `AnotherName` appendix-only. The other eight
GeneralName alternatives match.

**F-04 — An inline type name begins with a lowercase letter
(certificatePolicies).**
- Inline §4.2.1.4: `certificatePolicies ::= SEQUENCE SIZE (1..MAX) OF
  PolicyInformation` (1859).
- A.2: `CertificatePolicies ::=` (7044), with the same right-hand side.

*Inferred, from X.680, which is outside the source:* a type reference must
begin with an uppercase letter, so the inline line is not a well-formed type
assignment. A.2 is well formed.

**F-05 — Qualifier is defined only inline, and nothing uses it.**
- Inline §4.2.1.4: `Qualifier ::= CHOICE { cPSuri CPSuri, userNotice
  UserNotice }` (1880–1882).

A.2 has no `Qualifier`. Nothing inline or in either module references it,
because `PolicyQualifierInfo.qualifier` is `ANY DEFINED BY policyQualifierId`
in both (1870, 7065). So it documents the two qualifier syntaxes but is not
wired in.

**F-06 — The same definitions are printed more than once inline.** Every
repeat is token-identical to the others and to the appendix. Each module
defines the name once.

| name | inline (region, line) | appendix |
|---|---|---|
| `SkipCerts` | I-15 §4.2.1.11 2421; I-19 §4.2.1.14 2669 | A.2 7200 |
| `AccessDescription` | I-22 §4.2.2.1 2734; I-23 §4.2.2.2 2872 | A.2 7294 |
| `id-ad` | I-22 §4.2.2.1 2738; I-24 §4.2.2.2 2978 | A.1 6175 |
| `id-ce-freshestCRL` | I-20 §4.2.1.15 2681; I-29 §5.2.6 3724 | A.2 7271 |
| `FreshestCRL` | I-20 §4.2.1.15 2683; I-29 §5.2.6 3726 | A.2 7273 |

Within one module a second definition would be an error. The inline text is
not a module, so this is a defect of presentation only. The `id-ce-freshestCRL`
and `FreshestCRL` pair is **new** to the known-defects list.

**F-07 — Some MUST rules appear only in Appendix A comments.** None of these
three has an inline counterpart, either in ASN.1 or in prose (searched for
`authorityCertSerialNumber`, `notBefore or notAfter` and `augment`):
- A.2 6989–6990, after AuthorityKeyIdentifier: “authorityCertIssuer and
  authorityCertSerialNumber MUST both -- be present or both be absent”
  (`rfc-5280#R-0601`). §4.2.1.1 prints the same SEQUENCE (1534–1537) without
  this comment, and its prose never states the pairing rule.
- A.2 7036, in PrivateKeyUsagePeriod: “either notBefore or notAfter MUST be
  present” (`rfc-5280#R-0602`). This applies to an extension the body no
  longer profiles (F-08).
- A.2 7067–7068: “Implementations that recognize additional policy qualifiers
  MUST -- augment the following definition for PolicyQualifierId”
  (`rfc-5280#R-0603`).

Pass 3 should note that the AuthorityKeyIdentifier rule binds even though
§4.2.1.1 does not say it.

**F-08 — Appendix A.2 keeps two extensions that §1 says were removed.**
- `id-ce-privateKeyUsagePeriod` and `PrivateKeyUsagePeriod` (7031–7036).
  §1, lines 264–267: “Section 4.2.1.4 in RFC 3280, which specified the
  privateKeyUsagePeriod certificate extension but deprecated its use, was
  removed.  Use of this ISO standard extension is neither deprecated nor
  recommended for use in the Internet PKI.”
- `id-ce-holdInstructionCode`, `HoldInstructionCode`, `holdInstruction` and
  `id-holdinstruction-none`, `-callissuer`, `-reject` (7365–7383, with `none`
  commented `-- deprecated` at 7379). §1, lines 290–291: “Section 5.3.2 in
  RFC 3280, which specified the holdInstructionCode CRL entry extension, was
  removed.”

**F-09 — No prose states the tagging environment of the inline ASN.1.** The
keywords EXPLICIT and IMPLICIT, in capitals, occur outside the modules only as
tag keywords inside the inline ASN.1 (885, 892, 903, 905, 2106, 3105). The tag default comes only from the module headers. Nine inline
definitions use context tags with no keyword, and each is defined in A.2,
under `IMPLICIT TAGS`. The last row, OtherName, is shown for contrast: its one
tag carries a keyword:

| inline definition | tags with no keyword | lives in |
|---|---|---|
| AuthorityKeyIdentifier (1534) | [0] [1] [2] | A.2 IMPLICIT |
| GeneralName (2093) | [0]–[8] | A.2 IMPLICIT |
| EDIPartyName (2108) | [0] [1] | A.2 IMPLICIT |
| NameConstraints (2345) | [0] [1] | A.2 IMPLICIT |
| GeneralSubtree (2359) | [0] [1] | A.2 IMPLICIT |
| PolicyConstraints (2417) | [0] [1] | A.2 IMPLICIT |
| DistributionPoint (2613) | [0] [1] [2] | A.2 IMPLICIT |
| DistributionPointName (2618) | [0] [1] | A.2 IMPLICIT |
| IssuingDistributionPoint (3680) | [0]–[5] | A.2 IMPLICIT |
| OtherName (2104) | none: `[0] EXPLICIT` | not in either module (F-03) |

TBSCertificate and TBSCertList, which live in A.1, write their keywords out
(F-02). *Inferred, from X.680, which is outside the source and is flagged for
pass 3 and for decoders:* under `IMPLICIT TAGS`, a tag on an untagged CHOICE
or an open type (`ANY`) is still explicit. That makes these tags explicit:

- `GeneralName.directoryName [4] Name` (Name is a CHOICE);
- both `EDIPartyName` components, `[0]` and `[1] DirectoryString` (a CHOICE);
- `DistributionPoint.distributionPoint [0] DistributionPointName` and
  `IssuingDistributionPoint.distributionPoint [0] DistributionPointName`
  (a CHOICE).

The source states none of this. A hand-written DER decoder that takes the tags
as implicit will misparse these fields.

**F-10 — The inline ASN.1 is not self-contained.** Taken alone, the inline
regions reference five names they never define:

- `Attribute`, used by SubjectDirectoryAttributes (2144);
- `ORAddress`, used by GeneralName (2097);
- `UniversalString`, `BMPString` and `UTF8String`, used by DirectoryString
  (1102–1104) and by DisplayText (1897–1898, BMPString and UTF8String only).

All five are defined in A.1. The modules themselves are closed: every type and
value reference resolves inside the module or through A.2's IMPORTS (see
*Compile check*).

**F-11 — Comments differ.** These are comments, so they carry no ASN.1
meaning. The ones that carry content:

- Each inline id-kp purpose in I-17 (2485–2511) carries two comments: what
  the purpose is for, and a list that begins “Key usage bits that may be
  consistent:”. A.2's id-kp lines (7256–7261) carry none.
- `-- value 7 is not used` in CRLReason appears only inline (3883).
- The TBSCertList trailer comments differ. Inline (3109–3112) says “are all
  defined in the ASN.1 in Section 4.1” and “AlgorithmIdentifier is defined in
  Section 4.1.1.2”. A.1 (6582–6583) says “were -- defined earlier for use in the
  certificate structure”.
- The F-07 MUST comments.

The `-- MUST` comments in TBSCertificate and TBSCertList appear in both places
and are already extracted as requirements: R-0004–R-0006 and R-0261–R-0263
inline, R-0594–R-0599 in A.1.

**F-12 — A.1 comments name a type that is defined nowhere.** The comments that
show X.520's parameterised forms use `DirectoryName` at 6251, 6284, 6299,
6341, 6362, 6396 and 6429, for example “--   X520CommonName ::= DirectoryName
(SIZE (1..ub-common-name))”. No module defines `DirectoryName`. The first such
comment, at 6236, uses `DirectoryString`, the type defined at 6475. The
defect is in comments only.

**F-13 — A closing brace follows a terminated comment (parsing hazard).**
A.1 line 6516 reads `-- If present, version MUST be v3 --  }`. The second
`--` ends the comment, so the `}` that closes TBSCertificate is live ASN.1 on
a comment line. The inline form puts the brace on its own line (907). A tool
that reads every `--` as running to the end of the line drops the brace and
fails on A.1.

### Appendix-only names (151)

None of these is printed inline. 141 are in A.1 and 10 in A.2.

- **1993 UNIVERSAL string types defined as tagged OCTET STRING** (A.1
  6143–6151): `UniversalString`, `BMPString`, `UTF8String`.
- **`Attribute`** (A.1 6194). §4.2.1.8 uses it but does not print it (F-10).
- **Naming attributes**, 33 (A.1 6225–6469): `id-at` and the `id-at-*` OIDs
  for name, surname, givenName, initials, generationQualifier, commonName,
  localityName, stateOrProvinceName, organizationName, organizationalUnitName,
  title, dnQualifier, countryName, serialNumber and pseudonym, with their
  `X520*` syntaxes; `id-domainComponent`, `DomainComponent`, `pkcs-9`,
  `id-emailAddress`, `EmailAddress` and `DistinguishedName`.
- **The ORAddress family**, 67 (A.1 6594–6881): `ORAddress`,
  `BuiltInStandardAttributes` and its components, the
  `BuiltInDomainDefinedAttributes`, and the `ExtensionAttributes` with each
  lowercase extension-attribute value and its type, from `common-name` to
  `TeletexDomainDefinedAttribute`.
- **Upper bounds**, 37 (A.1 6900–6936): `ub-name` to `ub-x121-address-length`.
  The comment at 6895 says “specifications of Upper Bounds MUST be regarded as
  mandatory” (`rfc-5280#R-0600`).
- **A.2**, 10: `id-ce-privateKeyUsagePeriod`, `PrivateKeyUsagePeriod` (F-08);
  `CertificatePolicies` (F-04); `AnotherName` (F-03); and
  `id-ce-holdInstructionCode`, `HoldInstructionCode`, `holdInstruction`,
  `id-holdinstruction-none`, `id-holdinstruction-callissuer`,
  `id-holdinstruction-reject` (F-08).

### Inline-only names (3)

`certificatePolicies` (F-04), `Qualifier` (F-05), `OtherName` (F-03).

## Compile check

**No ASN.1 compiler is available offline here, and nothing was installed.**
Checked:

- `asn1c`: not on PATH;
- Python `asn1tools`, `pyasn1`, `pycrate` and `asn1crypto`: not importable;
- no Erlang `erlc`, and no ASN.1 compiler jar for the installed `java`.

`openssl` is present, but `openssl asn1parse` dumps DER and does not compile
modules. Python `cryptography` 41.0.7 is present: it is an X.509 parser, not a
schema compiler. **So the modules have not been compiled.**

What was checked instead, mechanically, by the same assignment parser as the
cross-comparison:

- every `::=` line outside a comment in both modules parses as a type or value
  assignment: 172 in A.1 and 85 in A.2;
- **reference closure:** every type and value reference resolves, within the
  module or through A.2's IMPORTS. Not counted as references are OID name
  forms such as `dod(6)`, `DEFINED BY` component references and named-number
  DEFAULTs such as `v1`. Zero references are left undefined in A.1 and zero in
  A.2.

A real compiler will still need the edits the RFC itself anticipates: the
UNIVERSAL redefinitions in A.1, and the IMPORTS line A.2 says to delete
(*The 1988 ASN.1 syntax*, above). It may also trip on F-13. Pass 2 or pass 3
should compile both modules if a compiler becomes available, and record any
error against these findings rather than editing the files.

## Appendix B: notes that bear on parsing and encoding

Quoted verbatim, with each line break and the indent after it read as one
space. Each quote names the requirement id it is extracted as.

- **DER and serial numbers** (7409–7413, R-0604): “CAs MUST force the
  serialNumber to be a non-negative integer, that is, the sign bit in the DER
  encoding of the INTEGER value MUST be zero.  This can be done by adding a
  leading (leftmost) `00'H octet if necessary.” See also §4.1 (874–877): “For
  signature calculation, the data that is to be signed is encoded using the
  ASN.1 distinguished encoding rules (DER) [X.690].”
- **Integer sizes** (7416–7418, R-0605, R-0606): “Certificate users MUST be
  able to handle serialNumber values up to 20 octets in length.  Conforming
  CAs MUST NOT use serialNumber values longer than 20 octets.” And
  (7421–7423, R-0607, R-0608): “CRL validators MUST be able to handle
  cRLNumber values up to 20 octets in length.  Conforming CRL issuers MUST NOT
  use cRLNumber values longer than 20 octets.”
- **SIZE (1..MAX)** (7427–7430): “The SIZE (1..MAX) construct constrains the
  sequence to have at least one entry.  MAX indicates that the upper bound is
  unspecified.  Implementations are free to choose an upper bound that suits
  their environment.”
- **PrintableString** (7437–7444, R-0609, R-0610): “Implementers should note
  that the at sign ('@') and underscore ('_') characters are not supported by
  the ASN.1 type PrintableString.” … “Conforming implementations MUST NOT
  encode strings that include either the at sign or underscore character as
  PrintableString.”
- **Named bit lists** (7464–7466, R-0611): “When DER encoding a named bit
  list, trailing zeros MUST be omitted.  That is, the encoded value ends with
  the last named bit that is set to one.” This applies to KeyUsage and
  ReasonFlags (I-07, I-18).
- **UTF8String** (7472–7477): “The character string type UTF8String was
  introduced in the 1997 version of ASN.1, and UTF8String was added to the
  list of choices for DirectoryString in the 2001 version of [X.520].
  UTF8String is a universal type and has been assigned tag number 12.  The
  content of UTF8String was defined by RFC 2044 and updated in RFC 2279, which
  was updated in [RFC3629].” This matches A.1's `UTF8String ::= [UNIVERSAL 12]
  IMPLICIT OCTET STRING` (6150).
- **The expanded DirectoryString** (7492–7495): “In Appendix A, in order to
  avoid the use of parameterized type definitions, the DirectoryString type is
  written in its expanded form for the definition of each of these attribute
  types.” This is why the `X520*` types in A.1 are CHOICEs, not
  `DirectoryString`.
- **DER: SET OF ordering and DEFAULT omission** (7511–7519): “Implementers
  should note that the DER encoding of the SET OF values requires ordering of
  the encodings of the values.  In particular, this issue arises with respect
  to distinguished names.” And: “Implementers should note that the DER
  encoding of SET or SEQUENCE components whose value is the DEFAULT omit the
  component from the encoded certificate or CRL.  For example, a
  BasicConstraints extension whose cA value is FALSE would omit the cA boolean
  from the encoded certificate.”
- **OID limits** (7524–7534, R-0612–R-0616): “This specification mandates
  support for OIDs that have arc elements with values that are less than 2^28,
  that is, they MUST be between 0 and 268,435,455, inclusive.” …
  “Implementations MUST be able to handle OIDs with up to 20 elements
  (inclusive).”
- **Encoding inside nameConstraints** (7542–7547, R-0617, R-0618): “The
  content-specific rules for encoding values in the nameConstraints extension
  are specified in Section 4.2.1.10, and these rules may not conform to the
  rules for the underlying type.  For example, when the
  uniformResourceIdentifier field appears in a nameConstraints extension, it
  must hold a DNS name (e.g., "host.example.com" or ".example.com") rather
  than a URI.” The ASN.1 type of a GeneralName alternative therefore does not
  settle its content rule.
- **Unknown elements and extensions** (7555–7580, R-0619–R-0623): “If unknown
  elements appear within an extension, and the extension is not marked as
  critical, those unknown elements ought to be ignored, as follows:”
  - “(a) ignore all unknown bit name assignments within a bit string;”
  - “(b) ignore all unknown named numbers in an ENUMERATED type or INTEGER
    type that is being used in the enumerated style, provided the number
    occurs as an optional element of a SET or SEQUENCE; and”
  - “(c) ignore all unknown elements in SETs, at the end of SEQUENCEs, or in
    CHOICEs where the CHOICE is itself an optional element of a SET or
    SEQUENCE.”
  - “If an extension containing unexpected values is marked as critical, the
    implementation MUST reject the certificate or CRL containing the
    unrecognized extension.”

  So a decoder for non-critical extensions must accept trailing SEQUENCE
  elements, extra bits and unknown enumerations that the 1988 modules, which
  have no extension markers, do not admit. A strict schema decode is the wrong
  test for those. Appendix B also says why (7552–7555): “at least two
  extension definitions included in [RFC2459], the predecessor to this profile
  document, have different ASN.1 definitions in this specification, but the
  same OID is used.”

## Why there is no derived JSON Schema

This pass adds none. The ASN.1 is the complete formal schema, and the source
prints it twice. A JSON Schema for decoded certificates would describe a
decoded *shape*, and that shape is set by how the examples artifact renders
its fixtures. This pass did not see that format. Writing the schema now would
make a second description to keep in sync with both.

For pass 3, which validates the Appendix C examples:

- the authoritative check is a DER decode of each example against
  `PKIX1Explicit88` and `PKIX1Implicit88`;
- with no compiler offline, `cryptography` 41.0.7, which is installed, can at
  least decode the examples as certificates and CRLs;
- a derived schema can be added then, marked `derived`, if the fixtures need
  one. It should take its field names from F-01, use the tagging of F-09, and
  allow unknown elements in non-critical extensions as Appendix B (a)–(c)
  says.

## Source defects for design-notes

Already in the shared list: SkipCerts, AccessDescription and id-ad printed
twice (F-06), and the MUSTs inside ASN.1 comments (F-07, F-11).

**New in this pass:**

- F-01, the signature/signatureValue component name;
- F-03, the OtherName/AnotherName rename;
- F-04, the lowercase `certificatePolicies`;
- F-05, the orphan `Qualifier`;
- F-06, `id-ce-freshestCRL` and `FreshestCRL` printed twice;
- F-07, the AuthorityKeyIdentifier pairing MUST that only A.2 states;
- F-08, the removed extensions still in A.2;
- F-09, the unstated inline tagging environment, with the inferred
  CHOICE-tagging consequence;
- F-10, the inline ASN.1 not being self-contained;
- F-12, the comment-only `DirectoryName`;
- F-13, the brace after a terminated comment;
- `[X.509]` cited only informatively.

## Pass 2 (verify)

- Both modules and all 32 inline regions re-extracted with a separate script (page breaks found from the form feed, not from a footer pattern): byte-identical to the files; every sha256, line range and byte count in the two tables matches; 15, 8 and 3 page joins found, the same 26 listed. No fix to any `.asn1` or `inline.verbatim.txt` byte.
- Completeness: every source line before Appendix A that contains `::=` (115, one of them the `-- reasonCode` comment) lies in a region, and no region boundary drops an adjacent ASN.1 or comment line.
- Cross-comparison re-run with an independent parser: 114 / 172 / 85 assignments, 260 names, 101 agree, 5 differ, 3 inline-only, 151 appendix-only (141 A.1, 10 A.2), 5 repeated; the 5 undefined inline names confirmed. F-01 to F-08, F-10, F-12, F-13 confirmed against the source with no change.
- Page-join paragraph: said a real separating blank line was removed at each of the 26 joins and that no join falls inside a comment. Corrected: 24 joins very probably lost one, 2 (893/903, 6942/6951) did not, and 6942/6951 does fall inside a comment paragraph.
- F-09: "Ten inline definitions use context tags with no keyword" → nine; the OtherName row is a contrast row.
- F-11: the id-kp comments do not all begin "Key usage bits…"; reworded.

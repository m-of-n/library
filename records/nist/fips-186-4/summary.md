---
schema: "library-summary/v1"
id: fips-186-4
record: fips-186-4
type: summary
updated: "2026-11-01"
---

# Digital Signature Standard (DSS), FIPS 186-4

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `historic` — **withdrawn 2024-02-03**, superseded in its entirety by FIPS 186-5 (PDF cover page; CSRC) |
| **Authors** | National Institute of Standards and Technology |
| **Published** | 2013-07-19. Supersedes FIPS 186-3 |
| **Identifier** | FIPS 186-4 · DOI 10.6028/NIST.FIPS.186-4 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf |
| **Digest** | `sha256:081dcccbcd8a1ffe4b5cca7b30dcedb739910e65b39e6182a3cdbae3e5f61689` (retrieved 2026-11-01). These bytes are the 2024 reissue with a withdrawal cover, 131 PDF pages, not the 2013 file |

## Overview

Approves three signature techniques for US federal use. DSA is specified here in
full; RSA (ANS X9.31 and PKCS #1 v2.1) and ECDSA (ANS X9.62-2005) are specified
elsewhere and adopted with added constraints on key generation, hash choice and
randomness (§1, §5, §6). Appendices supply domain-parameter and key-generation
methods and fifteen recommended curves: five prime, five binary and five Koblitz
(Appendix D).

Its lasting argument is the line it draws between **verification** and
**validation** (§3, §3.3). Mathematical verification shows only that a key checks
a signature over some data. Before accepting a signature the verifier also needs
assurance of the claimed identity, domain parameters, public key validity, and
the signatory's possession of the private key. §3 says plainly that without the
identity assurance, integrity is established but source authentication is not.

**For current work cite `fips-186-5`**, which per that record retires DSA for new
signatures and adds EdDSA. This record exists for signatures and keys made under
186-4, and for the lineage.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The rules behind a large installed base of signatures |
| Cryptography | `core` | Normative for these schemes in their time. Withdrawn now |
| This project | `adjacent` | Bears on no open `DEC-*`. It frames R-M-02 and adds nothing to the algorithm suite |

**R-M-02** (a principal may be identified solely by key or key digest). The
topic asks what approval settles for a principal named by its key, and this
document's answer is: less than one might assume. Its model has an owner distinct
from the key, and it requires a binding between them (§3, §4.4.2 items 8 to 10). A
key-named principal removes that gap by definition rather than meeting the
requirement, so approval of the algorithm says nothing about who the principal
is. The public-key-validity and possession assurances still apply in full. The
single-purpose rules also apply: a signature key pair is not for other purposes
(§3), and an RSA pair serves one scheme only (§5.1).

## Implementations

No search was run for this record. The live list is on `fips-186-5`. The one row
below is the DSA documentation checked on 2026-11-01.

| Name | Kind | License | URL |
|---|---|---|---|
| python-cryptography, which documents DSA as legacy | open source | Apache-2.0/BSD | https://cryptography.io/en/stable/hazmat/primitives/asymmetric/dsa/ |

Commercial: not searched. CMVP status of any given module was not checked.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata and typed relations |
| `summary.md` | this document |

No `distilled/`. Nothing justifies extracting a withdrawn standard; extraction of
this family belongs on `fips-186-5`, and no issue owns this record's extraction.
No `distilled/normative.md` exists, so this summary cites sections only.

## Limits

- **Withdrawn.** It supports no new conformance claim.
- **RSA and ECDSA are not here.** The signature algorithms are in X9.31, PKCS #1
  and X9.62, which are not held, and methods for the assurances are in SP 800-89,
  also not held. This document settles constraints on them, not their mechanics.
- **No signature encoding.** It defines (r, s) as integers and says nothing about
  a wire form, so it gives no help with signature malleability or canonical form.
- **Randomness is load-bearing.** DSA and ECDSA take a new secret k per message
  (§4.5, §6.3). Both methods offered draw on an RBG (B.2, B.5), though each section
  allows another approved method. Nothing here specifies deterministic signing.
- **The security floor is dated.** It admits L=1024 and nlen=1024 (§4.2, §5.1) and
  the recommended curves were generated with SHA-1 (footnote 2, Appendix D).
  Binary and Koblitz curves are still listed.
- **Non-repudiation is claimed, and conditional.** The abstract claims it, while
  item 15 says conformance does not assure a secure implementation, and the
  same item rests security on signatories keeping private keys secret.
- **Invalid is softer than valid.** A failed verification or assurance "should" be
  considered invalid while success "shall" be considered valid (§3.3), and the
  response is left to organisational policy. Timeliness is left to SP 800-102.
- **Source defect.** D.1.1.2 refers to Table E-1, but the table is labelled D-1.
- **Read scope:** read from text extracted from the PDF with pypdf, which loses
  superscripts and some mathematical layout. Front matter, §§1 to 6 and Appendices
  A to G were read. Curve constants and the D.9 and D.10 conversion rows were
  filtered out and not reviewed. No algorithm was checked against an implementation.

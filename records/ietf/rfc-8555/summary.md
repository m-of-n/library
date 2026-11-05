---
schema: "library-summary/v1"
id: rfc-8555
record: rfc-8555
type: summary
updated: "2026-11-04"
---

# Automatic Certificate Management Environment (ACME)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, per RFC Editor metadata |
| **Authors** | R. Barnes, J. Hoffman-Andrews, D. McCarney, J. Kasten |
| **Published** | March 2019 |
| **Identifier** | RFC 8555, DOI 10.17487/RFC8555 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8555.txt |
| **Digest** | `sha256:a40983bb…` (full value in `record.yaml`), fetched 2026-11-01, rechecked 2026-11-04 |
| **Errata** | 23 reports: 12 Verified (6 Technical), 6 Held for Document Update, 3 Reported, 2 Rejected; counted 2026-11-04, not read |

## Overview

ACME replaces ad hoc, human-driven certificate issuance with a protocol. §1 reports that, in the authors' informal usability tests, webmasters often needed one to three hours to obtain and install a certificate. An account key signs JSON messages over HTTPS; the client creates an order, proves control of the identifier by answering an HTTP or DNS challenge (§8.3, §8.4), then gets the certificate (§4). Renewal is a new order (§7.4.2), and key rollover and revocation fit the same flow (§7.3.5, §7.6). The point of §2 is the operator's experience: a CA-issued certificate becomes nearly as easy to deploy as a self-signed one, with minimal manual upkeep. That is its importance to this topic: it removed X.509's human issuance step.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Domain-validation issuance with a stated threat model (§10) |
| Cryptography | `adjacent` | Uses JWS account keys; defines no primitive |
| This project | `adjacent` | Shows what zero marginal issuance cost does for adoption |

It bears on no open `DEC-*` or `R-*`. It is evidence for mofn R-001 §5.7(e), that X.509 removed the incentive to switch from inside, and, by our reading, for condition C1 of R-0004 §7, which does not cite it. `R-O-02` is not listed: the RFC never speaks of short-lived validity.

## Relations

- `see_also: rfc-5280`: ACME issues certificates under this profile (§1; identifiers are encoded per its §7, §7.1.4).
- `see_also: rfc-6960`: §2's operator flow fetches stapled OCSP responses, and a §7.6 revocation request's reason code is what the server uses when it generates OCSP responses and CRLs.
- `rfc-9162` was dropped: the RFC never mentions Certificate Transparency; the pairing is R-001 §5.7(e)'s, not this document's.

## Implementations

Searched 2026-11-01; licences checked 2026-11-04. The Let's Encrypt client page lists many ACMEv2 clients and recommends Certbot.

| Name | Kind | License | URL |
|---|---|---|---|
| Certbot | client | Apache-2.0, per its LICENSE.txt (nginx plugin portions MIT) | https://github.com/certbot/certbot |
| Boulder | CA server (Let's Encrypt) | MPL-2.0, per GitHub | https://github.com/letsencrypt/boulder |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this file |

No `distilled/`: a summary-bar fill, not an extraction. FX-1 would apply to this `rfc` record if extracted; no issue owns that (#89's list does not include it).

## Limits

Read: §§1-4, the §7.1 resource list, the opening of §8 and of §10.1-10.2, from the .txt. §§5-6 (transport), §7's object and flow detail, §8.1-8.4 and §9 were read by heading only, so no message format or normative statement is reproduced here.

It settles issuance only. It says nothing about which CAs a relying party trusts, and it validates identifiers rather than people (§8), so it does not answer `ellison-schneier-2000-ten-risks`. It is one cause among several: that ACME "made issuance free" is mofn R-001's claim; the RFC discusses payment only as something a client might prompt for (§2). Actual adoption figures are not in this document.

---
schema: "library-summary/v1"
id: ellison-schneier-2000-ten-risks
record: ellison-schneier-2000-ten-risks
type: summary
updated: "2026-11-04"
---

# Ten Risks of PKI: What You're not Being Told about Public Key Infrastructure

|  |  |
|---|---|
| **Type** | paper (journal essay) |
| **Maturity** | `white-paper`: an opinion essay, not peer-reviewed research as far as the text shows |
| **Authors** | Carl Ellison, Bruce Schneier |
| **Published** | 2000, Computer Security Journal XVI(1) |
| **Identifier** | https://www.schneier.com/academic/paperfiles/paper-pki.pdf |
| **Source** | https://www.schneier.com/academic/paperfiles/paper-pki.pdf |
| **Digest** | `sha256:d400646f…` (full value in `record.yaml`), fetched 2026-11-01, rechecked 2026-11-04 |

## Overview

Sceptical of vendor claims that a PKI is needed for e-commerce, Ellison and Schneier list ten risks in CA-based systems, most of them not cryptographic. "Trusted" only means a CA guards its own key, not that its certificates mean anything for your purpose (Risk 1). Names do not identify people at scale (Risk 4). SSL CAs are not authorities on DNS names or corporate names (Risk 5), and users cannot check what a certificate covers (Risks 6, 9). The closing argument is about markets: busy buyers want a minimal-impact fix, and vendors sell them one (Risk 10).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Threat analysis of the CA trust model |
| Cryptography | `adjacent` | Keys and revocation appear, but the argument is about process |
| This project | `adjacent` | Motivates separating names from authorizations, and limiting X.509 imports |

`R-M-04`: Risk 1 attacks using an ID certificate as if it implied authorization, which is the split that requirement makes. `R-I-05`: Risk 1 (an ID certificate carries a name, not an authorization) and Risk 5 (an SSL CA is not an authority on the DNS or corporate name it certifies) support importing X.509 only as a foreign identity assertion about a key. mofn R-001 §5.7(e) and R-0004 §4.3 also quote its $5 certificate passage on CA economics (p.1).

## Relations

- `see_also: rfc-2693`: Ellison is an author of SPKI Certificate Theory, the authorization-certificate design this essay does not name but argues toward (Risk 1).
- `see_also: sdsi-1-1`: Risk 4 ("Which John Robinson is he?") is the global-name problem SDSI's local names answer.
- The `gutmann-2002-pki-not-dead` edge is authored on that record. `rfc-5280` was dropped: the essay predates it and argues about CA practice, not the profile.

## Implementations

None applicable: an essay. Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this file |

No `distilled/`: a summary-bar fill, and a `paper` record is outside FX-1 scope.

## Limits

Read whole, all 8 pages, from the PDF on Schneier's site. Page 8 is only a CSI Roundtable footer. The Figure "Problems of Authentication" on p.5 came through as extracted text, not as an image.

It is an essay, and it offers no measurements; "Most are very weak" (Risk 2, p.2) has no citation. Several risks apply to any key-centric design, including SPKI and mofn: key storage (Risk 2) and the verifying computer (Risk 3) are not X.509 problems. Risk 10's single sign-on argument is about CA deployment projects and has dated. The essay does not propose an alternative, though Ellison was an SPKI author (`rfc-2693`).

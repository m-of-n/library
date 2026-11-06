---
schema: "library-summary/v1"
id: keys-openpgp-org-faq
record: keys-openpgp-org-faq
type: summary
updated: "2026-11-04"
---

# keys.openpgp.org FAQ: third-party certification policy

|  |  |
|---|---|
| **Type** | web (operator FAQ) |
| **Maturity** | `informational`: an operator's policy page |
| **Authors** | keys.openpgp.org operators (not named on the page) |
| **Published** | Undated living page; retrieved 2026-11-01 |
| **Identifier** | https://keys.openpgp.org/about/faq |
| **Source** | https://keys.openpgp.org/about/faq |
| **Digest** | `sha256:34da28f0…` (full value in `record.yaml`), fetched 2026-11-01, rechecked 2026-11-04 |

## Overview

The replacement keyserver explains why it is not an SKS server. By default it does not distribute third-party certifications, the signatures behind the web of trust, and names spam as the reason ("The killer reason is spam"): they let anyone attach data to anyone's key. The exception is an "attested certification", which the key holder marks and adds locally. Identity data is published only with consent proved by email, one key per address, and search is by exact address. It refuses to certify keys after verification: it is for distribution, "not as a de facto certification authority". On this server, that ends default distribution of the web of trust's signatures by design.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A deployed answer to the third-party-signature abuse problem |
| Cryptography | `adjacent` | Consequence of OpenPGP certificate structure, no new crypto |
| This project | `adjacent` | Shows a subject must consent to what is attached to it |

`R-I-04`: importing OpenPGP signatures now depends on a channel that omits most of them by default, unless the key holder attests. The design lesson goes further than that requirement: third-party statements that can attach to a subject unilaterally are an attack surface.

## Relations

- `see_also: ulrich-2011-openpgp-wot`: the measured reach of the web of trust whose certifications this server stops distributing by default.
- `see_also: rfc-9580`: the FAQ's "attested certifications" correspond to signature subpacket 37, which RFC 9580's subpacket table (§5.2.3.7) lists only as reserved for Attested Certifications, with no definition; the mechanism this server relies on is not in the current OpenPGP standard.
- The `cve-2019-13050` edge is authored on that record.

## Implementations

Searched 2026-11-01; licence rechecked 2026-11-04. The FAQ names Hagrid as the server software. Its README says it is built and maintained only for the service at keys.openpgp.org, not as deployable software.

| Name | Kind | License | URL |
|---|---|---|---|
| Hagrid | keyserver | AGPL-3.0-or-later, per its README; GitLab metadata reports AGPL-3.0 | https://gitlab.com/keys.openpgp.org/hagrid |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this file |

No `distilled/`: a summary-bar fill, and a `web` record is outside FX-1 scope.

## Limits

Read whole, live page, retrieved 2026-11-01. It is the operator's own account, undated, and policy may change without notice. It gives no numbers, so it does not show how many keys or users moved, and does not establish that the web of trust is dead; mofn R-001 §5.2's "deliberately shut off" is our reading. It also records a disagreement with GnuPG over keys without identity: GnuPG rejected the server team's patch as "Wontfix" in March 2020 (issue T4393, not followed up). Distribution of revocations remains an open problem by its own account.

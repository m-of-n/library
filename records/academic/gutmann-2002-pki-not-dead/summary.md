---
schema: "library-summary/v1"
id: gutmann-2002-pki-not-dead
record: gutmann-2002-pki-not-dead
type: summary
updated: "2026-11-04"
---

# PKI: It's Not Dead, Just Resting

|  |  |
|---|---|
| **Type** | paper. **Extended version read, not the IEEE Computer article** |
| **Maturity** | `white-paper`: the extended version is a self-published paper |
| **Authors** | Peter Gutmann (University of Auckland) |
| **Published** | August 2002, IEEE Computer 35(8). Copy read generated 2006-11-06 |
| **Identifier** | DOI 10.1109/MC.2002.1023787 |
| **Source** | https://www.cs.auckland.ac.nz/~pgut001/pubs/notdead.pdf |
| **Digest** | `sha256:862bd5a7…` (full value in `record.yaml`), fetched 2026-11-01, rechecked 2026-11-04 |

## Overview

Gutmann argues that general-purpose X.509 identity PKI failed to appear because it inherited a design for X.500 directory access control, and that real problems want application-specific certificates. X.509 fails on the "Which directory?" and "Which John Smith?" problems (§2.3), and revocation by blacklist asks the wrong question, "Has this been revoked?" rather than "Is this currently valid?" (§3.4). Economics make this worse: nobody pays for CRLs, and per-use fees deter use (§3.1). His recommendations are locally meaningful plus key-derived identifiers (§6.1), designing revocation out (§6.2), and scoped PKIs (§6.3). SPKI is his recurring positive example.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Failure analysis of revocation, chains and root stores |
| Cryptography | `adjacent` | Cites authenticated dictionaries, but the argument is architectural |
| This project | `core` | Argues for the local names and short-lived validity that mofn adopted |

`R-O-02`: §3.2 and §6.2 argue for freshness over revocation, and §3.2 records the objection that short-lived certificates do not fully remove revocation. `R-M-03`: §2.3 and §6.1 reject global names for identifiers meaningful within a domain; his domain is a community or application, not an issuing principal, so this supports the rationale of R-M-03 rather than its exact rule. `R-M-01`: §2.1-2.3 on why X.509's model does not fit authorization.

## Relations

- `see_also: ellison-schneier-2000-ten-risks`: the earlier critique of CA-based PKI on the same grounds (names, authority, revocation); the edge is authored here only.
- `see_also: rfc-2693`: cited as [19]; SPKI is the paper's recurring positive example (§2.2, §3.4, §6.3).
- `see_also: rfc-6960`: §3.3-3.4 critique OCSP as RFC 2560 ([45]), which RFC 6960 obsoletes.
- `see_also: itu-x509`: the standard whose X.500 directory origins §2.1 analyses (cited as the 1993 X.509 v2, [12]).
- `rfc-5280` was dropped: the paper argues against the X.509 model, not the PKIX profile, and `itu-x509` already carries that link.

## Implementations

None applicable: an analysis paper. Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this file |

No `distilled/`: a summary-bar fill, and a `paper` record is outside FX-1 scope.

## Limits

**The published article was not read.** Read whole: the body of the author's extended version, 19 pages, from his Auckland site. The reference list was only sampled; it cites Wang et al., ESORICS 2006 ([15]), so the copy is no earlier than September 2006. The text is later than 2002, so nothing here may be cited as what the August 2002 article says without checking it. Its own §6.3 says the web of trust's real-world effectiveness is uncertain and gives no measurement; see `ulrich-2011-openpgp-wot`.

It praises SPKI's design without addressing why SPKI was not deployed, so it cannot be cited as evidence that SPKI worked. The cost figures (GSA 40¢ to $1.20 per use, the Johnson and Johnson CRL) are secondary citations we did not trace. mofn R-001's quotation of the opening is lightly reworded from this copy ("was access control", with `[which]`); check it against the IEEE text.

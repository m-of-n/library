---
schema: "library-summary/v1"
id: wang-2006-reducing-spki
record: wang-2006-reducing-spki
type: summary
updated: "2026-11-01"
---

# Reducing the Dependence of SPKI/SDSI on PKI

|  |  |
|---|---|
| **Type** | paper (peer-reviewed conference) |
| **Maturity** | `white-paper`, the nearest enum value for a conference paper |
| **Authors** | Hao Wang, Somesh Jha, Thomas Reps, Stefan Schwoon, Stuart Stubblebine |
| **Published** | 2006, ESORICS 2006 |
| **Identifier** | DOI 10.1007/11863908_11 |
| **Source** | https://pages.cs.wisc.edu/~jha/jha-papers/security/esorics_2006.pdf |
| **Digest** | `sha256:62da03df…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Wang et al. attribute SPKI/SDSI's limited deployment chiefly to requiring every user to manage a key pair, and remove that requirement. A per-site Kerberos service (K-SPKI/SDSI) accepts certificate requests over an authenticated Kerberos channel and signs SPKI/SDSI certificates itself, so only each site's server holds a key pair (§1). The paper claims no conceptual difference: possession of a secret still links user to certificate (§3.3). A prototype, on synthetic data with about 1,500 certificates and eight sites, answered complex authorization queries in about a second (§4).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Moves signing authority to a per-site server |
| Cryptography | `adjacent` | Trades user key pairs for symmetric session keys |
| This project | `adjacent` | A stated diagnosis of SPKI non-adoption, and a rejected trade |

`R-M-02` and `R-O-01`: mofn keeps principals as keys and every issuer as a key. This design removes the user key, and with it the principal: each signed certificate is the server's, so end users can no longer be identified solely by key. It shows what buying deployability that way costs. mofn R-0004 §3.1 quotes its diagnosis.

## Implementations

Searched 2026-11-01, one query: no public source for the K-SPKI/SDSI prototype found. The paper names MIT Kerberos 1.3.1 and the Distributed SPKI/SDSI library (§4).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this file |

No `distilled/`: a summary-bar fill, and a `paper` record is outside FX-1 scope.

## Limits

Read: abstract, §1, §3.3, §4 in part and the end of §5, from the author-hosted PDF. §2 and the protocol steps of §3.1-3.2 were not read closely, so the protocol is not described beyond the outline here.

"Primarily due to the difficulty of key-management" (§5) is asserted, not measured, and competes with the other causes in mofn R-0004 §5. The authors never deployed it: evaluation is simulated, on synthetic data (§4). Each site's server is a new central signer for its users, and a compromise of that server is not something the sections read deal with. It requires Kerberos already installed, so it speaks to enterprises, not the open web.

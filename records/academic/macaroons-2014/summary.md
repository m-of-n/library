---
schema: "library-summary/v1"
id: macaroons-2014
record: macaroons-2014
type: summary
updated: "2026-11-01"
---

# Macaroons: Cookies with Contextual Caveats for Decentralized Authorization in the Cloud

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_: the enum has no value for a conference paper |
| **Authors** | A. Birgisson, J. G. Politz, Ú. Erlingsson, A. Taly, M. Vrable, M. Lentczner |
| **Published** | 2014-02 |
| **Identifier** | no DOI in the copy read |
| **Source** | https://web.archive.org/web/20260204031436id_/http://theory.stanford.edu/~ataly/Papers/macaroons.pdf |
| **Digest** | `sha256:1bbb26fb…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Venue** | NDSS 2014 |

## Overview

Macaroons are bearer credentials carrying caveats, built from nested HMACs: each caveat is MACed under the previous signature, so any holder can add a caveat but none can remove one (§III, §IV). Each caveat is a predicate that must hold for the request, so authority is never computed. The target checks a conjunction against the concrete request, and third-party caveats push part of the check to a service that returns a discharge macaroon (§II, §IV-B). The paper is candid about SPKI/SDSI: it says macaroons have no real advantage over it "other than their efficiency and ease of adoption" (§II), and that only the minting target can verify an HMAC macaroon (§IV-D). It claims a formal proof of expressiveness against SPKI/SDSI and omits it (§IV-D). Its reason for preferring this design over public-key credentials is adoption cost, not any fault in SPKI's semantics (§II, §VIII).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Attenuation, delegation and contextual confinement in one token |
| Cryptography | `core` | Chained-MAC construction, with a security sketch and external proofs (§IV-D) |
| This project | `adjacent` | Prior art studied, not adopted. We sign with keys, and any party must be able to verify |

- **DEC-004, R-M-08**: this is the alternative to an intersection operator. A caveat is a predicate, nothing compares two authorities, and there is no intersection to define. The cost is that nobody can tell what a token authorizes without a request to test it against.
- **R-M-10**: there is no delegation flag. Any holder can derive a macaroon, which §VIII treats as the confinement problem and handles with caveats.
- **R-O-02**: §II and §V-E argue that very short lifetimes and third-party freshness checks make revocation tractable.

## Implementations

**Checked 2026-11-01.** Repositories confirmed through the GitHub API. No wider survey was done. Fly.io's implementation is listed under `ptacek-2024-macaroons`.

| Name | Kind | License | URL |
|---|---|---|---|
| pymacaroons | open source, Python; used by Veski 2026 | MIT | https://github.com/ecordell/pymacaroons |
| libmacaroons | open source, C; last push 2021 | BSD-3-Clause | https://github.com/rescrv/libmacaroons |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `paper` record owes FX-1 only if someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **Verification is local to the target.** The root key must not spread, so a macaroon cannot be publicly verified (§IV-D). §V-H sketches a public-key variant and calls its cost possibly prohibitive (§VII-A).
- **The SPKI proof is not in the paper.** The claim "at least as expressive" is stated with the proofs omitted (§IV-D), so we cannot check it.
- **The 2014 performance numbers are dated.** Table I uses 1024-bit RSA on a 2.33 GHz Core2 (§VII-A). The ratio to public-key verification should not be carried forward.
- **Internal slips.** Reference [17] labels RFC 6749 Informational, and `rfc6749.json` says Proposed Standard. §VIII refers to "three patterns illustrated in Figure 3", which are in Figure 2.
- **Read scope.** Read whole, including the appendix, from an Internet Archive capture of the author-hosted PDF. Formulas in the appendix were read through a lossy text layer.

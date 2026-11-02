---
schema: "library-summary/v1"
id: nistir-8547
record: nistir-8547
type: summary
updated: "2026-11-01"
---

# NIST IR 8547: Transition to Post-Quantum Cryptography Standards

|  |  |
|---|---|
| **Type** | spec (NIST Internal Report, final) |
| **Maturity** | `informational`: a NIST IR, which sets out a plan. Detailed guidelines and schedules follow in a revised SP 800-131A (§4.1) |
| **Authors** | D. Moody, R. Perlner, A. Regenscheid, A. Robinson, D. Cooper |
| **Published** | October 2026 (initial public draft 2024-11-12) |
| **Identifier** | NIST IR 8547 · DOI 10.6028/NIST.IR.8547 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/ir/2026/NIST.IR.8547.pdf |
| **Digest** | `sha256:cf1c5b3e…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The report sets NIST's retirement schedule. All quantum-vulnerable public-key cryptography (ECDSA, EdDSA, RSA, finite-field and elliptic-curve DH and MQV) is deprecated after 2030 and disallowed under NIST standards after 2035 (§4, Tables 2 and 4), with symmetric cryptography largely unaffected (§4.1.3). Federal high value assets and high impact systems move earlier under EO 14412 and OMB M-26-15: key establishment by 2030-12-31 and signatures by 2031-12-31 (§1, §4). The urgency differs by function. Encryption faces harvest-now-decrypt-later, but §3 says signatures are not vulnerable to HNDL, and §3.1.2 says authentication remains secure if the algorithms and keys are secure when it is performed. Signature migration is still urgent, because it takes longer and needs more parties (§3). Hybrids are permitted, not required, and are expected to lead to a second transition (§3.2).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Fixes the dates and the threat argument the migration records rest on |
| Cryptography | `core` | The approved post-quantum set, with security categories (Tables 1, 3, 5) |
| This project | `adjacent` | NG3 defers the suite, but a format designed today lives past 2035 |

- **R-O-02**: §3.1.2's argument holds for an authentication event, which is exactly what a short-lived object is. It does not hold for a signed attestation verified years later, and code signing already gets separate treatment (§3.1.1). The report does not address long-lived signed statements directly. That is our inference, and it supports preferring short validity.

It settles no open `DEC-*`.

**Disagreement on the record.** NIST and NSA part on hybrids and on scope. Here hybrid signatures are accommodated in FIPS 140 validation (§3.2), and §4.1.1 lists HSS, XMSS^MT and SLH-DSA as post-quantum, where `cnsa-2-0` excludes all three from NSS. The target populations differ, so this is `see_also`, not `contradicts`.

## Implementations

Not applicable and not searched: this is a planning document. The algorithms it names have their own records (`fips-204`, `fips-205`, `sp-800-208`).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled. EO 14412 and OMB M-26-15 are listed in `cites` as gaps: neither is held, and this record describes them only as IR 8547 does.

## Limits

- **Not the operative rule.** §4.1 defers the detailed guidelines and schedules to a revised SP 800-131A, and §4.2 says application-specific guidance may move earlier.
- **The final moved from the draft.** Anything citing the ipd's 112-bit versus 128-bit split is out of date. See `content.note`.
- **Long-lived signatures are not treated.** It does not discuss timestamps or evidence for signatures that must outlast a CRQC.
- **It gives no CRQC date.** §3 uses Mosca's inequality as an argument, not an estimate.
- **Read scope.** The whole report was read in the final version. The ipd was compared only on its transition tables and references.

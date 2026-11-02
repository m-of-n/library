---
schema: "library-summary/v1"
id: tcg-dice-layering
record: tcg-dice-layering
type: summary
updated: "2026-11-01"
---

# DICE Layering Architecture

|  |  |
|---|---|
| **Type** | spec (TCG) |
| **Maturity** | `standard`: cover marked PUBLISHED |
| **Authors** | Trusted Computing Group, individual contributors not recorded here |
| **Published** | 2020-07-23 |
| **Identifier** | TCG DICE Layering Architecture, Version 1.0 Revision 0.19 |
| **Source** | https://www.trustedcomputinggroup.org/resources/documents/dice-layering-architecture |
| **Digest** | `sha256:b2c748a5…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

This extends the CDI construction to every transition in a boot chain. Each layer combines its CDI with a measurement of the next, so a Layered Identity describes the components and their order (§6.2.1, §6.2.3). If a layer is compromised, every later layer's CDI-derived keys change, which is the recovery story (§6.1). Trust runs one way: a layer may not implicitly trust a later one (§6.2.4.3). §8.1 divides keys into certifying, attesting and identifying kinds, and restricts the first two to signing data known to the TCB layer.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Layered trust with defined constraints on each layer |
| Cryptography | `adjacent` | Algorithm examples only. Key derivation refers to SP 800-56C (§8.2.2) |
| This project | `adjacent` | Key-role separation and chaining are close to our concerns |

- **R-M-02**: §8.1.1 refuses to let attestation keys sign opaque data from outside the TCB, while Identity Keys may (Table 1). A key's meaning here depends on what it was restricted to sign, which is what a bare key does not express.
- **R-O-02**: §8.3.2 requires revoking the old keys when a layer is updated, and keeps persistence only for keys wrapped under the CDI.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **The root is trusted because it must be.** §6 says its misbehaviour cannot be detected.
- **Each layer's protection is assumed.** §4 assumes the key-generating layer is sufficiently protected and §6.2.2 puts hardening out of scope.
- **Measurements are not extended to a PCR** (§6.1), so there is no independent log to appraise.
- **Source defects.** §4 cites the DICE hardware specification as [4], which is IEEE 802.1AR in its own reference list, and writes 802.11AR for 802.1AR. `tcg-dice-cert-profiles` r01 repeats the second.
- **Read scope.** §1 to §8.3.2, §9's opening and §10 to §10.2.1 were read. The rest of §9, including the layered-certification procedures and their figures, was not.

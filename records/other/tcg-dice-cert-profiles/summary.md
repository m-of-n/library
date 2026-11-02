---
schema: "library-summary/v1"
id: tcg-dice-cert-profiles
record: tcg-dice-cert-profiles
type: summary
updated: "2026-11-01"
---

# DICE Certificate Profiles

|  |  |
|---|---|
| **Type** | spec (TCG) |
| **Maturity** | `standard`: cover marked PUBLISHED |
| **Authors** | Trusted Computing Group, individual contributors not recorded here |
| **Published** | 2025-04-24 |
| **Identifier** | TCG DICE Certificate Profiles, Version 1.1 |
| **Source** | https://www.trustedcomputinggroup.org/resources/documents/dice-certificate-profiles |
| **Digest** | `sha256:eb1704d5…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

This profiles X.509 for DICE-derived keys. Policy OIDs under `tcg-dice-kp` declare what a key is for: initial or local identity, attestation, assertion of reference measurements, or acting as an embedded CA (§5.1.5). Separate profiles cover IDevID, LDevID, embedded-CA and attestation certificates (§5.1.6). It advises verifiers against taking attestation claims from Subject or Issuer names (§5.1.3, §5.1.4). Revision r01 said SHOULD NOT there, and v1.1 softens the wording.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Certificate conventions, not a new mechanism |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Only if DICE chains are imported |

- **R-I-05**: these certificates would import as foreign identity assertions. Their policy OIDs are the mapping table's input.
- **R-M-01**: the X.509 path. `google-open-dice` shows the alternative.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Attestation extensions are deferred.** r01 Table 1 says a future TCG specification may address them.
- **No revocation story for embedded CAs at the device.** Key Usage forbids cRLSign in the ECA profile, while Table 3 requires CRLDistributionPoints, so CRLs must come from elsewhere (r01 §5.1.6.3).
- **Read scope.** r01 was read whole. In v1.1 the OID list and the section list were read and the Key Usage lines were checked by text search. v1.1 was not compared line by line, and locators for r01 may have moved.

---
schema: "library-summary/v1"
id: tcg-dice-cert-profiles
record: tcg-dice-cert-profiles
type: summary
updated: "2026-11-04"
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

This profiles X.509 for DICE-derived keys. Policy OIDs under `tcg-dice-kp` declare what a key is for: initial or local identity, attestation, assertion of reference measurements, or acting as an embedded CA (§5.1.5). Separate profiles cover IDevID, LDevID, embedded-CA and attestation certificates (§5.1.6). It advises verifiers against taking attestation claims from Subject or Issuer names (§5.1.3, §5.1.4). Revision r01 said "SHOULD NOT" there; v1.1 says the Verifier "is recommended to not", lowercase and so outside BCP 14 by the document's own §1.1. Attestation extensions themselves are left to "a future TCG specification" in every profile table (Tables 1 to 4).

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

**`cites`** lists the held records among v1.1's §2 references: [4] DICE hardware requirements, [5] DICE Layering Architecture and [6] RFC 5280. RFC 8392 was dropped from `cites`: r01 cited it ([8]) and v1.1 does not. **One `see_also`, ours:** `tcg-dice-implicit-identity` supplies the example FWID certificate extension (its §7.3.1) that this profile defers, and its §7.3.3 lifetime text reappears nearly word for word as §5.1.2 here. `tcg-dice-layering` and `rfc-5280` were dropped from `see_also` as duplicates of `cites`.

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Attestation extensions are deferred.** v1.1 Tables 1 to 4 each say a future TCG specification may address them.
- **No revocation story for embedded CAs at the device.** Key Usage forbids cRLSign in the ECA profile, while Table 3 requires CRLDistributionPoints, so CRLs must come from elsewhere (v1.1 §5.1.6.3, Table 3; the same in r01).
- **Read scope.** v1.1 was read whole on 2026-11-04, and the locators above are v1.1's. r01 was read whole earlier and spot-checked for the SHOULD NOT wording and its reference list. The r01 errata was not read.

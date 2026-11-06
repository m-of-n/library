---
schema: "library-summary/v1"
id: tcg-dice-implicit-identity
record: tcg-dice-implicit-identity
type: summary
updated: "2026-11-04"
---

# Implicit Identity Based Device Attestation

|  |  |
|---|---|
| **Type** | spec (TCG reference) |
| **Maturity** | `standard`: cover marked Published |
| **Authors** | Trusted Computing Group, individual contributors not recorded here |
| **Published** | 2018-03-05 |
| **Identifier** | TCG Implicit Identity Based Device Attestation, Version 1.0 Revision 0.93 |
| **Source** | https://www.trustedcomputinggroup.org/resources/documents/implicit-identity-based-device-attestation |
| **Digest** | `sha256:f6f23a30…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Attestation here is implicit: holding the right key proves the state, because the key could not exist otherwise. First Mutable Code derives a long-lived DeviceID key pair from the CDI, and an Alias key pair from the CDI and the firmware's identity (§7.1, §7.2, §7.2.1.1). DeviceID certifies Alias, with the firmware digest in an X.509 extension (§7.3.1). The vendor certifies DeviceID at manufacture, so no secret database of UDS values is needed (§4, §8.2). Updating firmware therefore re-keys the Alias and leaves DeviceID alone, while updating Layer 0 loses the device's identity (§7, §8.3.1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Identity and attestation with one chain, and recovery by firmware update |
| Cryptography | `adjacent` | Algorithm-free. ECC is favoured (§7.1.1.1) |
| This project | `adjacent` | Rich detail on how long-lived and short-lived keys should relate |

- **R-I-05**: everything is X.509 and relies on a manufacturer's chain. It would import as a foreign identity assertion about a key.
- **R-O-02**: without a secure clock, §7.3.3 sets notAfter to 99991231235959Z. In place of a short lifetime, expiry is assumed to coincide with firmware update. That is the opposite of short-lived validity.
- **R-M-02**: DeviceID alone can only be used during Layer 0, because it must be erased before handover (§7.2). A device's long-term key is in practice a certifier: §7.3 gives certifying Alias Keys as its primary use.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**`cites`** holds what the text names: the DICE hardware requirements specification it builds on (§1, §6.4) and RFC 5280 (§7.3). It has no reference list. **No `see_also`.** Every earlier edge was a duplicate: `tcg-dice-layering` and `tcg-dice-symmetric` cite this document, `tcg-dice-cert-profiles` holds the `see_also` with its reason, and the other two are now `cites`.

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **DICE's misbehaviour cannot be detected** (§5).
- **Single cloud assumption.** §4 and §8.3.4.1 assume one infrastructure knows the device, and flag that this may enable tracking.
- **Layer 0 updates lose identity**, and §7 defers recovery to a future use case.
- **Rollback.** §8.3.4.3 makes reprovisioning irrevocable, which destroys derived secrets.
- **Read scope.** Read whole.

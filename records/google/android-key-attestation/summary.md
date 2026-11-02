---
schema: "library-summary/v1"
id: android-key-attestation
record: android-key-attestation
type: summary
updated: "2026-11-01"
---

# Android Key and ID Attestation

|  |  |
|---|---|
| **Type** | web (vendor platform documentation) |
| **Maturity** | `implementation`: platform documentation |
| **Authors** | Google (Android Open Source Project), no individuals named |
| **Published** | last updated 2026-09-30 |
| **Identifier** | source.android.com/docs/security/features/keystore/attestation |
| **Source** | https://source.android.com/docs/security/features/keystore/attestation |
| **Digest** | `sha256:cb042fef…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Key attestation exists because before it a remote party had no reliable way to tell whether a Keystore key was hardware-backed: the keystore daemon just believed the HAL (opening section). An attestation is an X.509 certificate for the key, with an extension listing its properties and constraints, signed by a certified attestation key. A batch attestation key is named in the certificate's fields, so the signer is not unique to a device. ID attestation adds factory copies of hardware identifiers held by the TEE, surviving a bootloader unlock (ID attestation).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A deployed answer to hardware backing, device state and identifier spoofing |
| Cryptography | `adjacent` | ECDSA or RSA by key type. ASN.1 schema per version |
| This project | `adjacent` | Foreign evidence, and a clean example of key properties as signed claims |

- **R-I-05**: the format is an X.509 extension, so it fits the rule that X.509 imports as a foreign assertion about a key.
- **R-I-02**: the attestation key is certified by a party the verifier does not control. Which root that is was not read here.
- **R-M-02**: the attested properties are what the key cannot state alone, such as where it lives and which conditions gate its use.

## Implementations

**Not surveyed.** Licenses were read from each repository on 2026-11-01. No wider search was run.

| Name | Kind | License | URL |
|---|---|---|---|
| android-key-attestation | open source sample, Google | Apache-2.0 | https://github.com/google/android-key-attestation |

Repository archived on GitHub. Not named by the page; found by direct lookup.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A `web` record is not an FX-1 type, and nothing here needs extraction yet.

## Limits

- **Device state is reported, not repaired.** With an unlocked bootloader, the verified boot state is Unverified: no chain of trust is established, and integrity must be checked out of band.
- **ID attestation is optional** and can be disabled permanently by `destroyAttestationIds()`.
- **A batch signer** does not by itself identify one device.
- **Revocation not read.** This page was not found to cover it in the sections read.
- **Read scope.** Opening, the key attestation summary, the certificate overview, the verified boot state table and ID attestation were read from an Archive capture, by text extraction. Most ASN.1 schema versions and field tables were not.

---
schema: "library-summary/v1"
id: android-key-attestation
record: android-key-attestation
type: summary
updated: "2026-11-04"
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

Key attestation exists because before it a remote party had no reliable way to tell whether a Keystore key was hardware-backed: the keystore daemon just believed the HAL (opening section). An attestation is an X.509 certificate for the key, with an extension listing its properties and constraints, signed by a certified attestation key (Attestation certificate). The certificate's issuer is the subject of the batch attestation key, and its subject and serial number are fixed values, the same on all certificates (TBSCertificate table). Factory-provisioned RSA and ECDSA attestation keys are the original path; since Android 12, Remote Key Provisioning issues shorter-lived per-app ECDSA P-256 attestation certificates (Attestation keys). ID attestation adds factory copies of hardware identifiers held by the TEE, surviving a bootloader unlock (ID attestation).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A deployed answer to hardware backing, device state and identifier spoofing |
| Cryptography | `adjacent` | ECDSA or RSA attestation keys. ASN.1 schema per version |
| This project | `adjacent` | Foreign evidence, and a clean example of key properties as signed claims |

- **R-I-05**: the attestation is a standard X.509 certificate whose content is attributes of the attested key, carried in extension OID 1.3.6.1.4.1.11129.2.1.17 (Attestation certificate, Attestation extension). That is exactly the shape R-I-05 allows an X.509 import to take: a foreign attribute assertion about a key.
- **R-I-02**: the chain runs "back to and including the root attestation key" (How app developers use attestation), and for a TEE-held key "chains back to a known root of trust" (ID attestation). The page does not name that root. A verifier importing this evidence must accept the root for the claim without making it a native anchor.
- **R-M-02**: the certificate names its subject only by key. The subject is the fixed `CN = "Android Keystore Key"` and the serial is fixed at 1 on every certificate, so the name fields carry no identity and the attested key is told apart by its `subjectPublicKeyInfo` (TBSCertificate table); the attestation extension then adds claims about that key. A deployed case of a principal identified by key rather than by name.

## Implementations

**Not surveyed.** Licenses were read from each repository on 2026-11-01. No wider search was run.

| Name | Kind | License | URL |
|---|---|---|---|
| android-key-attestation | open source sample, Google | Apache-2.0 | https://github.com/google/android-key-attestation |

Repository archived on GitHub (read-only, last push 2025-06-11), licence re-checked 2026-11-04. Not named by the page; found by direct lookup.

## Relations

**No `see_also`.** `tcg-dice-implicit-identity` was dropped: the page does not mention DICE, and no reason beyond both being hardware attestation was stated. `rfc-5280` moved from `see_also` to `cites`, since both certificate tables say "see RFC 5280" for field names.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A `web` record is not an FX-1 type, and nothing here needs extraction yet.

## Limits

- **Device state is reported, not repaired.** With an unlocked bootloader, the verified boot state is Unverified: a chain of trust cannot be established, and integrity must be verified by the user out of band (VerifiedBootState values). The same table notes that Verified can also mean an approved test device with an unlocked bootloader.
- **softwareEnforced is only as good as the OS.** It can be trusted only while the bootloader is locked and the boot state is Verified (KeyDescription fields).
- **ID attestation is optional** and can be disabled permanently by `destroyAttestationIds()`.
- **A batch signer** does not by itself identify one device. The page uses the word "batch" but does not say how many devices share a factory attestation key.
- **No revocation.** The page does not cover it. The only hook is the certificate's CRL Distribution Points extension, whose value is "TBD" (TBSCertificate table).
- **Read scope.** Re-read 2026-11-04 from the Archive capture, by text extraction: the opening, key attestation, the certificate tables, KeyDescription and SecurityLevel fields, RootOfTrust and VerifiedBootState, AttestationApplicationId, the provisioning information extension, attestation keys, Unique ID, ID attestation through hardware identifiers, and the Java API. The ASN.1 schema versions and the AuthorizationList field table were not read.

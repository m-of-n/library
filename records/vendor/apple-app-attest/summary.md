---
schema: "library-summary/v1"
id: apple-app-attest
record: apple-app-attest
type: summary
updated: "2026-11-04"
---

# DCAppAttestService / App Attest

|  |  |
|---|---|
| **Type** | web (vendor developer documentation) |
| **Maturity** | `implementation`: vendor developer documentation |
| **Authors** | Apple Inc., no individuals named |
| **Published** | undated pages |
| **Identifier** | developer.apple.com DeviceCheck documentation |
| **Source** | https://developer.apple.com/documentation/devicecheck |
| **Digest** | `sha256:a03fbb55…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

App Attest starts from the rule that an app's own logic cannot vouch for itself. The app creates a key in the Secure Enclave, and an Apple server certifies it as belonging to a valid instance of the app (Establishing your app's integrity). The server checks the attestation object, stores the public key, and later checks assertions signed by that key, each bound to a one-time challenge and to a counter (Validating apps). What is attested is an app instance, not a device or a person. Apple's servers are part of the protocol at key certification, which `attestKey` makes against a remote Apple server (Establishing, Certify the key pairs), and again for the fraud metric (Assessing fraud risk). Checking later assertions needs only the stored public key.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Hardware-held key plus an online vendor certifier |
| Cryptography | `adjacent` | CBOR and WebAuthn-format authenticator data, a COSE (RFC 8152) public key |
| This project | `adjacent` | An example of one vendor as a mandatory root |

- **R-I-02**: the server verifies the `x5c` chain against Apple's App Attest root certificate (Validating, Verify the attestation, step 1). A design importing this evidence has to accept that root for the claim without making it a native anchor.
- **R-M-02**: after attestation the app instance is known to the server only by its key. The key identifier is the SHA-256 of the public key and must equal `credentialId` (Validating, Verify the attestation), and every later assertion's signature is checked with that stored public key, with no call to Apple (Verify the assertion, step 3). A deployed case of a principal identified by key and key digest.

**`see_also: android-key-attestation`**: the other mobile platform's answer to the same problem, with the opposite architecture. Apple certifies an app key through an online Apple service; on Android the device's secure hardware itself signs an X.509 certificate for the key, using an attestation key provisioned at the factory or, since Android 12, remotely (see that record). Read together they show where the vendor root sits in each.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**`cites`** lists what the Validating article itself links: RFC 8152 for the encoded public key, RFC 7049 for the CBOR attestation object, and WebAuthn for the authenticator data, which the library does not hold. `rfc-9052` was a `see_also` and is dropped: the page cites RFC 8152, and its successor is reached from that record.

**No `distilled/`.** This is the summary bar. A `web` record is not an FX-1 type, and nothing here needs extraction yet.

## Limits

- **A modified OS may bypass it.** Assessing fraud risk says so, and offers only an approximate count of attested keys for the app on a device over the past 30 days as a risk metric. The DeviceCheck overview adds that App Attest "can’t definitively pinpoint a device with a compromised operating system".
- **Not all devices support it**, and the server "can no longer require assertions" for such a device (Establishing, Check for availability), so absence cannot be treated as failure.
- **No user or device identity.** The attestation carries an App ID hash and the key; binding the key to a user is the server's job (Validating, Store the public key and receipt).
- **Keys do not survive reinstallation**, device migration or restore from backup (Establishing, Start over on reinstallation), so the identity is per installation.
- **Read scope.** The five pages named in `content.note` were read whole as text extracted from their JSON, on 2026-11-04. Code listings were not read, and the attestation-object validation guide the Validating article links was not fetched.

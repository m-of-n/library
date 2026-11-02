---
schema: "library-summary/v1"
id: apple-app-attest
record: apple-app-attest
type: summary
updated: "2026-11-01"
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

App Attest starts from the rule that an app's own logic cannot vouch for itself. The app creates a key in the Secure Enclave, and an Apple server certifies it as belonging to a valid instance of the app (Establishing your app's integrity). The server checks the attestation object, stores the public key, and later checks assertions signed by that key, each bound to a one-time challenge and to a counter (Validating apps). What is attested is an app instance, not a device or a person. Apple's servers are part of the protocol.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Hardware-held key plus an online vendor certifier |
| Cryptography | `adjacent` | CBOR and WebAuthn-format authenticator data, COSE key |
| This project | `adjacent` | An example of one vendor as a mandatory root |

- **R-I-02**: the attestation chain is Apple's, and Apple's servers must be reachable for it. A design importing this must treat Apple as a foreign, scoped asserter.
- **R-M-02**: the key is per user per device (Establishing). What it adds beyond a bare key comes from Apple's certificate, not from the Secure Enclave alone.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A `web` record is not an FX-1 type, and nothing here needs extraction yet.

## Limits

- **A modified OS may bypass it.** Assessing fraud risk says so, and offers only a count of attestations per device as a risk metric.
- **Not all devices support it**, and a server must then stop requiring assertions, so absence cannot be treated as failure.
- **No user or device identity.** The article scope is the app instance.
- **Read scope.** The pages named in `content.note` were read as rendered text, in part: all of the integrity article up to its assertions section, the validation article up to storing the key, the opening of the fraud page, and the openings of the two reference pages. Code listings were not read.

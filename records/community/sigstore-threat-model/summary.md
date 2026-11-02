---
schema: "library-summary/v1"
id: sigstore-threat-model
record: sigstore-threat-model
type: summary
updated: "2026-11-01"
---

# Sigstore Threat Model

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | informational |
| **Authors** | Sigstore project |
| **Published** | 2026, Sigstore project |
| **Identifier** | https://docs.sigstore.dev/about/threat-model/ |
| **Source** | https://docs.sigstore.dev/about/threat-model/ |
| **Digest** | `sha256:f04289c8…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The project's own threat modelling exercise for keyless signing, enumerating which parties an attacker can compromise and what each gains. The result is a table sorted by impact. Monitors alone gain nothing. Fulcio CT and Rekor compromise are detectable. The Fulcio CA gives arbitrary software attacks, an OIDC server does so for its domain, and the root of trust does so for everything. A valid signature guarantees only that the signer authenticated as that identity at that time. It says nothing about whether they should have been able to, or whether the artifact is good. *Policy considerations* leaves the question of whom to trust to the user.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Compromise by compromise, states what each party can do. Detection relies on monitoring |
| Cryptography | `adjacent` | Trust roots use TUF with threshold keys, e.g. 3 of 5 |
| This project | `core` | The project itself says the guarantee is minimal, which frames the entitlement gap exactly |

- **R-O-04**: transparency only pays if someone monitors. *Main takeaways* says so.
- **R-O-02**: certificates are short-lived, and TUF handles rotation and revocation of service keys.
- **R-M-02**: a contrast. Trust terminates in OIDC issuers, which the page calls highly trusted.
- **Topic**: *Policy considerations* lists the questions an entitlement layer would answer. The page answers none, and says the answers differ by setting.

## Implementations

**Searched 2026-11-01.** GitHub repository metadata checked. See `sigstore-2022` for the service components.

| Name | Kind | License | URL |
|---|---|---|---|
| rekor-monitor | open source, monitor | Apache-2.0 | https://github.com/sigstore/rekor-monitor |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A web source has no FX-1 obligation, and nothing here needed a further artifact.

## Limits

- **Evidence, not policy.** The page says outright that not everything signed is secure.
- **Assumes monitoring exists.** The table assumes multiple gossiping monitors, and treats compromise of all of them as one event.
- **OIDC account compromise is out of Sigstore's hands.** Its mitigation is 2FA, which the page admits OIDC cannot check.
- **Terminology.** See `sigstore-2022` for the difference over SCT.
- **Read scope.** The whole page was read. The linked TAP-18 was not read.

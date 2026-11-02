---
schema: "library-summary/v1"
id: draft-ietf-scitt-scrapi
record: draft-ietf-scitt-scrapi
type: summary
updated: "2026-11-01"
---

# Supply Chain Integrity, Transparency, and Trust (SCITT) Reference APIs

|  |  |
|---|---|
| **Type** | draft |
| **Maturity** | draft |
| **Authors** | H. Birkholz, J. Geater, A. Delignat-Lavaud |
| **Published** | 2026-06-26, IETF |
| **Identifier** | `draft-ietf-scitt-scrapi-11` |
| **Source** | https://www.ietf.org/archive/id/draft-ietf-scitt-scrapi-11.txt |
| **Digest** | `sha256:9eb8b068…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

SCRAPI turns the SCITT architecture's abstract interactions into one concrete HTTP protocol. It has four resources: `/.well-known/scitt-keys` for key discovery (§2.1), a per-`kid` key lookup (§2.2), `POST /entries` for registering a COSE Signed Statement (§2.3), and Receipt resolution (§2.4). Registration is asynchronous by design because logs may take a long time to reach finality, so a 202 returns a locator for the client to poll. Errors are CBOR Concise Problem Details, chosen to avoid mixing CBOR and JSON (§2). Registration Policy content, the Verifiable Data Structure, and authentication are all out of scope (§1.1, §4.3).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Threat model covers identification, payload integrity and non-equivocation at the API layer (§4.4.1). Authentication is left out (§4.3) |
| Cryptography | `adjacent` | Carries COSE objects, and recommends RFC 9679 thumbprints as `kid` (§2.2). Defines no cryptography of its own |
| This project | `adjacent` | The interface we would meet if we register statements, which R-O-04 keeps conditional |

- **R-O-04**: this is the wire protocol behind "a SCITT-like transparency service". R-O-04 is conditional, so the record is `adjacent`, not `core`.
- §2.2's RECOMMENDED thumbprint `kid` is key-derived, which fits R-M-12's direction. The rest of the surface uses a well-known URI and IANA-allocated COSE labels, which R-M-12 would treat as interchange.
- §4.4.2.3 says unauthenticated HTTP signals must not drive the registration decision. That rule is close to what we want for any registry-facing surface.

## Implementations

**Searched 2026-11-01.** GitHub repository metadata checked for license and archive state. Implementation coverage of revision -11 was not tested.

| Name | Kind | License | URL |
|---|---|---|---|
| scitt-ccf-ledger | open source, confidential ledger | MIT | https://github.com/microsoft/scitt-ccf-ledger |
| scitt-api-emulator | open source, emulator | MIT | https://github.com/scitt-community/scitt-api-emulator |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `draft` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **What cannot be pinned down.** Registration Policy evaluation is out of scope (§1.1, §2.3), so two conforming services can accept different statements. The API does not say who may register.
- **No authentication story.** §4.3 leaves it out, and asks only for rate limiting or other mitigations where authentication is absent.
- **Replay is argued away.** §4.4.2.1 treats replay as not particularly concerning, and leaves time-dependent payloads to issuer timestamps.
- **Detached payloads are underspecified.** §2.3 says the mechanism by which the service gets the payload is implementation-specific.
- **429 is worded twice.** §2.3.4 says a service MAY return 429 for over-frequent polling, and §5.3 says it MUST when a client exceeds the configured rate limit. The two can be reconciled through what "configured" covers, but an implementer has to do that reconciling. §2 separately says status codes in examples are illustrative.
- **Read scope.** The whole of -11 was read, apart from the reference list and the worked registration sequence at the end of §2.4. The RFC does not exist yet, and -11 is in the RFC Editor queue, so text may still change.

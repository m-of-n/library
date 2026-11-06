---
schema: "library-summary/v1"
id: draft-ietf-scitt-scrapi
record: draft-ietf-scitt-scrapi
type: summary
updated: "2026-11-04"
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
| **Digest** | `sha256:9eb8b068…` (full value in `record.yaml`), fetched 2026-11-01, re-verified 2026-11-04: identical bytes |

## Overview

SCRAPI turns the SCITT architecture's abstract interactions into one concrete HTTP protocol. It has four resources: `/.well-known/scitt-keys` for key discovery (§2.1), a per-`kid` key lookup (§2.2), `POST /entries` for registering a COSE Signed Statement (§2.3), and Receipt resolution (§2.4). Registration has an asynchronous mode because logs may take many seconds or longer to reach finality (§2.3): a 202 returns a locator for the client to poll (§2.3.2), while a service that can produce the Receipt in reasonable time MAY return it directly with a 201 (§2.3.1). Errors are CBOR Concise Problem Details, chosen to avoid mixing CBOR and JSON (§2). Registration Policy content, the Verifiable Data Structure, and authentication are all out of scope (§1.1, §4.3).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Threat model covers identification, payload integrity and non-equivocation at the API layer (§4.4.1). Authentication is left out (§4.3) |
| Cryptography | `adjacent` | Carries COSE objects, and recommends RFC 9679 thumbprints as `kid` (§2.2). Defines no cryptography of its own |
| This project | `adjacent` | The interface we would meet if we register statements, which R-O-04 keeps conditional |

- **R-O-04**: this is the wire protocol behind "a SCITT-like transparency service". R-O-04 is conditional, so the record is `adjacent`, not `core`.
- Not claimed: R-M-12 and DEC-003. §2.2 RECOMMENDS an RFC 9679 thumbprint as the Transparency Service's `kid`, but that is a choice about the service's own keys, and the thumbprint itself is `rfc-9679`'s to bear on. The surface uses a well-known URI and IANA-allocated COSE labels, which under R-M-12 (ADR-0001) are interchange, not native.
- §4.4.2.3 lets implementations route on unauthenticated HTTP-layer signals (MAY) but says they MUST NOT use unauthenticated signals as authoritative inputs to the registration decision. That rule is close to what we want for any registry-facing surface.

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

**Relations.** `cites` carries §7.1 and §7.2 whole. No `see_also` is authored here: `rfc-9943` and `rfc-9942` already author edges to this record, and RFC 9162, which §7.2 cites, sits under `cites`.

## Limits

- **What cannot be pinned down.** Registration Policy evaluation is out of scope (§1.1, §2.3), so two conforming services can accept different statements. The API does not say who may register.
- **No authentication story.** §4.3 leaves it out and only permits client authentication (MAY). Its one requirement is that, where authentication is not implemented, rate limiting or other denial-of-service mitigations MUST be implemented.
- **Replay is argued away.** §4.4.2.1 treats replay as not particularly concerning. For time-dependent payloads it puts the burden on the Issuer: timestamps MUST be added to the Issuer-signed protected header, the CWT `iat` claim MUST be used when the Issuer supplies the timestamp itself, and where a third-party timestamp is required the RFC 9921 header parameters or a similar mechanism (an Epoch Marker, for example) SHOULD be used unless the applicable profile specifies another protected-header mechanism.
- **Detached payloads are underspecified.** §2.3 says the mechanism by which the service gets the payload is implementation-specific.
- **429 is worded twice.** §2.3.4 says a service MAY return 429 for over-frequent polling, and §5.3 says it MUST when a client exceeds the configured rate limit. The two can be reconciled through what "configured" covers, but an implementer has to do that reconciling. §2 separately says status codes in examples are illustrative.
- **Read scope.** The whole of -11 was read, including both reference lists (§7.1, §7.2) and the worked registration sequence at the end of §2.4 (source check 2026-11-04). The RFC does not exist yet, and -11 is in the RFC Editor queue, so text may still change.

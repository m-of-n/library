---
schema: "library-summary/v1"
id: rfc-9668
record: rfc-9668
type: summary
updated: "2026-11-01"
---

# Using Ephemeral Diffie-Hellman Over COSE (EDHOC) with the Constrained Application Protocol (CoAP) and Object Security for Constrained RESTful Environments (OSCORE)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc9668.json` 2026-11-01 |
| **Authors** | F. Palombini, M. Tiloca, R. Höglund, S. Hristozov, G. Selander |
| **Published** | 2024-11 |
| **Identifier** | RFC 9668 · DOI 10.17487/RFC9668 · CoRE WG |
| **Source** | https://www.rfc-editor.org/rfc/rfc9668.txt |
| **Digest** | `sha256:8785201c…` (full value in `record.yaml`), verified 2026-11-01 |
| **Errata** | none: errata search returned no matching errata, 2026-11-01 |

## Overview

RFC 9668 cuts a round trip. Run in sequence, EDHOC then OSCORE takes three round trips to finish a first protected request (§2). This document folds EDHOC message_3 into the first OSCORE request, signalled by a new Critical CoAP option, so the exchange takes two (§3). The rest is plumbing: processing steps for both sides, rules tying connection identifiers to OSCORE IDs (§4), and web link attributes for discovering EDHOC resources (§6).

One sentence travels beyond CoAP: §7 says completing EDHOC and deriving the context does not determine whether the request is authorized. Key establishment is not authorization, and the access control checks are the same as for a request sent alone.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §7 states the authentication and authorization split |
| Cryptography | `none` | No new cryptography |
| This project | `none` | Bears on nothing |

Bears on no `DEC-*` or `R-*`. The usefulness verdict is the point of this record. No text in mofn `origin/main` `spec/` or `project/` names CoAP, OSCORE or EDHOC (searched 2026-11-01), and the §7 point adds no input to any requirement.

## Implementations

**Searched 2026-11-01.** A web search found no implementation reports. GitHub code search for `rfc9668` was sampled, first 10 hits, mostly RFC mirrors. `aiocoap` is confirmed in source: option 21 is named EDHOC, and `aiocoap/edhoc.py` has a `use_combined_edhoc` setting. `libcoap` is a second hit in `coap_option.h`, listed at header level only. Neither was run.

| Name | Kind | License | URL |
|---|---|---|---|
| aiocoap | open source, Python, CoAP stack | MIT, per README and the edhoc.py SPDX header | https://github.com/chrysn/aiocoap |
| libcoap | open source, C, CoAP stack, header-level hit | BSD-2-Clause (LICENSE file; GitHub detects Other) | https://github.com/obgm/libcoap |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

**No `see_also`.** This RFC cites `rfc-9528`, which already links the two. No reason was found for an edge to `rfc-9529` beyond both being EDHOC companions, so none is authored.

## Limits

- **It needs the forward flow.** Client as Initiator, server as Responder (§3). It cannot be combined with message_4 (§3.3.1, §5).
- **The gain can vanish** under Block-wise transfers with certain parameters (§1, §3.2.2).
- **It does not specify access control.** §7 requires the same checks and leaves what they are to the deployment.
- **Read scope.** §1 to §8.3 and the opening of §8.4, from the `.txt` with page furniture stripped. The rest of §8.4, references and acknowledgments not read, except reference entries cited in `record.yaml`.

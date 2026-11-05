---
schema: "library-summary/v1"
id: rfc-9334
record: rfc-9334
type: summary
updated: "2026-11-04"
---

# Remote ATtestation procedureS (RATS) Architecture

|  |  |
|---|---|
| **Type** | rfc (IETF, RATS WG) |
| **Maturity** | `informational`: confirmed in `rfc9334.json` 2026-11-01 |
| **Authors** | H. Birkholz, D. Thaler, M. Richardson, N. Smith, W. Pan |
| **Published** | 2023-01 |
| **Identifier** | RFC 9334 · DOI 10.17487/RFC9334 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9334.txt |
| **Digest** | `sha256:b80d035f…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

RFC 9334 names the roles and messages of remote attestation without defining a protocol. An Attester produces Evidence, a Verifier appraises it under policy using Endorsements and Reference Values, and a Relying Party acts on the resulting Attestation Results (§1, §3 to §5). Two topologies follow: the Passport Model, where the Attester carries the result, and the Background-Check Model, where the Relying Party forwards Evidence (§5.1, §5.2). The document separates trust, a choice one makes, from trustworthiness, a quality of the other system (§1). Freshness is left as a design choice among clocks, nonces and epoch IDs (§10).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The vocabulary for what attestation does and does not establish, and where the key-protection assumptions sit (§12.1) |
| Cryptography | `none` | No algorithms or formats. §12 says no wire protocol is documented |
| This project | `adjacent` | No import rule for hardware evidence exists yet, but this is the model such a rule would use |

- **R-I-02**: Verifiers and Relying Parties hold trust anchors by their own choice (§7, §12.4). Importing Evidence does not have to make the attestation vendor a native root, which is the shape R-I-02 asks for.
- **R-M-02**: §12.1 places the whole assurance on protecting the Attester and on how the attestation key was provisioned. A principal named solely by a key says nothing about either. That is this topic's question.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**`cites`** lists the held records among §14's references: RFC 5280, RFC 8392, [NIST-800-57-p1] (`sp-800-57pt1r5`) and [TCG-DICE-SIBDA] r0.95 (`tcg-dice-symmetric`). **No `see_also`.** The earlier edges to `rfc-9711` and `draft-ietf-rats-corim` were dropped: both cite this RFC, so the link is already a `cites` edge on their side.

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **No wire protocol, so nothing to conform to.** §12 reads as requirements on realisations, and states that without a specific proposal it is impossible to know if the threats are mitigated.
- **It assumes the hard part.** §12.1.1 assumes the Attesting Environment is sufficiently isolated from the Target Environment. It does not say how to establish that.
- **Off-device key generation rests on physical protection** (§12.1.2.1). Manufacturing is inside the trust base and the document cannot remove it.
- **Claims can be old when signed** (§10.4). A fresh signature does not make the measured value fresh.
- **Errata.** One report, EID 7314 (Technical, on role-versus-entity ambiguity), was Rejected on 2025-12-28. None is verified.
- **Read scope.** §1, §3.2, §3.3, §5.1, §5.2, §7.1, §10, §10.4, §11 in part, §12, §12.1, §12.1.1, §12.1.2.1 and §12.4 were read from the plain text. §4, §6, §8, §9 and the appendices were not read line by line. A search of the text found no uppercase BCP 14 keywords.

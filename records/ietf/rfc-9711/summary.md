---
schema: "library-summary/v1"
id: rfc-9711
record: rfc-9711
type: summary
updated: "2026-11-04"
---

# The Entity Attestation Token (EAT)

|  |  |
|---|---|
| **Type** | rfc (IETF, RATS WG) |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc9711.json` 2026-11-01 |
| **Authors** | L. Lundblade, G. Mandyam, J. O'Donoghue, C. Wallace |
| **Published** | 2025-04 |
| **Identifier** | RFC 9711 · DOI 10.17487/RFC9711 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9711.txt |
| **Digest** | `sha256:20d43b5a…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

EAT is a claims set about an entity, encoded as a CWT or a JWT, and inherits their security mechanisms (§1). It defines claims such as `ueid`, measurements, boot state and debug status, plus nesting for composite devices (§4). It is a framework, not a token: §6 makes a profile responsible for encoding, algorithms, key identification and freshness, and §6.4 gives one profile for constrained devices. §9.1 is the passage that matters here: the specification does not require any particular level of security in the implementation of the claims or of the attester, because it is about a message format.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Defines what attestation claims mean, and disclaims how far they can be believed (§9.1) |
| Cryptography | `adjacent` | Inherits COSE and JOSE and adds no primitive. §6.4 picks ES256, ES384 and ES512 |
| This project | `adjacent` | A CBOR claims set in COSE_Sign1 is a live precedent for our envelope and encoding decisions |

- **DEC-002 and DEC-005**: §6.4 fixes CBOR, COSE_Sign1 and definite lengths for constrained devices, so a CBOR signed-claims profile has working prior art. It decides neither.
- **R-O-03**: §6.3 lists CBOR map, string and serialization choices as issues a profile "should address" (lowercase, not BCP 14), and §6.4's profile says "Preferred serialization MUST be used". `draft-ffm-rats-cca-token` §4.11.1 goes the other way, so two EAT profiles in one family disagree on encoding (see that record).

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**`cites`** lists the held records among §10's references: RFC 9334, RFC 8392, RFC 8949, RFC 9052, RFC 7515, RFC 8259, RFC 8610, RFC 9090, RFC 9165 and RFC 9360. **No `see_also`.** The earlier edges were each already a `cites` edge, here (`rfc-9334`, `rfc-8392`, `rfc-9052`) or on the other record (`draft-ffm-rats-cca-token` and `draft-ietf-rats-corim` both cite this RFC).

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **No security level.** §9.1 says the specification does not require any particular level of security in the implementation, and that a receiver learns trustworthiness from the vendor's implementation or the verifier's checks. A valid EAT is not by itself evidence of hardware.
- **A UEID is usually not privacy-preserving** (§8.1). The identifier that makes attestation useful also correlates.
- **Key distribution is out of scope.** §6.4 assumes the receiver has a database of trusted verification keys.
- **Errata.** 14 reports on 2026-11-04: 7 Verified, 5 Reported, 2 Rejected. The verified ones are in §4.2.3, §4.2.15, §4.3.1, §7.3.1 and the Appendix A.1.7 example; none touches §6 or §9.
- **Read scope.** §1, §1.3, §1.3.1, §4.2.1, §6 headings, §6.4, §8.1, §9.1 and §9.2 were read. The rest of §4, §5, §7 and §10 were not read line by line. Claim-by-claim semantics are not covered here.

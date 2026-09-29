---
schema: "library-summary/v1"
id: sp-800-161r1
record: sp-800-161r1
type: summary
updated: "2026-09-25"
---

# Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `best-practice` — a NIST Special Publication. Guidance, not a FIPS; binding on federal agencies only where separately mandated |
| **Authors** | Jon Boyens, Angela Smith (NIST); Nadya Bartol, Kris Winkler, Alex Holbrook, Matthew Fallon (Boston Consulting Group) |
| **Published** | 2022-05 — Rev. 1, with updates through 2024-11-01 (upd1) |
| **Identifier** | SP 800-161r1-upd1 · DOI 10.6028/NIST.SP.800-161r1-upd1 |
| **Source** | https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final |
| **Digest** | `not fetched` |

## Overview

Tells an organisation how to stand up a **cybersecurity supply chain risk
management (C-SCRM)** programme: how to identify, assess and mitigate the risk
that an acquired product or service is counterfeit, carries malicious
functionality, or is vulnerable through poor development practice.

Its structure is the argument. C-SCRM is placed at **three levels** —
enterprise, mission/business process, and operational — on the claim that supply
chain risk cannot be managed at any one of them alone: a procurement decision
made at level 1 constrains what level 3 can defend against, and a vulnerability
found at level 3 is often unfixable without a level 1 contract change. The
guidance is then expressed as an overlay on existing NIST machinery rather than
a parallel system — it hangs off the SP 800-39 risk process and SP 800-53
controls instead of inventing its own.

The consequential framing for us: it treats **supplier assurance as evidence
you must demand and evaluate**, while remaining deliberately silent on what form
that evidence takes. It says *get assurance*; it does not say *here is a signed
statement and here is how to verify it*.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Organisational risk process, not a security mechanism — it defends nothing by itself |
| Cryptography | `none` | Specifies no primitive, format, or protocol |
| This project | `adjacent` | Describes the institutional consumer of an attestation without specifying one |

**Bears on no `DEC-*` or `R-*`.** This is a stub, kept deliberately. It is the
enterprise frame that explains *why* anyone wants verifiable supply chain
claims, which is useful when writing motivation and related-work sections, and
useless when deciding an encoding or a signature scheme.

Recorded rather than dropped so the judgement is not re-litigated: the
`usefulness` verdict is `marginal`, and the reason is that we conform to no
clause in it.

## Implementations

Not searched. An enterprise risk-management practice guide has no
implementations in the sense this field means — no library implements SP
800-161. The nearest analogue is GRC tooling that claims C-SCRM coverage, which
is out of scope for a build-on-it decision.

| Name | Kind | License | URL |
|---|---|---|---|
| — | — | — | — |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md` and none warranted — we extract no requirements from it.

## Limits

- **Written from the abstract and document structure, not a full read.** The
  record is `status: stub` for that reason. Do not cite any specific clause,
  control mapping, or appendix on the strength of this summary.
- **It settles nothing here.** It names no format, no signature scheme, no
  transparency mechanism. Citing it to justify a design decision would be citing
  motivation as if it were a requirement.
- **Process guidance, and its efficacy is unevidenced.** The document does not
  demonstrate that following it reduces incidents; it is expert-consensus
  practice, which is what `best-practice` maturity means and is not a stronger
  claim than that.
- **US-federal in framing.** Written against FISMA, the RMF and federal
  acquisition. The three-level model may not transfer to organisations without
  that structure.
- **`upd1` is undifferentiated here.** CSRC reports updates through 2024-11-01;
  what changed between the 2022 release and upd1 has not been checked, so the
  version is recorded but the delta is not.
- **`see_also` is our judgement, not its citation.** `in-toto-attestation-v1`
  and `rfc-9943` are linked because they supply mechanisms for the assurance
  this document only demands — not because it references them.

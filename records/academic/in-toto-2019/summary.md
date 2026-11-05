---
schema: "library-summary/v1"
id: in-toto-2019
record: in-toto-2019
type: summary
updated: "2026-11-04"
---

# in-toto: Providing farm-to-table guarantees for bits and bytes

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed conference paper |
| **Authors** | Santiago Torres-Arias, Hammad Afzali, Trishank Karthik Kuppusamy, Reza Curtmola, Justin Cappos |
| **Published** | 2019-08-14, USENIX Association |
| **Identifier** | https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias |
| **Source** | https://www.usenix.org/system/files/sec19-torres-arias.pdf |
| **Digest** | `sha256:55024dfc…` (full value in `record.yaml`), fetched 2026-11-01, re-verified 2026-11-04 |

## Overview

The argument is that securing each supply chain step separately fails, because nothing verifies that the right steps ran or that output was not swapped between steps. in-toto has a project owner sign a *layout*: which steps run, in what order, by which functionary keys, with what artifact rules. Functionaries sign *link* metadata recording materials and products by hash. The client verifies all of it against the layout. Security degrades by which key is lost: a functionary key affects one step, and a layout key subverts the whole chain (§5.2). The paper evaluates 30 historical compromises, 23 of which involved no key compromise.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Goals include layout integrity, artifact flow integrity, step authentication and graceful degradation (§2.3), with a graded compromise analysis (§5.2) |
| Cryptography | `adjacent` | Signatures and thresholds used as given. No new primitive |
| This project | `core` | It states who may do what per step, in a signed object verified by the consumer |

- **R-I-03**: background to the in-toto export target. The paper's link format is older than the Statement in `in-toto-attestation-v1`.
- **R-M-07**: materials and products bind hashes at every step.
- **R-M-06**: a step or the layout can require a threshold of functionary keys (§5.2.1, §5.2.2). §7.2 credits thresholds, in the Reproducible Builds build step and the Datadog packaging step, for those deployments catching some of the five sophisticated key-compromise attacks in Table 3; the Cloud Native deployment, with no thresholds, catches none of the five.
- **Topic**: this is the strongest counterexample to "no entitlement layer". A layout grants named keys named steps. `in-toto-attestation-v1` says layouts are not part of the Attestation Framework, so the part the ecosystem adopted is the evidence half.

## Implementations

**Searched 2026-11-01.** GitHub repository metadata checked. Both report `NOASSERTION`; the Apache-2.0 reading comes from `in-toto-attestation-v1`, which checked their LICENSE files.

| Name | Kind | License | URL |
|---|---|---|---|
| in-toto (Python reference) | open source, library and CLI | Apache-2.0 | https://github.com/in-toto/in-toto |
| in-toto-golang | open source, library and CLI | Apache-2.0 | https://github.com/in-toto/in-toto-golang |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A paper has no FX-1 obligation, and nothing here needed a further artifact.

**Relations.** `cites`: [121] is `tuf-2010`. [28] cites the TUF project site, not a document we hold. One `see_also`: `tuf-spec`, because the paper leaves key bootstrap to other systems and names TUF for it (§2.2), and `tuf-spec` is the current statement of that system. The lineage to `in-toto-attestation-v1` is authored on that record, not here.

## Limits

- **The compromise evaluation is a counterfactual.** Table 3 and the *Key Takeaway* percentages are the authors' assessment of how three deployments would have fared, not a measurement of attacks stopped. No deployment faced those attacks.
- **Rogue insiders are outside the base model.** §5.1 assumes developer hosts are uncompromised and no developer is rogue, then treats a rogue functionary as equivalent to key compromise. An attacker who is the legitimate functionary signs valid links.
- **Trust bootstrap is not solved.** §2.2 leaves it open and points at TUF.
- **Read scope.** Abstract, §1 (opening), §2.2, §2.3, §3.2, §3.3, §5, the opening of §7, §7.2 and §9 were read through text extraction. §4 (metadata details), §6 (deployments), §7.1 (overhead), §8 and the appendices were not read closely, so no overhead figure is given.

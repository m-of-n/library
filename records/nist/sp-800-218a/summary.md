---
schema: "library-summary/v1"
id: sp-800-218a
record: sp-800-218a
type: summary
updated: "2026-10-02"
---

# SP 800-218A: Secure Software Development Practices for Generative AI and Dual-Use Foundation Models — An SSDF Community Profile

|  |  |
|---|---|
| **Type** | spec (NIST Special Publication; guidance) |
| **Maturity** | best-practice (final NIST SP; checked on CSRC 2026-10-02) |
| **Authors** | H. Booth, M. Souppaya, A. Vassilev, M. Ogata (NIST); M. Stanley (CISA); K. Scarfone (Scarfone Cybersecurity) |
| **Published** | July 2024 (approved by the NIST ERB 2024-07-25) |
| **Identifier** | NIST SP 800-218A · doi:10.6028/NIST.SP.800-218A |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf (30 pp.) |
| **Digest** | `e088c8bc75716824dae7c36a987f408364638561d381ed001b5c12254a7b10d8` (retrieved 2026-10-02) |

## Currency check (2026-10-02)

- https://csrc.nist.gov/pubs/sp/800/218/a/final lists **SP 800-218A, July 2024** as final.
  The page shows no withdrawal notice and no supplemental files.
- https://csrc.nist.gov/pubs/sp/800/218/a/r1/ipd returns 404, so no revision draft exists.
- The SSDF project page https://csrc.nist.gov/projects/ssdf (updated 2026-04-13) still
  lists 218A as the only NIST-provided Community Profile.
- The SSDF 1.2 initial public draft (SP 800-218r1 ipd, 2025-12-17;
  https://csrc.nist.gov/pubs/sp/800/218/r1/ipd) is still a draft and does **not** mention
  218A. The Profile remains pinned to SSDF **1.1**.
- **Its mandate has been revoked.** 218A was written for EO 14110 §4.1.a. EO 14148
  (2025-01-20, 90 FR 8237; govinfo FR-2025-01-28 2025-01901, §2(ggg)) revoked EO 14110.
  The document is still published and usable on a voluntary basis, but the "dual-use
  foundation model" definition comes from a revoked order.
- **Two of its references have newer editions.** The Informative References point at
  OWASP Top 10 for LLM Applications **v1.1** and NIST AI 100-2 **e2023**. Both have
  since been revised: OWASP Top 10 for LLM 2025 (https://genai.owasp.org/llm-top-10/)
  and NIST AI 100-2 **E2025** (https://csrc.nist.gov/pubs/ai/100/2/e2025/final). The
  mappings in this record keep the cited versions.

## Overview

218A is an **SSDF Community Profile**, which §1 defines as "a baseline of SSDF practices
and tasks that have been enhanced to address a particular use case". This profile
covers secure *AI model development*: data sourcing, design, training, fine-tuning,
evaluation, and integrating models into other software. Deployment and operation are
out of scope.

The profile overlays SSDF 1.1's 4 groups, 19 practices and 42 tasks with the following:

- one new practice, **PW.3** (confirm the integrity of training, testing, fine-tuning
  and aligning data before use);
- six new tasks: PO.5.3, PS.1.2, PS.1.3, PW.3.1, PW.3.2, PW.3.3;
- three modified tasks (PO.1.3, PS.3.2 which now names SLSA, PW.2.1 which now requires
  both human *and* automated design review) and two modified practices (PO.5, PS.1);
- a High / Medium / Low **Priority** on every task;
- 86 AI-specific **Recommendations / Considerations / Notes**, with ids of the form
  `PO.1.2.R1`;
- Informative References to AI RMF 1.0, the OWASP LLM Top 10 v1.1 and NIST adversarial
  ML taxonomy.

Its argument is that AI blurs the code/data boundary. Weights, datasets and prompts form
"closed loops that can be manipulated", so code-style protection, provenance and testing
have to extend to model weights, training data and model I/O. §2 also introduces a
shared-responsibility model across AI model producers, AI system producers and AI system
acquirers.

## Why it matters for an SDL

- **It is the template for tailoring a requirement set.** The overlay of base
  requirements plus per-profile priority, additions and change status is what the
  MAP-0001 crosswalk (R-044) and conformance (R-042) need in order to handle sector or
  company variants of SSDF without forking it.
- **PW.1.1 with PW.1.1.R1 is the threat-model requirement.** It names seven AI threat
  types that a threat model must cover (training-data poisoning, malicious I/O content,
  DoS from adversarial prompts, supply chain, information disclosure, weight theft,
  data-pipeline misconfiguration). A tmodel instance is the evidence for this task.
- **It has the most explicit human-in-the-loop gates in the SSDF family.** See
  PO.4.1.C1, PW.1.1.C2, PW.2.1 and RV.1.2.R2.
- **It is the only SSDF document that distributes tasks across organizations** (§2
  agreement plus attestation).

## Relation to other records

- `sp-800-218` (SSDF 1.1) is the base. 218A "should not be used without" it. The
  relation is recorded as `see_also` rather than `updates` or `supersedes`, because 218A
  changes nothing in SP 800-218 itself. It is an overlay, and its implementation
  examples and SSDF references are inherited from the base.
- `sp-800-218r1` (SSDF 1.2 IPD) is a sibling line that has not yet absorbed the
  Profile.
- **Identifier trap.** SSDF 1.1 *retired* PW.3, PW.3.1 and PW.3.2. 218A reuses them with
  new meaning, so a citation must always be record-qualified (`sp-800-218a#PW.3.1`).
- 218A cites `eo-14028`, `sp-800-53r5` and `sp-800-161r1`, which are all held. It also
  cites AI RMF, AI 100-2 and OWASP LLM Top 10, which are not held (see the frontier).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | It is the NIST secure-development baseline for AI models: weights, data and pipeline protection, model scanning, and adversarial testing. |
| Cryptography | adjacent | It asks for hashes and signatures over models, components and changes (PS.2.1.R1/R2), and encryption, signatures, multi-party authorization and air-gapping for weights (PS.1.3.R4). It names mechanisms only, with no algorithms. |
| This project | adjacent | It bears on R-040, R-041, R-042, R-044 and DEC-009 (SDL modelling, which is post-MVP), and it supplies AI threat types and AI artifact classes for threat-modelling AI systems. |

## Implementations

Searched 2026-10-02. These are tools that implement specific tasks; none claims 218A
conformance as a whole.

| Name | Kind | License | URL |
|---|---|---|---|
| NIST Dioptra (cited [5]) | ML security test bed (PW.8 adversarial testing) | NIST / public domain | https://github.com/usnistgov/dioptra |
| ModelScan | model artifact scanner (PW.7.2.R1, PW.4.4.R2) | Apache-2.0 | https://github.com/protectai/modelscan |
| safetensors | secure model serialization (PW.6.1.C1) | Apache-2.0 | https://github.com/safetensors/safetensors |
| sigstore model-transparency (OpenSSF model signing) | model signing and verification (PS.2.1) | Apache-2.0 | https://github.com/sigstore/model-transparency |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata, relations, cites, and the distillation block (FX-1, profile full) |
| `distilled/README.md` | Index of the artifacts and the extraction method |
| `distilled/normative.md` | All of Table 1 verbatim, plus governing prose, column semantics and the glossary |
| `distilled/requirements.yaml` | 168 typed entries (library-requirements/v2) with Priority, profile status and `maps_to` |
| `distilled/design-notes.md` | What we adopt, adapt or reject against R-040..R-044 and DEC-009; source defects |
| `distilled/object-model.yaml` | Object-model pass: 62 objects, 52 edges, 9 gaps |
| `distilled/object-model.md` | Mermaid diagram and headline findings |

## Limits

- **It gives no "how".** There is no Implementation Examples column; the source says
  one may come in a future version. Verification is left to the adopter.
- **It is voluntary and risk-based.** Organizations "adapt, customize, and omit". No
  conformance criterion is defined, so any pass/fail check is ours, not NIST's.
- **Its scope ends at deployment.** Operation of AI systems, and most of data governance,
  is out of scope, so runtime prompt-injection defence appears only as a development-time
  coding practice (PW.5.1.R2/R3).
- **The mapping targets are outdated** (OWASP v1.1, AI 100-2 e2023), and the mandate
  (EO 14110) has been revoked.
- **It has internal inconsistencies:** a reused retired id (PW.3), an untagged text
  change (PO.5.2) and an untagged editorial expansion (PO.1, "SDLC"). See `distilled/design-notes.md` §3.

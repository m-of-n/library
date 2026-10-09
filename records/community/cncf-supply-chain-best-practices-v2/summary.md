---
schema: "library-summary/v1"
id: cncf-supply-chain-best-practices-v2
record: cncf-supply-chain-best-practices-v2
type: summary
updated: "2026-10-02"
---

# Software Supply Chain Best Practices v2 (CNCF TAG Security)

|  |  |
|---|---|
| **Type** | paper (community white paper; secondary reference) |
| **Maturity** | white-paper |
| **Authors** | Marina Moore, Michael Lieberman, John Kjell (original white paper authors), James Carnegie, Ben Cotton, Aditya Sirish A Yelgundhalli; reviewers Aonan Guan, Justin Cappos (PDF title page) |
| **Published** | v2 PDF added 2025-03-20 (cncf/tag-security#1461; PDF created 2025-03-11). The PDF's "Published" field still reads `xxxxxxxxx` |
| **Identifier** | `SSCBPv2.md` / `Software_Supply_Chain_Practices_whitepaper_v2.pdf` in cncf/tag-security `community/working-groups/supply-chain-security/supply-chain-security-paper-v2/` |
| **Source** | https://github.com/cncf/tag-security/blob/main/community/working-groups/supply-chain-security/supply-chain-security-paper-v2/SSCBPv2.md |
| **Digest** | markdown `e2087a3f0929d149f4f986462ab1bd42757f14bae7fd9a4afeb2adfbfb1a3f33` (the extracted text); PDF `0af09b1f1b4549411d8f817484778d28b45cda676e1d441a70b7915a4163250b` (37 pp.) |

**Version verified 2026-10-02:**

- The GitHub contents API lists both papers side by side:
  `supply-chain-security-paper/CNCF_SSCP_v1.pdf` (v1, 2021-05, 45 pp., sha256 `be96fbd8…fa4b`) and
  `supply-chain-security-paper-v2/` (v2 markdown + PDF).
- The v2 commit history shows the PDF added 2025-03-20, with no later commits in that folder.
- The `cncf/tag-security` repository is **archived** on GitHub (API `archived: true`, last push
  2025-12-08). No v3 was found.

So v2 is current. The v1 paper (2021, CNCF_SSCP_v1.pdf) is the earlier edition of this line; the
library holds no record for it.

## Overview

The paper is the CNCF Security TAG's end-to-end guide to securing a software supply chain. It
splits the chain into five stages: **Source Code, Materials, Build Pipelines, Artifacts, and
Deployments and Distribution**. It reuses SLSA's threat diagram, mapping A–C to Source, the
dependencies to Materials, D–E to Build, F to Artifacts and G–I to Deployments. Within each stage,
practices are grouped as Verification, Automation, Controlled Environments and Secure
Authentication.

v2 changes the following from v1:

- adds **personas**, each with a "where do I start" path: developer, producer's security team,
  CISO, ops/platform, consumer's security team (verifier) and end user;
- adds VEX and audit-data handling;
- adds verification that actions such as tests were really performed;
- moves build-system detail to the Secure Software Factory paper.

The central model: signed **attestations**, produced at every step, are evaluated against a
**supply-chain policy** written in software. The policy names authorized actors, expected actions
and expected tests. Verification happens at a deployment gate and again by the end user. All of it
rests on a hardened **root of trust**. The paper names its own out-of-scope topics, including
supply-chain threat modeling, governance, compliance and incident response.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | the cloud-native reference practice catalog for supply-chain integrity |
| Cryptography | adjacent | signing, root of trust, key rotation/revocation, TUF; no algorithms |
| This project | adjacent | its policy-evaluated-against-attestations model is the automated gate check of R-041/R-042; its personas and Distributor role and its VEX statuses inform ARCH-0001 §2b/§5 |

Bears on **R-041** (gates: the deployment gate and the policy as exit criterion), **R-042**
(conformance as policy evaluation over attestations), **R-044** (60 practices as crosswalk rows)
and **R-037** (the stages as a supply-chain slice of the lifecycle axis).

## Implementations

The paper names CNCF/OpenSSF tooling as examples:

- in-toto (Witness, Archivista)
- TUF (RSTUF, tuf-on-ci)
- Sigstore
- SPIFFE/SPIRE
- gittuf, Peribolos/Prow
- Tekton, Argo, Jenkins, GitLab
- Syft, Trivy
- vexy
- Kubernetes admission controllers

Searched 2026-10-02. We list the names and do not evaluate them.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/README.md` | index |
| `distilled/requirements.yaml` | the 60 Part 3 practices: 59 level-4/5 headings plus the level-3 Second and Third-Party Risk Management subsection (stage, category, parent, full verbatim markdown body) |
| `distilled/verification.md` | verify-pass report (2026-10-02) |
| `distilled/object-model.yaml` | object-model pass: 39 objects, 29 edges, 5 gaps |
| `distilled/object-model.md` | Mermaid graph, attestation-lifecycle state diagram, findings |

This is a secondary reference, so its status is `summarized`. No FX-1 artifact set was produced.

## Limits

- **Recommendations, not requirements.** There are no levels, conformance criteria or verification
  method. v1's high/medium-risk-environment framing is not carried as per-practice tiers in the v2
  markdown.
- **Two renderings that differ.** The PDF is copy-edited away from the markdown, for example in the
  Scope wording. Our verbatim text comes from the markdown. One practice title ("Only allow pipeline
  modifications through \"pipeline as code\"") differs in punctuation in the PDF.
- **Explicitly out of scope:** supply-chain threat modeling, hardware, policy determination,
  application security, monitoring, governance, zero trust, incident response and compliance.
  For tmodel, this means it says nothing about *how to decide* which threats a policy must cover.
- **Stage-intro prose not itemized.** The intros carry lowercase must/should statements, for
  example "Producers must take care to verify the quality of these materials", that the
  requirements file does not list separately.
- **Archived home.** The repository is read-only, so later corrections, if any, will live
  elsewhere.

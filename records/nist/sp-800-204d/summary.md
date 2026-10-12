---
schema: "library-summary/v1"
id: sp-800-204d
record: sp-800-204d
type: summary
updated: "2026-10-02"
---

# SP 800-204D: Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines

|  |  |
|---|---|
| **Type** | spec (NIST Special Publication, guidance) |
| **Maturity** | best-practice (final NIST SP; checked on CSRC 2026-10-02) |
| **Authors** | Ramaswamy Chandramouli (NIST), Frederick Kautz (TestifySec), Santiago Torres-Arias (Purdue University) |
| **Published** | February 2024 (final 2024-02-12; draft 2023-08-30); approved by the NIST ERB 2024-01-31 |
| **Identifier** | NIST SP 800-204D · DOI 10.6028/NIST.SP.800-204D |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204D.pdf (41 pp.) |
| **Digest** | `74e404d98c9dd74722b678246e5127ffeede71c4b80d0c631c995650128174e8` |

**Currency check (2026-10-02).** The CSRC landing page https://csrc.nist.gov/pubs/sp/800/204/d/final
lists only two events: "08/30/23: SP 800-204D (Draft)" and "02/12/24: SP 800-204D (Final)". It shows
no supersession, errata or planning note. The guessed revision URLs `/pubs/sp/800/204/d/r1/ipd` and
`/pubs/sp/800/204/d/upd1/final` both return 404. **The February 2024 final is current.** Its SSDF
mapping targets SSDF v1.1 (`sp-800-218`). SSDF v1.2 (`sp-800-218r1`) is still an initial public
draft, so the mapping has not been redone.

## Overview

SP 800-204D turns the SSDF's supply-chain practices into concrete controls for **CI/CD pipelines in
cloud-native DevSecOps**. Its model is simple: a software supply chain is a sequence of *steps*.
Each step is *carried out* by an actor, human or machine, *uses* artifacts and resources, and
*produces* artifacts.

Its argument is that pipeline security comes from two things. The first is **evidence generated
while the build runs**, by something more trusted than the build: environment, process, materials
and artifacts attestations, signed and kept in tamper-proof storage. The second is **signed
policies** that verifiers evaluate before an artifact is signed, merged or admitted to deployment.

Around that core it sets out:

- source-control hygiene: role-consistent access, no self-approved merges, and maintainer approval
  before CI runs on outside contributions;
- commit-time controls: SAST/DAST, full transitive SCA, and secret push protection;
- update-system key management in the TUF style;
- GitOps release discipline.

Appendix A maps the tasks onto 12 SSDF v1.1 practices. Appendix B says why the design (PW.1–PW.4,
PW.7) and vulnerability-response (RV) practices are left out.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Build integrity, provenance, signing, admission control and secret handling for the pipeline that produces the software. |
| Cryptography | adjacent | Requires signatures on attestations and policies and threshold or offline keys, but defers all formats and algorithms. |
| This project | adjacent | Bears on R-041 (SDL Gate: deployment admission as an automatable gate) and R-042 (conformance: policy evaluated against typed, time-sensitive evidence). It is post-MVP per DL-0009. It is also a concrete source for MAP-0001 rows 13 and 16 and for SSDF crosswalk edges (R-044). |

## Implementations

Drawn from the document's own references and examples, plus the records we hold. This is not a
market survey (checked 2026-10-02).

| Name | Kind | License | URL |
|---|---|---|---|
| Witness (TestifySec) — attestation wrapper for CI commands (ref. [8]) | open source | Apache-2.0 | https://github.com/testifysec/witness |
| in-toto / in-toto attestation framework | open source | Apache-2.0 | records `in-toto-2019`, `in-toto-attestation-v1` |
| The Update Framework (TUF), ref. [11] | open source spec + implementations | Apache-2.0 / MIT | record `tuf-spec` |
| OpenSSF Scorecard (footnote 4, SCM posture) | open source | Apache-2.0 | record `openssf-scorecard-checks` |
| Open Policy Agent (policy engine example, §5.1.2) | open source | Apache-2.0 | https://www.openpolicyagent.org/ |
| Argo CD, Flux (GitOps, §5.2.1) | open source | Apache-2.0 | https://argoproj.github.io/cd/ · https://fluxcd.io/ |
| GitHub push protection / dependency review (refs. [12], [13], [15]) | commercial (SaaS) | proprietary | https://docs.github.com/ |
| GitLab secret detection / dependency scanning / push rules (refs. [19]–[21]) | commercial (open core) | MIT (CE) / proprietary (EE) | https://docs.gitlab.com/ |
| Google Cloud Build / Binary Authorization for Cloud Run and GKE (ref. [14]) | commercial | proprietary | https://cloud.google.com/build/docs/securing-builds/secure-deployments-to-run-gke |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, cites, distillation block |
| `distilled/README.md` | index of the distilled artifacts with coverage |
| `distilled/normative.md` | every normative statement verbatim with locator and R-id; Tables 1–3; Fig. 1 transcription |
| `distilled/requirements.yaml` | 126 typed requirements (library-requirements/v2), SSDF `maps_to` from Appendix A |
| `distilled/protocol.yaml`, `distilled/protocol.md` | 4 derived interaction flows with Mermaid sequence diagrams |
| `distilled/state-machine.yaml` | artifact-admission, GitOps-drift and SSC-attack lifecycles |
| `distilled/design-notes.md` | adopt/adapt/reject against R-040–R-044, DEC-009, ARCH-0001, ADR-0001; source inconsistencies |
| `distilled/object-model.yaml`, `distilled/object-model.md` | object-model pass: 62 objects, 45 edges, gaps; Mermaid class diagram |

## Limits

- **No formats.** SBOM, attestation and signing formats are explicitly out of scope (§1.2, §6). So
  is artifact testing that produces tamper-proof test records (§5.1), and the emerging integrated
  "DevSecOps platform" (§6).
- **Not a full SDL.** It omits secure design and design review (SSDF PW.1–PW.4, PW.7) and
  vulnerability response (RV.1–RV.3); see Appendix B. It cannot stand in for SSDF conformance.
- **Lowercase modals throughout,** and the strength sometimes differs between §5 and Appendix A
  (for example online keys: "should not" vs "must not"). See design-notes.
- **Weak sourcing.** Many citations are vendor blogs and product documentation ([4], [5], [7], [9],
  [10], [12]–[21]) rather than standards.
- **Coverage gaps in Appendix A.** Its mapping leaves the process/materials/artifacts attestation and signing/storage, push-protection and most
  GitOps requirements without an SSDF practice, so a Table-2-only crosswalk undercounts the
  document's coverage.

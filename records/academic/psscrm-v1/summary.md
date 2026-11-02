---
schema: "library-summary/v1"
id: psscrm-v1
record: psscrm-v1
type: summary
updated: "2026-11-01"
---

# Proactive Software Supply Chain Risk Management Framework (P-SSCRM) Version 1

|  |  |
|---|---|
| **Type** | paper (framework, arXiv preprint, "will not be submitted to a conference") |
| **Maturity** | `white-paper`: authors' framework, no standards body |
| **Authors** | Laurie Williams, Sammy Migues, Jamie Boote, Ben Hutchison |
| **Published** | Version 1.01, 28 April 2025. First submitted 18 April 2024 |
| **Identifier** | arXiv:2404.12300 |
| **Source** | https://arxiv.org/pdf/2404.12300v4 |
| **Digest** | `sha256:751228a9…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

P-SSCRM unifies ten government and industry frameworks with observations from nine real initiatives into 73 tasks, in 15 practices and four groups (Governance, Product, Environment, Deployment). It presents itself as descriptive, reporting what assessed organisations do, not prescribing what they should. Each task maps back to its sources, so it works as a crosswalk: Table 1 shows that all of EO 14028, SSDF, self-attestation, SLSA v1.0, SCVS, S2C2F and CNCF SSC are absorbed, but only 37 of BSIMM13's 125 tasks and 44 of NIST 800-161's 183. Automatic detection is thin: only nine tasks are detectable from OpenSSF Scorecard (Table 1). Funded by Synopsys.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Programme-level task model, not a mechanism |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | The task mapping the sponsor asked for in the final report |

It bears on no open `DEC-*` or `R-*`. It is a reporting obligation: mofn PROC-0004 and the project plan name a P-SSCRM task mapping for the final report. G.1.3 (produce attestation, naming in-toto) and G.1.4 (deliver provenance) are the tasks nearest to what mofn builds. The `uptake-failure` topic is a loose fit, because this document says nothing on why SPKI or PICS failed.

## Implementations

None applicable: a framework. It names OpenSSF Scorecard for automatic detection of nine tasks. Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this file |

No `distilled/`: a summary-bar fill, and a `paper` record is outside FX-1 scope.

## Limits

Read: most of pp.1-11 (front matter, introduction, structure, provenance of the tasks). Of the task tables on pp.12-18, only G.1.3 and G.1.4 were read, so no other task is described here, and the mapping itself is not done. The nine initiatives are not named in what was read. The authors' descriptive claim cannot be checked from the paper: the underlying interview data is not published in it. "P-SSCRM1" is a snapshot of 2022-23 data, so it predates later SLSA versions.

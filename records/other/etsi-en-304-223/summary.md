---
schema: "library-summary/v1"
id: etsi-en-304-223
record: etsi-en-304-223
type: summary
updated: "2026-10-01"
---

# Securing Artificial Intelligence (SAI); Baseline Cyber Security Requirements for AI Models and Systems

|  |  |
|---|---|
| **Type** | spec (European Standard) |
| **Maturity** | `standard` — EN adopted 2025-12-08; national transposition by 2026-09-30 |
| **Authors** | ETSI Technical Committee Securing Artificial Intelligence (SAI) |
| **Published** | 2025-12 — V2.1.1 |
| **Identifier** | ETSI EN 304 223 V2.1.1 (REN/SAI-0022) |
| **Source** | https://www.etsi.org/deliver/etsi_en/304200_304299/304223/02.01.01_60/en_304223v020101p.pdf |
| **Digest** | `sha256:1ef542acf1fac7f108aa0b3c8548d91d82395fe026f0036bffe7f1f32456d21a` |

## Overview

The European baseline for securing AI models and systems, including generative AI (§1). It
sets **13 principles** across five lifecycle phases — secure design, development, deployment,
maintenance and end of life — and **72 numbered provisions** (49 *shall*, 23 *should*), each
assigned to stakeholders: Developers, System Operators, Data Custodians and End-users (§4,
§5). It treats AI as different from ordinary software because of risks such as data
poisoning, model obfuscation and indirect prompt injection (Introduction), and requires
threat modelling that covers AI-specific attacks (5.1.3-1), human oversight (5.1.4), audit
trails of models, datasets and prompts (5.1.2-3, 5.2.4-1, 5.2.4-3), and published hashes of
shared model components (5.2.4-1.2). It was first published as ETSI TS 104 223 V1.1.1
(April 2025) and became this EN in December 2025 (History).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A baseline security requirement set for AI systems |
| Cryptography | `adjacent` | Requires cryptographic hashes for shared model components (5.2.4-1.2); specifies no algorithm |
| This project | `core` | The testable requirement set behind tmodel #13; names AI threats the object model must express |

`bears_on: DEC-001` — 5.1.3-1 asks threat models to address data poisoning, model inversion
and membership inference; `distilled/normative.md` §4 lists every AI threat the standard
names. `bears_on: R-018` — Principle 4 asks for human oversight and outputs humans can
assess, matching ARCH-0001 §7.

## Implementations

Nothing to list. This is a requirements standard, not a file format or protocol, so no
software "implements" it. Conformance is to be assessed under ETSI TS 104 216, which is still
a draft work item; tools for individual provisions (e.g. NeMo-Guardrails, cited as [i.25])
belong in their own records.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, including all 25 informative references as `cites` |
| `summary.md` | this document |
| `distilled/README.md` | index of the distillation, the checks run and their results |
| `distilled/requirements.yaml` | **machine source:** all 72 provisions, verbatim, typed for audit |
| `distilled/requirements.md` | human view of the provisions, generated from the YAML |
| `distilled/normative.md` | stakeholders, the 13 principles by phase, AI threats named, bearing on tmodel |

## Limits

- **No way to check conformance yet.** The provisions are high-level ("shall analyse threats
  and manage security risks"), and the companion that would say how to assess them,
  TS 104 216, is unpublished.
- **Who is obliged is sometimes unclear.** Four provisions name no stakeholder (marked
  `(implied)` in the YAML), and several bind "Developers and/or System Operators" jointly.
- **Generic on threats.** It names AI attack classes but offers no taxonomy or catalogue;
  pair it with MITRE ATLAS or NIST AI 100-2 (both cited informatively) for that.
- **Predecessor not held.** TS 104 223 V1.1.1 is not yet a record, so no `supersedes` link.

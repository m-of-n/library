---
schema: "library-summary/v1"
id: etsi-en-304-223
record: etsi-en-304-223
type: summary
updated: "2026-11-15"
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
maintenance and end of life — and **72 numbered provisions** (49 *shall*, 23 *should*, by
the strongest verbal form in each), addressed to stakeholders: Developers, System Operators,
Data Custodians and End-users (§4, §5). Principle 10 names no stakeholders it primarily applies
to, and some provisions name no obliged party. It treats AI as different from ordinary
software because of risks such as data poisoning, model obfuscation and indirect prompt
injection (Introduction). It requires threat analysis and risk management (5.1.3-1) and only
recommends that threat modelling address AI-specific attacks; it requires technical measures
where human oversight is a risk control (5.1.4-3) and recommends oversight capabilities
(5.1.4-1); it requires audit trails of models, datasets and prompts (5.1.2-3) and of system
design and maintenance plans (5.2.4-1), recommends an audit log of prompt and configuration
changes (5.2.4-3), and requires published hashes of shared model components (5.2.4-1.2). It was
first published as ETSI TS 104 223 V1.1.1 (April 2025) and became this EN in December 2025
(History).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A baseline security requirement set for AI systems |
| Cryptography | `adjacent` | Requires cryptographic hashes for shared model components (5.2.4-1.2); specifies no algorithm |
| This project | `core` | The testable requirement set behind tmodel #13; names AI threats the object model must express |

`bears_on: tmodel:DEC-001` — 5.1.3-1 recommends that threat modelling address data poisoning,
model inversion and membership inference. The other AI attacks the EN names are adversarial
attacks (5.1.2-2), reverse engineering of the model or its training data and unintended
influence through outputs (5.2.5-4, 5.2.5-4.1), and, in the Introduction only, model
obfuscation and indirect prompt injection; `distilled/design-notes.md` maps clause 5.1.3 onto
what a threat model must carry. `bears_on: tmodel:R-018` — Principle 4 asks for human
oversight and outputs humans can assess, matching tmodel's ARCH-0001 §7.

## Implementations

Nothing to list. This is a requirements standard, not a file format or protocol, so no
software "implements" it. Conformance is to be assessed under ETSI TS 104 216, which is still
a draft work item; tools for individual provisions (e.g. NeMo-Guardrails, cited as [i.25])
belong in their own records.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, including all 25 informative references as `cites`; FX-1 coverage of each artifact |
| `summary.md` | this document |
| `distilled/README.md` | index of the FX-1 extraction |
| `distilled/requirements.yaml` | **machine source:** the 72 provisions under their original ids, each split into sentence entries (`R-NNNN`) with actor, normativity and testability; scope and applicability lines; inferred obligations flagged |
| `distilled/inferred-candidates.yaml` | every keyword-less sentence that might bind, and every verbal form in informative text, each with a verdict |
| `distilled/normative.md` | the normative text by clause, quoted by line marker, and the source defects (SD-1 to SD-19) |
| `distilled/messages.yaml`, `distilled/schema/` | the work products the provisions require, and JSON Schemas derived from them |
| `distilled/protocol.yaml`, `distilled/protocol.md` | process flows between stakeholder roles, with diagrams |
| `distilled/state-machine.yaml` | the lifecycles the provisions imply |
| `distilled/examples/` | the finding that the EN has no examples or test vectors; our schema test cases |
| `distilled/design-notes.md` | how the EN bears on tmodel's and mofn's decisions, and open questions |

## Limits

- **No way to check conformance yet.** The provisions are high-level ("shall analyse threats
  and manage security risks"), and the companion that would say how to assess them,
  TS 104 216, is unpublished.
- **Who is obliged is sometimes unclear.** Five provisions carry only an implied actor
  (5.1.1-1.1, 5.1.1-2.1, 5.1.2-1.1, 5.1.3-1.1, 5.2.4-2.1; marked `(implied)` in the YAML), 14
  binding sentences name no obliged party (SD-15 in `distilled/normative.md`), and several bind
  "Developers and/or System Operators" without saying whether one of them suffices (SD-16).
- **Generic on threats.** It names AI attack classes but offers no taxonomy or catalogue;
  pair it with MITRE ATLAS or NIST AI 100-2 (both cited informatively) for that.
- **Predecessor not held.** TS 104 223 V1.1.1 is not yet a record, so no `supersedes` link.

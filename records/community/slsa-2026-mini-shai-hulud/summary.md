---
schema: "library-summary/v1"
id: slsa-2026-mini-shai-hulud
record: slsa-2026-mini-shai-hulud
type: summary
updated: "2026-11-01"
---

# Mini Shai-Hulud: Where SLSA's Boundaries Fall

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | informational |
| **Authors** | Andrew McNamara |
| **Published** | 2026-05-15, SLSA project blog |
| **Identifier** | https://slsa.dev/blog/2026/05/mini-shai-hulud-what-slsa-can-and-cannot-do |
| **Source** | https://slsa.dev/blog/2026/05/mini-shai-hulud-what-slsa-can-and-cannot-do |
| **Digest** | `sha256:7bc3af34…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

A SLSA post on the May 2026 npm attack, in which 84 artifacts across 42 `@tanstack` packages were published through legitimate CI. An attacker chained a `pull_request_target` workflow, cache poisoning and extraction of an OIDC token from runner memory. The resulting attestations were cryptographically valid and named the correct repository and workflow, so an expected-builder check would have passed. The post argues that the attestation is accurate and the build was compromised, and that SLSA Build L3 isolation would have blocked this vector. It distinguishes evidence (*what happened?*) from policy (*was that good enough?*).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A live attack that defeated provenance verification without forging anything |
| Cryptography | `adjacent` | Signatures and Sigstore worked as designed |
| This project | `core` | Direct evidence that strong evidence does not imply entitlement |

- **R-M-07**: digest and provenance were correct and useless. This is the sharpest available argument that binding is necessary and not sufficient.
- **R-O-02**: a short-lived OIDC token was stolen from process memory and used inside its window. Short lifetime narrows exposure, it does not stop use.
- **Topic**: the post says SLSA records evidence and policy decides what is acceptable, which is the topic's own distinction, in the project's words.

## Implementations

None applicable: this source describes an incident, not something to build on. No search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A web source has no FX-1 obligation, and nothing here needed a further artifact.

## Limits

- **The counterfactual is the author's.** The claim that an L3 builder would have stopped this is an argument from requirements, not a test.
- **A tension in the argument.** The post says an attacker who fully controls code inside a trusted builder can still produce conforming provenance, and also that L3 addresses this class of attack. The second claim depends on L3 keeping that code out, and the post names no platform where this was tested.
- **Secondary source.** Attack details come from TanStack's postmortem and GHSA-g7cv-rxg3-hmpx, which were not read here.
- **Read scope.** The whole post was read. No package from the incident was fetched.

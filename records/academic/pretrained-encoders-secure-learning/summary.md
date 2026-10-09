---
schema: "library-summary/v1"
id: pretrained-encoders-secure-learning
record: pretrained-encoders-secure-learning
type: summary
updated: "2026-10-01"
---

# Pre-trained Encoders in Self-Supervised Learning Improve Secure and Privacy-preserving Supervised Learning

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_ — workshop paper; standing not checked |
| **Authors** | Hongbin Liu, Wenjie Qu, Jinyuan Jia, Neil Zhenqiang Gong |
| **Published** | 2022-12-06 (arXiv); accepted at SAGAI'24 |
| **Identifier** | arXiv:2212.03334 |
| **Source** | https://arxiv.org/pdf/2212.03334 |
| **Digest** | `sha256:4ca85a38891f99bcc5fe2e86201f7817adeca10cd3b247c5b5fdfe1a4015ec86` |

## Overview

A measurement study on image **classifiers**, not GenAI applications. Building a classifier
on a clean encoder pre-trained on public data (OpenAI's CLIP) makes certified defenses —
against data poisoning and backdoors (bagging, KNN), adversarial examples (randomized
smoothing) and privacy attacks (differential privacy, exact unlearning) — both more
accurate and stronger (§1). Example on STL10: bagging accuracy rises from 0.352 to 0.979
and the certified poisoning size from 1.3 to 68.8; differentially private accuracy rises
from 0.237 to 0.956 (§1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Training-time and model attacks, at model level |
| Cryptography | `none` | — |
| This project | `none` | tmodel does not train classifiers; it names threat classes (poisoning, membership inference) that other records cover |

Bears on no open decision. `usefulness: marginal` — kept because it is a SAGAI'24 paper.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Assumes a clean encoder.** Attacks on the pre-trained encoder itself are out of scope
  (§3, §9).
- **Not about GenAI systems**, which is the focus of the rest of this topic.

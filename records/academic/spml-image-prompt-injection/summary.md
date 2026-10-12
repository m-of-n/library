---
schema: "library-summary/v1"
id: spml-image-prompt-injection
record: spml-image-prompt-injection
type: summary
updated: "2026-10-01"
---

# Defending Language Models Against Image-Based Prompt Attacks via User-Provided Specifications

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_ — workshop paper; standing not checked |
| **Authors** | Reshabh K Sharma, Vinayak Gupta, Dan Grossman (University of Washington) |
| **Published** | 2024 — IEEE SPW 2024 (SAGAI'24) |
| **Identifier** | IEEE Xplore 10579532 |
| **Source** | https://homes.cs.washington.edu/~reshabh/SAGAI.pdf (author copy) |
| **Digest** | `sha256:e315bf3a3488339f9e93c6150e90685387330e26c794be8e4832ec4972a4a1f8` |

## Overview

Multimodal chatbots can be prompt-injected through **images** (text written on, hidden in
or blended into a picture), which text-only defenses never see (§I-A, §II). The paper's
defense runs two checks driven by developer-written specifications in SPML, a small
language for chatbot definitions: **input validation** rejects images that do not match
what the chatbot is meant to accept (§III), and **injection detection** reads the image as
if it were an instruction and drops the interaction when the chatbot behaviour it implies
differs from the real specification (§IV). In a small case study (7 attack images, 3
models), every image that actually succeeded against a model was detected; detection was
100% with GPT-4-Vision, 42.8% with LLaVA-13B and 0% with MiniGPT-4 (§VI).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Prompt injection via a new input channel, and a defense |
| Cryptography | `none` | — |
| This project | `adjacent` | Widens the AI threat types the object model must express (DEC-001) |

`bears_on: DEC-001`.

## Implementations

Not searched. SPML itself is described in `cites` (arXiv 2402.11755).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **The checker can be attacked too.** Both checks use a multimodal model that the same
  input may manipulate (§VII).
- **Small evaluation.** 7 attack images, 2 valid images, one example chatbot (§V–VI).
- **Model-dependent.** The checker must be at least as capable as the chatbot's own model
  (§VI).

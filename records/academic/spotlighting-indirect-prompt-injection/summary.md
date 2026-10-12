---
schema: "library-summary/v1"
id: spotlighting-indirect-prompt-injection
record: spotlighting-indirect-prompt-injection
type: summary
updated: "2026-10-01"
---

# Defending Against Indirect Prompt Injection Attacks With Spotlighting

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_ — workshop paper; standing not checked |
| **Authors** | Keegan Hines, Gary Lopez, Matthew Hall, Federico Zarfati, Yonatan Zunger, Emre Kıcıman (Microsoft) |
| **Published** | 2024-03-20 (arXiv); accepted at SAGAI'24 |
| **Identifier** | arXiv:2403.14720 |
| **Source** | https://arxiv.org/pdf/2403.14720v1 |
| **Digest** | `sha256:8c57c6da480eb46c0deaec1f34dfd98fc75810bd352d4391c6f423430774877d` |

## Overview

An LLM receives its instructions and any outside data as one stream of text, so it cannot
tell "code" from "data". **Indirect prompt injection** exploits this: an attacker plants
instructions in content the LLM later processes (a web page, an email, a document), and
they run in the victim's session (§1, §2.2). **Spotlighting** transforms the untrusted input
so its origin stays visible to the model — *delimiting* (markers around it), *datamarking*
(a token interleaved through it) or *encoding* (e.g. base64) — and tells the model in the
system prompt never to follow instructions inside it (§3). On 2023 GPT models, attack
success fell from over 50% to under 2% with little loss of task performance (abstract,
§5).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Defines and measures a defense for a core LLM attack class |
| Cryptography | `none` | Encoding is used as marking, not as cryptography |
| This project | `adjacent` | Indirect prompt injection is an AI threat type the object model must express (DEC-001); tmodel's own AI features read third-party text too |

`bears_on: DEC-001`.

## Implementations

Not searched. The technique is prompt engineering an application implements itself.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Not a guarantee.** The authors do not know why it works and say it is not perfectly
  secure; a real fix would carry instructions and data in separate channels, which current
  models do not support (§6).
- **Narrow evaluation.** 2023 GPT models and a simple keyword-payload attack (§4).
- **Delimiting is weak.** An attacker who learns the delimiters can forge them; the authors
  recommend datamarking at least, encoding for high-capacity models, and randomizing the
  marking token per request (§5.3–5.4).

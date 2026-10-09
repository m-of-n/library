---
schema: "library-summary/v1"
id: llm-programmatic-dual-use
record: llm-programmatic-dual-use
type: summary
updated: "2026-10-01"
---

# Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_ — workshop paper; standing not checked |
| **Authors** | Daniel Kang, Xuechen Li, Ion Stoica, Carlos Guestrin, Matei Zaharia, Tatsunori Hashimoto |
| **Published** | 2023-02-11 (arXiv); accepted at SAGAI'24 |
| **Identifier** | arXiv:2302.05733 |
| **Source** | https://arxiv.org/pdf/2302.05733v1 |
| **Digest** | `sha256:3340777038e9909067f6deed3e1b7a57cd6bb98ff3c9e25148c9512bec601adf` |

## Overview

Instruction-following LLMs behave like programs — they concatenate strings, assign
variables, follow sequences and branch (§2) — so classic program attacks carry over to
**misuse**, where the user tries to get a hosted model to write scams, phishing or hate
speech: obfuscation (typos, synonyms), code injection / payload splitting, and
virtualization (a fictional scenario built over several prompts) (§3.3–3.4). Obfuscation
and virtualization bypassed OpenAI's input filter, output filter and refusals in 100% of
tested scenarios (Table 1, §4), and generated scams were convincing and cheap ($0.0064–
$0.016 each) (§5–6). The authors argue input filtering is fundamentally limited and that
defenses should borrow from traditional security, such as sandboxing (§3.5, §8).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Content-filter bypass and LLM misuse |
| Cryptography | `none` | — |
| This project | `adjacent` | Names misuse / filter bypass as an AI threat type (DEC-001) |

`bears_on: DEC-001`.

## Implementations

Not applicable: the authors withheld their prompts from release (Responsible Disclosure).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Dated targets.** Early-2023 OpenAI models; OpenAI patched the specific prompts, though
  modified ones still worked (§1).
- **Misuse, not injection.** The attacker is the user; this does not cover third-party
  content attacking an application (see `spotlighting-indirect-prompt-injection`).

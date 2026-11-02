---
schema: "library-summary/v1"
id: eu-ai-act-art-50
record: eu-ai-act-art-50
type: summary
updated: "2026-11-01"
---

# EU AI Act Article 50: Transparency Obligations

|  |  |
|---|---|
| **Type** | spec (regulation, one article, read from a secondary rendering) |
| **Maturity** | `standard`: enacted law |
| **Authors** | European Parliament and Council |
| **Published** | Official Journal, 12 July 2024 (per the Explorer). Art. 50 comes into force 2 August 2026 |
| **Identifier** | Regulation (EU) 2024/1689, Article 50 |
| **Source** | https://artificialintelligenceact.eu/article/50/ |
| **Digest** | `sha256:ce8ce007…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Article 50 sets four transparency duties. Interactive AI must tell people they are dealing with AI (§1). Providers of systems generating synthetic audio, image, video or text must mark outputs in a machine-readable format and make them detectable, with solutions effective, interoperable, robust and reliable as far as technically feasible (§2). Deployers of emotion recognition or biometric categorisation must inform those exposed (§3), and deployers must disclose deep fakes and AI-generated public-interest text, unless it has had human editorial control (§4). §7 provides for codes of practice, assessed by the Commission, with implementing acts as a fallback. It names no technique: "marked" could mean a watermark or signed metadata.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Machine-readable marking, not an authenticity guarantee |
| Cryptography | `none` | Names no cryptographic mechanism |
| This project | `adjacent` | A statutory demand for statements, in a market mofn might serve |

`DEC-005`: it does not choose an envelope, but "interoperable" (§2) favours one a third party can verify without our tooling. It is also evidence for R-0004 §4.1. The obligation falls on AI providers and deployers, so it creates supply for AI output only, not for artifacts in general.

## Implementations

None applicable: legislation. See `eu-code-of-practice-marking` for the techniques. Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this file |

No `distilled/`: a summary-bar fill, not an extraction. FX-1 would apply to this `spec` record if extracted; no issue owns that.

## Limits

Read: Article 50 whole, on the AI Act Explorer. This is a **secondary rendering**: the Official Journal text was not read, and its hover-glossary text had to be stripped by hand. No wording here should be quoted without checking EUR-Lex.

**Amendment not resolved.** The Explorer shows two versions of §7 under an "amended" marker. Search snippets (2026-11-01, law-firm notes, not the act itself) report that the Digital Omnibus on AI entered into force on 27 July 2026 and gives systems on the market before 2 August 2026 until 2 December 2026 to meet §2. We did not read the Omnibus, so the dates above are the base Regulation's. It needs a check before any citation of the deadline, including R-0004 §4.1.

It does not say how "marked" is judged, and it does not settle whether signed metadata that is stripped still satisfies §2. Recitals 132-135 were not read.

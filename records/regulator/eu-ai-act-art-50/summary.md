---
schema: "library-summary/v1"
id: eu-ai-act-art-50
record: eu-ai-act-art-50
type: summary
updated: "2026-11-04"
---

# EU AI Act Article 50: Transparency Obligations

|  |  |
|---|---|
| **Type** | spec (regulation, one article, read from a secondary rendering) |
| **Maturity** | `standard`: enacted law |
| **Authors** | European Parliament and Council |
| **Published** | Official Journal, 12 July 2024 (OJ L, 2024/1689, as cited in the Omnibus recital 1 on the Explorer). Art. 50 applies from 2 August 2026 (the Explorer: "Comes into force 2 August 2026, according to Article 113") |
| **Identifier** | Regulation (EU) 2024/1689, Article 50 |
| **Source** | https://artificialintelligenceact.eu/article/50/ |
| **Digest** | `sha256:ce8ce007…` (full value in `record.yaml`), fetched 2026-11-01; not reproducible, see `record.yaml` note |

## Overview

Article 50 sets four transparency duties. Interactive AI must tell people they are dealing with AI (§1). Providers of systems generating synthetic audio, image, video or text must mark outputs in a machine-readable format and make them detectable, with solutions effective, interoperable, robust and reliable as far as technically feasible (§2). Deployers of emotion recognition or biometric categorisation must inform those exposed (§3), and deployers must disclose deep fakes and AI-generated public-interest text, unless it has had human editorial control (§4). §7, as replaced by the Digital Omnibus, provides for codes of practice, assessed by the Commission for adequacy, with implementing acts as a fallback if a code is inadequate. It names no technique: "marked" could mean a watermark or signed metadata.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Machine-readable marking, not an authenticity guarantee |
| Cryptography | `none` | Names no cryptographic mechanism |
| This project | `adjacent` | A statutory demand for statements, in a market mofn might serve |

It bears on no open `DEC-*` or `R-*`. The word "interoperable" in §2 does not separate the options of DEC-005 (DSSE or COSE_Sign1 for `ArtifactStatement`), both of which a third party can verify, so `DEC-005` was removed on 2026-11-04 as a stretch. It is evidence for R-0004 §4.1. The obligation falls on AI providers and deployers, so it creates supply for AI output only, not for artifacts in general.

## Relations

- `see_also: eu-code-of-practice-marking`: the code of practice §7 provides for, which the Commission and the AI Board have assessed as adequate.
- `see_also: eu-cra-2024-2847`: R-0004 §4.1 contrasts the two, an AI Act duty to mark against a CRA duty to hold an SBOM in no named format.
- The `ca-sb-942` edge is authored on that record. `c2pa-2-4` was dropped: Article 50 names no technique, and the link runs through the Code and the California record.

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

**Amendment, read from the Explorer only.** The Explorer shows two versions of §7 under an "amended" marker. Its rendering of the Digital Omnibus on AI, Regulation (EU) 2026/1744, says it entered into force on 27 July 2026. Article 1 point 20 replaces §7 (the version summarised above; the old text let the AI Office facilitate codes and the Commission approve them by implementing act). Point 39 adds Article 111(4): providers whose systems were placed on the market before 2 August 2026 must comply with §2 by 2 December 2026. R-0004 §4.1's "applies from 2 August 2026" holds for new systems only. The Omnibus is not a library record; read on the Explorer, not in the Official Journal.

It does not say how "marked" is judged, and it does not settle whether signed metadata that is stripped still satisfies §2. Recitals 132-135 were not read.

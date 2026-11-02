---
schema: "library-summary/v1"
id: ide-2025-signals-of-provenance
record: ide-2025-signals-of-provenance
type: summary
updated: "2026-11-01"
---

# Signals of Provenance: Practices & Challenges of Navigating Indicators in AI-Generated Media for Sighted and Blind Individuals

|  |  |
|---|---|
| **Type** | paper (preprint) |
| **Maturity** | unset. **Withdrawn 2026-06-16** |
| **Authors** | Ayae Ide, Tory Park, Jaron Mink, Tanusree Sharma |
| **Published** | v1 2025-05-21 · v2 withdrawal 2026-06-16 |
| **Identifier** | arXiv:2505.16057 |
| **Source** | https://arxiv.org/pdf/2505.16057v1 (v1, withdrawn) |
| **Digest** | `sha256:05821760…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

**Do not cite this as evidence. The authors withdrew it on 2026-06-16, and arXiv gives the reason as an error in the reporting of results. The error is not identified, so any result in v1 may be affected.** v1 reports semi-structured interviews (N=28) with 15 sighted and 13 blind or low-vision participants, about self-disclosed AI indicators on YouTube, TikTok and Instagram. It claims both groups overlooked platform labels and used titles, descriptions and comments instead, and that indicators were less accessible to blind and low-vision users. Its §7.4 proposes a canonical machine-readable disclosure schema decoupled from presentation, a public disclosure registry modelled on certificate transparency, and a tiered controlled vocabulary of labels.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `none` | Usability of disclosure labels, not a security analysis |
| Cryptography | `none` | None. §7.4 only sketches signed entries in an append-only log |
| This project | `adjacent` | The §7.4 design proposals are worth reading as proposals. The empirical results are not usable |

- **DEC-007**: §7.4's call to decouple disclosure logic from presentation, with level-tiered labels in several modalities, restates DEC-007's option 2 from the accessibility side. That is an argument, and it stands or falls without the withdrawn data. It adds one thing DEC-007 does not say: a rendering may need to be non-visual. **DEC-007** is proposed, not accepted: it exists only in ARCH-0001-PROPOSAL v0.2.0 §5, and mofn's DECISIONS-0001 item 5d asks whether it survives at all.

## Implementations

None applicable: this is a study, not software, and no implementation search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. No issue owns the eventual extraction of this record yet.

## Limits

- **Withdrawn, and the error is unidentified.** Nothing here should be repeated as a result. No published version was found: Crossref and OpenAlex title searches and one web search on 2026-11-01 returned none, and that is a weak negative.
- **The platforms were not C2PA surfaces as such.** The study concerns self-disclosed labels. C2PA appears as background and as the model for the proposed schema (§2.2, §7.4).
- **Small and qualitative**, by its own design, so even uncorrected it would not generalise.
- **Read scope.** v1 only; v2 is an empty withdrawal notice. Read: abstract, start of §1, starts of §5.2 and §5.3, Table 4, §7 and §8. §2, §3, §4 and most of §5 and §6 were not read. That is deliberate: reading results that their authors withdrew would add nothing we could use.

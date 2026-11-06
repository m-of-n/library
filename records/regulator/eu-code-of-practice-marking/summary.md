---
schema: "library-summary/v1"
id: eu-code-of-practice-marking
record: eu-code-of-practice-marking
type: summary
updated: "2026-11-04"
---

# Code of Practice on Transparency of AI-Generated Content

|  |  |
|---|---|
| **Type** | web record; the source is the 38-page Code PDF |
| **Maturity** | `best-practice`: voluntary code, assessed adequate by the Commission and the AI Board |
| **Authors** | The six working group chairs and vice-chairs named on the cover: K. Bontcheva, A. Bechmann, D. Pedreschi, G. De Gregorio, C. Riess, M. Botan |
| **Published** | 10 June 2026 |
| **Identifier** | Commission press item of 10 June 2026 (IP/26/1328) |
| **Source** | https://ec.europa.eu/newsroom/dae/redirection/document/129555 |
| **Digest** | `sha256:7bd22c5a…` (full value in `record.yaml`), fetched 2026-11-01, rechecked 2026-11-04 |

## Overview

The voluntary route to compliance with AI Act Article 50. Section 1 (providers) holds that no single technique currently meets Art. 50(2), so signatories apply at least two machine-readable layers: digitally signed, time-stamped metadata (Sub-measure 1.1.1) and an imperceptible watermark (1.1.2), with fingerprinting or logging optional (1.1.3). Free-form text cannot carry metadata, so one layer suffices there. Detection must be offered, with results disclosed (Commitment 2). Section 2 (deployers) sets the labelling of deep fakes and public-interest text, through the EU icon of Annex 1 or an equivalent label. Signatories rely on the Code to show compliance; others must show adequacy individually. The Commission reports about 190 signatories by the end of July 2026.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Layered marking, explicitly because each layer alone fails |
| Cryptography | `adjacent` | Requires signed metadata and key protection; no algorithm named |
| This project | `adjacent` | The clearest statement of what signed provenance must coexist with |

It bears on no open `DEC-*` or `R-*`. Sub-measure 1.1.1 requires signing and time-stamping but names no format, so it does not inform DEC-005 (DSSE or COSE_Sign1 for `ArtifactStatement`); `DEC-005` was removed on 2026-11-04 as a stretch. Its signature layer alone would not be enough for a signatory, which limits what a signing-only system can claim here. It is evidence for R-0004 §4.1.

## Relations

- `see_also: ca-sb-942`: AB 853's duty on large platforms not to strip standard-compliant provenance data (§22757.3.1(b)) parallels the Code's Measure 1.2 on non-removal of markings.
- `see_also: c2pa-2-4`: by our reading the "relevant established standards" for signed metadata in Measure 3.4(a); the Code names none (see Limits).
- `see_also: nsa-2025-content-credentials`: government guidance on the same signed-metadata layer that, unlike this Code, names Content Credentials.
- The `eu-ai-act-art-50` edge is authored on that record. `cawg-identity-1-2` was dropped: the Code does not cite CAWG, and keeping the edge would repeat the mofn error recorded below.

## Implementations

None named. The Code cites no product or specification (see Limits). Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this file |

No `distilled/`: a summary-bar fill, and this `web` record's source is a code of practice, not a standard under FX-1.

## Limits

Read: Section 1 Commitment 1 (Measures 1.1-1.4), Measure 3.4 and the glossary entries used here, closely. The rest (Commitments 2-4, Section 2) by heading and in part, so none of it is relied on beyond this summary. Also read: the press item, the policy page and the signatories news item. The Commission's Opinion on adequacy was not read; its assessment is taken from the policy page. "about 190" is the Commission's figure, from the policy page.

**Disagreement with mofn.** R-001 §6.4, §6.5 and R-0004 §4.1 say this Code "points at C2PA" and cites CAWG. A full-text search of the PDF finds no "C2PA", "CAWG" or "Content Credentials"; it speaks only of "open standards" and "relevant standards". The Commission's Q&A page has none either. Either those reports read a draft, or the claim came from commentary. They should drop it or cite the source. Text search cannot see inside images, so a human should open the PDF once. The nearest the Code comes is Measure 3.4: interoperability standards "are yet to be developed, except for digitally signed metadata", and signatories will "adopt relevant established standards or best practices to implement metadata marking and detection". That is consistent with C2PA without naming it.

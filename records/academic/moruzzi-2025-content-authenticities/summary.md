---
schema: "library-summary/v1"
id: moruzzi-2025-content-authenticities
record: moruzzi-2025-content-authenticities
type: summary
updated: "2026-11-01"
---

# Content Authenticities: A Discussion on the Values of Provenance Data for Creatives and Their Audiences

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed paper |
| **Authors** | Caterina Moruzzi, Ella Tallyn, Frances Liddell, Billy Dixon, John Collomosse, Chris Elsden |
| **Published** | 2025-06-22, C&C '25, pp. 128-140 |
| **Identifier** | doi:10.1145/3698061.3726918 |
| **Source** | Internet Archive capture of the co-author's copy (URL in `record.yaml`) |
| **Digest** | `sha256:8e853f7a…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

An online workshop with 34 experts across the creative media chain, analysed by reflexive thematic analysis of 275 sticky notes and 221 minutes of transcript (§3). It argues that the need for provenance depends on context (§4.1), that a binary human-or-AI label is not meaningful and whether AI changed the semantics matters more (§4.2), and that provenance signals can raise suspicion and be mistaken for signals of truth (§4.3, §4.6). Participants asked above all about the creator's intent, which the paper treats as an original insight (§4.5, §5.3). It offers a lens of multiple "authenticities", drawn from Dutton, Newman and Smith and others, as a tool for designing flexible systems (§3.5, §5).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `none` | Trust and signalling, not attacks |
| Cryptography | `none` | Mentions C2PA signing as background only (§2.1, Figure 1) |
| This project | `adjacent` | Argues a single fixed rendering cannot fit every reader, which is a constraint on any answer to DEC-007 |

- **DEC-007**: DEC-007 asks how a value becomes words. This paper asks whose words, and for which reader. A vocabulary with one rendering per value would match the binary labels participants rejected, and §5.4 suggests tiered information. Intent (§4.5) is a claim only the issuer can make, so a vocabulary would need a category for it rather than a rendering. **DEC-007** is proposed, not accepted: it exists only in ARCH-0001-PROPOSAL v0.2.0 §5, and mofn's DECISIONS-0001 item 5d asks whether it survives at all.

## Implementations

None applicable: this is a study, not software, and no implementation search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. No issue owns the eventual extraction of this record yet.

## Limits

- **Expert opinion, not behaviour.** A convenience and snowball sample of interested experts (§3.1), who responded to provocation clips, with no measured effects. §4.4's statements about ordinary users are experts' views of them.
- **Lens applied after the fact.** The authenticities categories were applied post-hoc (§3.5). They organise the findings; they were not tested.
- **No design was tested** (§5.4).
- **Conflation check.** The paper's Figure 1 says the manifest sits in XMP metadata. `c2pa-2-4` embeds manifests in JUMBF. This may be shorthand in the caption, but it should not be taken as a description of the format.
- **Read scope.** The whole body, §1 to §6 and Appendix A's first table, in the co-author's copy. References and Appendix B were not read. The ACM text was not compared.

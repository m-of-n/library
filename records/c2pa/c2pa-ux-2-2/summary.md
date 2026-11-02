---
schema: "library-summary/v1"
id: c2pa-ux-2-2
record: c2pa-ux-2-2
type: summary
updated: "2026-11-01"
---

# C2PA User Experience Guidance for Implementers 2.2

|  |  |
|---|---|
| **Type** | spec (informative guidance) |
| **Maturity** | `recommendation`, a mapping |
| **Authors** | none named; C2PA |
| **Published** | undated |
| **Identifier** | version 2.2 |
| **Source** | https://spec.c2pa.org/specifications/specifications/2.2/ux/UX_Recommendations.html |
| **Digest** | `sha256:ecd084d1…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

C2PA's informative guidance on presenting Content Credentials. It proposes four levels of progressive disclosure: L1 presence and status, L2 a summary, L3 full provenance, and L4 forensic tools (§3.1). Its stance is to give users information and not to assert authenticity (§2.1). It offers recommended strings, such as "Signed by [name]" (§3.2), warns that "Made with AI" is ambiguous and discourages AI-edited or AI-enhanced disclosures without verifiable context (§3.3.2), and flags the implied truth effect of partial labelling (§4.3). It wants created and gathered assertions distinguished (§3.4.1), and says what to show when a manifest fails each validation state (§4.5). Custom assertions get no meaning from C2PA, so §3.4.2 leaves each implementer to label them or hide them.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Anti-spoofing placement and failure display (§4.2, §4.5), but it is guidance, not a control |
| Cryptography | `none` | None directly |
| This project | `core` | The live answer to DEC-007's question in the largest deployed system |

- **DEC-007**: confirms the gap from the other side. Words for actions (§3.3.1) and states are examples in an informative document, so each implementer writes its own. §3.4.2 shows the failure directly: an unknown assertion has no declared meaning, so it is labelled by hand or left out. Its four levels could be a requirement on a vocabulary: one value may need more than one rendering. **DEC-007** is proposed, not accepted: it exists only in ARCH-0001-PROPOSAL v0.2.0 §5, and mofn's DECISIONS-0001 item 5d asks whether it survives at all.
- **R-O-06** (proposed): §4.5 is a rendering of separate results, and shows that separating them is not sufficient without agreed words for each failure.
- **R-O-05** (proposed): a Manifest Consumer here regenerates a display from verified data, as the rule requires.

## Implementations

None listed in this document, and no search was run for it. The SDKs are on `c2pa-2-4`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. No issue owns the eventual extraction of this record yet.

## Limits

- **Disagrees with `c2pa-2-4` on validation states, hence `contradicts`.** §4.5 defines Well-formed as hard bindings being intact, and §4.5.3 treats failed hard bindings as not well-formed. §14.3.4 and §14.3.5 of 2.4 do not include content bindings in Well-Formed or Valid; a modified asset is a separate asset state (§14.3.3). §4.5.2 also says uncaptured edits invalidate the signature, whereas in 2.4 such an edit changes the asset, not the claim signature. A reader following this document would hide or mislabel a case 2.4 treats differently. The cause may be version lag, but 2.4 §16.1 still points to this guidance and no later text is reachable.
- **It points to guidance that was not there.** §3.4.3 says CAWG assertions should follow CAWG UX guidance, and `cawg-identity-1-2` §10.1 says that guidance is forthcoming.
- **Internal tension.** §3.1.1 says L1 communicates validation status, and §4.1 says not to add a valid status because the icon alone implies a valid manifest.
- **Little user research is cited.** §5.1 calls research ongoing. `cscw-2023-provenance-trust` found that readers conflate provenance and content credibility; the colours §4.5.1 suggests are the mechanism that study warns about.
- **Read scope.** The whole document, read as extracted text. Figures were not viewed. The 2.2 technical specification was not compared, so the disagreement above is against 2.4 only.

---
schema: "library-summary/v1"
id: cscw-2023-provenance-trust
record: cscw-2023-provenance-trust
type: summary
updated: "2026-11-05"
---

# Examining the Impact of Provenance-Enabled Media on Trust and Accuracy Perceptions

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed paper |
| **Authors** | K. J. Kevin Feng, Nick Ritchie, Pia Blumenthal, Andy Parsons, Amy X. Zhang |
| **Published** | 2023-09-28, PACM HCI 7(CSCW2), Article 270 |
| **Identifier** | doi:10.1145/3610061 · arXiv:2303.12118 |
| **Source** | https://arxiv.org/pdf/2303.12118v3 (author copy) |
| **Digest** | `sha256:92c8e73c…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

An online experiment with 595 valid participants from the US and UK (§3.3.2) showed media in a Twitter-like prototype, without and then with a C2PA-style provenance indicator and details panel. Provenance often lowered trust and helped people doubt deceptive media, especially when it revealed compositing. Incomplete and invalid provenance states lowered trust and perceived accuracy whatever the content claimed, so honest media was sometimes disbelieved (§5.1). The authors' explanation is that participants confused provenance credibility with content credibility, two things the paper calls related but orthogonal (§5.1). A deceptive composite with an intact chain can therefore look better than an honest image with a broken one.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | The failure is a misread signal. §5.1 notes an attacker could introduce incompleteness on purpose, or flood a feed with invalid indicators |
| Cryptography | `none` | Studies a signed format's UI, not its cryptography |
| This project | `adjacent` | Direct evidence on what a verifier's output does to a reader |

- **DEC-007**: rendering is the claim at stake. The experiment shows a correct validation state being read as a verdict on content, so a renderer that shows only a state and a colour would mislead. §5.3 suggests early deployments consider removing colour. **DEC-007** is proposed, not accepted: it exists only in ARCH-0001-PROPOSAL v0.2.0 §5, and mofn's DECISIONS-0001 item 5d asks whether it survives at all.
- **No other id.** An earlier draft also named R-O-06. The paper tests one provenance-state indicator; it does not study separate verifier results, so that was a stretch and is removed.

## Relations

- `see_also: c2pa-2-4`: the prototype implements the C2PA standard (§3.1.3), and the states it tested predate 2.4's (Limits). Authored only here.
- `c2pa-ux-2-2`, `moruzzi-2025-content-authenticities` and `ide-2025-signals-of-provenance` author their edges to this record, so they are not repeated here.

## Implementations

None applicable: this is a study, not software, and no implementation search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. No issue owns the eventual extraction of this record yet.

## Limits

- **It studied C2PA's UI metaphors and nothing else** (§6). The findings do not generalise to other provenance systems.
- **The states are older than the current spec.** The paper uses `normal`, `incomplete` and `invalid` as C2PA's states (§3.1.3). `c2pa-ux-2-2` and `c2pa-2-4` now use well-formed, valid and trusted. No result maps across automatically.
- **Simulated first exposure.** Participants were not taught the states, panels had at most 3 manifests, and there was no longitudinal measure (§3.1.3, §5.3, §6). Signers and details were fabricated to fit each item's backstory (§3.1.3).
- **Coverage gaps.** No composited news media and no composited invalid media (§6). The deceptive media were composites, not generative AI (§6).
- **Author affiliation.** Two authors are at Adobe and one at BBC, both involved in the ecosystem studied. The paper's method was not audited here.
- **Read scope.** arXiv v3, not the ACM version of record. Read: abstract, §3.1.3, §3.3.2, §5, §6, §7. §1, §2, the rest of §3, and §4 with its tables and statistics were not read, so no effect size is reported here. All findings above come from the abstract and §5 to §7.

---
schema: "library-summary/v1"
id: ca-sb-942
record: ca-sb-942
type: summary
updated: "2026-11-04"
---

# California AI Transparency Act SB 942, as amended by AB 853

|  |  |
|---|---|
| **Type** | spec (statute, read as the two chaptered bills) |
| **Maturity** | `standard`: enacted law |
| **Authors** | California Legislature |
| **Published** | SB 942 chaptered 19 September 2024; AB 853 chaptered 13 October 2025 |
| **Identifier** | Cal. Bus. & Prof. Code § 22757 et seq. |
| **Source** | https://web.archive.org/web/20261005023915id_/https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB853 |
| **Digest** | `sha256:9aeaf88e…` (full value in `record.yaml`), fetched 2026-11-01, rechecked 2026-11-04 |

## Overview

SB 942 requires a GenAI provider with over 1,000,000 monthly users to offer a free public detection tool (§22757.2), offer a manifest disclosure, and always include a latent one, conveying provider, system, time and a unique identifier where feasible (§22757.3). Penalties are $5,000 per violation, per day (§22757.4). AB 853 moved the operative date to 2 August 2026 and widened the chain. From 1 January 2027 large online platforms must detect and expose standard-compliant provenance data and not knowingly strip it (§22757.3.1), and GenAI hosting platforms may not knowingly offer non-disclosing systems (§22757.3.2). From 1 January 2028 capture devices first produced for sale on or after that date must offer a latent disclosure and embed one by default, but only to the extent technically feasible and compliant with widely adopted specifications (§22757.3.3).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Mandates authenticity signals; sets no assurance level |
| Cryptography | `adjacent` | AB 853 defines "digital signature" but mandates none |
| This project | `adjacent` | A forcing function that recognises only widely adopted specifications |

It bears on no open `DEC-*` or `R-*`. The platform duties reach only data compliant with "widely adopted specifications adopted by an established standards-setting body" (§22757.3.1(a)(1), (b)), and SB 942's latent disclosure must be "consistent with widely accepted industry standards" (§22757.3(b)(3)). That favours content-provenance formats such as C2PA, not either option of DEC-005 (DSSE or COSE_Sign1 for `ArtifactStatement`), so `DEC-005` was removed on 2026-11-04 as a stretch. It is evidence for R-0004 §4.1, the forcing function PICS lacked.

## Relations

- `see_also: eu-ai-act-art-50`: the EU statute with the same operative date, 2 August 2026, to which AB 853 moved this Act.
- `see_also: c2pa-2-4`: the obvious candidate for a "widely adopted specification", by our reading only; the statute names none.
- The `eu-code-of-practice-marking` edge is authored on that record.

## Implementations

None applicable: a statute. It names no specification. `c2pa-2-4` is the obvious candidate, by our reading only. Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this file |

No `distilled/`: a summary-bar fill, not an extraction. FX-1 would apply to this `spec` record if extracted; no issue owns that.

## Limits

Read whole, both bills as chaptered, from Internet Archive captures of leginfo, because the live site refused our client. These are session laws, not a consolidated code: amendments after AB 853 were not checked. SB 942's §22757.3 is taken as still current because AB 853 does not amend it.

It does not define "latent" beyond "present but not manifest", name any standard, or say what counts as "established". Detection covers image, video and audio; text is out of the tool and disclosure duties. No court or Attorney General reading was consulted.

mofn R-0004 §4.1 says the Act "became operative 2 August 2026 and reaches large platforms and capture-device manufacturers". As enacted, those two duties start in 2027 and 2028. R-001 §6.4 adds that the Act was "deliberately realigned to match the EU timeline"; the bills give no reason for the new date, so that motive needs another source.

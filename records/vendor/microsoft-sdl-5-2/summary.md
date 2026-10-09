---
schema: "library-summary/v1"
id: microsoft-sdl-5-2
record: microsoft-sdl-5-2
type: summary
updated: "2026-10-02"
---

# Microsoft Security Development Lifecycle (SDL) Process Guidance – Version 5.2

|  |  |
|---|---|
| **Type** | spec (vendor process guidance, 168 pp. Word document) |
| **Maturity** | historic — superseded by the current web practice set; Microsoft files it under "Legacy archive" |
| **Authors** | Microsoft Corporation |
| **Published** | May 23, 2012 (title page). The Download Center page (id 29884) shows "Date Published: 7/15/2024" for the same file (2,372,954 bytes, file version 1) — a re-publication date of the page, not of the document (checked 2026-10-03) |
| **Identifier** | Microsoft Download Center id 29884 |
| **Source** | https://download.microsoft.com/download/3/4/3/343bafcb-c685-4a70-9639-ff76bcbb609c/Microsoft%20SDL_Version%205.2.docx (via https://www.microsoft.com/en-us/download/details.aspx?id=29884) |
| **Digest** | `108cd2ee8cc7a1eb082da5a6e8c796a17ad93104e7b00ed772da7e86abf975f2` |
| **Licence** | "Licensed under Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported" (front matter) |

**Version verified 2026-10-02.** The download page still serves 5.2 as the last
version of the process guidance; Microsoft's SDL Resources page lists
"Microsoft SDL Process Guidance Version 5.2" under **Legacy archive**, and the
SDL FAQ answers "Should I use the Microsoft SDL Process Guidance as a resource to
implement the SDL at my organization?" with "No." The current guidance is the
10-practice web set (`microsoft-sdl`). 5.2's own "Changes in This Version":
typographical corrections plus new/updated requirements in Design,
Implementation (two recommendations promoted to requirements) and SDL-LOB, and
updated Appendix N.

## Overview

SDL 5.2 is the detailed process Microsoft applied to its own products: a
pre-SDL training requirement, five phases (Requirements, Design,
Implementation, Verification, Release) and a post-release Response
requirement, each with explicit Security/Privacy *Requirements* (mandatory for
SDL-subject projects) and *Recommendations*. Release is gated by the **Final
Security Review**, run by an assigned security advisor, with outcomes Passed,
Passed (with exceptions) and FSR escalation. It adds SDL-Agile (every-sprint,
bucket and one-time requirement categories) and SDL-LOB (risk-tiered service
levels for line-of-business apps), plus appendices with tool/compiler
requirements, bug bars and a sample security plan.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The classic reference SDL; MAP-0001's phase line comes from it |
| Cryptography | adjacent | crypto requirements in Design/Implementation (e.g. strong crypto only, in the Agile every-sprint list) |
| This project | core | The FSR is the most complete public model of an SDL gate (R-041); its threat-model review and the rule "Create an individual work item for each vulnerability listed in the threat model" (Phase Two > Risk Analysis) are the R-042 check; bug bars and work-item fields feed severity and Finding classification |

Bears on **R-041, R-042, R-044**, and R-040.

## Implementations

Searched 2026-10-02. Tools the document mandates or recommends that still exist:
BinSkim (successor of BinScope; https://github.com/Microsoft/binskim), Microsoft
Threat Modeling Tool (successor of the SDL Threat Modeling Tool), Application
Verifier (Windows SDK), Attack Surface Analyzer
(https://github.com/microsoft/attacksurfaceanalyzer, MIT). Many 2012 tools
(FxCop, CAT.NET, MiniFuzz, RegexFuzzer, BinScope) are retired.

| Name | Kind | License | URL |
|---|---|---|---|
| BinSkim | binary analyzer | see repository | https://github.com/Microsoft/binskim |
| Attack Surface Analyzer | attack surface diff | MIT | https://github.com/microsoft/attacksurfaceanalyzer |
| Microsoft Threat Modeling Tool | threat modeling | freeware | https://www.microsoft.com/download/details.aspx?id=49168 |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, distillation |
| `distilled/README.md` | artifact index |
| `distilled/normative.md` | every requirement/recommendation statement by section, plus Appendices B, M, N |
| `distilled/requirements.yaml` | 510 entries (408 extract pass + 102 added by the verify pass) |
| `distilled/schema/` | derived JSON Schema |
| `distilled/protocol.yaml`, `protocol.md` | FSR and privacy-escalation exchanges |
| `distilled/state-machine.yaml` | phases, applicability, FSR gate, Agile cadence |
| `distilled/examples/` | bug bars, LOB/Agile tables |
| `distilled/design-notes.md` | bearing on our design |
| `distilled/object-model.yaml`, `object-model.md` | object-model pass |

## Limits

- Legacy and Windows-centric (2012 toolchain, Win32/Win64/CE appendices).
- Requirements carry no identifiers; our R-NNNN are document-order ids.
- The "security score of B or above" FSR criterion is never defined.
- Two release criteria are worded differently (bug-bar severity criteria vs
  "no known vulnerabilities ... Critical, Important, Moderate, or Low").
- Proprietary internal resources were omitted by Microsoft ("Proprietary
  technologies and resources that are only available internally at Microsoft
  have been omitted").

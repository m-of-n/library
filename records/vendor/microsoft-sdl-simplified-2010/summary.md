---
schema: "library-summary/v1"
id: microsoft-sdl-simplified-2010
record: microsoft-sdl-simplified-2010
type: summary
updated: "2026-10-02"
---

# Simplified Implementation of the Microsoft SDL

|  |  |
|---|---|
| **Type** | paper (vendor white paper, 17 pp. Word document + companion spreadsheet) |
| **Maturity** | white-paper; historic (Microsoft's Resources page files it under "Legacy archive") |
| **Authors** | Microsoft Corporation |
| **Published** | "Updated November 4, 2010" (title page) |
| **Identifier** | Microsoft Download Center id 12379 |
| **Source** | https://download.microsoft.com/download/f/7/d/f7d6b14f-0149-4fe8-a00f-0b9858404d85/Simplified%20Implementation%20of%20the%20SDL.doc |
| **Digest** | `ef676ae49c83ce0d1a2bb6f6cabb298194ec1bb712d16942da0392356a27d413` (.doc); spreadsheet `094b8e5f382807473fd412835990200f28af1cc2e5e424ababb33b21324049c9` |
| **Licence** | Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported (front matter) |

**Currency verified 2026-10-02.** Still downloadable (id 12379, with
`Simplified SDL_Spreadsheet.xlsx`); the SDL FAQ recommends it ("You should
download and use the Simplified Implementation of the Microsoft SDL white
paper"), while the Resources page lists it under "Legacy archive". Its own text
says it relates to the published process ("There is a strong correlation
between this paper and the published process") — i.e. the SDL 5.x process
guidance; it predates 5.2 (2012).

## Overview

The paper is Microsoft's minimum bar for claiming SDL compliance outside
Microsoft: sixteen mandatory practices grouped by phase (training; security
requirements, quality gates/bug bars, risk assessment; design requirements,
attack surface reduction, threat modeling; approved tools, deprecated
functions, static analysis; dynamic analysis, fuzzing, threat-model and
attack-surface review; incident response plan, Final Security Review,
release/archive), three optional activities, root-cause analysis and periodic
process updates, and an application security verification process built on a
central compliance-tracking application. It positions this set as the
"Advanced" level of the SDL Optimization Model (Basic → Standardized →
Advanced → Dynamic across five capability areas).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The portable statement of the Microsoft SDL |
| Cryptography | adjacent | minimal cryptographic design requirements (Practice 5; spreadsheet Design 3.1.3) |
| This project | core | per-phase quality gates with an approving advisor (R-041), auditor attestation (R-042), compliance-tracking application as source of truth (R-043), numbered practices for the crosswalk (R-044) |

## Implementations

Searched 2026-10-02: the tools named (SDL Threat Modeling Tool, AppVerifier,
banned.h/strsafe.h) survive as the Microsoft Threat Modeling Tool, Application
Verifier (Windows SDK) and banned.h (https://github.com/x509cert/banned).

| Name | Kind | License | URL |
|---|---|---|---|
| Microsoft Threat Modeling Tool | threat modeling | freeware | https://www.microsoft.com/download/details.aspx?id=49168 |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/README.md` | index |
| `distilled/normative.md` | paper + spreadsheet verbatim |
| `distilled/requirements.yaml` | 61 entries (52 extract pass + 9 added by the verify pass) |
| `distilled/schema/` | derived enums and record |
| `distilled/state-machine.yaml` | maturity levels; FSR/release |
| `distilled/design-notes.md` | bearing on our design |
| `distilled/object-model.yaml`, `object-model.md` | object-model pass |

## Limits

- Summary-level by design ("In the interest of brevity, detailed discussion of
  each security activity is omitted"); depth is in SDL 5.2.
- Optimization-model criteria other than "Advanced" are not given.
- The .doc→text conversion cannot recover list bullets at body indent; texts are
  verbatim but list structure is partly flattened.

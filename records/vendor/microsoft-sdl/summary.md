---
schema: "library-summary/v1"
id: microsoft-sdl
record: microsoft-sdl
type: summary
updated: "2026-10-02"
---

# Microsoft Security Development Lifecycle (SDL) — current practice set

|  |  |
|---|---|
| **Type** | spec (vendor process guidance, web) |
| **Maturity** | recommendation (vendor guidance) |
| **Authors** | Microsoft (no individual authors on the pages) |
| **Published** | undated pages; text says "It’s been 20 years since we introduced the Microsoft Security Development Lifecycle" and cites Build 2024 sessions, so ~2024; unchanged as of 2026-10-02 |
| **Identifier** | https://www.microsoft.com/en-us/securityengineering/sdl/practices |
| **Source** | 16 pages under https://www.microsoft.com/en-us/securityengineering/sdl |
| **Digest** | `c55e38c4e36bd83dce9c28f267664b66d110efbdd568670126cbed15b09d8029` (practices index page) |

**Currency verified 2026-10-02.** The practices page lists 10 practices and
says they "will be updated as the SDL, learnings, best practices, and tooling
evolve". The Resources page files *SDL Process Guidance 5.2* and the
*Simplified Implementation* under "Legacy archive". Microsoft's blog post
"Microsoft SDL: Evolving security practices for an AI-powered world"
(2026-02-03, Yonatan Zunger) announces "SDL for AI" focus areas but no change to
the 10-practice web set.

Per-page digests of the bytes fetched (pages embed a per-request Trace Id, so a
re-fetch will not reproduce them):

| page | sha256 |
|---|---|
| `sdl.html` | `bf9c4616142b82023f882e9c0488d4b0a134f6c709133d2672222339868ebb30` |
| `sdl_about.html` | `10359b1914f7fd18316fca485f50e2a1270266eaac2aea5e3f2f14b3924afd6b` |
| `sdl_practices.html` | `c55e38c4e36bd83dce9c28f267664b66d110efbdd568670126cbed15b09d8029` |
| `p01.html` | `e17a29fbbebe236b92735d8b1eb94e2bf014924a06cfd430d9a224f77c6d6277` |
| `p02.html` | `ab017eb6c61111766953aa5ccaa6ad7b84ec85700fe76b1e0fe35b30851d4cb3` |
| `p03.html` | `15c6bd431b73bee957c0ad4b747cf4034e2cb3442fa6a220283dea0ea9752ed3` |
| `p04.html` | `610fbc5166774fc5a68408d0e830687319c1202925480b5d4674f45630683e19` |
| `p05.html` | `4558f6eccb9a548a13986d2c262e4d6633d307e824aa7364839b6a3ad5e346d7` |
| `p06.html` | `bbed9a3c2838ad3c400cb28e34dbe9544c6a4ef370e1eadec682091b98edb1fd` |
| `p07.html` | `e9eaf37776f9118b98343a2d2bd31b25137e8f1496d971f197f42884ec6f26e2` |
| `p08.html` | `5deb8e5e17d9620fe76c6b70e29752784b680e2e5d84a9464d6c5daef08f71f3` |
| `p09.html` | `602fa69b62b75f806dadc30ba92345ef94ecc7594914d00b6694af2424320ea6` |
| `p10.html` | `3f4511ee4b733fc3d1676ffc196775ad2525525fafb575d52b6568098ed7e4e6` |
| `sdl_howto.html` | `3b7f9295a4e78dd0e17b05acdbbfbb33e06fb7697c399b56ccf829615ad0662c` |
| `sdl_faq.html` | `96ec1c6d2c376a013e092793e73923064f35851c6d9547e0e05039cafb134cfd` |
| `sdl_resources.html` | `d10cb7f9ef9bd7605636045e360c35bfda16943ab9aaf09c27252ec1294d6ddd` |

## Overview

The current Microsoft SDL is ten practices — standards/metrics/governance,
proven security features, design review and threat modeling, cryptography
standards, supply chain, engineering environment, security testing, operational
platform security, monitoring and response, training — each with numbered
sub-practices (48 in all) and links to Microsoft and GitHub tooling. It is
framed for DevSecOps across four stages (Design, Code, Build and Deploy, Run)
under Zero Trust principles. Unlike SDL 5.2 it has no phase gates, no
mandatory/optional requirement split and no Final Security Review; its strongest
process content is the threat-modeling method (practice 3) and the security
exception process (1.4).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Microsoft's current SDL; practice 3 is a threat-modeling method |
| Cryptography | adjacent | Practice 4: TLS, PQC, crypto agility, key/certificate lifecycle |
| This project | core | Practice 3 ≈ tmodel's core layers; 1.4 exception lifecycle → accept disposition (R-042, DEC-009); kinds of mitigation (R-040); ids targeted by SAMM's crosswalk (R-044) |

Bears on **R-040, R-041, R-042, R-044, DEC-009**.

## How it relates to the others

- **Supersedes** `microsoft-sdl-5-2` (2012 process guidance), which Microsoft
  now files as legacy; see also `microsoft-sdl-simplified-2010`.
- **OWASP SAMM** maps 47 stream pairs onto these sub-practice ids.
- Practice 1.1 points to the **NIST SSDF** (`sp-800-218`) as a starting
  standard; the Resources page links a **SAFECode** white paper on third-party
  components.

## Implementations

Searched 2026-10-02 (from the Resources page and practice pages).

| Name | Kind | License | URL |
|---|---|---|---|
| Microsoft Threat Modeling Tool | threat modeling tool | proprietary freeware | https://www.microsoft.com/download/details.aspx?id=49168 |
| DevSkim | IDE security linter | MIT | https://github.com/Microsoft/DevSkim |
| BinSkim | binary SDL compliance checker | see repo (GitHub reports "other") | https://github.com/Microsoft/binskim |
| Attack Surface Analyzer | system-change analysis | MIT | https://github.com/microsoft/attacksurfaceanalyzer |
| SBOM Tool | SBOM generator | MIT | https://github.com/microsoft/sbom-tool |
| CoseSignTool | artifact signing | MIT | https://github.com/microsoft/CoseSignTool |
| CodeQL | SAST engine | GitHub CodeQL terms | https://codeql.github.com/ |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, distillation block |
| `distilled/README.md` | artifact index |
| `distilled/normative.md` | all practice and sub-practice text |
| `distilled/requirements.yaml` | 73 entries |
| `distilled/state-machine.yaml` | exception lifecycle |
| `distilled/protocol.yaml`, `protocol.md` | exception exchange |
| `distilled/examples/threat-modeling-examples.yaml` | practice-3 example lists |
| `distilled/design-notes.md` | bearing on our design |
| `distilled/object-model.yaml`, `object-model.md` | object-model pass |

## Limits

- Guidance, not a standard: no keyword convention, no conformance criteria, no
  work-product list, no gate.
- Heavily product-linked (Azure, GitHub); vendor-neutral content must be
  separated from product pointers.
- Undated and silently editable: a re-fetch may differ; the capture is the
  reference for these artifacts.
- Small editorial defects (duplicated 3.4/3.5 paragraph; garbled practice-10
  sentence; title variant "secure" vs "security" design review).

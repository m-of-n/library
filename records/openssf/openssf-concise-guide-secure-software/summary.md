---
schema: "library-summary/v1"
id: openssf-concise-guide-secure-software
record: openssf-concise-guide-secure-software
type: summary
updated: "2026-10-02"
---

# Concise Guide for Developing More Secure Software

|  |  |
|---|---|
| **Type** | web (living guidance page; secondary reference) |
| **Maturity** | best-practice (OpenSSF Best Practices WG guidance) |
| **Authors** | OpenSSF Best Practices Working Group (byline; content edited by David A. Wheeler et al.) |
| **Published** | byline 2023-06-14; living — last content change 2026-09-19 (commit `99c65a8522`, "Add cooldowns to an existing point") |
| **Identifier** | `docs/Concise-Guide-for-Developing-More-Secure-Software.md` in ossf/wg-best-practices-os-developers |
| **Source** | https://best.openssf.org/Concise-Guide-for-Developing-More-Secure-Software |
| **Digest** | `adb2925c4bbe4f384c262f91107265e8fc396f1f3a636b31b7ea703ad8e7572c` (raw markdown, `main`, retrieved 2026-10-02) |

**Version verified 2026-10-02:** the guide is unversioned and still carries its 2023-06-14 byline.
The repo's commit history for the file
(https://api.github.com/repos/ossf/wg-best-practices-os-developers/commits?path=docs/Concise-Guide-for-Developing-More-Secure-Software.md)
shows edits in 2025-03, 2025-04 and 2026-09-19. The published page at best.openssf.org carries the
same byline. So the record tracks the raw markdown at `main` as of the retrieval date, and the
digest pins that state.

## Overview

The guide is a one-page list of 29 numbered imperatives "for all software developers for secure
software development, building, and distribution". It covers:

- account security: MFA for privileged developers;
- learning secure development;
- tooling in CI;
- dependency hygiene: evaluate before adopting, use package managers, monitor vulnerabilities in
  direct and indirect dependencies, update after a ~3-day cooldown;
- no secrets in repositories, and review before accepting changes;
- vulnerability reporting, advisories and CVEs;
- signed releases, SBOMs and SLSA levels;
- third-party audits, succession, memory-safe languages;
- source packages that contain only VCS content (the xz lesson), and loading web assets only from
  your own domains.

Several items delegate to heavier frameworks: the OpenSSF Best Practices badge, Scorecard, SLSA,
the CNCF Supply Chain Best Practices, ASVS and SAFECode. That makes the guide a small **index of
the SDL ecosystem** as OpenSSF sees it.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | a compact consensus checklist of developer-side SDL practices |
| Cryptography | adjacent | signing (cosign) and MFA tokens only |
| This project | adjacent | supplies crosswalk rows and delegation edges (R-044) and examples of all three mitigation kinds (R-040); no SDL structure |

Bears on **R-044** (crosswalk; delegations to other requirement sets) and **R-040** (mitigation
kind).

## Implementations

None as such: it is guidance. The tools it names as examples are dependabot / GitLab dependency
scanning, Sigstore cosign, OpenSSF Scorecard, Allstar, the OpenSSF Best Practices badge and LFX
Security. Searched 2026-10-02.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/README.md` | index |
| `distilled/requirements.yaml` | all 29 items verbatim, `#CG-01..CG-29` |
| `distilled/object-model.yaml` | object-model pass (30 objects, 22 edges) |
| `distilled/object-model.md` | Mermaid diagram + findings |

## Limits

- **Not normative.** The guide has no levels, no conformance criteria and no verification method.
  "All tools or services listed are merely examples."
- **Living text, stale byline.** The 2023-06-14 date undersells the content, which now includes the
  2026 cooldown advice. A citation must use the digest and the retrieval date.
- **Out of date in one place.** Item 20 still links the CNCF **v1** paper (CNCF_SSCP_v1.pdf), not
  v2 (2025). See `cncf-supply-chain-best-practices-v2`.
- **No phases or ordering.** Any SDL phase in requirements.yaml is our own assignment.

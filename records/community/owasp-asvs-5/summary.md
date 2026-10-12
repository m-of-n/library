---
schema: "library-summary/v1"
id: owasp-asvs-5
record: owasp-asvs-5
type: summary
updated: "2026-10-02"
---

# OWASP Application Security Verification Standard 5.0.0

|  |  |
|---|---|
| **Type** | spec (community standard) |
| **Maturity** | best-practice (OWASP Flagship Project per the project page; a community standard, not a de jure one; OWASP certifies no one) |
| **Authors** | Elar Lang, Josh C Grossman, Jim Manico, Daniel Cuthbert (project leads), with the ASVS working group |
| **Published** | May 2025 (GitHub release `v5.0.0_release`, 2025-05-30) |
| **Identifier** | ASVS 5.0.0; cite requirements as `v5.0.0-<chapter>.<section>.<requirement>` |
| **Source** | https://github.com/OWASP/ASVS/releases/tag/v5.0.0_release (JSON export: `OWASP_Application_Security_Verification_Standard_5.0.0_en.json`) |
| **Digest** | `bcdbec214d70abcfad9284a31d4f9e5134305831d628aad3aa85d7e26626cb35` (JSON export). PDF: `f3e9a2f1098bc4af594578acb404121af69e3964aa4d90abd4b00607218d30c6` (123 pp.). CSV: `6124dba1…6cd5` |
| **License** | CC BY-SA 4.0 |

**Version check (2026-10-02).** 5.0.0 is the current stable release:

- The OWASP project page (https://owasp.org/www-project-application-security-verification-standard/)
  reads "Get the latest stable version of the ASVS (5.0.0)".
- The GitHub releases API lists only `v5.0.0_release` (2025-05-30) and older 4.x tags, plus a
  continuously rebuilt "Bleeding Edge" release (`latest`, generated 2026-09-03). Its notes say it is "for
  testing and preview purposes only" and that "The latest stable release is v5.0.0".
- No 5.0.1 or 5.1 tag exists.

## Overview

ASVS lists security requirements that a web application or service must meet, written so that each one can
be verified to a pass or fail decision. Version 5.0 is a full rewrite with 345 requirements (L1 70, L2 183,
L3 92) in 17 chapters, from encoding and sanitization through OAuth/OIDC, cryptography, secure coding and
architecture, logging and WebRTC. The levels are cumulative and priority-based. L1 is the first layer of
defense (about 20% of requirements). L2 is what "most applications should be striving" for (all L1+L2, 253
requirements). L3 adds defense-in-depth.

The new idea in 5.0 is *documented security decisions*. A requirement in a chapter's first section demands
that the organization document its decision for a context-dependent control. A paired implementation
requirement then demands that the decision be applied. The two are verified separately. 5.0 also cut
scope:

- The V1 Architecture chapter is gone, its content redistributed or removed.
- The direct CWE and NIST SP 800-63 mappings are gone.
- The SDL process items (secure SDLC, threat modeling, security user stories, secure-coding checklist) are
  now non-mandatory "Software Security processes" in Appendix D, pointing to SAMM.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The most widely used open catalogue of verifiable application-security requirements. It is the content of a verification gate. |
| Cryptography | adjacent | Chapter V11 plus Appendix C approval tables (A/L/D) for ciphers, modes, hashes, KDFs, KEX groups, MACs, signatures and PQC. |
| This project | core | R-042 (conformance: per-requirement pass/fail/N/A + evidence + report), R-040 (documentation vs technical mitigation, stated by the standard), R-041 (level as a gate exit criterion), R-043 (the verification report as a governed view), R-044 (versioned ids and a published v4↔v5 mapping), DEC-009. |

## Implementations

Searched 2026-10-02 (web; GitHub topic `owasp-asvs`; OWASP project pages). Tools that consume the ASVS
requirement exports. Version support for 5.0.0 was not verified tool by tool unless stated.

| Name | Kind | License | URL |
|---|---|---|---|
| OWASP ASVS exports (CSV, JSON, flat JSON, XML, legacy, CycloneDX 1.6) | data | CC BY-SA 4.0 | https://github.com/OWASP/ASVS/releases/tag/v5.0.0_release |
| OWASP Cheat Sheet Series ASVS index | guidance mapping | CC BY-SA 4.0 | https://cheatsheetseries.owasp.org/IndexASVS.html |
| OWASP Common Requirement Enumeration (OpenCRE) | cross-standard mapping (planned ASVS 5 target) | CC0 / open | https://www.opencre.org/ |
| SecurityRAT | requirements-management tool (ASVS import; last push 2025-08-28, 5.0.0 support not verified) | see repo (GitHub reports NOASSERTION) | https://github.com/SecurityRAT/SecurityRAT |
| OWASP Cornucopia (Website App Edition) | card game mapped to ASVS | CC BY-SA | https://owasp.org/www-project-cornucopia/ |
| TarkinLarson/asvs-auditor | agent skill auditing against ASVS 5.0 | MIT | https://github.com/TarkinLarson/asvs-auditor |
| pipeworx-io/mcp-owasp | MCP server exposing ASVS 5.0 requirements | MIT | https://github.com/pipeworx-io/mcp-owasp |

No open-source tool was found that links ASVS 5.0 verification results to a threat model. Commercial
requirement-library products (e.g. SD Elements, IriusRisk) advertise ASVS content. Their 5.0.0 support was
not verified (searched 2026-10-02).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, cites, relations, distillation block |
| `distilled/README.md` | index of the FX-1 artifacts with coverage |
| `distilled/requirements.yaml` | 345 requirements + 27 framing + 25 Appendix C + 48 chapter-prose + 16 Appendix D entries (library-requirements/v2) |
| `distilled/normative.md` | verbatim normative content in source structure |
| `distilled/crypto-registry.yaml` | Appendix C approval tables (14 tables, 120 rows) |
| `distilled/schema/` | derived JSON Schemas for the exports (validated) + README |
| `distilled/messages.yaml` | identifier, export structures, verification report |
| `distilled/protocol.yaml`, `protocol.md` | verification engagement and procurement flows |
| `distilled/state-machine.yaml` | level attainment and requirement outcome |
| `distilled/examples/` | identifier vectors and an every-format export fixture |
| `distilled/design-notes.md` | mapping to R-040..R-044, DEC-009 |
| `distilled/object-model.yaml`, `object-model.md` | object-model pass |

## Limits

- **Web applications and services only.** Mobile (MASVS), IoT, CI/CD, hosting and operations are
  explicitly out of scope. ASVS "does not prescribe development lifecycle activities", so it cannot stand
  in for SSDF, SAMM or an SDL. It defines what a verified product must exhibit, not how it was built.
- **No method per requirement.** The verification method is the verifier's choice, and there is no test
  procedure. OWASP WSTG is the intended companion.
- **No threat linkage.** The CWE/NIST mappings were dropped, and the planned OWASP CRE mapping is not yet
  published. The CWE links in our requirements.yaml are reconstructed from a pre-release export and marked
  inferred.
- **Levels are not risk tiers by mandate.** The organization picks its level. The allocation "may not be a
  100% fit for every situation".
- **Source defects recorded.** The CycloneDX export has empty level lists. The typos "execptions" and
  "onyly" are kept verbatim. The referencing example `1.11.3` does not resolve in 5.0.0.
- **No certification.** OWASP endorses no ASVS certification or trust mark.

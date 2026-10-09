---
schema: "library-summary/v1"
id: lockheed-kill-chain-2011
record: lockheed-kill-chain-2011
type: summary
updated: "2026-09-29"
---

# Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains

|  |  |
|---|---|
| **Type** | paper (Lockheed Martin white paper, 14 pp.) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Eric M. Hutchins, Michael J. Cloppert, Rohan M. Amin |
| **Published** | 2011 — *Leading Issues in Information Warfare & Security Research*, Vol. 1, pp. 1–14; Lockheed Martin white paper |
| **Identifier** | https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf |
| **Source** | same (PDF) |
| **Digest** | `fe94be07a81a07eab1deabe5238fb45d65fb558c6585f782bbcf188a6bc32a98` (retrieved 2026-09-29) |

## Overview

The paper that introduced the **intrusion kill chain**. It argues that
conventional defence (anti-virus, intrusion detection, incident response after
the fact) addresses only the vulnerability side of risk and fails against
well-resourced, persistent adversaries (APTs); defenders should instead study the
*adversary*. An intrusion is modelled as seven ordered phases —
reconnaissance, weaponization, delivery, exploitation, installation, command and
control, actions on objectives — and because the adversary must succeed at every
phase, **one mitigation anywhere breaks the chain**. Defenders map the indicators
seen at each phase to a **courses-of-action matrix** (detect, deny, disrupt,
degrade, deceive, destroy — taken from US DoD information-operations doctrine),
and link repeated indicators across intrusions into **campaigns**, creating an
intelligence feedback loop that makes each later intrusion harder. A worked case
study analyses a real APT campaign phase by phase.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Foundational model of intrusion phases and threat-intelligence-driven defence. |
| Cryptography | none | Not about cryptography. |
| This project | core | An *ordered* phase model of an attack — directly relevant to tmodel's ordered `AttackPath` (ARCH-0001 §3) and to RPT-0002 §9. |

Bears on **DEC-001** (object model — ordered attack steps) and **DEC-005** (MVP scope).

## Implementations

The paper is a method, not software. Kill-chain phases are used as a
classification in threat-intelligence practice and appear alongside ATT&CK
tactics (see `mitre-attack`). No dedicated open-source implementation
identified; searched 2026-09-29.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Intrusion-centric.** Written for malware-delivered network intrusions by
  external APTs; phases such as *weaponization* and *installation* fit insider
  threats, cloud-account abuse, or attacks with no malware poorly.
- **Linear and coarse.** Seven phases in a fixed order; real intrusions loop
  (e.g. repeated reconnaissance after gaining access) and the phases say nothing
  about the concrete actions inside each one — the gap MITRE ATT&CK fills
  (`mitre-attack-design-philosophy`, §4.1.3).
- **A defender's model, not a design-time method.** It analyses intrusions that
  happen, rather than finding threats in a system being designed.
- **Publication details.** The Lockheed PDF carries no venue or date on its face;
  the published version is *Leading Issues in Information Warfare & Security
  Research*, Vol. 1 (2011), pp. 1–14 (per BibSonomy / Semantic Scholar entries).

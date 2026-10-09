---
schema: "library-normative/v1"
id: etsi-en-304-223-normative
record: etsi-en-304-223
type: normative
updated: "2026-10-01"
coverage: "Scope, stakeholder roles (Table 4-1), the 13 principles by lifecycle phase, AI-specific threats named, relation to ISO/IEC 22989 and tmodel. Provisions themselves: requirements.yaml."
reviewed_by: ""
---

# ETSI EN 304 223 — distilled normative content

> Compacted so an implementer can work from it without re-reading the source. Provision ids
> resolve in `requirements.yaml`. **Baseline:** 72 provisions in clause 5 — 59 *shall*,
> 28 *should*, 5 *can* — all catalogued.

## 1. What it is

A European Standard (adopted 2025-12-08) of baseline security requirements for AI models and
systems, including systems built on deep neural networks such as generative AI (§1). It has
**no normative references** (§2.1): everything needed to conform is in the document. Systems
built only for research and never deployed are out of scope (§1). Conformance assessment is
left to ETSI TS 104 216 (Introduction), still a draft work item.

## 2. Stakeholders (Table 4-1)

Each principle names who is primarily responsible; one organisation can hold several roles.

| role | who (paraphrased) |
|---|---|
| **Developer** | creates or adapts an AI model or system, proprietary or open source; may be an "AI provider" under the EU AI Act |
| **System Operator** | embeds or deploys an AI system in its infrastructure and maintains it; may be a "deployer" under the EU AI Act |
| **Data Custodian** | controls permissions and integrity of data an AI system uses, and sets data policy |
| **End-user** | anyone using the AI system, inside an organisation or as a consumer |
| **Affected entity** | people and technologies affected by an AI system without using it |

Provisions also oblige **Organizations** generally (staff training and awareness, §5.1.1).

## 3. The 13 principles

| # | clause | principle | phase | primarily applies to | provisions | shall / should |
|---|---|---|---|---|---|---|
| 1 | §5.1.1 | Raise awareness of AI security threats and risks | design | System Operators, Developers, and Data Custodians | 5 | 4 / 1 |
| 2 | §5.1.2 | Design the AI system for security as well as functionality and performance | design | System Operators and Developers | 9 | 8 / 1 |
| 3 | §5.1.3 | Evaluate the threats and manage the risks to the AI system | design | Developers and System Operators | 7 | 5 / 2 |
| 4 | §5.1.4 | Enable human responsibility for AI systems | design | Developers and System Operators | 5 | 1 / 4 |
| 5 | §5.2.1 | Identify, track and protect the assets | development | Developers, System Operators and Data Custodians | 7 | 6 / 1 |
| 6 | §5.2.2 | Secure the infrastructure | development | Developers and System Operators | 6 | 5 / 1 |
| 7 | §5.2.3 | Secure the supply chain | development | Developers, System Operators and Data Custodians | 6 | 6 / 0 |
| 8 | §5.2.4 | Document data, models and prompts | development | Developers | 6 | 3 / 3 |
| 9 | §5.2.5 | Conduct appropriate testing and evaluation | development | Developers and System Operators | 6 | 2 / 4 |
| 10 | §5.3.1 | Communication and processes associated with End-users and Affected Entities | deployment | not stated | 5 | 4 / 1 |
| 11 | §5.4.1 | Maintain regular security updates, patches and mitigations | maintenance | Developers and System Operators | 4 | 2 / 2 |
| 12 | §5.4.2 | Monitor the system's behaviour | maintenance | Developers and System Operators | 4 | 1 / 3 |
| 13 | §5.5.1 | Ensure proper data and model disposal | end-of-life | Developers and System Operators | 2 | 2 / 0 |

Phases map to ISO/IEC 22989 lifecycle stages: design and development → *Design and
development*; deployment → *Deployment*; maintenance → *Operations and monitoring*; end of
life → *Retirement* (Introduction, NOTE).

## 4. AI-specific threats the standard names

| threat | where |
|---|---|
| data poisoning | Introduction; definition (§3.1); 5.1.3-1; 5.2.2-2; 5.2.4-2, 5.2.4-2.1; 5.4.2-2 |
| model obfuscation | Introduction |
| indirect prompt injection | Introduction |
| model inversion | definition (§3.1); 5.1.3-1 |
| membership inference | 5.1.3-1 |
| adversarial attacks, unexpected inputs | definition (§3.1); 5.1.2-2 |
| reverse engineering of the model or training data via outputs | 5.2.5-4 |
| unintended influence over the system via outputs | 5.2.5-4.1 |
| risk from superfluous functionality (e.g. unused modalities) | 5.1.3-1.2 |

## 5. Bearing on tmodel

- **Threat model content (DEC-001).** 5.1.3-1 requires threat modelling that addresses
  AI-specific attacks; §4 above is a starting list of AI threat types the object model must
  express.
- **Human oversight (R-018).** Principle 4 (5.1.4-1 … 5.1.4-5) asks for human oversight
  capabilities and assessable outputs — the same commitment as ARCH-0001 §7.
- **Audit trail.** 5.1.2-3, 5.2.4-1 and 5.2.4-3 ask for audit trails of models, datasets,
  prompts and prompt changes — relevant to any AI feature in tmodel.
- **Automated compliance (#19).** 22 provisions name a checkable artefact
  (`expects_deliverables`), the natural first targets for automated checks.

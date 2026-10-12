---
schema: "library-doc/v1"
id: etsi-en-304-223-requirements-table
record: etsi-en-304-223
type: index
audience: human   # generated from requirements.yaml — do not hand-edit
generated_from: distilled/requirements.yaml
updated: "2026-10-01"
---

# ETSI EN 304 223 V2.1.1 — provisions (human-viewable list)

> **Generated** from `requirements.yaml` (the machine/AI source of truth). Do not hand-edit.
> **72 provisions**: 49 requirements (*shall*) + 23 recommendations (*should*). `P`=process, `D`=deliverable-producing.
> Full verbatim text, verbs and deliverables are in the YAML. Actor, title, nature and deliverables are derived and not yet reviewed.

## Principle 1 — Raise awareness of AI security threats and risks (§5.1.1, secure-design)

Primarily applies to: System Operators, Developers, and Data Custodians

| designator | norm | nature | actor | short title | deliverables |
|---|---|---|---|---|---|
| `5.1.1-1` | req | D | Organization | Include AI security content in cyber security training | AI security content in the cyber security training programme |
| `5.1.1-1.1` | req | P | Organization (implied) | Tailor AI security training to staff roles | — |
| `5.1.1-2` | req | P | Organization | Keep all staff aware of AI-related threats and mitigations | — |
| `5.1.1-2.1` | rec | P | Organization (implied) | Share AI threat updates through multiple channels | — |
| `5.1.1-2.2` | req | P | Organization | Train developers in secure AI coding and design | — |

## Principle 2 — Design the AI system for security as well as functionality and performance (§5.1.2, secure-design)

Primarily applies to: System Operators and Developers

| designator | norm | nature | actor | short title | deliverables |
|---|---|---|---|---|---|
| `5.1.2-1` | req | D | System Operator, Developer | Assess business need, AI security risks and mitigations before building | documented business requirements, AI security risks and mitigation strategies |
| `5.1.2-1.1` | req | P | Data Custodian | Include the Data Custodian in requirements discussions | — |
| `5.1.2-2` | req | P | Developer, System Operator | Design AI systems to withstand adversarial attacks and failures | — |
| `5.1.2-3` | req | D | Developer | Keep an audit trail of models, datasets and prompts | audit trail covering operation and lifecycle of models, datasets and prompts |
| `5.1.2-4` | req | D | Developer, System Operator | Risk-assess external components for AI-specific risks | AI security risk assessment and due diligence for external components |
| `5.1.2-5` | req | P | Data Custodian | Match intended use to the sensitivity of training data | — |
| `5.1.2-5.1` | rec | P | Organization | Encourage staff to report AI security risks | — |
| `5.1.2-6` | req | P | Developer, System Operator | Give the AI system only the permissions it needs on other systems | — |
| `5.1.2-7` | req | D | Developer, System Operator | Do due diligence on external providers | due diligence assessment of the external provider |

## Principle 3 — Evaluate the threats and manage the risks to the AI system (§5.1.3, secure-design)

Primarily applies to: Developers and System Operators

| designator | norm | nature | actor | short title | deliverables |
|---|---|---|---|---|---|
| `5.1.3-1` | req | D | Developer, System Operator | Threat-model and manage risks, including AI-specific attacks | threat model and security risk management record |
| `5.1.3-1.1` | req | P | System Operator (implied), Developer (implied) | Re-run threat modelling when settings or configuration change | — |
| `5.1.3-1.2` | req | P | Developer | Manage risks of superfluous model functionality | — |
| `5.1.3-1.3` | req | P | System Operator | Apply controls in line with corporate risk tolerance | — |
| `5.1.3-2` | req | P | Developer, System Operator | Pass unresolved AI threats on to System Operators and End-users | — |
| `5.1.3-3` | rec | P | System Operator | Get assurance from external parties responsible for AI risks | — |
| `5.1.3-4` | rec | P | Developer, System Operator | Continuously monitor and review infrastructure against risk appetite | — |

## Principle 4 — Enable human responsibility for AI systems (§5.1.4, secure-design)

Primarily applies to: Developers and System Operators

| designator | norm | nature | actor | short title | deliverables |
|---|---|---|---|---|---|
| `5.1.4-1` | rec | P | Developer, System Operator | Build in capabilities for human oversight | — |
| `5.1.4-2` | rec | P | Developer | Make outputs easy for humans to assess | — |
| `5.1.4-3` | req | P | Developer, System Operator | Build technical measures where human oversight is a risk control | — |
| `5.1.4-4` | rec | P | Developer | Verify Data Custodian security controls are built in | — |
| `5.1.4-5` | rec | P | Developer, System Operator | Tell End-users about prohibited use cases | — |

## Principle 5 — Identify, track and protect the assets (§5.2.1, secure-development)

Primarily applies to: Developers, System Operators and Data Custodians

| designator | norm | nature | actor | short title | deliverables |
|---|---|---|---|---|---|
| `5.2.1-1` | req | D | Developer, Data Custodian, System Operator | Maintain an inventory of assets and their interdependencies | inventory of assets and their interdependencies |
| `5.2.1-2` | req | P | Developer, Data Custodian, System Operator | Track, authenticate, version-control and secure AI assets | — |
| `5.2.1-3` | req | D | System Operator | Tailor disaster recovery plans to attacks on AI systems | disaster recovery plan covering attacks on AI systems |
| `5.2.1-3.1` | rec | P | System Operator | Be able to restore a known good state | — |
| `5.2.1-4` | req | P | Developer, System Operator, Data Custodian, End-user | Protect sensitive data such as training and test data | — |
| `5.2.1-4.1` | req | P | Developer, Data Custodian, System Operator | Check and sanitise data and inputs, and repeat on model revisions | — |
| `5.2.1-4.2` | req | P | Developer | Protect confidential training data and model weights | — |

## Principle 6 — Secure the infrastructure (§5.2.2, secure-development)

Primarily applies to: Developers and System Operators

| designator | norm | nature | actor | short title | deliverables |
|---|---|---|---|---|---|
| `5.2.2-1` | req | P | Developer, System Operator | Secure access to APIs, models, data and pipelines | — |
| `5.2.2-2` | req | P | Developer | Protect externally offered APIs, e.g. with rate limits | — |
| `5.2.2-3` | req | P | Developer | Use separate, least-privilege development and tuning environments | — |
| `5.2.2-4` | req | D | Developer, System Operator | Publish a vulnerability disclosure policy | published vulnerability disclosure policy |
| `5.2.2-5` | req | D | Developer, System Operator | Maintain an AI incident management plan and recovery plan | AI system incident management plan; AI system recovery plan |
| `5.2.2-6` | rec | P | Developer, System Operator | Make cloud contracts support these requirements | — |

## Principle 7 — Secure the supply chain (§5.2.3, secure-development)

Primarily applies to: Developers, System Operators and Data Custodians

| designator | norm | nature | actor | short title | deliverables |
|---|---|---|---|---|---|
| `5.2.3-1` | req | P | Developer, System Operator | Follow secure software supply chain processes | — |
| `5.2.3-2` | req | D | System Operator | Justify using poorly documented or unsecured models or components | documented justification for using poorly documented or unsecured models or components |
| `5.2.3-2.1` | req | D | Developer, System Operator | Mitigate and risk-assess such models or components | risk assessment for those models or components |
| `5.2.3-2.2` | req | P | System Operator | Share that justification with End-users | — |
| `5.2.3-3` | req | P | Developer, System Operator | Re-run evaluations on released models before using them | — |
| `5.2.3-4` | req | P | System Operator | Tell End-users before models are updated | — |

## Principle 8 — Document data, models and prompts (§5.2.4, secure-development)

Primarily applies to: Developers

| designator | norm | nature | actor | short title | deliverables |
|---|---|---|---|---|---|
| `5.2.4-1` | req | D | Developer | Document an audit trail of design and maintenance plans | audit trail of system design and post-deployment maintenance plans |
| `5.2.4-1.1` | rec | P | Developer | Include security-relevant information in the documentation | — |
| `5.2.4-1.2` | req | D | Developer | Release cryptographic hashes of shared model components | published cryptographic hashes of model components |
| `5.2.4-2` | req | D | Developer | Document the source and use of public training data | documentation of how public training data was obtained, its source and use |
| `5.2.4-2.1` | rec | P | Developer (implied) | Record the source URL and date of training data | — |
| `5.2.4-3` | rec | D | Developer | Keep an audit log of system prompt and configuration changes | audit log of changes to system prompts and model configuration |

## Principle 9 — Conduct appropriate testing and evaluation (§5.2.5, secure-development)

Primarily applies to: Developers and System Operators

| designator | norm | nature | actor | short title | deliverables |
|---|---|---|---|---|---|
| `5.2.5-1` | req | D | Developer | Security-test all released models, applications and systems | security assessment results for released models, applications and systems |
| `5.2.5-2` | req | P | System Operator | Test before deployment, with Developer support | — |
| `5.2.5-2.1` | rec | P | System Operator, Developer | Use independent security testers | — |
| `5.2.5-3` | rec | P | Developer | Share test findings with System Operators | — |
| `5.2.5-4` | rec | P | Developer | Check outputs do not allow reverse engineering of the model or data | — |
| `5.2.5-4.1` | rec | P | Developer | Check outputs do not give unintended influence over the system | — |

## Principle 10 — Communication and processes associated with End-users and Affected Entities (§5.3.1, secure-deployment)

Primarily applies to: _not stated_

| designator | norm | nature | actor | short title | deliverables |
|---|---|---|---|---|---|
| `5.3.1-1` | req | P | System Operator, Developer | Tell End-users how their data is used, accessed and stored | — |
| `5.3.1-2` | req | D | System Operator, Developer | Give End-users guidance on use and configuration | End-user guidance on use, management, integration and configuration |
| `5.3.1-2.1` | req | D | System Operator | Cover appropriate use, limitations and failure modes in guidance | guidance on appropriate use, limitations and failure modes |
| `5.3.1-2.2` | req | P | System Operator | Proactively inform End-users of security-relevant updates | — |
| `5.3.1-3` | rec | D | Developer, System Operator | Support End-users and Affected Entities during incidents | documented incident-support process agreed in contracts with End-users |

## Principle 11 — Maintain regular security updates, patches and mitigations (§5.4.1, secure-maintenance)

Primarily applies to: Developers and System Operators

| designator | norm | nature | actor | short title | deliverables |
|---|---|---|---|---|---|
| `5.4.1-1` | req | P | Developer, System Operator | Provide security updates and deliver them to End-users | — |
| `5.4.1-1.1` | req | D | Developer | Have contingency plans where updates cannot be provided | contingency plans for AI systems that cannot be updated |
| `5.4.1-2` | rec | P | Developer | Treat major updates as a new model and re-test | — |
| `5.4.1-3` | rec | P | Developer | Help System Operators evaluate model changes | — |

## Principle 12 — Monitor the system's behaviour (§5.4.2, secure-maintenance)

Primarily applies to: Developers and System Operators

| designator | norm | nature | actor | short title | deliverables |
|---|---|---|---|---|---|
| `5.4.2-1` | req | D | System Operator | Log system and user actions | logs of system and user actions |
| `5.4.2-2` | rec | P | System Operator | Analyse logs for anomalies, drift and poisoning | — |
| `5.4.2-3` | rec | P | System Operator, Developer | Monitor internal states of the AI system | — |
| `5.4.2-4` | rec | P | System Operator, Developer | Monitor model performance over time | — |

## Principle 13 — Ensure proper data and model disposal (§5.5.1, secure-end-of-life)

Primarily applies to: Developers and System Operators

| designator | norm | nature | actor | short title | deliverables |
|---|---|---|---|---|---|
| `5.5.1-1` | req | P | Developer, System Operator | Involve Data Custodians and dispose securely when transferring ownership | — |
| `5.5.1-2` | req | P | Developer, System Operator | Involve Data Custodians and delete data when decommissioning | — |

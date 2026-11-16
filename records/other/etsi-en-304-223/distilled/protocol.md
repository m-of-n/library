---
record: etsi-en-304-223
kind: protocol
title: "etsi-en-304-223 — protocol model"
extracted: "2026-11-15"
reviewed_by: ""
---

# ETSI EN 304 223: process flows

The machine-readable model is `protocol.yaml` (roles, work products, flows F01 to F16 with their
error paths, provisions not in any flow, open issues OI-01 to OI-19). The lifecycles are
`state-machine.yaml` (SM01 to SM10). This file is the prose and one sequence diagram per flow.
Every quotation below is a marker rendered from `.cache/etsi-en-304-223.txt` by
`bin/check-quotes --render`; nothing in a blockquote was typed. Requirement ids live in
`protocol.yaml`, where a script emitted them from provision keys.

## What kind of protocol this is

None on the wire. The EN has no transport, encoding or message syntax, and sets no timer, deadline
or retry (retention time and review frequency are only items a Developer documents). It sorts its provisions into five lifecycle phases and gives each principle to stakeholder
roles:

<!-- q L195-196 "The present document separates" .. "secure end of life." -->
> The present document separates principles and requirements into five phases. These are secure design, secure development, secure deployment, secure maintenance and secure end of life.

What passes between the roles is documents, notices, plans, updates and decisions, which
`protocol.yaml` calls work products. A flow below is the order in which the provisions make
those happen. Where the source fixes an order (prior to, post-, during, following, this
information, these updates, a perfect tense) the step is marked stated; everything else is
inferred, and every failure the source does not answer is marked unspecified.

## Roles

| role | who | source |
|---|---|---|
| developer | creates or adapts AI models or systems | Table 4-1 |
| system_operator | embeds, deploys or maintains them, including contracted services | Table 4-1 |
| data_custodian | controls data permissions, integrity and data-use policy | Table 4-1 |
| end_user | employees and consumers using the system | Table 4-1 |
| affected_entity | affected by the system without necessarily using it (OI-01) | Table 4-1 |
| organization | the employer of any stakeholder; trains and encourages reporting | §5.1.1, §5.1.2-5.1 |
| staff | employees, staff members, developers in lower case | §5.1.1, §5.1.2-5.1 |
| external_provider | a provider subject to due diligence | §5.1.2-7 |
| external_risk_owner | an outside party responsible for identified AI security risks | §5.1.3-3 |
| cloud_service_operator | cloud services under contract | §5.2.2-6 |
| api_consumer | external customers or collaborators calling an API | §5.2.2-2 |
| attacker | the adversary of the API example | §5.2.2-2 |
| independent_security_tester | testers independent of Developer and System Operator | §5.2.5-2.1 |
| receiving_entity | the other entity in a transfer or sharing of ownership | §5.5.1-1 |
| reporter | whoever reports a vulnerability or a poisoning attack (inferred) | §5.2.2-4, §5.2.4-2.1 |

Roles are not organizations:

<!-- q L434-436 "A single entity can hold" .. "regulatory regimes." -->
> A single entity can hold multiple stakeholder roles, as defined in the present document, in addition to any responsibilities arising from different regulatory regimes.

## Reading the diagrams

- A solid arrow hands a work product (named as in `protocol.yaml` work_products) to another role.
- Each work product carries a `structure` key in `protocol.yaml` naming the `messages.yaml` structure that holds it, or `none` with a reason.
- A dashed arrow is a response the EN does not define.
- A note over a role is an act of that role alone.
- `opt` is a step that applies only under its provision's condition (Where..., If...).
- `alt` is a branch; every error and exception outcome is listed under error_paths in `protocol.yaml`.
- `loop` is a stated re-entry; `par` joins steps the source gives without an order.
- Numbers are the step numbers of `protocol.yaml`; parenthesised keys are provisions. Inferred,
  purpose and presupposed carry the meanings of the `protocol.yaml` conventions.

## F01. Deciding whether to create an AI system (§5.1.2)

The assessment is part of the decision, so it comes first. The Data Custodian joins the
requirements work when it sits in the Developer's organization. The EN gives no criterion for
deciding not to create (F01-E2).

<!-- q L545-547 "As part of deciding" .. "mitigation strategies." -->
> As part of deciding whether to create an AI system, a System Operator and/or Developer shall conduct a thorough assessment that includes determining and documenting the business requirements and/or problem they are seeking to address, along with associated AI security risks and mitigation strategies.

```mermaid
sequenceDiagram
  participant SO as System Operator
  participant D as Developer
  participant DC as Data Custodian
  Note over SO,D: 1. CreationAssessment - requirements or problem, risks, mitigations (5.1.2-1)
  opt Data Custodian inside the Developer's organization
    D->>DC: 2. RequirementsAndDataNeeds discussions (5.1.2-1.1)
  end
  Note over DC: 3. UsageAppropriatenessCheck against data sensitivity (5.1.2-5), order inferred
  opt the system will interact with other systems or data sources
    Note over SO,D: 4. PermissionGrant - functional need only, risk-assessed (5.1.2-6)
  end
  alt create
    Note over SO,D: 5. CreationDecision (5.1.2-1), then secure development
  else do not create (inferred, F01-E2)
    Note over SO,D: no system, criterion unstated
  end
```

## F02. Threat modelling and risk treatment (§5.1.3, §5.1.4-1, §5.1.4-3)

Developers and System Operators analyse threats; System Operators apply controls to what the
analysis found. The process re-runs on review, on any new or changed setting at any stage, and as
continuous review finds change.

<!-- q L594-595 "The threat modelling and risk management process" .. "of the AI lifecycle." -->
> The threat modelling and risk management process shall be conducted to address any security risks that arise when a new setting or configuration option is implemented or updated at any stage of the AI lifecycle.

```mermaid
sequenceDiagram
  participant D as Developer
  participant SO as System Operator
  participant X as External risk owner
  Note over D,SO: 1. ThreatModel - analyse threats, manage risks (5.1.3-1)
  Note over D: 2. risks of superfluous functionality (5.1.3-1.2)
  Note over SO: 3. RiskTreatment - controls against cost and risk tolerance (5.1.3-1.3)
  Note over D,SO: 4. OversightMeasures (5.1.4-1, 5.1.4-3)
  opt an external entity owns identified risks
    SO->>X: 5. attain RiskAssurance (5.1.3-3), failure unspecified
  end
  opt a threat Developers cannot resolve
    D->>SO: 6. UnresolvedThreatNotice, see F03 (5.1.3-2)
  end
  loop regular review, new or changed setting, continuous infrastructure review
    Note over D,SO: 7. re-run steps 1 to 3 (5.1.3-1, 5.1.3-1.1, 5.1.3-4)
  end
```

## F03. Communicating threats Developers cannot resolve (§5.1.3-2)

A two-hop relay. The first sentence is passive, so neither who identifies the threat nor who
sends it is named (OI-08); Developers is this model's reading.

<!-- q L604-607 "Where AI security threats" .. "monitor these threats." -->
> Where AI security threats are identified that cannot be resolved by Developers, this shall be communicated to System Operators so they can threat model their systems. System Operators shall communicate this information to End-users, so they are made aware of these threats. This communication should include detailed descriptions of the risks, potential impacts, and recommended actions to address or monitor these threats.

```mermaid
sequenceDiagram
  participant D as Developer
  participant SO as System Operator
  participant EU as End-user
  Note over D: 1. a threat Developers cannot resolve (5.1.3-2)
  D->>SO: 2. UnresolvedThreatNotice (5.1.3-2), sender inferred
  Note over SO: 3. threat model own systems, purpose, see F02 (5.1.3-1)
  SO->>EU: 4. ThreatAdvisory - risks, impacts, recommended actions (5.1.3-2)
```

## F04. Data Custodian controls: specified, built in, verified (§5.1.4-4)

Only the verification is asked for; specifying and building the controls are presupposed.

<!-- q L631-632 "Developers should verify" .. "into the system." -->
> Developers should verify that the security controls specified by the Data Custodian have been built into the system.

```mermaid
sequenceDiagram
  participant DC as Data Custodian
  participant D as Developer
  DC->>D: 1. DataSecurityControls (presupposed)
  Note over D: 2. build them in (presupposed)
  Note over D: 3. ControlVerification (5.1.4-4)
  opt a control is missing
    Note over D: outcome unspecified (F04-E1)
  end
```

## F05. External components, models and providers (§5.1.2-4, §5.1.2-7, §5.2.2-6, §5.2.3, §5.2.4-1.2)

Due diligence precedes use. No rejection outcome is ever stated; instead a component that is not
well-documented or secured may be used on three conditions (F05-E1):

<!-- q L716-718 "System Operators that choose" .. "for said component)." -->
> System Operators that choose to use or adapt any models, or components, which are not well-documented or secured shall be able to justify their decision to use such models or components through documentation (for example if there was no other supplier for said component).

<!-- q L720-721 "In this case" .. "such models or components." -->
> In this case, Developers and System Operators shall have mitigating controls and undertake a risk assessment linked to such models or components.

```mermaid
sequenceDiagram
  participant U as Upstream Developer
  participant DS as Developer or System Operator
  participant P as External provider
  participant C as Cloud service operator
  participant EU as End-user
  Note over DS: 1. SupplyChainProcess frames every step (5.2.3-1)
  opt an external component is used
    Note over DS: 2. ComponentDueDiligence (5.1.2-4)
  end
  opt an external provider is engaged
    DS->>P: 3. ProviderDueDiligence, adherence to the EN (5.1.2-7)
  end
  opt cloud service operators help deliver
    DS->>C: 4. ServiceContract supports compliance (5.2.2-6)
  end
  U->>DS: 5. ComponentHashes (5.2.4-1.2)
  Note over DS: 6. HashVerification, purpose only, mismatch unspecified
  Note over DS: 7. EvaluationResult, evaluations re-run (5.2.3-3)
  Note over DS: 8. UseDecision, use or adapt (5.2.3-2)
  alt not well-documented or secured, used anyway (F05-E1)
    Note over DS: justification, mitigating controls, risk assessment (5.2.3-2, 5.2.3-2.1)
    DS->>EU: JustificationDocumentation, accessible (5.2.3-2.2)
  else not used (inferred, F05-E2)
    Note over DS: no source text for a rejection
  end
```

## F06. Security testing, release and pre-deployment testing (§5.2.5)

Release and deployment each follow a test. Neither test has a pass criterion or a stated
consequence of failure (OI-09).

<!-- q L766-767 "Developers shall ensure that all models" .. "security assessment process." -->
> Developers shall ensure that all models, applications and systems that are released to System Operators and/or End-users have been tested as part of a security assessment process.

<!-- q L769-770 "System Operators shall conduct testing" .. "from Developers." -->
> System Operators shall conduct testing prior to the system being deployed with support from Developers.

```mermaid
sequenceDiagram
  participant D as Developer
  participant T as Independent tester
  participant SO as System Operator
  participant EU as End-user
  Note over D: 1. SecurityAssessment of everything to be released (5.2.5-1)
  D->>T: 2. SecurityTestEngagement (5.2.5-2.1)
  Note over D: 3. OutputEvaluation, reverse engineering and influence (5.2.5-4, 5.2.5-4.1)
  alt release to a System Operator
    D->>SO: 4. Release (5.2.5-1)
    D->>SO: 5. TestFindings (5.2.5-3)
    Note over SO: 6. PreDeploymentTest with Developer support (5.2.5-2)
    Note over SO: 7. Deployment
  else release directly to End-users
    D->>EU: 4. Release (5.2.5-1), no End-user test stated
  end
  Note over D,SO: a failed test has no stated outcome (F06-E1, F06-E2)
```

## F07. Information to System Operators and End-users (§5.2.4-1, §5.2.4-3, §5.3.1-1 to §5.3.1-2.1, §5.1.4-5)

Two hand-offs are ordered by the text itself when the Developer is an external entity: its input
precedes the System Operator's notice and guidance. Nothing is timed against deployment.

<!-- q L797-799 "System Operators shall convey" .. "to System Operators." -->
> System Operators shall convey to End-users in an accessible way where and how their data will be used, accessed and stored (for example, if it is used for model retraining, or reviewed by employees or partners). If the Developer is an external entity, they shall provide this information to System Operators.

```mermaid
sequenceDiagram
  participant D as Developer
  participant DC as Data Custodian
  participant SO as System Operator
  participant EU as End-user
  Note over D: 1. SystemDocumentation - design, post-deployment maintenance plans (5.2.4-1, 5.2.4-1.1)
  D->>SO: 2. SystemDocumentation (5.2.4-1)
  D->>DC: 2. SystemDocumentation (5.2.4-1)
  opt the Developer is an external entity
    D->>SO: 3. DataUseInformation (5.3.1-1)
  end
  SO->>EU: 4. DataUseNotice (5.3.1-1)
  opt the Developer is an external entity
    D->>SO: 5. OperatorInformation (5.3.1-2)
  end
  SO->>EU: 6. UserGuidance - use, limitations, failure modes (5.3.1-2, 5.3.1-2.1)
  SO->>EU: 7. ProhibitedUseNotice, Developers and System Operators (5.1.4-5)
  D->>SO: 8. PromptChangeAuditLog, can be made available (5.2.4-3, possibility)
```

## F08. Security updates, patches and model changes (§5.4.1, §5.3.1-2.2, §5.2.3-3, §5.2.3-4, §5.2.1-4.1, §5.2.4-3)

Developers provide and notify, System Operators deliver; a model update is announced first. Where
no update can be provided the contingency applies, and no notice to anyone is stated (OI-17).

<!-- q L823-824 "Developers shall provide security updates" .. "patches to End-users." -->
> Developers shall provide security updates and patches, where possible, and notify System Operators of the security updates. System Operators shall deliver these updates and patches to End-users.

<!-- q L826-827 "Developers shall have mechanisms" .. "cannot be provided for AI systems." -->
> Developers shall have mechanisms and contingency plans to mitigate security risks, particularly in instances where updates cannot be provided for AI systems.

```mermaid
sequenceDiagram
  participant D as Developer
  participant DC as Data Custodian
  participant SO as System Operator
  participant EU as End-user
  alt an update can be provided
    Note over D: 1. SecurityUpdate (5.4.1-1)
    opt a major update
      Note over D: 2. retest as a new version, see F06 (5.4.1-2)
    end
    opt revision driven by user feedback or continuous learning
      Note over D,SO: 3. DataCheck repeated (5.2.1-4.1)
    end
    opt a prompt, setting or configuration option changes
      Note over D: 4. ConfigurationChangeRecord and risk process, see F02 (5.2.4-3, 5.1.3-1.1)
    end
    D->>SO: 5. SecurityUpdateNotice (5.4.1-1)
    D->>SO: 6. PreviewAccess, beta-testing or versioned APIs (5.4.1-3)
    Note over SO: 7. re-run evaluations (inferred, 5.2.3-3)
    opt the update changes a model
      SO->>EU: 8. ModelUpdateNotice, before the update (5.2.3-4)
    end
    SO->>EU: 9. SecurityUpdate delivered (5.4.1-1)
    SO->>EU: 10. SecurityUpdateExplanation (5.3.1-2.2)
  else no update can be provided (F08-E1)
    Note over D: ContingencyMitigation (5.4.1-1.1), no notice stated
  end
```

## F09. Logging, monitoring and detection (§5.4.2)

The EN says what monitoring should find, never what to do when it finds it; step 5 and its three
branches are inferred.

<!-- q L850-852 "System Operators should analyse their logs" .. "poisoning)." -->
> System Operators should analyse their logs to ensure that AI models continue to produce desired outputs and to detect anomalies, security breaches, or unexpected behaviour over time (such as due to data drift or data poisoning).

```mermaid
sequenceDiagram
  participant SO as System Operator
  participant D as Developer
  Note over SO: 1. ActivityLog, system and user actions (5.4.2-1)
  Note over SO: 2. analyse the logs, DetectionFinding (5.4.2-2)
  Note over SO,D: 3. InternalStateTelemetry (5.4.2-3)
  Note over SO,D: 4. PerformanceTrend over time (5.4.2-4)
  alt anomaly, breach or unexpected behaviour (inferred link)
    Note over SO,D: 5. incident response, see F10
  else data drift or poisoning suspected (inferred link)
    Note over SO,D: 5. training-data check, see F11
  else behaviour change affecting security (inferred link)
    Note over SO,D: 5. threat model revision, see F02
  end
```

## F10. Incident preparation, support and recovery (§5.1.2-3, §5.2.1-3, §5.2.2-5, §5.3.1-3, §5.4.2-1)

Preparation is stated; of the response only support during and after the incident is. The
support covers Affected Entities, but the agreed process covers End-users only (OI-02).

<!-- q L811-813 "Developers and System Operators should support" .. "contracts with End-users." -->
> Developers and System Operators should support End-users and Affected Entities during and following a cyber security incident to contain and mitigate the impacts of an incident. The process for undertaking this should be documented and agreed in contracts with End-users.

```mermaid
sequenceDiagram
  participant D as Developer
  participant SO as System Operator
  participant EU as End-user
  participant AE as Affected entity
  Note over D,SO: 1. IncidentManagementPlan and recovery plan (5.2.2-5)
  Note over SO: 2. DisasterRecoveryPlan, known good state restorable (5.2.1-3, 5.2.1-3.1)
  SO->>EU: 3. IncidentSupportAgreement in contracts (5.3.1-3)
  Note over D: 4. AuditTrail (5.1.2-3)
  Note over D,SO: 5. incident recognised (inferred)
  SO->>EU: 6. IncidentSupport, during and following (5.3.1-3)
  SO->>AE: 6. IncidentSupport, during and following (5.3.1-3)
  Note over SO: 7. IncidentInvestigation with the logs (purpose of 5.4.2-1)
  Note over SO: 8. RecoveryAction to a known good state (inferred)
  Note over D,SO: 9. remediation through a SecurityUpdate, see F08 (inferred)
```

## F11. Training-data provenance and a reported poisoning attack (§5.2.4-2, §5.2.4-2.1)

The record is written in advance because poisoning is expected to surface late:

<!-- q L749-750 "As discovery of poisoned data" .. "used in the model." -->
> As discovery of poisoned data is likely to occur after training (if at all), Developers shall document how they obtained the public training data, where it came from and how that data is used in the model.

and it exists so that a report can be checked:

<!-- q L753-754 "This will allow Developers to identify" .. "in their data sets." -->
> This will allow Developers to identify whether a reported data poisoning attack was in their data sets.

```mermaid
sequenceDiagram
  participant R as Reporter, unnamed
  participant D as Developer
  Note over D: 1. TrainingDataProvenance - source, date and time, use (5.2.4-2, 5.2.4-2.1)
  R->>D: 2. DataPoisoningReport (presupposed)
  Note over D: 3. PoisoningAssessment against the record (purpose)
  alt the data sets are affected
    Note over D: 4. ModelRevision, see F06 and F08 (inferred)
  else not affected
    Note over D: no action (inferred, F11-E2)
  end
```

## F12. Vulnerability disclosure and internal risk reporting (§5.2.2-4, §5.1.2-5.1)

A published policy and encouragement to report are all the EN states; the report itself and its
handling are inferred.

<!-- q L692-693 "Developers and System Operators shall implement and publish" .. "disclosure policy." -->
> Developers and System Operators shall implement and publish a clear and accessible vulnerability disclosure policy.

```mermaid
sequenceDiagram
  participant R as Reporter, unnamed
  participant DS as Developer or System Operator
  participant O as Organization
  participant S as Staff
  DS->>R: 1. VulnerabilityDisclosurePolicy, published (5.2.2-4)
  R->>DS: 2. VulnerabilityReport (inferred)
  O->>S: 3. ReportingEncouragement with safeguards (5.1.2-5.1)
  S->>O: 4. RiskReport, encouraged, not required
  Note over DS: 5. triage and remediate, see F02 and F08 (inferred)
```

## F13. AI security awareness and training (§5.1.1)

<!-- q L521-522 "Organizations' cyber security training programme" .. "threats emerge." -->
> Organizations' cyber security training programme shall include AI security content which shall be regularly reviewed and updated, such as if new substantial AI-related security threats emerge.

```mermaid
sequenceDiagram
  participant O as Organization
  participant S as Staff
  Note over O: 1. TrainingProgramme with AI security content, role-tailored (5.1.1-1, 5.1.1-1.1)
  loop regularly, and when substantial new AI-related threats emerge
    Note over O: 2. review and update the content (5.1.1-1)
  end
  O->>S: 3. ThreatAwarenessUpdate, latest threats and mitigations (5.1.1-2)
  O->>S: 4. ThreatAwarenessUpdate over several channels (5.1.1-2.1)
  O->>S: 5. SecureCodingTraining for developers (5.1.1-2.2)
```

## F14. Transferring or sharing ownership of training data or a model (§5.5.1-1)

Three acts joined by and, with no order; disposal sits oddly with sharing (OI-03).

<!-- q L865-867 "If a Developer or System Operator decides to transfer" .. "to another." -->
> If a Developer or System Operator decides to transfer or share ownership of training data and/or a model to another entity they shall involve Data Custodians and securely dispose of these assets. This will protect AI against security issues that can transfer from one AI system instantiation to another.

```mermaid
sequenceDiagram
  participant DS as Developer or System Operator
  participant DC as Data Custodian
  participant RE as Another entity
  Note over DS: 1. TransferDecision (5.5.1-1)
  par order not stated
    DS->>DC: 2. DataCustodianInvolvement (5.5.1-1)
  and
    Note over DS: 3. DisposalRecord, these assets (5.5.1-1)
  and
    DS->>RE: 4. TransferredAssets, no duty on the receiver
  end
```

## F15. Decommissioning a model or system (§5.5.1-2)

<!-- q L869-870 "If a Developer or System Operators decides" .. "configuration details." -->
> If a Developer or System Operators decides to decommission a model and/or system, they shall involve Data Custodians and securely delete applicable data and configuration details.

```mermaid
sequenceDiagram
  participant DS as Developer or System Operator
  participant DC as Data Custodian
  Note over DS: 1. DecommissionDecision (5.5.1-2)
  par order not stated
    DS->>DC: 2. DataCustodianInvolvement (5.5.1-2)
  and
    Note over DS: 3. DeletionRecord, applicable data and configuration (5.5.1-2)
  end
  Note over DS,DC: 4. AssetInventory updated (inferred, 5.2.1-1)
```

## F16. Offering an API to external parties (§5.2.2-1, §5.2.2-2)

The one outward-facing interaction the EN implies, given only through its example:

<!-- q L683-685 "If a Developer offers an API" .. "poison a model." -->
> If a Developer offers an API to external customers or collaborators, they shall apply controls that mitigate attacks on the AI system via the API. For example, placing limits on model access rate to limit an attacker's ability to reverse engineer or overwhelm defences to rapidly poison a model.

```mermaid
sequenceDiagram
  participant C as External customer or collaborator
  participant D as Developer
  Note over D: 1. AccessControlEvaluation, with System Operators (5.2.2-1)
  Note over D: 2. ApiControls, for example access-rate limits (5.2.2-2)
  C->>D: 3. ApiRequest (inferred)
  alt within the limit
    D-->>C: response, not defined by the EN
  else over the limit, for example an attacker (F16-E1)
    D-->>C: access limited, response unspecified
  end
```

## Lifecycles

`state-machine.yaml` holds SM01 ai-system-lifecycle, SM02 model-version, SM03 training-data,
SM04 prompt-and-configuration, SM05 security-update, SM06 cyber-security-incident, SM07
external-component, SM08 end-of-life, SM09 threat-model and SM10 training-content, and lists the
candidate lifecycles the source does not support, with the reason for each (vulnerability, plans,
documentation, API access, human oversight, End-user communications, provider relationship,
asset inventory).

## Open issues

The source questions this model raises are OI-01 to OI-19 in `protocol.yaml`, each with its
quotation: Affected entities definition (OI-01); support without contract (OI-02); dispose while
sharing (OI-03); Principle 10 has no applicability line (OI-04); non-Table 4-1 actors (OI-05);
who assesses creation (OI-06); trained-on tense in design (OI-07); passive threat relay (OI-08);
test without pass criterion (OI-09); antecedent of these updates (OI-10); before or after a
configuration change (OI-11); the above requirements (OI-12); which evaluations (OI-13); System
Operators or Developers choose (OI-14); major undefined (OI-15); re-check triggers (OI-16); no
notice without an update (OI-17); dangling cross-references (OI-18); the voluntary Code (OI-19).

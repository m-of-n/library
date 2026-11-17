---
record: owasp-dsomm
kind: protocol
title: "owasp-dsomm — protocol model"
extracted: "2026-11-16"
reviewed_by: ""
---

# OWASP DSOMM: exchanges stated inside activities

The machine-readable model is `protocol.yaml` (roles, work products, flows F01 to F14 with
their error paths, provisions not in any flow, open issues OI-01 to OI-07). The lifecycles
are `state-machine.yaml` (SM01 to SM15). This file is the prose and one sequence diagram
per flow. Every quotation below is a marker rendered from `.cache/owasp-dsomm.txt` by
`bin/check-quotes --render`; nothing in a blockquote was typed. Requirement ids, activity
uuids and levels live in `protocol.yaml`, where a script emitted them.

## What kind of protocol this is

The model itself defines none: it is a catalogue of 251 activities, and its structure
(dimension, sub-dimension, level, dependsOn) relates activities, not parties. But some
activities describe exchanges between distinct parties in their own text, and say how
they chain:

<!-- q L3391-3396 "It completes the human-oversight ladder" .. "a running agent does." -->
> It completes the human-oversight ladder started by the artifact reviews (_Human review of AI generated specifications_, _Human review of AI generated plans_, _Human review of AI generated code_ in Verification): those gate what is built, this activity gates what a running agent does.

and treat agent-to-agent traffic as a protocol in its own right:

<!-- q L3504-3507 "Explicit trust boundaries treat every delegation" .. "trusting the chain." -->
> Explicit trust boundaries treat every delegation like an external request. The receiving agent verifies the identity and authorization of the delegating agent instead of trusting the chain.

Each flow below is assembled from the activities its `activities` list names (computed
from the lines its quotations and ids come from), in the order their texts state. The
other activities state no exchange this model treats as a flow (`provisions_not_in_flows`
names the near misses) and are carried by `requirements.yaml`.

## Roles

| role | who | source |
|---|---|---|
| organization | the adopting organization (DSOMM names no implementer; inferred) | all |
| development_team | developers and product teams | Culture and Organization, Consolidation |
| security_team | security engineers, champions, SMEs | Consolidation |
| ai_agent | AI agents and coding assistants | Agentic AI |
| peer_agent | the agent receiving a delegation | Trust boundaries between AI agents |
| agent_registry | registry or discovery mechanism | Trust boundaries between AI agents |
| approval_gate | enforcement point: approval step, push proxy | Isolation |
| human_reviewer | reviewer or approver | Verification, Isolation |
| second_approver | the independent second approver | Human approval for irreversible AI agent actions |
| audit_log | the agent audit log | Audit logging of AI agent actions |
| anomaly_detection | detection, tripwires, alerting channel | Guidance, Monitoring |
| containment_automation | pre-approved reversible containment | Automated containment |
| human_responder | the notified human | Automated containment |
| triage_assistant | AI assistant drafting triage | Automated containment, Alerting |
| vcs_host | source code management system | Development and Source Control |
| ci_pipeline | build, test and deployment pipeline | Build and Deployment, Verification |
| requester, access_approver, identity_provider, resource_owner | access parties | Identity and Access Management |
| dependency_bot | automated pull request tool | Patch Management |
| ai_gateway, external_ai_service | LLM gateway and provider | Data Protection, Isolation |
| egress_proxy, external_system | egress point and systems agents reach | Isolation |
| security_tests, vuln_management | scanners and the vulnerability management system | Test and Verification |
| artifact_repository, compromise_intelligence | managed repository and compromise sources | Verification, Static depth |
| traffic_router, monitoring | canary traffic control and checks | Deployment |
| drift_detector | drift detection | Deployment, Verification |
| agent_inventory, dependent_systems | agent inventory and systems holding registrations | Guidance |
| attacker | the adversary of the risks | Agentic AI |

## Reading the diagrams

- A solid arrow hands a work product (named as in `protocol.yaml` work_products) to another role.
- A note over a role is an act of that role alone.
- `opt` is a step that applies only under its condition, or an error path with its outcome
  and kind (stated, inferred, unspecified).
- Numbers are the step numbers of `protocol.yaml`; (inferred) marks this model's own step.

## F01. Approving an AI agent's action (Agentic AI / Isolation)

The last rung of the human-oversight ladder: the reviews of specification, plan and code gate what is built; this gates what a running agent does.

<!-- q L3409-3415 "Classify agent action types by reversibility" .. "default to pre-approval." -->
> Classify agent action types by reversibility and assign approval tiers: pre-approval for irreversible actions, monitoring with an intervention window for reversible actions with business impact (e.g. buffer outbound messages for a defined period so an intervention stops delivery), autonomy only for low-risk reversible actions. If the reversibility of an action class cannot be demonstrated, default to pre-approval.

```mermaid
sequenceDiagram
  participant ORG as Organization
  participant AG as AI agent
  participant GATE as Approval gate
  participant HR as Human reviewer
  participant HR2 as Second approver
  participant LOG as Audit log
  Note over ORG: 1. ActionClassification - tier by reversibility
  AG->>GATE: 2. ActionRequest - proposed action
  opt pre-approval tier
    GATE->>HR: 3. ApprovalRequest - hold, show action and context
  end
  HR->>GATE: 4. ApprovalDecision - approve
  opt high-risk action
    HR2->>GATE: 5. ApprovalDecision - independent second approval
  end
  GATE->>LOG: 6. ApprovalRecord - approver, context, reason
  GATE->>AG: 7. ActionRelease - execute (inferred)
  opt monitoring tier
    GATE->>HR: 8. BufferedAction - intervention window
  end
  opt F01-E1 no approval
    Note over GATE: stays blocked (stated)
  end
  opt F01-E2 human intervenes in the window
    Note over GATE: delivery stopped (stated)
  end
  opt F01-E3 rubber-stamping
    Note over HR: oversight in appearance only (stated)
  end
```

## F02. Delegating a task to another agent (Agentic AI / Isolation / Trust boundaries between AI agents)

DSOMM's one inter-agent protocol, with its rejection paths stated as assessment items.

<!-- q L3504-3507 "Explicit trust boundaries treat every delegation" .. "trusting the chain." -->
> Explicit trust boundaries treat every delegation like an external request. The receiving agent verifies the identity and authorization of the delegating agent instead of trusting the chain.

```mermaid
sequenceDiagram
  participant REG as Agent registry
  participant AG as AI agent
  participant PA as Receiving agent
  participant LOG as Audit log
  participant ATT as Attacker
  REG->>PA: 1. AgentAdmission - verified admission
  AG->>PA: 2. DelegationRequest - scoped, signed, replay-protected
  Note over PA: 3. DelegationCheck - verify delegator
  PA->>AG: 4. DelegationResult - result (inferred)
  PA->>LOG: 5. DelegationRecord - record the communication
  opt F02-E1 unauthorized or unknown delegator
    Note over PA: rejected (stated)
  end
  opt F02-E2 unregistered, replayed or downgraded
    Note over PA: rejected (stated)
  end
  opt F02-E3 confused deputy
    Note over ATT: executed unchecked (the risk) (stated)
  end
```

## F03. An agent's push through the version-control gates (Agentic AI / Isolation; Implementation / Development and Source Control; Agentic AI / Verification)

The guardrails a push meets, in order, each placed where the agent cannot touch it.

<!-- q L2954-2958 "Server-side rejection of pushed secrets" .. "bypass or rewrite." -->
> Server-side rejection of pushed secrets is defined in _Block pushes containing secrets_ (Implementation, Development and Source Control): it applies to humans and agents alike, and because it is enforced on the git host, it belongs to the enforcement points an agent cannot bypass or rewrite.

```mermaid
sequenceDiagram
  participant AG as AI agent
  participant GATE as Approval gate
  participant HR as Human reviewer
  participant SCM as Source code management
  participant CI as Pipeline
  Note over AG: 1. PolicyHookCheck - hook outside write reach
  AG->>GATE: 2. AgentPush - push via proxy
  GATE->>HR: 3. PushReview - held for review
  HR->>GATE: 4. ReviewDecision - release (inferred)
  GATE->>SCM: 5. ForwardedPush - forward (inferred)
  Note over SCM: 6. PushProtection - reject known secret formats
  SCM->>CI: 7. PipelineRun - same pipeline, no bypass
  opt F03-E1 push holds a known secret format
    Note over SCM: rejected, bypass for false positives (stated)
  end
  opt F03-E2 direct route attempted
    Note over SCM: closed to agent credentials (stated)
  end
  opt F03-E3 agent rewrites its guardrails
    Note over AG: managed baseline prevails (stated)
  end
```

## F04. Detecting and containing an anomalous agent (Agentic AI / Guidance; Information Gathering / Monitoring)

Automate the bookkeeping, not the decisions: the activity's own guiding principle.

<!-- q L2365-2369 "Far-reaching decisions remain with humans." .. "communication)." -->
> Far-reaching decisions remain with humans. The guiding principle: automate the bookkeeping (evidence collection, correlation, documentation of the incident), not the decisions (containment of business-critical systems, disclosure, customer communication).

```mermaid
sequenceDiagram
  participant AG as AI agent
  participant LOG as Audit log
  participant DET as Detection and alerting
  participant CONT as Containment automation
  participant TA as Triage assistant
  participant HUM as Notified human
  AG->>LOG: 1. AgentActionRecord - actions recorded
  LOG->>DET: 2. BehaviorDeviation - deviation from profile
  opt honeytoken used
    AG->>DET: 3. TripwireHit - honeytoken used
  end
  DET->>CONT: 4. Detection - routed to containment
  CONT->>AG: 5. ContainmentAction - pause, revoke, reduce
  CONT->>HUM: 6. ContainmentNotice - logged, human notified
  TA->>HUM: 7. TriageContext - drafted triage context
  HUM->>CONT: 8. ContainmentDecision - far-reaching decisions
  HUM->>AG: 9. Reintegration - verify, approve, return
  opt F04-E1 not verified or not approved
    Note over HUM: stays contained (stated)
  end
  opt F04-E2 cascade: fan-out or retry loops
    Note over CONT: alert, circuit breaker stops the plan (stated)
  end
  opt F04-E3 alert reaches nobody
    Note over DET: path must be tested (stated)
  end
```

## F05. An AI-assisted change through the oversight ladder (Agentic AI / Guidance; Agentic AI / Verification)

The human-oversight ladder: one gate per phase, specification first because an error there is multiplied into every downstream artifact.

<!-- q L1218-1222 "Establish a spec-driven workflow" .. "under version control." -->
> Establish a spec-driven workflow for AI-assisted development: specify requirements and acceptance criteria first, derive a plan, implement against the plan and review against the specification. Use tooling that enforces the phases and keep the phase artifacts (specification, plan) under version control.

```mermaid
sequenceDiagram
  participant DEV as Development team
  participant AG as AI agent
  participant HR as Human reviewer
  participant CI as Pipeline
  Note over DEV: 1. FeatureThreatModel - threat model, acceptance criteria
  DEV->>AG: 2. Specification - specify first
  HR->>DEV: 3. SpecificationReview - gate of the specify phase
  AG->>HR: 4. Plan - derive a plan
  HR->>AG: 5. PlanReview - gate of the plan phase
  Note over AG: 6. ContextLoad - step-specific security artifacts
  Note over AG: 7. VerifiedChange - implement, self-verify
  opt AI-suggested dependency
    Note over AG: 8. DependencyValidation - validate suggested package
  end
  AG->>CI: 9. AnalysisFindings - SAST, DAST, SCA in the loop
  AG->>HR: 10. ReviewRequest - present, test edits flagged
  HR->>CI: 11. CodeReviewApproval - human review before merge
  Note over CI: 12. IndependentRerun - independent re-run, merge
  opt F05-E1 specification incomplete
    Note over HR: phase cannot be left (stated)
  end
  opt F05-E2 checks never pass
    Note over AG: budget ends the attempt (stated)
  end
  opt F05-E3 reward hacking
    Note over AG: baseline, review, re-run guard it (stated)
  end
  opt F05-E4 hallucinated or slopsquatted package
    Note over AG: not adopted (stated)
  end
  opt F05-E5 agent approves its own PR
    Note over CI: impossible by branch protection (stated)
  end
```

## F06. Reviewing and merging a pull request (Implementation / Development and Source Control; Culture and Organization / Process; Implementation / Identity and Access Management)

Two-eyes review with segregation of duties, and approvals that go stale on a new commit.

<!-- q L7927-7929 "Implement a policy where any commits made after" .. "re-approval process." -->
> Implement a policy where any commits made after a pull request has been approved automatically revoke that approval, necessitating a fresh review and re-approval process.

```mermaid
sequenceDiagram
  participant DEV as Development team
  participant SCM as Source code management
  participant HR as Human reviewer
  participant CI as Pipeline
  DEV->>SCM: 1. PullRequest - PR to protected branch
  SCM->>HR: 2. PeerReview - security peer review
  HR->>SCM: 3. PeerReview - approval, not by the author
  CI->>SCM: 4. StatusChecks - security checks pass
  opt commit after approval
    DEV->>SCM: 5. NewCommit - commit after approval
  end
  opt commit after approval
    SCM->>HR: 6. ApprovalRevocation - approval revoked, re-review
  end
  Note over SCM: 7. Merge - merge (inferred)
  opt F06-E1 author approves own PR
    Note over SCM: prevented technically (stated)
  end
  opt F06-E2 a status check fails
    Note over SCM: does not proceed (stated)
  end
```

## F07. Just-in-time privileged access and access lifecycle (Implementation / Identity and Access Management)

Zero standing administrative access for day-to-day work.

<!-- q L8570-8572 "Privileged access is requested on demand" .. "day-to-day work." -->
> Privileged access is requested on demand, time-boxed, approved and automatically revoked, so there is zero standing administrative access for day-to-day work.

```mermaid
sequenceDiagram
  participant REQ as Requester
  participant IDP as Identity provider
  participant APP as Access approver
  participant OWN as Access owner
  REQ->>IDP: 1. ElevationRequest - request on demand
  IDP->>APP: 2. ApprovalRequest - approval required
  APP->>IDP: 3. ApprovalDecision - approve
  IDP->>REQ: 4. TimeBoxedGrant - just-in-time, time-boxed
  IDP->>REQ: 5. AccessRevocation - automatic expiry
  opt review cadence
    OWN->>IDP: 6. Recertification - re-attest on cadence
  end
  opt joiner, mover or leaver
    Note over IDP: 7. ProvisioningChange - joiner, mover, leaver
  end
  opt F07-E1 not approved
    Note over IDP: no grant (inferred)
  end
  opt F07-E2 unconfirmed or unused
    Note over IDP: revoked (stated)
  end
  opt F07-E3 break-glass
    Note over REQ: minimal standing set (stated)
  end
```

## F08. Automated dependency updates (Build and Deployment / Patch Management; Information Gathering / Test KPI)

The patch pipeline DSOMM spreads across four activities, in the order they state.

<!-- q L5670-5672 "A good practice is to merge trusted dependencies" .. "after a grace period." -->
> A good practice is to merge trusted dependencies (e.g. spring boot) after a grace period like one week. Often, patches, fixes and minor updates are automatically merged. Be aware that automated merging requires a high automated test coverage. Enforcement of merging of pull requests after a grace period.

```mermaid
sequenceDiagram
  participant BOT as Update tool
  participant SCM as Source code management
  participant DEV as Development team
  participant CI as Pipeline
  Note over BOT: 1. UpdateDetection - watch versions, advisories
  BOT->>SCM: 2. UpdatePullRequest - PR at once
  DEV->>SCM: 3. PatchReview - review and merge per policy
  opt trusted or minor, high coverage
    Note over SCM: 4. AutomatedMerge - auto-merge after grace period
  end
  SCM->>CI: 5. AutomatedDeployment - deploy after merge
  Note over CI: 6. BaseImageRebuild - nightly base images
  Note over DEV: 7. PatchKpi - time to patch vs SLA
  opt F08-E1 coverage too low
    Note over SCM: auto-merge unsafe (stated)
  end
```

## F09. AI traffic through the gateway and the egress point (Agentic AI / Data Protection; Agentic AI / Isolation)

One enforced point per direction: a gateway for model traffic, an egress point for everything else.

<!-- q L228-230 "Route traffic to external AI services through a gateway" .. "of AI tool usage." -->
> Route traffic to external AI services through a gateway that scans prompts and attachments for secrets and personal data, blocks or redacts findings and provides an audit trail of AI tool usage.

```mermaid
sequenceDiagram
  participant DEV as Development team
  participant AG as AI agent
  participant GW as AI gateway
  participant EXT as External AI service
  participant EP as Egress point
  participant XS as External system
  DEV->>GW: 1. PromptTraffic - via the gateway only
  Note over GW: 2. LeakScan - scan, block or redact
  GW->>EXT: 3. FilteredPrompt - within rate and size limits
  Note over GW: 4. AuditTrail - audit trail
  AG->>EP: 5. AgentEgress - allow-listed egress only
  opt where supported
    EP->>XS: 6. CredentialInjection - secretless injection
  end
  Note over AG: 7. BudgetCheck - budgets, iteration caps
  opt F09-E1 secret or personal data in a prompt
    Note over GW: blocked or redacted (stated)
  end
  opt F09-E2 host not allow-listed
    Note over EP: blocked and logged (stated)
  end
  opt F09-E3 rate limit exceeded
    Note over GW: limit triggers (stated)
  end
  opt F09-E4 budget or cap reached
    Note over AG: alert, loop terminates (stated)
  end
```

## F10. Triaging findings and handing them to product teams (Test and Verification / Consolidation; Test and Verification / Static depth for applications)

The finding lifecycle DSOMM builds up over several Consolidation activities, from triaged versus untriaged to a release gate.

<!-- q L11058 "At this maturity level, a simple tracking system suffices" .. "without complex categorization." -->
> At this maturity level, a simple tracking system suffices - tools need only distinguish between "triaged" and "untriaged" findings, without complex categorization.

```mermaid
sequenceDiagram
  participant SCAN as Security tests
  participant VMS as Vulnerability management
  participant TA as Triage assistant
  participant SEC as Security engineers
  participant DEV as Development team
  participant CI as Pipeline
  SCAN->>VMS: 1. Finding - aggregated in one tool
  opt AI-supported triage
    TA->>SEC: 2. TriageProposal - AI-proposed verdict
  end
  SEC->>VMS: 3. TriageDecision - triage, persist outcome
  opt scoped decision
    SEC->>VMS: 4. ScopedSuppression - per artifact or global
  end
  VMS->>DEV: 5. BacklogItem - into the team backlog
  CI->>DEV: 6. QualityGate - release gate by severity
  DEV->>VMS: 7. Fix - resolve, prioritized
  opt F10-E1 false positive
    Note over SEC: documented, not re-analysed (stated)
  end
  opt F10-E2 accepted risk
    Note over SEC: documented as accepted (stated)
  end
  opt F10-E3 high or critical open at release
    Note over CI: not approved for release (stated)
  end
  opt F10-E4 AI would auto-close a true positive
    Note over SEC: human decides (stated)
  end
```

## F11. Adopting a component and reacting to its compromise (Agentic AI / Guidance; Agentic AI / Verification; Test and Verification; Build and Deployment)

Trust at adoption, then continuous re-checking, because compromise comes after approval.

<!-- q L4331-4335 "Trust evaluation at adoption time" .. "a malicious update." -->
> Trust evaluation at adoption time (see _Evaluation of the trust of used AI components_) does not catch compromise that happens afterwards: AI components can be hijacked later like any other dependency, e.g. through a compromised publisher account or a malicious update.

```mermaid
sequenceDiagram
  participant ORG as Organization
  participant AR as Artifact repository
  participant CTI as Compromise intelligence
  Note over ORG: 1. ComponentEvaluation - evaluate before use
  ORG->>AR: 2. ApprovedInventory - approve, pin, inventory
  AR->>ORG: 3. DependencyConsumption - managed repository, cooldown
  CTI->>ORG: 4. CompromiseSignal - match, behaviour deviation
  ORG->>AR: 5. Quarantine - block, purge, rebuild
  opt F11-E1 fails vetting
    Note over ORG: not approved (inferred)
  end
  opt F11-E2 advisory or behaviour deviation
    Note over ORG: identified and blocked (stated)
  end
```

## F12. Releasing a version by canary (Build and Deployment / Deployment / Canary deployment)

Promotion is gated; rollback is automatic.

<!-- q L5399-5400 "Rollback must be automated" .. "without human intervention." -->
> Rollback must be automated and triggered by gate failure without human intervention.

```mermaid
sequenceDiagram
  participant CI as Pipeline
  participant TR as Traffic control
  participant MON as Monitoring
  CI->>TR: 1. CanaryShift - 1-10% for a window
  MON->>CI: 2. GateSignal - SLI and security checks
  opt gates pass
    CI->>TR: 3. Promotion - promote
  end
  opt gate fails
    CI->>TR: 4. Rollback - automatic rollback
  end
  Note over CI: 5. DecisionLog - decisions retained
  opt F12-E1 anomalies reported
    Note over CI: rolled back before broad exposure (stated)
  end
```

## F13. Detecting and answering drift (Build and Deployment / Deployment; Agentic AI / Verification)

Drift is answered by revert or by re-approval, never by leaving it.

<!-- q L5172-5174 "either revert it automatically" .. "regular review process." -->
> either revert it automatically to the approved state or bring the change through the regular review process.

```mermaid
sequenceDiagram
  participant DD as Drift detection
  participant ORG as Organization
  participant HR as Human reviewer
  Note over DD: 1. DriftCheck - deployed vs approved
  DD->>ORG: 2. DriftAlert - alert, high priority
  ORG->>DD: 3. Revert - revert or restore
  opt change kept
    ORG->>HR: 4. ReApproval - regular review, re-approve
  end
  ORG->>DD: 5. ExceptionRecord - document exceptions
  opt F13-E1 out-of-band change
    Note over DD: detected, alerted (stated)
  end
```

## F14. Decommissioning an AI agent (Agentic AI / Guidance)

Switching an agent off is not the end of its lifecycle: every access path must be closed.

<!-- q L1478-1481 "The lifecycle of an AI agent does not end" .. "preserves the audit evidence." -->
> The lifecycle of an AI agent does not end with switching it off. During operation an agent accumulates an identity, credentials, permissions, policies and integrations with other systems. Secure decommissioning unwinds all of them and preserves the audit evidence.

```mermaid
sequenceDiagram
  participant ORG as Organization
  participant INV as Agent inventory
  participant IDP as Identity provider
  participant DS as Dependent systems
  participant LOG as Audit log
  ORG->>INV: 1. StatusUpdate - status in inventory
  ORG->>IDP: 2. IdentityRevocation - revoke identity and grants
  ORG->>DS: 3. Cleanup - clean up dependents
  ORG->>LOG: 4. LogArchive - archive logs
  Note over ORG: 5. ResidualAccessCheck - zero residual access
  opt F14-E1 residual access remains
    Note over ORG: orphaned identity at risk (stated)
  end
  opt F14-E2 logs deleted too early
    Note over ORG: evidence destroyed (stated)
  end
```

## Lifecycles

`state-machine.yaml` holds SM01, the model's own level and dependsOn structure read as an
adoption lifecycle (inferred throughout, with the data derived by script and one
dependency no level reading can satisfy), and SM02 to SM15, lifecycles individual
activities state: an AI agent, an AI-assisted change, a pull request, a finding, deployed
state against its approved version, a canary release, a privileged grant, a dependency
update, a component, agent memory, a WAF's mode, a container image, an ephemeral
environment and an agent action. The term the levels borrow appears only in passing:

<!-- q L5919 "At maturity level 1," .. "such as STRIDE." -->
> At maturity level 1, you perform threat modeling ad-hoc for high-risk applications and use simple threat checklists, such as STRIDE.

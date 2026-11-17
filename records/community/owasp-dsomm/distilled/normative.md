---
record: owasp-dsomm
kind: normative
title: "owasp-dsomm — normative text"
generated_by: bin/fx1-skeleton, restructured by the FX-1 pass 1 requirements lane (script)
reviewed_by: ""
---

# Normative text

OWASP DSOMM v5.1.0 (`generated/model.yaml`) as a normative text: 6 dimensions, 24 sub-dimensions, 251 activities, in source order. The model states no requirement level: nothing in it is mandatory, and an organisation adopts activities level by level. So the normative content is each activity's **measure** (the practice the model recommends at that level), its **assessment** lines where it has them (the evidence an assessor asks for), and the few sentences elsewhere that recommend, scope or permit something; the rest (risk narratives, explanations, tool descriptions) is descriptive and listed by id only.

Every quotation below is a marker `<!-- q Lx-y -->` (with anchors when it is part of a line range) whose words `bin/check-quotes --render` wrote from the source; line numbers are those of `.cache/owasp-dsomm.txt`. The ids are those of `requirements.yaml`: an activity is `owasp-dsomm#<uuid>`, everything else `R-NNNN`. A quoted scalar keeps its quote marks and literal backslash escapes (`\n`, `\u2014`) exactly as the source bytes have them.

## Agentic AI

### Agentic AI / Data Protection

6 activities, levels 2: 1, 3: 1, 4: 3, 5: 1.

#### Basic data leak prevention

`owasp-dsomm#dc62d384-0b9c-47d9-b7a5-9d82e53642ba` · level 2 · depends on AI usage policy (level 2) · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L21-23 -->
> Define which data classes may be used with which AI tools. If a commercial AI is used, use AI offerings with training opt-out and data retention agreements. Train employees to keep secrets and personal data out of prompts.

Measure — recommendation; its sentences: R-0003, R-0245

<!-- q L27-27 -->
> - Show the definition of which data classes may be used with which AI tools.

R-0004 — assessment

<!-- q L28-28 -->
> - Show the enterprise agreements or provider settings (training opt-out, data retention).

R-0246 — assessment

<!-- q L29-29 -->
> - Show the training or awareness material that tells employees to keep secrets and personal data out of prompts.

R-0247 — assessment

Descriptive, not normative: description R-0001, R-0002.

#### Input validation for AI systems

`owasp-dsomm#0012e51c-a068-4549-a4d5-d1957b52676f` · level 3 · usefulness 5 · difficulty knowledge 4, time 3, resources 2 · testable yes

<!-- q L85-88 -->
> Validate and constrain all input entering the model context: separate instructions from data in prompt templates, sanitize or annotate untrusted content, restrict input length and format where possible and use guardrail filters that detect known injection patterns before the model call.

Measure — recommendation

<!-- q L90-90 -->
> - Show prompt templates that separate instructions from untrusted data.

R-0248 — assessment

<!-- q L91-91 -->
> - Show the guardrail or filter configuration applied before the model call and a test where a known injection pattern is detected.

R-0249 — assessment

#### Automated data leak detection for AI interactions

`owasp-dsomm#8d5ce64e-ebf0-45ab-93cb-d592287e3023` · level 4 · depends on Basic data leak prevention (level 2) · usefulness 4 · difficulty knowledge 3, time 3, resources 3 · testable yes

<!-- q L228-230 -->
> Route traffic to external AI services through a gateway that scans prompts and attachments for secrets and personal data, blocks or redacts findings and provides an audit trail of AI tool usage.

Measure — recommendation

<!-- q L217-220 "Typical setup:" .. "for credentials." -->
> Typical setup: route all model traffic through an LLM gateway (e.g. LiteLLM Proxy) and attach scanners as guardrail hooks, such as Presidio for PII redaction and LLM Guard or trufflehog-style secret detectors for credentials.

R-0706 — recommendation (description)

<!-- q L234-234 -->
> - Show the gateway or proxy through which traffic to external AI services flows and its scanner configuration.

R-0250 — assessment

<!-- q L235-235 -->
> - Demonstrate that a test secret or test personal data in a prompt is blocked or redacted.

R-0251 — assessment

<!-- q L236-236 -->
> - Show the audit trail of AI tool usage.

R-0252 — assessment

Descriptive, not normative: risk R-0005.

#### Hallucination detection for AI responses

`owasp-dsomm#51a63793-c2c5-4438-bfd6-b7dee604a76d` · level 4 · depends on Secure output handling in AI applications (level 4) · usefulness 3 · difficulty knowledge 4, time 3, resources 2 · testable yes

<!-- q L389-394 -->
> Validate the factual grounding of AI responses before they are trusted: check claims against the retrieved sources in retrieval-augmented generation (RAG) systems, require and verify citations, verify that emitted URLs, API endpoints and identifiers exist, and route low-confidence or ungrounded answers to a human or suppress them.

Measure — recommendation (promotes C-0016)

<!-- q L398-398 -->
> - Show the groundedness or fact-checking configuration and citations in user-facing answers.

R-0258 — assessment

<!-- q L399-399 -->
> - Show the existence checks for emitted URLs, API endpoints and identifiers.

R-0259 — assessment

<!-- q L400-400 -->
> - Show evaluation results tracking the hallucination rate over prompt, model and guardrail changes.

R-0260 — assessment

<!-- q L360-361 "Applies" .. "ships." -->
> Applies to AI features the organization ships.

R-0253 — scope (description)

<!-- q L365-368 -->
> 1. **Constrain generation**: prefer retrieval-augmented generation over free generation for factual answers and instruct the model to answer only from the provided sources and to say "I don't know" otherwise.

R-0254 — recommendation (description)

<!-- q L373-374 "3." .. "used." -->
> 3. **Existence checks**: mechanically verify artifacts the model emits before they are shown or used.

R-0255 — recommendation (description)

<!-- q L374-376 "Do" .. "system?" -->
> Do referenced URLs resolve, do cited documents exist in the knowledge base, do emitted API endpoints and identifiers exist in the target system?

R-0256 — recommendation (description)

<!-- q L377-379 -->
> 4. **Citations and confidence**: require source citations in user-facing answers and display them, so users can verify claims; route ungrounded or low-confidence answers to a human fallback.

R-0008 — recommendation (description)

<!-- q L380-382 -->
> 5. **Regression testing**: track hallucination rates with an evaluation suite (e.g. promptfoo) over prompt, model and guardrail changes.

R-0257 — recommendation (description)

Descriptive, not normative: description R-0006, R-0007.

#### Secure output handling in AI applications

`owasp-dsomm#24990a5e-b0e6-4e2c-b06b-4e9f0d6f7b21` · level 4 · depends on Input validation for AI systems (level 3); Context-aware output encoding (level 1) · usefulness 5 · difficulty knowledge 3, time 3, resources 2 · testable yes

<!-- q L506-510 -->
> Treat model responses as untrusted data and apply the existing activity [Context-aware output encoding](/activity-description?uuid=e1f37abb-d848-4a3a-b3df-65e91a89dcb7) to them at every sink (browser, shell, SQL, downstream systems). Add the AI-specific controls on top: strict markdown rendering, schema enforcement for tool calls and output guardrails.

Measure — recommendation

<!-- q L472-477 "The sink-side controls" .. "output guardrails." -->
> The sink-side controls are already defined in OWASP DSOMM [Context-aware output encoding](/activity-description?uuid=e1f37abb-d848-4a3a-b3df-65e91a89dcb7); this activity applies them to the AI features the organization ships (chat UIs, retrieval-augmented generation (RAG) features, tool-calling agents) and adds the AI-specific controls: strict markdown rendering, schema enforcement for tool calls and output guardrails.

R-0707 — scope (description)

<!-- q L479-483 "The core of this activity is a reference" .. "Content Security Policy." -->
> The core of this activity is a reference: model responses are untrusted data, and the sink-side controls are already defined in [Context-aware output encoding](/activity-description?uuid=e1f37abb-d848-4a3a-b3df-65e91a89dcb7) (Implementation, Application Hardening): safe framework bindings, encoding libraries, parameterized APIs, Content Security Policy.

R-0708 — scope (description)

<!-- q L499-500 "Whether the content" .. "AI responses_." -->
> Whether the content of a response is factually correct is a separate concern, see _Hallucination detection for AI responses_.

R-0709 — scope (description)

<!-- q L515-515 -->
> - Show the rendering pipeline for model output (markdown renderer settings, sanitizer configuration, Content Security Policy).

R-0265 — assessment

<!-- q L516-516 -->
> - Show the schema validation for structured output and the confirmation step for sensitive tool calls.

R-0266 — assessment

<!-- q L517-517 -->
> - Demonstrate with a test that injected markup and markdown-based exfiltration (external images/links) are neutralized.

R-0267 — assessment

<!-- q L471-472 "Model" .. "input." -->
> Model responses must therefore be treated like user input.

R-0010 — recommendation (description)

<!-- q L483-484 "Apply" .. "input." -->
> Apply them to model output exactly as to user input.

R-0261 — recommendation (description)

<!-- q L488-490 "-" .. "DOMPurify)." -->
> - **Markdown rendering in chat UIs**: render with inline HTML disabled (e.g. `markdown-it` with `html: false`) plus an allow-list HTML sanitizer (e.g. DOMPurify).

R-0262 — recommendation (description)

<!-- q L493-494 "So" .. "domains." -->
> So block or proxy external images and restrict link/image URLs to trusted domains.

R-0263 — recommendation (description)

<!-- q L495-497 -->
> - **Tool/function calls**: enforce a JSON schema on structured output, validate tool-call arguments against allow-lists and require human confirmation for sensitive calls.

R-0264 — recommendation (description)

Descriptive, not normative: description R-0009.

#### Protection of agent memory against poisoning

`owasp-dsomm#106622af-8969-4d9b-81ad-86d8e2bfd631` · level 5 · depends on Input validation for AI systems (level 3) · usefulness 4 · difficulty knowledge 3, time 2, resources 1 · testable yes

<!-- q L630-644 -->
> Treat writes to agent memory and rule files like code changes: keep them under version control and human review, restrict write access to shared rule files and knowledge/vector stores, validate the provenance of ingested knowledge and periodically review or reset persistent memory. Apply retention limits (time-to-live) so that unverified memory, especially content derived from external inputs or tool outputs, expires instead of persisting indefinitely. Version memory stores so that detected poisoning can be answered by rolling back to a known-good state instead of purging everything. Segment memory by user and session and keep credentials and other secrets out of it: cached secrets in shared memory let a later session act with the permissions of an earlier one (OWASP Top 10 for Agentic Applications, ASI03). Do not re-ingest the agent's own outputs into trusted memory automatically, as this self-reinforces errors and planted instructions ("bootstrap poisoning", ASI06).

Measure — recommendation; its sentences: R-0012, R-0268

<!-- q L648-648 -->
> - Show that agent rule files and memory are under version control and require review on change.

R-0269 — assessment

<!-- q L649-649 -->
> - Show the write-access restrictions on shared rule files and knowledge/vector stores.

R-0270 — assessment

<!-- q L650-650 -->
> - Show the last review or reset of persistent agent memory.

R-0271 — assessment

<!-- q L651-651 -->
> - Show the retention limits for unverified memory and demonstrate a rollback of a memory store to a known-good state.

R-0272 — assessment

<!-- q L652-652 -->
> - Show the memory segmentation between users and sessions and the rule that keeps credentials out of agent memory.

R-0273 — assessment

Descriptive, not normative: description R-0011.

### Agentic AI / Guidance

15 activities, levels 1: 1, 2: 6, 3: 5, 4: 2, 5: 1.

#### Static load of security rules

`owasp-dsomm#51ebc877-c4fd-4b50-9305-320152242ddf` · level 1 · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L737-739 -->
> Define and roll out a baseline secure coding rule set for AI assistants covering topics like input validation, output encoding, parameterized queries, secret handling and usage of evaluated components (e.g. images, libraries).

Measure — recommendation (promotes C-0034)

<!-- q L740-740 "-" .. "assistants." -->
> - Show the secure coding rule set for AI assistants.

R-0274 — assessment

<!-- q L740-741 "- Show a" .. "(e.g. via `CLAUDE.md`)." -->
> - Show a sample of project that the rules are loaded automatically (e.g. via `CLAUDE.md`).

R-0275 — assessment

#### AI usage policy

`owasp-dsomm#a511a9a9-1b75-4dfd-8a4f-e516e8096150` · level 2 · usefulness 3 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L828-829 -->
> Define, communicate and enforce a policy for the usage of AI tools during development, including an approval process for new tools and models.

Measure — recommendation (promotes C-0035)

<!-- q L831-831 -->
> - Show the published AI usage policy including approved tools, allowed data classes and handling rules for AI-generated output.

R-0276 — assessment

<!-- q L832-832 -->
> - Show the approval process for new tools and models with a recent example.

R-0277 — assessment

<!-- q L833-833 -->
> - Show how the policy is communicated to employees (e.g. onboarding, training).

R-0278 — assessment

<!-- q L820-822 -->
> An AI usage policy defines which AI tools and models are approved, for which tasks they may be used, which data may be shared with them and how AI-generated output has to be handled (e.g. mandatory review).

R-0013 — scope (description)

#### Instructed load of security rules

`owasp-dsomm#364123db-b41c-431a-94a0-dfd8236b2daa` · level 2 · depends on Static load of security rules (level 1); Spec-driven development (level 2) · usefulness 4 · difficulty knowledge 2, time 1, resources 1 · testable yes

<!-- q L945-948 -->
> Declare in the repository instruction file which security artifact the AI assistant reads at which workflow step (e.g. threat model during planning, secure coding rules during implementation) and verify in sample sessions that the artifacts are actually loaded.

Measure — recommendation (promotes C-0044)

<!-- q L937-938 "Deterministic, tool-enforced" .. "security rules_." -->
> Deterministic, tool-enforced loading of the same mapping is covered by _Dynamic load of security rules_.

R-0710 — scope (description)

<!-- q L953-953 -->
> - Show the step-to-artifact mapping in the instruction file.

R-0279 — assessment

<!-- q L954-954 -->
> - Show a session where the assistant loads the matching security artifact when a workflow step is invoked.

R-0280 — assessment

Descriptive, not normative: description R-0014.

#### Inventory of AI agents

`owasp-dsomm#c1f02ad7-e97e-4c87-b827-7542793ddb0a` · level 2 · depends on AI usage policy (level 2) · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L1023-1026 -->
> Maintain an inventory of all AI agents and assistants: identity/service account, human owner, purpose, granted permissions and connected systems. Review it periodically, decommission stale agents and detect unregistered ones (e.g. via identity provider and audit log analysis).

Measure — recommendation

<!-- q L1030-1030 -->
> - Show the inventory of AI agents with identity, human owner, purpose and granted permissions.

R-0283 — assessment

<!-- q L1031-1031 -->
> - Show the last periodic review and an example of a decommissioned agent.

R-0284 — assessment

<!-- q L1032-1032 -->
> - Explain how unregistered ("shadow") agents are detected, e.g. via identity provider or audit log analysis.

R-0285 — assessment

Descriptive, not normative: risk R-0015 (parts R-0281, R-0282).

#### Language and framework specific security rules

`owasp-dsomm#ac152a8d-2628-4db1-a7d6-6d75031bb40e` · level 2 · depends on Static load of security rules (level 1); Spec-driven development (level 2) · usefulness 4 · difficulty knowledge 3, time 3, resources 1 · testable yes

<!-- q L1108-1112 -->
> Create and maintain secure coding rule sets for every language and framework used in the organization and distribute them to all AI-assisted projects. Review the rules regularly and after security incidents. The rules are to be dynamically imported during the correct spec-driven development phase.

Measure — recommendation

<!-- q L1117-1117 -->
> - Show the rule sets for the languages and frameworks.

R-0286 — assessment

#### Spec-driven development

`owasp-dsomm#923a2a23-d63b-421c-926a-191d1dd5f570` · level 2 · depends on Version control (level 1) · usefulness 3 · difficulty knowledge 2, time 3, resources 1 · testable yes

<!-- q L1218-1222 -->
> Establish a spec-driven workflow for AI-assisted development: specify requirements and acceptance criteria first, derive a plan, implement against the plan and review against the specification. Use tooling that enforces the phases and keep the phase artifacts (specification, plan) under version control.

Measure — recommendation

<!-- q L1226-1226 -->
> - Show the phase artifacts (specification, plan) of a recent AI-assisted change under version control.

R-0287 — assessment

<!-- q L1227-1227 -->
> - Demonstrate the tooling that enforces the phases (e.g. a spec-driven workflow tool).

R-0288 — assessment

Descriptive, not normative: description R-0016.

#### Threat modeling rule

`owasp-dsomm#1caad69c-316c-422a-a56b-04ad6f6cc306` · level 2 · depends on Conduction of simple threat modeling on technical level (level 1); Spec-driven development (level 2) · usefulness 4 · difficulty knowledge 3, time 2, resources 1 · testable yes

<!-- q L1287-1289 -->
> Perform lightweight, feature-level threat modeling before AI-assisted implementation and add the resulting security requirements as acceptance criteria to the user story and to the prompt/task given to the AI assistant.

Measure — recommendation

<!-- q L1294-1294 -->
> - Show user stories whose security acceptance criteria were passed into the AI task or prompt.

R-0290 — assessment

<!-- q L1295-1295 -->
> - Show the lightweight threat modeling notes for a recently implemented feature.

R-0291 — assessment

<!-- q L1279-1280 "AI" .. "all." -->
> AI is the tool, and the feature itself need not involve AI at all.

R-0018 — scope (description)

<!-- q L1280-1281 "Threat" .. "components_." -->
> Threat modeling of applications that *contain* AI components is covered by _Threat modeling of AI components_.

R-0289 — scope (description)

Descriptive, not normative: description R-0017.

#### Audit logging of AI agent actions

`owasp-dsomm#84ba7525-857e-4849-98ba-5fada1a1454d` · level 3 · depends on Inventory of AI agents (level 2); Centralized application logging (level 2) · usefulness 4 · difficulty knowledge 3, time 3, resources 2 · testable yes

<!-- q L1366-1374 -->
> Log every agent action in a structured audit log covering the causal chain: initiator, request, used data sources, tool calls with parameters, generated output, policy decision, delegation context and human approval. Propagate correlation identifiers across agents and systems (e.g. via OpenTelemetry traces) so multi-agent chains stay reconstructable, store the log tamper-evident (e.g. hash chaining, write-once storage) with a defined retention period, and protect the log itself: it contains sensitive prompts and outputs, so restrict access and redact where possible.

Measure — recommendation (promotes C-0060)

<!-- q L1379-1379 -->
> - Show the structured audit log entry of a recent agent action including initiator, tool calls with parameters, data sources and (where required) the human approval.

R-0294 — assessment

<!-- q L1380-1380 -->
> - Demonstrate that a multi-agent chain can be reconstructed end-to-end via correlation identifiers.

R-0021 — assessment

<!-- q L1381-1381 -->
> - Show the tamper protection (e.g. hash chain verification) and the retention configuration of the audit log.

R-0295 — assessment

<!-- q L1382-1382 -->
> - Show who has access to the audit log and how sensitive content in it is protected (e.g. redaction).

R-0296 — assessment

Descriptive, not normative: risk R-0019 (parts R-0292, R-0293), R-0020.

#### Decommissioning of AI agents

`owasp-dsomm#44a195ec-da9e-4fd4-be6d-a5a688852cf7` · level 3 · depends on Inventory of AI agents (level 2); Least privilege on external systems for AI agents (level 3) · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L1494-1502 -->
> Define and enforce a decommissioning checklist that covers every access path: set the agent status in the inventory, revoke the agent identity and its certificates, deactivate associated service accounts and OAuth clients, remove or deny agent-specific permissions and policies, clean up dependent systems (broker registrations, message queue subscriptions, caches, stored sessions, third-party integrations, shadow credentials), archive the audit logs according to the retention requirements and verify after completion that no residual access remains.

Measure — recommendation (promotes C-0067)

<!-- q L1507-1507 -->
> - Show the decommissioning checklist and the completed protocol of a recently retired agent (timestamp, reason, approver).

R-0298 — assessment

<!-- q L1508-1508 -->
> - Demonstrate for a retired agent that its identity, credentials, permissions and registrations in dependent systems no longer grant access (zero residual access).

R-0299 — assessment

<!-- q L1509-1509 -->
> - Show that the audit logs of the retired agent are archived according to the retention requirements.

R-0300 — assessment

<!-- q L1482-1483 -->
> The _Inventory of AI agents_ records what exists; this activity ensures that what is retired actually loses all access.

R-0297 — scope (description)

#### Evaluation of the trust of used AI components

`owasp-dsomm#399c5b7f-1310-4841-89f7-16daff2fe3ef` · level 3 · depends on AI usage policy (level 2); Evaluation of the trust of used components (level 2) · usefulness 4 · difficulty knowledge 3, time 2, resources 1 · testable yes

<!-- q L1588-1599 -->
> Evaluate and approve AI tool, server, skill and model integrations before use: verify publisher and supply chain, review requested permissions and data flows, verify that declared capabilities match the actual code and instructions (behavioral integrity, e.g. via a behavioral classification registry), use safe model formats (e.g. safetensors instead of pickle), pin versions and maintain an inventory of allowed integrations and models. For model artifacts, record provenance, training data lineage and fine-tuning parameters in an AI Bill of Materials (AI-BOM), e.g. based on OWASP's extension of the CycloneDX machine learning bill of materials (ML-BOM), so model components carry the same supply chain evidence as code dependencies (see _SBOM of components_ in Build and Deployment).

Measure — recommendation

<!-- q L1574-1577 "The generic trust evaluation" .. "is adopted." -->
> The generic trust evaluation of components is defined in _Evaluation of the trust of used components_ (Build and Deployment); this activity adds the AI-specific checks before a component is adopted.

R-0711 — scope (description)

<!-- q L1577-1579 "Compromise after approval" .. "AI components_." -->
> Compromise after approval is covered by _Continuous detection of compromised AI components_.

R-0712 — scope (description)

<!-- q L1604-1604 -->
> - Show the approval process and the inventory of allowed AI integrations (tools, MCP servers, skills, models) with pinned versions.

R-0301 — assessment

<!-- q L1605-1605 -->
> - Show the vetting record of a recently added integration (publisher, permissions, behavioral integrity check).

R-0302 — assessment

Descriptive, not normative: description R-0022; implementation R-0023.

#### Threat modeling of AI components

`owasp-dsomm#5a1cd6cd-ebd0-4e70-b314-37b8ab0b7d8d` · level 3 · depends on Conduction of simple threat modeling on technical level (level 1) · usefulness 4 · difficulty knowledge 4, time 3, resources 1 · testable yes

<!-- q L1762-1768 -->
> Extend the established threat modeling practice to AI components: model the context window, tool integrations, agents and data sources explicitly and use AI-specific threat catalogs (e.g. OWASP Top 10 for LLM Applications, MITRE ATLAS) alongside the generic methodology. For agentic systems, the MAESTRO framework of the Cloud Security Alliance (CSA) structures threats along seven layers, from the foundation model to the agent ecosystem.

Measure — recommendation

<!-- q L1727-1729 "General threat modeling practices" .. "subdimension _Design_." -->
> General threat modeling practices (how to run sessions, processes and standards) are defined in the _Culture and Organization_ dimension, subdimension _Design_.

R-0713 — scope (description)

<!-- q L1735-1738 "Passing security requirements" .. "development_." -->
> Passing security requirements into AI-*assisted* implementation of arbitrary features is covered by _Security requirements for AI-assisted development_.

R-0714 — scope (description)

<!-- q L1740-1744 "A data-centric approach" .. "threat modeling)." -->
> A data-centric approach works well for the AI delta: follow the data (prompts, retrieved documents, tool results, training and evaluation data) through every transformation and storage point and model the threats along that flow, as described in the guidance of NIST SP 800-154 (data-centric system threat modeling).

R-0715 — recommendation (description)

<!-- q L1772-1772 -->
> - Show a threat model of an AI feature that covers the model context, tool integrations, agents and data sources.

R-0306 — assessment

<!-- q L1773-1773 -->
> - Show which AI-specific threat catalog (e.g. OWASP Top 10 for LLM Applications, MITRE ATLAS) was used and the resulting mitigations.

R-0307 — assessment

<!-- q L1729-1729 "This" .. "delta." -->
> This activity only adds the AI-specific delta.

R-0303 — scope (description)

<!-- q L1734-1735 "The" .. "components." -->
> The subject here is the product: applications that contain AI components.

R-0304 — scope (description)

<!-- q L1753-1755 "Favor" .. "expired." -->
> Favor controls that take a capability away entirely, such as a network path that simply does not exist or a credential that has already expired.

R-0305 — recommendation (description)

#### Tripwires for AI agent environments

`owasp-dsomm#0d617373-e48f-4bbe-9792-a1bd82b25c54` · level 3 · depends on Alerting (level 2) · usefulness 4 · difficulty knowledge 2, time 1, resources 1 · testable yes

<!-- q L1994-2001 -->
> Plant honeytokens (e.g. fake cloud credentials, API keys or documents that alert on use) in locations AI agents can reach but no legitimate workflow uses: the agent workspace, memory and configuration paths and tool-reachable data stores. Route triggered tokens into the existing alerting channel with a defined response (contain the agent, revoke real credentials, investigate via the audit log), and verify regularly that a triggered token actually produces an alert that a human receives.

Measure — recommendation; its sentences: R-0026, R-0308

<!-- q L2005-2005 -->
> - Show where honeytokens are planted in agent-reachable locations (workspace, memory or configuration paths, tool-reachable data stores).

R-0309 — assessment

<!-- q L2006-2006 -->
> - Trigger a test token and show the resulting alert including who received it and the defined response.

R-0310 — assessment

<!-- q L2007-2007 -->
> - Show the documented response procedure for a triggered tripwire and the protocol of the last alert-path test.

R-0311 — assessment

<!-- q L1983-1986 "Whereas" .. "is\ndecoration." -->
> Whereas _Anomaly detection for AI agent behavior_ needs a\nbehavior profile and produces probabilistic signals, a tripwire\nneeds neither and fires exactly once at the moment of compromise.\nThe alert path must be tested: a tripwire nobody receives is\ndecoration.

R-0025 — recommendation (description)

Descriptive, not normative: description R-0024.

#### Anomaly detection for AI agent behavior

`owasp-dsomm#99049c0a-400f-4c58-986c-ab448ca8e0fc` · level 4 · depends on Audit logging of AI agent actions (level 3); Alerting (level 2) · usefulness 4 · difficulty knowledge 4, time 3, resources 2 · testable yes

<!-- q L2091-2098 -->
> Define an expected behavior profile per AI agent (used tools, data volumes, action frequency, typical target systems) and detect deviations from it: start with rule-based thresholds (e.g. tool-call rate, data volume per time window, first-time access to a system), extend towards statistical or learning-based detection. Route detections into the existing alerting channel with a defined response, e.g. pause the agent or revoke its credentials, then investigate via the audit log.

Measure — recommendation; its sentences: R-0312

<!-- q L2081-2083 "This activity builds on" .. "(Information Gathering)." -->
> This activity builds on _Audit logging of AI agent actions_ and feeds detections into the generic _Alerting_ (Information Gathering).

R-0716 — scope (description)

<!-- q L2103-2103 -->
> - Show the expected behavior profile of an AI agent and the detection rules or models derived from it.

R-0313 — assessment

<!-- q L2104-2104 -->
> - Demonstrate an alert for anomalous agent behavior (e.g. unusual tool-call frequency or first-time access to a system) and the defined response (e.g. pausing the agent, revoking credentials).

R-0314 — assessment

<!-- q L2105-2105 -->
> - Show how a past alert was investigated using the audit log.

R-0315 — assessment

#### Dynamic load of security rules

`owasp-dsomm#862d08a4-7299-4b2c-9d38-8fcaade66d3e` · level 4 · depends on Static load of security rules (level 1); Threat modeling rule (level 2); Spec-driven development (level 2); Instructed load of security rules (level 2) · usefulness 4 · difficulty knowledge 4, time 2, resources 1 · testable yes

<!-- q L2264-2268 -->
> Structure AI-assisted development workflows so that each step loads its relevant security artifacts into the model context (e.g. via step-specific instruction templates in spec-driven development). Verify that security requirements from the specification are carried through plan, implementation and review steps.

Measure — recommendation; its sentences: R-0323

<!-- q L2275-2275 -->
> - Show the mapping of security artifacts to workflow steps (step templates or hook configuration).

R-0324 — assessment

<!-- q L2276-2276 -->
> - Demonstrate that the matching security artifact is loaded into the model context when a workflow step is invoked.

R-0325 — assessment

<!-- q L2205-2208 "Security" .. "verification." -->
> Security artifacts are therefore assigned to the step where they are effective: security requirements and abuse cases during specification, threat model results during planning, secure coding rules during implementation, review checklists during verification.

R-0316 — recommendation (description)

<!-- q L2209-2211 -->
> In contrast to the instruction-based mapping of _Instructed load of security rules_, this activity requires the loading to be enforced by the tooling instead of relying on the model to follow instructions.

R-0317 — scope (description)

<!-- q L2216-2217 "1." .. "`.specify/templates/`)." -->
> 1. **Extend the step templates**: add the security artifact references directly to the phase templates (e.g. `.specify/templates/`).

R-0318 — permission (description)

<!-- q L2220-2223 "2." .. "`additionalContext`." -->
> 2. **Hook that detects the step command** (update-safe and automatic): a `UserPromptSubmit` hook fires on every prompt, checks which workflow command was invoked and injects the matching file as `additionalContext`.

R-0319 — permission (description)

<!-- q L2246-2251 "3." .. "fileMatch`." -->
> 3. **Meta-framework with per-step context loading**: spec-driven meta-frameworks let the workflow definition itself declare which documents each phase loads, e.g. BMAD-Method agents and tasks declare the checklists and templates they load when activated, and Kiro steering files are included conditionally via `inclusion: fileMatch`.

R-0320 — permission (description)

<!-- q L2251-2254 "A" .. "rules_)." -->
> A meta-framework satisfies this activity only where the tool enforces the inclusion: if its phases are themselves just instructions the model follows, the loading remains probabilistic (see _Instructed load of security rules_).

R-0321 — scope (description)

<!-- q L2256-2257 -->
> Keep the loaded artifacts small and step-specific: the goal is the right rules in context, not all rules.

R-0322 — recommendation (description)

Descriptive, not normative: description R-0027, R-0028.

#### Automated containment of anomalous AI agents

`owasp-dsomm#3bbd6dd9-0821-426c-8a19-41737ed61459` · level 5 · depends on Anomaly detection for AI agent behavior (level 4); Least privilege on external systems for AI agents (level 3) · usefulness 4 · difficulty knowledge 4, time 3, resources 2 · testable yes

<!-- q L2380-2394 -->
> Define an automated containment action per detection class and wire it to the anomaly detection: pause the agent, terminate its sessions, revoke its credentials or reduce its privileges. Keep the actions reversible and graduated by confidence and severity, log every automated action and notify a human immediately. Let an AI assistant draft the triage context (timeline, affected systems, collected evidence) so the notified human decides instead of collecting, and test the containment path regularly like a fire drill. Alert on cascade symptoms such as rapid fan-out (one decision triggers many downstream agents or tasks) and oscillating retry loops between agents, and place circuit breakers between planning and execution so that a runaway plan stops instead of propagating. Return a contained agent to production only after its instructions, memory and dependencies have been verified against a known-good state and a human has approved the reintegration.

Measure — recommendation; its sentences: R-0326, R-0327

<!-- q L2357-2358 "_Anomaly detection for AI agent behavior_ raises" .. "acted on." -->
> _Anomaly detection for AI agent behavior_ raises the signal; this activity determines how fast it is acted on.

R-0717 — scope (description)

<!-- q L2365 "Far-reaching decisions" .. "with humans." -->
> Far-reaching decisions remain with humans.

R-0718 — scope (description)

<!-- q L2365-2369 "The guiding principle:" .. "customer communication)." -->
> The guiding principle: automate the bookkeeping (evidence collection, correlation, documentation of the incident), not the decisions (containment of business-critical systems, disclosure, customer communication).

R-0719 — recommendation (description)

<!-- q L2399-2399 -->
> - Show the mapping of detection classes to automated containment actions and their graduation by confidence and severity.

R-0328 — assessment

<!-- q L2400-2400 -->
> - Demonstrate in a test that an anomalously behaving agent is automatically paused or its credentials revoked, the action is logged and a human is notified.

R-0329 — assessment

<!-- q L2401-2401 -->
> - Show the drafted triage context of a past or simulated incident and the human decision based on it.

R-0330 — assessment

<!-- q L2402-2402 -->
> - Show the protocol of the last containment test.

R-0331 — assessment

<!-- q L2403-2403 -->
> - Show the cascade guardrails (fan-out alerts, circuit breakers between planning and execution) and the reintegration protocol of a contained agent.

R-0332 — assessment

<!-- q L2369-2372 "In" .. "ASI08)." -->
> In multi-agent systems, containment also has to stop cascades: one faulty or compromised agent can trigger many downstream agents in a short time (OWASP Top 10 for Agentic Applications, ASI08).

R-0030 — recommendation (description)

Descriptive, not normative: description R-0029.

### Agentic AI / Isolation

9 activities, levels 1: 1, 2: 3, 3: 3, 4: 2.

#### Usage of sandboxing for AI agents

`owasp-dsomm#4debe8ea-f54a-4a00-a1cb-6fad9e571a88` · level 1 · usefulness 4 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L2503-2505 -->
> Run AI agents and AI coding assistants with command execution capabilities in a dedicated, least-privilege sandbox (e.g. a container or virtual machine) which contains only the required project files and is destroyed after use.

Measure — recommendation (promotes C-0121)

<!-- q L2495 "Destroy the environment" .. "is finished." -->
> Destroy the environment after the task is finished.

R-0720 — recommendation (description)

<!-- q L2495-2496 "Restricting network egress" .. "AI agents_." -->
> Restricting network egress of the sandbox is addressed by _Network isolation for AI agents_.

R-0721 — scope (description)

<!-- q L2507-2507 -->
> - Show the sandbox configuration used for AI agent runs (e.g. a dev container definition) and demonstrate a live agent session running inside it.

R-0335 — assessment

<!-- q L2508-2508 -->
> - Show that only the project working directory is mounted and no credentials (SSH keys, cloud CLI configuration) are reachable from inside the environment.

R-0336 — assessment

<!-- q L2509-2509 -->
> - Demonstrate that the environment is destroyed after the task is finished.

R-0337 — assessment

<!-- q L2491-2493 "Use" .. "mechanisms." -->
> Use a sandboxing technology to isolate agent runs, e.g. container-based isolation (dev containers), lightweight virtual machines or OS-level sandboxing mechanisms.

R-0333 — recommendation (description)

<!-- q L2493-2494 "Mount" .. "capabilities." -->
> Mount only the repository being worked on, avoid mounting credentials (e.g. cloud CLI configuration, SSH keys) and drop unneeded capabilities.

R-0334 — recommendation (description)

Descriptive, not normative: risk R-0031, R-0032; implementation R-0033.

#### Permission management for AI agents

`owasp-dsomm#4a618049-19da-4e20-b933-81f203ecd4d2` · level 2 · usefulness 4 · difficulty knowledge 2, time 1, resources 1 · testable yes

<!-- q L2627-2631 -->
> "Configure agent permissions default-deny if agents are not isolated (e.g. least privileges with a container): \nrequire confirmation for sensitive operations (pushes, deletions, network access, credential\npaths), distribute a hardened baseline configuration to all projects and\naudit the accumulated allow-lists regularly."

Measure — recommendation

<!-- q L2633-2633 -->
> - Show the hardened baseline permission configuration that is distributed to projects.

R-0338 — assessment

<!-- q L2634-2634 -->
> - Demonstrate that a sensitive operation (e.g. push, deletion, access to credential paths) requires confirmation.

R-0339 — assessment

<!-- q L2635-2635 -->
> - Show the last audit of accumulated allow-lists including date and findings.

R-0340 — assessment

Descriptive, not normative: description R-0034.

#### Rate limiting and resource budgets for AI systems

`owasp-dsomm#64aef733-bfb0-4df4-95de-bcecf668605d` · level 2 · depends on Monitoring of costs (level 2); Alerting (level 2) · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L2743-2748 -->
> Enforce rate limits per user, API key or tenant on all AI endpoints and restrict input size before it reaches the model. Set token and cost budgets per agent, team and time period, with alerts before a budget is exhausted. Cap agent iterations (maximum tool calls or recursion depth per task) so runaway loops terminate. An LLM gateway or proxy centralizes these limits across models and providers.

Measure — recommendation

<!-- q L2732-2734 "The generic resource limits" .. "(Implementation)." -->
> The generic resource limits for infrastructure are defined in _Virtual environments are limited_ (Implementation).

R-0722 — scope (description)

<!-- q L2734-2735 "This activity adds the AI-specific units" .. "and cost." -->
> This activity adds the AI-specific units: requests, tokens and cost.

R-0723 — scope (description)

<!-- q L2753-2753 -->
> - Show the rate limit configuration of an AI endpoint and a test where the limit triggers.

R-0341 — assessment

<!-- q L2754-2754 -->
> - Show the token and cost budgets per agent or team and the alert before a budget is exhausted.

R-0342 — assessment

<!-- q L2755-2755 -->
> - Show the iteration cap of an agent and what happens when it is reached.

R-0343 — assessment

Descriptive, not normative: description R-0035.

#### Untrusted workspace handling for AI agents

`owasp-dsomm#859c71b6-110f-40a9-9c98-20e8314ebdb7` · level 2 · depends on Usage of sandboxing for AI agents (level 1) · usefulness 4 · difficulty knowledge 2, time 1, resources 1 · testable yes

<!-- q L2856-2859 -->
> Treat third-party repositories as untrusted workspaces: open them only in an isolated container, do not honor repo-local agent configuration (hooks, MCP servers, settings) of untrusted origin, keep agent versions patched and never disable workspace trust prompts.

Measure — recommendation (promotes C-0134)

<!-- q L2863-2863 -->
> - Show the documented procedure for opening third-party repositories with AI agents.

R-0344 — assessment

<!-- q L2864-2864 -->
> - Demonstrate that workspace trust prompts are enabled and that repository-local agent configuration (hooks, MCP servers, settings) is not honored for untrusted repositories.

R-0345 — assessment

<!-- q L2865-2865 -->
> - Show how agent versions are kept patched (update mechanism or policy).

R-0346 — assessment

Descriptive, not normative: description R-0036, R-0037; implementation R-0038.

#### Enforcement of guardrails outside the reach of AI agents

`owasp-dsomm#c01906d5-4db2-4a9d-a692-63928ff6575c` · level 3 · depends on Permission management for AI agents (level 2); Block pushes containing secrets (level 3) · usefulness 4 · difficulty knowledge 3, time 2, resources 2 · testable yes

<!-- q L2967-2971 -->
> Enforce agent guardrails at points outside the agent's write reach: administratively managed permission baselines that local settings cannot override (including disabled standing auto-approve), policy hooks stored outside the workspace and an approval gate at the version control boundary for agent pushes.

Measure — recommendation; its sentences: R-0046

<!-- q L2976-2976 -->
> - Show the administratively enforced permission baseline and demonstrate that a local project or user setting (e.g. enabling auto-approve) does not override it.

R-0350 — assessment

<!-- q L2977-2977 -->
> - Show that policy hooks run from a location the agent cannot write to.

R-0047 — assessment

<!-- q L2978-2978 -->
> - Demonstrate that an agent push is held at the approval gate (proxy) and that the direct route to the version control host is closed for agent credentials.

R-0351 — assessment

<!-- q L2930-2932 "_Permission" .. "definition." -->
> _Permission management for AI agents_ defines what an agent may do; this activity makes sure neither the agent nor a convenience-driven user can weaken that definition.

R-0039 — scope (description); its parts: R-0347 may scope, R-0348 can scope

<!-- q L2935-2936 "Enforcement" .. "touch:" -->
> Enforcement therefore has to move to points the agent process cannot touch:

R-0041 — recommendation (description)

<!-- q L2938-2941 -->
> - **Managed configuration**: distribute the permission baseline via administratively enforced settings that local project or user configuration cannot override, and disable standing auto-approve modes there.

R-0042 — recommendation (description)

<!-- q L2942-2944 "-" .. "modify." -->
> - **Hooks outside the write reach**: store policy hooks that run before tool calls outside the workspace and repository the agent can modify.

R-0043 — recommendation (description)

<!-- q L2944-2946 "Prefer" .. "code." -->
> Prefer narrow allow-lists over deny-lists: deny patterns are obfuscatable, and an allowed interpreter can run arbitrary code.

R-0044 — recommendation (description)

<!-- q L2947-2952 -->
> - **Approval gate at the version control boundary**: route agent pushes through a proxy that holds them for review (e.g. FINOS GitProxy) and close the direct route to the version control host through credential and network design (see _Network isolation for AI agents_ and _Least privilege on external systems for AI agents_).

R-0349 — recommendation (description)

<!-- q L2954-2958 -->
> Server-side rejection of pushed secrets is defined in _Block pushes containing secrets_ (Implementation, Development and Source Control): it applies to humans and agents alike, and because it is enforced on the git host, it belongs to the enforcement points an agent cannot bypass or rewrite.

R-0045 — scope (description)

Descriptive, not normative: description R-0040.

#### Least privilege on external systems for AI agents

`owasp-dsomm#45f722b2-25b4-472a-a743-f7207a77b5c9` · level 3 · depends on Permission management for AI agents (level 2) · usefulness 4 · difficulty knowledge 3, time 2, resources 2 · testable yes

<!-- q L3069-3074 -->
> Provide AI agents with dedicated identities and short-lived, minimally scoped credentials (e.g. fine-grained access tokens restricted to one repository). Where supported, keep credentials out of the agent process entirely: a proxy or gateway injects them at the network boundary ("secretless" architecture), so a prompt-injected agent cannot exfiltrate what it never holds. Log and review agent actions separately from human actions.

Measure — recommendation; its sentences: R-0050

<!-- q L3078-3078 -->
> - Show a dedicated agent identity in the source code management system (or other external system) and the scopes granted to it.

R-0352 — assessment

<!-- q L3079-3079 -->
> - Show that agent credentials are short-lived and minimally scoped (token configuration or issuance policy).

R-0353 — assessment

<!-- q L3080-3080 -->
> - Show where agent credentials are stored and injected, preferably outside the agent process (e.g. credential injection at a proxy or gateway).

R-0354 — assessment

<!-- q L3081-3081 -->
> - Demonstrate that agent actions are distinguishable from human actions in the audit log.

R-0355 — assessment

Descriptive, not normative: description R-0048; risk R-0049.

#### Network isolation for AI agents

`owasp-dsomm#951e6090-057b-4dc4-8b4f-18c6adcfc1ab` · level 3 · depends on Usage of sandboxing for AI agents (level 1) · usefulness 4 · difficulty knowledge 3, time 3, resources 2 · testable yes

<!-- q L3249-3251 -->
> Limit network access of AI agent environments to an allow-list of required endpoints (e.g. model API, package registries, source code management system). Deny all other egress traffic by default.

Measure — recommendation; its sentences: R-0360

<!-- q L3255-3255 -->
> - Show the egress policy of the agent environment (firewall init script, proxy configuration or network policies) including the domain allow-list.

R-0361 — assessment

<!-- q L3256-3256 -->
> - Demonstrate from inside the agent environment that an allow-listed endpoint is reachable and a request to an arbitrary host is blocked.

R-0362 — assessment

<!-- q L3257-3257 -->
> - Show where blocked egress attempts are logged and who reviews them.

R-0363 — assessment

<!-- q L3218-3223 "1." .. "system." -->
> 1. **Firewall inside the container**: on container start, an init script running with the `NET_ADMIN` capability configures a default-deny egress policy (iptables) and resolves an allow-list of required domains into an ipset: model API (e.g. `api.anthropic.com`), package registries (e.g. `registry.npmjs.org`) and the source code management system.

R-0356 — permission (description)

<!-- q L3224-3225 "The" .. "by." -->
> The agent process runs as a non-root user afterwards, so it cannot alter the firewall rules it is confined by.

R-0051 — permission (description)

<!-- q L3226-3230 "2." .. "requests." -->
> 2. **Alternative, egress proxy**: attach the container to an internal network without direct internet access (e.g. `docker network create --internal`) and route traffic through a filtering HTTP(S) proxy (`HTTPS_PROXY` environment variable) that enforces the domain allow-list and logs all requests.

R-0357 — permission (description)

<!-- q L3230-3232 "In" .. "gateway." -->
> In Kubernetes, enforce the same with NetworkPolicies or a service mesh egress gateway.

R-0358 — permission (description)

<!-- q L3233-3235 -->
> 3. **DNS**: allow DNS only to the internal resolver and only for allow-listed domains, otherwise blocked domains remain reachable via direct IP or DNS tunneling can be used for exfiltration.

R-0052 — recommendation (description)

<!-- q L3236-3238 -->
> 4. **Verify**: from inside the running container, check that a request to an allow-listed endpoint succeeds and a request to an arbitrary host (e.g. `curl https://example.com`) is blocked.

R-0359 — recommendation (description)

Descriptive, not normative: description R-0053; risk R-0054; implementation R-0055.

#### Human approval for irreversible AI agent actions

`owasp-dsomm#cd1cb2bd-4bd6-4b9f-beaa-921fe9ea9576` · level 4 · depends on Permission management for AI agents (level 2); Audit logging of AI agent actions (level 3) · usefulness 4 · difficulty knowledge 3, time 3, resources 2 · testable yes

<!-- q L3409-3419 -->
> Classify agent action types by reversibility and assign approval tiers: pre-approval for irreversible actions, monitoring with an intervention window for reversible actions with business impact (e.g. buffer outbound messages for a defined period so an intervention stops delivery), autonomy only for low-risk reversible actions. If the reversibility of an action class cannot be demonstrated, default to pre-approval. Require a second, independent approver for high-risk actions, record the approver identity, the decision context and the reason in the audit log, and design the approval step so the approver actually sees the action and its context instead of clicking through.

Measure — recommendation; its sentences: R-0365, R-0058

<!-- q L3389-3391 "Whereas _Permission management" .. "those tools." -->
> Whereas _Permission management for AI agents_ governs the agent's tool-level permission model, this activity governs the business actions an agent performs through those tools.

R-0724 — scope (description)

<!-- q L3391-3396 "It completes the human-oversight ladder" .. "a running agent does." -->
> It completes the human-oversight ladder started by the artifact reviews (_Human review of AI generated specifications_, _Human review of AI generated plans_, _Human review of AI generated code_ in Verification): those gate what is built, this activity gates what a running agent does.

R-0725 — scope (description)

<!-- q L3424-3424 -->
> - Show the classification of agent action types by reversibility and the approval tier assigned to each class.

R-0366 — assessment

<!-- q L3425-3425 -->
> - Demonstrate that an irreversible action (e.g. an outbound message or a permission change) is blocked until a human approves it, and that an intervention within the monitoring window stops a buffered action.

R-0367 — assessment

<!-- q L3426-3426 -->
> - Show a high-risk action with two documented, independent approvals.

R-0368 — assessment

<!-- q L3427-3427 -->
> - Show an audit log entry of an approval including approver identity, decision context and reason.

R-0369 — assessment

<!-- q L3381-3388 "Graduated" .. "principle)." -->
> Graduated human oversight assigns every class of agent action an approval tier based on its reversibility: low-risk, reversible actions run autonomously within guardrails; reversible actions with business impact run under monitoring with an intervention window; irreversible actions (financial transactions, permission changes, sharing data with third parties, outbound communication) require explicit human approval before execution, high-risk ones by two independent people (four-eyes principle).

R-0364 — recommendation (description)

Descriptive, not normative: risk R-0056, R-0057.

#### Trust boundaries between AI agents

`owasp-dsomm#abe74dfd-d554-4ec5-8b94-f75d352afaaa` · level 4 · depends on Least privilege on external systems for AI agents (level 3); Audit logging of AI agent actions (level 3) · usefulness 4 · difficulty knowledge 4, time 3, resources 2 · testable yes

<!-- q L3525-3538 -->
> Give every agent its own identity and its own credentials, never shared between agents. Scope each delegated task to the minimum permissions it needs instead of passing on the delegating agent's access context. Check at every step of a multi-agent workflow that the delegating agent is who it claims to be and is authorized to request the action. Secure the communication channel itself with mutual authentication and signed messages (e.g. mutual TLS), replay protection (e.g. nonces and expiry times) and rejection of protocol downgrades. Accept agents into a workflow only from a registry or discovery mechanism that verifies agent identity and descriptors. Record the communication between agents so that delegations deviating from the usual patterns surface for review (see _Audit logging of AI agent actions_ and _Anomaly detection for AI agent behavior_).

Measure — recommendation; its sentences: R-0370, R-0371

<!-- q L3514-3517 "_Least privilege on external systems for AI agents_ scopes" .. "agents themselves." -->
> _Least privilege on external systems for AI agents_ scopes each agent's access to external systems; this activity scopes the trust between the agents themselves.

R-0726 — scope (description)

<!-- q L3543-3543 -->
> - Show that each agent in a multi-agent workflow has its own identity and credentials (no shared credentials).

R-0372 — assessment

<!-- q L3544-3544 -->
> - Show how a delegated task receives a reduced permission scope instead of the delegating agent's full access context.

R-0373 — assessment

<!-- q L3545-3545 -->
> - Demonstrate that a delegation from an unauthorized or unknown agent is rejected.

R-0374 — assessment

<!-- q L3546-3546 -->
> - Show how inter-agent messages are authenticated and protected against replay, and that a message from an unregistered agent or a protocol downgrade is rejected.

R-0375 — assessment

<!-- q L3547-3547 -->
> - Show how inter-agent communication is logged and how unusual delegation patterns are flagged.

R-0376 — assessment

<!-- q L3507-3511 "The" .. "Communication)." -->
> The messages between agents need the same protection as the delegation itself: without mutual authentication, message signing and replay protection, an attacker can spoof or replay agent messages and register fake agents in the discovery mechanism (ASI07, Insecure Inter-Agent Communication).

R-0059 — recommendation (description)

### Agentic AI / Verification

10 activities, levels 2: 5, 3: 3, 4: 1, 5: 1.

#### Human review of AI generated plans

`owasp-dsomm#1bd1308d-ae3b-499a-ae81-818993571f52` · level 2 · depends on Human review of AI generated specifications (level 2); Spec-driven development (level 2) · usefulness 4 · difficulty knowledge 3, time 2, resources 1 · testable yes

<!-- q L3658-3664 -->
> Require human review of the plan before AI-assisted implementation: verify that every security requirement from the specification is carried through, that security-relevant design decisions are justified and that changes to security-critical components are flagged for deeper review. In spec-driven workflows, make this review the gate of the plan phase and keep the reviewed plan under version control.

Measure — recommendation; its sentences: R-0377

<!-- q L3669-3669 -->
> - Show a recent AI-generated plan and its documented human review before implementation.

R-0378 — assessment

<!-- q L3670-3670 -->
> - Show that the review traced the security requirements from the specification into the plan.

R-0379 — assessment

<!-- q L3671-3671 -->
> - Show how plans touching security-critical components are flagged for deeper review.

R-0380 — assessment

<!-- q L3646-3649 "In" .. "way." -->
> In spec-driven development this is the gate of the plan phase; agents also propose plans outside formal workflows (e.g. a plan mode) that can be reviewed the same way.

R-0060 — scope (description)

#### Human review of AI generated specifications

`owasp-dsomm#09307f26-bf34-49c2-828e-649130876978` · level 2 · depends on Spec-driven development (level 2) · usefulness 5 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L3757-3762 -->
> Require human review of the specification before AI-assisted implementation starts: are the security acceptance criteria complete, are scope and assumptions correct, is anything security-relevant missing? In spec-driven workflows, make this review the gate of the specify phase and keep the reviewed specification under version control.

Measure — recommendation; its sentences: R-0381

<!-- q L3745-3748 "It is the first rung" .. "(Isolation)." -->
> It is the first rung of the human-oversight ladder that continues with _Human review of AI generated plans_, _Human review of AI generated code_ and _Human approval for irreversible AI agent actions_ (Isolation).

R-0727 — scope (description)

<!-- q L3766-3766 -->
> - Show a recent specification an AI assistant worked from and its documented human review before implementation started.

R-0382 — assessment

<!-- q L3767-3767 -->
> - Show that the review checked the security acceptance criteria (e.g. review comments or a checklist).

R-0383 — assessment

<!-- q L3768-3768 -->
> - In spec-driven workflows: show that the specify phase cannot be left without the review gate.

R-0061 — assessment

#### Self-verification of AI generated changes

`owasp-dsomm#63e82b31-4167-480d-a22b-baf8ef79af61` · level 2 · depends on Defined build process (level 1); Security unit tests for important components (level 2) · usefulness 5 · difficulty knowledge 3, time 2, resources 2 · testable yes

<!-- q L3844-3849 -->
> Require AI agents to verify their changes against the project's own checks before presenting them, and guard the loop against test manipulation: record which checks failed before the agent started so it can only claim genuinely new fixes, route every edit that touches test code into human review, and re-run the full suite in the pipeline independent of the agent's environment.

Measure — recommendation; its sentences: R-0063

<!-- q L3854-3854 -->
> - Show the agent workflow or configuration that runs the project's own checks (tests, type checker, linter, build) before changes are presented.

R-0385 — assessment

<!-- q L3855-3855 -->
> - Show the guardrails against test manipulation: baseline comparison of test results, review flags on modified test code and an independent re-run of the suite in the pipeline.

R-0386 — assessment

<!-- q L3828-3832 "Instead" .. "attempt." -->
> Instead of presenting an untested edit, the agent executes the checks the project already defines for humans (test suite, type checker, linter, build) in its sandboxed environment and keeps refining the change until the checks succeed or a defined budget ends the attempt.

R-0384 — recommendation (description)

Descriptive, not normative: description R-0062.

#### Static and dynamic analysis of AI generated code

`owasp-dsomm#10362082-f48f-4218-be08-4ab78e589df0` · level 2 · depends on Static analysis for important server side components (level 3); Simple Scan (level 2) · usefulness 4 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L3934-3938 -->
> Apply the established static and dynamic security analysis to all AI-generated code and artifacts. Include AI-produced infrastructure code and scripts in the scan scope and surface findings inside the AI-assisted development loop, so agents can fix them before human review.

Measure — recommendation; its sentences: R-0064

<!-- q L3916-3918 "Static and dynamic security testing" .. "author-agnostic." -->
> Static and dynamic security testing (SAST, DAST, software composition analysis) is defined in the _Test and Verification_ dimension and is author-agnostic.

R-0728 — scope (description)

<!-- q L3918-3919 "This activity references" .. "duplicating them." -->
> This activity references those activities for AI-generated code instead of duplicating them.

R-0729 — scope (description)

<!-- q L3943-3943 -->
> - Show that the scan scope includes AI-produced artifacts such as generated infrastructure code and scripts.

R-0388 — assessment

<!-- q L3944-3944 -->
> - Show a recent AI-generated change where static analysis findings were surfaced and fixed inside the AI-assisted development loop.

R-0389 — assessment

<!-- q L3925-3926 -->
> Complementary: _No verification bypass for AI generated code_ ensures no delivery path skips these scans.

R-0387 — scope (description)

#### Validation of AI-suggested dependencies

`owasp-dsomm#df2db3f4-bae6-448e-844e-9562a4eabc39` · level 2 · depends on Software Composition Analysis (server side) (level 2) · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L4032-4035 -->
> Verify every AI-suggested dependency before adoption: check that the package exists, is the intended one (name, publisher, repository), is actively maintained and passes the established software composition analysis. Prefer dependencies already used in the organization.

Measure — recommendation

<!-- q L4039-4039 -->
> - Show the documented verification steps for adopting a new dependency and a recent example of an AI-suggested package that was checked (or rejected).

R-0394 — assessment

<!-- q L4040-4040 -->
> - Show that software composition analysis covers AI-suggested packages before merge.

R-0395 — assessment

<!-- q L4010-4010 -->
> Automate the checks so they do not depend on developer discipline:

R-0390 — recommendation (description)

<!-- q L4012-4014 "-" .. "pipeline." -->
> - **Enforce a minimum OpenSSF Scorecard score** for new dependencies, e.g. as a policy check in a pull-through proxy like an artifact registry or in the pull request pipeline.

R-0391 — recommendation (description)

<!-- q L4018-4020 "-" .. "counts)?" -->
> - **Verify identity and existence**: does the package match the intended project (publisher, source repository, age, download counts)?

R-0392 — recommendation (description)

<!-- q L4022-4025 -->
> - **Gate before merge**: run the established software composition analysis and the artifact repository policy on the change that adds the dependency, so a malicious or compromised version never enters the build.

R-0393 — recommendation (description)

Descriptive, not normative: implementation R-0065, R-0066.

#### Human review of AI generated code

`owasp-dsomm#d6bc0b7f-fd98-49fe-b66c-7c5fa70452c6` · level 3 · depends on Least privilege on external systems for AI agents (level 3) · usefulness 5 · difficulty knowledge 2, time 3, resources 1 · testable yes

<!-- q L4122-4124 -->
> Require human review for all AI-generated changes before merge. Reviewers are accountable for the change as if they had written it. AI agents must not be able to approve or merge their own pull requests.

Measure — recommendation; its sentences: R-0396, R-0069

<!-- q L4114-4116 "Neither replaces this activity" .. "before merge." -->
> Neither replaces this activity: agents deviate from approved plans, so the code remains the last artifact gate before merge.

R-0730 — scope (description)

<!-- q L4128-4128 -->
> - Show branch protection requiring human review before merge and that agent identities cannot approve or merge their own pull requests.

R-0070 — assessment

<!-- q L4129-4129 -->
> - Show recent reviews of AI-generated changes and who is accountable for them.

R-0397 — assessment

<!-- q L4107-4109 "It" .. "merged." -->
> It must be treated like code from an untrusted contributor: a human with knowledge of the codebase reviews it before it is merged.

R-0067 — recommendation (description)

Descriptive, not normative: description R-0068.

#### No verification bypass for AI generated code

`owasp-dsomm#c548df0b-0964-4fad-9f98-28fcd7442011` · level 3 · depends on Defined build process (level 1); Static analysis for important server side components (level 3); Simple Scan (level 2) · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L4223-4225 -->
> Enforce that every AI-generated change goes through the same defined build and security testing pipeline as human-written code. Verify branch protection and pipeline gates cannot be bypassed by agent identities.

Measure — recommendation; its sentences: R-0072

<!-- q L4231-4231 -->
> - Show the branch protection and pipeline gates and that agent identities cannot bypass them (e.g. no direct-push or auto-merge exceptions).

R-0073 — assessment

<!-- q L4232-4232 -->
> - Show for a sample of recent AI-generated changes that each went through the full security testing pipeline.

R-0399 — assessment

<!-- q L4211-4213 "Automated" .. "author." -->
> Automated security testing of source code and running applications (SAST, DAST, SCA) is defined in the _Test and Verification_ dimension and applies to all code regardless of its author.

R-0398 — scope (description)

<!-- q L4213-4216 "This" .. "pipeline)." -->
> This activity does not duplicate those activities; it ensures AI-generated code cannot reach production on a path that skips them (e.g. agent-pushed commits, auto-merge bots, generated infrastructure code outside the pipeline).

R-0071 — scope (description)

#### Security test generation with AI

`owasp-dsomm#fea96e68-de10-4a62-9df0-4727f700a4a0` · level 3 · depends on Threat modeling rule (level 2); Human review of AI generated code (level 3) · usefulness 3 · difficulty knowledge 3, time 2, resources 1 · testable yes

<!-- q L4287-4290 -->
> Use AI assistants to generate security test cases from security acceptance criteria and threat models (e.g. negative tests, authorization matrices, injection payloads). Review generated tests like any other AI-generated code and run them in the delivery pipeline.

Measure — recommendation

<!-- q L4295-4295 -->
> - Show security test cases generated from acceptance criteria or threat models and their human review.

R-0400 — assessment

<!-- q L4296-4296 -->
> - Show the generated tests running in the delivery pipeline.

R-0401 — assessment

Descriptive, not normative: description R-0074.

#### Continuous detection of compromised AI components

`owasp-dsomm#db390bba-3a49-4b1f-9982-c7d79fe88ea1` · level 4 · depends on Evaluation of the trust of used AI components (level 3); Test for compromised components (level 3) · usefulness 4 · difficulty knowledge 3, time 2, resources 2 · testable yes

<!-- q L4349-4354 -->
> Continuously check the inventory of approved AI components against compromise intelligence: match components and versions against behavioral classification registries and compromise advisories, alert on deviations between declared and observed behavior and quarantine affected components analogous to _Test for compromised components_.

Measure — recommendation

<!-- q L4359-4359 -->
> - Show how the inventory of approved AI components is matched against compromise intelligence (e.g. a behavioral classification registry) and how often.

R-0402 — assessment

<!-- q L4360-4360 -->
> - Show the alerting and quarantine process and what happened on the last hit or test.

R-0403 — assessment

Descriptive, not normative: description R-0075, R-0076.

#### Drift detection for agent instructions and guardrails

`owasp-dsomm#30e29dfc-2bb8-4fe1-bc7e-b3a9ade1ee9e` · level 5 · depends on Protection of agent memory against poisoning (level 5); Drift detection for deployed configuration (level 3) · usefulness 4 · difficulty knowledge 3, time 2, resources 2 · testable yes

<!-- q L4449-4456 -->
> Compare the deployed state of agent instructions (system prompts, rule files) and guardrail configurations against the last approved repository version on a schedule (at every deployment and at least daily) using hashes of normalized content. Alert on every deviation, treat drift of instructions or guardrails as a security incident with high priority, and either restore the approved version or formally re-approve the change. Document known runtime transformations as normalization exceptions to keep the false-positive rate low.

Measure — recommendation

<!-- q L4429-4431 "_Protection of agent memory against poisoning_ puts" .. "version control and review." -->
> _Protection of agent memory against poisoning_ puts system prompts, rule files and guardrail configurations under version control and review.

R-0731 — scope (description)

<!-- q L4437-4439 "The generic detection of configuration drift" .. "(Build and Deployment)." -->
> The generic detection of configuration drift in production is defined in _Drift detection for deployed configuration_ (Build and Deployment).

R-0732 — scope (description)

<!-- q L4439-4440 "This activity extends it" .. "agent behavior." -->
> This activity extends it to the content assets that determine agent behavior.

R-0733 — scope (description)

<!-- q L4461-4461 -->
> - Show the drift detection mechanism (hash comparison of normalized content), its schedule and the covered assets (system prompts, rule files, guardrail configurations).

R-0404 — assessment

<!-- q L4462-4462 -->
> - Demonstrate that an out-of-band change to a deployed system prompt or guardrail raises an alert within the scan cycle.

R-0405 — assessment

<!-- q L4463-4463 -->
> - Show how the last drift alert was handled (restore or formal re-approval) and the documented normalization exceptions.

R-0406 — assessment

Descriptive, not normative: description R-0077.

## Build and Deployment

### Build and Deployment / Build

6 activities, levels 1: 1, 2: 3, 3: 1, 5: 1.

#### Defined build process

`owasp-dsomm#f6f7737f-25a9-4317-8de2-09bf59f29b5b` · level 1 · usefulness 4 · difficulty knowledge 2, time 3, resources 2 · testable yes

<!-- q L4547-4548 -->
> Find a tool that suits your environment. Add your manual build steps, include steps for running tests, scanning and preparation for deployment.

Measure — recommendation

<!-- q L4550-4550 -->
> - Show your build pipeline configuration (e.g., Jenkinsfile, GitHub Actions workflow) and an exemplary job (build + test + security scan).

R-0414 — assessment

<!-- q L4533-4533 -->
> - Managing (third party) dependencies

R-0407 — scope (description)

<!-- q L4534-4534 -->
> - Environment configuration

R-0408 — scope (description)

<!-- q L4535-4535 -->
> - Running unit and integration tests

R-0409 — scope (description)

<!-- q L4536-4536 -->
> - Security scanning and compliance checks

R-0410 — scope (description)

<!-- q L4537-4537 -->
> - Artifact creation and storage

R-0411 — scope (description)

<!-- q L4538-4538 -->
> - Deployment preparation

R-0412 — scope (description)

<!-- q L4542-4542 "Use" .. "process." -->
> Use tools such as Jenkins, GitHub Actions, GitLab CI, or Maven to codify the process.

R-0413 — recommendation (description)

<!-- q L4544-4544 -->
> A simplified, but still a *defined build process*, may be a checklist of the steps to be performed.

R-0080 — permission (description)

Descriptive, not normative: description R-0078, R-0079.

#### Building and testing of artifacts in virtualized environments

`owasp-dsomm#a340f46b-6360-4cb8-847b-a0d3483d09d3` · level 2 · depends on Usage of containers (level 2) · usefulness 2 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L4604-4605 -->
> Each step during within the build and testing phase is performed in a separate virtual environments, which is destroyed afterward.

Measure — recommendation

<!-- q L4598-4599 "After" .. "builds." -->
> After the build, the filesystem should not be used again in other builds.

R-0081 — recommendation (description)

#### Pinning of artifacts

`owasp-dsomm#f3c4971e-9f4d-4e59-8ed0-f0bdb6262477` · level 2 · depends on Defined build process (level 1) · usefulness 3 · difficulty knowledge 2, time 2, resources 2 · testable partial

<!-- q L4647-4647 -->
> Pinning of artifacts ensure that changes are performed only when intended.

Measure — recommendation (promotes C-0226)

<!-- q L4641-4642 "Instead of using the latest tag" .. "version or digest." -->
> Instead of using the latest tag for your base image, select a specific version or digest.

R-0734 — recommendation (description)

<!-- q L4642 "For example, replace" .. "abcdef12." -->
> For example, replace FROM node:latest, to FROM node@sha256:abcdef12.

R-0735 — recommendation (description)

<!-- q L4648-4648 "The" .. "patching." -->
> The usage of pinning requires a good processes for patching.

R-0415 — scope (comment)

Descriptive, not normative: risk R-0082; implementation R-0083.

#### SBOM of components

`owasp-dsomm#2858ac12-0179-40d9-9acf-1b839c030473` · level 2 · depends on Defined build process (level 1) · usefulness 3 · difficulty knowledge 2, time 2, resources 3 · testable yes

<!-- q L4699-4700 -->
> Creation of an SBOM of components (e.g. application and container image content) during build.

Measure — recommendation

Descriptive, not normative: description R-0084.

#### Signing of code

`owasp-dsomm#9f107927-61e9-4574-85ad-3f2b4bca8665` · level 3 · depends on Defined build process (level 1) · usefulness 3 · difficulty knowledge 2, time 2, resources 2 · testable partial

<!-- q L4741-4742 -->
> Digitally signing commits helps to prevent unauthorized manipulation of source code.

Measure — recommendation

#### Signing of artifacts

`owasp-dsomm#5786959d-0c6f-46a6-8e1c-a32ff1a50222` · level 5 · depends on Defined build process (level 1); Pinning of artifacts (level 2) · usefulness 4 · difficulty knowledge 2, time 2, resources 2 · testable partial

<!-- q L4780-4781 -->
> Digitally signing artifacts for all steps during the build and especially docker images, helps to ensure their integrity and authenticity.

Measure — recommendation (promotes C-0230)

<!-- q L4783-4793 "It's" .. "repository." -->
> It's important to note that GitHub does not verify if the authenticated user's email address matches the one in the commit.\nTo clearly identify the author of a commit for reviewers, commit signing is recommended.\n\nGitHub actions such as [semantic-release-action](https://github.com/cycjimmy/semantic-release-action) do not automatically sign commits and may encounter issues as a result. \n\nTo address this, you can refer to a working configuration example in the [workflow folder](https://github.com/devsecopsmaturitymodel/DevSecOps-MaturityModel/blob/master/.github/workflows/main.yml) of DSOMM, which demonstrates how to use semantic release action in conjunction with [planetscale/ghcommit-action](https://github.com/planetscale/ghcommit-action).\nFor added security, consider using [Fine-grained personal access tokens](https://github.blog/2022-10-18-introducing-fine-grained-personal-access-tokens-for-github/) provided by your organization for a specific repository.

R-0086 — recommendation (description); its parts: R-0416 none recommendation, R-0417 may descriptive, R-0418 can descriptive, R-0419 none recommendation

<!-- q L4793-4794 "Store" .. "project." -->
> Store the Personal Access Token (PAT) as a secret in your project.

R-0420 — recommendation (description)

Descriptive, not normative: description R-0085.

### Build and Deployment / Deployment

15 activities, levels 1: 3, 2: 4, 3: 4, 4: 3, 5: 1.

#### Automated deployment process

`owasp-dsomm#67e1a9aa-9fbf-4ec5-a2de-400f01960c51` · level 1 · depends on Defined build process (level 1); Defined deployment process (level 1) · usefulness 4 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L4832-4833 -->
> Automating the deployment process enforces predefined criteria for security, compliance, and performance, ensuring reliable artifact delivery.

Measure — recommendation

<!-- q L4835-4835 -->
> - Deployment process is documented and available to relevant staff

R-0421 — assessment

<!-- q L4836-4836 -->
> - All deployment steps are automated

R-0422 — assessment

<!-- q L4837-4837 -->
> - Provide audit logs or evidence of deployments

R-0423 — assessment

#### Defined deployment process

`owasp-dsomm#74938a3f-1269-49b9-9d0f-c43a79a1985a` · level 1 · depends on Defined build process (level 1); Version control (level 1) · usefulness 1 · difficulty knowledge 1, time 1, resources 1 · testable yes

<!-- q L4881-4882 -->
> Establish a written deployment process documented in README files, wikis, or implemented as executable scripts and automated steps.

Measure — recommendation

<!-- q L4884-4884 -->
> - Deployment process is documented and available to relevant staff

R-0424 — assessment

<!-- q L4885-4885 -->
> - Logs of deployments are documented and availabe to relevant staff

R-0425 — assessment

#### Inventory of production components

`owasp-dsomm#2a44b708-734f-4463-b0cb-86dc46344b2f` · level 1 · depends on Automated deployment process (level 1) · usefulness 4 · difficulty knowledge 1, time 1, resources 1 · testable yes

<!-- q L4916-4917 -->
> A documented inventory of components in production exists (gathered manually or automatically). For example a manually created document with applications in production. In a kubernetes cluster, namespaces can be automatically gathered and documented, e.g. in a JSON in a S3 bucket/git repository, dependency track.

Measure — recommendation; its sentences: R-0087 permission

<!-- q L4919-4919 -->
> - Inventory of all production applications with application name, owner, and date of last review

R-0426 — assessment

<!-- q L4920-4920 -->
> - Inventory is accessible to development, security and operations teams

R-0427 — assessment

Descriptive, not normative: implementation R-0088.

#### Defined decommissioning process

`owasp-dsomm#da4ff665-dcb9-4e93-9d20-48cdedc50fc2` · level 2 · usefulness 2 · difficulty knowledge 1, time 2, resources 1 · testable partial

<!-- q L4983-4985 -->
> A clear decommissioning process ensures the removal of unused applications from the `Inventory of production components` and if implemented from `Inventory of production artifacts`.

Measure — recommendation (promotes C-0238)

<!-- q L4978-4979 "This" .. "applications." -->
> This process must be carefully executed to avoid impacting other services and applications.

R-0089 — recommendation (description)

Descriptive, not normative: risk R-0090, R-0091.

#### Environment depending configuration parameters (secrets)

`owasp-dsomm#df428c9d-efa0-4226-9f47-a15bb53f822b` · level 2 · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L5008-5010 -->
> Set configuration parameters via environment variables stored using specific platform functionalities or secrets management systems (e.g. Kubernetes secrets or Hashicorp Vault).

Measure — recommendation

#### Evaluation of the trust of used components

`owasp-dsomm#0de465a6-55a7-4343-af79-948bb5ff10ba` · level 2 · usefulness 3 · difficulty knowledge 3, time 3, resources 1 · testable yes

<!-- q L5049-5053 -->
> Each components source is evaluated to be trusted. For example the source, number of developers included, email configuration used by maintainers to prevent maintainer account theft, typo-squatting, ... Create image assessment criteria, perform an evaluation of images and create a whitelist of artifacts/container images/virtual machine images.

Measure — recommendation

Descriptive, not normative: risk R-0092; implementation R-0093, R-0094.

#### Inventory of production artifacts

`owasp-dsomm#83057028-0b77-4d2e-8135-40969768ae88` · level 2 · depends on Automated deployment process (level 1); Inventory of production components (level 1) · usefulness 3 · difficulty knowledge 2, time 2, resources 3 · testable yes

<!-- q L5098-5099 -->
> A documented inventory of artifacts in production like container images exists (gathered manually or automatically).

Measure — recommendation

Descriptive, not normative: implementation R-0095.

#### Drift detection for deployed configuration

`owasp-dsomm#9cba815f-02d2-4b06-a11f-7f28580e135a` · level 3 · depends on Automated deployment process (level 1) · usefulness 4 · difficulty knowledge 3, time 2, resources 2 · testable yes

<!-- q L5169-5175 -->
> Continuously compare the deployed state of infrastructure and configuration against the versioned desired state (e.g. via GitOps controllers that reconcile and report drift, or scheduled infrastructure-as-code plan runs). Alert on every deviation and either revert it automatically to the approved state or bring the change through the regular review process. Document intentional exceptions so the alerts stay actionable.

Measure — recommendation

<!-- q L5179-5179 -->
> - Show the drift detection mechanism (e.g. GitOps reconciliation status or scheduled plan diffs) and the covered environments.

R-0428 — assessment

<!-- q L5180-5180 -->
> - Demonstrate that an out-of-band change to production configuration raises an alert or is reverted automatically.

R-0429 — assessment

<!-- q L5181-5181 -->
> - Show how the last drift finding was handled (automatic revert or formal re-approval) and the documented exceptions.

R-0430 — assessment

Descriptive, not normative: description R-0096.

#### Handover of confidential parameters

`owasp-dsomm#94a96f79-8bd6-4904-97c0-994ff88f176a` · level 3 · depends on Environment depending configuration parameters (secrets) (level 2) · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable partial

<!-- q L5233-5235 -->
> Encryption ensures confidentiality of credentials e.g. from unauthorized access on the file system. Also, the usage of a credential management system can help protect credentials.

Measure — recommendation; its sentences: R-0431, R-0098 permission

Descriptive, not normative: risk R-0097.

#### Inventory of production dependencies

`owasp-dsomm#13e9757e-58e2-4277-bc0f-eadc674891e6` · level 3 · depends on Inventory of production artifacts (level 2); SBOM of components (level 2) · usefulness 3 · difficulty knowledge 2, time 2, resources 3 · testable yes

<!-- q L5271-5272 -->
> A documented inventory of dependencies used in artifacts like container images and containers exists.

Measure — recommendation

Descriptive, not normative: implementation R-0099.

#### Rolling update on deployment

`owasp-dsomm#85d52588-f542-4225-a338-20dc22a5508d` · level 3 · depends on Automated deployment process (level 1) · usefulness 2 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L5334-5334 -->
> A deployment without downtime is performed*.

Measure — recommendation

Descriptive, not normative: risk R-0100.

#### Canary deployment

`owasp-dsomm#c4204a32-2545-4424-b524-d1cc52b46abd` · level 4 · depends on Automated deployment process (level 1) · usefulness 3 · difficulty knowledge 3, time 2, resources 2 · testable yes

<!-- q L5394-5400 -->
> Adopt a canary deployment strategy in which a small percentage of production traffic (commonly 1-10%) is routed to the new artifact version for a defined observation window. Promotion to higher traffic percentages is gated on automated SLI checks (error rate, latency, saturation) and security checks (DAST, runtime anomaly detection). Rollback must be automated and triggered by gate failure without human intervention.

Measure — recommendation; its sentences: R-0432, R-0103

<!-- q L5402-5403 -->
> - Canary stage exists in the deployment pipeline with a configured initial traffic percentage and observation window.

R-0433 — assessment

<!-- q L5404-5405 -->
> - Automated promotion and rollback gates are defined based on SLIs and security signals.

R-0434 — assessment

<!-- q L5406-5407 -->
> - Audit logs of canary deployments and their promotion or rollback decisions are retained.

R-0435 — assessment

Descriptive, not normative: risk R-0101, R-0102.

#### Same artifact for environments

`owasp-dsomm#a854b48d-83bd-4f8d-8621-a0bdd470837f` · level 4 · depends on Defined build process (level 1) · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L5445-5446 -->
> Building an artifact once and deploying it to different environments means that only tested artifacts are allowed to reach the production environment

Measure — recommendation (promotes C-0252)

#### Usage of feature toggles

`owasp-dsomm#a511799b-045e-4b96-9843-7d63d8c1e2ad` · level 4 · depends on Same artifact for environments (level 4) · usefulness 2 · difficulty knowledge 2, time 1, resources 1 · testable partial

<!-- q L5481-5483 -->
> Usage of environment independent configuration parameter, called static feature toggles, mitigates the risk of accidentally enabling insecure features in production.

Measure — recommendation

Descriptive, not normative: risk R-0104.

#### Blue/Green Deployment

`owasp-dsomm#0cb2626b-fb0d-4a0f-9688-57f787310d97` · level 5 · depends on Smoke Test (level 4) · usefulness 2 · difficulty knowledge 1, time 2, resources 1 · testable partial

<!-- q L5528-5529 -->
> Using a blue/green deployment strategy increases application availability and reduces deployment risk by simplifying the rollback process if a deployment fails.

Measure — recommendation

Descriptive, not normative: risk R-0105.

### Build and Deployment / Patch Management

8 activities, levels 1: 2, 2: 4, 3: 1, 4: 1.

#### A patch policy is defined

`owasp-dsomm#99415139-6b50-441b-89e1-0aa59accd43d` · level 1 · usefulness 4 · difficulty knowledge 3, time 1, resources 2 · testable yes

<!-- q L5572-5573 -->
> Define a patch policy for all artifacts (e.g. in images) is defined. How often is an image rebuilt?

Measure — recommendation; its sentences: R-0437

<!-- q L5575-5575 -->
> - Patch policy is documented and accessible to relevant staff.

R-0438 — assessment

<!-- q L5576-5576 -->
> - The policy defines patch frequency and responsible roles.

R-0439 — assessment

<!-- q L5577-5577 -->
> - Patch actions and exceptions are logged and reviewed.

R-0440 — assessment

<!-- q L5578-5578 -->
> - Evidence of regular patching and policy review is available.

R-0441 — assessment

<!-- q L5569-5569 "The" .. "patching." -->
> The policy should specify the frequency, responsibilities, and documentation requirements for patching.

R-0106 — recommendation (description)

<!-- q L5569-5569 "A" .. "updated." -->
> A patch policy defines how and when software components, images, and dependencies are updated.

R-0436 — scope (description)

Descriptive, not normative: risk R-0107.

#### Automated PRs for patches

`owasp-dsomm#8ae0b92c-10e0-4602-ba22-7524d6aed488` · level 1 · usefulness 4 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L5609-5613 -->
> Fast patching of third-party components is needed. The DevOps way is to have an automated pull request for new components. This includes: * Applications * Virtualized operating system components (e.g., container images) * Operating systems * Infrastructure as Code/GitOps (e.g., ArgoCD based on a git repository or Terraform)

Measure — recommendation; its sentences: R-0442, R-0443, R-0444, R-0445

<!-- q L5615-5615 -->
> - Automated PR tooling is enabled for all relevant repositories.

R-0446 — assessment

<!-- q L5616-5616 -->
> - PRs are created automatically for outdated or vulnerable dependencies.

R-0447 — assessment

<!-- q L5617-5617 -->
> - PRs are reviewed and merged according to the defined patch policy.

R-0448 — assessment

<!-- q L5618-5618 -->
> - Evidence of automated PRs and patching activity is available.

R-0449 — assessment

Descriptive, not normative: description R-0108.

#### Automated merge of automated PRs

`owasp-dsomm#f2594f8f-1cd6-45f9-af29-eaf3315698eb` · level 2 · depends on Automated PRs for patches (level 1) · usefulness 3 · difficulty knowledge 2, time 1, resources 1 · testable yes

<!-- q L5670-5672 -->
> A good practice is to merge trusted dependencies (e.g. spring boot) after a grace period like one week. Often, patches, fixes and minor updates are automatically merged. Be aware that automated merging requires a high automated test coverage. Enforcement of merging of pull requests after a grace period.

Measure — recommendation; its sentences: R-0450 scope

#### Nightly build of images (base images)

`owasp-dsomm#34869eaf-f2e1-4926-b0bd-28c43402f057` · level 2 · usefulness 3 · difficulty knowledge 3, time 2, resources 2 · testable yes

<!-- q L5717-5719 -->
> Custom base images are getting build at least nightly. In case the packages in the base image e.g. <i>centos</i> has changed, the build server triggers the build of depending images.

Measure — recommendation

#### Reduction of the attack surface

`owasp-dsomm#16e39c8f-5336-4001-88ed-a552d2447531` · level 2 · usefulness 3 · difficulty knowledge 3, time 3, resources 2 · testable partial

<!-- q L5749-5750 -->
> Removal of unneeded components, dependencies, files or file access rights. For container images the usage of distroless images is recommended.

Measure — recommendation; its sentences: R-0451

Descriptive, not normative: description R-0109.

#### Usage of a maximum lifetime for images

`owasp-dsomm#485a3383-7f2e-4dba-bb84-479377070904` · level 2 · usefulness 3 · difficulty knowledge 3, time 4, resources 2 · testable yes

<!-- q L5800-5803 -->
> A short maximum lifetime for images is defined, e.g. 30 days. The project images, based on the nightly builded images, are deployed at leased once within the defined lifetime. Third Party images are deployed at leased once within the defined lifetime.

Measure — recommendation

<!-- q L5792-5795 "As" .. "images." -->
> As a best practice, it is essential to define a reasonable maximum lifetime for containers to ensure that you consistently deploy the most recent, patched, and secure versions of both your custom base images and third-party images.

R-0452 — recommendation (description)

Descriptive, not normative: description R-0110.

#### Automated deployment of automated PRs

`owasp-dsomm#08f27c26-2c6a-47fe-9458-5e88f188085d` · level 3 · depends on Automated merge of automated PRs (level 2) · usefulness 3 · difficulty knowledge 3, time 3, resources 1 · testable partial

<!-- q L5829-5829 -->
> After merging of an automated dependency PR, automated deployment is needed,

Measure — recommendation

#### Usage of a short maximum lifetime for images

`owasp-dsomm#6b96e5a0-ce34-4ea4-a88f-469d3b84546e` · level 4 · usefulness 3 · difficulty knowledge 3, time 4, resources 2 · testable yes

<!-- q L5875-5875 -->
> A good practice is to perform the build and deployment daily or even just-in-time, when a new component (e.g. package) for the image is available.

Measure — recommendation

<!-- q L5868-5871 "As" .. "images." -->
> As a best practice, it is essential to define a reasonable maximum lifetime for containers to ensure that you consistently deploy the most recent, patched, and secure versions of both your custom base images and third-party images.

R-0453 — recommendation (description)

Descriptive, not normative: description R-0111.

## Culture and Organization

### Culture and Organization / Design

7 activities, levels 1: 1, 2: 1, 3: 3, 4: 1, 5: 1.

#### Conduction of simple threat modeling on technical level

`owasp-dsomm#47419324-e263-415b-815d-e7161b6b905e` · level 1 · usefulness 3 · difficulty knowledge 2, time 3, resources 1 · testable yes

<!-- q L5963-5963 -->
> Perform threat modeling of technical features during product sprint planning using simple checklists and diagrams. Document identified threats and mitigations for new or changed functionality.

Measure — recommendation

<!-- q L5959 "The team exercise" .. "of this activity." -->
> The team exercise and the shared understanding remain the core of this activity.

R-0736 — scope (description)

<!-- q L5965-5965 -->
> - Evidence of threat modeling activities exists for high-risk applications, including annotated diagrams and documented threats/mitigations.

R-0458 — assessment

<!-- q L5966-5966 "-" .. "stakeholders." -->
> - Activities are performed during sprint planning and involve relevant stakeholders.

R-0459 — assessment

<!-- q L5966-5966 "Outcomes" .. "review." -->
> Outcomes are recorded and accessible for review.

R-0460 — assessment

<!-- q L5919-5919 "Always" .. "use." -->
> Always make sure to persist the outcome of a threat modeling discussion for later use.

R-0454 — recommendation (description)

<!-- q L5919-5919 "Avoid" .. "threats." -->
> Avoid lengthy workshops and overly detailed lists of low-relevant threats.

R-0455 — recommendation (description)

<!-- q L5919-5919 "If" .. "scope." -->
> If you add new functionality to an existing application, look only into the newly added functions instead of trying to cover the entire scope.

R-0456 — scope (description)

<!-- q L5919-5919 "Perform" .. "paradigms." -->
> Perform threat modeling iteratively to align to more iterative development paradigms.

R-0457 — recommendation (description)

<!-- q L5933-5933 ">" .. "remediations." -->
> > Note: _A threat model can be as simple as a data flow diagram with attack vectors on every flow and asset and equivalent remediations.

R-0114 — permission (description)

Descriptive, not normative: description R-0112, R-0113, R-0115, R-0116, R-0117, R-0118, R-0119.

#### Information security targets are communicated

`owasp-dsomm#1b9281b9-48e2-4c01-9ac6-9db9931c4885` · level 2 · usefulness 3 · difficulty knowledge 1, time 1, resources 1 · testable partial

<!-- q L6083-6084 -->
> Transparent and timely communication of the security targets by senior management is essential to ensure teams' buy-in and support.

Measure — recommendation (promotes C-0289)

Descriptive, not normative: risk R-0120.

#### Conduction of simple threat modeling on business level

`owasp-dsomm#48f97f31-931c-46eb-9b3e-e2fec0cd0426` · level 3 · usefulness 3 · difficulty knowledge 2, time 3, resources 1 · testable yes

<!-- q L6110-6111 -->
> Threat modeling of business functionality is performed during the product backlog creation to facilitate early detection of security defects.

Measure — recommendation

#### Creation of simple abuse stories

`owasp-dsomm#bacf85b6-5bc0-405d-b5ba-a5d971467cc1` · level 3 · depends on Conduction of simple threat modeling on technical level (level 1); Creation of threat modeling processes and standards (level 3) · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L6153-6153 -->
> Abuse stories are created during the creation of user stories.

Measure — recommendation

<!-- q L6143-6145 "Large language models are well suited" .. "abuse stories." -->
> Large language models are well suited as a complementary tool for this activity: given a user story and its acceptance criteria, they generate candidate abuse stories.

R-0737 — permission (description)

Descriptive, not normative: description R-0121, R-0122.

#### Creation of threat modeling processes and standards

`owasp-dsomm#dd5ed7c1-bdbf-400f-b75f-6d3953a1a04e` · level 3 · depends on Conduction of simple threat modeling on technical level (level 1) · usefulness 3 · difficulty knowledge 4, time 3, resources 2 · testable partial

<!-- q L6195-6197 -->
> Creation of threat modeling processes and standards through the organization helps to enhance the security culture and provide more structure to the threat model exercises.

Measure — recommendation

#### Conduction of advanced threat modeling

`owasp-dsomm#ae22dafd-bcd6-41ee-ba01-8b7fe6fc1ad9` · level 4 · depends on Conduction of simple threat modeling on technical level (level 1); Creation of threat modeling processes and standards (level 3) · usefulness 3 · difficulty knowledge 4, time 3, resources 2 · testable yes

<!-- q L6259-6260 -->
> Threat modeling is performed by using reviewing user stories and producing security driven data flow diagrams.

Measure — recommendation

<!-- q L6284-6284 "The" .. "level_." -->
> The generated models require expert review, see the note on failure modes in _Conduction of simple threat modeling on technical level_.

R-0461 — recommendation (description)

Descriptive, not normative: description R-0123.

#### Creation of advanced abuse stories

`owasp-dsomm#0a929c3e-ab9a-4206-8761-adf84b74622e` · level 5 · depends on Creation of simple abuse stories (level 3) · usefulness 4 · difficulty knowledge 4, time 2, resources 1 · testable partial

<!-- q L6399-6399 -->
> Advanced abuse stories are created as part of threat modeling activities.

Measure — recommendation

### Culture and Organization / Education and Guidance

17 activities, levels 1: 2, 2: 5, 3: 5, 4: 4, 5: 1.

#### Ad-Hoc Security trainings for software developers

`owasp-dsomm#12c90cc6-3d58-4d9b-82ff-d469d2a0c298` · level 1 · usefulness 3 · difficulty knowledge 2, time 1, resources 1 · testable yes

<!-- q L6446-6446 -->
> Provide security awareness training for all personnel involved in software development on an ad-hoc basis, ensuring that relevant topics are covered when new risks or needs are identified.

Measure — recommendation (promotes C-0313)

<!-- q L6448-6448 -->
> - Conduct security training for developers and relevant personnel

R-0462 — assessment

<!-- q L6449-6449 -->
> - Training materials are available

R-0463 — assessment

<!-- q L6450-6450 -->
> - Attendance records are available

R-0464 — assessment

Descriptive, not normative: risk R-0124.

#### Security consulting on request

`owasp-dsomm#0b28367b-75a0-4bae-a926-3725c1bf9bb0` · level 1 · usefulness 3 · difficulty knowledge 3, time 1, resources 1 · testable yes

<!-- q L6490-6490 -->
> Make security consulting available to teams on request, ensuring that expert advice is accessible when needed to address security concerns during development.

Measure — recommendation

<!-- q L6492-6492 -->
> - Show evidence that an it security expert is available for questions at least quarterly.

R-0465 — assessment

<!-- q L6493-6493 -->
> - Documentation of consultations and resulting actions is available for review.

R-0466 — assessment

<!-- q L6486-6486 "This" .. "development." -->
> This support can be provided by internal or external security consultants and helps address specific concerns during software development.

R-0125 — permission (description)

Descriptive, not normative: risk R-0126.

#### Each team has a security champion

`owasp-dsomm#6217fe11-5ed7-4cf4-9de4-555bcfa6fe87` · level 2 · usefulness 4 · difficulty knowledge 3, time 2, resources 1 · testable yes

<!-- q L6529-6530 -->
> Each team defines an individual to be responsible for security. These individuals are often referred to as 'security champions'

Measure — recommendation; its sentences: R-0467

<!-- q L6538-6538 "Depending" .. "manager." -->
> Depending on the size and structure of the team the "Security Champion" may be a software developer, tester, or a product manager.

R-0127 — permission (description)

<!-- q L6538-6538 "You" .. "reasons." -->
> You may need to customize the way you create and support "Security Champions" for cultural reasons.

R-0128 — permission (description)

<!-- q L6538-6538 "Implement" .. "developers." -->
> Implement a program where each software development team has a member considered a "Security Champion" who is the liaison between Information Security and developers.

R-0468 — recommendation (description)

#### Regular security training for all

`owasp-dsomm#9768f154-357a-4c06-af6f-d66570677c9b` · level 2 · usefulness 4 · difficulty knowledge 3, time 4, resources 2 · testable yes

<!-- q L6569-6570 -->
> Provide security awareness training for all internal personnel involved in software development on a regular basis like twice in a year for 1-3 days.

Measure — recommendation

<!-- q L6578-6578 "Ideally," .. "option." -->
> Ideally, deliver training in person so participants can have discussions as a team, but Computer-Based Training (CBT) is also an option.

R-0129 — permission (description)

<!-- q L6578-6578 "Develop" .. "externally." -->
> Develop training internally or procure it externally.

R-0469 — permission (description)

<!-- q L6578 "Conduct security awareness training" .. "of the software." -->
> Conduct security awareness training for all roles currently involved in the management, development, testing, or auditing of the software.

R-0738 — recommendation (description)

<!-- q L6580-6580 "Course" .. "audience." -->
> Course content should include a range of topics relevant to application security and privacy, while remaining accessible to a non-technical audience.

R-0130 — recommendation (description)

<!-- q L6580-6580 "Additionally," .. "security." -->
> Additionally, the training should include references to any organization-wide standards, policies, and procedures defined to improve application security.

R-0131 — recommendation (description)

<!-- q L6580-6580 "The" .. "level." -->
> The OWASP Top 10 vulnerabilities should be covered at a high level.

R-0132 — recommendation (description)

<!-- q L6582-6582 "Consider" .. "desensitization." -->
> Consider incorporating innovative ways of delivery (such as gamification) to maximize its effectiveness and combat desensitization.

R-0470 — recommendation (description)

<!-- q L6582 "Training is mandatory" .. "demonstrate compliance." -->
> Training is mandatory for all employees and contractors involved with software development and includes an auditable sign-off to demonstrate compliance.

R-0739 — recommendation (description)

#### Regular security training of security champions

`owasp-dsomm#f88d1b17-3d7d-4c3d-8139-ad44fc4942d4` · level 2 · depends on Each team has a security champion (level 2) · usefulness 5 · difficulty knowledge 4, time 2, resources 2 · testable partial

<!-- q L6614-6614 -->
> Regular security training of security champions.

Measure — recommendation

Assessment (L6616-6617): placeholder lines only, not reproduced (one carries the placeholder token, the other a misspelling of it).

#### Reward of good communication

`owasp-dsomm#91b6f75b-9f4a-4d77-95a2-af7ad3222c7c` · level 2 · usefulness 3 · difficulty knowledge 3, time 2, resources 1 · testable partial

<!-- q L6651-6653 -->
> Good communication and transparency encourages cross-organizational support. Gamification of security is also known to help, examples include T-Shirts, mugs, cups, gift cards and 'High-Fives'.

Measure — recommendation

Descriptive, not normative: implementation R-0133.

#### Security code review

`owasp-dsomm#7121b0c7-6ace-4d6b-95d0-94535dbccb57` · level 2 · usefulness 3 · difficulty knowledge 3, time 2, resources 1 · testable partial

<!-- q L6694-6701 -->
> The following areas of code tend to have a high-risk of containing security vulnerabilities: - Crypto implementations / usage - Parser, unparser - System configuration - Authentication, authorization - Session management - Request throttling - :unicorn: (self-developed code, only used in that one software)

Measure — recommendation; its sentences: R-0471, R-0472, R-0473, R-0474, R-0475, R-0476, R-0477

<!-- q L6707-6707 -->
> - Present the performed reviews (including participants, findings, consequences) and assess whether it is reasonable.

R-0478 — assessment

Descriptive, not normative: description R-0134.

#### Conduction of build-it, break-it, fix-it contests

`owasp-dsomm#bfdb576e-a416-4ec6-96fe-a078d58b2ff8` · level 3 · usefulness 3 · difficulty knowledge 5, time 3, resources 1 · testable partial

<!-- q L6740-6742 -->
> The build-it, break-it, fix-it contest allows to train people with security related roles like security champions the build, break and fix part of a secure application. This increases the learning of building secure components.

Measure — recommendation

#### Office Hours

`owasp-dsomm#185d5a74-19dc-4422-be07-44ea35226783` · level 3 · usefulness 3 · difficulty knowledge 1, time 1, resources 1 · testable yes

<!-- q L6770-6771 -->
> As a security team, be open for questions and hints during defined office hours. x x d

Measure — recommendation

#### Security Coaching

`owasp-dsomm#f7b215dc-73a4-4c61-9e49-b3a3af1c9ac3` · level 3 · usefulness 3 · difficulty knowledge 4, time 3, resources 1 · testable partial

<!-- q L6794-6796 -->
> By coaching teams on security topics using for example the samman coaching method, teams internalize security practices as new habits in their development process.

Measure — recommendation

#### Security-Lessoned-Learned

`owasp-dsomm#58c46807-fee9-448b-b6dd-8050c464ab52` · level 3 · usefulness 3 · difficulty knowledge 3, time 3, resources 1 · testable partial

<!-- q L6828-6830 -->
> Running a 'lessons learned' session after an incident helps drive continuous improvement. Regular meetings with security champions are a good place to share and discuss lessons learned.

Measure — recommendation

#### Simple mob hacking

`owasp-dsomm#535f301a-e8e8-4eda-ad77-a08b035c92de` · level 3 · usefulness 3 · difficulty knowledge 5, time 3, resources 1 · testable yes

<!-- q L6855-6857 -->
> Participate with your whole team in a simple mob hacking session organized by the Security Champion Guild. In the session the guild presents a vulnerable application and together you look at possible exploits. Just like in mob programming there is one driver and several navigators.

Measure — recommendation

<!-- q L6860-6860 -->
> - All exploits happen via the user interface.

R-0479 — recommendation (description)

<!-- q L6861-6861 -->
> - No need for security/hacking tools.

R-0480 — permission (description)

<!-- q L6862-6862 -->
> - No need for deep technical or security knowledge.

R-0481 — permission (description)

<!-- q L6863-6863 -->
> - Use an insecure training app, e.g., [DVWA](https://dvwa.co.uk/) or [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/).

R-0482 — recommendation (description)

<!-- q L6864-6864 -->
> - Encourage active participation, e.g., use small groups.

R-0483 — recommendation (description)

<!-- q L6865-6865 -->
> - Allow enough time for everyone to run at least one exploit.

R-0484 — recommendation (description)

Descriptive, not normative: description R-0135, R-0136.

#### Aligning security in teams

`owasp-dsomm#f994a55d-71bb-45a4-a887-0a213d72c504` · level 4 · usefulness 5 · difficulty knowledge 4, time 4, resources 1 · testable partial

<!-- q L6908-6909 -->
> By aligning security Subject Matter Experts with project teams, a higher security standard can be achieved.

Measure — recommendation; its sentences: R-0138

<!-- q L6906-6907 "However," .. "security." -->
> However, everyone in the project team should be responsible for security.

R-0137 — recommendation (risk)

#### Conduction of collaborative team security checks

`owasp-dsomm#35446784-7610-40d9-af9e-d43f3173bf8c` · level 4 · usefulness 2 · difficulty knowledge 4, time 4, resources 2 · testable partial

<!-- q L6937-6938 -->
> Mutual security testing the security of other teams project enhances security awareness and knowledge.

Measure — recommendation

#### Conduction of war games

`owasp-dsomm#534f60bf-0995-4314-bb9c-f0f2bf204694` · level 4 · usefulness 3 · difficulty knowledge 4, time 5, resources 4 · testable yes

<!-- q L6964-6966 -->
> War Games like activities help train for incidents. Security SMEs create attack scenarios in a testing environment enabling the trainees to learn how to react in case of an incident.

Measure — recommendation

#### Regular security training for externals

`owasp-dsomm#31833d56-35af-4ef3-9300-f23d27646ce7` · level 4 · usefulness 4 · difficulty knowledge 3, time 2, resources 3 · testable partial

<!-- q L6996-6997 -->
> Provide security awareness training for all personnel including externals involved in software development on a regular basis.

Measure — recommendation

#### Conduction of collaborative security checks with developers and system administrators

`owasp-dsomm#95caef96-36ed-458c-a087-5c35d4f9dec2` · level 5 · usefulness 3 · difficulty knowledge 3, time 2, resources 1 · testable partial

<!-- q L7034-7036 -->
> Periodically security reviews of source code (SCA), in which security SME, developers and operations are involved, are effective at increasing the robustness of software and the security knowledge of the teams involved.

Measure — recommendation

### Culture and Organization / Process

4 activities, levels 1: 1, 2: 1, 3: 2.

#### Definition of simple BCDR practices for critical components

`owasp-dsomm#c72da779-86cc-45b1-a339-190ce5093171` · level 1 · usefulness 4 · difficulty knowledge 4, time 3, resources 2 · testable yes

<!-- q L7074-7074 -->
> Develop, document, and communicate a BCDR plan for all critical components. The plan must define roles and responsibilities, Service Level Agreements (SLAs), Recovery Point Objectives (RPOs), Recovery Time Objectives (RTOs), and failover procedures. Ensure all relevant personnel are trained and the plan is reviewed and updated regularly.

Measure — recommendation; its sentences: R-0139, R-0486

<!-- q L7075-7078 -->
> "- There is a documented BCDR plan covering all critical components of the application(s).\n- The plan clearly defines responsibilities, SLAs, RPOs, RTOs, and failover steps. \n- Relevant staff are aware of the plan, and evidence of regular review and testing is available.\n"

R-0487 — assessment

<!-- q L7072-7072 -->
> This applies to cyber attacks as well as natural emergencies, such as a power outage.

R-0485 — scope (risk)

#### Determining the protection requirement

`owasp-dsomm#72737130-472c-4984-80f8-9ab2f1c2ed5d` · level 2 · depends on Inventory of production components (level 1) · usefulness 3 · difficulty knowledge 2, time 2, resources 1 · testable partial

<!-- q L7102-7105 -->
> "Defining the protection requirement. \nThe protection requirements for an application should consider:\n- Processed data criticality\n- Application accessibility (internal vs. external)\n- Regulatory compliance\n- Other relevant factors"

Measure — recommendation; its sentences: R-0141

Descriptive, not normative: risk R-0140.

#### Approval by reviewing any new version

`owasp-dsomm#3f63bdbc-c75f-4780-a941-e6ad42e894e1` · level 3 · usefulness 3 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L7166-7168 -->
> On each new version (e.g. Pull Request) of source code or infrastructure components a security peer review of the changes is performed (two eyes principle) and approval given by the reviewer.

Measure — recommendation

#### Definition of a change management process

`owasp-dsomm#b4193d32-3948-47e2-a326-3748c48019a1` · level 3 · usefulness 3 · difficulty knowledge 4, time 3, resources 1 · testable partial

<!-- q L7195-7195 -->
> Each change of a system is automatically recorded and adequately logged.

Measure — recommendation

## Implementation

### Implementation / Application Hardening

9 activities, levels 1: 3, 2: 2, 3: 2, 4: 1, 5: 1.

#### App. Hardening Level 1 (50%)

`owasp-dsomm#b597928e-54d6-48a5-a806-8003dcd56aab` · level 1 · usefulness 3 · difficulty knowledge 2, time 2, resources 1 · testable partial

<!-- q L7224-7228 -->
> Following frameworks like the * OWASP Application Security Verification Standard Level 1 * OWASP Mobile Application Security Verification Standard in all applications provides a good baseline. Implement 50% of the recommendations.

Measure — recommendation; its sentences: R-0488, R-0489

Descriptive, not normative: description R-0142, R-0143, R-0144, R-0145.

#### Context-aware output encoding

`owasp-dsomm#e1f37abb-d848-4a3a-b3df-65e91a89dcb7` · level 1 · usefulness 3 · difficulty knowledge 1, time 2, resources 1 · testable yes

<!-- q L7300-7304 -->
> "* Use modern secure frameworks such as React/Angular/Vue/Svelte. The default method here renders data in a safe way.\n* Use established and well-maintained encoding libraries such as OWASP\u2019s Java Encoder and Microsoft\u2019s AntiXSS.\n* Implement content security policies (CSP) to restrict the types of content that can be loaded and executed.\n"

Measure — recommendation; its sentences: R-0148

<!-- q L7293-7293 "Apply" .. "both." -->
> Apply both.

R-0490 — recommendation (description)

<!-- q L7294-7297 "In" .. "*/</script>\n```\n" -->
> In the sample below the `{{bad_data}}` must be encoded differently, depending on its context, to render safe HTML.\n\n```html\n<div>{{bad_data}}</div>\n<a href=\"{{bad_data}}\">Click me</a>\n<script>var x = '{{bad_data}}';</script>\n<script>/** Comment {{bad_data}} */</script>\n```\n

R-0146 — recommendation (description)

Descriptive, not normative: risk R-0147.

#### Parametrization

`owasp-dsomm#00e91a8a-3972-4692-8679-674ab8547486` · level 1 · usefulness 3 · difficulty knowledge 1, time 2, resources 1 · testable yes

<!-- q L7363-7367 -->
> * Identify which of the types your application is using. Check that you use: * Use _parametrized queries_ (or _prepared statements_) * For database queries, you may also use: * Use _stored procedures_ () * Use ORM (Object-Relational Mapping) tools that automatically handle input sanitization

Measure — recommendation; its sentences: R-0493, R-0494, R-0495, R-0151 permission, R-0496 permission, R-0497 permission

<!-- q L7352-7352 -->
> This is called *SQL injection* but the principle applies to NoSql, and anywhere that your code is building commands that will be executed.

R-0491 — scope (description)

<!-- q L7358-7358 "The same" .. "execution, etc." -->
> The same principle applies to other types, such as command line execution, etc.

R-0492 — scope (description)

Descriptive, not normative: description R-0149; risk R-0150.

#### App. Hardening Level 1

`owasp-dsomm#cf819225-30cb-4702-8e32-60225eedc33d` · level 2 · depends on App. Hardening Level 1 (50%) (level 1) · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable partial

<!-- q L7398-7402 -->
> Following frameworks like the * OWASP Application Security Verification Standard Level 1 * OWASP Mobile Application Security Verification Standard in all applications provides a good baseline. Implement 95%-100% of the recommendations.

Measure — recommendation; its sentences: R-0498, R-0499

Descriptive, not normative: description R-0152, R-0153, R-0154, R-0155.

#### Containers are running as non-root

`owasp-dsomm#a86c1fbc-28fd-4610-89a3-a7f73acfe45f` · level 2 · usefulness 3 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L7500-7501 -->
> "Containers are running as non-root. This can be enforced in the image itself or during runtime parameters \n(e.g. `podman run --user [...]`)."

Measure — recommendation; its sentences: R-0159 permission

Descriptive, not normative: risk R-0156, R-0157, R-0158.

#### App. Hardening Level 2 (75%)

`owasp-dsomm#03643ca2-03c2-472b-8e19-956bf02fe9b7` · level 3 · depends on App. Hardening Level 1 (level 2) · usefulness 3 · difficulty knowledge 3, time 3, resources 1 · testable partial

<!-- q L7527-7531 -->
> Following frameworks like the * OWASP Application Security Verification Standard Level 2 * OWASP Mobile Application Security Verification Standard Level 2 Implement 75% of the recommendations.

Measure — recommendation; its sentences: R-0500, R-0501

#### Secure headers

`owasp-dsomm#29318d60-18ce-4526-80ea-f5928e49f639` · level 3 · usefulness 4 · difficulty knowledge 2, time 1, resources 2 · testable yes

<!-- q L7589-7599 -->
> Implement and enforce security headers across all applications and services Implementation Methods: 1. Reverse Proxy/Load Balancer: Configure at nginx/Apache level 2. Web Application: Implement in the application middleware 3. Service Mesh: Configure at the ingress controller level 4. Standard Docker Image: Use secure base images with preset headers Remove or Secure: - Server header: Hide server version information - X-Powered-By: Remove technology stack information

Measure — recommendation; its sentences: R-0508 permission, R-0509 permission, R-0510 permission, R-0511 permission, R-0512, R-0513

<!-- q L7575-7575 -->
> - Content-Security-Policy: Define trusted sources for content

R-0502 — recommendation (description)

<!-- q L7576-7576 -->
> - Strict-Transport-Security: Enforce HTTPS connections

R-0503 — recommendation (description)

<!-- q L7577-7577 -->
> - X-Frame-Options: Prevent clickjacking attacks

R-0504 — recommendation (description)

<!-- q L7578-7578 -->
> - X-Content-Type-Options: Prevent MIME-type sniffing

R-0505 — recommendation (description)

<!-- q L7579-7579 -->
> - X-XSS-Protection: Enable browser's XSS filtering

R-0506 — recommendation (description)

<!-- q L7580-7580 -->
> - Referrer-Policy: Control information in the Referrer header

R-0507 — recommendation (description)

Descriptive, not normative: risk R-0160; implementation R-0161, R-0162.

#### App. Hardening Level 2

`owasp-dsomm#ffe86caf-2fec-4630-b514-2db83983984d` · level 4 · depends on App. Hardening Level 2 (75%) (level 3) · usefulness 3 · difficulty knowledge 3, time 3, resources 1 · testable partial

<!-- q L7637-7641 -->
> Following frameworks like the * OWASP Application Security Verification Standard Level 2 * OWASP Mobile Application Security Verification Standard Level 2 Implement 95%-100% of the recommendations.

Measure — recommendation; its sentences: R-0514, R-0515

#### App. Hardening Level 3

`owasp-dsomm#4cae98c2-4163-44ed-bb88-3c67c569533a` · level 5 · depends on App. Hardening Level 2 (level 4) · usefulness 4 · difficulty knowledge 4, time 4, resources 2 · testable partial

<!-- q L7678-7682 -->
> Following frameworks like the * OWASP Application Security Verification Standard Level 3 * OWASP Mobile Application Security Verification Standard Implement 95%-100% of the recommendations.

Measure — recommendation; its sentences: R-0516, R-0517

### Implementation / Development and Source Control

8 activities, levels 1: 1, 2: 1, 3: 4, 4: 1, 5: 1.

#### Version control

`owasp-dsomm#066084c6-1135-4635-9cc5-9e75c7c5459f` · level 1 · usefulness 5 · difficulty knowledge 3, time 3, resources 3 · testable yes

<!-- q L7722-7724 -->
> Version your source code in order to identify deployed features and issues. This includes application and infrastructure code, jenkins configuration, container and virtual machine images definitions.

Measure — recommendation; its sentences: R-0519

<!-- q L7717-7717 -->
> Use a _version control system_ like Github, Gitlab, Bitbucket, etc to version your source code.

R-0518 — recommendation (description)

#### Require a PR before merging

`owasp-dsomm#e7598ac4-b082-4e56-b7df-e2c6b426a5e2` · level 2 · usefulness 4 · difficulty knowledge 2, time 1, resources 2 · testable yes

<!-- q L7753-7757 -->
> Define source code management system policies (e.g. branch protection rules, mandatory code reviews from at least one person, ...) to ensure that changes to critical branches are only possible under defined conditions. These policies can be implemented at repository level or organization level, depending on the source code management system.

Measure — recommendation; its sentences: R-0520, R-0163 permission

#### Block force pushes

`owasp-dsomm#c7d99b18-c3e1-4d22-b2e3-9aa9146c0b17` · level 3 · depends on Require a PR before merging (level 2) · usefulness 3 · difficulty knowledge 2, time 1, resources 2 · testable yes

<!-- q L7801-7801 -->
> Mandate blocking of force pushes in the version control platform.

Measure — recommendation

Descriptive, not normative: risk R-0164, R-0165, R-0166.

#### Block pushes containing secrets

`owasp-dsomm#50ba2bfb-2ae3-4576-8813-a8f00d8a3220` · level 3 · depends on Test for stored secrets in code (level 1) · usefulness 3 · difficulty knowledge 1, time 1, resources 2 · testable yes

<!-- q L7861-7865 -->
> Enable server-side push protection on the source code management system so that pushes containing known secret formats are rejected before entering the repository, with a documented bypass procedure for false positives. Optionally add local pre-commit or CI scanning as an early warning.

Measure — recommendation; its sentences: R-0521

<!-- q L7852-7854 "Pattern-based blocking" .. "detection activities." -->
> Pattern-based blocking catches known secret formats, not everything, so this activity complements rather than replaces the detection activities.

R-0740 — scope (description)

<!-- q L7869-7869 -->
> - Demonstrate that a push containing a test secret is rejected by the source code management system.

R-0522 — assessment

<!-- q L7870-7870 -->
> - Show that push protection is enabled for all relevant repositories, not only a sample.

R-0523 — assessment

<!-- q L7871-7871 -->
> - Show the documented bypass procedure and who may use it.

R-0169 — assessment

<!-- q L7845-7849 "Like" .. "checks." -->
> Like other source control policies (e.g. _Require a PR before merging_, _Block force pushes_), enforcement on the server also covers commits produced by AI coding agents and other automation, which push at higher volume than humans and cannot be assumed to run local checks.

R-0168 — scope (description)

Descriptive, not normative: description R-0167.

#### Dismiss stale PR approvals

`owasp-dsomm#ea6f69f7-54a5-4922-ac15-a77ff0c16162` · level 3 · depends on Require a PR before merging (level 2) · usefulness 4 · difficulty knowledge 2, time 1, resources 2 · testable yes

<!-- q L7927-7929 -->
> Implement a policy where any commits made after a pull request has been approved automatically revoke that approval, necessitating a fresh review and re-approval process.

Measure — recommendation

#### Require status checks to pass

`owasp-dsomm#ac8730a2-ccc0-465c-9550-d91edae9d5ee` · level 3 · depends on Require a PR before merging (level 2) · usefulness 4 · difficulty knowledge 2, time 1, resources 2 · testable yes

<!-- q L7976-7977 -->
> Mandate passing of security related specified status checks, like successful builds or static application security tests, before proceeding.

Measure — recommendation

#### .gitignore

`owasp-dsomm#363a3eea-baf9-4010-88ca-bb8186a2989d` · level 4 · usefulness 5 · difficulty knowledge 2, time 1, resources 1 · testable partial

<!-- q L8021-8022 -->
> .gitignore files help prevent accidental commits of secrets, debug, or workstation specific data

Measure — recommendation

#### Local development linting & style checks performed

`owasp-dsomm#517b0957-4981-4ac0-b4c7-0d8d1934c474` · level 5 · usefulness 2 · difficulty knowledge 1, time 1, resources 1 · testable yes

<!-- q L8050-8050 -->
> Integrate static code analysis tools in IDEs.

Measure — recommendation

### Implementation / Identity and Access Management

17 activities, levels 1: 3, 2: 4, 3: 4, 4: 4, 5: 2.

#### Enforce server-side authorization on every request

`owasp-dsomm#2244983e-5279-4a6c-b594-155a5d26ebc2` · level 1 · usefulness 5 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L8101-8103 -->
> - Authorization is checked server-side on every state-changing and data-returning endpoint. - Checks are centralized (middleware / policy layer), not duplicated ad-hoc per handler. - Access is deny-by-default; missing a check fails closed, not open.

Measure — recommendation; its sentences: R-0524, R-0525, R-0526

<!-- q L8105-8105 -->
> - Pick 3 endpoints and show the server-side authorization check for each.

R-0527 — assessment

<!-- q L8106-8106 -->
> - Attempt an IDOR test (swap an ID/role in the request) and show it is rejected.

R-0528 — assessment

<!-- q L8107-8107 -->
> - Show the authorization logic lives in one reusable place, not copy-pasted.

R-0529 — assessment

Descriptive, not normative: risk R-0170.

#### MFA for admins

`owasp-dsomm#8098e416-e1ed-4ae4-a561-83efbe76bf57` · level 1 · usefulness 4 · difficulty knowledge 2, time 1, resources 2 · testable yes

<!-- q L8132-8133 -->
> Two or more factor authentication for all privileged accounts on systems and applications.

Measure — recommendation

#### Simple access control for systems

`owasp-dsomm#82e499d1-f463-4a4b-be90-68812a874af6` · level 1 · usefulness 5 · difficulty knowledge 3, time 3, resources 3 · testable partial

<!-- q L8174-8174 -->
> All internal systems are using simple authentication.

Measure — recommendation

<!-- q L8176-8176 -->
> - Presenting the documentation of the review of all user privileges yearly.

R-0530 — assessment

<!-- q L8177-8177 -->
> - Presenting the admin count and validating that there are less than 5 admins per system.

R-0531 — assessment

#### Account inventory

`owasp-dsomm#7fe91f4d-1228-46e3-84ca-47b1d1cb8e1b` · level 2 · usefulness 4 · difficulty knowledge 2, time 3, resources 2 · testable yes

<!-- q L8214-8216 -->
> - An inventory of human and non-human accounts is maintained and has a named owner. - Each account maps to a responsible person or system and its purpose. - The inventory is refreshed on a defined cadence or generated automatically.

Measure — recommendation; its sentences: R-0532, R-0533, R-0534

<!-- q L8218-8218 -->
> - Present the account inventory and its owner.

R-0535 — assessment

<!-- q L8219-8219 -->
> - Sample entries and confirm each has an accountable owner and purpose.

R-0536 — assessment

Descriptive, not normative: description R-0171.

#### Central identity provider for human access

`owasp-dsomm#6ffb2c07-8fca-4bc1-a219-1d1944a3bbac` · level 2 · depends on Simple access control for systems (level 1) · usefulness 4 · difficulty knowledge 3, time 3, resources 2 · testable yes

<!-- q L8251-8253 -->
> - Human access to systems and applications is federated through a central IdP / SSO. - Local accounts are the documented exception, not the norm, and are inventoried. - Disabling an identity in the IdP removes access across federated systems.

Measure — recommendation; its sentences: R-0537, R-0538, R-0539

<!-- q L8255-8255 -->
> - Present the IdP and the list of federated applications.

R-0540 — assessment

<!-- q L8256-8256 -->
> - Show that a sample of critical systems authenticate via the IdP.

R-0541 — assessment

<!-- q L8257-8257 -->
> - Demonstrate that disabling a test identity removes its access.

R-0542 — assessment

<!-- q L8258-8259 -->
> - Show your application delegates login to the IdP via OIDC/SAML rather than a custom login form.

R-0543 — assessment

#### Least-privilege access baseline

`owasp-dsomm#d9dc7614-81fb-45a9-a1e0-e033755ddbed` · level 2 · depends on Simple access control for systems (level 1); Account inventory (level 2) · usefulness 5 · difficulty knowledge 3, time 3, resources 2 · testable yes

<!-- q L8298-8303 -->
> - Access is default-deny; permissions are granted through defined roles. - No shared accounts; every action is attributable to one identity. - Standing administrative access is inventoried and capped (e.g. < 5 admins per system). - Application and pipeline service accounts are scoped to only the resources/actions they need (narrow IaC-defined IAM policies, minimal CI `permissions:` blocks), not broad admin roles.

Measure — recommendation; its sentences: R-0544, R-0545, R-0546, R-0547

<!-- q L8292-8293 "This activity establishes" .. "administrative access." -->
> This activity establishes a default-deny posture and removes shared or ambient administrative access.

R-0741 — scope (description)

<!-- q L8305-8305 -->
> - Present the role / permission definitions and show default-deny is in effect.

R-0548 — assessment

<!-- q L8306-8306 -->
> - Present the admin inventory per critical system and show the cap is met.

R-0549 — assessment

<!-- q L8307-8307 -->
> - Sample 3 identities and demonstrate their grants match their role.

R-0550 — assessment

<!-- q L8308-8308 -->
> - Pick one service's IaC-defined role and show it grants only what that service actually uses.

R-0551 — assessment

<!-- q L8291-8292 "Every" .. "more." -->
> Every identity - human and machine - should hold only the permissions it needs to do its job, and nothing more.

R-0172 — recommendation (description)

Descriptive, not normative: risk R-0173.

#### MFA

`owasp-dsomm#598e9f13-1ac8-4a01-b85e-8fab93ee81de` · level 2 · depends on MFA for admins (level 1) · usefulness 4 · difficulty knowledge 2, time 2, resources 2 · testable partial

<!-- q L8344-8345 -->
> Two or more factor authentication for all accounts on all (important) systems and applications.

Measure — recommendation

#### Automated authorization test coverage

`owasp-dsomm#55d43b9a-ab12-4b6f-b289-23ff0cf38565` · level 3 · depends on Enforce server-side authorization on every request (level 1) · usefulness 4 · difficulty knowledge 2, time 3, resources 2 · testable yes

<!-- q L8392-8394 -->
> - A test suite covers each role against each sensitive endpoint/action. - Tests include negative cases (should be denied), not only allowed paths. - Tests run in CI and block merge on failure.

Measure — recommendation; its sentences: R-0552, R-0175, R-0553

<!-- q L8396-8396 -->
> - Show the authorization test suite, including at least one negative test.

R-0554 — assessment

<!-- q L8397-8397 -->
> - Show CI results proving these tests gate merges.

R-0555 — assessment

<!-- q L8398-8398 -->
> - Introduce a deliberate regression and show CI catches it.

R-0556 — assessment

Descriptive, not normative: description R-0174.

#### Automated joiner-mover-leaver provisioning

`owasp-dsomm#582ff41d-99a6-4142-83f5-16e949422e18` · level 3 · depends on Least-privilege access baseline (level 2); Central identity provider for human access (level 2) · usefulness 4 · difficulty knowledge 3, time 4, resources 3 · testable yes

<!-- q L8432-8434 -->
> - Provisioning and de-provisioning are automated from an authoritative source. - Role changes trigger corresponding access changes (removing stale grants). - Leavers lose all access within an agreed, measured SLA.

Measure — recommendation; its sentences: R-0557, R-0558, R-0559

<!-- q L8436-8436 -->
> - Show the automated provisioning pipeline and its authoritative source.

R-0560 — assessment

<!-- q L8437-8437 -->
> - Present metrics on leaver de-provisioning time against the SLA.

R-0561 — assessment

<!-- q L8438-8438 -->
> - Trace one recent mover and confirm stale access was removed.

R-0562 — assessment

#### Fine-Grained Access Controls for authentication and authorization

`owasp-dsomm#070bb14b-e04a-4f3d-896a-a08eba7a35f9` · level 3 · depends on Least-privilege access baseline (level 2) · usefulness 4 · difficulty knowledge 3, time 3, resources 2 · testable yes

<!-- q L8476-8480 -->
> Access is restricted through defined roles (RBAC) rather than per-user grants. The usage of fine-grained access controls access control helps to restrict system access to authorized users. And enhancement is to use *attribute based access control*. Roles, attributes and policies are explicitly defined and documented.

Measure — recommendation

<!-- q L8482-8482 -->
> - Present the role / attribute / policy definitions for a sample system.

R-0563 — assessment

<!-- q L8483-8484 -->
> - Trace one access decision back to a specific role, attribute or policy rule rather than a hardcoded per-user check.

R-0564 — assessment

Descriptive, not normative: risk R-0176.

#### Use correct OAuth2/OIDC authorization flows

`owasp-dsomm#2a2405ca-bfee-4dea-a391-dd5060cc07fa` · level 3 · depends on Central identity provider for human access (level 2) · usefulness 4 · difficulty knowledge 3, time 2, resources 1 · testable yes

<!-- q L8531-8535 -->
> - Each client type uses its recommended flow (Auth Code + PKCE for public/ user-facing clients, Client Credentials for service-to-service). - Implicit Grant and ROPC are not used for new integrations, and existing usage is inventoried and being retired. - Redirect URIs are exact-match allow-listed, not wildcarded.

Measure — recommendation; its sentences: R-0565, R-0566, R-0567

<!-- q L8537-8538 -->
> - For a sample of applications, show which flow each uses and confirm it matches its client type.

R-0568 — assessment

<!-- q L8539-8539 -->
> - Show PKCE is enforced for public clients.

R-0569 — assessment

<!-- q L8540-8541 -->
> - Show the IdP's client registrations for any Implicit/ROPC grants and, if present, the remediation plan.

R-0570 — assessment

#### Just-in-time privileged access

`owasp-dsomm#d42995ac-f4e5-4fa6-b01a-83a0d35ef3b1` · level 4 · depends on Least-privilege access baseline (level 2); MFA for admins (level 1) · usefulness 5 · difficulty knowledge 4, time 4, resources 3 · testable yes

<!-- q L8577-8580 -->
> - Privileged access is granted just-in-time, time-boxed, and auto-revoked. - Requests require approval and produce an audit record. - Standing admin access for routine work is eliminated or reduced to a justified, minimal break-glass set.

Measure — recommendation; its sentences: R-0571, R-0572, R-0573

<!-- q L8582-8582 -->
> - Demonstrate a JIT elevation request, approval and automatic expiry.

R-0574 — assessment

<!-- q L8583-8583 -->
> - Show that routine admin roles carry no standing membership.

R-0575 — assessment

<!-- q L8584-8584 -->
> - Present the break-glass account list and its controls.

R-0576 — assessment

<!-- q L8585-8586 -->
> - Show developers requesting prod access for debugging go through the JIT flow rather than holding standing prod credentials.

R-0577 — assessment

#### Periodic access recertification

`owasp-dsomm#7f216405-fb84-4c84-a495-6b8f4958834a` · level 4 · depends on Least-privilege access baseline (level 2); Automated joiner-mover-leaver provisioning (level 3) · usefulness 4 · difficulty knowledge 2, time 3, resources 3 · testable yes

<!-- q L8621-8623 -->
> - Access reviews run on a defined cadence (e.g. quarterly for privileged access). - Owners re-attest each grant; unconfirmed or unused access is revoked. - Reviews are recorded and auditable.

Measure — recommendation; its sentences: R-0578, R-0579, R-0580

<!-- q L8625-8625 -->
> - Present the most recent recertification campaign and its outcomes.

R-0581 — assessment

<!-- q L8626-8626 -->
> - Show evidence that flagged access was actually revoked.

R-0582 — assessment

<!-- q L8627-8628 -->
> - Show reviews cover your application's own service-account permissions, not just human accounts.

R-0583 — assessment

#### Segregation of duties for critical actions

`owasp-dsomm#879e1f8f-61db-4af5-bb9b-07f21ac417b8` · level 4 · depends on Least-privilege access baseline (level 2) · usefulness 4 · difficulty knowledge 3, time 3, resources 2 · testable yes

<!-- q L8664-8667 -->
> - Conflicting duty pairs are identified (e.g. author vs approver, deploy vs approve-to-prod, security audit vs infrastructure admin). - Each pair is enforced technically (branch protection, maker-checker, separate accounts / roles), not just by policy.

Measure — recommendation; its sentences: R-0584, R-0585

<!-- q L8669-8669 -->
> - Present the documented list of conflicting duty pairs.

R-0586 — assessment

<!-- q L8670-8671 -->
> - Demonstrate enforcement for at least one pair (e.g. a pull request cannot be approved by its author; a production deploy requires a second approver).

R-0179 — assessment

Descriptive, not normative: description R-0177; risk R-0178.

#### Workload and machine identity

`owasp-dsomm#9f83087c-7d97-4715-a2ff-10d3f167c3cc` · level 4 · depends on Least-privilege access baseline (level 2) · usefulness 4 · difficulty knowledge 4, time 4, resources 3 · testable yes

<!-- q L8705-8707 -->
> - Workloads authenticate with short-lived, verifiable identities. - Long-lived static machine credentials are being actively retired. - Each workload identity is attributable and least-privileged.

Measure — recommendation; its sentences: R-0587, R-0588, R-0589

<!-- q L8709-8709 -->
> - Show a workload authenticating via federated / short-lived identity.

R-0590 — assessment

<!-- q L8710-8711 -->
> - Present the inventory of remaining static machine credentials and the plan to retire them.

R-0591 — assessment

Descriptive, not normative: risk R-0180.

#### Continuous and risk-adaptive access

`owasp-dsomm#eba1a951-df6b-4c02-86c5-0370654aa930` · level 5 · depends on Just-in-time privileged access (level 4); Fine-Grained Access Controls for authentication and authorization (level 3); Periodic access recertification (level 4) · usefulness 4 · difficulty knowledge 5, time 5, resources 4 · testable yes

<!-- q L8748-8750 -->
> - Access is continuously evaluated using device, context and risk signals. - Policy decisions incorporate real-time risk (step-up or denial on anomaly). - Segregation-of-duties conflicts are detected and flagged automatically.

Measure — recommendation; its sentences: R-0592, R-0593, R-0594

<!-- q L8742-8743 "Builds on policy-based access control" .. "rather than static." -->
> Builds on policy-based access control to make decisions dynamic rather than static.

R-0742 — scope (description)

<!-- q L8752-8753 -->
> - Demonstrate a risk-based access decision (e.g. step-up or denial on anomalous context).

R-0595 — assessment

<!-- q L8754-8754 -->
> - Show automated SoD conflict detection output and how conflicts are resolved.

R-0596 — assessment

#### Externalized policy-as-code authorization

`owasp-dsomm#3153c507-8e40-44c5-9957-fba236a80a5a` · level 5 · depends on Fine-Grained Access Controls for authentication and authorization (level 3) · usefulness 3 · difficulty knowledge 5, time 4, resources 3 · testable yes

<!-- q L8794-8797 -->
> - A central policy engine (e.g. OPA) evaluates authorization decisions for multiple services rather than each service deciding in isolation. - Policies are version-controlled and covered by automated tests. - Authorization decisions are logged and auditable.

Measure — recommendation; its sentences: R-0597, R-0598, R-0599

<!-- q L8799-8799 -->
> - Show the policy engine and a sample policy under version control with tests.

R-0600 — assessment

<!-- q L8800-8800 -->
> - Show at least two services delegating decisions to the central engine.

R-0601 — assessment

<!-- q L8801-8801 -->
> - Present authorization decision logs.

R-0602 — assessment

Descriptive, not normative: risk R-0181.

### Implementation / Infrastructure Hardening

21 activities, levels 1: 1, 2: 8, 3: 7, 4: 4, 5: 1.

#### Usage of edge encryption at transit

`owasp-dsomm#ad23be9c-5661-4f1f-81a3-5a5dc7061629` · level 1 · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L8836-8839 -->
> By using encryption at the edge of traffic in transit, it is impossible or at least harder to sniff credentials or information being outside of the organization. Using standard secure protocols like HTTPS is recommended.

Measure — recommendation; its sentences: R-0603

#### Backup

`owasp-dsomm#5c61fd6b-8106-4c68-ac28-a8a42f1c67dc` · level 2 · depends on Defined deployment process (level 1) · usefulness 4 · difficulty knowledge 1, time 2, resources 1 · testable yes

<!-- q L8863-8864 -->
> Performing automated periodical backups are used. Backup before deployment can help facilitate deployments whilst testing the backup restore processes.

Measure — recommendation; its sentences: R-0604, R-0182 permission

<!-- q L8876-8876 -->
> A Point in Time Recovery for databases should be implemented.

R-0183 — recommendation (implementation[2].name)

#### Baseline Hardening of the environment

`owasp-dsomm#5992c38c-8597-4035-89db-d15820d81c3a` · level 2 · usefulness 4 · difficulty knowledge 4, time 3, resources 2 · testable partial

<!-- q L8898-8900 -->
> Harden environments according to best practices. Level 1 and partially level 2 from hardening practices like 'CIS Kubernetes Bench for Security' should be considered.

Measure — recommendation; its sentences: R-0184

#### Isolated networks for virtual environments

`owasp-dsomm#4ce24abd-8ba6-494c-828d-4d193e28e4a1` · level 2 · usefulness 5 · difficulty knowledge 3, time 3, resources 3 · testable partial

<!-- q L8967-8967 -->
> The communication between virtual environments is controlled and regulated.

Measure — recommendation

Descriptive, not normative: risk R-0185.

#### Usage of an security account

`owasp-dsomm#746025a6-dbfb-4087-a000-e46acab64ee1` · level 2 · usefulness 4 · difficulty knowledge 3, time 2, resources 3 · testable yes

<!-- q L9006-9006 -->
> Usage of a separate account dedicated for security activities.

Measure — recommendation

#### Usage of containers

`owasp-dsomm#3a94d55e-fd82-4996-9eb3-20d23ff2a873` · level 2 · usefulness 3 · difficulty knowledge 3, time 3, resources 5 · testable yes

<!-- q L9030-9030 -->
> Applications are running in a dedicated and isolated virtualized environments.

Measure — recommendation

#### Usage of encryption at rest

`owasp-dsomm#0ff45fb8-7eef-46ed-9b3a-84c955cd7060` · level 2 · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable partial

<!-- q L9056-9057 -->
> By using encryption at rest, it is impossible or at least harder to to read information.

Measure — recommendation

#### Usage of test and production environments

`owasp-dsomm#bfdacb52-1e3f-431d-ae72-d844a5e86415` · level 2 · depends on Defined deployment process (level 1) · usefulness 4 · difficulty knowledge 3, time 3, resources 5 · testable yes

<!-- q L9081-9081 -->
> A test and a production like environment is used

Measure — recommendation (promotes C-0505)

#### Virtual environments are limited

`owasp-dsomm#760f1056-b0ee-4f22-a35b-f65446f944ca` · level 2 · depends on Usage of containers (level 2) · usefulness 3 · difficulty knowledge 2, time 2, resources 3 · testable yes

<!-- q L9111-9112 -->
> All virtual environments are using resource limits on hard disks, memory and CPU

Measure — recommendation

#### Filter outgoing traffic

`owasp-dsomm#6df508ef-86fc-4c22-bd9f-646c3127ce7d` · level 3 · usefulness 2 · difficulty knowledge 3, time 3, resources 3 · testable yes

<!-- q L9143-9144 -->
> Having a whitelist and explicitly allowing egress traffic provides the ability to stop unauthorized data leakage.

Measure — recommendation

#### Immutable infrastructure

`owasp-dsomm#48e92bb1-fdba-40e8-b6c2-35de0d431833` · level 3 · depends on Infrastructure as Code (level 3) · usefulness 3 · difficulty knowledge 2, time 2, resources 1 · testable no

<!-- q L9178-9178 -->
> Redundancies in the IT systems

Measure — recommendation

<!-- q L9189-9189 -->
> Remove direct access to infrastructure

R-0605 — recommendation (implementation[1].name)

#### Infrastructure as Code

`owasp-dsomm#8b994601-575e-4ea5-b228-accb18c8e514` · level 3 · usefulness 4 · difficulty knowledge 3, time 5, resources 4 · testable yes

<!-- q L9209-9211 -->
> Systems are setup by code. A full environment can be provisioned. In addition, software like Jenkins 2 can be setup and configured in in code too. The code should be stored in a version control system.

Measure — recommendation; its sentences: R-0186, R-0187 permission, R-0188

#### Limitation of system events

`owasp-dsomm#e5386abf-9154-4752-a1a8-c3a8900f732d` · level 3 · depends on Audit of system events (level 3) · usefulness 5 · difficulty knowledge 2, time 2, resources 1 · testable partial

<!-- q L9258-9258 -->
> System calls are limited.

Measure — recommendation

Descriptive, not normative: risk R-0189.

#### Usage of internal encryption at transit

`owasp-dsomm#ecb0184c-6bc9-45da-bbbb-a983797ffc93` · level 3 · usefulness 4 · difficulty knowledge 3, time 4, resources 3 · testable partial

<!-- q L9302-9303 -->
> By using encryption internally, e.g. inside of a cluster, it is impossible or at least harder to sniff credentials.

Measure — recommendation

#### Usage of security by default for components

`owasp-dsomm#11b3848e-e931-4146-a35d-35409ada24ee` · level 3 · depends on Defined build process (level 1) · usefulness 3 · difficulty knowledge 4, time 3, resources 1 · testable yes

<!-- q L9326-9328 -->
> Hardening of components is important, specially for image on which other teams base on. Hardening should be performed on the operation system and on the services inside (e.g. Nginx or a Java-Application).

Measure — recommendation; its sentences: R-0190

#### WAF baseline

`owasp-dsomm#f0e01814-3b88-4bd0-a3a9-f91db001d20b` · level 3 · depends on Context-aware output encoding (level 1) · usefulness 3 · difficulty knowledge 3, time 4, resources 3 · testable partial

<!-- q L9369-9370 -->
> Implementing a web application firewall (WAF) is a critical security control. At a baseline level, the objective is to finely balance the reduction of false positives, maintaining user experience, against a potential increase in the less noticeable false negatives. Begin with the WAF in a monitoring state to understand the traffic and threats. Progressively enforce blocking actions based on intelligence gathered, ensuring minimal disruption to legitimate traffic.

Measure — recommendation

<!-- q L9374-9374 -->
> - Configure WAF in alert mode to establish traffic patterns

R-0606 — recommendation (description)

<!-- q L9375-9375 -->
> - Analyze alerts and adjust sensitivity to optimize for fewer false positives

R-0607 — recommendation (description)

<!-- q L9376-9376 -->
> - Gradually switch to a proactive blocking stance as confidence in the accuracy of the rules increases

R-0608 — recommendation (description)

<!-- q L9378 "It's crucial to monitor" .. "false negatives." -->
> It's crucial to monitor and update the WAF configuration to adapt to evolving threats and minimize the potential for both false positives and false negatives.

R-0743 — recommendation (description)

Descriptive, not normative: risk R-0191.

#### Hardening of the Environment

`owasp-dsomm#dcf9601b-b4f2-4e25-9143-e39af75f7c33` · level 4 · usefulness 3 · difficulty knowledge 4, time 4, resources 2 · testable partial

<!-- q L9416-9418 -->
> Harden environments according to best practices. Level 2 and partially level 3 from hardening practices like 'CIS Kubernetes Bench for Security' should be considered.

Measure — recommendation; its sentences: R-0192

#### Production near environments are used by developers

`owasp-dsomm#e14de741-94b3-447c-8b07-eea947d82e61` · level 4 · depends on Automated deployment process (level 1); Infrastructure as Code (level 3) · usefulness 4 · difficulty knowledge 3, time 3, resources 3 · testable yes

<!-- q L9483-9487 -->
> Usage of infrastructure as code helps to create a production near environment. The developer needs to be trained in order to setup a local development environment. In addition, it should be possible to create production like test data. Often personal identifiable information is anonymized in order to comply with data protection laws.

Measure — recommendation; its sentences: R-0609, R-0193

#### Usage of a chaos technology

`owasp-dsomm#f8e80f18-2503-4e3e-b3bc-7f67bb28defe` · level 4 · usefulness 3 · difficulty knowledge 3, time 5, resources 5 · testable yes

<!-- q L9517-9518 -->
> A randomized periodically shutdown of systems makes sure, that nobody will perform manual changes to a system.

Measure — recommendation

#### WAF medium

`owasp-dsomm#f0e01814-3b88-4bd0-a3a9-f91db001d20b-medium` · level 4 · depends on WAF baseline (level 3) · usefulness 3 · difficulty knowledge 4, time 5, resources 4 · testable partial

<!-- q L9557-9558 -->
> A WAF deployed with a medium level of protection strengthens the security posture by striking a more advanced balance between the detection of genuine threats and the minimization of false alarms. Maintain the WAF in alert mode initially to ensure a comprehensive understanding of potential threats. With a medium-level configuration, the WAF settings are refined for greater precision in threat detection, with a stronger emphasis on security without significantly impacting legitimate traffic.

Measure — recommendation; its sentences: R-0610

<!-- q L9559-9566 -->
> "A medium-level WAF configuration builds upon the baseline to offer a more nuanced and responsive defense mechanism against a wider array of threats.\n\nSample steps:\n - Implement an enhanced set of WAF rules based on baseline data\n \ - Continuous monitoring and fine-tuning of the WAF configuration\n - Develop a strategic incident response plan utilizing WAF insights \n \nThe medium configuration requires diligent management and continuous improvement to address new vulnerabilities while maintaining the integrity of application access.\n\nThere are debates on how useful a WAF is for APIs.\n"

R-0611 — recommendation (description)

#### WAF Advanced

`owasp-dsomm#f0e01814-3b88-4bd0-a3a9-f91db001d20b-advanced` · level 5 · depends on WAF baseline (level 3) · usefulness 4 · difficulty knowledge 5, time 5, resources 5 · testable partial

<!-- q L9604-9605 -->
> An advanced WAF protection level includes rigorous input validation, rejecting any parameters not explicitly required, and custom rule sets that are dynamically updated in response to emerging threats. The advanced WAF setup is designed to ensure all data is in the correct format and any superfluous input parameters are automatically rejected. It includes machine learning algorithms to detect anomalies, custom-developed rules for real-time traffic analysis, and seamless integration with existing security infrastructures to adapt to the ever-changing threat landscape.

Measure — recommendation; its sentences: R-0612, R-0613

<!-- q L9610-9610 -->
> - Implement strict data type and format validation rules to ensure only correctly formatted data is processed.

R-0614 — recommendation (description)

<!-- q L9611-9611 -->
> - Establish a denylist for all parameters that are not explicitly required, blocking them by default.

R-0615 — recommendation (description)

<!-- q L9612-9612 -->
> - Develop and continuously refine custom rulesets based on the application's traffic patterns, user behavior, and known vulnerabilities.

R-0616 — recommendation (description)

<!-- q L9613-9613 -->
> - Integrate machine learning algorithms to enhance anomaly detection and automatic rule adjustment.

R-0617 — recommendation (description)

<!-- q L9614-9614 -->
> - Correlate and analyze WAF logs with other security systems like SIEM for comprehensive threat intelligence.

R-0618 — recommendation (description)

<!-- q L9615-9615 -->
> - Conduct regular red team exercises to test and validate the effectiveness of the WAF configurations against simulated advanced attack scenarios.

R-0619 — recommendation (description)

<!-- q L9616-9616 -->
> - Activate automated threat response mechanisms to immediately neutralize detected threats.

R-0620 — recommendation (description)

## Information Gathering

### Information Gathering / Logging

8 activities, levels 1: 1, 2: 2, 3: 3, 5: 2.

#### Centralized system logging

`owasp-dsomm#4eced38a-7904-4c45-adb0-50b663065540` · level 1 · usefulness 2 · difficulty knowledge 1, time 1, resources 1 · testable yes

<!-- q L9661-9663 -->
> - Implement a centralized logging solution for all critical systems. - System logs must be stored in a central repository, protected from unauthorized access and modification. - Ensure that log collection is automated and covers all relevant system events.

Measure — recommendation; its sentences: R-0621, R-0195, R-0622

Descriptive, not normative: risk R-0194.

#### Centralized application logging

`owasp-dsomm#fe875e17-ae4a-45f8-a359-244aa4fcbc04` · level 2 · depends on Alerting (level 2) · usefulness 5 · difficulty knowledge 1, time 1, resources 1 · testable yes

<!-- q L9702-9703 -->
> A centralized logging system is used and applications logs (including application exceptions) are shipped to it.

Measure — recommendation (promotes C-0526)

Descriptive, not normative: risk R-0196, R-0197.

#### Logging of security events

`owasp-dsomm#ccfdd0a8-991e-4269-ad77-c0a54ca655cb` · level 2 · usefulness 4 · difficulty knowledge 1, time 1, resources 1 · testable yes

<!-- q L9736-9737 -->
> Security-relevant events like login/logout or creation, change, deletion of users should be logged.

Measure — recommendation; its sentences: R-0198

<!-- q L9739-9739 -->
> - Show which events are logged.

R-0630 — assessment

<!-- q L9740-9740 -->
> - Show a test for one event logging.

R-0631 — assessment

<!-- q L9729-9729 "Implement" .. "events." -->
> Implement logging of security relevant events.

R-0623 — recommendation (description)

<!-- q L9730-9730 -->
> - successful/failed login/logout

R-0624 — recommendation (description)

<!-- q L9731-9731 -->
> - creation, change, and deletion of users

R-0625 — recommendation (description)

<!-- q L9732-9732 -->
> - errors during input validation and output creation

R-0626 — recommendation (description)

<!-- q L9733-9733 -->
> - exceptions and errors with security in their name

R-0627 — recommendation (description)

<!-- q L9734-9734 -->
> - transactions of value (e.g., financial transactions, costly operations)

R-0628 — recommendation (description)

<!-- q L9735-9735 -->
> - :unicorn: (special things of your application)

R-0629 — recommendation (description)

Descriptive, not normative: risk R-0199.

#### Analyze logs

`owasp-dsomm#b217c8bb-5d61-4b41-a675-1083993f83b1` · level 3 · usefulness 3 · difficulty knowledge 2, time 2, resources 2 · testable partial

<!-- q L9790-9790 -->
> Check logs for keywords.

Measure — recommendation

#### Logging of AI interactions

`owasp-dsomm#053ca80e-c2e7-4ec6-8a6d-2879187df357` · level 3 · depends on Centralized application logging (level 2) · usefulness 4 · difficulty knowledge 3, time 3, resources 2 · testable yes

<!-- q L9826-9830 -->
> Log AI interactions centrally: prompts, tool/command invocations, used model versions and resulting actions, attributed to dedicated agent identities. Feed the logs into the existing security monitoring and alert on anomalies (e.g. unusual repositories, mass file access, activity at odd hours).

Measure — recommendation

<!-- q L9834-9834 -->
> - Show where AI interactions (prompts, responses, tool calls) are logged and which fields are captured.

R-0632 — assessment

<!-- q L9835-9835 -->
> - Show that the logs are integrated into centralized logging with appropriate retention and access restrictions.

R-0633 — assessment

Descriptive, not normative: risk R-0200, R-0201.

#### Visualized logging

`owasp-dsomm#7c735089-6a83-419f-8b27-c1e676cedea1` · level 3 · depends on Centralized system logging (level 1); Centralized application logging (level 2) · usefulness 4 · difficulty knowledge 1, time 3, resources 3 · testable yes

<!-- q L9954-9955 -->
> Protocols are visualized in a simple to use real time monitoring system. The GUI gives the ability to search for special attributes in the protocol.

Measure — recommendation

#### Correlation of security events

`owasp-dsomm#ccf4561d-253f-4762-adcb-bc4622fd6fc5` · level 5 · depends on Visualized logging (level 3); Alerting (level 2) · usefulness 3 · difficulty knowledge 4, time 4, resources 4 · testable yes

<!-- q L9988-9989 -->
> Events are correlated on one system. For example the correlation and visualization of failed login attempts combined with successful login attempts.

Measure — recommendation

#### PII logging concept

`owasp-dsomm#613a73dc-4f60-49db-a6ce-4fb7bf8519f9` · level 5 · usefulness 1 · difficulty knowledge 1, time 1, resources 1 · testable yes

<!-- q L10018-10018 -->
> A concept how to log PII is documented and applied.

Measure — recommendation

### Information Gathering / Monitoring

16 activities, levels 1: 3, 2: 3, 3: 5, 4: 4, 5: 1.

#### Simple application metrics

`owasp-dsomm#e9a6d403-a467-445e-b98a-74f0c29da0b1` · level 1 · usefulness 5 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L10072-10083 -->
> Gathering of application metrics helps to identify incidents like brute force attacks, login/logout patterns, and unusual spikes in activity. Key metrics to monitor include: - Authentication attempts (successful/failed logins) - Transaction volumes and patterns (e.g. orders, payments) - API call rates and response times - User session metrics - Resource utilization Example: An e-commerce application normally processes 100 orders per hour. A sudden spike to 1000 orders per hour could indicate either: - A legitimate event (unannounced marketing campaign, viral social media post) - A security incident (automated bulk purchase bots, credential stuffing attack) By monitoring these basic metrics, teams can quickly investigate abnormal patterns and determine if they represent security incidents requiring response.

Measure — recommendation; its sentences: R-0634, R-0635, R-0636, R-0637, R-0638, R-0204 descriptive

<!-- q L10085-10085 -->
> - Basic application metrics are collected and reviewed.

R-0639 — assessment

Descriptive, not normative: description R-0202; risk R-0203.

#### Simple budget metrics

`owasp-dsomm#f08a3219-6941-43ec-8762-4aff739f4664` · level 1 · usefulness 5 · difficulty knowledge 1, time 1, resources 1 · testable yes

<!-- q L10116-10116 -->
> Set up budget monitoring and alerting for all critical resources. Use provider tools to track spending and configure alerts when thresholds are reached. Implement hard limits where possible to prevent budget overruns.

Measure — recommendation

<!-- q L10118-10118 -->
> - The organization regularly monitors budget metrics

R-0640 — assessment

<!-- q L10119-10119 -->
> - Alerting outside given thresholds are implemented

R-0641 — assessment

Descriptive, not normative: description R-0205; risk R-0206.

#### Simple system metrics

`owasp-dsomm#3d1f4c3b-f713-46d9-933a-54a014a26c03` · level 1 · usefulness 5 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L10149-10149 -->
> Collect and monitor key system metrics, including CPU, memory, and disk usage.

Measure — recommendation

<!-- q L10151-10151 -->
> - Basic system metrics are monitored and reviewed regularly

R-0642 — assessment

#### Alerting

`owasp-dsomm#8a442d8e-0eb1-4793-a513-571aef982edd` · level 2 · depends on Visualized metrics (level 2) · usefulness 5 · difficulty knowledge 2, time 5, resources 5 · testable partial

<!-- q L10193-10193 -->
> Thresholds for metrics are set. In case the thresholds are reached, alarms are send out. Which should get attention due to the critically.

Measure — recommendation; its sentences: R-0208

<!-- q L10180-10184 "AI" .. "judgement." -->
> AI can improve both (see Anthropic's eBook _Zero Trust for AI Agents_): give a triage assistant read-only access to the monitoring data and let it write a structured first assessment for every alert, so analysts start with the alerts that actually need human judgement.

R-0207 — permission (description)

<!-- q L10184-10188 "Introduce" .. "rule." -->
> Introduce it incrementally: choose a single rule that is known to generate mostly false positives, let the model handle its alert stream for a trial period while a human independently assesses the same alerts, compare the two, and only then move on to the next rule.

R-0643 — recommendation (description)

<!-- q L10188-10190 "The assistant prepares evidence" .. "remain with humans." -->
> The assistant prepares evidence, correlation and documentation; decisions about containment and disclosure remain with humans.

R-0744 — scope (description)

#### Monitoring of costs

`owasp-dsomm#10e23a8c-22ff-4487-a706-87ccc9d0798e` · level 2 · depends on Simple application metrics (level 1); Simple system metrics (level 1) · usefulness 3 · difficulty knowledge 1, time 2, resources 2 · testable yes

<!-- q L10239-10241 -->
> Implement cost budgets. Setting of an alert threshold and sending out errors when it is reached. In the best case, a second threshold with a limit is set so that the cost can not go higher.

Measure — recommendation; its sentences: R-0209 permission

#### Visualized metrics

`owasp-dsomm#ded39bcf-4eaa-4c5f-9c94-09acde0a4734` · level 2 · depends on Simple application metrics (level 1); Simple system metrics (level 1) · usefulness 3 · difficulty knowledge 1, time 2, resources 2 · testable yes

<!-- q L10267-10267 -->
> Metrics are visualized in real time in a user friendly way.

Measure — recommendation

#### Advanced availability and stability metrics

`owasp-dsomm#ed715b38-c34b-40cd-83fd-ce807f306fc1` · level 3 · depends on Simple application metrics (level 1); Visualized metrics (level 2) · usefulness 4 · difficulty knowledge 3, time 3, resources 2 · testable partial

<!-- q L10293-10294 -->
> Advanced metrics are gathered in relation to availability and stability. For example unplanned downtime's per year.

Measure — recommendation

#### Audit of system events

`owasp-dsomm#1cd5e4b8-be36-4726-adc7-d8f843f47ac8` · level 3 · depends on Visualized metrics (level 2) · usefulness 4 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L10320-10320 -->
> Gathering of system calls.

Measure — recommendation

#### Deactivation of unused metrics

`owasp-dsomm#7f36b9ba-bc05-4fd6-9a2a-73344c249722` · level 3 · depends on Visualized metrics (level 2) · usefulness 5 · difficulty knowledge 2, time 5, resources 5 · testable partial

<!-- q L10354-10354 -->
> Deactivation of unused metrics helps to free resources.

Measure — recommendation

#### Grouping of metrics

`owasp-dsomm#42170a71-d4c8-47af-bd71-bf36875fd05b` · level 3 · usefulness 2 · difficulty knowledge 2, time 4, resources 2 · testable partial

<!-- q L10381-10381 -->
> Meaningful grouping of metrics helps to speed up analysis.

Measure — recommendation

#### Targeted alerting

`owasp-dsomm#d6f06ae8-401a-4f44-85df-1079247fa030` · level 3 · depends on Alerting (level 2) · usefulness 5 · difficulty knowledge 2, time 5, resources 5 · testable yes

<!-- q L10407-10408 -->
> By the definition of target groups for incidents people are only getting alarms for incidents they are in charge for.

Measure — recommendation (promotes C-0553)

#### Advanced app. metrics

`owasp-dsomm#d03bc410-74a7-4e92-82cb-d01a020cb6bf` · level 4 · depends on Simple application metrics (level 1); Visualized metrics (level 2) · usefulness 4 · difficulty knowledge 3, time 3, resources 2 · testable partial

<!-- q L10437-10437 -->
> All defects from the dimension Test- and Verification are instrumented.

Measure — recommendation

#### Coverage and control metrics

`owasp-dsomm#d0d681e7-d6de-4829-ac64-a9eb2546aa0d` · level 4 · depends on Visualized metrics (level 2) · usefulness 4 · difficulty knowledge 3, time 5, resources 2 · testable partial

<!-- q L10464-10469 -->
> "Usage of Coverage- and control-metrics to show the effectiveness of the security program. Coverage is the degree in \n which a specific security control for a specific target group is applied with all resources.\n \ The control degree shows the actual application of security standards and security-guidelines. Examples are gathering information on anti-virus, anti-rootkits, patch management, server configuration and vulnerability management."

Measure — recommendation

#### Defense metrics

`owasp-dsomm#e808028c-351c-42f1-bcd9-fba738d1fc55` · level 4 · depends on Visualized metrics (level 2); Filter outgoing traffic (level 3) · usefulness 4 · difficulty knowledge 3, time 5, resources 2 · testable partial

<!-- q L10496-10497 -->
> Gathering of defense metrics like TCP/UDP sources enables to assume the geographic location of the request. Assuming a Kubernetes cluster with an egress-traffic filter (e.g. IP/domain based), an alert might be send out in case of every violation. For ingress-traffic, alerting might not even be considered.

Measure — recommendation; its sentences: R-0644

#### Screens with metric visualization

`owasp-dsomm#8746647c-638c-473f-8e17-82c068e4c311` · level 4 · depends on Grouping of metrics (level 3) · usefulness 5 · difficulty knowledge 2, time 1, resources 1 · testable yes

<!-- q L10525-10526 -->
> By having an internal accessible screen with a security related dashboards helps to visualize incidents.

Measure — recommendation

#### Metrics are combined with tests

`owasp-dsomm#71699daf-b2a4-466b-a0b2-89f7dbb18506` · level 5 · depends on Grouping of metrics (level 3) · usefulness 5 · difficulty knowledge 2, time 3, resources 2 · testable partial

<!-- q L10553-10553 -->
> Metrics during tests helps to identify programming errors.

Measure — recommendation

### Information Gathering / Test KPI

7 activities, levels 2: 3, 3: 3, 4: 1.

#### Number of vulnerabilities/severity

`owasp-dsomm#bc548cba-cb82-4f76-bd4b-325d9d256279` · level 2 · usefulness 3 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L10580-10581 -->
> Measurement and communication of vulnerabilities per severity for components like applications. At least quarterly.

Measure — recommendation

<!-- q L10583-10583 -->
> Communication can be performed in a simple way, e.g. text based during the build process.

R-0210 — permission (description)

<!-- q L10584-10584 -->
> This activity depends on at least one security testing implementation.

R-0645 — scope (description)

#### Number of vulnerabilities/severity/layer

`owasp-dsomm#0ec92899-a5cb-4649-984b-2fb1d6c784ad` · level 2 · usefulness 3 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L10612-10614 -->
> Measurement and communication of vulnerabilities per severity for components like applications and split it depending on the layer (e.g. app/infra). At least quarterly.

Measure — recommendation

<!-- q L10616-10616 -->
> Communication can be performed in a simple way, e.g. text based during the build process.

R-0211 — permission (description)

<!-- q L10617-10617 -->
> This activity depends on at least one security testing implementation.

R-0646 — scope (description)

<!-- q L10619-10619 -->
> - Cloud provider (if insights are possible)

R-0647 — scope (description)

<!-- q L10620-10620 -->
> - Runtimes, e.g. Kubernetes nodes

R-0648 — scope (description)

<!-- q L10621-10621 -->
> - Base images and container images

R-0649 — scope (description)

<!-- q L10622-10622 -->
> - Application

R-0650 — scope (description)

<!-- q L10625-10625 -->
> - Cloud provider

R-0651 — scope (description)

<!-- q L10626-10626 -->
> - Runtime, e.g. Kubernetes

R-0652 — scope (description)

<!-- q L10627-10627 -->
> - Base images and container images

R-0653 — scope (description)

<!-- q L10628-10628 -->
> - Application

R-0654 — scope (description)

#### Patching mean time to resolution via PR

`owasp-dsomm#86d490b9-d798-4a5b-a011-ab9688014c46` · level 2 · depends on Automated PRs for patches (level 1) · usefulness 3 · difficulty knowledge 1, time 1, resources 2 · testable yes

<!-- q L10657-10663 -->
> "Measurement and communication of patching Mean Time to Resolution (MTTR) in alignment with Service Level Agreements (SLAs), conducted at least on a quarterly basis.\nThis includes the measurement of the existence of a properly configured automated pull request (PR) tool (e.g., Dependabot or Renovate) in a repository. \nIn addition, the measurement of the time from opening an automated PR to merging it.\n\nAverage time to patch is visualized per component/project/team."

Measure — recommendation

Descriptive, not normative: risk R-0212.

#### Fix rate per repo/product

`owasp-dsomm#cf0d600e-114d-4887-9059-d81c53805f0d` · level 3 · usefulness 3 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L10693-10696 -->
> "Measurement and communication of the number of vulnerabilities handled per severity level for components such as applications, ensuring alignment with SLAs. \nThe rate should be broken down by team, product, application, repository, and/or service. This analysis should be conducted at least quarterly."

Measure — recommendation; its sentences: R-0214, R-0215

Descriptive, not normative: risk R-0213.

#### Generation of response statistics

`owasp-dsomm#c922981b-65ed-40f3-a947-96fee9a0125f` · level 3 · depends on Usage of a vulnerability management system (level 3) · usefulness 3 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L10754-10755 -->
> Creation and response statistics (e.g. Mean Time to Resolution) of findings. This is also referred to as _Mean Time to Resolve_.

Measure — recommendation

#### SLA per criticality

`owasp-dsomm#51f3fce5-b5c8-4683-8c41-e785fe4f3b5f` · level 3 · usefulness 3 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L10822-10825 -->
> "Measurement and communication of how many of the vulnerabilities handling per severity for components like applications are aligned to SLAs. \nThis is performed for the hole organization and doesn't need to be broken down (yet) on team/product/application. \nAt least quarterly."

Measure — recommendation; its sentences: R-0655, R-0656

Descriptive, not normative: risk R-0216.

#### Patching mean time to resolution via production

`owasp-dsomm#77ffc53e-9f3d-41f4-92d3-02f04f9b6b0f` · level 4 · depends on Patching mean time to resolution via PR (level 2); Automated PRs for patches (level 1) · usefulness 3 · difficulty knowledge 1, time 1, resources 2 · testable yes

<!-- q L10887-10888 -->
> Measurement and communication of the time from the availability of a patch to its deployment in production in alignment with Service Level Agreements (SLAs), conducted at least on a quarterly basis. Average time to patch is visualized per component/project/team.

Measure — recommendation

Descriptive, not normative: risk R-0217.

## Test and Verification

### Test and Verification / Application tests

4 activities, levels 2: 1, 3: 1, 4: 1, 5: 1.

#### Security unit tests for important components

`owasp-dsomm#eb2c7f9d-d0bd-4253-a2ba-cff2ace4a075` · level 2 · usefulness 3 · difficulty knowledge 3, time 4, resources 2 · testable yes

<!-- q L10917-10918 -->
> Usage of unit tests to test important security related features like authentication and authorization.

Measure — recommendation

#### Security integration tests for important components

`owasp-dsomm#f57d55f2-dc05-4b34-9d1f-f8ce5bfb0715` · level 3 · usefulness 2 · difficulty knowledge 3, time 4, resources 2 · testable yes

<!-- q L10955-10956 -->
> Implementation of essential security related integration tests. For example for authentication and authorization.

Measure — recommendation

#### Smoke Test

`owasp-dsomm#73aaae0b-5d68-4953-9fa4-fd25bf665f2a` · level 4 · depends on Automated deployment process (level 1) · usefulness 2 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L10981-10982 -->
> Integration tests are performed against the production environment after each deployment.

Measure — recommendation

#### High coverage of security related module and integration tests

`owasp-dsomm#67667c97-c33e-4306-a4e5-e7b1d8e10c5a` · level 5 · usefulness 3 · difficulty knowledge 5, time 5, resources 3 · testable partial

<!-- q L11010-11011 -->
> Implementation of security related tests via unit tests and integration tests. Including the test of libraries, in case the are not tested already.

Measure — recommendation

### Test and Verification / Consolidation

14 activities, levels 1: 2, 2: 2, 3: 7, 4: 2, 5: 1.

#### Simple false positive treatment

`owasp-dsomm#c1acc8af-312e-4503-a817-a26220c993a0` · level 1 · usefulness 4 · difficulty knowledge 1, time 1, resources 1 · testable yes

<!-- q L11053-11063 -->
> Findings from security tests must be triaged and outcomes persisted/documented to: - Prevent re-analysis of known issues in subsequent test runs - Track accepted risks vs false positives - Enable consistent decision-making across teams At this maturity level, a simple tracking system suffices - tools need only distinguish between "triaged" and "untriaged" findings, without complex categorization. Some tools refer to this as "suppression" of findings. Samples for false positive handling: - [OWASP Dependency Check](https://jeremylong.github.io/DependencyCheck/general/suppression.html) - [Kubescape with VEX](https://kubescape.io/blog/2023/12/07/kubescape-support-for-vex-generation/) - [OWASP DefectDojo Risk Acceptance](https://docs.defectdojo.com/en/working_with_findings/findings_workflows/risk_acceptances/) and [False Positive Handling](https://docs.defectdojo.com/en/working_with_findings/intro_to_findings/#triage-vulnerabilities-using-finding-status)

Measure — recommendation; its sentences: R-0221, R-0661, R-0662, R-0663, R-0664 permission

<!-- q L11065-11065 -->
> A process is defined for triaging and documenting false positives and accepted risks

R-0665 — assessment

<!-- q L11043-11047 "This" .. "decision." -->
> This must also be documented.\n\nAI can support triage as a complementary tool: a language model with access to the finding and the surrounding code can assess reachability and exploitability in context, propose a triage verdict with reasoning and draft the documentation of the decision.

R-0219 — recommendation (description); its parts: R-0657 must recommendation, R-0658 can permission, R-0659 can descriptive

<!-- q L11047-11048 "The human" .. "for it" -->
> The human decision stays: AI verdicts are input to triage, not a substitute for it

R-0660 — scope (description)

Descriptive, not normative: description R-0218; risk R-0220.

#### Treatment of defects with high or critical severity

`owasp-dsomm#44f2c8a9-4aaa-4c72-942d-63f78b89f385` · level 1 · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L11121-11122 -->
> - Make it a rule that all _high_ or _critical_ security findings must be fixed before the software is approved for release or use. - Track these issues and make sure they are resolved quickly.

Measure — recommendation; its sentences: R-0224, R-0668

<!-- q L11124-11124 "-" .. "production." -->
> - Provide evidence that vulnerabilities are treated within the defined time frame in production.

R-0669 — assessment

<!-- q L11124-11124 "For" .. "statistics." -->
> For example via the DSOMM activity [Number of vulnerabilities/severity](./activity-description?uuid=bc548cba-cb82-4f76-bd4b-325d9d256279) or [Patching mean time to resolution via PR](./activity-description?uuid=86d490b9-d798-4a5b-a011-ab9688014c46) with extra deployment statistics.

R-0670 — assessment

<!-- q L11117-11117 "All" .. "production." -->
> All security problems that are rated as "high" or "critical" must be fixed before the software can be released or used in production.

R-0222 — recommendation (description); its parts: R-0666 must recommendation, R-0667 can descriptive

<!-- q L11117-11117 "This" .. "postponed." -->
> This means that if a serious vulnerability is found, it cannot be ignored or postponed.

R-0223 — recommendation (description)

#### Artifact-based false positive treatment

`owasp-dsomm#8f2b4d5a-3c1e-4b7a-9d8f-2e6c4a1b5d7f` · level 2 · depends on Simple false positive treatment (level 1) · usefulness 3 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L11163-11166 -->
> "Implement false positive marking and temporary acceptance of findings \nbased on specific artifacts (applications, components, or repositories).\nThis allows teams to suppress findings for specific versions or builds\nwhile maintaining visibility for future releases."

Measure — recommendation

Descriptive, not normative: risk R-0225.

#### Simple visualization of defects

`owasp-dsomm#55f4c916-3a34-474d-ad96-9a9f7a4f6a83` · level 2 · usefulness 3 · difficulty knowledge 2, time 2, resources 1 · testable partial

<!-- q L11239-11239 -->
> Vulnerabilities are simple visualized.

Measure — recommendation

#### Fix based on accessibility

`owasp-dsomm#0c10a7f7-f78f-49f2-943d-19fdef248fed` · level 3 · depends on Treatment of defects with high or critical severity (level 1); Inventory of production components (level 1) · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L11318-11319 -->
> Implement a simple risk-based prioritization framework for vulnerability remediation based on accessibility of the applications.

Measure — recommendation

<!-- q L11312-11312 -->
> Develop a scoring system for asset accessibility, considering factors like:

R-0671 — recommendation (description)

<!-- q L11313-11313 -->
> - Whether the asset is internet-facing (highly recommended)

R-0672 — recommendation (description)

<!-- q L11314-11314 -->
> - The number of network hops required to reach the asset (recommended)

R-0673 — recommendation (description)

<!-- q L11315-11315 -->
> - Authentication requirements for access (recommended)

R-0674 — recommendation (description)

#### Global false positive treatment

`owasp-dsomm#9e3a7c2f-1b4d-4e8a-a5c6-7f2b9d1e3a8c` · level 3 · depends on Artifact-based false positive treatment (level 2); Usage of a vulnerability management system (level 3) · usefulness 4 · difficulty knowledge 3, time 3, resources 2 · testable yes

<!-- q L11354-11356 -->
> "Implement global false positive and acceptance management that applies \nconsistently across all applications. This enables organization-wide security decisions and reduces redundant \nanalysis of common false positives."

Measure — recommendation

<!-- q L11359-11361 "When" .. "environment" -->
> When a finding is marked as a false positive or temporarily \naccepted at the global level, this decision automatically applies to \nall applications in the specified environment

R-0675 — recommendation (description)

#### Integration in development process

`owasp-dsomm#aaffa73f-59f6-4267-b0ab-732f3d13e90d` · level 3 · usefulness 3 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L11395-11396 -->
> Integration of findings into the development process. E.g. adding findings to the backlog of products teams.

Measure — recommendation

Descriptive, not normative: risk R-0226; description R-0227.

#### Integration of vulnerability issues into the development process

`owasp-dsomm#ce970c9b-da94-41cf-bd78-8c15357b7e8e` · level 3 · usefulness 2 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L11481-11481 -->
> Vulnerabilities are tracked in the teams issue system (e.g. jira).

Measure — recommendation

Descriptive, not normative: implementation R-0228, R-0229, R-0230.

#### Treatment of defects per protection requirement

`owasp-dsomm#2b7cc923-bdaf-43e3-8fb4-a995b7783969` · level 3 · usefulness 3 · difficulty knowledge 2, time 2, resources 2 · testable partial

<!-- q L11525-11528 -->
> "Defining the protection requirement and the corresponding handling of vulnerabilities per severity for components like applications are aligned to SLAs. \n This is performed for the hole organization and doesn't need to be broken down (yet) on team/product/application. \n At least quarterly."

Measure — recommendation (promotes C-0592)

<!-- q L11530-11530 -->
> The protection requirements for an application should consider:

R-0232 — recommendation (description)

<!-- q L11531-11531 -->
> - Data criticality

R-0676 — recommendation (description)

<!-- q L11532-11532 -->
> - Application accessibility (internal vs. external)

R-0677 — recommendation (description)

<!-- q L11533-11533 -->
> - Regulatory compliance

R-0678 — recommendation (description)

<!-- q L11534-11534 -->
> - Other relevant factors

R-0679 — recommendation (description)

Descriptive, not normative: risk R-0231.

#### Treatment of defects with medium severity

`owasp-dsomm#9cac3341-fe83-4079-bef2-bfc4279eb594` · level 3 · usefulness 3 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L11599-11599 -->
> Vulnerabilities with severity middle are added to the quality gate.

Measure — recommendation

#### Usage of a vulnerability management system

`owasp-dsomm#85ba5623-84be-4219-8892-808837be582d` · level 3 · depends on Exploit likelihood estimation (level 2); Each team has a security champion (level 2); Office Hours (level 3) · usefulness 2 · difficulty knowledge 3, time 3, resources 2 · testable partial

<!-- q L11627-11628 -->
> Aggregation of vulnerabilities in one tool reduce the workload to handle them, e.g. mark as false positives.

Measure — recommendation

<!-- q L11639-11642 "For" .. "scale." -->
> For known vulnerabilities a processes to estimate the exploit ability of a vulnerability is recommended.\n\nTo implement a security culture including training, office hours and security champions can help integrating \nsecurity scanning at scale.

R-0233 — recommendation (description); its parts: R-0680 none recommendation, R-0681 can descriptive

#### Advanced visualization of defects

`owasp-dsomm#7a82020c-94d1-471c-bbd3-5f7fe7df4876` · level 4 · usefulness 2 · difficulty knowledge 2, time 4, resources 1 · testable yes

<!-- q L11690-11690 -->
> Findings are visualized per component/project/team.

Measure — recommendation

#### Reproducible defect tickets

`owasp-dsomm#27337442-e4b1-4e87-8dc9-ce86fbb79a39` · level 4 · usefulness 2 · difficulty knowledge 3, time 2, resources 2 · testable yes

<!-- q L11751-11753 -->
> Vulnerabilities include the test procedure to give the staff from operations and development the ability to reproduce vulnerabilities. This enhances the understanding of vulnerabilities and therefore the fix have a higher quality.

Measure — recommendation

#### Treatment of all defects

`owasp-dsomm#b2f77606-3e6c-41e9-b72d-7c0b1d3d581d` · level 5 · usefulness 2 · difficulty knowledge 3, time 4, resources 1 · testable yes

<!-- q L11782-11782 -->
> All vulnerabilities are added to the quality gate.

Measure — recommendation

### Test and Verification / Dynamic depth for applications

9 activities, levels 2: 3, 3: 3, 4: 1, 5: 2.

#### Coverage of client side dynamic components

`owasp-dsomm#9711f871-f79d-4573-8d4f-d2c98fd0d18e` · level 2 · depends on Usage of different roles (level 2) · usefulness 4 · difficulty knowledge 3, time 3, resources 1 · testable yes

<!-- q L11811-11812 -->
> Usage of a spider which executes dynamic content like JavaScript, e.g. via Selenium.

Measure — recommendation

#### Simple Scan

`owasp-dsomm#07796811-37f9-467c-9ff2-48f346e77ff3` · level 2 · depends on Defined build process (level 1) · usefulness 1 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L11853-11855 -->
> A simple scan is performed to get a security baseline. In case the test is done in under 10 minutes, it should be part of the build and deployment process.

Measure — recommendation; its sentences: R-0235

<!-- q L11847-11849 "As with static" .. "not guaranteed." -->
> As with static\nanalysis, AI-based testing complements deterministic scanners rather\nthan replacing them \u2014 results are non-deterministic and coverage is\nnot guaranteed.

R-0745 — scope (description)

Descriptive, not normative: description R-0234.

#### Usage of different roles

`owasp-dsomm#65a2d7d9-5441-46bf-a4e3-f76919857750` · level 2 · depends on Simple Scan (level 2) · usefulness 2 · difficulty knowledge 3, time 3, resources 1 · testable yes

<!-- q L11918-11918 -->
> Integration of authentication with all roles used in the service.

Measure — recommendation

<!-- q L11947-11947 -->
> For REST APIs, multiple OAuth2 scopes are used.

R-0682 — assessment

#### Coverage of hidden endpoints

`owasp-dsomm#6a9cb303-0f98-48a8-bdcd-56d41c0012b8` · level 3 · depends on Usage of different roles (level 2) · usefulness 5 · difficulty knowledge 3, time 2, resources 1 · testable yes

<!-- q L11954-11955 -->
> Hidden endpoints are getting detected and included in the vulnerability scan.

Measure — recommendation

#### Coverage of more input vectors

`owasp-dsomm#5e0ff85b-ec89-4ef0-96b1-5695fa0025dc` · level 3 · depends on Usage of different roles (level 2) · usefulness 4 · difficulty knowledge 5, time 5, resources 1 · testable yes

<!-- q L12007-12008 -->
> Special parameter and special encodings are defined, so that they get fuzzed by the used vulnerability scanners.

Measure — recommendation

#### Coverage of sequential operations

`owasp-dsomm#845f06ec-148c-4c67-9755-7041911dcca5` · level 3 · depends on Usage of different roles (level 2) · usefulness 5 · difficulty knowledge 3, time 3, resources 1 · testable yes

<!-- q L12043-12044 -->
> Sequential operations are defined and checked by the vulnerability scanner in the defined order.

Measure — recommendation

#### Usage of multiple scanners

`owasp-dsomm#5b5a1eb2-113f-41fb-a3d6-06af4fdc9cea` · level 4 · depends on Usage of different roles (level 2) · usefulness 1 · difficulty knowledge 3, time 3, resources 5 · testable partial

<!-- q L12076-12077 -->
> Usage of multiple spiders and scanner enhance the coverage and the vulnerabilities.

Measure — recommendation

#### Coverage analysis

`owasp-dsomm#d0ba0be5-c573-405f-b905-b7a8f87a9cc7` · level 5 · usefulness 4 · difficulty knowledge 4, time 5, resources 3 · testable yes

<!-- q L12112-12112 -->
> Check that there are no missing paths in the application with coverage-tools.

Measure — recommendation

#### Coverage of service to service communication

`owasp-dsomm#22aab0ef-76ce-4b8c-979c-3699784330db` · level 5 · depends on Simple Scan (level 2) · usefulness 3 · difficulty knowledge 4, time 5, resources 2 · testable yes

<!-- q L12148-12148 -->
> Service to service communication is dumped and checked.

Measure — recommendation

### Test and Verification / Dynamic depth for infrastructure

7 activities, levels 2: 3, 3: 2, 4: 1, 5: 1.

#### Test for exposed services

`owasp-dsomm#a6c4cefb-a0b7-4787-8cc7-a0f96b4b00d8` · level 2 · depends on Isolated networks for virtual environments (level 2) · usefulness 2 · difficulty knowledge 1, time 1, resources 2 · testable yes

<!-- q L12185-12188 -->
> With the help of tools the network configuration of unintentional exposed cluster(s) are tested. To identify clusters, all subdomains might need to be identified with a tool like OWASP Amass to perform port scans based o the result.

Measure — recommendation; its sentences: R-0683 permission

#### Test network segmentation

`owasp-dsomm#6d2c3ac6-8afc-4af6-a5e9-6188341aca01` · level 2 · depends on Isolated networks for virtual environments (level 2) · usefulness 3 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L12226-12227 -->
> Cluster internal test needs to be performed. Integration of fine granulated network segmentation (also between pods in the same namespace).

Measure — recommendation; its sentences: R-0684

#### Test of the configuration of cloud environments

`owasp-dsomm#7bb70764-9392-4462-935d-e55b2e148199` · level 2 · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable partial

<!-- q L12261-12262 -->
> With the help of tools the configuration of virtual environments are tested.

Measure — recommendation

#### Test for unauthorized installation

`owasp-dsomm#dccf1949-b9a8-4ce8-b992-6a4a7f3a623a` · level 3 · depends on Evaluation of the trust of used components (level 2) · usefulness 3 · difficulty knowledge 2, time 1, resources 1 · testable yes

<!-- q L12307-12309 -->
> Components must be whitelisted. Regular scans on the docker infrastructure (e.g. cluster) need to be performed, to verify that only standardized base images are used.

Measure — recommendation; its sentences: R-0236, R-0685

#### Weak password test

`owasp-dsomm#61e10f9c-e126-4ffa-af12-fdbe0d0a831f` · level 3 · usefulness 1 · difficulty knowledge 2, time 1, resources 1 · testable yes

<!-- q L12341-12342 -->
> Automatic brute force attacks are performed. Specially the usage of standard accounts like 'admin' and employee user-ids is recommended.

Measure — recommendation; its sentences: R-0686

#### Load tests

`owasp-dsomm#ab5725aa-4d53-47b9-96df-c14b3fa93bcd` · level 4 · usefulness 3 · difficulty knowledge 3, time 2, resources 5 · testable yes

<!-- q L12371-12372 -->
> Load test against the production system or a production near system is performed.

Measure — recommendation

Descriptive, not normative: risk R-0237.

#### Test for unused Resources

`owasp-dsomm#6532c1fe-9d23-4228-8722-558ddabca7d4` · level 5 · usefulness 2 · difficulty knowledge 1, time 1, resources 1 · testable partial

<!-- q L12401-12401 -->
> Test for unused resources helps to identify unused resources.

Measure — recommendation

### Test and Verification / Static depth for applications

17 activities, levels 2: 4, 3: 7, 4: 2, 5: 4.

#### Exploit likelihood estimation

`owasp-dsomm#f2f0f274-c1a0-4501-92fe-7fc4452bc8ad` · level 2 · depends on Software Composition Analysis (server side) (level 2) · usefulness 4 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L12445-12445 -->
> Use CISA KEV and EPSS to prioritize vulnerabilities that are more likely to be exploited.

Measure — recommendation

<!-- q L12439-12441 "Use the likelihood of exploitation" .. "(EPSS)." -->
> Use the likelihood of exploitation by using *known exploited vulnerabilities* (CISA KEV), or prediction models such as \n*Exploit Prediction Scoring System* (EPSS).

R-0746 — recommendation (description)

Descriptive, not normative: risk R-0238.

#### Software Composition Analysis (server side)

`owasp-dsomm#d918cd44-a972-43e9-a974-eff3f4a5dcfe` · level 2 · depends on Defined build process (level 1); Inventory of production components (level 1) · usefulness 5 · difficulty knowledge 1, time 3, resources 1 · testable yes

<!-- q L12486-12487 -->
> Tests for known vulnerabilities in server side components (e.g. backend/middleware) are performed.

Measure — recommendation

<!-- q L12482-12482 -->
> Use a tool like trivy and concentrate on application related vulnerabilities.

R-0687 — recommendation (description)

<!-- q L12483-12484 -->
> At this stage, ignore vulnerabilities in container base images used in the service.

R-0688 — scope (description)

#### Test for Time to Patch

`owasp-dsomm#13af1227-3dd1-4d4f-a9e9-53deb793c18f` · level 2 · depends on Automated PRs for patches (level 1) · usefulness 3 · difficulty knowledge 1, time 1, resources 1 · testable yes

<!-- q L12563-12564 -->
> Test of the Time to Patch (e.g. based on Mean Time to Close automatic PRs) This activity is not repeated in the Sub-Dimension "Static depth for infrastructure", but it applies to infrastructure as well.

Measure — recommendation; its sentences: R-0689 scope

<!-- q L12600-12601 "Usage" .. "information." -->
> Usage of a version control platform API (e.g. github API) can be used to fetch the information.

R-0239 — permission (description)

<!-- q L12601-12602 "Consider" .. "activity." -->
> Consider that `Measure libyears` might be an alternative to this activity.

R-0690 — scope (description)

#### Test libyear

`owasp-dsomm#87b54313-fafd-4860-930f-5ef132b3e4ad` · level 2 · depends on Defined build process (level 1) · usefulness 3 · difficulty knowledge 1, time 1, resources 1 · testable yes

<!-- q L12608-12609 -->
> Test `libyear`, which provides a good insight how good patch management is.

Measure — recommendation

<!-- q L12642-12642 -->
> `libyear` can be integrated into the build process and flag or even better break the build in case the defined threshold (e.g. 30 years) is reached.

R-0240 — permission (description)

<!-- q L12643-12643 -->
> An alternative approach is to determine `libyear` based on deployed artifacts (which requires more effort in implementation).

R-0691 — permission (description)

#### API design validation

`owasp-dsomm#017d9e26-42b5-49a4-b945-9f59b308fb99` · level 3 · depends on Inventory of production components (level 1) · usefulness 3 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L12650-12652 -->
> Design contract-first APIs using an interface description language such as OpenAPI, AsyncAPI or SOAP and validate the specification using specific tools. Checks should be integrated in IDEs and CI/CD pipelines.

Measure — recommendation; its sentences: R-0241

#### Local development security checks performed

`owasp-dsomm#6e180abc-7c98-4265-b4e9-852cb91b067b` · level 3 · usefulness 4 · difficulty knowledge 2, time 1, resources 1 · testable yes

<!-- q L12700-12701 -->
> Integration of quality and linting plugins with interactive development environment (IDEs). Implement pre-commit checks to prevent secrets & other security issues being commit to source code.

Measure — recommendation

#### Software Composition Analysis (client side)

`owasp-dsomm#07fe8c4f-ae33-4409-b1b2-cf64cfccea86` · level 3 · depends on Defined build process (level 1); Inventory of production components (level 1); Exploit likelihood estimation (level 2) · usefulness 2 · difficulty knowledge 1, time 2, resources 1 · testable yes

<!-- q L12760-12761 -->
> Tests for known vulnerabilities in components via Software Composition Analysis of the frontend are performed.

Measure — recommendation

#### Static analysis for important client side components

`owasp-dsomm#e237176b-bec5-447d-a926-e37d6dd60e4b` · level 3 · depends on Defined build process (level 1); Inventory of production components (level 1) · usefulness 3 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L12821-12823 -->
> Usage of static analysis tools for important parts of the frontend are used. Static analysis uses for example string matching algorithms and/or dataflow analysis.

Measure — recommendation; its sentences: R-0692

#### Static analysis for important server side components

`owasp-dsomm#6c05c837-8c99-46e2-828b-7c903e27dba4` · level 3 · depends on Defined build process (level 1); Inventory of production components (level 1) · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L12897-12899 -->
> Usage of static analysis tools for important parts of the middleware are used. Static analysis uses for example string matching algorithms and/or dataflow analysis.

Measure — recommendation; its sentences: R-0693

Descriptive, not normative: description R-0242.

#### Test for Patch Deployment Time

`owasp-dsomm#0cb2c39a-3cec-4353-b3ab-8d70daf4c9d2` · level 3 · depends on Automated PRs for patches (level 1); Defined build process (level 1) · usefulness 3 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L12976-12977 -->
> Test of the Patch Deployment Time. This activity is not repeated in the Sub-Dimension "Static depth for infrastructure", but it applies to infrastructure as well.

Measure — recommendation; its sentences: R-0694 scope

<!-- q L13005-13006 "This" .. "well." -->
> This activity is not repeated in the Sub-Dimension "Static depth for infrastructure", but it applies to infrastructure as well.

R-0695 — scope (description)

#### Test for compromised components

`owasp-dsomm#9c776b4e-5895-4040-b63b-c74236ec71b3` · level 3 · depends on Defined build process (level 1); Software Composition Analysis (server side) (level 2) · usefulness 4 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L13023-13028 -->
> Consume dependencies exclusively through a managed artifact repository and check components against malware and compromise intelligence: block or quarantine known-compromised versions (e.g. packages affected by Shai-Hulud) at the artifact repository, enforce a cooldown period for newly published versions and react to compromise advisories by purging affected artifacts from caches and rebuilding.

Measure — recommendation

Descriptive, not normative: description R-0243; implementation R-0244.

#### Static analysis for all self written components

`owasp-dsomm#ee68331f-9b1d-4f61-844b-b2ea04753a84` · level 4 · depends on Static analysis for important client side components (level 3); Static analysis for important server side components (level 3); Inventory of production components (level 1) · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable yes

<!-- q L13089-13091 -->
> Usage of static analysis tools for all parts of the middleware and frontend. Static analysis uses for example string matching algorithms and/or dataflow analysis.

Measure — recommendation

#### Usage of multiple analyzers

`owasp-dsomm#297be001-8d94-41ee-ab29-207020d423c0` · level 4 · depends on Software Composition Analysis (server side) (level 2); Software Composition Analysis (client side) (level 3); Static analysis for all self written components (level 4) · usefulness 1 · difficulty knowledge 3, time 3, resources 5 · testable partial

<!-- q L13168-13168 -->
> Usage of multiple static tools to find more vulnerabilities.

Measure — recommendation

#### Dead code elimination

`owasp-dsomm#a8d7d1f1-fc24-49ab-8fb6-f3a03da9c61d` · level 5 · depends on Defined build process (level 1) · usefulness 1 · difficulty knowledge 1, time 1, resources 1 · testable yes

<!-- q L13200-13200 -->
> Collection of unused code and then manual removal of unused code.

Measure — recommendation

#### Exclusion of source code duplicates

`owasp-dsomm#d17dbff0-1f10-492a-b4c7-17bb59a0a711` · level 5 · depends on Defined build process (level 1) · usefulness 1 · difficulty knowledge 1, time 1, resources 1 · testable yes

<!-- q L13232-13232 -->
> Automatic Detection and manual removal of duplicates in source code.

Measure — recommendation

#### Static analysis for all components/libraries

`owasp-dsomm#f4ff841d-3b2a-45d9-853e-5ec7ecbcb054` · level 5 · depends on Static analysis for important client side components (level 3); Static analysis for important server side components (level 3); Inventory of production components (level 1) · usefulness 3 · difficulty knowledge 2, time 4, resources 2 · testable yes

<!-- q L13264-13264 -->
> Usage of a static analysis for all used components.

Measure — recommendation

#### Stylistic analysis

`owasp-dsomm#efa52cc8-6c5c-4ba2-a3d2-7164b0402f34` · level 5 · usefulness 1 · difficulty knowledge 1, time 1, resources 1 · testable yes

<!-- q L13292-13293 -->
> Analysis of compliance to style guides of the source code ensures that source code formatting rules are met (e.g. indentation, loops, ...).

Measure — recommendation (promotes C-0613)

### Test and Verification / Static depth for infrastructure

12 activities, levels 1: 2, 2: 5, 3: 2, 4: 3.

#### Test for stored secrets in build artifacts

`owasp-dsomm#d5e6303c-d5c6-4d59-b258-a3b9de38a07f` · level 1 · usefulness 2 · difficulty knowledge 2, time 1, resources 2 · testable yes

<!-- q L13351-13351 -->
> Test for secrets in container images and other artifacts

Measure — recommendation

#### Test for stored secrets in code

`owasp-dsomm#c6e3c812-56e2-41b0-ae01-b7afc41a004c` · level 1 · usefulness 2 · difficulty knowledge 2, time 1, resources 2 · testable yes

<!-- q L13387-13387 -->
> Test for secrets in code and git history

Measure — recommendation

#### Test cluster deployment resources

`owasp-dsomm#621fb6a5-5c0a-4408-826a-068868bb031b` · level 2 · usefulness 3 · difficulty knowledge 2, time 1, resources 2 · testable yes

<!-- q L13423-13424 -->
> Test the deployment configuration for virtualized environments for unsecured configurations.

Measure — recommendation

#### Test for image lifetime

`owasp-dsomm#ddfe7c3c-b7a4-4cba-9041-b044d4a34e5b` · level 2 · usefulness 2 · difficulty knowledge 2, time 1, resources 1 · testable yes

<!-- q L13458-13458 -->
> Check the image age of containers in production.

Measure — recommendation

#### Test of virtualized environments

`owasp-dsomm#58825d22-1ce6-4748-af81-0ec9956e4129` · level 2 · usefulness 3 · difficulty knowledge 2, time 1, resources 2 · testable yes

<!-- q L13497-13497 -->
> Test virtualized environments for unsecured configurations.

Measure — recommendation

#### Test the cloud configuration

`owasp-dsomm#46d6a2a8-f9dc-4c15-9fc8-1723cfecbddc` · level 2 · usefulness 4 · difficulty knowledge 2, time 2, resources 1 · testable partial

<!-- q L13538-13539 -->
> With the help of tools, the configuration of virtual environments are tested.

Measure — recommendation

#### Test the definition of virtualized environments

`owasp-dsomm#8fc3de67-7b8d-420b-8d24-f35928cfed6e` · level 2 · usefulness 3 · difficulty knowledge 2, time 1, resources 2 · testable yes

<!-- q L13575-13575 -->
> Test the definition of virtualized environments for unsecured configurations.

Measure — recommendation

<!-- q L13571-13572 -->
> For containier (images), test that the images are following best practices like distroless or non-root.

R-0696 — recommendation (description)

#### Test for malware

`owasp-dsomm#837f8f90-adc2-4e6b-9ebb-60c2ee29494d` · level 3 · usefulness 3 · difficulty knowledge 2, time 2, resources 2 · testable yes

<!-- q L13626-13627 -->
> Check for malware in components (e.g. container images, VM baseline images, libraries).

Measure — recommendation

#### Test for new image version

`owasp-dsomm#cb6321aa-0fbf-4996-9e08-05ab26ef4c1e` · level 3 · usefulness 2 · difficulty knowledge 3, time 3, resources 1 · testable yes

<!-- q L13663-13663 -->
> Check for new images of containers in production.

Measure — recommendation

#### Correlate known vulnerabilities in infrastructure with new image versions

`owasp-dsomm#7de0ae33-6538-45cd-8222-a1475647ba58` · level 4 · depends on Usage of a maximum lifetime for images (level 2) · usefulness 1 · difficulty knowledge 2, time 5, resources 4 · testable no

Measure: **none** — the source's measure field (L13690) holds a placeholder, not a measure, and is not reproduced here (kind: inferred in requirements.yaml).

#### Software Composition Analysis

`owasp-dsomm#26e1c6d5-5632-4ec7-80d2-e564b98732ad` · level 4 · usefulness 4 · difficulty knowledge 2, time 1, resources 1 · testable partial

<!-- q L13734-13734 -->
> Check for known vulnerabilities

Measure — recommendation

#### Test of infrastructure components for known vulnerabilities

`owasp-dsomm#13367d8f-e37f-4197-a610-9ffca4fde261` · level 4 · depends on Usage of a maximum lifetime for images (level 2) · usefulness 1 · difficulty knowledge 2, time 5, resources 2 · testable yes

<!-- q L13782-13786 -->
> Test for known vulnerabilities in infrastructure components. Often, the only way to respond to known vulnerabilities in operating system packages is to accept the risk and wait for a patch. As the patch needs to be applied fast when it is available, this activity depends on 'Usage of a maximum life for images'.

Measure — recommendation; its sentences: R-0697 scope

### Test and Verification / Test Intensity

5 activities, levels 1: 1, 2: 1, 3: 2, 4: 1.

#### Default settings for intensity

`owasp-dsomm#ab0a4b51-3b18-43f1-a6fc-a98e4b28453d` · level 1 · usefulness 1 · difficulty knowledge 1, time 1, resources 1 · testable yes

<!-- q L13831-13831 -->
> The intensity of the used tools are not modified to save time.

Measure — recommendation

#### Regular automated tests

`owasp-dsomm#598897a2-358e-441f-984c-e12ec4f6110a` · level 2 · usefulness 2 · difficulty knowledge 1, time 1, resources 1 · testable yes

<!-- q L13859-13860 -->
> On each push and/or at given intervals automatic security tests are performed.

Measure — recommendation

#### Deactivating of unneeded tests

`owasp-dsomm#1bd78cdd-ef11-4bb5-9b58-5af2e25fe1c5` · level 3 · usefulness 1 · difficulty knowledge 2, time 3, resources 1 · testable yes

<!-- q L13889-13891 -->
> Unneeded tests are deactivated. For example in case the service is using a Mongo database and no mysql database, the dynamic scan doesn't need to test for sql injections.

Measure — recommendation

#### High test intensity

`owasp-dsomm#2ebfc421-8c76-415c-a3b0-fa518915bd10` · level 3 · usefulness 3 · difficulty knowledge 3, time 3, resources 5 · testable yes

<!-- q L13919-13920 -->
> A deep scan with high test intensity and a low confidence threshold is performed.

Measure — recommendation

#### Creation and application of a testing concept

`owasp-dsomm#79ef8103-e1ed-4055-8df8-fd2b2015bebe` · level 4 · usefulness 2 · difficulty knowledge 3, time 3, resources 3 · testable yes

<!-- q L13947-13950 -->
> A testing concept considering the amount of time per scan/intensity is created and applied. A dynamic analysis needs more time than a static analysis. The dynamic scan, depending on the test intensity might be performed on every commit, every night, every week or once in a month.

Measure — recommendation

## Inferred (kind: inferred, our words — no quotation)

What the model never states outright but an implementer or assessor acts on. Each is in requirements.yaml with its derived_from; the text is ours.

- **R-0698** (scope; dependsOn): Implementing an activity presupposes that every activity in its dependsOn list is implemented, and so, transitively, every activity those depend on; an assessment that credits an activity checks its dependsOn activities as well.

- **R-0699** (scope; level): Reaching level n of a sub-dimension means implementing every activity of that sub-dimension at level n and below; the levels run from 1 to 5 (level 1: 29, level 2: 75, level 3: 80, level 4: 43, level 5: 24 activities, over 24 sub-dimensions).

- **R-0700** (scope; level, dependsOn): An activity presupposes no activity at a higher level than its own: dependsOn targets sit at the same level or below (205 of 206 entries). The one exception, Static and dynamic analysis of AI generated code (level 2) depending on Static analysis for important server side components (level 3), contradicts the ordering.

- **R-0701** (assessment; assessment): Where an activity has an assessment field (78 of 251 activities), each list item (201 in all) is a separate piece of evidence the assessed organisation produces for the assessor (the items open mostly with Show, Demonstrate or Present: 118, 23 and 12; the 118 sit on 117 source lines); where it has none (173 activities), the measure is the only criterion an assessment has.

- **R-0702** (scope; implementation): An implementation entry names a tool or resource that helps implement the activity (551 entries over the 180 activities whose list is not empty); using a listed tool is neither required for nor sufficient to implement the activity, whose criterion is its measure.

- **R-0703** (scope; references): A references entry maps the activity to another framework (samm2 on 251, iso27001-2017 on 243, iso27001-2022 on 251, openCRE on 251 and d3f on 12 activities); implementing the activity does not by itself establish conformance with the mapped control, and some ISO 27001 entries say the control is not covered there.

- **R-0704** (scope; uuid, dependsOn): An activity is identified by its uuid value read as an opaque string: 2 values are not RFC 4122 UUIDs (WAF medium at L9552, WAF Advanced at L9599, a UUID with a suffix), so a consumer that validates the UUID format rejects real activities; a dependsOn entry is that value, and its trailing comment is a label only.

- **R-0705** (scope; measure): Where a measure states only what a practice achieves, not the practice (22 activities), implementing the activity means carrying out the practice that the activity name and the stated effect imply; the effect alone is not an assessable criterion.

## Source defects

Found while extracting; each is a property of the source (v5.1.0, `generated/model.yaml`), checked by script against the cached bytes. Line numbers are the .txt's.

### SD-1: meta.version is not the release

The file's meta block gives version 5.0.2 (L3) and released 2026-09-17 (L4), but the record pins this file as release 5.1.0 (identifiers.git github.com/devsecopsmaturitymodel/DevSecOps-MaturityModel-data@v5.1.0; content.url https://raw.githubusercontent.com/devsecopsmaturitymodel/DevSecOps-MaturityModel-data/v5.1.0/generated/model.yaml): the meta block was not bumped for the release, so a consumer that reads the version from the data reports the wrong one.

### SD-2: an activity with no measure

Correlate known vulnerabilities in infrastructure with new image versions (L13687, Static depth for infrastructure, level 4) has the placeholder token as its measure (L13690) and as its risk (L13689); it still carries 1 dependency, 4 implementation tools and references. DSOMM v5.1.0 defines no practice for it. Its activity entry is kind: inferred and quotes nothing.

### SD-3: an assessment of placeholders

Regular security training of security champions (L6611): both assessment lines (L6616-6617) are placeholders, one the token itself and one a misspelling of it, so the activity has no usable assessment; its measure (L6614) repeats the activity name.

### SD-4: a placeholder SAMM mapping

Backup's references.samm2 (L8882) holds the placeholder token instead of a SAMM 2 practice id.

### SD-5: two ids that are not UUIDs

WAF medium (L9552); WAF Advanced (L9599): each uuid is the WAF baseline activity's UUID with a suffix (-medium, -advanced). All 251 ids are distinct, so they work as identifiers, but a consumer validating RFC 4122 format rejects both activities. Their requirements ids use the values as they are.

### SD-6: a dependency on a higher level

Static and dynamic analysis of AI generated code (level 2) depends on Static analysis for important server side components (level 3) at L3940: the only one of the 206 dependsOn entries whose target sits above its source, so level 2 of Agentic AI / Verification cannot be reached without a level-3 activity of Test and Verification.

### SD-7: prose naming activities that do not exist

Three sentences name an activity by a name no activity has (checked against all 251 names): the measure of Test of infrastructure components for known vulnerabilities (R-0697) names its dependency with a shortened name, while its dependsOn (L13794) points by uuid to Usage of a maximum lifetime for images; the description of Test for Time to Patch (R-0690) names an alternative whose only match is Test libyear; and the description of Threat modeling of AI components routes the requirements side of AI-assisted development to an activity that v5.1.0 does not contain (Threat modeling rule is the nearest in content). A delimited-span audit over the whole prose (italic, backtick and quoted spans; 146 examined, 53 naming a real activity, sub-dimension or dimension) found these three; the other non-matching spans are external document titles, quoted implementation names, file and variable names, terms and code, and one (L1210) is a real activity name split by a literal newline escape.

<!-- q L13784-13786 "As" .. "images'." -->
> As the patch needs to be applied fast when it is available, this activity depends on 'Usage of a maximum life for images'.

<!-- q L12601-12602 "Consider" .. "activity." -->
> Consider that `Measure libyears` might be an alternative to this activity.

<!-- q L1735-1738 "Passing security" .. "development_." -->
> Passing security requirements into AI-*assisted* implementation of arbitrary features is covered by _Security requirements for AI-assisted development_.

### SD-8: a truncated measure

Automated deployment of automated PRs: the measure (L5829) is one clause ending in a comma; whatever followed is missing.

<!-- q L5829-5829 -->
> After merging of an automated dependency PR, automated deployment is needed,

### SD-9: a measure that does not describe its activity

Immutable infrastructure: the measure (L9178) speaks of redundancy, not immutability; the only text that states an immutable-infrastructure practice is an implementation entry's name (L9189), extracted as a hunted entry.

<!-- q L9178-9178 -->
> Redundancies in the IT systems

### SD-10: a misplaced description

Signing of artifacts' description (L4782-4794) is about signing commits on GitHub, the subject of Signing of code (L4737), which has no description; its recommendations are extracted where they stand, under Signing of artifacts, with a note.

### SD-11: near-duplicate activities

Test of the configuration of cloud environments (L12261-12262, Dynamic depth for infrastructure) and Test the cloud configuration (L13538-13539, Static depth for infrastructure) have measures that differ by one comma and identical risks; SLA per criticality (L10822-10825) and Treatment of defects per protection requirement (L11525-11528) have near-identical measures, the second garbled. 12 groups of activities share a risk text verbatim and 1 pair a description (by script), which is mostly deliberate reuse.

### SD-12: garbled measures

Measures with a grammatical or editing defect that leaves the practice readable: A patch policy is defined (L5572-5573); Building and testing of artifacts in virtualized environments (L4604-4605); Office Hours (L6770-6771); Rolling update on deployment (L5334); Alerting (L10193); Usage of a maximum lifetime for images (L5800-5803); Conduction of advanced threat modeling (L6259-6260); Usage of encryption at rest (L9056-9057); Infrastructure as Code (L9209-9211); Pinning of artifacts (L4647). Respectively: an imperative fused with a passive; a doubled preposition; stray characters at the end; an asterisk that refers to nothing; a sentence fragment; a misspelt at least; a doubled verb; a doubled word; a doubled word; a verb that does not agree.

### SD-13: dependencies stated in prose, not in dependsOn

Number of vulnerabilities/severity and Number of vulnerabilities/severity/layer each say they depend on a security testing implementation (R-0645, R-0646) and their dependsOn lists are empty; Pinning of artifacts' comment states a patch-process precondition (R-0415) that dependsOn does not carry. A dependency graph built from dependsOn alone misses all three.

### SD-14: an assessment that checks what the measure does not say

Simple access control for systems: the measure (L8174) asks for simple authentication on internal systems; the assessment (L8176-8177) checks a yearly review of all user privileges and fewer than five admins per system.

### SD-15: one activity's comment key

Pinning of artifacts carries its note under comment (L4648) where the other activities use comments (213 activities); a consumer reading comments misses it.

### SD-16: ISO 27001 mapping notes that break off

8 references notes end mid-phrase, after may be (C-0320, C-0321, C-0347, C-0348, C-0349, C-0350, C-0353, C-0354); in C-0353 and C-0354 the be sits on a continuation line that bin/_source_text does not read (Reading notes), so those two texts end at may; prose notes and control numbers share the same lists.

## Reading notes

Not defects of the source: how the skeleton's reading of this YAML shaped some entries, so that a later pass does not mistake them for extraction errors.

- The skeleton's sentence splitter treats a word ending in al. as an abbreviation (its et al. rule), so a sentence ending in such a word is not split from the next: R-0058, C-0060, C-0086.

- In a double-quoted scalar a literal newline escape glues the next sentence onto the last token, so 21 skeleton entries and candidates carry two or more sentences (or a sentence and a list or code block): R-0024, R-0025, R-0086, R-0096, R-0141, R-0146, R-0148, R-0150, R-0166, R-0214, R-0218, R-0219, R-0226, R-0233, R-0242, C-0276, C-0356, C-0513, C-0565, C-0566, C-0592 (recounted by the verify pass, 2026-11-16, as sentence-final punctuation followed by the escape; pass 1 listed 17, one of them R-0234, which holds one sentence).

- A parenthesised word at the start of a line reads as a list marker, which cut one measure sentence in two: C-0565 ends where C-0566 begins.

- Consecutive YAML list items are one prose block, so 12 of the 24 references notes routed as informative weld two list items into one sentence (C-0287, C-0288, C-0290, C-0291, C-0293, C-0295, C-0297, C-0298, C-0306, C-0307, C-0309, C-0311); the other 12 are one list item each, and no control number is welded, because a one-word item is not prose (counted by the verify pass against the parsed YAML). The routing itself is sound: every one sits under its activity's own references key, none under a path that only happens to contain the word.

- C-0325: the skeleton's text ended with the placeholder token; this pass cut it, by script, to the label before the token, so no file carries the token. check-quotes still verifies the words that remain.

- bin/_source_text does not read the continuation line of a multi-line plain list item as prose: 5 such lines (L6682, L7050, L7056, L13605, L13612), all under references, so those notes read truncated. None holds a verbal form (checked), so the source count is unaffected, and none is binding text.

- Quoted scalars keep their quote marks and literal backslash escapes in every text, as the bytes have them; a sentence that opens or closes such a scalar carries the quote mark.

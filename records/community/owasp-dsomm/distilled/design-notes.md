---
schema: "library-distilled/v1"
id: owasp-dsomm-design-notes
record: owasp-dsomm
type: design-notes
updated: "2026-11-16"
---

# OWASP DevSecOps Maturity Model (DSOMM), data model at v5.1.0: design notes for tmodel and mofn

This note covers how DSOMM bears on `tmodel:R-041`, `tmodel:R-042` and `tmodel:R-044`, the record's `bears_on`. It also bears on `tmodel:R-018`, which no `bears_on` id names yet, and on mofn's supply-chain approvals.

- **Read against** tmodel@ddac1b9: `tmodel:ARCH-0001` and its proposal v0.2.0 §3c, `tmodel:ADR-0012`, `tmodel:ADR-0013`, `tmodel:MAP-0001` v0.2.0 with `spec/MAP-0001.yaml`, `tmodel:RPT-0013` and its object model `tmodel:RPT-0013-OM` v0.2.1, `tmodel:DL-0044`, `tmodel:DL-0046`, tmodel's `CLAUDE.md`, `spec/vectors/sdl-01-tmodel-desktop.yaml` and `spec/schema/tmodel-object-model.linkml.yaml`. Two items read mofn@7c3c731 (`ARCH-0001` v0.3.1, `ARCH-0002`). Every tmodel id is written `tmodel:…` (`docs/scope.md`, Two registers); a bare id is mofn's.
- **What DSOMM is.** A maturity model published as one YAML file: 6 dimensions, 24 sub-dimensions and 251 activities. Each activity has a `uuid`, a `level` from 1 to 5, a `measure`, a `risk`, `difficultyOfImplementation`, `usefulness`, `tags` and `references`. Some also have a `description` (122), an `assessment` (78), a `dependsOn` list (143) and `implementation` items (180). Counted by script.
- **Source.** `.cache/owasp-dsomm.txt` is the source of record, sha256 `319f86d788484f03ac70e39ad1dfb31c09b54a90c38c73abeb6dc945beb68e55`, which equals `content.sha256` and the skeleton's `source_digest`; it was recomputed in this pass. It is `generated/model.yaml` at tag v5.1.0, but its own `meta` says otherwise (open question 1).
- **How it was read.** The structure was parsed with a full YAML parser (Ruby 2.6 Psych), and every activity's path, key set and `dependsOn` list was checked against a line index of the .txt by script. All counts here come from that parse.
- **Ids.** `` `#<uuid>` `` means `owasp-dsomm#<uuid>`, the activity-level entry of `requirements.yaml`, whose text is the `measure`. A script emits every id: it selects the entry by activity name and `field: measure`, raises unless exactly one matches, and checks the id against the activity's own `uuid` in the source. `(Ln)` after a name is the activity's level.
- **tmodel already cites DSOMM.** `tmodel:RPT-0013` lists it (`research/0013-sdl-conformance/sources.md`, at the summary bar). `tmodel:RPT-0013-OM` uses it for `MaturityLevel` (findings C1 and D2), for `Activity.assessment` as a conformance criterion, for the team implementation and evidence records (residual P7), and for the dependency and reference edges. Each is taken up below.

## Adopt

### An activity is a Requirement, and its uuid is the source id

This bears on `tmodel:R-044`, `Requirement` (`tmodel:ADR-0012`) and `RequirementSource` (`tmodel:ADR-0013`).

- One `Requirement` per activity: `source_ref: library:owasp-dsomm#<uuid>`, `source_locator` the key path (for example `Culture and Organization / Design / Conduction of simple threat modeling on technical level`), `text` the measure.
- `requirement_kind` has to be set per activity, not per dimension. The hardening and access activities of the Implementation dimension are mostly properties of an application or its infrastructure (`technical`); most of the others are things a team does (`process`). The Agentic AI split is under Adapt.
- `normativity: recommended`, matching the library's activity entries, all 251 of which carry `normativity: recommendation`. DSOMM obliges no one, and which activities an adopter takes on is its own choice (the level item under Adapt).
- The `RequirementSource` is `source_ref: library:owasp-dsomm`, with the edition of open question 1.
- **The uuid outlives a rename.** DSOMM gives every activity its own id, so a citation does not depend on an activity's name or position. Two activities break the pattern (open question 5).
- **Risk is prose, not an edge.** `risk` describes the threat in words. `Requirement.addresses` takes a `ThreatInstance`, `Weakness` or `AttackPattern`, so any such link from a DSOMM activity is ours, and a `proposed` Assertion until a Review accepts it.

### DSOMM states tmodel's rule for AI-drafted threat models

This bears on `tmodel:R-018` and `tmodel:R-042`, on tmodel's `CLAUDE.md`, and on `tmodel:DL-0044` and `tmodel:DL-0046`.

- DSOMM's threat-modeling activities, 8 by name, run from level 1 to level 5. 7 of them reach `tmodel:MAP-0001` row 3 (threat modeling) through DSOMM's own SAMM references:
  - Conduction of simple threat modeling on technical level (L1, `#47419324-e263-415b-815d-e7161b6b905e`): Culture and Organization / Design; MAP-0001 row 3
  - Threat modeling rule (L2, `#1caad69c-316c-422a-a56b-04ad6f6cc306`): Agentic AI / Guidance; MAP-0001 row 2
  - Conduction of simple threat modeling on business level (L3, `#48f97f31-931c-46eb-9b3e-e2fec0cd0426`): Culture and Organization / Design; MAP-0001 row 3
  - Creation of simple abuse stories (L3, `#bacf85b6-5bc0-405d-b5ba-a5d971467cc1`): Culture and Organization / Design; MAP-0001 row 3
  - Creation of threat modeling processes and standards (L3, `#dd5ed7c1-bdbf-400f-b75f-6d3953a1a04e`): Culture and Organization / Design; MAP-0001 row 3
  - Threat modeling of AI components (L3, `#5a1cd6cd-ebd0-4e70-b314-37b8ab0b7d8d`): Agentic AI / Guidance; MAP-0001 row 3
  - Conduction of advanced threat modeling (L4, `#ae22dafd-bcd6-41ee-ba01-8b7fe6fc1ad9`): Culture and Organization / Design; MAP-0001 row 3
  - Creation of advanced abuse stories (L5, `#0a929c3e-ab9a-4206-8761-adf84b74622e`): Culture and Organization / Design; MAP-0001 row 3
- The entry activity, Conduction of simple threat modeling on technical level (L1, `#47419324-e263-415b-815d-e7161b6b905e`), warns about AI-generated threat models:

<!-- q L5959 "Be aware of the failure modes" .. "not its result." -->
> Be aware of the failure modes: a language model confidently fills gaps in an incomplete system description and produces threats for components that do not exist, and its output is non-deterministic (the same input yields different threat models). Validating an AI-generated threat model requires exactly the security expertise the tool seems to replace (see [Team Werewolves wins!](https://threatmodeling.dev/team-werewolves-wins/)). AI-generated threats are a starting point for the discussion, not its result.

  The level-4 activity, Conduction of advanced threat modeling (L4, `#ae22dafd-bcd6-41ee-ba01-8b7fe6fc1ad9`), which describes AI tools that draft and re-run threat models, repeats it:

<!-- q L6284 "The generated models require expert review" .. "require expert review" -->
> The generated models require expert review

- tmodel holds the same rule. `CLAUDE.md` forbids presenting an AI-generated threat or attack path as reviewed; `tmodel:R-018` makes nothing machine-proposed final without a human Review; the AI hook of `tmodel:DL-0044` and `tmodel:DL-0046` writes proposals only, and only a sponsor's Review accepts them. DSOMM reaches the rule independently, from practice. It supports the rule and changes nothing in it.

### Assessment items are evidence criteria; implementation items are not

This bears on `tmodel:R-042` and on `Evidence` (`tmodel:ADR-0013`).

- 78 activities have an `assessment`: all 40 of the Agentic AI dimension and 38 of the other 211. Their 201 list items are evidence criteria, and 118 of them begin with Show. Each names a work product, which becomes `Evidence`: `work_product` for a definition, policy or training material, `by_product` for a log, a scan result or a test run.
- The `tmodel:R-042` verdict proves linkage and approval, not adequacy, and the assessment text is what the reviewer reads to judge adequacy. `tmodel:RPT-0013-OM` already maps it to a conformance criterion.
- Testable is not the same as evidenced. The library rates 189 measures testable, 60 in part and 2 not (`testable`, by script), but only 78 activities say what evidence shows it.
- The other 173 activities can be judged only from their `measure`. Under finding D9 of `tmodel:RPT-0013-OM` (evidence optional on interview-mode criteria, required on gate criteria), none of them can be a gate criterion until someone writes its evidence criterion.
- **The team records are not in this file.** No key holds per-team implementation or evidence (checked by script). The `TeamImplementation` and `TeamEvidence` objects of `tmodel:RPT-0013-OM` come from DSOMM's separate implementation schema, so its residual P7 stays open (Hold).
- **Implementation items are a catalogue.** 551 items over 180 activities, 245 of them distinct, 125 reused by more than one activity, 53 tagged documentation. They are tools, frameworks and documents, not evidence and not Requirements. In tmodel they go in `SdlPractice.external_refs`. `tmodel:RPT-0013-OM` also proposes a `generated_by` edge from Evidence to the Tool that produced it (post-MVP), but the `Evidence` that `tmodel:ADR-0013` accepted has no such slot. `tmodel:RPT-0013-OM` files DSOMM's implementation items under `MitigationTemplate`, a generic, non-binding implementation example that never counts as conformance. The mapping it carries over from the source pass, a `Component` (a tool) realizing a Mitigation, fits only the few items that ship inside the product, such as a guardrail library, because in tmodel a `Component` is a deployed artifact of the product.

### D3FEND references are Mitigation catalog references

This bears on `Mitigation.catalog_ref` (core).

- 12 activities name a D3FEND technique under `references.d3f`, and `catalog_ref` already lists D3FEND as a catalogue. So the generic `Mitigation` that is `stated_as` a DSOMM activity's Requirement carries the technique: MFA (L2, `#598e9f13-1ac8-4a01-b85e-8fab93ee81de`) names Multi-factorAuthentication, Least-privilege access baseline (L2, `#d9dc7614-81fb-45a9-a1e0-e033755ddbed`) names AccessModeling.

### mofn: an approval bound to a digest cannot silently outlive a change

This bears on mofn's software supply-chain target (`ARCH-0001` §2.3.1: the `outcome` type of DV-1, SC-3), `R-M-07`, `R-M-06` and `R-O-01`.

- DSOMM's source-control approvals: Require a PR before merging (L2, `#e7598ac4-b082-4e56-b7df-e2c6b426a5e2`), Approval by reviewing any new version (L3, `#3f63bdbc-c75f-4780-a941-e6ad42e894e1`) and Dismiss stale PR approvals (L3, `#ea6f69f7-54a5-4922-ac15-a77ff0c16162`).

<!-- q L7927-7929 "Implement a policy" .. "re-approval process." -->
> Implement a policy where any commits made after a pull request has been approved automatically revoke that approval, necessitating a fresh review and re-approval process.

- In mofn an approval is a statement over a content digest (`R-M-07`), typed `outcome` (approve, changes or reject). A new commit is a new digest, so an approval of the old one cannot cover it. DSOMM's staleness rule therefore holds by construction, with no revocation step.
- For high-risk actions of AI agents, DSOMM asks for a second approver, in Human approval for irreversible AI agent actions (L4, `#cd1cb2bd-4bd6-4b9f-beaa-921fe9ea9576`):

<!-- q L3388 "high-risk ones by two independent people" .. "(four-eyes principle)." -->
> high-risk ones by two independent people (four-eyes principle).

<!-- q L3409-3419 "Require a second, independent" .. "in the audit log," -->
> Require a second, independent approver for high-risk actions, record the approver identity, the decision context and the reason in the audit log,

  That is a 2-of-n approval (`R-M-06`) with the approver's identity recorded (`R-O-01`). But AI agent attestation is motivation only for mofn (`ARCH-0001` §2.3.3), so this changes no scope.
- No open mofn decision changes. If a supply-chain profile is drafted (`ARCH-0002` P7, DEC-004), these activities name the approval types it has to express.

## Adapt

### A level selects activities; it is neither applicability nor a gate

This bears on `tmodel:R-041` and `tmodel:R-042`, and on findings C1 and D2 of `tmodel:RPT-0013-OM`.

- **Levels.** 29 at level 1, 75 at level 2, 80 at level 3, 43 at level 4, 24 at level 5, counted by script. The file never defines a level: its `meta` holds a version, a release date and a publisher, nothing more. The level texts `tmodel:RPT-0013-OM` quotes come from another file of the DSOMM application, which the library does not hold (open question 9).
- **Not applicability.** `applies_to` and `applies_to_family` say which products a Requirement binds. A DSOMM level says how mature the adopting team should be before the activity pays off. Mapping a level to `applies_to_family` would scope a requirement to teams, not products.
- **Not a gate.** Findings C1 and D2 of `tmodel:RPT-0013-OM` keep maturity levels out of gate criteria. A Gate may be `gated_by` an activity's Requirement, with its evidence; never by a team having reached a level.
- **A selection rationale.** A team's target level picks which activities it takes on: a `selects_practice` Assertion with a Review (`tmodel:ADR-0013`), with the level as the reason. `tmodel:RPT-0013-OM` proposes `MaturityLevel` and an `applies_at` edge to carry it; neither is accepted, so until then the level stays on the library entry and in the Assertion's rationale.
- **A level as a source.** `tmodel:ADR-0013` lets a `RequirementSource` be a named level, as with SLSA Build L2. For DSOMM that would be the activities at or below a level, and that set must contain every activity its members depend on. One edge breaks this: Static and dynamic analysis of AI generated code (L2, `#10362082-f48f-4218-be08-4ab78e589df0`), in Agentic AI / Verification, depends on Static analysis for important server side components (L3, `#6c05c837-8c99-46e2-828b-7c903e27dba4`), in Test and Verification / Static depth for applications (L3940). A level-2 source must either drop the first or include a level-3 activity (open question 4).
- **Assurance targets inside maturity activities.** The application-hardening ladder, App. Hardening Level 1 (50%) (L1, `#b597928e-54d6-48a5-a806-8003dcd56aab`); App. Hardening Level 1 (L2, `#cf819225-30cb-4702-8e32-60225eedc33d`); App. Hardening Level 2 (75%) (L3, `#03643ca2-03c2-472b-8e19-956bf02fe9b7`); App. Hardening Level 2 (L4, `#ffe86caf-2fec-4630-b514-2db83983984d`); App. Hardening Level 3 (L5, `#4cae98c2-4163-44ed-bb88-3c67c569533a`), sets OWASP ASVS levels with a coverage fraction:

<!-- q L7527-7531 -->
> Following frameworks like the * OWASP Application Security Verification Standard Level 2 * OWASP Mobile Application Security Verification Standard Level 2 Implement 75% of the recommendations.

  A Gate may use an ASVS level: that is product assurance, the `level-target` criterion form of `tmodel:RPT-0013-OM`. The fraction (50%, 75%, 95% to 100%) is DSOMM's own, not ASVS's, so a gate criterion would need a coverage parameter, which nothing accepted has. DSOMM also names no ASVS edition (open question 7).

### dependsOn is a prerequisite, and tmodel has no edge for it

This bears on `tmodel:R-041` and `SdlPractice` (`tmodel:ADR-0013`).

- 206 edges from 143 activities. Every target resolves to an activity, every trailing comment names its target correctly, there is no cycle, and 63 edges cross dimensions (all by script).
- None of tmodel's edges fits. A prerequisite is neither a narrower statement of the same intent (`refines`) nor a derivation (`derived_from`, `tmodel:ADR-0012`). `ProgramNode.depends_on_node` orders a program's Gates and Milestones, not practices.
- `tmodel:RPT-0013-OM` proposes the edge between Requirements. It belongs better on the practice: the prerequisite is about doing one activity before another, not about what either requires. Proposal for the open part of `tmodel:DEC-001b`: `SdlPractice.depends_on` (practice to practice), with a program check that no practice is due at an earlier node than its prerequisites.

### DSOMM as a MAP-0001 column: the one-hop join, and where it misplaces

This bears on `tmodel:R-044` and `tmodel:MAP-0001`.

- **DSOMM publishes its own SAMM mapping.** It writes SAMM ids stream-first (`O-EM-A-1`); the `owasp-samm-2` record writes them level-first (`O-EM-1-A`). Transposed, all 278 well-formed references of the 280 resolve against that record's ids; the other two are malformed (open questions 2 and 3).
- **The one-hop join.** Under `tmodel:MAP-0001`'s chaining rule, an activity is `chained` into a row when DSOMM maps it to a SAMM activity that is an anchor or direct id of that row. 144 of the 251 activities reach at least one row, across 20 rows; the most populated are row 18 (vulnerability-intake): 30, row 10 (code-review-sast): 22, row 14 (secure-defaults): 20, row 2 (security-requirements): 15, row 1 (security-training): 13, row 7 (third-party-components): 12, row 3 (threat-modeling): 11.
- **It cannot reach the AI rows.** SAMM has no AI practice, so the SAMM cells of rows 31 (AI/ML components: inventory, provenance & AI-specific threats) and 32 (AI-generated code & AI dev tools) are empty, and no Agentic AI activity lands there. 25 of the 40 land on generic rows instead: row 2: 9, row 14: 5, row 10: 4, row 1: 2, row 3: 1, row 8: 1, row 13: 1, row 15: 1, row 18: 1, row 19: 1. Some of those placements contradict the row. The 5 that reach row 14 (Secure-by-default configuration & hardening guidance) are Automated data leak detection for AI interactions (L4, `#8d5ce64e-ebf0-45ab-93cb-d592287e3023`); Protection of agent memory against poisoning (L5, `#106622af-8969-4d9b-81ad-86d8e2bfd631`); Untrusted workspace handling for AI agents (L2, `#859c71b6-110f-40a9-9c98-20e8314ebdb7`); Network isolation for AI agents (L3, `#951e6090-057b-4dc4-8b4f-18c6adcfc1ab`); Drift detection for agent instructions and guardrails (L5, `#30e29dfc-2bb8-4fe1-bc7e-b3a9ade1ee9e`).
- **So:** take the one-hop placements for the activities outside the Agentic AI dimension, with provenance `chained` and DSOMM as the publisher. Place the Agentic AI activities in rows 31 and 32 as `ours`, using the split in the next item, and record their SAMM references under `also`, not adopted.
- **ISO/IEC 27001 references mix ids and notes.** Under `iso27001-2017`, 387 of 475 items are control ids and 88 are prose notes, 4 of them saying the mapping is missing. Under `iso27001-2022` the figures are 418, 503, 85 and 14. A converter keeps only items shaped like control ids. The 2017 ids run from clause 5 to 18 of Annex A, the 2013 numbering, which EN ISO/IEC 27001:2017 republished.
- **OpenCRE references are addresses, not mappings.** 250 of the 251 are the activity's own page in OpenCRE's DSOMM catalogue: the section is its sub-dimension and the subsection its name, matching in every case (by script). Only Secure headers (L3, `#29318d60-18ce-4526-80ea-f5928e49f639`) points at a common requirement, OpenCRE id 620-421. A crosswalk through OpenCRE needs OpenCRE's own graph, which the library does not hold.

### The Agentic AI dimension covers four subjects

This bears on rows 31 and 32 of `tmodel:MAP-0001`, on `requirement_kind` (`tmodel:ADR-0012`) and on the `ai-assisted-development` practice of `spec/vectors/sdl-01-tmodel-desktop.yaml`.

- The dimension mixes AI as a development tool, AI in the product, and agents in operation. A tmodel import has to split them, because the split decides the row, the `requirement_kind` and whether the Requirement is about the team or the product. The split is ours:

  | subject (ours) | activities | MAP-0001 row (ours) | `requirement_kind` |
  |---|---|---|---|
  | AI used to build software: assistants, coding agents and their rules | 26: Static load of security rules (L1, `#51ebc877-c4fd-4b50-9305-320152242ddf`); Usage of sandboxing for AI agents (L1, `#4debe8ea-f54a-4a00-a1cb-6fad9e571a88`); AI usage policy (L2, `#a511a9a9-1b75-4dfd-8a4f-e516e8096150`); Basic data leak prevention (L2, `#dc62d384-0b9c-47d9-b7a5-9d82e53642ba`); Human review of AI generated plans (L2, `#1bd1308d-ae3b-499a-ae81-818993571f52`); Human review of AI generated specifications (L2, `#09307f26-bf34-49c2-828e-649130876978`); Instructed load of security rules (L2, `#364123db-b41c-431a-94a0-dfd8236b2daa`); Inventory of AI agents (L2, `#c1f02ad7-e97e-4c87-b827-7542793ddb0a`); Language and framework specific security rules (L2, `#ac152a8d-2628-4db1-a7d6-6d75031bb40e`); Permission management for AI agents (L2, `#4a618049-19da-4e20-b933-81f203ecd4d2`); Self-verification of AI generated changes (L2, `#63e82b31-4167-480d-a22b-baf8ef79af61`); Spec-driven development (L2, `#923a2a23-d63b-421c-926a-191d1dd5f570`); Static and dynamic analysis of AI generated code (L2, `#10362082-f48f-4218-be08-4ab78e589df0`); Threat modeling rule (L2, `#1caad69c-316c-422a-a56b-04ad6f6cc306`); Untrusted workspace handling for AI agents (L2, `#859c71b6-110f-40a9-9c98-20e8314ebdb7`); Validation of AI-suggested dependencies (L2, `#df2db3f4-bae6-448e-844e-9562a4eabc39`); Decommissioning of AI agents (L3, `#44a195ec-da9e-4fd4-be6d-a5a688852cf7`); Enforcement of guardrails outside the reach of AI agents (L3, `#c01906d5-4db2-4a9d-a692-63928ff6575c`); Evaluation of the trust of used AI components (L3, `#399c5b7f-1310-4841-89f7-16daff2fe3ef`); Human review of AI generated code (L3, `#d6bc0b7f-fd98-49fe-b66c-7c5fa70452c6`); Least privilege on external systems for AI agents (L3, `#45f722b2-25b4-472a-a743-f7207a77b5c9`); Network isolation for AI agents (L3, `#951e6090-057b-4dc4-8b4f-18c6adcfc1ab`); No verification bypass for AI generated code (L3, `#c548df0b-0964-4fad-9f98-28fcd7442011`); Security test generation with AI (L3, `#fea96e68-de10-4a62-9df0-4727f700a4a0`); Automated data leak detection for AI interactions (L4, `#8d5ce64e-ebf0-45ab-93cb-d592287e3023`); Dynamic load of security rules (L4, `#862d08a4-7299-4b2c-9d38-8fcaade66d3e`) | 32 | process |
  | AI components and their threats | 2: Threat modeling of AI components (L3, `#5a1cd6cd-ebd0-4e70-b314-37b8ab0b7d8d`); Continuous detection of compromised AI components (L4, `#db390bba-3a49-4b1f-9982-c7d79fe88ea1`) | 31 | process |
  | Security features of an AI application | 5: Rate limiting and resource budgets for AI systems (L2, `#64aef733-bfb0-4df4-95de-bcecf668605d`); Input validation for AI systems (L3, `#0012e51c-a068-4549-a4d5-d1957b52676f`); Hallucination detection for AI responses (L4, `#51a63793-c2c5-4438-bfd6-b7dee604a76d`); Secure output handling in AI applications (L4, `#24990a5e-b0e6-4e2c-b06b-4e9f0d6f7b21`); Protection of agent memory against poisoning (L5, `#106622af-8969-4d9b-81ad-86d8e2bfd631`) | none | technical |
  | Running agents: oversight in operation, wherever the agent runs | 7: Audit logging of AI agent actions (L3, `#84ba7525-857e-4849-98ba-5fada1a1454d`); Tripwires for AI agent environments (L3, `#0d617373-e48f-4bbe-9792-a1bd82b25c54`); Anomaly detection for AI agent behavior (L4, `#99049c0a-400f-4c58-986c-ab448ca8e0fc`); Human approval for irreversible AI agent actions (L4, `#cd1cb2bd-4bd6-4b9f-beaa-921fe9ea9576`); Trust boundaries between AI agents (L4, `#abe74dfd-d554-4ec5-8b94-f75d352afaaa`); Automated containment of anomalous AI agents (L5, `#3bbd6dd9-0821-426c-8a19-41737ed61459`); Drift detection for agent instructions and guardrails (L5, `#30e29dfc-2bb8-4fe1-bc7e-b3a9ade1ee9e`) | 19 at most | process, technical |

- **tmodel's own SDL example.** `sdl-01` (example data, not a conformance claim) records its `ai-assisted-development` practice (row 32) as `complete`, citing `CLAUDE.md` and the design log. Against DSOMM, that evidence speaks to review of AI output, the subject of Human review of AI generated plans (L2, `#1bd1308d-ae3b-499a-ae81-818993571f52`), Human review of AI generated specifications (L2, `#09307f26-bf34-49c2-828e-649130876978`) and Human review of AI generated code (L3, `#d6bc0b7f-fd98-49fe-b66c-7c5fa70452c6`). It shows neither of the dimension's two level-1 activities. Static load of security rules (L1, `#51ebc877-c4fd-4b50-9305-320152242ddf`) asks for secure-coding rules:

<!-- q L737-739 -->
> Define and roll out a baseline secure coding rule set for AI assistants covering topics like input validation, output encoding, parameterized queries, secret handling and usage of evaluated components (e.g. images, libraries).

  tmodel's `CLAUDE.md` is a rule file for agents, but its rules govern decisions, sources, names, worktrees and the design log; none is a secure-coding rule. Usage of sandboxing for AI agents (L1, `#4debe8ea-f54a-4a00-a1cb-6fad9e571a88`) asks for a sandbox:

<!-- q L2503-2505 -->
> Run AI agents and AI coding assistants with command execution capabilities in a dedicated, least-privilege sandbox (e.g. a container or virtual machine) which contains only the required project files and is destroyed after use.

  A git worktree, which tmodel's agents use, is not one.
- The practice `implements` no Requirement today. The first group of the table gives it 26 candidates. Two of them are close to what tmodel already does: Enforcement of guardrails outside the reach of AI agents (L3, `#c01906d5-4db2-4a9d-a692-63928ff6575c`) (the engine of `tmodel:DL-0044` refuses any proposal that carries a review or a decision key), and Human review of AI generated code (L3, `#d6bc0b7f-fd98-49fe-b66c-7c5fa70452c6`):

<!-- q L4122-4124 "AI agents must not" .. "their own pull requests." -->
> AI agents must not be able to approve or merge their own pull requests.

## Reject or hold

### Reject difficulty and usefulness as risk or as normativity

- `difficultyOfImplementation` (knowledge, time, resources, each 1 to 5) and `usefulness` (1 to 5) are on every activity. They are planning inputs for choosing what to select, and belong in a selection's rationale. They are not a `RiskScore` input (`tmodel:ADR-0006`: risk is feasibility, impact and mitigation status), and not `normativity`.

### Reject dimensions as lifecycle phases

- The 6 dimensions are topics. Finding D1 of `tmodel:RPT-0013-OM` ruled the same for SSDF practice groups: not phases, so any phase placement is ours. A DSOMM activity gets its phase from the `tmodel:MAP-0001` row it lands on (`at_phase`), where it has one.

### Hold: the team implementation and evidence records

- `tmodel:RPT-0013-OM` residual P7 asks for DSOMM's implementation schema to be cached so its team records can be checked. This record's source does not contain it. Hold until it is fetched as a source of its own.

## Open questions and source defects

### 1. Which edition is this?

- The file comes from tag v5.1.0, the library records version 5.1.0, and `tmodel:RPT-0013` cites 5.1.0. The file's own `meta` gives version 5.0.2, released 2026-09-17 (L3-4).
- A `RequirementSource.version` must say which it pins. The tag is the safer choice, because the digest was taken at the tag; the mismatch is worth reporting upstream.

### 2. Four fields hold placeholder text

These are described, never quoted, because the token they hold is one this library rejects.

- Correlate known vulnerabilities in infrastructure with new image versions (L4, `#7de0ae33-6538-45cd-8222-a1475647ba58`): its `risk` and `measure` hold only a placeholder (L13689-13690). The activity has nothing but a name, a uuid, metadata and tools, so it cannot become a Requirement with a text. The library's entry for it is `kind: inferred`, with no text.
- Backup (L2, `#5c61fd6b-8106-4c68-ac28-a8a42f1c67dc`): its `samm2` list holds a placeholder instead of a SAMM id (L8882).
- Regular security training of security champions (L2, `#f88d1b17-3d7d-4c3d-8139-ad44fc4942d4`): both `assessment` items hold placeholders, one misspelled (L6616-6617).

### 3. A malformed SAMM id, and activities with none

- Load tests (L4, `#ab5725aa-4d53-47b9-96df-c14b3fa93bcd`) references `V-RT-AB-1`, whose stream is two letters long; SAMM streams are A or B. It probably stands for both streams of that practice, and it resolves against nothing.
- 5 activities have an empty `samm2` list, so they have no SAMM hop at all: Automated deployment of automated PRs (L3, `#08f27c26-2c6a-47fe-9458-5e88f188085d`); Approval by reviewing any new version (L3, `#3f63bdbc-c75f-4780-a941-e6ad42e894e1`); Definition of a change management process (L3, `#b4193d32-3948-47e2-a326-3748c48019a1`); Test of the configuration of cloud environments (L2, `#7bb70764-9392-4462-935d-e55b2e148199`); Test for unauthorized installation (L3, `#dccf1949-b9a8-4ce8-b992-6a4a7f3a623a`).

### 4. A dependency on a higher level

- Static and dynamic analysis of AI generated code (L2, `#10362082-f48f-4218-be08-4ab78e589df0`) depends on Static analysis for important server side components (L3, `#6c05c837-8c99-46e2-828b-7c903e27dba4`) (L3940). An organization at level 2 cannot meet the first without an activity of level 3. Either the dependency or one of the levels is wrong.

### 5. Ids that are not UUIDs

- WAF medium (L4, `#f0e01814-3b88-4bd0-a3a9-f91db001d20b-medium`) and WAF Advanced (L5, `#f0e01814-3b88-4bd0-a3a9-f91db001d20b-advanced`) carry the uuid of WAF baseline (L3, `#f0e01814-3b88-4bd0-a3a9-f91db001d20b`) with a suffix appended. They are unique, but they are not UUIDs, so a converter that validates the field rejects them.

### 6. Three ways to say nothing

- An empty `implementation` appears as null (4), an empty string (5) and an empty list (60), and 2 activities have no `implementation` key (Defined decommissioning process and Security integration tests for important components).
- 154 activities carry the single tag none.
- Pinning of artifacts (L2, `#f3c4971e-9f4d-4e59-8ed0-f0bdb6262477`) uses `comment` where 213 activities use `comments`.

### 7. ASVS without an edition

- The application-hardening activities name ASVS levels but no ASVS edition, and the levels' content differs between editions. The library's ASVS record is `owasp-asvs-5`.

### 8. Two names for one reviewer

<!-- q L7166-7168 "On each new version" .. "approval given by the reviewer." -->
> On each new version (e.g. Pull Request) of source code or infrastructure components a security peer review of the changes is performed (two eyes principle) and approval given by the reviewer.

<!-- q L7179 "Peer review - four eyes principle" .. "required by ISO 27001" -->
> Peer review - four eyes principle is not explicitly required by ISO 27001

- The measure of Approval by reviewing any new version (L3, `#3f63bdbc-c75f-4780-a941-e6ad42e894e1`) says two eyes; its ISO/IEC 27001 notes say four eyes. Counted as eyes they disagree on the number of people; read as the usual four-eyes principle, both mean one reviewer besides the author. A threshold principal (`R-M-06`) names its k, so a policy has to choose one. Require a PR before merging (L2, `#e7598ac4-b082-4e56-b7df-e2c6b426a5e2`) says at least one person:

<!-- q L7753-7757 "Define source code management system policies" .. "under defined conditions." -->
> Define source code management system policies (e.g. branch protection rules, mandatory code reviews from at least one person, ...) to ensure that changes to critical branches are only possible under defined conditions.

### 9. tmodel cites what this source does not hold

- `tmodel:RPT-0013-OM` takes its level definitions and its team objects from other files of the DSOMM repository, and its implementation records from a schema not in `.cache`. Only the activity, reference, assessment and dependency objects can be checked against this record.

### 10. A state-machine guard cites an entry classed descriptive

- Guard PR-T01 in `state-machine.yaml` (the approver is not the author) lists `owasp-dsomm#R-0177` and `owasp-dsomm#R-0179` as ids. R-0177 is the goal sentence of its activity and `requirements.yaml` classes it descriptive: it binds no one and is not testable. R-0179, an assessment line, holds the testable form. Pass 2 moved descriptive entries from `constrained_by` to `related` in `protocol.yaml`, but a guard has no `related` slot, so R-0177 stayed in `ids`.
- Either guards gain a `related` list for context entries, or R-0177 comes out of PR-T01. Which one is open; neither changes the guard's meaning.

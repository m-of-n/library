---
schema: "library-distilled/v1"
id: etsi-en-304-223-design-notes
record: etsi-en-304-223
type: design-notes
updated: "2026-11-15"
---

# ETSI EN 304 223 V2.1.1: design notes for tmodel

This note covers how the EN bears on `tmodel:DEC-001` and `tmodel:R-018`, the record's `bears_on`. `tmodel:DEC-001` is now split:

- `tmodel:DEC-001a`, the core type system, is accepted (`tmodel:ADR-0010`, amended by `tmodel:ADR-0011` and by `tmodel:ADR-0012`, which put `Requirement` in the core).
- `tmodel:DEC-001b`, the governed layer, is accepted only in part (`tmodel:ADR-0013`).

It was read against tmodel@ddac1b9 (`tmodel:ARCH-0001` v0.1.11 and `spec/schema/tmodel-object-model.linkml.yaml`), and one item against mofn@10e357f. Every tmodel id is written `tmodel:…` (`docs/scope.md`, Two registers), including its reports and design logs; a bare id is mofn's.

- **What the EN is.** A process standard: 13 principles and 72 provisions, keyed `Provision 5.x.y-n[.m]`, counted by script. It defines no message, format or protocol.
- **Who already consumes it.** The `tmodel:RPT-0017` file `research/0017-requirements-extraction/etsi-en-304-223.yaml` (`tmodel:DL-0033`) holds 64 Requirements built from this record: 44 `mandatory` and 20 `recommended`.
- **Source.** `.cache/etsi-en-304-223.txt`, sha256 `b1bdc6d293fcf5583d84a7251d9b73dd45cb2350642fae35a96060b930f480e3`, which is the pinned `source_text_digest`. It renders the PDF whose sha256, `1ef542acf1fac7f108aa0b3c8548d91d82395fe026f0036bffe7f1f32456d21a`, equals `content.sha256`. Both digests were recomputed in this pass.
- **Ids.** `R-NNNN` means `etsi-en-304-223#R-NNNN`. A script emits every id from `requirements.yaml`. It selects the entries whose `source_lines` start inside the named provision, and raises unless exactly one matches.

## Adopt

### Clause 5.1.3 is the threat-modelling duty a tmodel model must carry

This bears on `tmodel:DEC-001a` and `tmodel:R-018`. The clause, sentence by sentence:

| EN | form | a threat model must carry | tmodel today |
|---|---|---|---|
| R-0022 threats analysed and risks managed | shall | threats, attack paths, risk and mitigations, per system | have: the core (`tmodel:DEC-001a`) |
| R-0023 AI-specific attacks: data poisoning, model inversion, membership inference | should | the attack classes | have: AttackPattern stubs with `catalog_ref` (NIST AI 100-2, ATLAS), as `tmodel:RPT-0017` does |
| R-0023 regular reviews and updates | should | when each review happened | gap: `Review` has no date slot (`tmodel:ADR-0010`), and `ThreatModel.revision` is `tmodel:DEC-001b`, still open |
| R-0024 threat modelling re-run when a setting or configuration option is added or changed, at any lifecycle stage | shall | a sign-off tied to the configuration it covered | gap: `ThreatModel.approval_digest` is `tmodel:DEC-001b`, still open |
| R-0025 risk from functionality the system does not use, such as a multi-modal model used for one modality | shall | a model component's capabilities, compared with those the system uses | gap: no slot; `tmodel:RPT-0014` proposes capability edges on components |
| R-0026 controls the System Operator chooses, weighing their cost against its risk tolerance | shall | the treatment decision and its grounds | partial: `accepted_risk` and `Review.justification` record the outcome; `tmodel:ADR-0006` has no input for cost or tolerance |
| R-0027 R-0028 R-0029 threats the Developer cannot resolve, passed to the System Operator and on to End-users, with the risks, impacts and recommended actions | shall, shall, should | a threat hand-off between Parties: ThreatInstance, DamageScenario and Mitigation, attributed with `asserted_by` and mapped onto the receiver's product | partial: export per `tmodel:ADR-0007`; mapping onto the product is `tmodel:DEC-009` (open) and `tmodel:R-020` |
| R-0030 a risk held by an external party, for which the System Operator obtains assurance | should | who holds the risk, and the evidence | partial: `Mitigation.implementation_owner`; the evidence edge is blocker C1 of `tmodel:ADR-0010`, held in `tmodel:DEC-001b` |
| R-0031 monitoring against risk appetite, with risk left over | should | the remaining risk shown beside the mitigation state | have: mitigation status is a peer of derived risk (`tmodel:ADR-0006`) |

The clause also states that the risk left over is significant:

<!-- q L613-614 "It is important" .. "against them." -->
> It is important to recognize that a higher level of risk will remain in AI systems despite the application of controls to mitigate against them.

Two further points:

- Other risk-assessment duties land on the same objects. They apply before building (R-0012), to each external component (R-0017), to each permission the AI system holds on other systems (R-0020), and to each poorly documented model or component (R-0055).
- The EN defines threat modelling as a design and development activity (open question 6), but its provisions apply it later too. tmodel should leave `applies_in_phase` open over every phase.

### Clause 5.1.4, human oversight, is the EN's statement of `tmodel:R-018`

This bears on `tmodel:R-018`, on A-007 and A-045 of `tmodel:APP-0001`, and on `tmodel:DEC-001b`.

- R-0034 (shall) covers human oversight used as a risk control. The provision requires its technical measures to be designed, developed, **verified** and maintained.
- tmodel's review gate is that kind of control: human oversight over machine proposals. Under the EN, verifying the gate is therefore part of the duty.
- Part of the gate is mechanized already: the `check.py` of `tmodel:RPT-0017` fails any `accepted` Assertion that lacks a Review by a person. SR-Q3 of `tmodel:RPT-0016` asks for the same check across the whole model. That gate sits in `tmodel:DEC-001b`, which is held pending the critique fixes of `tmodel:DL-0020`. This provision supports building it, with a test vector the gate must reject.
- R-0033 (should) asks that outputs be easy for a person to assess. tmodel does this with the `Basis:` rule that `tmodel:RPT-0017` applies to every proposed Assertion, and A-007 asks the same of the UI.
- R-0032 (should) asks for oversight capabilities to be designed in and maintained.
- R-0086 (shall) logs system and user actions, and R-0065 (should) logs changes to system prompts. tmodel's counterparts are:
  - Assertion provenance: `asserted_by`, `asserted_at` and `generated_by` (`tmodel:ADR-0011`);
  - the design-log entry that tmodel's `CLAUDE.md` requires of any agent writing specification, schema, mappings or vectors; `tmodel:DL-0033` also records its prompt.
- For tmodel's own AI hook, see the last item under Reject or hold.

### Training data and models are both Assets and Components

This answers G10 and open question 2 of `tmodel:RPT-0009` (`tmodel:DEC-001a`; Asset and Component per `tmodel:ADR-0011`).

- **The EN treats them as assets.** R-0090 calls training data and models assets. They also fall under:
  - the asset inventory (R-0037);
  - asset tracking and version control (R-0038);
  - protection of confidential training data and weights (R-0044).
- **The EN also treats them as components.** R-0062 calls them model components and requires hashes for them.
- So model each one as an `Asset` (with `security_properties`, `owned_by` and `stored_in`) held in a `Component` of kind `machine_learning_model` or `data`, with the digest in `identifiers`.
- The inventory in R-0037 includes interdependencies. In tmodel that is the composition graph (`depends_on`, `uses_component` and `DataFlow`), shown as a View (`tmodel:R-001`).

### The EN is a RequirementSource

This bears on `tmodel:ADR-0013` and `tmodel:ADR-0012`. The source is `source_ref: library:etsi-en-304-223` at `version: V2.1.1`, with the Requirements as its `source_members`.

The scope states one inclusion and one exclusion:

<!-- q L226-227 "The present document includes" .. "generative AI." -->
> The present document includes in its scope systems that incorporate deep neural networks, such as generative AI.

<!-- q L230-231 "The present document is not designed" .. "deployed)." -->
> The present document is not designed for academics who are creating and testing AI systems only for research purposes (AI systems which are not going to be deployed).

`tmodel:DL-0033` set no `applies_to_family`. The inclusion narrows nothing; the research-only exclusion is the one rule that does. It can become a family value once `tmodel:DEC-009` names AI systems.

### mofn: provision 5.2.4-1.2 is an artifact statement

R-0062 bears on mofn's `R-M-07`, `R-M-11` and `R-O-01` (`spec/ARCH-0001-authorization-attestation.md@10e357f`):

<!-- q L745-746 -->
> Provision 5.2.4-1.2 Developers shall release cryptographic hashes for model components that are made available to other stakeholders to allow them to verify the authenticity of the components.

- The released digest is what `R-M-07` and `R-M-11` bind. A statement that binds it and is signed with the Developer's key (`R-O-01`) gives the authenticity the provision promises.
- **The EN stops short of that.** A hash shows only that a component matches the hash. It shows origin only if the hash itself arrives authenticated, and the provision does not say how it should. The provision treats integrity as if it were authenticity.
- This supports mofn's premise that a signature is what adds origin. It does not narrow any mofn decision.

## Adapt

### Normativity belongs to the sentence, not the provision

This bears on `normativity` in `tmodel:ADR-0012`, and on `tmodel:RPT-0017` and `tmodel:DL-0033`.

- 4 provisions mix shall and should: 5.1.2-7, 5.1.3-1, 5.1.3-2 and 5.2.4-1. The count comes from the directives regex over all 72 provision spans.
- `tmodel:RPT-0017` gives each of the four one `mandatory` Requirement, whose paraphrase includes the should part. As a result it marks as mandatory four things the EN only recommends:
  - that the provider follows the EN (R-0108, the should half of R-0021);
  - regular review, and coverage of AI-specific attacks (R-0023);
  - what the threat hand-off contains (R-0029);
  - making the documentation available (R-0060).
- **Naming AI-specific attacks in the threat model is only a recommendation in the EN.** Provision 5.1.3-1 requires only that threats are analysed and risks managed (R-0022); its AI-specific attacks are the should of R-0023. The clause's other requirements do not name them either: threat modelling on a setting or configuration change (R-0024), the risk of superfluous model functionality (R-0025), and passing unresolved threats on (R-0111).
- Fix: one tmodel Requirement per leaf entry, each citing its R-id, grouped with `refines`. A leaf is a sentence, or a split child where one sentence carries both forms: R-0021 is one sentence with a shall (R-0107) and a should (R-0108), so a Requirement per sentence would still mix them. A single `normativity` value cannot describe a provision, or a sentence, that mixes the two.
- `conditional` mixes two separate things, strength and condition. 17 provisions are conditional. The regex looked for an opening `Where` or `If`, and for `If the Developer is an external entity`, `where possible`, `Where available` and `In this case`.
  - A conditional shall is mandatory once its condition holds. So keep `normativity` for strength, and put the condition in the text.
  - The converter of `tmodel:RPT-0017` already refuses to map a condition to `conditional`.

### Stakeholder roles become a typed actor model

This answers G8 and open question 3 of `tmodel:RPT-0009`. It bears on `Party` in `tmodel:DEC-001a`; `tmodel:ADR-0012` has no slot for the party a Requirement obliges.

Roles are relations, not kinds. R-0001 (can) lets one entity hold several roles, and Table 4-1 gives an example:

<!-- q L453-458 "For context" .. "System Operator." -->
> For context, a business or organization that creates an AI model and who is also responsible for embedding/deploying that model/system in their organization are defined in the present document to be both a Developer and a System Operator.

So a role is an edge between a Party and the system it plays that role for, not a `PartyKind`. tmodel's schema already makes party roles edges (`manufactured_by`, `supplied_by`, `owned_by`), not classifications.

**Who is obliged.** This note read each of the 85 binding sentences in clause 5 and recorded the party it obliges; a script counted them. A sentence naming two roles counts for both:

- Developer 50, System Operator 43, Data Custodian 5, End-user 1 (R-0041), Affected entity 0.
- Organizations 4, a party Table 4-1 does not define: R-0006, R-0008, R-0011 and R-0019.
- No stated party: 14, each passive or with a work product as its subject. SD-15 of `normative.md` lists the same 14 at leaf level, so it names R-0111 where this count has its sentence R-0027.

**Each, or whoever acts.** 7 sentences oblige whichever of the Developer or System Operator performs the act: R-0012, R-0017, R-0021, R-0032, R-0034, R-0090 and R-0092. Another 20 oblige each of several roles. A slot that lists roles cannot tell these two cases apart. It needs the set of roles plus a quantifier: each, or whoever performs the act.

**Proposal.**

- Add `Requirement.obliges`, a role from {developer, system_operator, data_custodian, end_user}, with its quantifier.
- The nearest existing edges express a different relation. Developer is close to `manufactured_by`, and Data Custodian to `owned_by` on a data Asset. System Operator and End-user have no edge.
- Affected entities are never obliged. They are the people and systems that suffer the impact, so they belong in DamageScenario and ImpactVector, and in `RiskScore.for_stakeholder` (open question 2).
- The lower-case developers in R-0011 are staff, not the Developer role.
- The EN maps its roles to AI Act roles only with can (R-0004, R-0005). That is a conditional crosswalk, never an identity.

### Prompts are a third kind of AI asset

This bears on `ComponentKind` in `tmodel:DEC-001a`, and on G6 of `tmodel:RPT-0009`.

- The EN lists models, datasets and prompts together (R-0016, and Principle 8's title).
- It asks for a record of every change to system prompts and model configuration (R-0065).
- `ComponentKind` has no value for a prompt or a configuration. Until G6 adds AI component kinds, model a system prompt as an `Asset` (integrity) `stored_in` the Component that serves it.

### The EN's lifecycle phases fit `LifecyclePhaseCode`, except ownership transfer

This bears on `LifecyclePhaseCode` in `tmodel:DEC-001a`, and on `tmodel:DEC-009`.

- The EN's five phases map onto tmodel's codes as follows:

  | EN phase | `LifecyclePhaseCode` |
  |---|---|
  | design | concept, architecture, design |
  | development | implementation, verification_validation |
  | deployment | deployment |
  | maintenance | operation, maintenance |
  | end of life | end_of_support, decommission |

- R-0090 places transfer or sharing of ownership of training data or a model in end of life, with the Data Custodian involved. That is the returns and resale branch whose codes `LifecyclePhaseCode` defers. Add it when that branch is built.
- R-0084 treats a major update as a new model version. In tmodel that is a new ProductInstance, with its own test evidence.

### Conformance testability

This bears on `conformance_status` in `tmodel:DEC-001b` (the proposed `tmodel:R-042`), and on Evidence per `tmodel:ADR-0013`.

This note sorted each of the 72 provisions into three kinds, and a script counted them: 13 artifact checks, 10 system properties and 49 attestations.

**Artifact checks** name an artifact and a property of it that a script or a fixed test can decide. 9 use shall and 4 use should:

- R-0062: the released hashes. Recompute each one and compare; nothing is left to judgement.
- R-0064: the source URL and date/time for each item of training data.
- R-0063: how public training data was obtained, its origin, and its use in the model.
- R-0061: the listed documentation fields.
- R-0065: the log of prompt and configuration changes, checked against the configuration history.
- R-0086: system and user actions are logged.
- R-0015: the audit trail covers every model, dataset and prompt in the inventory.
- R-0037: an inventory that includes interdependencies.
- R-0040: a restore test.
- R-0046: the rate limit the provision gives as its example.
- R-0047: separate environments, and where training data is kept.
- R-0050: a published vulnerability disclosure policy.
- R-0077: guidance that names limitations and failure modes.

**System properties** can be tested only by security testing, and the EN gives no pass criterion: R-0014, R-0020, R-0032, R-0033, R-0034, R-0041, R-0042, R-0044, R-0071 and R-0072.

**Attestations** are all the rest: training, assessment, threat modelling, testing, monitoring, communication and disposal.

How tmodel can carry each kind:

- The accepted carrier is an `SdlPractice` that `implements` the Requirement and `produces` Evidence.
  - An artifact check can be discharged by `by_product` Evidence that the check itself emits, with its `digest`.
  - An attestation needs `work_product` Evidence plus a Review.
- The `tmodel:R-042` verdict proves linkage and approval, not adequacy. It stays in `tmodel:DEC-001b`, behind blocker C1 of `tmodel:ADR-0010`.

21 of the 72 provisions use a qualifier the EN never quantifies (found by script). The words searched were: thorough, appropriate, comprehensive, proportionate, clear, accessible, regularly, substantial, major, where possible, as required, detailed, continuously, proactively, all necessary and well-documented. *Accessible* alone occurs in 6 provisions and is never defined. These remain human judgements, even within an artifact check: for example, comprehensive in R-0037.

## Reject or hold

### Reject `Primarily applies to` as an applicability filter

This bears on the obliged-party slot proposed above, and on `tmodel:DEC-001b`. The EN itself calls the line an indication:

<!-- q L433-434 "An indication" .. "implementation." -->
> An indication is given for each principle on which stakeholders are primarily responsible for its implementation.

The line is unreliable as a filter:

- **It is missing for Principle 10.** There are 12 such lines for 13 principles. Principle 10's 8 binding sentences, R-0073 to R-0080, have no fallback.
- **It is too narrow.** Principle 2 (5.1.2) omits Data Custodians, though R-0018 obliges them with shall. Principle 5 (5.2.1) omits End-users, though R-0041 obliges them.
- **It is too wide.** Principle 7 (5.2.3) lists Data Custodians, but none of its sentences names them. Principle 1 (5.1.1) lists three roles, but each of its sentences obliges either Organizations or no one.
- **It has no open-source criterion.** The open-source exception never says which provisions it relaxes, and its one pointer leads nowhere (open question 4):

<!-- q L443-444 "Some provisions for" .. "open-source models." -->
> Some provisions for Developers in the present document are less applicable to AI systems involving open-source models.

Instead, take the obliged role from each sentence. Use the principle line, where there is one, only as the default for the 4 sentences that oblige Organizations and the 14 that name no party.

### Reject reading should as mandatory

See the normativity item under Adapt.

### Hold: do not derive a conformance score from the EN

The EN has no conformance clause. The word conformance occurs only in the boilerplate on informative references (L262) and in the title of [i.4] (L275). The EN defines no levels, classes or scores, and leaves evaluation to TS 104 216:

<!-- q L214-215 -->
> ETSI TS 104 216 [i.4] provides guidance on how to evaluate and validate AI systems in accordance with the provisions of the present document.

- The library has no record for [i.4]. ETSI's deliver directory for TS 104 216 returned 404 on 2026-11-15, as `tmodel:DL-0006` had also found.
- Keep `RequirementConformanceStatus` as it is, and ingest TS 104 216 once it is published.

### Hold: TR 104 128 [i.1] is guidance

<!-- q L212 -->
> Information on the AI lifecycle and implementation examples are given in ETSI TR 104 128 [i.1].

<!-- q L261-262 -->
> The following referenced documents may be useful in implementing an ETSI deliverable or add to the reader's understanding, but are not required for conformance to the present document.

- TR 104 128 is published: ETSI's deliver directory lists version 01.01.01_60. The library has no record for it.
- `tmodel:RPT-0009` reads its clause 6 for prompt-injection examples on 15 provisions. Any `addresses` link that rests on the guide stays `inferred`, never `stated`.

### Hold: the EN does not bind tmodel's own AI hook today

- Under `tmodel:DL-0044` the app holds no model and no API key; the agent runs outside it. So tmodel holds no Table 4-1 role for the hook.
- Clause 5.1.4 and R-0086 are therefore design guidance for `tmodel:R-018` (see Adopt, human oversight). They become obligations only if tmodel embeds a model.
- This narrows §7 of `tmodel:RPT-0009`, which applies those provisions to tmodel's own AI features.

## Open questions and source defects

### 1. tmodel's ids resolve; its converter would now duplicate every obligation

[Rewritten by the verify pass, 2026-11-15. As first written this item said the branch kept 0 designator ids and resolved 0 of tmodel's 64 citations. That was true of the skeleton file this note was read against; the requirements lane then restored the 72 provision ids, which made it false.]

- On `main`, `requirements.yaml` is `library-requirements/v2`: 72 ids keyed by ETSI's designator, for example `etsi-en-304-223#5.1.3-1`.
- This branch writes `library-requirements/v1` with 212 entries. The 72 designator ids are kept, one provision-level entry each, carrying `designator`, `normativity` and `verb`; their texts equal `main`'s apart from the added `Provision <designator>` label. The other 140 entries are `R-NNNN` ids: sentences, split children, scope and applicability lines, and inferred entries.
- The `tmodel:RPT-0017` file cites 64 distinct `library:etsi-en-304-223#<designator>` ids, and all 64 resolve on this branch (checked by script).
- The `convert.py` of `tmodel:RPT-0017` (tmodel@ddac1b9) was re-run on this branch's record. It warns that the file is not v2, then converts 167 of the 212 entries: the 72 provisions, plus 95 `R-` entries whose `normativity` is requirement or recommendation. Those 95 are the sentences and their split children, so each obligation comes out two or three times. The 45 skipped entries are the possibility, applicability, convention and inferred ones.
- With `--only 5.` it converts exactly the 72 provisions. Their names are still left as bare designators marked for review, and every `requirement_kind` defaults to `other`, because `short_title` and `nature` (on all 72 entries at `main`) are not on this branch.
- The existing `tmodel:RPT-0017` file needs no change: its ids resolve. A re-conversion should pass `--only 5.`, or read the provision-level entries only. This note cites R-ids, which stay valid alongside the designators.

### 2. Table 4-1 defines Affected entities as the opposite of their name

<!-- q L504-508 "Encompasses" .. "application." -->
> Encompasses all individuals and technologies, such as apps and autonomous systems, that are not directly affected by AI systems or decisions based on the output of AI systems. These individuals do not necessarily interact with the deployed system or application.

- Read literally, this covers everyone who is *not* directly affected. But R-0079 asks Developers and System Operators to support Affected Entities through an incident, which assumes they are affected.
- The second sentence suggests the intent: affected, but not necessarily interacting with the system. tmodel should model them as the people and systems that suffer the impact (see the actor model under Adapt), not by the literal definition.

### 3. The voluntary Code refers to nothing

<!-- q L491-494 "This stakeholder group has been created" .. "end-users." -->
> This stakeholder group has been created because the voluntary Code has placed expectations on Developers, System Operators and Data custodians to help inform and protect end-users.

- The row cites nothing; Table 4-1's only citations are to [i.2], at L460 and L472. The only other Code in the document is in the title of [i.21].
- It reads as left over from the text the EN was drafted from, not as a reference.

### 4. Two cross-references in 5.2.1 lead nowhere

<!-- q L663-664 "(see clause 5.2.3" .. "securing data)" -->
> (see clause 5.2.3 for details on securing data)

- This is in R-0041. Clause 5.2.3 is the supply-chain principle, and in L708-731 the word `data` occurs only in its applicability line.

<!-- q L668-669 "See clause 5.2.2" .. "open source." -->
> See clause 5.2.2 for relevant provisions for open source.

- This is the last sentence of provision 5.2.1-4.1, after R-0043. It has no verbal form, so no requirement entry holds it. Clause 5.2.2 never mentions open source: L675-707 contains no `open`.

### 5. Not every principle has references

The Introduction promises them for each principle:

<!-- q L196-197 "Relevant standards" .. "present document." -->
> Relevant standards and publications are signposted at the start of each principle to highlight links between the various documents and the present document.

- There are 11 References lines for 13 principles; Principles 10 and 13 have none.
- Principle 10 also has no applicability line. It has a NOTE in its place.

### 6. The definition of threat modelling is narrower than the provisions that require it

<!-- q L405-406 -->
> threat modelling: process to identify and address potential security threats to a system during its design and development phases

- R-0024 requires threat modelling at any stage of the lifecycle.
- R-0027 has System Operators threat-model their own systems. Table 4-1 makes them the party that deploys and maintains a system, so this is not confined to design and development.

### 7. Some terms are named but never defined

- §3.1 defines data poisoning, model inversion and adversarial attack.
- It does not define membership inference (L592, its only occurrence), model obfuscation (L187, its only occurrence) or indirect prompt injection (L187-188). The second is open question 1 of `tmodel:RPT-0009`.
- Risk tolerance (R-0026) and risk appetite (R-0031) are two undefined terms, possibly for the same threshold. Both bear on `tmodel:ADR-0006`.

### 8. Transfer, or disposal?

<!-- q L865-866 "transfer or share ownership" .. "these assets." -->
> transfer or share ownership of training data and/or a model to another entity they shall involve Data Custodians and securely dispose of these assets.

- Disposing of an asset that is being transferred or shared only makes sense for the copies the transferring party keeps. R-0090 does not say which is meant.
- This matters for the lifecycle event (see the lifecycle item under Adapt).

### 9. Numbering does not imply refinement

- Provision 5.1.2-5.1 (R-0019: Organizations encourage staff to report risks) sits under 5.1.2-5 (R-0018: Data Custodians match intended use to data sensitivity), yet the two share no subject.
- Provision 5.2.3-2.1 (R-0055) adds Developers to its parent 5.2.3-2 (R-0054), which obliges only System Operators.
- So do not derive `refines` from the numbering alone. `tmodel:DL-0033` already proposes such a link only where the child narrows the parent.
- R-0049 states an obligation inside a because-clause. A paraphrase can easily drop it; `tmodel:RPT-0017` keeps it.

### 10. Related documents have no library record

- TR 104 128 [i.1], TS 104 216 [i.4] and the predecessor TS 104 223 have no record, and `relations.supersedes` is empty. The History table names the predecessor:

<!-- q L882 -->
> V1.1.1 April 2025 Publication as ETSI TS 104 223

- `tmodel:DL-0006` records stubs for TR 104 128 and TS 104 223, and a `supersedes` link, all made in Threat-Radar/library#40. None of them is in this library: `records/`, `topics/` and `git log -S` were searched.

### 11. Checked, nothing found

A script over the rendering found 72 provision keys and 13 principles, numbered 1 to 13. There is no duplicate key and no gap in any sequence, and every sub-provision comes after its parent.

### 12. Pass 3 joins: what the artifacts do not yet agree on

These are differences between our own artifacts, found by script in the cross-check. None is a source defect.

- `requirements.yaml` `field` names a record for 5.1.4-3 (R-0034), 5.1.4-4 (R-0035) and 5.2.3-1 (R-0053), and a re-run for 5.2.1-4.1 (R-0043), while `messages.yaml` `considered_not_structures` lists those provisions as having no record content defined. The EN requires the measures, the verification and the processes, and names no record of them, so the `field` wording reads more into the provisions than the messages do. The `field` text is left as pass 1 wrote it; a reader building on these four should take the `considered_not_structures` reason.
- Thirteen inferred entries (R-0128 to R-0140) have a `field` but no field of any structure cites them. Each rests on stated entries named in its `derived_from`, and the structures cite those; an inferred ordering or actor rule adds no work product of its own. R-0138 (a defined list of prohibited uses) and R-0139 (the specification 5.1.4-4 verifies against) are the two that name a thing a reader might look for: `EndUserGuidance.prohibited_use_cases` holds the first; nothing holds the second (protocol work product `DataSecurityControls`, structure none).
- `protocol.yaml` `work_products` is its own vocabulary and only 5 names equal a `messages.yaml` structure name. Each work product now carries `structure` or `structure_reason` (58 mapped, 22 none).


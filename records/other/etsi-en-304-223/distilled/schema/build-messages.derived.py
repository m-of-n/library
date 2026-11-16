#!/usr/bin/env python3
"""Build distilled/messages.yaml for ETSI EN 304 223 from the spec below.

Run:  python3 -I schema/build-messages.derived.py   (from the distilled/ dir)

The spec is OUR derivation of the work products the EN's provisions require.
Every constrained_by id is resolved from requirements.yaml by a selector
("5.2.4-1" or "5.2.4-1::substring"); a selector matching 0 or >1 requirements
raises. The requirement ids are never typed here.

Selector rules: only LEAF sentence entries are candidates: an id R-NNNN,
kind stated, with no split_into. A provision-level entry (#5.x.y-n) and a
sentence split into children are never selected, so every field cites the one
entry that holds its verbal form (verify pass, 2026-11-15: the provision-level
entries added by the requirements lane made every earlier selector match 2
entries, the sentence and its provision, and the file could no longer be rebuilt).
The requirement's locator must be '§<clause>' (clause = the part of the key
before '-'). Without '::' the requirement text must start with
'Provision <key> ' (the first sentence of a provision, when it is not split).
With '::substr' the text must contain substr (continuation sentences, and the
split children of a provision's first sentence).

considered_not_structures cites the provision-level entry #<key> itself.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.dirname(HERE)
REPO = os.path.abspath(os.path.join(DIST, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "bin"))
import _yaml  # noqa: E402

REQS = _yaml.parse(open(os.path.join(DIST, "requirements.yaml")).read())["requirements"]
LEAVES = [r for r in REQS if str(r["id"]).split("#")[-1].startswith("R-")
          and r.get("kind") == "stated" and not r.get("split_into")]


def resolve(sel):
    key, _, sub = sel.partition("::")
    clause = key.split("-")[0]
    hits = [r for r in LEAVES if r["locator"] == "§" + clause
            and ((sub in r["text"]) if sub else r["text"].startswith("Provision %s " % key))]
    if len(hits) != 1:
        raise SystemExit("selector %r matched %d requirements" % (sel, len(hits)))
    return hits[0]["id"]


def resolve_provision(key):
    hits = [r for r in REQS if str(r["id"]).split("#")[-1] == key]
    if len(hits) != 1:
        raise SystemExit("provision %r matched %d entries" % (key, len(hits)))
    return hits[0]["id"]


USED = set()


def F(name, typ, ob, sels, desc, cond=None, reason=None, items=None, values=None, with_field=None):
    assert ob in ("shall", "should", "can", "inferred"), name
    assert sels, name
    if ob == "inferred":
        assert reason, name
    else:
        assert not reason, name
    if with_field:
        assert cond, name   # required only alongside with_field, so never unconditionally
    for s in sels:
        USED.add(s.split("::")[0])
    return dict(name=name, type=typ, obligation=ob, sels=sels, desc=desc,
                cond=cond, reason=reason, items=items, values=values, with_field=with_field)


AS = "array<string>"
AO = "array<object>"
DT = "date-time"
INF_ACC = "the provision requires an accessible way of conveying this; the source defines no format"

S = []


def M(name, producer, desc, fields, plans=None, any_of=None):
    # any_of: groups of conditional fields, at least one group of which a record
    # must carry (the structure covers several cases, each under its own condition).
    names = {f["name"] for f in fields}
    for g in any_of or []:
        assert g and set(g) <= names, (name, g)
    S.append(dict(name=name, producer=producer, desc=desc, fields=fields, any_of=any_of))


M("AISecurityTrainingProgramme", "Organizations (5.1.1-1); developers receive additional training (5.1.1-2.2)",
  "The cyber security training programme and its AI security content.",
  [F("ai_security_content", AS, "shall", ["5.1.1-1::shall include AI security content"], "AI security content included in the training programme"),
   F("content_reviews", AO, "shall", ["5.1.1-1::which shall be regularly reviewed"], "the regular review and update of that content",
     items=[F("reviewed_at", DT, "inferred", ["5.1.1-1::which shall be regularly reviewed"], "when a review took place",
              reason="the source requires regular review and update but names no record of it; a dated entry is the minimal evidence"),
            F("update_trigger", "string", "inferred", ["5.1.1-1::which shall be regularly reviewed"], "what prompted an update, e.g. new substantial AI-related security threats",
              reason="the source gives new substantial AI-related security threats only as an example (such as) of when to review and update; it asks for no record of the trigger"),
            ]),
   F("role_tailoring", AO, "shall", ["5.1.1-1.1"], "training tailored to the roles and responsibilities of staff",
     items=[F("role", "string", "shall", ["5.1.1-1.1"], "the role or responsibility"),
            F("tailored_content", AS, "shall", ["5.1.1-1.1"], "content tailored to that role")]),
   F("staff_awareness_topics", AS, "shall", ["5.1.1-2"], "latest AI-related security threats and vulnerabilities all staff must stay aware of"),
   F("proposed_mitigations", AS, "shall", ["5.1.1-2::Where available"], "proposed mitigations for those threats",
     cond="where available"),
   F("communication_channels", AS, "should", ["5.1.1-2.1"], "channels used to communicate updates (bulletins, newsletters, knowledge-sharing platforms)"),
   F("developer_training_topics", AS, "shall", ["5.1.1-2.2"], "secure coding and system design techniques specific to AI development, aimed at preventing and mitigating vulnerabilities in algorithms, models and associated software")])

M("BusinessRequirementsAndRiskAssessment", "System Operator and/or Developer (5.1.2-1)",
  "The documented assessment made as part of deciding whether to create an AI system.",
  [F("business_requirements_or_problem", "string", "shall", ["5.1.2-1"], "the business requirements and/or problem the system addresses"),
   F("ai_security_risks", AS, "shall", ["5.1.2-1"], "associated AI security risks"),
   F("mitigation_strategies", AS, "shall", ["5.1.2-1"], "mitigation strategies for those risks"),
   F("data_custodian_included", "boolean", "shall", ["5.1.2-1.1"], "the Data Custodian took part in internal discussions on requirements and data needs",
     cond="where the Data Custodian is part of the Developer's organization"),
   F("assessing_parties", AS, "inferred", ["5.1.2-1"], "which of System Operator / Developer conducted the assessment",
     reason="the source assigns the duty to 'a System Operator and/or Developer' but does not say the record names them"),
   F("decision_outcome", "string", "inferred", ["5.1.2-1"], "whether the AI system was to be created",
     reason="the assessment is 'part of deciding whether to create an AI system'; the source does not say the outcome is recorded")])

M("AuditTrail", "Developer (5.1.2-3, 5.2.4-1)",
  "The audit trail of the AI system: design, post-deployment maintenance plans, and the operation and lifecycle management of models, datasets and prompts.",
  [F("system_design", "string", "shall", ["5.2.4-1"], "documentation of the system design"),
   F("post_deployment_maintenance_plans", AS, "shall", ["5.2.4-1"], "post-deployment maintenance plans"),
   F("incorporated_items", AO, "shall", ["5.1.2-3"], "models, datasets and prompts incorporated into the system",
     items=[F("item_kind", "enum", "shall", ["5.1.2-3::This shall include"], "model, dataset or prompt", values=["model", "dataset", "prompt"]),
            F("item_ref", "string", "inferred", ["5.1.2-3::This shall include"], "identifier of the item",
              reason="an audit trail entry must say which item it concerns; the source defines no identifier"),
            F("operation_records", AS, "shall", ["5.1.2-3::This shall include"], "operation of the item"),
            F("lifecycle_management_records", AS, "shall", ["5.1.2-3::This shall include"], "lifecycle management of the item")]),
   F("available_to_downstream", AS, "should", ["5.2.4-1::Developers should make the documentation"], "downstream System Operators and Data Custodians given access to the documentation")])

M("SecurityRelevantDocumentation", "Developer (5.2.4-1.1)",
  "The security-relevant information the system documentation includes.",
  [F("training_data_sources", AS, "should", ["5.2.4-1.1"], "sources of training data, including fine-tuning data and human or other operational feedback"),
   F("intended_scope", "string", "should", ["5.2.4-1.1"], "intended scope"),
   F("limitations", AS, "should", ["5.2.4-1.1"], "limitations"),
   F("guardrails", AS, "should", ["5.2.4-1.1"], "guardrails"),
   F("retention_time", "string", "should", ["5.2.4-1.1"], "retention time"),
   F("suggested_review_frequency", "string", "should", ["5.2.4-1.1"], "suggested review frequency"),
   F("potential_failure_modes", AS, "should", ["5.2.4-1.1"], "potential failure modes")])

M("ModelComponentHashRelease", "Developer (5.2.4-1.2)",
  "Cryptographic hashes released for model components made available to other stakeholders.",
  [F("components", AO, "shall", ["5.2.4-1.2"], "model components made available to other stakeholders",
     items=[F("component_ref", "string", "inferred", ["5.2.4-1.2"], "which component the hash covers",
              reason="a hash is meaningless without the component it identifies; the source names no identifier"),
            F("cryptographic_hash", "string", "shall", ["5.2.4-1.2"], "released cryptographic hash allowing verification of authenticity"),
            F("hash_algorithm", "string", "inferred", ["5.2.4-1.2"], "algorithm that produced the hash",
              reason="the source requires 'cryptographic hashes' and names no algorithm; a verifier needs it")])])

M("PublicTrainingDataProvenance", "Developer (5.2.4-2, 5.2.4-2.1)",
  "Documentation of how training data from publicly available sources was obtained.",
  [F("entries", AO, "shall", ["5.2.4-2::As discovery"], "one entry per publicly sourced training dataset",
     items=[F("how_obtained", "string", "shall", ["5.2.4-2::As discovery"], "how the public training data was obtained"),
            F("origin", "string", "shall", ["5.2.4-2::As discovery"], "where the data came from"),
            F("use_in_model", "string", "shall", ["5.2.4-2::As discovery"], "how the data is used in the model"),
            F("source", "string", "should", ["5.2.4-2.1"], "at a minimum the source, such as the URL of the scraped page"),
            F("obtained_at", DT, "should", ["5.2.4-2.1"], "date and time the data was obtained")])])

M("PromptAndConfigurationAuditLog", "Developer (5.2.4-3)",
  "Audit log of changes to system prompts or other model configuration that affect how the system works.",
  [F("entries", AO, "should", ["5.2.4-3"], "changes to system prompts or other model configuration (including prompts)",
     items=[F("changed_item", "string", "should", ["5.2.4-3"], "the system prompt or model configuration changed"),
            F("change_description", "string", "should", ["5.2.4-3"], "the change"),
            F("changed_at", DT, "inferred", ["5.2.4-3"], "when the change was made",
              reason="an audit log is ordered by time; the source does not list log fields")]),
   F("available_to", AS, "can", ["5.2.4-3::Developers can make this available"], "System Operators and End-Users with access to the model who are given the log")])

M("ThreatModelAndRiskRegister", "Developers and System Operators (5.1.3-1); System Operators for controls (5.1.3-1.3)",
  "Threat analysis, risk management, controls applied and review of AI system security risks.",
  [F("threats_analysed", AS, "shall", ["5.1.3-1"], "threats analysed"),
   F("security_risks_managed", AS, "shall", ["5.1.3-1"], "security risks managed"),
   F("ai_specific_attacks_addressed", AS, "should", ["5.1.3-1::Threat modelling should include"], "AI-specific attacks addressed, such as data poisoning, model inversion and membership inference"),
   F("reviews_and_updates", AO, "should", ["5.1.3-1::Threat modelling should include"], "regular reviews and updates of the threat model",
     items=[F("reviewed_at", DT, "inferred", ["5.1.3-1::Threat modelling should include"], "when a review took place",
              reason="regular review needs a date to be evidenced; the source defines no record")]),
   F("configuration_change_assessments", AO, "shall", ["5.1.3-1.1"], "risks from a new or updated setting or configuration option at any AI lifecycle stage",
     cond="when a new setting or configuration option is implemented or updated",
     items=[F("setting_or_option", "string", "shall", ["5.1.3-1.1"], "the setting or configuration option"),
            F("lifecycle_stage", "string", "shall", ["5.1.3-1.1"], "the stage of the AI lifecycle"),
            F("risks", AS, "shall", ["5.1.3-1.1"], "security risks arising")]),
   F("superfluous_functionality_risks", AS, "shall", ["5.1.3-1.2"], "risks of models providing superfluous functionality (Developers)"),
   F("applied_controls", AO, "shall", ["5.1.3-1.3"], "controls applied to risks identified by the analysis (System Operators)",
     items=[F("risk", "string", "shall", ["5.1.3-1.3"], "the identified risk"),
            F("control", "string", "shall", ["5.1.3-1.3"], "the control applied"),
            F("implementation_cost", "string", "shall", ["5.1.3-1.3"], "cost of implementation considered against corporate risk tolerance")]),
   F("external_entity_assurance", AS, "should", ["5.1.3-3"], "assurance obtained that an external entity responsible for AI security risks can address them (System Operators)",
     cond="where an external entity has responsibility for AI security risks within the organization's infrastructure"),
   F("risk_appetite", "string", "should", ["5.1.3-4"], "risk appetite against which infrastructure is continuously monitored and reviewed"),
   F("infrastructure_reviews", AO, "should", ["5.1.3-4"], "continuous monitoring and review of system infrastructure",
     items=[F("reviewed_at", DT, "inferred", ["5.1.3-4"], "when a review took place",
              reason="continuous review needs a date to be evidenced; the source defines no record")])])

M("UnresolvedThreatCommunication", "Developers to System Operators; System Operators to End-users (5.1.3-2)",
  "Communication of AI security threats that Developers cannot resolve.",
  [F("threat_description", "string", "inferred", ["5.1.3-2::cannot be resolved by Developers", "5.1.3-2::this shall be communicated to System Operators"], "the unresolved threat",
     reason="the source requires the threat to be communicated but defines no field for identifying it"),
   # Not conditional within this structure: an unresolved threat Developers cannot
   # resolve is the structure's own premise (its description), so the shall holds
   # for every record (verify pass 2026-11-15; the condition had made it optional).
   F("communicated_to_system_operators", "boolean", "shall", ["5.1.3-2::this shall be communicated to System Operators"], "threat communicated by the Developer to System Operators so they can threat model"),
   F("communicated_to_end_users", "boolean", "shall", ["5.1.3-2::System Operators shall communicate this information"], "threat communicated by the System Operator to End-users"),
   F("risk_descriptions", AS, "should", ["5.1.3-2::This communication should include"], "detailed descriptions of the risks"),
   F("potential_impacts", AS, "should", ["5.1.3-2::This communication should include"], "potential impacts"),
   F("recommended_actions", AS, "should", ["5.1.3-2::This communication should include"], "recommended actions to address or monitor the threats")])

M("AssetInventory", "Developers, Data Custodians and System Operators (5.2.1-1)",
  "Comprehensive inventory of assets including interdependencies and connectivity.",
  [F("assets", AO, "shall", ["5.2.1-1"], "the assets held",
     items=[F("asset_ref", "string", "inferred", ["5.2.1-1"], "identifier or name of the asset",
              reason="an inventory entry must identify the asset; the source defines no identifier"),
            F("interdependencies_connectivity", AS, "shall", ["5.2.1-1"], "interdependencies and connectivity of the asset"),
            F("version", "string", "inferred", ["5.2.1-2"], "version under control",
              reason="5.2.1-2 requires processes and tools to track and version-control assets; the source does not say the inventory carries the version"),
            F("authenticity_evidence", "string", "inferred", ["5.2.1-2"], "how the asset was authenticated",
              reason="5.2.1-2 requires processes and tools to authenticate assets; the source does not say the inventory records the result")]),
   F("maintained_by", AS, "inferred", ["5.2.1-1"], "which of Developers, Data Custodians and System Operators maintains the inventory",
     reason="each named role shall maintain an inventory; the source does not say the record names its maintainer")])

M("DisasterRecoveryPlan", "System Operators (5.2.1-3)",
  "Disaster recovery plan tailored to attacks aimed at AI systems.",
  [F("ai_attack_scenarios", AS, "shall", ["5.2.1-3"], "specific attacks aimed at AI systems the plan accounts for"),
   F("known_good_state_restoration", "string", "should", ["5.2.1-3.1::should ensure that a known good state", "5.2.1-3.1::can be restored"], "how a known good state can be restored")])

M("AccessControlEvaluation", "Developers and System Operators (5.2.2-1)",
  "Evaluation of the organization's access control frameworks and the measures identified to secure AI assets.",
  [F("frameworks_evaluated", AS, "shall", ["5.2.2-1"], "access control frameworks evaluated"),
   F("measures", AO, "shall", ["5.2.2-1"], "appropriate measures identified, per asset class",
     items=[F("target", "enum", "shall", ["5.2.2-1"], "what the measure secures", values=["API", "model", "data", "training pipeline", "processing pipeline"]),
            F("measure", "string", "shall", ["5.2.2-1"], "the measure identified")])])

M("VulnerabilityDisclosurePolicy", "Developers and System Operators (5.2.2-4)",
  "Published vulnerability disclosure policy.",
  [F("policy_statement", "string", "shall", ["5.2.2-4"], "the clear vulnerability disclosure policy"),
   F("published", "boolean", "shall", ["5.2.2-4"], "the policy is published"),
   F("publication_location", "string", "inferred", ["5.2.2-4"], "where the policy is accessible",
     reason="the policy shall be 'clear and accessible'; the source gives no location format")])


def plan(name, label, sel):
    M(name, "Developers and System Operators (5.2.2-5)", "The %s." % label,
      [F("plan_content", "string", "shall", [sel], "the %s as created" % label),
       F("tests", AO, "shall", [sel], "tests of the plan",
         items=[F("tested_at", DT, "inferred", [sel], "when the plan was tested", reason="the source requires testing; it defines no test record"),
                F("outcome", "string", "inferred", [sel], "result of the test", reason="the source requires testing; it defines no test record")]),
       F("maintenance_history", AO, "shall", [sel], "maintenance of the plan",
         items=[F("maintained_at", DT, "inferred", [sel], "when the plan was maintained", reason="the source requires maintenance; it defines no record")])])


plan("AISystemIncidentManagementPlan", "AI system incident management plan", "5.2.2-5")
plan("AISystemRecoveryPlan", "AI system recovery plan", "5.2.2-5")

M("ThirdPartyComponentAssessment", "Developer or System Operator (5.1.2-4, 5.1.2-7, 5.2.3-3)",
  "AI security risk assessment and due diligence for external components, providers and released models.",
  [F("component_ref", "string", "inferred", ["5.1.2-4"], "the external component, provider or released model assessed",
     reason="the source defines no identifier"),
   F("ai_security_risk_assessment", "string", "shall", ["5.1.2-4"], "AI security risk assessment of the external component",
     cond="where an external component is used"),
   F("due_diligence", "string", "shall", ["5.1.2-4"], "due diligence in line with existing software development processes, assessing AI-specific risks",
     cond="where an external component is used"),
   F("external_provider_due_diligence", "string", "shall", ["5.1.2-7::they shall undertake a due diligence assessment"], "due diligence assessment of the external provider",
     cond="where the Developer or System Operator chooses to work with an external provider"),
   F("provider_adherence", "boolean", "should", ["5.1.2-7::should ensure that the provider"], "the provider is adhering to the present document"),
   F("re_run_evaluations", AS, "shall", ["5.2.3-3"], "evaluations re-run on released models intended for use",
     cond="for released models the organization intends to use")],
  # The structure covers three cases, each under its own condition; a record is
  # at least one of them (verify pass 2026-11-15: the schema had accepted {}).
  any_of=[["ai_security_risk_assessment", "due_diligence"], ["external_provider_due_diligence"], ["re_run_evaluations"]])

M("UndocumentedComponentJustification", "System Operators (5.2.3-2); Developers and System Operators (5.2.3-2.1)",
  "Justification and mitigation for using models or components that are not well-documented or secured.",
  [F("component_ref", "string", "inferred", ["5.2.3-2"], "the model or component", reason="the source defines no identifier"),
   # Not conditional within this structure: a model or component that is not
   # well-documented or secured is the structure's premise (verify pass 2026-11-15).
   F("justification_documentation", "string", "shall", ["5.2.3-2"], "documentation justifying the decision to use it"),
   F("mitigating_controls", AS, "shall", ["5.2.3-2.1"], "mitigating controls"),
   F("risk_assessment", "string", "shall", ["5.2.3-2.1"], "risk assessment linked to the model or component"),
   F("shared_with_end_users", "boolean", "shall", ["5.2.3-2.2"], "the documentation is shared with End-users in an accessible way")])

M("AIPermissionRiskRecord", "Developers and System Operators (5.1.2-6)",
  "Permissions granted to the AI system on other systems, and their risk assessment.",
  [F("connected_system", "string", "inferred", ["5.1.2-6"], "the other system or data source",
     reason="the source defines no identifier for the interacting system"),
   # Not conditional within this structure: interaction with another system or
   # data source is the structure's premise (verify pass 2026-11-15).
   F("permissions_granted", AS, "shall", ["5.1.2-6"], "permissions granted on the other system or data source"),
   F("functional_justification", "string", "shall", ["5.1.2-6"], "why each permission is required for functionality"),
   F("risk_assessment", "string", "shall", ["5.1.2-6"], "risk assessment of the permissions")])

M("ModelUpdateAdvanceNotice", "System Operators (5.2.3-4)",
  "Communication to End-users of an intention to update models, prior to the update.",
  [F("intended_update", "string", "shall", ["5.2.3-4"], "the model update intended"),
   F("communicated_at", DT, "inferred", ["5.2.3-4"], "when End-users were told",
     reason="the notice must precede the update; evidencing that needs a date the source does not define"),
   F("communication_means", "string", "inferred", ["5.2.3-4"], "how the notice was made accessible", reason=INF_ACC)])

M("DeveloperSecurityAssessmentReport", "Developers (5.2.5-1, 5.2.5-3, 5.2.5-4, 5.2.5-4.1)",
  "Security testing and evaluation of models, applications and systems released to System Operators and/or End-users.",
  [F("subject_kind", "enum", "shall", ["5.2.5-1"], "what was tested", values=["model", "application", "system"]),
   F("security_assessment_performed", "boolean", "shall", ["5.2.5-1"], "the subject was tested as part of a security assessment process"),
   F("independent_testers", "boolean", "should", ["5.2.5-2.1"], "independent security testers with technical skills relevant to the AI system were used"),
   F("findings", AS, "should", ["5.2.5-3"], "findings of the testing and evaluation"),
   F("findings_shared_with_system_operators", "boolean", "should", ["5.2.5-3"], "findings shared with System Operators"),
   F("output_reverse_engineering_evaluation", "string", "should", ["5.2.5-4"], "evaluation that model outputs do not allow reverse engineering of non-public aspects of the model or training data"),
   F("unintended_influence_evaluation", "string", "should", ["5.2.5-4.1"], "evaluation that model outputs give no unintended influence over the system")])

M("PreDeploymentTestReport", "System Operators (5.2.5-2)",
  "Testing conducted before the system is deployed, with support from Developers.",
  [F("tests_conducted", AS, "shall", ["5.2.5-2"], "testing conducted prior to deployment"),
   F("developer_support", "string", "shall", ["5.2.5-2"], "support given by Developers"),
   F("independent_testers", "boolean", "should", ["5.2.5-2.1"], "independent security testers with relevant technical skills were used")])

M("EndUserDataUseNotice", "System Operators (5.3.1-1); external Developer to System Operators",
  "Conveys to End-users where and how their data will be used, accessed and stored.",
  [F("data_use", "string", "shall", ["5.3.1-1"], "how data will be used"),
   F("data_access", "string", "shall", ["5.3.1-1"], "who or what can access the data"),
   F("data_storage", "string", "shall", ["5.3.1-1"], "where and how the data is stored"),
   F("developer_supplied_information", "string", "shall", ["5.3.1-1::they shall provide this information"], "information the Developer provides to the System Operator for this notice",
     cond="where the Developer is an external entity"),
   F("presentation_means", "string", "inferred", ["5.3.1-1"], "how the notice is made accessible", reason=INF_ACC)])

M("EndUserGuidance", "System Operators (5.3.1-2, 5.3.1-2.1); Developers (5.3.1-2); also 5.1.4-5",
  "Accessible guidance for End-users on using, managing, integrating and configuring the AI system.",
  [F("use_guidance", "string", "shall", ["5.3.1-2"], "guidance on use"),
   F("management_guidance", "string", "shall", ["5.3.1-2"], "guidance on management"),
   F("integration_guidance", "string", "shall", ["5.3.1-2"], "guidance on integration"),
   F("configuration_guidance", "string", "shall", ["5.3.1-2"], "guidance on configuration"),
   F("appropriate_use", "string", "shall", ["5.3.1-2.1"], "guidance on the appropriate use of the model or system"),
   F("limitations", AS, "shall", ["5.3.1-2.1"], "limitations highlighted"),
   F("potential_failure_modes", AS, "shall", ["5.3.1-2.1"], "potential failure modes highlighted"),
   F("prohibited_use_cases", AS, "should", ["5.1.4-5"], "prohibited use cases of the AI system End-users are made aware of"),
   F("developer_supplied_information", "string", "shall", ["5.3.1-2::they shall provide all necessary information"], "all necessary information the Developer provides to the System Operator",
     cond="where the Developer is an external entity")])

M("EndUserSecurityUpdateNotice", "System Operators (5.3.1-2.2)",
  "Proactive notice to End-users of a security-relevant update, with an explanation.",
  [F("update_ref", "string", "inferred", ["5.3.1-2.2"], "the update announced", reason="the source defines no identifier"),
   F("explanation", "string", "shall", ["5.3.1-2.2"], "clear explanation, in an accessible way"),
   F("proactively_informed", "boolean", "shall", ["5.3.1-2.2"], "End-users were informed proactively")])

M("IncidentSupportProcess", "Developers and System Operators (5.3.1-3)",
  "Process for supporting End-users and Affected Entities during and after a cyber security incident.",
  [F("process_description", "string", "should", ["5.3.1-3::The process for undertaking this"], "the documented process"),
   F("agreed_in_contracts", "boolean", "should", ["5.3.1-3::The process for undertaking this"], "the process is agreed in contracts with End-users"),
   F("supported_parties", AS, "should", ["5.3.1-3"], "End-users and Affected Entities supported")])

M("SecurityUpdateRecord", "Developers (5.4.1-1, 5.4.1-1.1, 5.4.1-2, 5.4.1-3); System Operators deliver (5.4.1-1)",
  "Security updates and patches, their notification and delivery, and the contingency where none can be provided.",
  [F("update_or_patch", "string", "shall", ["5.4.1-1"], "the security update or patch provided",
     cond="where possible"),
   # Notification and delivery concern the update, so they bind only where one is
   # provided: required with update_or_patch, never on their own (a record of the
   # no-update case would otherwise have to claim both; verify pass 2026-11-15).
   F("notified_system_operators", "boolean", "shall", ["5.4.1-1"], "System Operators notified of the update",
     cond="where an update or patch is provided", with_field="update_or_patch"),
   F("delivered_to_end_users", "boolean", "shall", ["5.4.1-1::System Operators shall deliver"], "System Operator delivered the update to End-users",
     cond="where an update or patch is provided", with_field="update_or_patch"),
   F("contingency_mechanisms", AS, "shall", ["5.4.1-1.1::Developers shall have mechanisms", "5.4.1-1.1::updates cannot be provided"], "mechanisms and contingency plans to mitigate security risks, particularly where updates cannot be provided"),
   F("major_update_retested", "boolean", "should", ["5.4.1-2"], "a major update was treated as a new model version with new security testing and evaluation"),
   F("operator_support_mechanisms", AS, "should", ["5.4.1-3"], "support to System Operators to evaluate and respond to model changes, e.g. beta-testing preview access and versioned APIs")])

M("SystemAndUserActionLog", "System Operators (5.4.2-1)",
  "Log of system and user actions supporting security compliance, incident investigation and vulnerability remediation.",
  [F("entries", AO, "shall", ["5.4.2-1"], "logged actions",
     items=[F("actor_kind", "enum", "shall", ["5.4.2-1"], "system or user action", values=["system", "user"]),
            F("action", "string", "shall", ["5.4.2-1"], "the action logged"),
            F("logged_at", DT, "inferred", ["5.4.2-1"], "when the action occurred",
              reason="a log supporting incident investigation is time-ordered; the source lists no log fields")])])

M("LogAnalysisRecord", "System Operators (5.4.2-2)",
  "Analysis of logs for desired output and for anomalies, breaches or unexpected behaviour.",
  [F("outputs_continue_as_desired", "boolean", "should", ["5.4.2-2"], "AI models continue to produce desired outputs"),
   F("detections", AO, "should", ["5.4.2-2"], "anomalies, security breaches or unexpected behaviour detected over time",
     items=[F("kind", "enum", "should", ["5.4.2-2"], "what was detected", values=["anomaly", "security breach", "unexpected behaviour"]),
            F("suspected_cause", "string", "inferred", ["5.4.2-2"], "e.g. data drift or data poisoning",
              reason="the source gives data drift and data poisoning only as examples (such as) of causes; it asks for no record of the cause")])])

M("ModelPerformanceMonitoringRecord", "System Operators and Developers (5.4.2-3, 5.4.2-4)",
  "Monitoring of internal states and of model and system performance over time.",
  [F("internal_state_observations", AS, "should", ["5.4.2-3"], "internal states monitored where this better enables addressing security threats or future security analytics"),
   F("performance_over_time", AS, "should", ["5.4.2-4::should monitor the performance"], "performance of models and system monitored over time"),
   F("detected_behaviour_changes", AO, "should", ["5.4.2-4::should monitor the performance", "5.4.2-4::can detect sudden or gradual"], "sudden or gradual changes in behaviour that could affect security",
     items=[F("change_pace", "enum", "should", ["5.4.2-4::should monitor the performance", "5.4.2-4::can detect sudden or gradual"], "sudden or gradual", values=["sudden", "gradual"]),
            F("description", "string", "should", ["5.4.2-4::should monitor the performance", "5.4.2-4::can detect sudden or gradual"], "the change")])])

M("AssetTransferDisposalRecord", "Developer or System Operator (5.5.1-1)",
  "Transfer or sharing of ownership of training data and/or a model, with secure disposal.",
  [F("assets", AS, "shall", ["5.5.1-1"], "training data and/or model transferred or shared"),
   F("receiving_entity", "string", "inferred", ["5.5.1-1"], "the entity ownership passes to", reason="the source says 'another entity' and defines no field"),
   F("data_custodians_involved", AS, "shall", ["5.5.1-1"], "Data Custodians involved"),
   F("secure_disposal", "string", "shall", ["5.5.1-1"], "how the assets were securely disposed of")])

M("DecommissioningRecord", "Developer or System Operator (5.5.1-2)",
  "Decommissioning of a model and/or system with secure deletion of applicable data and configuration details.",
  [F("decommissioned_items", AS, "shall", ["5.5.1-2"], "model and/or system decommissioned"),
   F("data_custodians_involved", AS, "shall", ["5.5.1-2"], "Data Custodians involved"),
   F("deleted_data", AS, "shall", ["5.5.1-2"], "applicable data securely deleted"),
   F("deleted_configuration_details", AS, "shall", ["5.5.1-2"], "configuration details securely deleted")])

# Provisions that prescribe action, not a record whose content the source defines.
CONSIDERED = [
    ("5.1.2-2", "design property (withstand adversarial attacks, unexpected inputs, failure); no record content defined"),
    ("5.1.2-5", "Data Custodian assurance about intended usage; no record content defined"),
    ("5.1.2-5.1", "organizational encouragement of reporting; no record content defined"),
    ("5.1.4-1", "capability to enable human oversight; a system property"),
    ("5.1.4-2", "design for assessable outputs; a system property"),
    ("5.1.4-3", "technical measures for oversight; a system property"),
    ("5.1.4-4", "verification of Data Custodian controls; no record content defined"),
    ("5.2.1-2", "processes and tools to track, authenticate, version and secure assets; fields inferred under AssetInventory"),
    ("5.2.1-4", "protection of sensitive data; a control"),
    ("5.2.1-4.1", "checks and sanitisation of data and inputs; a control, no record defined"),
    ("5.2.1-4.2", "proportionate protections for confidential data or weights; a control"),
    ("5.2.2-2", "API controls such as rate limiting; a control"),
    ("5.2.2-3", "dedicated development and tuning environments; a control"),
    ("5.2.2-6", "contractual support from cloud service operators; a contract, no content defined"),
    ("5.2.3-1", "secure software supply chain processes; a process, no record defined"),
]


def emit(o, ind=0):
    p = "  " * ind
    out = []
    if isinstance(o, dict):
        for k, v in o.items():
            if isinstance(v, (dict, list)) and v:
                out.append("%s%s:" % (p, k))
                out.extend(emit(v, ind + 1))
            else:
                out.append("%s%s: %s" % (p, k, json.dumps(v, ensure_ascii=False) if not (isinstance(v, (dict, list))) else ("[]" if isinstance(v, list) else "{}")))
    else:
        for it in o:
            if isinstance(it, dict):
                sub = emit(it, ind + 1)
                sub[0] = p + "- " + sub[0].lstrip()
                out.extend(sub)
            else:
                out.append("%s- %s" % (p, json.dumps(it, ensure_ascii=False)))
    return out


def field_out(fd):
    ids = []
    for s in fd["sels"]:
        i = resolve(s)
        if i not in ids:
            ids.append(i)
    d = {"name": fd["name"], "type": fd["type"]}
    if fd["values"]:
        d["values"] = fd["values"]
    d["obligation"] = fd["obligation"]
    d["required"] = fd["obligation"] == "shall" and not fd["cond"]
    if fd["cond"]:
        d["condition"] = fd["cond"]
    if fd["with_field"]:
        d["required_with"] = fd["with_field"]
    d["description"] = fd["desc"]
    if fd["reason"]:
        d["inferred_reason"] = fd["reason"]
    d["constrained_by"] = ids
    if fd["items"]:
        d["items"] = [field_out(x) for x in fd["items"]]
    return d


def main():
    msgs = []
    for m in S:
        clauses = []

        def walk(f):
            for s in f["sels"]:
                c = "§" + s.split("::")[0].split("-")[0]
                if c not in clauses:
                    clauses.append(c)
            for x in f["items"] or []:
                walk(x)
        for fd in m["fields"]:
            walk(fd)
        msg = {"name": m["name"], "locator": ", ".join(clauses), "produced_by": m["producer"],
               "encoding": "none in source", "description": m["desc"]}
        if m["any_of"]:
            # one scalar per group (field names joined by ", "): a block list of
            # plain strings, which both bin/ YAML readers read alike
            msg["requires_any_of"] = [", ".join(g) for g in m["any_of"]]
        msg["fields"] = [field_out(f) for f in m["fields"]]
        msgs.append(msg)
    considered = []
    for k, why in CONSIDERED:
        considered.append({"provision": k, "constrained_by": [resolve_provision(k)], "reason": why})
    head = [
        'schema: "library-messages/v1"',
        "record: etsi-en-304-223",
        "note: >",
        "  The EN defines no wire messages and no encodings. These structures are the work products and records that clause 5",
        "  provisions require someone to produce or maintain. Field names, JSON types and the grouping into structures are OURS",
        "  (derived); only the obligation (shall / should / can) and the constrained_by ids come from the source. obligation:",
        "  inferred marks a field the source does not demand, with inferred_reason. A shall under a condition is not required",
        "  (condition names it); required_with names the field it is required alongside, and requires_any_of the groups of",
        "  conditional fields of which a record carries at least one. constrained_by ids are emitted by",
        "  distilled/schema/build-messages.derived.py from requirements.yaml: each field cites the leaf sentence entries that",
        "  hold its verbal form; considered_not_structures cites the provision-level entry.",
    ]
    body = ["messages:"] + emit(msgs, 1)
    tail = ["considered_not_structures:"] + emit(considered, 1)
    open(os.path.join(DIST, "messages.yaml"), "w").write("\n".join(head + body + tail) + "\n")
    # coverage: every clause-5 provision key is used or considered
    all_keys = set()
    for r in REQS:
        t = r["text"]
        if t.startswith("Provision "):
            all_keys.add(t.split(" ")[1])
    covered = USED | {k for k, _ in CONSIDERED}
    miss = sorted(all_keys - covered)
    print("structures", len(msgs), "provision keys", len(all_keys), "uncovered", miss)


main()

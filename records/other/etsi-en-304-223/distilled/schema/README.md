---
record: etsi-en-304-223
kind: schema
title: "etsi-en-304-223 — schemas"
extracted: "2026-11-15"
reviewed_by: ""
---

# Derived schemas

The EN contains no schema, grammar or encoding of any kind (clause 5 is prose provisions; there is no CDDL, ASN.1, JSON or XML anywhere in the 16 pages). So there is nothing to copy verbatim. These JSON Schemas (draft 2020-12) are **derived**: one per work product in `../messages.yaml`, `$id: urn:library:etsi-en-304-223:<Name>`. They are our reading of what the provisions require someone to produce; the EN does not prescribe them.

Generated, not hand-written: `generate.derived.py` reads `../messages.yaml` and writes every `<Name>.derived.schema.json` and the matching `../examples/<Name>.cases.derived.json`. `build-messages.derived.py` writes `../messages.yaml` from a field spec, resolving every `constrained_by` requirement id from `../requirements.yaml` by selector (raises on zero or several matches). A selector picks only leaf sentence entries (an `R-` id with no `split_into`), so a field cites the entry that holds its verbal form; `considered_not_structures` cites the provision-level entry. `selftest.derived.py` runs every schema against its cases and checks the rules below (needs `jsonschema`; install it in a venv, not in the repo).

Rebuild order: `build-messages.derived.py`, then `generate.derived.py`, then `selftest.derived.py`. The verify pass (2026-11-15) found the first of these no longer ran: the provision-level entries added to `../requirements.yaml` after `messages.yaml` was built made all 83 of its selectors match two entries, the sentence and its provision (counted by script). The `messages.yaml` it had written cited the split-parent sentence for 14 fields (counted by script), one of them a should field joined to a sentence whose verb is shall. It now runs, and the rebuilt `messages.yaml` cites leaf entries.

## What binds

- Every object is closed (`additionalProperties: false`), top level and in array items.
- `required` is exactly the fields whose obligation is `shall` and carry no condition. A `shall` under a condition (for example the external-Developer condition of 5.3.1-1 and 5.3.1-2) is optional in the schema and carries `x-condition`. A condition that is the structure's own premise is not a field condition: an `UnresolvedThreatCommunication` exists only for a threat Developers cannot resolve, so its communication to System Operators is required.
- A `shall` boolean is `const: true`. The field records that the act was done, so `false` is rejected; a required boolean that accepted `false` would bind nothing.
- `required_with` in `../messages.yaml` becomes `dependentRequired`: in `SecurityUpdateRecord`, notifying System Operators and delivering to End-users are required whenever an `update_or_patch` is present, and not otherwise.
- `requires_any_of` becomes `anyOf` over required groups: `ThirdPartyComponentAssessment` covers three cases (external component, external provider, released model), each under its own condition, and must carry at least one, so it rejects `{}`.
- `should`, `can` and `inferred` fields are optional properties. `x-obligation` records which. `x-inferred-reason` says why an inferred field exists.
- A required array has `minItems: 1`; strings have `minLength: 1`.
- Every property has a non-empty `x-constrained-by` (requirement ids).
- `format: date-time` is an annotation, not asserted by default validators.
- A structure with no `shall` field (all `should`, `can` or inferred) accepts `{}`; that is the source's weight, not a gap. The five that do: `SecurityRelevantDocumentation`, `PromptAndConfigurationAuditLog`, `IncidentSupportProcess`, `LogAnalysisRecord`, `ModelPerformanceMonitoringRecord`. `selftest.derived.py` fails any structure with a `shall` field that accepts `{}`.
- Every `shall`, `should` or `can` obligation occurs as a verbal form in at least one requirement its field cites (checked by `selftest.derived.py`). A field whose only support is an example (`such as`) is `inferred`.

## Files

- `AIPermissionRiskRecord.derived.schema.json`
- `AISecurityTrainingProgramme.derived.schema.json`
- `AISystemIncidentManagementPlan.derived.schema.json`
- `AISystemRecoveryPlan.derived.schema.json`
- `AccessControlEvaluation.derived.schema.json`
- `AssetInventory.derived.schema.json`
- `AssetTransferDisposalRecord.derived.schema.json`
- `AuditTrail.derived.schema.json`
- `BusinessRequirementsAndRiskAssessment.derived.schema.json`
- `DecommissioningRecord.derived.schema.json`
- `DeveloperSecurityAssessmentReport.derived.schema.json`
- `DisasterRecoveryPlan.derived.schema.json`
- `EndUserDataUseNotice.derived.schema.json`
- `EndUserGuidance.derived.schema.json`
- `EndUserSecurityUpdateNotice.derived.schema.json`
- `IncidentSupportProcess.derived.schema.json`
- `LogAnalysisRecord.derived.schema.json`
- `ModelComponentHashRelease.derived.schema.json`
- `ModelPerformanceMonitoringRecord.derived.schema.json`
- `ModelUpdateAdvanceNotice.derived.schema.json`
- `PreDeploymentTestReport.derived.schema.json`
- `PromptAndConfigurationAuditLog.derived.schema.json`
- `PublicTrainingDataProvenance.derived.schema.json`
- `SecurityRelevantDocumentation.derived.schema.json`
- `SecurityUpdateRecord.derived.schema.json`
- `SystemAndUserActionLog.derived.schema.json`
- `ThirdPartyComponentAssessment.derived.schema.json`
- `ThreatModelAndRiskRegister.derived.schema.json`
- `UndocumentedComponentJustification.derived.schema.json`
- `UnresolvedThreatCommunication.derived.schema.json`
- `VulnerabilityDisclosurePolicy.derived.schema.json`
- `generate.derived.py`, `build-messages.derived.py`, `selftest.derived.py`

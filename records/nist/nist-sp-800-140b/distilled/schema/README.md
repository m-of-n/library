---
record: nist-sp-800-140b
kind: schema
title: "nist-sp-800-140b — schemas"
extracted: "2026-11-15"
reviewed_by: ""
---

# Schemas

SP 800-140B has no formal notation: its Annex B content is bulleted requirements, blank table templates and figure placeholders. Each schema describes one table row, one figure rule or the document spine.

## Derived (written by this library)

Every file here is **derived**: `nist-sp-800-140b` ships no CDDL, ASN.1 or JSON Schema of its own, so each is a JSON Schema (draft 2020-12, `additionalProperties: false`, `$id: urn:library:nist-sp-800-140b:<Name>`) written from the prose or tables the Source lines column names. Nothing here is verbatim.

| file | locator | what it validates | source lines |
|---|---|---|---|
| `SecurityPolicy.derived.schema.json` | §6.1 | the non-proprietary security policy as an ordered list of the twelve Annex B sections, each marked applicable or not | L328-330 |
| `SecurityLevelsTable.derived.schema.json` | Annex B.2.1 | B.2.1: the overall security rating and the security level of each of the twelve areas (Table x - Security Levels) | L358-359 |
| `TestedOperationalEnvironment.derived.schema.json` | Annex B.2.2 | B.2.2: one tested operational environment of a software, firmware or hybrid module | L405-406 |
| `VendorAffirmedOperationalEnvironment.derived.schema.json` | Annex B.2.2 | B.2.2: one operational environment the vendor affirms the module can be used on | L420 |
| `HardwareModuleTestedConfiguration.derived.schema.json` | Annex B.2.2 | B.2.2: one tested configuration of a hardware module | L433-436 |
| `ApprovedAlgorithmRow.derived.schema.json` | Annex B.2.2 | B.2.2: one row of Table x - Approved Algorithms (security functions employed for approved services) | L458-460 |
| `NonApprovedAlgorithmAllowedRow.derived.schema.json` | Annex B.2.2 | B.2.2: one row of Table x - Non-Approved Algorithms Allowed in the Approved Mode of Operation | L471 |
| `NonApprovedAlgorithmNoSecurityClaimedRow.derived.schema.json` | Annex B.2.2 | B.2.2: one row of Table x - Non-Approved Algorithms Allowed in the Approved Mode of Operation with No Security Claimed | L479 |
| `NonApprovedAlgorithmNotAllowedRow.derived.schema.json` | Annex B.2.2 | B.2.2: one row of Table x - Non-Approved Algorithms Not Allowed in the Approved Mode of Operation | L507 |
| `ModuleRepresentation.derived.schema.json` | Annex B.2.2 | B.2.2: the illustrations of the module (photograph, block diagram, per-version handling) | L514-518 |
| `RulesOfOperation.derived.schema.json` | Annex B.2.2 | B.2.2: overall security design and rules of operation, with the guidance footnote 6 requires | L556 |
| `PortInterfaceRow.derived.schema.json` | Annex B.2.3 | B.2.3: one row of Table x - Ports and Interfaces | L567-568 |
| `RoleServiceRow.derived.schema.json` | Annex B.2.4 | B.2.4: one row of Table x - Roles, Service Commands, Input and Output | L601 |
| `RoleAuthenticationRow.derived.schema.json` | Annex B.2.4 | B.2.4: one row of Table x - Roles and Authentication | L616 |
| `ApprovedServiceRow.derived.schema.json` | Annex B.2.4 | B.2.4: one row of Table x - Approved Services | L641-643 |
| `NonApprovedServiceRow.derived.schema.json` | Annex B.2.4 | B.2.4: one row of Table x - Non-Approved Services | L666-667 |
| `PhysicalSecurityInspectionRow.derived.schema.json` | Annex B.2.7 | B.2.7: one row of Table x - Physical Security Inspection Guidelines (physical Security Level 2 and above) | L710-716 |
| `TamperSealApplication.derived.schema.json` | Annex B.2.7 | B.2.7: the photos or illustrations of operator-applied tamper-evident seals or security appliances | L725-741 |
| `EfpEftRow.derived.schema.json` | Annex B.2.7 | B.2.7: one row of Table x - EFP/EFT (physical Security Level 3 and above) | L764-766 |
| `HardnessTemperatureRow.derived.schema.json` | Annex B.2.7 | B.2.7: one row of Table x - Hardness testing temperature ranges (strong or hard enclosures, coatings or potting) | L792 |
| `SspTableRow.derived.schema.json` | Annex B.2.9 | B.2.9: one row of Table x - SSPs (the key and SSP table) | L820-823 |
| `EntropySourceRow.derived.schema.json` | Annex B.2.9 | B.2.9: one row of Table x - Non-Deterministic Random Number Generation Specification | L849-850 |

## Rebuild and self-check

`build.derived.py` writes every `*.derived.schema.json` here, `../messages.yaml` and `../examples/*.derived.json`. It resolves every `constrained_by` id from `../requirements.yaml` by script (it raises on 0 or more than 1 match), writes every quotation from the cached source, then validates every case in `../examples/*-cases.derived.json` with the `jsonschema` package (`Draft202012Validator`) and exits 1 on any surprise. Run it with a Python that has `jsonschema` installed, from the repository root:

```sh
python3 records/nist/nist-sp-800-140b/distilled/schema/build.derived.py
```

Last run: 22 structures, 323 cases (27 accept, 296 reject), 0 unexpected.

Every structure with a mandatory field is tested with the empty object and with each mandatory field omitted in turn (each must be rejected), with a wrong-typed value for each field, and with an undefined extra field; a field the source makes a `shall` boolean is `const: true`, so `false` is rejected.

Source defects and decisions:

- B.2.9 is headed 'Sensitive security parameters management' but the Security Levels table prints 'Sensitive
  security parameter management'; both spellings are used where the source uses them.
- The six 'No change' sections (B.2.5, B.2.6, B.2.8, B.2.10, B.2.11, B.2.12) have no schema; their content is
  the open `content` object of their section.
- Footnote requirements that are `should` (ports map to images, algorithms map to services, SSPs map to
  certificates, I/O method in the Import/Export column) cannot be checked inside one row, so they are fields'
  notes, not schema rules. Footnote 6 (`shall`) is required fields of `RulesOfOperation`.
- One cross-row rule is not enforced: the placements count equal to `total_items` (TamperSealApplication).
  SecurityLevelsTable pins each of its twelve positions to the number and title the table prints.

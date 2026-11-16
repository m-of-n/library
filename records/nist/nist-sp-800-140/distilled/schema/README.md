---
record: nist-sp-800-140
kind: schema
title: "nist-sp-800-140 — schemas"
extracted: "2026-11-15"
reviewed_by: ""
---

# Schemas

SP 800-140 has no formal notation. Each schema describes one evidence framework object or the parts a Vendor Evidence item lists.

## Derived (written by this library)

Every file here is **derived**: `nist-sp-800-140` ships no CDDL, ASN.1 or JSON Schema of its own, so each is a JSON Schema (draft 2020-12, `additionalProperties: false`, `$id: urn:library:nist-sp-800-140:<Name>`) written from the prose or tables the Source lines column names. Nothing here is verbatim.

| file | locator | what it validates | source lines |
|---|---|---|---|
| `Assertion.derived.schema.json` | §6 | one assertion of ISO/IEC 24759 6.x as SP 800-140 modifies it: its id, area, levels and the evidence items under it | L333-334 |
| `EvidenceItem.derived.schema.json` | §5.2 | one Vendor Evidence or Test Evidence item | L290-293 |
| `TestEvidenceResponse.derived.schema.json` | §6 | a CSTL's response to one Test Evidence item (documentation, operational testing, verify / verify by inspection) | L298-319 |
| `ProcessorEvidence.derived.schema.json` | §6.2 | VE02.15.05/06 and VE02.17.04/05: what the vendor identifies for each processor of a hardware or firmware module | L349-354 |
| `HybridModuleDesignation.derived.schema.json` | §6.2 | VE02.18.01: the module is identified as a Hybrid Software Module or a Hybrid Firmware Module | L466-467 |
| `VendorAffirmedSecurityMethod.derived.schema.json` | §6.2 | VE02.20.03/04: one vendor-affirmed security method, listed in the non-proprietary security policy | L505-508 |
| `DataOutputPathSeparation.derived.schema.json` | §6.3 | VE03.07.03-05: how output data paths are separated from SSP processes | L524-540 |
| `AuthenticationDataProtection.derived.schema.json` | §6.4 | VE04.44.01: protection of authentication data against four named threats | L569-572 |
| `AuthenticationFeedbackObscuring.derived.schema.json` | §6.4 | VE04.54.01/02: how feedback of authentication data is obscured | L610-615 |
| `OperatingSystemControls.derived.schema.json` | §6.6 | VE06.11.01: operating system control mechanisms that protect SSPs, control and status data | L643-646 |
| `EnclosureHardness.derived.schema.json` | §6.7 | VE07.26.01/02: strength or hardness of the enclosure, coating or potting and the temperature range the security policy states | L673-677 |
| `EnvironmentalProtectionStatement.derived.schema.json` | §6.7 | VE07.77.01/02 and VE07.81.01/02: which EFP or EFT approach was chosen and the ranges met | L712-726 |
| `SplitKnowledgeEvidence.derived.schema.json` | §6.9 | VE09.23.01/02: split knowledge procedure documentation | L791-802 |
| `SspZeroisationInformation.derived.schema.json` | §6.9 | VE09.28.01: zeroisation information for unprotected SSPs (items a to e) | L825-833 |
| `PlaintextSspZeroisationInformation.derived.schema.json` | §6.9 | VE09.30.01: zeroisation information for plaintext SSPs (items a to e) | L934-942 |
| `ProceduralZeroisation.derived.schema.json` | §6.9 | VE09.28.03: zeroisation performed procedurally under operator control | L838-841 |
| `ZeroisedSspNonRetrievability.derived.schema.json` | §6.9 | VE09.29.01: how a zeroised SSP cannot be retrieved or reused | L894-895 |
| `FunctionalTestingDocumentation.derived.schema.json` | §6.11 | VE11.29.01: functional testing performed on the module | L1021-1023 |
| `CveDisclosure.derived.schema.json` | §6.11 | VE11.38.03: one CVE associated with the module and its disposition | L1050-1054 |

## Rebuild and self-check

`build.derived.py` writes every `*.derived.schema.json` here, `../messages.yaml` and `../examples/*.derived.json`. It resolves every `constrained_by` id from `../requirements.yaml` by script (it raises on 0 or more than 1 match), writes every quotation from the cached source, then validates every case in `../examples/*-cases.derived.json` with the `jsonschema` package (`Draft202012Validator`) and exits 1 on any surprise. Run it with a Python that has `jsonschema` installed, from the repository root:

```sh
python3 records/nist/nist-sp-800-140/distilled/schema/build.derived.py
```

Last run: 19 structures, 286 cases (29 accept, 257 reject), 0 unexpected.

Every structure with a mandatory field is tested with the empty object and with each mandatory field omitted in turn (each must be rejected), with a wrong-typed value for each field, and with an undefined extra field; a field the source makes a `shall` boolean is `const: true`, so `false` is rejected.

Findings from reading the evidence ids by script (22 assertions, 76 evidence items, all with source lines in
`../examples/`): every evidence id carries its assertion's number prefix.
Other source anomalies: TE09.28.01 cites VE09.30.01 (the plaintext assertion's item) from assertion AS09.28, and
NOTE 1 of AS09.28 says the assertion 'is tested AS09.30'; TE02.15.10 and TE02.17.06 verify documentation 'provided
under assertion AS02.02', an assertion this document does not modify.

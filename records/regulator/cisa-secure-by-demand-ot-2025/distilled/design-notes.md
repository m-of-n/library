---
schema: "library-distilled/v1"
id: cisa-secure-by-demand-ot-2025-design-notes
record: cisa-secure-by-demand-ot-2025
type: design-notes
updated: "2026-11-16"
---

# Secure by Demand: Priority Considerations for OT Owners and Operators (CISA and partners, 2025-01-13): design notes for tmodel and mofn

This note covers how the guide bears on `tmodel:R-042`, `tmodel:R-043` and `tmodel:R-044`, the record's `bears_on`. It also bears on `tmodel:DEC-009` and on mofn's software supply-chain target, which no `bears_on` id names yet.

- **Read against** tmodel@ddac1b9: `tmodel:ARCH-0001` and its proposal v0.2.0 §3c, `tmodel:ADR-0012`, `tmodel:ADR-0013`, `tmodel:MAP-0001` v0.2.0, `tmodel:RPT-0013-OM` v0.2.0 (`research/0013-sdl-conformance/sdl-object-model.yaml`) and `spec/schema/tmodel-object-model.linkml.yaml`. One item reads mofn@7c3c731 (`ARCH-0001` v0.3.1). Every tmodel id is written `tmodel:…` (the library's `docs/scope.md`, Two registers), and this note extends the prefix to tmodel's reports, maps and design logs; a bare id is mofn's.
- **What the guide is.** Joint guidance from CISA and eleven partner agencies. Twelve considerations, under the titles of its table of contents. Each has a selection criterion, questions to ask the manufacturer, a reason, a goal sentence and a body; a Summary list restates all twelve. `requirements.yaml` holds 330 entries. By `role`, counted by script: 15 criterion, 46 question (40 in the twelve questions-to-ask lists, 6 threat-model questions), 12 goal, 13 element and 12 seek-out.
- **Source.** `.cache/cisa-secure-by-demand-ot-2025.txt`, sha256 `0a853a7c6ad38050d7c0cd7dabff895089fb3e3fc324140f0cd1ea0b8dbf49cb`, the pinned `source_text_digest`. It renders the PDF whose sha256, `172daac421ad9d3c535cba962f9aa4a3b894065c4c2522bcdbb0f064c6696d16`, equals `content.sha256` and the skeleton's `source_digest`. All three were recomputed in this pass.
- **Ids.** `R-NNNN` means `cisa-secure-by-demand-ot-2025#R-NNNN`. A script emits every id from `requirements.yaml`. It selects by `role`, `consideration`, `kind` and `locator` and by the text (its opening words, or the whole text for a split child), and raises unless exactly one entry matches. The resolved pairs were read back.

## Adopt

### The criteria and questions are a RequirementSource for OT products

This bears on `tmodel:R-044`, on `Requirement` (`tmodel:ADR-0012`) and on `RequirementSource` (`tmodel:ADR-0013`).

- **The source.** `source_ref: library:cisa-secure-by-demand-ot-2025`, with `version: "2025-01-13"`: the guide has no version number, so its date names the edition. Its scope is a product family (R-0207), which goes in `applies_to_family`; see the `tmodel:DEC-009` item under Adapt.
- **The members** are the 15 criterion entries and the 46 question entries.
  - The 12 goals are left out. Each states a purpose and is `testable: no`.
  - The Summary's 13 elements and 12 seek-outs are left out as members, because they restate the sections. Where the Summary asks for more, the library's inferred entries carry the stricter reading: R-0319, R-0327, R-0328 and R-0329 (open question 2).
- **Wording.** The guide is TLP:CLEAR:

<!-- q L24-25 "Subject to standard copyright rules" .. "without restriction." -->
> Subject to standard copyright rules, TLP:CLEAR information may be distributed without restriction.

  That is a distribution marking which defers to copyright, not a licence. `tmodel:ADR-0012` allows `text_origin: verbatim` only where the source's licence permits it, so whether a criterion may travel verbatim turns on a licence the guide does not state (open question 7). A paraphrase with the library id is safe either way, and the questions cannot be verbatim requirements in any case (next point).
- **A question is not a statement a product meets.** Its truth condition is ours. `favourable_answer` gives 37 yes, 2 no, 6 open and 1 none over the 46 questions, and R-0322 records that the guide states none of them.
  - A yes-or-no question becomes a declarative Requirement: `text_origin: paraphrase`, with the question's `source_locator`. A link to the source that an AI proposes stays a `proposed` Assertion until a human Review accepts it, under the review rule of `tmodel:ADR-0012`.
  - The 6 open questions ask for information: R-0144, R-0266, R-0270, R-0271, R-0272, R-0273. Each becomes a `documentation` Requirement. The manufacturer's written answer is `Evidence` for it, not what discharges it (`satisfied_by` ranges over Mitigations), and whether the answer is adequate is the buyer's Review.
  - The one question whose answer neither meets nor fails anything, R-0143, asks whether the product ever communicates back to the manufacturer. It is threat-model input, not a Requirement: a yes is a `DataFlow` from one of the product's `Component`s to a manufacturer-owned `Component` across a `TrustBoundary` (`tmodel:ADR-0011`).

### The threat-modeling consideration describes the threat model a manufacturer shows a buyer

This bears on `tmodel:R-043` and on `ThreatModel` and `GovernedView` (`tmodel:DEC-001b`, open).

- The criterion asks for a complete, detailed threat model (R-0265), and the Summary asks that it be current (R-0196). The questions ask whether the manufacturer can articulate the attack vectors (R-0142), which measures reduce them (R-0266) and whether it has a roadmap for the gaps (R-0267).
- That is the governed view of `tmodel:R-043`, seen by a party outside the producer. The buyer needs a revision, a date and a sign-off it can compare between purchases. `ThreatModel.revision`, `updated` and `approved_by` carry them, with `approval_digest` pinning the sign-off to a state, and all of them are still `tmodel:DEC-001b`. The roadmap is `tmodel:RPT-0013-OM` `ActionPlan`, and who may see the model is the `audience` tier of its governed view. Neither is in the schema: the governed view is open under `tmodel:DEC-001b`, and no class holds a roadmap.
- The 6 threat-model questions are a content checklist, and each lands on a class the core already has:

  | question | where tmodel holds the answer |
  |---|---|
  | R-0270: security products, controls and policies the manufacturer assumes protect the product | a `Mitigation` whose `implementation_owner` is the operator, or an `Environment` assumption |
  | R-0271: communication capabilities | `DataFlow`, with its `protocol` and `carries` slots |
  | R-0143: communication back to the manufacturer | a `DataFlow` across a `TrustBoundary` (above) |
  | R-0144: intended environment and secure use | `Environment`, with the hardening guidance as `Evidence` |
  | R-0272: common classes of coding error | `Weakness` (CWE), which a Requirement `addresses`; a Mitigation `mitigates` the ThreatInstance that exploits it |
  | R-0273: protection against supply-chain attacks | supply-chain `AttackPattern`s such as CAPEC-538 and CAPEC-439, which `spec/vectors/sdl-01-tmodel-desktop.yaml` already holds, joined there to its threats through proposed Assertions (no slot links a `ThreatInstance` to an `AttackPattern`), with the `Mitigation`s of those threats |

- **Threat sources.** The guide asks for threat models that track public threat sources, and names one:

<!-- q L713-714 "Buyers should seek out threat models" .. "modern threat actor capabilities." -->
> Buyers should seek out threat models that track and incorporate threat sources, such as MITRE EMB3D, so that threats are aligned with modern threat actor capabilities.

  `catalog_ref` names CWE, CAPEC, ATT&CK, CVE and D3FEND. EMB3D is not among them, and the library holds no EMB3D record. The slot leaves its schemes unpinned, so an EMB3D `AttackPattern` needs only an agreed identifier form; the vectors write the others bare (`CAPEC-538`).
- **Logging depends on the threat model.** The log types beyond the minimum come from the manufacturer's threat model (R-0022; R-0320). In tmodel that is a detection `Mitigation` for each `ThreatInstance`, which `tmodel:RPT-0013-OM` names `threat_model_drives`.

### mofn: checking that an update is authentic is a question SC-1 answers

This bears on mofn's software supply-chain target (`ARCH-0001` §2.3.1), on `R-M-07` and on `R-I-07`.

- The guide asks whether the buyer can verify that an update is authentic (R-0294), and it asks for the controls that protect the update pipeline:

<!-- q L852-855 "For verification" .. "updates are legitimate." -->
> For verification, buyers should be able to reliably determine the authenticity of an update. The delivery mechanism for that update needs to be over a secure channel to help guarantee integrity. Buyers should ask for the security controls the manufacturer uses to protect the update development, build, and delivery pipeline to help ensure their updates are legitimate.

- mofn's artifact statements answer both. A statement over the update's digest (`R-M-07`), signed by a key the buyer trusts for releases, shows that the update is authentic. SC-1's build-provenance statement, with SC-2 where that authority is delegated, gives the buyer a machine-checkable answer for the build part of the pipeline the guide asks about; development and delivery it does not cover. The guide keeps authenticity apart from transport: the secure channel is there for integrity (R-0299). Once an update is copied onward, for example on removable media into an isolated OT network, the channel says nothing about its origin, while a signed statement still verifies.
- The guide asks whether the manufacturer has produced an SBOM (R-0276), in a common machine-readable format (R-0147). In mofn that travels as SPDX or CycloneDX inside an `ArtifactStatement` predicate (`R-I-07`).
- **Where the guide stops short.** It never says whose key, never asks for more than one approver and names no format. Its freight-rail example is multi-factor authentication by one engineer, not approval by several:

<!-- q L675-677 "For example, in the Freight Rail Subsector" .. "signaling logic." -->
> For example, in the Freight Rail Subsector it is commonplace for wayside interface units to require a local button press on the controller and a dynamic code along with a password to change vital (safety-critical) signaling logic.

  So it does not bear on threshold principals (G4, `R-M-06`).
- OT is not one of mofn's two targets (`ARCH-0001` §2.3, scoped by MD-1: the software supply chain, and archives), and §2.3.3 leaves IoT onboarding unscoped. This record is therefore a consumer of the supply-chain target, and no mofn DEC changes.

## Adapt

### Most of the twelve are product capabilities, which `tmodel:MAP-0001` holds only as CRA product properties

This bears on `tmodel:R-044` and `tmodel:MAP-0001` v0.2.0.

- The guide publishes no item-level mapping. Its alignment statement is about the document as a whole:

<!-- q L270-274 "Note: This guidance aligns" .. "Cyber Resilience Act (CRA)." -->
> Note: This guidance aligns with established cybersecurity standards, including National Institute of Standards and Technology (NIST) 800-213a for industrial internet of things or NIST 800-82 for OT and Security Level 3 of ISA/IEC 62443-4-2 and 62443-3-3 for cybersecurity features in industrial automation and control systems. 8 This guidance aligns to technology-neutral and objective-oriented approaches contemplated by the Cyber Resilience Act (CRA).

  So every placement below is ours. `tmodel:RPT-0013-OM` already records the guide's alignment as document-level, not item-level.
- `tmodel:MAP-0001` crosswalks 34 rows of secure-development practice. The guide asks largely for product properties. By `actor`, counted by script: 10 of the 15 criteria and 23 of the 46 questions are about the product, 4 criteria and 23 questions are about the manufacturer, and one criterion is about both.

  | consideration | `tmodel:MAP-0001` rows (ours) | `requirement_kind` |
  |---|---|---|
  | Threat Modeling | 3 | process, documentation |
  | Vulnerability Management | 17, 18, 20, 22, 23, 24, 25 | process, documentation |
  | Upgrade and Patch Tooling | 24, 25 | process, technical |
  | Secure by Default | 14 | technical |
  | Strong Authentication | 33, for shared role-based passwords; 2 and 4 for access control, through CRA Annex I Part I(2)(d) | technical |
  | Secure Communications | 6, for cryptographic agility only | technical |
  | Configuration Management, Protection of Data, Secure Controls | 2 and 4, through CRA Annex I Part I(2)(e), (f) and (h) only | technical |
  | Logging in the Baseline Product, Open Standards | none | technical |
  | Ownership | none | organizational, other (support contracts, warranty terms) |

  The cryptographic agility the Secure Communications row rests on:

<!-- q L576-578 "buyers should ask for products that support" .. "long lifecycles of products." -->
> buyers should ask for products that support cryptographic agility to allow system upgrades if a product’s cryptography becomes vulnerable. Cryptographic agility is particularly useful in OT due to the long lifecycles of products.

- **Logging is not row 19.** Row 19 is the producer's own monitoring and incident response. `tmodel:MAP-0001`'s own adversarial review lists product logging features placed there as weak placements (CRA I(2)(l), FDA App1.F-04 and F-06).
- **Rows 2 and 4 are a precedent, not a home.** They carry the CRA's Annex I Part I(2) product properties because ETSI Annex A maps them to SSDF PO.1.2, PW.1.2 and PW.1.3, and `tmodel:MAP-0001` notes there that they are product-property requirements, not a design-process duty. Confidentiality (e), integrity of data, commands and configuration (f) and availability of essential functions (h) are where Configuration Management, Protection of Data and Secure Controls would land by that precedent, and access control (d) is where Strong Authentication would; nothing in the guide maps them.
- **So two paths, both existing.** A technical criterion is a product `Requirement` that no `SdlPractice` implements, discharged by a product `Mitigation` through `Requirement.satisfied_by` (core). Only the process subset goes through `SdlPractice.implements` (`tmodel:ADR-0013`). No schema change is needed.

### A buyer's verdict is per Requirement, over the manufacturer's evidence

This bears on `tmodel:R-042` (`Requirement.conformance_status`, `tmodel:DEC-001b`) and on `Evidence` (`tmodel:ADR-0013`).

- `tmodel:R-042` as drafted is the producer's check, run at a Gate: a threat model is conformant when every in-scope ThreatInstance has an approved, evidenced Mitigation. Here the checker is the buyer and the evidence is the manufacturer's. The guide sets no threshold for a whole product (R-0312) and no order among the twelve (R-0313):

<!-- q L260 "These elements" .. "priority order." -->
> These elements are not in priority order.

- So use `RequirementConformanceStatus` per Requirement and stop there.
  - `not_assessed` until the manufacturer answers.
  - A qualifier the guide never quantifies decides 10 of the 15 criteria and 15 of the 46 questions (`testable: partial`, by script). That is an adequacy call for the buyer's Review: `conformance_status` records linkage and approval, not adequacy, so `partial` there means a link or approval is missing, not that the qualifier is half met.
  - `conformant` only with a buyer's approving Review.
- **Who produced the evidence matters.** A manufacturer's answer is a claim; a buyer's test is a check. `Evidence` has no producer slot (`gathered_by` is deferred by `tmodel:ADR-0013`). Record the answer as an Assertion `asserted_by` the manufacturer's `Party`, with an opaque reference to the answer's `Evidence` in its `evidence` slot (a string slot, not the `Evidence` class; `tmodel:ADR-0013`), and let the buyer's Review decide it.
- **Judge the baseline product.** Conformance is judged on the product as sold, without paid options (R-0316). Logging is no add-on (R-0017), and every version carries every security feature (R-0180). `Evidence.about_version` names a version, not a commercial edition. Until tmodel models editions, model the baseline edition as its own `Product` and judge that one.
- `tmodel:RPT-0013-OM`'s `profile_selects` edge (a buyer prioritizes elements) is the buyer's own selection among the twelve. That is a `RequirementProfile`, which `tmodel:ADR-0013` defers, and it belongs to the buyer, not to the guide.

### OT products are a product family, and the guide subdivides it

This bears on `tmodel:DEC-009` (open), on `tmodel:R-020` (mapping a generic threat onto a product and a product family) and on `applies_to_family` (`tmodel:ADR-0012`).

- `tmodel:DEC-009` is the mapping of generic threats onto products and product families. The guide's premise is the case for it: threat actors target products, not organizations, so what is known about a threat follows the product across every organization that buys it:

<!-- q L222-224 "Threat actors are successfully targeting" .. "points to control systems." -->
> Threat actors are successfully targeting particular OT products, rather than specific organizations, because vulnerabilities span multiple victims and critical infrastructure sectors, and OT products can be access points to control systems.

- Its scope is a family (R-0207): OT products, with industrial automation and control systems singled out. It also subdivides that family. MFA from supervisory control is asked of every IACS baseline (R-0141), while tiny sensors and cheap components may go without it for now (R-0140).
- `tmodel:ADR-0012` scopes a family by a string matched against `Product.classifications`. It is not an edge, so the graph cannot hang properties on a family (its trade-off (a)), and nothing relates one family to another. Two levels, OT products and supervisory IACS components within them, need either two classification values on every product or the ProductFamily class that `tmodel:DEC-009` may add. This guide is evidence for that class.

### ISA/IEC 62443 Security Level 3 is product assurance, not maturity

This bears on `tmodel:R-044`, on `RequirementSource` (`tmodel:ADR-0013`) and on finding C1 and disagreement D2 (what a level measures) of `tmodel:RPT-0013-OM`'s report, `sdl-object-model.md` v0.2.1.

- The guide names 62443 in four places, three in its text and one in a footnote. It asks buyers to look for manufacturers that adopt 62443 standards (R-0105). It aligns with Security Level 3 of 62443-4-2 and 62443-3-3 (quoted above). And it asks whether the manufacturer demonstrates alignment (R-0225). Its footnote 7:

<!-- q L279-282 "The ISA/IEC 62443" .. "development lifecycles." -->
> The ISA/IEC 62443 multi-part standard is internationally recognized as defining requirements and processes for implementing and maintaining electronically secure OT products, systems, and development lifecycles.

- Security Level 3 of 62443-4-2 and 62443-3-3 is a capability level of a component or system. In `tmodel:RPT-0013-OM` it would be an `AssuranceLevel`, which may feed a gate; the placement is ours, since its listed levels name no 62443 security level. It is not the maturity level of 62443-4-1, which finding C1 keeps out of gates. As a tmodel object it is a `RequirementSource` that names a level of a standard, which `tmodel:ADR-0013` allows, as it does for SLSA Build L2.
- **The library cannot follow the alignment yet.** It holds `iec-62443-4-1-2018`, the development-lifecycle part, which only footnote 7's last words point to. It holds no record for 62443-4-2 or 62443-3-3. `spec/vectors/sdl-01-tmodel-desktop.yaml` carries 62443-4-1 as a source with no members, and a proposed Assertion excludes it because the desktop app is not an IACS component.
- **An alignment is not an overlap.** No criterion is mapped to any 62443 requirement, and the guide names no evidence of 62443 adoption (R-0315). So no `maps_to` edge can be built from it.

## Reject or hold

### Reject reading must, need or should as mandatory

This bears on `normativity` (`tmodel:ADR-0012`).

- The guide binds no one (R-0311). Its disclaimer:

<!-- q L922-924 "This document is without prejudice" .. "implementation of such legislation." -->
> This document is without prejudice to any type of legislation that is applicable in the jurisdictions of CISA and its co-sealers. This document does not bind CISA and its co-sealers and is not intended to provide guidance on the implementation of such legislation.

- Six entries are worded as requirements (must, need, it is essential): R-0013, R-0050, R-0060, R-0079, R-0275, R-0299, found by script. They import as `recommended`, like the rest. A buyer who writes one into a contract makes it mandatory in its own `RequirementProfile`, not in this source.

### Reject a score, a ranking or a pass for the whole product

- The guide calls its elements priority considerations, but it orders none of them (R-0209), weights none and sets no threshold (R-0312). A tool that adds up the twelve, or weights some above others, applies a method the guide does not have.

### Hold: the laws it cites are their own sources

- NIS2, the delegated regulation under the Radio Equipment Directive and the CRA's CE marking are legal duties (R-0205, R-0206). Each needs its own `RequirementSource`. The guide disclaims interpreting EU law (R-0164) and offers itself to entities under Union law for information only (R-0167). Of the three, only the CRA has a library record (`eu-cra-2024-2847`).

### Hold: documents it points to that the library does not hold

- It offers BSI TR-03191 as a basis for procurement requirements, and footnote 8 points to a profile that was still forthcoming:

<!-- q L792 "Information in BSI TR-03191" .. "procurement requirements." -->
> Information in BSI TR-03191 may provide the basis for procurement requirements.

<!-- q L283 "NSA recommends" .. "profile in ISA." -->
> NSA recommends maintainers of National Security Systems (NSS) use the forthcoming OT NSS profile in ISA.

- The library also holds no record for NIST SP 800-82, NIST SP 800-213A, MITRE EMB3D, CSAF or RFC 9116, all of which the guide names. It does hold the two vulnerability-handling standards the guide names, `iso-iec-29147-2018` and `iso-iec-30111-2019`.
- **Its own series.** The guide places itself in a series and cites no other document in it:

<!-- q L218 "This document is part of" .. "Secure by Demand series" -->
> This document is part of CISA’s Secure by Demand series

  It does cite the manufacturer-side guide, `cisa-secure-by-design-2023`. Buyers are to check that their manufacturers know its three principles (R-0010), and the only evidence of adoption the guide names is a published roadmap (R-0106). The series' guide for software buyers is `cisa-secure-by-demand-guide-2024`.

## Open questions and source defects

### 1. One section prints a different label for its questions

<!-- q L554 "Key considerations:" .. "certificates for devices?" -->
> Key considerations: Does the product simplify the deployment and renewal of certificates for devices?

- Secure Communications introduces its questions as key considerations. A parser keyed on the label the other eleven sections use misses R-0247 and R-0248; `requirements.yaml` files both under `question_set: questions to ask`.
- Its criterion (R-0135) is also one of only two phrased with should; the other is R-0145. The remaining 13 criterion entries carry no verbal form.

### 2. The Summary and the sections disagree

Each pair, with the inferred entry that reconciles it:

- **Insecure protocols.** The Summary gives examples (e.g.) and names SSL and TLS 1.0/1.1 (R-0183):

<!-- q L106-107 "use secure up-to-date versions" .. "disabled by default;" -->
> use secure up-to-date versions of protocols with older insecure protocols (e.g., SNMPv1/2, Telnet, SSL, TLS 1.0/1.1) disabled by default;

  The question introduces its list with i.e. and names TFTP instead (R-0240):

<!-- q L487-488 "Are older insecure protocols" .. "[TFTP])?" -->
> Are older insecure protocols disabled by default (i.e., SNMPv1/2, Telnet, Trivial File Transfer Protocol [TFTP])?

  Read literally, i.e. makes the question's list complete, and a product with TLS 1.0 enabled would pass it. R-0319 takes the union.
- **Bill of materials.** The Summary asks for hardware and software (R-0200); the section asks only for software (R-0276). R-0327 reconciles them.
- **MFA.** The Summary element (R-0193) and the body (R-0068) ask for phishing-resistant MFA; the criterion (R-0258) and the question (R-0260) do not. R-0329 reconciles them.
- **Moving to a supported operating system.** The Summary triggers it before the original leaves support (R-0204); the criterion triggers it once the original has left (R-0289). R-0328 reconciles them.

### 3. Two cross-references name sections that do not exist

- A Vulnerability Handling section (L857; R-0326) and a Threat Model section (L364-365). The sections are Vulnerability Management and Threat Modeling.

### 4. A wrong standard designation, and an example that is not a standard

<!-- q L402-404 "These standards might apply" .. "cross-vendor communication." -->
> These standards might apply to logging formats (sysmon), networking protocols (OPC-UA), programming languages (IEEE 61131-3), encryption protocols (TLS), or any element of a device that would benefit from cross-vendor communication.

- The PLC programming-language standard is IEC 61131-3, not an IEEE standard. A tool mapping the guide's examples to standard ids must correct it.
- Sysmon is a Microsoft Sysinternals monitoring tool, not a published log-format standard. The criterion asks for open standard logging formats (R-0218), and the guide's only example names no standard a tool could check a product against.

### 5. tmodel's reading of this record predates FX-1

- `tmodel:RPT-0013-OM` cites this record by page (for example pp.3, 7 and p.17), from its pre-FX-1 object model. It records an edge in which the threat model assumes a Standard, at p.17. The question there is about assumed security products, controls and policies, not standards (R-0270):

<!-- q L727-728 "What security products" .. "protecting the product?" -->
> What security products (e.g., EDR, network monitoring, firewalls) or security controls and policies (segmentation, password policies) does the manufacturer assume are protecting the product?

  The target is a `Mitigation` or an `Environment` assumption (the table under Adopt).
- The FX-1 entries now give each of its objects a line-exact home. Its SelectionCriterion object, for example, is the 15 criterion entries. A Selection criteria paragraph holds one to three of them: three in Vulnerability Management, two in Upgrade and Patch Tooling.

### 6. Minor wording defects

None of these changes a check: a stray comma in the first logging question (R-0219, L340), a missing word, of (L396), a missing noun after CERT/CC's (L801), application where applicable is meant (L767) and operation system for operating system (L143).

### 7. May tmodel carry the criteria verbatim?

- The guide is TLP:CLEAR and distributable without restriction, subject to copyright (Adopt, first item). Several co-sealers are not U.S. federal agencies, so U.S. public-domain status cannot be assumed for the whole text. `tmodel:ADR-0012` allows `text_origin: verbatim` only where the source's licence does, and names no one to decide it; until the licence is settled, paraphrase with the library id.

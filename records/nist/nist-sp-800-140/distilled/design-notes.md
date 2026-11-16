---
schema: "library-distilled/v1"
id: nist-sp-800-140-design-notes
record: nist-sp-800-140
type: design-notes
updated: "2026-11-15"
---

# NIST SP 800-140 (FIPS 140-3 DTR): design notes for tmodel and mofn

This note covers how SP 800-140 bears on `tmodel:DEC-009`, the record's `bears_on`, and on mofn's key handling, which no `bears_on` id can name (see the mofn items).

- **Read against** tmodel@ddac1b9 and mofn@10e357f, as the `fips-140-3` notes are. A tmodel id is written `tmodel:…`; a bare id is mofn's.
- **What it is.** The CMVP's changes to the test requirements of ISO/IEC 24759 for FIPS 140-3. It modifies 22 assertions (`ASnn.nn`), each with the vendor evidence (`VE…`) and test procedures (`TE…`) it changes, across §6.2 to §6.11; §6.1, §6.5, §6.8 and §6.12 say No change. A script counted the assertion headings.
- **What it leaves out.** Every test requirement it does not change stays in ISO/IEC 24759 (R-0142), which the library holds only as the queued record `iso-iec-24759`, with no digest.
- **Source.** `.cache/nist-sp-800-140.txt`, sha256 `b1c2fe61dab70b77778185fb487e451b1cf6286d88dbe8b4b894fa93f61a041e`, the pinned `source_text_digest`. It renders the PDF whose sha256, `dfb6d1b9c829c3d8caad960a4d0e3bcc076852604061dd755718c259d79fc3f7`, equals `content.sha256` and the skeleton's `source_digest`. All three were recomputed in this pass.
- **Ids.** `R-NNNN` means `nist-sp-800-140#R-NNNN`. A script emits every id from `requirements.yaml`: it selects the entry whose `source_lines` start on a given line, narrowed by a phrase of its text, and raises unless exactly one matches.
- **Entries that share a text.** `bin/check-id-joins --surface` finds six groups, 15 entries in all. The one this note cites is R-0010 (TE02.15.11, hardware) and R-0021 (TE02.17.07, firmware), the same sentence; it cites each where it means that module type.

## Adopt

### AS11.38: a CVE disposition per module is tmodel's per-product override

This bears on `tmodel:DEC-009` (generic threat to product), on `tmodel:R-021`, on `tmodel:R-010` (`tmodel:DEC-008`), and on the Assertion and Review spine (`tmodel:DEC-001a`, `tmodel:ADR-0010`).

<!-- q L1050-1054 -->
> VE11.38.03: The vendor shall list any CVEs associated with the module, and either - provide assurance that they are not security relevant; - or, for any CVE’s that are considered security relevant, the vendor shall describe how they have been mitigated.

<!-- q L1058-1061 -->
> TE11.38.03: The tester shall verify that any CVEs associated with the module: - are not security relevant, or, - if they are security relevant, mitigations provided by the vendor are appropriate.

- R-0137 obliges the vendor to list every CVE associated with the module. Each is then either not security relevant (R-0234) or mitigated as described (R-0138). R-0139 has the tester verify the disposition and judge whether each mitigation is appropriate.
- That is the shape of tmodel's vector `spec/vectors/mvp-18-shared-vuln-vex-override.yaml`: a finding on a shared crypto core, overridden for one product by an Assertion and its Review. The vendor's disposition is the proposed Assertion, `asserted_by` the vendor. The tester's verification is the Review.
- The disposition reaches the laboratory, not the public. SP 800-140B's security-policy template has no CVE table (the word does not occur in it), so tmodel cannot import these dispositions from a published policy.

### §6: a yes or no is not evidence

This bears on `Evidence` (`tmodel:ADR-0013`) and on the R-042 verdict (`tmodel:DEC-001b`).

<!-- q L298-300 -->
> In responding to test evidence (TE), a yes/no answer does not provide sufficient assurance. CMVP requires the following information when responding to a documentation, operational testing, or verify/verify by inspection requirement.

- R-0157 rejects a bare answer. For each TE the CMVP wants the documentation cited and summarised (R-0159), the test method, tools and results (R-0160), or the inspection method with its detailed results (R-0161).
- That is `tmodel:ADR-0013`'s rule for Evidence: it shows linkage, and a person judges adequacy. Documentation and operational testing map onto `evidence_kind` `document` and `test_suite`, each with a `locator`. Inspection has no `EvidenceKind`; today it can only be a `document` that describes the inspection.

### §6.2: boundaries by embodiment, and labelled flows

This bears on `TrustBoundary`, `Component` and `DataFlow` (`tmodel:ADR-0011`, `tmodel:DEC-001a`) and on the instance types of `tmodel:ADR-0002` (`tmodel:DEC-005`).

<!-- q L455-459 -->
> The cryptographic boundary of a hybrid cryptographic module shall: - be the composite of the module’s hardware component boundary and the disjoint software or firmware component(s) boundary; and - include the collection of all ports and interfaces from each component.

- R-0003 (hardware), R-0016 (firmware) and R-0027 (hybrid, quoted) say what each module's cryptographic boundary must delimit. R-0028 makes the vendor declare which kind of hybrid a module is.
- A boundary is a `TrustBoundary`, and the parts inside it are Components `in_trust_zone` of it. The hybrid boundary is one zone whose members are disjoint hardware and software or firmware parts, with the ports and interfaces of each. tmodel's zones nest, and nothing stops one zone holding both parts.
- The block diagram must label every interconnection with the type of information it carries: R-0010 for hardware modules and R-0021 for firmware modules. In tmodel that is `DataFlow.carries`. A flow that carries no Asset would fail this TE.

### §6.9: zeroisation is the bar for the wallet's wipe (mofn)

This bears on mofn's `PLAN-0004` §6.1 (proposed: the plaintext key exists only inside the engine, for one signature, and is then wiped), on `PLAN-0004` §6.2 (engine v0 wipes the seed in `signer.sign`), and on `DECISIONS-0001` item 28 (Python throughout, DL-0038). None of them is a DEC.

- R-0095 requires methods to zeroise every unprotected SSP, R-0111 that a zeroised SSP be neither retrievable nor reusable, and R-0116 gives overwriting with zeros, ones or random data as examples.
- For values held only for a moment, AS09.28's NOTE 2 states the same expectation as a recommendation:

<!-- q L885-886 -->
> NOTE 2 Temporarily stored SSPs and other stored values owned by the module should be zeroised when they are no longer needed for future use.

- TE09.28.02 is a test the wallet can adopt as written: initiate zeroisation, then try to use each SSP and confirm it cannot be accessed (R-0103, R-0104, R-0105). For the engine: sign, then search the engine's memory for the seed.
- `PLAN-0004` §6.2 calls engine v0's wipe "best effort in Python". Whether a Python engine can meet R-0111 at all is open question 7.

### §6.4: authentication data (mofn)

This bears on `PLAN-0004` §6.1 (the passphrase prompt) and on the Textual UI (`DECISIONS-0001` item 28).

- R-0046 protects authentication data against unauthorised use, disclosure, modification and substitution. R-0056 obscures its feedback from anyone but the operator.
- `PLAN-0004` §6.1 already keeps the passphrase off the command line and out of logs. The two assertions add that the Textual prompt must not echo it, and that a later OS keychain holding the passphrase is authentication data under R-0046.

## Adapt

### Level applicability is data, and a text-only import flattens it

This bears on `Requirement` (`tmodel:ADR-0012`), on `RequirementSource` and the deferred `RequirementProfile` (`tmodel:ADR-0013`, `tmodel:DEC-001b`), and on `tmodel:DEC-009`.

- Every assertion heading names the levels it applies at. Over the 22 headings, by script: 14 apply at all four levels, 3 at Levels 2 to 4, 2 at Levels 3 and 4, and 3 at one level only (AS06.11 at Level 2, AS07.81 and AS09.23 at Level 3).
- tmodel has `normativity: conditional`, and the ETSI EN 304 223 notes kept conditions in the text. A level is different: a RequirementProfile will select requirements by it, so it should be a slot holding the set of levels, not words in the text.
- In the skeleton's texts a heading survives only where it shares a span with the assertion's first sentence: R-0039 begins with AS03.07's heading, R-0003 does not carry AS02.15's. Pass 1 made each of the other 13 headings an entry of its own (R-0163 for AS02.15) and set `levels` by script on every entry under an assertion. A converter must read that key: from the texts alone it finds the levels of 9 assertions in their first entry and of the other 13 only in a separate heading entry.

### The text layer cannot show what was added or deleted

This bears on the import from the library's requirement format, which `tmodel:ADR-0012` leaves outside its scope (`tmodel:DEC-002`, `tmodel:RPT-0017`), and on `text_origin`.

- R-0002 says a modification marks additions by underline and deletions by strikethrough. The pinned `pdftotext` rendering keeps neither mark, so deleted and added words read as one text. Three places where that reads wrong:
  - VE02.18.01 a) gives two ranges of VE numbers side by side (R-0029):

<!-- q L469-471 -->
> a) For Hybrid Software Module components, the vendor documentation shall provide information required under VE02.15.01 through VE02.15.04 VE02.15.06 and VE02.16.01 through VE02.16.03.

  - TE09.23.02 runs two different rationales together, the second starting mid-sentence (R-0092):

<!-- q L806-809 -->
> TE09.23.02: The tester shall verify the vendor provided documentation provides a rationale that no information is gained without knowing all the necessary split keys. that the output of CSPs under split knowledge procedures does not result in the output of a single component that can be used to construct the original CSP.

  - AS09.29's NOTE 1 names the same document twice, once as this document and once as International Standard (R-0214):

<!-- q L913-915 -->
> NOTE 1 Zeroisation of protected PSPs, encrypted CSPs, or CSPs otherwise physically or logically protected within an additional embedded validated module (meeting the requirements of this document International Standard) is not required.

- So no text in this record can be trusted to say which words are in force, and `text_origin: verbatim` does not make an imported text authoritative. A tmodel import should mark these entries for checking against the PDF, where the marks survive.

### Self-tests: run the conformance vectors when the wallet starts (mofn)

This bears on mofn's `SPEC-0002` §6.3 (a library verify function that accepts small-order keys or S ≥ L must not be relied on alone) and `SPEC-0001` §4.2 (a Statement Verifier passes `SPEC-0002` Appendix A).

- R-0127 and R-0128 require every self-test to run, with the module deciding pass or fail itself and with no external input. R-0129 puts a module that fails one into an error state.
- mofn checks a library against `SPEC-0002` Appendix A once, as a conformance class. The FIPS pattern repeats the check at run time. A Wallet could run the negative vectors N-4 (a small-order key) and N-5 (S ≥ L) before its first verification, and refuse to sign or verify if either is accepted.
- This is a proposal for `SPEC-0001` §4.2. No DEC rests on it.

## Reject or hold

### Reject (mofn): split knowledge is not an m-of-n threshold

This bears on `ARCH-0001` G4 and R-M-06, `SPEC-0002` §8.6 and `SPEC-0004` §6.4 and §11.5. mofn's wallet survey (`research/0002-wallets/report.md`) already recommends refusing to treat OpenPGP's split-key flag as m-of-n.

<!-- q L784-788 -->
> AS09.23: (Sensitive security parameter entry and output – Level 3) {If the module employs split knowledge procedures, the module shall employ separate identity-based operator authentication for entering or outputting each key component,} and at least two key components shall be required to reconstruct the original cryptographic key.

<!-- q L791-802 -->
> VE09.23.01: The vendor documentation shall specify the number of components that are required to construct the original CSP. VE09.23.02: If knowledge of the number of key components is required to reconstruct the original key, the vendor provided documentation shall include rationale stating how knowledge of any one less than the number of key components provides no information about the original key other than the length.

- **Different objects.** R-0088 splits one key into components and needs at least two to rebuild it. R-0089 and R-0090 ask how many components rebuild it, and why one fewer tells nothing but the key's length. A mofn threshold never forms a key. It counts statements by distinct kids (`SPEC-0004` §6.4), and `SPEC-0002` §8.6 allows a threshold of 1.
- **What does carry over.** The braced clause of AS09.23 ties each component to a separate identity-based operator authentication. The braces seem to mark a clause another assertion tests, as AS10.01 and AS10.02 brace the two halves of one sentence; that reading is ours. `SPEC-0004` §11.5 counts kids and leaves it to whoever sets the threshold to stop one party holding several keys, and `ARCH-0003` W-24 counts keys delegated from one identity key once. The FIPS rule is the module-side answer to the same worry. It is not a mechanism mofn can take over.

### Reject (tmodel): this record as the DTR

This bears on `RequirementSource` (`tmodel:ADR-0013`).

<!-- q L198-203 "Unless otherwise specified" .. "ISO/IEC 24759." -->
> Unless otherwise specified in this document, the test requirements are specified in ISO/IEC 24759.

- A RequirementSource built from this record holds the 22 changed assertions, not the test requirements. The rest is ISO/IEC 24759, which tmodel can only paraphrase (`tmodel:ADR-0012`). The `fips-140-3` notes propose how to carry a source that edits another.

### Hold: the vendor-affirmed lists

This bears on `tmodel:DEC-009` and on the review rule of `tmodel:ADR-0012`.

- R-0035 and R-0036 make the vendor list its vendor-affirmed security methods, in its documentation and in the public policy. R-0037 and R-0038 have the tester check that list and the documentation of how each method conforms. Nothing in the procedure tests the methods.
- The record never defines vendor affirmed. SP 800-140B uses the words for operational environments the laboratory did not test, and its footnote 3 for approved algorithms the CAVP cannot test yet (`nist-sp-800-140b` notes). No other record of the family uses them.
- In tmodel each is a claim by the vendor whose Review rests on documents alone. Hold the mapping until a definition is found; none of the eight records gives one.

## Open questions and source defects

### 1. AS09.28 and AS09.30 each say the other tests them

<!-- q L883 -->
> NOTE 1 This assertion is tested AS09.30.

<!-- q L930 -->
> NOTE 1 This assertion is tested in AS09.28.

- R-0210 and R-0217 point at each other, and both assertions carry test procedures of their own. One of the two notes may be struck through in the PDF; the text layer cannot tell (see the Adapt item on marks).

### 2. TE09.28.01 checks AS09.30's vendor information, not AS09.28's

- R-0100 has the tester verify the information VE09.30.01 lists. AS09.28 has its own list, VE09.28.01 (L825–L833). The two lists differ in one word: unprotected SSPs in VE09.28.01, plaintext SSPs in VE09.30.01.

### 3. Unprotected or plaintext

- The two words alternate across §6.7 and §6.9 and sometimes stand side by side. VE07.77.01 b) and VE07.81.01 c) both read as zeroising all plaintext unprotected SSPs (R-0191, R-0195), which looks like a struck word kept beside its replacement.
- Which term governs decides what a module must zeroise. tmodel would model the obligation differently for each.

### 4. One section, two editions of ISO/IEC 19790

- TE09.28.04 accepts SSPs kept inside an embedded module validated to ISO/IEC 19790, with no edition (R-0207). TE09.30.04 says ISO/IEC 19790:2012/Cor.1:2015 (R-0126). §2 pins the 2012 edition with the 2015 corrections.

### 5. Where the CMVP's authority to modify comes from

<!-- q L136-141 "As a validation authority" .. "ISO/IEC 24759." -->
> As a validation authority, the Cryptographic Module Validation Program (CMVP) may modify, add or delete TEs and/or VEs as specified under paragraph 5.2 of ISO/IEC 24759.

- This record cites paragraph 5.2 of ISO/IEC 24759. SP 800-140A's abstract cites paragraph 5.2 of ISO/IEC 19790, SP 800-140B's cites paragraph 6.14 of ISO/IEC 24759, and FIPS 140-3 §1 says only paragraph 5.2 (each record's notes). The family names three different sources for one authority. The library cannot check any of them: both ISO/IEC standards are paywalled.

### 6. No revision history

- The Document Revisions table at the end (L1081–L1088) is empty in the rendering. Nothing in the record says whether it has been revised since March 2020.

### 7. Can a Python engine zeroise? (mofn)

- R-0111 asks that a zeroised SSP not be retrievable. `PLAN-0004` §6.2 records the engine's wipe as best effort. Whether the engine and the libraries it calls leave copies of the seed has not been tested in mofn. The TE09.28.02 test under Adopt would show it.

### 8. Pass 3 joins: what our artifacts do not yet agree on

These are differences between our own artifacts, found by script in the cross-check. None is a source defect.

- `requirements.yaml` `field`: 242 entries. 13 stated entries name no structure, step or state and keep a descriptive `field`: what they constrain is real, but no message structure, flow step or state models it: the reading rules R-0143 and R-0144, the map of which SP addresses which Annex (R-0147 to R-0152), the "No change." entries R-0162, R-0181, R-0196 and R-0237, and the notation R-0156. R-0105 and R-0124 read `none accessible`, which looked like the `none` marker; they now name what they constrain (accessibility of an unprotected or a plaintext SSP). The 4 inferred entries R-0238, R-0240, R-0241 and R-0242 keep a `field` and no message field, step or guard cites them; each rests on the stated entries in its `derived_from`.
- `messages.yaml`: 189 citations from 19 structures and 77 fields. 60 cite an entry whose lines overlap the field's, 72 one that overlaps the structure's, 42 one within 40 lines of it, and 15 were read against the field's own text (`Assertion` and `Assertion.security_area` cite R-0001, §5.1; `ProcessorEvidence`, `EnvironmentalProtectionStatement` and `Assertion.levels` cite entries a VE or TE paragraph below the quoted lines; all 15 read as meant).
- `protocol.yaml` `work_products`: 11 of 44 carry a `structure`, 33 carry `structure: none` with a reason (a test action, a module behaviour the tester observes, or a tester's response with no record defined). 8 of the 19 structures are held by no work product: `Assertion`, `ProcessorEvidence`, `HybridModuleDesignation`, `VendorAffirmedSecurityMethod`, `DataOutputPathSeparation`, `AuthenticationDataProtection`, `EnclosureHardness` and `FunctionalTestingDocumentation`. Their assertions (AS02.15, AS02.17, AS02.18, AS02.20, AS03.07, AS04.44, AS07.26, AS11.29) are documentation-only checks that `assertion_index` lists and no flow walks. `request for additional information` and `additional information` are work products of an error path only (F01.E1).
- Ids added by pass 3: 27 in `protocol.yaml` and 15 in `state-machine.yaml` (R-0140, R-0141, R-0158, R-0188, R-0189, R-0225, R-0227, R-0232, R-0235 and R-0236 among them), and 72 in `assertion_index`, which now holds 209 of the 242 entries. Where an entry's text repeats across assertions, only the copy whose split parent the step cites was added: F08 step 5 does not cite R-0101 or R-0120 (AS09.28 and AS09.30 copies of the sentence it quotes from AS09.23), and M01.T12, T13, T14, T15 and T16 each cite only the alternative they take of AS07.77 and AS07.81. SA-10 said the TE response forms and AS07.77's outcome items were not entries; they are R-0159 to R-0161, R-0188 and R-0189, and SA-10 now says so.

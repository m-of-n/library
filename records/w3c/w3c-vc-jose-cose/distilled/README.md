---
record: w3c-vc-jose-cose
kind: index
title: "w3c-vc-jose-cose — distilled artifacts"
extracted: "2026-11-03"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

FX-1 full extraction of **Securing Verifiable Credentials using JOSE and
COSE**, W3C Recommendation 15 May 2025 (REC-vc-jose-cose-20250515; editors
Jones, Prorock, Cohen). Authoritative bytes: the REC HTML,
`.cache/w3c-vc-jose-cose.bin`, sha256 `6c70cf8d7de9…6709af9` (=
`content.sha256`). Quotes and line numbers count in its plain-text rendering
`.cache/w3c-vc-jose-cose.txt` (1980 lines, sha256 `f02bd4966800…bb46c126`),
one line per HTML block element with RFC-style headings so `bin/check-locators`
can read it. Example fixtures are taken from the HTML elements, never from the
rendering, which inserts a space at each `<span>` boundary of a compact JWS.
Neither file is committed.

**Status: passes 1–3 complete.** `record.yaml` declares
`distillation.profile: full`. `reviewed_by` is empty on every artifact. A
person signs it, and until then these are readable but not buildable-on.

**97 BCP 14 keywords in the source, 87 in the requirement texts.** The 10 left
out are the three quoted "MUST" in the §1.1.1 class definitions, six in
§3.1.3 (which the source marks non-normative) and one in Appendix A (revision
history), each named by line in `requirements.yaml` `reconciliation`.

**No exchange, no trust model, no canonicalisation.** The source profiles
envelopes defined elsewhere (RFC 7515/7519, SD-JWT, RFC 9052) around the VC
Data Model 2.0; rows that depend on those are marked as outside this source.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 147 verbatim entries `N-001`–`N-147` in source order, each with a section/¶ locator (every block counted, each example one) and line range: 110 normative, 37 in sections, notes or examples the source marks non-normative, reproduced and flagged. All 97 keywords land in an entry. `[permissive]` flags a lowercase *can* that reads as a MAY. 34 source defects `SD-1`–`SD-34`. Front matter, the 26 examples, §1 ¶2–¶4, §4 ¶2, §B ¶2 and Appendix C not reproduced, each omission named. |
| requirements | `requirements.yaml` | 85 entries `R-0001`–`R-0085`, §1.1.1 to §5.4, all stated, 0 inferred. 97 in source, 87 extracted, 10 reconciled by line. Splits at R-0042/43 and R-0045/46. §4.2's requirements (R-0070–R-0074) carry the section's condition ("When using controlled identifier documents…"). Paragraph locators count paragraphs only (examples skipped); the header states the convention. |
| schema | `schema/` | No CDDL, JSON Schema, ABNF or ASN.1 in the source (searched, 0 found). Verbatim: 11 regions in `inline.verbatim.txt` — the six §6.1.x media-type templates (non-normative §6), the §5 inputs/outputs, the §1.1.2.2 list. Derived: 6 JSON Schemas 2020-12 (JOSE header, payload, SD-JWT, enveloped data: URLs, CID verification method, verification result), a COSE_Sign1 CDDL, a data: URL ABNF, 11 cross-field rules; MUST roots with separate `-should` profiles. 375 test verdicts, 0 mismatches. Nothing from non-normative §3.1.3 or §6 grounds a constraint. 27 findings `F-01`–`F-27`. |
| messages | `messages.yaml` | 32 messages, 229 fields: the JOSE header and JWT claims set as profiled, SD-JWT and its disclosures and KB-JWT, COSE_Sign1 and its header buckets with typ (16), content type (3) and CWT Claims (15), the Enveloped types and their data: URLs, the CID verification method, the §5 inputs/outputs, the six registrations. 8 encoding rules, 29 tensions `TEN-01`–`TEN-29`. |
| protocol | `protocol.yaml`, `protocol.md` | No exchange of its own: each flow is one party building an object, an unspecified delivery, and local processing. 14 roles, 17 flows with 113 steps (41 inferred, flagged), 21 error paths, `on_error` "unspecified by source" wherever the source gives none. The §5 algorithm text verbatim, 17 sequence and 6 state diagrams. 33 source defects and tensions, 14 `not_defined`. |
| state-machine | `state-machine.yaml` | 6 machines, 53 states, 66 transitions, verifier side only: M02–M04 the §5.1–§5.3 algorithms as printed, M05 §5.4 validation, M06 §4 key discovery, M01 the receiving lifecycle around them (almost wholly inferred, and says so). No issuer or holder machine: the source defines no lifecycle for either. 13 tensions, 7 `not_modelled`. |
| examples | `examples/` | 105 fixtures (80 verbatim: every tab and display of the 26 examples and the §8.1 controller documents; 25 derived decodes) and 56 vectors wired to R-ids. 592 checks: 347 pass, 166 fail, 77 unverifiable, 2 not run. Of 26 distinct signatures, 1 verifies (Example 22's KB-JWT under its own `cnf` key); no issuer signature verifies under any printed key. Every COSE example pairs alg -35 with a 64-octet signature. 23 defects `D-01`–`D-23`, 3 presentation artefacts `P-01`–`P-03`, recorded not repaired. |
| design-notes | `design-notes.md` | 25 mapping rows against our decisions read at m-of-n `db472d2`: adopts 6, constrains 12, conflicts 2 (ADR-0005's import rule; ARCH-0002 draft P5.2 vs R-0064), silent 5. Nothing conflicts with ADR-0004; the one cut against option 5 is weak (every payload is JSON, so an export is a re-signed translation). Header-by-header mapping for MD-3, a draft R-I-01 export table for R-I-06, consequences for mofn#110, 12 open questions. Decides nothing. |

## Known gaps, stated rather than hidden

- `reviewed_by` is empty throughout. No person has signed any artifact.
- RFC 9052, 9053, 9596 and 7519 are not in `.cache`; COSE and JWT facts beyond
  this source point at their records' artifacts or are marked outside this
  source.
- 25 of the 26 distinct signatures in the examples cannot be verified: no
  printed key verifies them and none of their kids names a printed key.
- `requirements.yaml` counts paragraphs only, `normative.md` counts every
  block; six requirement/entry pairs carry different ¶ numbers for the same
  text. Each file states its rule.
- Design-notes row 11 (ADR-0005 import rule vs R-0072) stays "conflicts";
  R-0072 binds producers and is conditional on §4.2, so a reviewer may read
  it as "constrains".
- The design notes propose `bears_on` corrections (§9); `record.yaml` was not
  edited for them.

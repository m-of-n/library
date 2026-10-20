---
record: rfc-8551
kind: index
title: "rfc-8551 — distilled artifacts"
extracted: "2026-10-19"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

FX-1 full extraction of **RFC 8551, S/MIME Version 4.0 Message Specification**
(Schaad, Ramsdell, Turner, April 2019, Standards Track). Source
`.cache/rfc-8551.txt`, sha256 `dac39f749a08…884ae2`, 3531 lines, read in full.

**Status: passes 1–3 complete.** `record.yaml` declares
`distillation.profile: full`. `reviewed_by` is empty on every artifact. A
person signs it, and until then these are readable but not buildable-on.

**190 BCP 14 keywords in the source, 152 in the requirement texts.** The 38
left out are the §1.3 SHOULD+/SHOULD-/MUST- definitions (14), the §1.5/§1.6
change logs (23) and the ASN.1 `OPTIONAL` (1), each named by line in
`requirements.yaml` `reconciliation`.

**No delegation and no trust model.** The source defers certificate handling
to RFC 8550 and the CMS structures to RFC 5652; rows that depend on either are
marked as outside this source.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 185 verbatim entries `N-001`–`N-185` in source order, each with a section/¶ locator and line range. BCP 14 reconciled 190 = 190, no keyword line outside an entry. 22 entries flagged lowercase; 12 cross a page break and are flagged. Front matter, history, keyword-free changelog bullets, sample messages, references, Appendix C and back matter excluded. |
| requirements | `requirements.yaml` | 151 entries `R-0001`–`R-0151`, §1.1 to Appendix B.2, including §6 and the §4.2–§4.5 key-size rows. 190 in source, 152 extracted, 38 reconciled by line. 151 stated, 0 inferred. 107 testable, 41 partial, 3 not. Tensions at `R-0037`, `R-0049`, `R-0108`, `R-0125`. |
| schema | `schema/` | Verbatim: the Appendix A ASN.1 module `SecureMimeMessageV3dot1` and 13 formal displays (`inline.verbatim.txt`). Derived: a JSON Schema 2020-12 for the S/MIME media types, the multipart/signed Content-Type ABNF, and the algorithm requirements as YAML. 13 source defects in `README.md`. The module is not compiled; imported CMS modules are not carried. |
| messages | `messages.yaml` | 44 messages, 199 fields: the five CMS content types as profiled, SignerInfo and its attributes, the five smime-types, multipart/signed, the canonical inner entity, the §3.10 identification table, the §5 registrations and Appendix B. 6 encoding rules (BER vs DER unstated, `ENC-01`), 14 tensions. |
| protocol | `protocol.yaml`, `protocol.md` | Store-and-forward, no exchange of its own. 13 roles, 22 flows with 126 steps, 36 error paths. One Mermaid sequence diagram per flow and 6 decision flowcharts. 17 source defects and tensions. |
| state-machine | `state-machine.yaml` | 11 machines, 90 states, 131 transitions (39 states and 43 transitions inferred). Every trigger is a `messages.yaml` entry or a declared event. M11 is a document lifecycle (the §1.3 requirement levels across versions) and says so. 10 `not_modelled` items, 13 tensions. |
| examples | `examples/` | 47 vectors: 16 from the source, 31 constructed. 7 verbatim fixtures and 10 derived decodes. openssl verifies §3.5.2; §3.5.3.3 cannot be verified and its digest does not match its content (S-02); §3.6 is a bare zlib stream, not CompressedData (S-01). 10 source defects. |
| design-notes | `design-notes.md` | 11 adopt, 8 adapt, 7 reject. A mapping row for every `bears_on` id. MD-3 addressed with a CMS non-mapping and a DEC-002 options table; three cuts against option 5, all toward option 2. A draft R-I-01 import table. 18 open questions. Decisions read from m-of-n `643fba2`. Decides nothing. |

## Known gaps, stated rather than hidden

- `reviewed_by` is empty throughout. No person has signed any artifact.
- The ASN.1 module has not been compiled; no ASN.1 compiler was available.
- §3.5.3.3's signature cannot be verified; the source prints no signer
  certificate.
- CMS rows depend on RFC 5652, which has no library record yet.
- The design notes read our decisions at m-of-n `643fba2`. A reviewer should
  check each mapping row against the current decisions.
- The design notes propose `bears_on` corrections (§8); `record.yaml` was not
  edited for them.

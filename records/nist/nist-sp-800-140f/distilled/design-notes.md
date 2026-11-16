---
schema: "library-distilled/v1"
id: nist-sp-800-140f-design-notes
record: nist-sp-800-140f
type: design-notes
updated: "2026-11-15"
---

# NIST SP 800-140F (CMVP approved non-invasive attack mitigation test metrics): design notes for tmodel and mofn

This note covers how SP 800-140F bears on `tmodel:DEC-009`, the record's `bears_on`. It found nothing that bears on a mofn decision.

- **Read against** tmodel@ddac1b9 and mofn@10e357f, as the `fips-140-3` notes are. A tmodel id is written `tmodel:…`; a bare id is mofn's.
- **What it is.** The CMVP's replacement for ISO/IEC 19790 Annex F and ISO/IEC 24759 §6.18, the test metrics for mitigating non-invasive attacks. Its content is one sentence: there are none yet.
- **Not withdrawn.** The cached PDF carries no withdrawal notice.
- **Source.** `.cache/nist-sp-800-140f.txt`, sha256 `c416d495c9b99325e40b5c4d085bb1e2121d1cbbebc27e40c9b647f741d10334`, the pinned `source_text_digest`. It renders the PDF whose sha256, `7772ec5af1909a87b7e724afeef77bb3206174c321aa59f80e32500df7fc48ed`, equals `content.sha256` and the skeleton's `source_digest`. All three were recomputed in this pass.
- **Ids.** `R-NNNN` means `nist-sp-800-140f#R-NNNN`. A script emits every id from `requirements.yaml`: it selects the entry whose `source_lines` start on a given line, narrowed by a phrase of its text, and raises unless exactly one matches.

## The content

<!-- q L243-244 -->
> Section 6 of this document replaces the approved non-invasive attack mitigation test metrics requirements of ISO/IEC 19790 Annex F and ISO/IEC 24759 paragraph 6.18.

<!-- q L263-267 -->
> This document identifies CMVP-approved non-invasive attack mitigation test metrics. 6.2 Approved non-invasive attack mitigation test metrics No additional requirements at this time

§6 contains no verbal form, by the `directives` regex over L259–L267. The skeleton found one in the body, in R-0001, about how modifications are marked.

## Adopt

### An empty source is still a source, with a date (tmodel)

This bears on `RequirementSource` and `Evidence.fresh_until` (`tmodel:ADR-0013`) and on the mitigation lifecycle (`tmodel:DEC-009`, `tmodel:R-021`).

- A RequirementSource for this annex has no members, and its `version` records that it had none on the revision read. That is a fact a validation depends on: a module tested while the annex was empty has no non-invasive metrics to have met.
- When the CMVP adds metrics, a module validated before has not been tested against them. The RequirementSource built from this list needs `version` naming this revision (Evidence's `about_version` is the product's version), so a later reader can tell an old validation from a failed one.

## Adapt

Nothing. With no metrics there is nothing to reshape, for either project.

## Reject or hold

### Hold: nothing for mofn

- Non-invasive attacks are measured on a module, such as its timing or power. mofn ships no validated module (a mofn wallet that holds its own keys is a software cryptographic module in FIPS terms, the `fips-140-3` notes say) and uses a vetted library for every primitive (`APP-0001` §5). No mofn specification or decision addresses side channels. The one mention in mofn's research is that FN-DSA's floating-point sampling is hard to implement in constant time (`research/0001-signatures-and-attestation/mini-reports/H-post-quantum.md`), and FN-DSA is no mofn suite. Nothing here rests on a mofn decision.

### Hold: reading the gap as permission

- The annex adds no metrics, but it does not say that the area is untested. The non-invasive security area stays in ISO/IEC 19790 and in ISO/IEC 24759 §6.8, which SP 800-140 leaves unchanged; this annex replaces only the metrics of Annex F and §6.18. A tmodel import must not read the empty list as an empty area. Whether the replaced Annex F had metrics of its own, which an empty replacement would remove, is open question 1.

## Open questions and source defects

### 1. Replaces, or adds nothing?

- §5.1 says §6 replaces the metrics of ISO/IEC 19790 Annex F. §6.2 says there are no additional requirements. Replacing an annex with nothing removes whatever it held; adding nothing leaves it in force. The record does not say which it means, and Annex F is in ISO/IEC 19790, which the library does not hold.

### 2. The one change FIPS 140-3 names gets no metrics

- FIPS 140-3 §1 limits its major changes from FIPS 140-2 to the new non-invasive requirements (`fips-140-3`, L307–L308). SP 800-140 §6.8, the test requirements for that area, says No change (`nist-sp-800-140`, L778–L780). This annex adds no metrics. So for the one area FIPS 140-3 calls new, neither the DTR nor this annex changes anything.

### 3. The scope promises evidence methods

<!-- q L185-190 "This document also specifies" .. "paragraph 6.18." -->
> This document also specifies the modification of methods for evidence that a vendor or testing laboratory provides to demonstrate conformity. Unless otherwise specified in this document, the test requirements are specified in ISO/IEC 24759 paragraph 6.18.

- The record has no vendor-evidence or test-evidence item (0 `VE`/`TE` identifiers by grep), as in SP 800-140C and 800-140E (`nist-sp-800-140c` notes).

### 4. No revision history

- The Document Revisions table (L276–L278) is empty.

### 5. Pass 3 joins: what our artifacts do not yet agree on

These are differences between our own artifacts, found by script in the cross-check. None is a source defect.

- `requirements.yaml` `field`: 14 entries. All 14 name no structure, step or state and keep a descriptive `field`: what they constrain is real, but no message structure, flow step or state models it: the notation of §5.2, scope, editions, definitions, the statement that §6.2 adds no requirement (R-0013) and the inferred R-0014. This agrees with `messages.yaml` (no structure, `not_applicable`) and with the absence of a protocol and state machine.

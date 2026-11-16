---
schema: "library-distilled/v1"
id: nist-sp-800-140e-design-notes
record: nist-sp-800-140e
type: design-notes
updated: "2026-11-15"
---

# NIST SP 800-140E (CMVP approved authentication mechanisms): design notes for tmodel and mofn

This note covers how SP 800-140E bears on `tmodel:DEC-009`, the record's `bears_on`, and on how a mofn wallet unlocks its keys, which no `bears_on` id names.

- **Read against** tmodel@ddac1b9 and mofn@10e357f, as the `fips-140-3` notes are. A tmodel id is written `tmodel:…`; a bare id is mofn's.
- **What it is.** The CMVP's replacement for ISO/IEC 19790 Annex E and ISO/IEC 24759 §6.17: which operator authentication mechanisms a module may use at each security level. Its content is one table (Table 1) and a pointer to SP 800-63B as the framework.
- **Not withdrawn.** Unlike SP 800-140B, 800-140C and 800-140D, the cached PDF carries no withdrawal notice.
- **Source.** `.cache/nist-sp-800-140e.txt`, sha256 `516184a71c0b90ba4d1ca57c857e909d74f2215b571d19678aa53e057f35514f`, the pinned `source_text_digest`. It renders the PDF whose sha256, `26616caa396fc292dd1d726309e34287683c8089ea401f3dc7f55ccb671aa28e`, equals `content.sha256` and the skeleton's `source_digest`. All three were recomputed in this pass.
- **Ids.** `R-NNNN` means `nist-sp-800-140e#R-NNNN`. A script emits every id from `requirements.yaml`: it selects the entry whose `source_lines` start on a given line, narrowed by a phrase of its text, and raises unless exactly one matches.

## What the annex approves: nothing

<!-- q L282-285 -->
> While there are currently no approved authentication mechanisms, allowed authentication mechanisms may be used as indicated in Table 1. Except at level 1, operator authentication acceptance is required to be performed by the module or by the Operating Environment as defined in ISO/IEC 19790.

R-0003 says it plainly: there are no approved authentication mechanisms, only allowed ones, by level. Table 1 (L290–L322) gives them:

- **Level 1:** none required; authentication may be implicit, and if used should meet Level 2 (R-0004, R-0005).
- **Level 2:** a memorized secret or any Level 3 mechanism (L299–L302, R-0026).
- **Level 3:** nine mechanisms, memorized secret first (R-0031):

<!-- q L304-318 -->
> Level 3 • Memorized Secret; • Look-Up Secret; • Out-of-Band; • Single-Factor One Time Password (OTP) Device; • Multi-Factor OTP Device; • Single-Factor Crypto Software; • Single-Factor Crypto Device; • Multi-Factor Crypto Software; • Multi-Factor Crypto Device

- **Level 4:** multi-factor crypto software or a multi-factor crypto device only (L321–L322, R-0041).

## Adopt

### A passphrase caps a wallet's authentication at Level 3 (mofn)

This bears on mofn's `PLAN-0004` §6.1 (proposed: the engine prompts for a passphrase to unlock a key file) and `SPEC-0001` §5.1 (custody). Neither is a DEC.

- A wallet passphrase is a memorized secret. Table 1 allows it at Levels 2 and 3 and not at Level 4. A mofn wallet that unlocks keys with a passphrase alone could therefore not reach Level 4 in this area, whatever else it did.
- §6.2 also says where the check runs. Except at Level 1, the module or its operating environment performs the authentication (R-0013, quoted above). The engine checking the passphrase is the first case; a later OS keychain holding the passphrase (`PLAN-0004` §6.1) is the second.
- This is a mapping, not a change: `PLAN-0004` §6.1 already keeps the passphrase out of arguments and logs, and SP 800-140 adds to it: AS04.44 protects authentication data and AS04.54 obscures feedback during entry, so a keychain entry counts as authentication data and entry does not echo (`nist-sp-800-140` notes).

### SP 800-63B is the framework (tmodel)

This bears on `RequirementSource` (`tmodel:ADR-0013`) and on `tmodel:DEC-009`.

<!-- q L324-333 -->
> Vendors should use SP 800-63B as a framework for authentication requirements and should provide justification whenever SP 800-63B requirements cannot be met. Testers should review and affirm the vendor documentation. Normative SP 800-63B sections include ● Section 5, Detailed requirements specific to each type of authenticator; ● Section 6, Lifecycle management; ● Section 7, Session Management; Informative information to be assessed for each authenticator includes: ● Section 8, Threats and Security Considerations; and ● Section 10, Usability Considerations.

- The binding text is a should (R-0006, R-0007). The requirements of each mechanism live in SP 800-63B, which this annex adopts by reference, the way FIPS 140-3 adopts ISO/IEC 19790. A tmodel RequirementSource for this annex is small, and points at a second one for SP 800-63B.
- The library holds no record for SP 800-63B (a search of every other record's `record.yaml` for 800-63 finds only the OWASP ASVS record), so that second source cannot be built yet.

## Adapt

### Levels select mechanisms, and Levels 2 and 3 select the same ones (tmodel)

This bears on level applicability in the deferred `RequirementProfile` (`tmodel:ADR-0013`, `tmodel:DEC-001b`).

- Level 2 allows a memorized secret or any Level 3 mechanism. Level 3's list starts with the memorized secret. So the two levels admit the same nine mechanisms, and Table 1 does not distinguish them.
- What else differs between the levels is outside this record. SP 800-140B asks of each method whether it is identity-based or role-based (its B.2.4), which suggests the levels differ there; ISO/IEC 19790, which the library does not hold, would say.
- A RequirementProfile that selects by level gets the same mechanism set for Levels 2 and 3 from this table. It has to take the difference from ISO/IEC 19790, which the library does not hold.

## Reject or hold

### Reject (mofn): proof of possession is not operator authentication

This bears on mofn's `SPEC-0001` §8.1 (a presentation's proof of possession) and `SPEC-0002` §6.4 (the `KSA-POP-SIG-v1` label).

- Table 1 governs how an operator authenticates to a module before using its keys. mofn's proof of possession is a persona proving to a relying party that it holds a key, by signing a presentation. The first is local and ahead of every signature; the second is a statement on the wire. Neither stands in for the other.
- R-0002 reaches only the case where a module uses such a mechanism to set up protected communication: it must then meet SP 800-140C and 800-140D. A mofn transport (`SPEC-0001` §8.2) would be that case. A presentation's proof of possession is a signature, which SP 800-140C governs (`nist-sp-800-140c` notes).

## Open questions and source defects

### 1. The scope sentence has SP 800-140D's subject

<!-- q L188-190 "The approved sensitive security parameter" .. "paragraph 6.17." -->
> The approved sensitive security parameter generation and establishment methods specified in this document supersede those specified in ISO/IEC 19790 Annex E and ISO/IEC 24759 paragraph 6.17.

- This annex is about authentication mechanisms, but its scope (R-0016) says sensitive security parameter generation and establishment methods, SP 800-140D's subject, in the sentence SP 800-140C's §1 uses for its own. §5.1 states the scope correctly (R-0021).

### 2. ISO/IEC 24579

<!-- q L26-29 -->
> CMVP Approved Authentication Mechanisms: CMVP Validation Authority Requirements for ISO/IEC 19790 Annex E and ISO/IEC 24579 Section 6.17

- The title page and §5.2 (L266) cite ISO/IEC 24579; the cover (L5–L8) cites ISO/IEC 24759. The first is a transposition. A tool that extracts citations would record ISO/IEC 24579, a number no other record of the family cites.

### 3. Informative, or normative?

<!-- q L259-262 "While this document serves" .. "module authentication." -->
> While this document serves a different purpose, much of the authentication is purposely meant to align with SP 800-63B, which is an informative reference for module authentication.

- §5.1 calls SP 800-63B an informative reference (R-0022); §6.2 lists its normative sections (R-0044, quoted under Adopt). The reference is also undated, and FIPS 140-3 §3.1 applies the latest edition of an undated NIST SP (`fips-140-3` notes). The section numbers 5, 6, 7, 8 and 10 belong to whichever edition the authors read, which the record does not name.

### 4. Defined, then never used

<!-- q L212-213 -->
> Rate Limiting: Used to control the rate of requests sent or received by a network interface and is used to prevent automated attacks.

- Rate Limiting (§3), FMR and PAD (§4) are defined and appear nowhere else in the record (grep). FMR and PAD are biometric terms, and Table 1 lists no biometric mechanism. They read as left over from a draft that had one.

### 5. Pass 3 joins: what our artifacts do not yet agree on

These are differences between our own artifacts, found by script in the cross-check. None is a source defect.

- `requirements.yaml` `field`: 54 entries. 13 stated entries name no structure, step or state and keep a descriptive `field`: what they constrain is real, but no message structure, flow step or state models it (the notation of §5.2, scope, editions and definitions). The 4 inferred entries R-0051 to R-0054 keep a `field` (Table 1, security levels 2 to 4, SP 800-140C and SP 800-140D) and no field, step or guard cites them; each rests on stated entries in its `derived_from`, which are cited.
- `messages.yaml`: 31 citations from 2 structures and 11 fields; 5 cite an entry whose lines overlap the field's, 1 one that overlaps the structure's, 24 one within 40 lines, and 1 was read (`AuthenticationMechanismClaim.sp_800_63b_requirements_met` cites R-0044, the line that names the normative SP 800-63B sections).
- `protocol.yaml` `work_products`: 4 of 5 carry a `structure` (all `AuthenticationMechanismClaim`); `review and affirmation` carries `structure: none`, because the testers' review has no record defined. `AuthenticationLevelRow` (Table 1) is held by no work product: F02 reads it through `permitted_mechanisms`, which are not work products.
- Ids added by pass 3: 16 in `protocol.yaml`, among them R-0044 to R-0050 (the SP 800-63B section lists), the Table 1 rows R-0026, R-0031 and R-0041, and the children R-0011 to R-0015 beside the parents R-0002, R-0003 and R-0006. F02 step 1 quotes only the Level 3 row, so it cites none of the rows.

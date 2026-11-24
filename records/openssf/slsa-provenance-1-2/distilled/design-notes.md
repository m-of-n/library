---
record: slsa-provenance-1-2
kind: design-notes
title: "slsa-provenance-1-2 — bearing on our design"
extracted: "2026-11-16"
reviewed_by: ""
---

# SLSA Build Provenance v1.2 — bearing on our design

The source is `spec/build-provenance.md` of the SLSA specification, branch
`releases/v1.2` of slsa-framework/slsa at `ae7fc76`, whose bytes are
`content.sha256` in `record.yaml`,
`182ab5cf823c374874136371466ba43f99f0a9ba87a8046757d26a2ed74854a0`, recomputed
from `.cache/` in this pass. What this file reads is the rendering
`distilled/render-source.py` makes of it, with `provenance.cue` and
`provenance.proto` spliced in at L125-172 and L189-238:
`.cache/slsa-provenance-1-2.txt`, 704 lines, sha256
`1a3828724437a0fc24bb492bca6db28df114e318bbaace85cc9f75204035db55`. That equals
`source_digest` in the skeleton's `requirements.yaml`, and re-running the script
in this pass reproduced it byte for byte. `record.yaml` gives the date
2025-11-24 and `maturity: standard`.

It defines one predicate type for the in-toto attestation framework (L13-17): a
`buildDefinition` (the build type, the external and internal parameters, the
dependencies resolved) and `runDetails` (the builder's id, version and
dependencies, invocation metadata, byproducts), with parsing rules (§3), an
informative cue and protobuf summary (§4.1), extension fields (§4.7) and a
migration from v0.2 (§7). **It does not define** a signature, an envelope, a key
or a verification procedure. Provenance is an attestation (L42-43) carried in an
in-toto Statement (L126-131); verification is another page (§5 L555-560); and the
signer is distinct from the builder (L501-505).

It reaches us four ways, the four ids in `bears_on`, and through three I4 tasks.

1. **R-I-01** (Must; `ARCH-0001`:441): a published mapping table per foreign
   format. The §6 row for SLSA provenance v1 maps it, for import and export, to an
   ArtifactStatement predicate, with an empty loss cell (`ARCH-0001`:499). T-053
   fills it (`BACKLOG`:190). §3 below is the field-by-field input.
2. **R-I-03** (Should; `ARCH-0001`:443): export to an in-toto Statement in DSSE,
   or COSE_Sign1 with CWT claims. This predicate is one payload such an export
   would carry; C-07 says what it costs.
3. **R-M-07** (Must; `ARCH-0001`:430): an artifact statement binds a content
   digest. C-02.
4. **R-M-12**, relocated to `ARCH-0002` P1 by `ADR-0001` (`ADR-0001`:32-38):
   every extension point in the source is a URI or a vendor-prefixed name. X-02,
   X-04.

The tasks: T-051, `MAP-0002`, between in-toto Statement and `ArtifactStatement`
in both directions (`BACKLOG`:188); T-052, round-trip a real SLSA provenance (`BACKLOG`:189); T-053,
the losses (`BACKLOG`:190). I4's demo is that a real SLSA attestation imports as
an `ArtifactStatement` and round-trips (`PLAN-0001`:487; `PLAN-0003`:48); M5
asks for at least five public examples (`PLAN-0002`:391). MD-1 kept the in-toto, SLSA and
SCITT mapping as the supply-chain target's interchange (`MEET-0928`:37-40).

What it is not, for us: a name system (`ARCH-0001`:284), and its local-name and
threshold authorization is weak (`ARCH-0001`:293). We do not verify builds; the mapping is interchange
(`LIMITATIONS`:20-21).

## Things to hold while reading

1. **Our documents are read from m-of-n at `7c3c731`**
   (`7c3c73165197e9c63152a65ba51345d65a268b89`, HEAD on 2026-11-16, unchanged
   through the pass), only with `git -C /Users/nfn/Projects/mofn show
   7c3c731:<path>`. A location in them is written `DOC:n` or `DOC:n-m`, with DOC
   from this table and n a line of that blob. **No mofn text is set as a
   quotation here:** each reference is a paraphrase with its lines. *(Pass 2: 22 of
   the paraphrases keep a run of six to twelve of mofn's own words, unmarked; §11.)*

   | DOC | path at 7c3c731 | standing at 7c3c731 |
   |---|---|---|
   | `ARCH-0001` | `spec/ARCH-0001-authorization-attestation.md` | draft 0.3.1. §4 model, §5 requirements, §6 matrix, §7 decisions |
   | `ARCH-0002` | `spec/ARCH-0002-key-relative-naming.md` | draft 0.10.0. P1 accepted (`ADR-0001`); P2, P3, P5 with P5.1 and P5.2, and P6 accepted (`ADR-0002`); P1.1, P4, P7 draft; DEC-008, DEC-009 open |
   | `ARCH-0003` | `spec/ARCH-0003-wallet-object-model.md` | draft 0.3.1 |
   | `SPEC-0002` | `spec/SPEC-0002-ksa-core.md` | draft 0.10.1 (front matter); governs where it and an ARCH document differ (`ADR-0003`) |
   | `SPEC-0003` | `spec/SPEC-0003-ksa-definitions.md` | draft 0.2.0 |
   | `SPEC-0004` | `spec/SPEC-0004-ksa-trust-evaluation.md` | draft 0.6.2 |
   | `ADR-0001` | `spec/ADR-0001-key-relative-naming.md` | accepted: R-M-12 stands, as `ARCH-0002` P1 |
   | `ADR-0003` | `spec/ADR-0003-ksa-core-decisions.md` | accepted: D1, no URN identifiers and no namespaced extension fields |
   | `ADR-0004` | `spec/ADR-0004-dec-002-encoding.md` | accepted 2026-10-25: DEC-002 is option 5, KSA-CBOR; `reviewed: false`; closes MD-3's narrowing |
   | `ADR-0005` | `spec/ADR-0005-dec-003-key-identifier.md` | accepted: `kid` is SHA-256 of the suite's public-key encoding |
   | `ADR-0007` | `spec/ADR-0007-dec-007-predicate-rendering.md` | accepted 2026-11-07: DEC-007 is option 2 |
   | `MEET-0928` | `project/meetings/2026-09-28.md` | MD-1 … MD-7 |
   | `BACKLOG` | `project/BACKLOG-0001.md` | draft 0.15.1. T-051, T-052, T-053 todo; L-041 is library#136 |
   | `PLAN-0001`, `PLAN-0002`, `PLAN-0003` | `project/PLAN-0001-project-plan.md`, `project/PLAN-0002-product-spec.md`, `project/PLAN-0003-semester-plan.md` | drafts 0.7.1, 0.4.1, 0.1.0: D7, I4, M5 |
   | `DL-0047` | `design-log/0047-l-041-d7-extraction/review.md` | open (status line 10 of its `question.md`); `review.md` leaves T-052's version to its owner |
   | `MECH` | `research/0006-mechanism/report.md` | mofn report R-0006, draft 0.3.0 |
   | `SURVEY` | `research/0001-signatures-and-attestation/report.md` | mofn survey R-001, draft 0.2.0 |
   | `LANE-A README`, `LANE-A 02`, `LANE-A 03`, `LANE-A .gitignore`, `LANE-A SUMS` | `prototype/lane-a/README.md`, `02_dsse_intoto.py`, `03_slsa_provenance.py`, `.gitignore`, `out/SHA256SUMS` | throwaway; decides nothing (`LANE-A README`:3) |
   | `GLOSSARY`, `LIMITATIONS` | `project/GLOSSARY-0001.md`, `LIMITATIONS.md` | draft 0.3.0; — |

   `docs/extraction.md` still says no DEC-002 ADR exists (its lines
   129-131). At `7c3c731` `ADR-0004` accepts DEC-002 for option 5, so this file maps
   against `ADR-0004`, and §7 still records where the source cuts against option
   5, because an accepted ADR is superseded, not patched.

2. **Numbering.** A bare `R-NNNN` is `slsa-provenance-1-2#R-NNNN`. Pass 1 cited
   only ids the skeleton wrote (R-0001 to R-0050); pass 2 added ids the
   requirements lane appended (R-0051 to R-0170) where this file relies on their
   statements (§10). R-0001 is the RFC 2119 recital (L25-27) and is not cited as a
   requirement. mofn's research report R-0006 is always *mofn report R-0006*
   (`MECH`), never bare, since `R-0006` here is a requirement; its survey is
   *mofn survey R-001* (`SURVEY`). `R-M-nn`, `R-I-nn`, `R-O-nn` are `ARCH-0001`
   §5; `P1` … `P7`, `P1.1`, `P5.1`, `P5.2` are `ARCH-0002`. Row ids are `A-nn`
   adopt, `D-nn` adapt, `X-nn` reject, `C-nn` constrains, `K-nn` conflicts,
   `S-nn` silent: two digits, so C-01 is a row and not an inferred candidate
   (those are `C-NNNN`), and D-01 is a row and not deliverable D7.

3. **Quotation.** No word of the source is typed here. Each quotation is a
   `<!-- q Lx-y -->` marker whose blockquote `bin/check-quotes --render` wrote.
   Elsewhere a passage is cited by line and paraphrased, and a paraphrase is
   never set in quotation marks. Field names in backticks are identifiers, not
   quotations. The source is Markdown, and a rendered quotation keeps its markup:
   backticks, link brackets, list dashes, and `//` inside code.

4. **Labels.** *(inferred)* marks a consequence the source does not state.
   **Ours** marks a proposal of this library, offered to the task that owns it
   and decided by nobody here. A number carries the method that produced it
   (§11).

5. **One word.** mofn's glossary reserves *artifact* for the thing a statement is
   about, never files or build outputs (`GLOSSARY`:182-185). The source uses it
   for build outputs and inputs (L8, L82-83, L426). Here the source's sense is
   written *SLSA artifact*; `ArtifactStatement` and `ArtifactId` keep mofn's.

---

## 1. Rows by verdict

32 rows: **4 adopt, 5 adapt, 4 reject, 10 constrains, 4 conflicts, 5 silent**.
*Adopt (confirms)* means the source does what an accepted decision of ours
already does, and is recorded as independent evidence for it, not as a new
commitment. Nothing here changes a decision; §12 says so.

| id | verdict | in the source | where | ids | maps to | finding |
|---|---|---|---|---|---|---|
| A-01 | adopt (confirms) | External parameters are untrusted, must be included and verified downstream; verifiers should reject unknown or unexpected fields inside them | §2 L73-75; §4.3 L302-303 | R-0005, R-0018 | `ARCH-0002` P5 (`ARCH-0002`:394-396); `SPEC-0002` §13.5 (`SPEC-0002`:918-922) | SLSA reverses its own ignore-unknown default for the one object it calls untrusted; SHOULD strength, that object only |
| A-02 | adopt (confirms) | A parameter carries the locator the caller passed; the digest it resolved to goes in `resolvedDependencies` | §4.3 L336-351, L381-383, L396-401 | R-0024, R-0025, R-0029, R-0031 | R-M-11 (`ARCH-0001`:434); `SPEC-0002`:479-486, :947-955 | the separation mofn#144 made by withdrawing the locator target; but the worked digest has no native code (C-02) |
| A-03 | adopt (confirms) | `invocationId` is opaque and case-sensitive unless the builder defines otherwise | §4.6 L519-522 | R-0124, R-0042 | `SPEC-0002`:222; `SPEC-0003`:269 | a text attribute with nothing to normalise; byte comparison fails closed under any looser builder rule |
| A-04 | adopt (form) | §7 maps v0.2 to v1 field by field, marks fields with no v0.2 source, lists the fields gone, and moves two into `builder.id` | §7 L574-631 | R-0048, R-0049, R-0050 | R-I-01 (`ARCH-0001`:441); T-053 (`BACKLOG`:190) | a worked R-I-01 table, with a fourth column R-I-01 lacks: moved out of the signed bytes |
| D-01 | adapt | Consumers accept only specific signer-builder pairs; one signer may sign for several builders; modes of different security take different ids | §4.5 L453-456, L489-505 | R-0036, R-0038, R-0039, R-0040 | `ARCH-0001`:393; `SPEC-0002`:591-617; `SPEC-0004`:179-198, :519-536; `ADR-0003` D4 | the pair becomes a trust statement or anchor whose `about` is a `builder-id` text range: evaluable, where SLSA keeps the list outside the format (`SURVEY`:1297-1299) |
| D-02 | adapt | `buildType` names a parameterised template whose documentation should give its parameter schemas, how to start it, and an example | §2 L65-68; §4.3 L277-287, L339-340, L355-357 | R-0013, R-0026, R-0027 | `ARCH-0002` P3 (`ARCH-0002`:199-214), P1; `ADR-0007`:57-66; `SPEC-0003` §5.4, §7 | **Ours:** a per-build-type definition is the only structured native home for the parameters (C-01); identity by `DefinitionId`, not URI |
| D-03 | adapt | Unset, null and empty values are read the same | §3 L110 | R-0010 | `SPEC-0002`:428-429, :227-229 | import collapses three spellings to omission; export emits omission, which SLSA consumers must read the same; only a byte round trip loses (§6) |
| D-04 | adapt | Consumers should know what good looks like; parameters kept few and simple to ease verification | §4.3 L297-300, L331-333 | R-0016, R-0017, R-0022 | `SPEC-0003`:357-372, :384-425; `SPEC-0004`:578 | the expectation becomes a published template on the acceptance line, P5's *expected* level; needs D-02 |
| D-05 | adapt | The builder id should resolve to documentation of its scope, claimed level, guarantees, unverified tenant fields and extension fields | §4.5 L449-451, L458-465; §4.2 L258-259 | R-0037 | `SPEC-0002`:458, :947-955; `ADR-0003`:66-67; `SPEC-0004` §10.2 | **Ours:** a trusted key attests those about the builder, as a description target holding the URI; the properties SLSA keeps out of band become claims a verdict can name |
| X-01 | reject | Ignore unrecognized fields; any object may carry vendor extension fields | §3 L103-105; §4.7 L540-550 | R-0009, R-0043, R-0044, R-0045, R-0046 | P5 (`ARCH-0002`:394-396); `SPEC-0002`:440-444, :918-922; `ADR-0003`:47 | natively nothing is skippable; at import it is K-01 |
| X-02 | reject | Types and identities named by URI: the predicate type, `buildType`, `builder.id` | L17; §4.3 L278; §4.5 L447 | R-0051, R-0081, R-0106 | P1 (`ARCH-0002`:65-72); `ADR-0001`:32-35, :55-56; `ADR-0007`:64-66; `ARCH-0001`:340, :496 | lossy at the boundary: the URI travels as data, the authority behind it does not |
| X-03 | reject | Meaning held at a URL: the build type's specification, the builder's documentation, a predicate type that resolves to the latest minor version | L20-23; §4.2 L258-259; §4.3 L283-286; §4.5 L458-465; §7 L630-631 | R-0013, R-0037 | `ADR-0003`:66-67; `ADR-0007`:91-101; `SPEC-0003`:181-186 | not dropped by an import: never in the signed bytes. D-02 and D-05 are the adapted forms |
| X-04 | reject | Extension field names namespaced by a vendor prefix | §4.7 L543-546; §4.5 L465 | R-0044 | `ADR-0001`:64-67; `ARCH-0002`:82-84 | an escape by convention with no principal attached; the meaning is builder-relative, the prefix is bound to nothing |
| C-01 | constrains | Parameters are arbitrary JSON objects; annotations take any JSON value; `version` is a free map | §4.3 L330-333; §4.1 L135-136, L143, L167-169, L207-208, L219 | R-0022 | `SPEC-0002`:220, :227-229; `SPEC-0003`:202-205, :265-278; `ADR-0004`:38-42 | floats, null, large integers, non-label keys, lists and bytes have no structured home (§3); option 5's cost here (§7) |
| C-02 | constrains | Digest sets name `sha256`, `sha512`, `gitCommit` and any other key; the source's only digest value is a `gitCommit`; dependency completeness is best effort | §4.1 L157-162; §4.3 L318-322, L342-351, L391-394; §2 L84-87 | R-0020, R-0025 | R-M-07 (`ARCH-0001`:430); `SPEC-0002`:454, :473-477, :848-854; `MECH`:288-294 | two of the three named keys have native codes; the worked dependency has none; a URI-only dependency is a target only as a description of its name |
| C-03 | constrains | `resolvedDependencies` is an unordered collection, carried in an array | §4.3 L318 | R-0089, R-0163 (inferred) | `SPEC-0002`:224; `ADR-0004`:105-108; `ARCH-0002`:474-477 | a foreign case of condition (5): sort and lose the producer's order, or keep it and let equal sets differ in bytes |
| C-04 | constrains | Build times: the cue spells whole-second UTC; the proto uses a protobuf Timestamp; the text defers to in-toto's | §4.1 L172, L194, L236-237; §4.6 L524-532 | R-0125, R-0127 | `SPEC-0002`:268-282; `SPEC-0003`:276 | whole-second UTC maps exactly; a fraction or a leap second has no native form (open question 4) |
| C-05 | constrains | One provenance covers every output of the build, named in `subject` | §2 L96-97; §4.1 L128; §4.2 L245-246 | R-0041, R-0042 | `SPEC-0002`:436; `ARCH-0001`:481 | import fans out to one attestation per digest; the grouping and a subject's other digests are lost unless carried |
| C-06 | constrains | One signed provenance mixes what the platform vouches for with what it relays, and some fields are tenant-written and unchecked | §2 L73-80; §4.3 L311-313; §4.5 L463-464 | R-0005, R-0006 | `SPEC-0002`:585; P2 (`ARCH-0002`:146-148) | an importer that re-attests every field asserts what the source's signer did not vouch for |
| C-07 | constrains | Export needs `buildType`, `externalParameters` and `builder.id`; `reproducible` and `completeness` left v0.2 for `builder.id` | §4.2 L250; §4.3 L272; §4.4 L407; §4.5 L441, L503-504; §7 L630-631 | R-0011, R-0012, R-0032, R-0035, R-0040 | `ARCH-0001`:499, :443; DV-1 (`SPEC-0003`:565-610) | no DV-1 statement exports as SLSA provenance; DV-1's `reproducible` has no v1 field |
| C-08 | constrains | The predicate has no signature, key, algorithm or signer; its only cryptographic content is digests | §2 L42-43; §4.5 L496-505; §4.1 L157-162 | R-0039 | `SPEC-0002`:409-422, :629-638, :833-838; `ADR-0005`:36-43 | an envelope migration leaves the predicate as it is, and changes the signer half of every accepted pair: natively a new `kid` (§8) |
| C-09 | constrains | The provenance is always serialised as JSON with lowerCamelCase names | §4.1 L196-198 | R-0158 (inferred: an informative protobuf comment) | T-052 (`BACKLOG`:189); `PLAN-0001`:487; `PLAN-0002`:391; R-I-02 (`ARCH-0001`:442) | a KSA-CBOR form is a translation, never a provenance; with R-0039, only the original signed bytes stay acceptable to SLSA consumers (§6) |
| C-10 | constrains | Parameter completeness is required at Build L3 and best effort below; dependency completeness is best effort through L3; accuracy and completeness are implied by `builder.id` | §4.3 L292-295, L318-319, L391-394; §4.2 L258-259 | R-0014, R-0015 | D-04; `SPEC-0004`:613-615; `LIMITATIONS`:20-21 | a template over imported parameters is as strong as the completeness the relying party grants the builder, and no byte evidences it |
| K-01 | conflicts | Ignore-unknown and extension fields inside the payload of an imported statement | §3 L103-105; §4.7 L540-550 | R-0009, R-0043, R-0045, R-0046 | P5 (`ARCH-0002`:394-396); P5.2 (`ARCH-0002`:498-505, :519-521); `SPEC-0002`:918-922; `MECH`:1243-1246 | P5.2 scopes the collision to the envelope exterior and calls the interior ours; an imported Statement's interior is SLSA's (§4) |
| K-02 | conflicts | Minor versions add fields under one predicate type, which resolves to the latest minor version | L17, L20-23; §3 L106-109 | R-0051, R-0052, R-0170, R-0070, R-0071, R-0072 | `SPEC-0003`:495-501, :366-367; `ARCH-0003`:744; P5 | an import definition fixes one minor version; a later one's fields fail import or acceptance. T-052's version note is the live case (§6) |
| K-03 | conflicts | The builder is distinct from the signer, and is what is trusted to have run the build and populated the provenance | §2 L53-57; §4.4 L415-416; §4.5 L501-505 | R-0040 | P2 (`ARCH-0002`:146-148) | P2 has one party, the key; resolved in mapping by putting `builder.id` in C, not A (D-01) |
| K-04 | conflicts | Ignoring is made safe by asking producers for monotonic extensions | §4.7 L551-553; §3 L108 | R-0047 | P5 (`ARCH-0002`:394-403) | two answers to one hazard; and a consumer cannot check the monotonicity of a field it does not understand |
| S-01 | silent | Envelope, signature, signer identity | §2 L42-43; §4.5 L496-505 | — | R-I-03 (`ARCH-0001`:443); DEC-005 (`ARCH-0001`:633-635); `ADR-0004`:51-52 | nothing here bears on DEC-005 |
| S-02 | silent | Which digest algorithms are acceptable, and how strong | §4.1 L157-162 | — | R-M-07; `SPEC-0002`:848-854; `MECH`:288-294 | an import profile names its algorithms itself (C-02) |
| S-03 | silent | How provenance is verified: subject match, predicate type, builder | §5 L555-560 | — | `ARCH-0001`:400; `SPEC-0004`:513-516 | another SLSA page, outside this record |
| S-04 | silent | Lifetime, expiry or revocation of a provenance | whole source | — | `SPEC-0002`:437, :488-501; R-O-02 (`ARCH-0001`:454) | build times are not validity; an import chooses `valid` or omits it |
| S-05 | silent | Human-readable names and meanings as language maps | §4.2–§4.6 | — | P3 (`ARCH-0002`:222-224); `SPEC-0003`:433-435 | a conforming import definition's definer writes every map; nothing ties them to the source's prose |

---

## 2. Row details

Source passages are markers rendered by `bin/check-quotes`. Each row's
`finding` above is argued here or in the section it names.

### 2.1 Adopt

**A-01 — must-understand where the input is the caller's.**

<!-- q L73-75 "`externalParameters`" .. "downstream." -->
> `externalParameters`: the external interface to the build. In SLSA, these values are untrusted; they MUST be included in the provenance and MUST be verified downstream.

<!-- q L302-303 -->
> Verifiers SHOULD reject unrecognized or unexpected fields within `externalParameters`.

The second is the one place the source turns its own ignore-unknown default
(§3, K-01) around, and it does so for the one object it calls untrusted. That is
P5's reason in SLSA's own terms: `ARCH-0002`:394-396 makes an unknown field in a
signed payload an error, and `SPEC-0002`:918-922 forbids a verifier to skip
what it does not understand. Two limits. It is a SHOULD (R-0018), so a SLSA
verifier that accepts unknown parameters conforms. And it reaches only
`externalParameters`, where the underscore rule can contradict it (open
question 1).

**A-02 — the name the caller gave, apart from the digest it resolved to.**

<!-- q L336-339 "The parameters SHOULD" .. "`resolvedDependencies`." -->
> The parameters SHOULD only contain the actual values passed in through the interface to the build platform. Metadata about those parameter values, particularly digests of artifacts referenced by those parameters, SHOULD instead go in `resolvedDependencies`.

L342-351 shows it: a repository URL and a ref as parameters, the commit they
resolved to as a dependency's digest. R-0029 (L381-383) and the footnote, R-0031, R-0098 and R-0099
(L396-401), apply the same split to build configuration. `SPEC-0002`:479-486
makes the same move: a locator is evidence, carried as an attribute beside a
target that binds a digest, never the target itself (R-M-11, `ARCH-0001`:434);
mofn#144 withdrew the locator target for it (`SPEC-0002`:457). What the two do
not share is the digest. The example's is a `gitCommit` (L349), which has no
native code (C-02).

**A-03 — an opaque, case-sensitive identifier.**

<!-- q L519-522 "The exact meaning" .. "case-sensitive." -->
> The exact meaning and format is defined by `builder.id`; by default it is treated as opaque and case-sensitive.

KSA text is byte-exact and never normalised (`SPEC-0002`:222), and the text base
kind compares byte for byte (`SPEC-0003`:269), so `invocationId` maps with
nothing to decide. If a builder defines a looser equality, byte comparison can
only report two equivalent ids as different, never two different ids as equal:
it fails closed. R-0042 (globally unique) is the builder's to keep; nothing
native checks it.

**A-04 — a migration table already in R-I-01's shape.** §7 maps v0.2 to v1
field by field (L579-617), marks with `null` the three v1 fields v0.2 had no
source for (L606, L607, L614), lists the v0.2 fields no longer present with what
replaces each (L619-629), and has a category R-I-01 (`ARCH-0001`:441) does not:

<!-- q L630-631 -->
> - `metadata.completeness`: Now implicit from `builder.id`. - `metadata.reproducible`: Now implicit from `builder.id`.

R-I-01's columns are preserved, dropped and inferred. What those two lines
describe is none of the three: the value is not carried, not discarded by the
mapping, and not derivable from the bytes. It moved to an authority outside
them (X-03). **Ours:** T-053's table (`BACKLOG`:190) needs a fourth column for
this source, or what X-03 lists will read as dropped by our mapping when the
source moved it out first. §7 also carries a defect: R-0048 names a field that
appears nowhere else in the source (open question 5).

### 2.2 Adapt

**D-01 — signer-builder pairs as scoped trust.**

<!-- q L496-499 -->
> Consumers MUST accept only specific signer-builder pairs. For example, "GitHub" can sign provenance for the "GitHub Actions" builder, and "Google" can sign provenance for the "Google Cloud Build" builder, but "GitHub" cannot sign for the "Google Cloud Build" builder.

<!-- q L501-505 -->
> Design rationale: The builder is distinct from the signer in order to support the case where one signer generates attestations for more than one builder, as in the GitHub Actions example above. The field is REQUIRED, even if it is implicit from the signer, to aid readability and debugging. It is an object to allow additional fields in the future, in case one URI is not sufficient.

Under P2 the speaker is the key, and there is no second party who *said* it
(`ARCH-0002`:146-148). So `builder.id` cannot be a principal here. It is part of
the claim, an attribute of the attestation, and the pair becomes a trust
statement or an anchor whose `about` is that attribute's range
(`SPEC-0002`:591-617; `SPEC-0004`:179-198). An ask about `builder-id = X` is then
covered only by an attestation from a key the context trusts about a range that
contains X (`SPEC-0004`:519-536). That is `ARCH-0001`:393's configured trust in
which issuer may assert what, one level finer than a predicate type; and it
keeps `ADR-0003` D4's rule that a key trusted for one purpose gains nothing
elsewhere (`ADR-0003`:50). mofn survey R-001 observes that
SLSA's list of pairs lives nowhere in the format (`SURVEY`:1297-1299); natively
it is a signed or local anchor, and its evaluation is the authorization line
(`SPEC-0004`:577). DV-1 already asks a reviewer whether the provenance names the
expected builder (`SPEC-0003`:589).

What changes:

- `builder.id` is compared as text, byte for byte (`SPEC-0003`:269). The source
  types it as an in-toto TypeURI (L447) and gives no equivalence rule of its own;
  any URI equivalence wider than bytes makes the native check stricter, not
  looser.
- The source makes separate modes take separate ids, and only *should* take
  separate signers:

<!-- q L453-456 -->
> If a build platform has multiple modes of operations that have differing security attributes or SLSA Build levels, each mode MUST have a different `builder.id` and SHOULD have a different signer identity. This is to minimize the risk that a less secure mode compromises a more secure one.

  Natively a range scopes what counts; it does not stop a key trusted for one
  mode's id from signing another mode's id. Where one key signs for both, the
  separation SLSA wants rests on every relying party scoping every anchor, and
  the separation that holds without that is the key *(inferred)*. **Ours:** an
  import profile could treat the signer SHOULD as a condition of import.
- R-0040 keeps the builder REQUIRED even when the signer implies it (L503-504;
  the sentence names no field, read as `runDetails.builder`, SD-8), and R-0035
  requires its `id`, which is what lets the native attribute exist on every import.
- Scopes here are `SPEC-0003` attribute ranges, not a tag language, so DEC-004
  stays open (`ARCH-0001`:174-175).

**D-02 — `buildType` is a schema; give it a definer.**

<!-- q L283-286 "The URI SHOULD" .. "complete example." -->
> The URI SHOULD resolve to a human-readable specification that includes: overall description of the build type; schema for `externalParameters` and `internalParameters`; unambiguous instructions for how to initiate the build given this BuildDefinition, and a complete example.

That list covers three of P3's five parts (`ARCH-0002`:199-214): representation
(the parameter schemas), constraints on usage (how to initiate the build) and a
semantic description (the overall description). P3 has no part for the complete
example, and the list has nothing for P3's review tags or its short, possibly
multilingual descriptions. **Ours:** one
definition per build type, signed by whoever writes the import profile, holding
a record type for that build type's `externalParameters` and
`internalParameters` and a template for the attestation. It is the only
structured native home the parameters can have (C-01, §3), and the only way
R-0017's expectation can be a template (D-04). The identity changes: a
`DefinitionId` and its definer (`ADR-0007`:57-66), with the build type's URI kept
as data so that an export can write it back. The owner of the meaning changes
too. SLSA's is whatever the URL serves (X-03); a definition's is fixed by its
hash, and a later edit of the build type's page is a new definition or nothing
(`SPEC-0003`:495-501).

**D-03 — three spellings of absence, one native spelling.**

<!-- q L110 "Unset" .. "equivalently." -->
> Unset, null, and empty field values MUST be interpreted equivalently.

`SPEC-0002`:428-429 requires an absent optional field to be omitted, never
present empty or as a placeholder, and KSA has no null at all
(`SPEC-0002`:227-229). The rules agree on meaning and differ on enforcement:
SLSA accepts three spellings and reads them as one; KSA accepts one. Import maps
all three to omission with no loss of meaning, by R-0010 itself. Export emits
omission, which every SLSA consumer must read the same way. What is lost is the
producer's choice of spelling, which matters only to a byte round trip (§6). Two
cautions: R-0010 speaks of field values, and whether it reaches keys inside
`externalParameters`, which the build type defines, is not said; and a required
field whose empty value is read as unset is open question 2.

**D-04 — the expectation, published.**

<!-- q L297-300 "The build platform SHOULD" .. "harder that task becomes." -->
> The build platform SHOULD be designed to minimize the size and complexity of `externalParameters`, in order to reduce fragility and ease [verification]. Consumers SHOULD have an expectation of what "good" looks like; the more information that they need to check, the harder that task becomes.

`SPEC-0003`'s template is that expectation as a signed object: `fixed` values, a
closed attribute set, constraint rules (`SPEC-0003`:357-372, :384-425), checked
on the acceptance line (`SPEC-0004`:578), which `SPEC-0003` calls a rejection at
P5's *expected* level (`SPEC-0003`:358-360). What changes is who holds it: SLSA
leaves it to each consumer's policy; a template is published, cited by hash and
reused. It needs D-02, because a template can fix only attributes whose types
exist, and `externalParameters` has no type until a build type's definition gives
it one. R-0016 and R-0022 make it cheaper: few, string-valued parameters are the
case a text or enum attribute carries.

**D-05 — the builder's documentation, as statements.**

<!-- q L458-465 -->
> The `builder.id` URI SHOULD resolve to documentation explaining: - The scope of what this ID represents. - The claimed SLSA Build level. - The accuracy and completeness guarantees of the fields in the provenance. - Any fields that are generated by the tenant-controlled build process and not verified by the trusted control plane, except for the `subject`. - The interpretation of any extension fields.

<!-- q L449-451 -->
> URI indicating the transitive closure of the trusted build platform. This is [intended](verifying-artifacts#step-1-check-slsa-build-level) to be the sole determiner of the SLSA Build level.

Every item on that list is something a relying party relies on and the signed
bytes do not carry (X-03). **Ours:** a key the relying party trusts says them
about the builder, in attestations whose target is a description holding the
`builder.id` URI (`SPEC-0002` target type 6, `SPEC-0002`:458). A description
that is only a URI is a statement about the name, not about whatever the URL
serves (`SPEC-0002`:947-955), which is the reading wanted here. The claimed
level, the guarantees and the list of unverified tenant fields then become claims
a verdict can name, with who made them and with what standing, instead of a
page. `ADR-0003` rejected unsigned vocabulary documents on the same ground
(`ADR-0003`:66-67). Whether anyone would sign such statements is not a question
this source can answer.

### 2.3 Reject

**X-01 — skip what you do not understand, as a native rule.** The parsing rule
is in-toto's, summarised (L103); the extension clause is the source's own
(L540-550). Natively neither has anything to act on: KSA maps are closed, there
are no namespaced extension fields, all extension goes through attributes typed
by definitions (`SPEC-0002`:440-444; `ADR-0003`:47), and an unknown field is
invalid (`SPEC-0002`:918-922). Rejected as a native rule by P5
(`ARCH-0002`:394-396). At import it is a conflict, not a rejection: K-01.

**X-02 — names that are URIs.** The predicate type is a fixed URI (L17);
`buildType` and `builder.id` are typed TypeURI (L278, L447). P1 makes every
native extension point a pair of a defining key and a local label
(`ARCH-0002`:65-72), `ADR-0001` counts predicate types among them
(`ADR-0001`:32-35), and a statement cites its type by `type-ref`, never by URI
(`ADR-0007`:64-66; `ARCH-0001`:340). At the boundary each maps lossily
(`ADR-0001`:55-56; `ARCH-0001`:196, :496): the URI can travel as data, in a text
attribute or a definition; the authority behind it, whoever holds the DNS name,
does not. lane-a's first finding lists the same two SLSA identifiers among the
ones it found (`LANE-A README`:36).

**X-03 — meaning held at a URL.**

<!-- q L258-259 "The accuracy" .. "`runDetails.builder.id`." -->
> The accuracy and completeness are implied by `runDetails.builder.id`.

Add the predicate type URI that resolves to the latest minor version rather than
to a fixed text (L21-22), R-0013 (D-02), R-0037 (D-05) and the two fields v1.0
made implicit (L630-631, A-04). Each puts something a consumer relies on behind a
URL, unsigned, whose content can change. `ADR-0003` rejected that pattern
(`ADR-0003`:66-67); `ADR-0007` rejected leaving meaning to the application and
reusing URI-identified vocabularies (`ADR-0007`:91-101); and `SPEC-0003` treats
a URL as a retrieval hint whose content counts only if its hash matches
(`SPEC-0003`:181-186). On import none of it is lost by the mapping: it was never
in the signed bytes. D-02 and D-05 are the adapted forms.

**X-04 — a vendor prefix is not a namespace.**

<!-- q L543-546 -->
> - Extension fields SHOULD use names of the form `<vendor>_<fieldname>`, e.g. `examplebuilder_isCodeReviewed`. This practice avoids field name collisions by namespacing each vendor. Non-extension field names never contain an underscore.

`ADR-0001` rejected private-use ranges because two parties using one private
label collide with no principal to tell them apart (`ADR-0001`:64-67;
`ARCH-0002`:82-84). A vendor prefix is the same escape, by convention, without
even a registry. One thing the source does that a registry does not: it hands
the interpretation of extension fields to the builder's documentation (L465), so
an extension means what *a builder* says. That is closer to P1 than a registry
is. Nothing binds the prefix to that builder, though: two builders may write one
prefix, and the only thing in the bytes that names a builder is `builder.id`,
which the prefix does not mention.

### 2.4 Constrains

**C-01 — arbitrary JSON has no structured home.**

<!-- q L330-333 "The `externalParameters`" .. "aid verification." -->
> The `externalParameters` and `internalParameters` are the top-level inputs to the template, meaning inputs not derived from another input. Each is an arbitrary JSON object, though it is RECOMMENDED to keep the structure simple with string values to aid verification.

The cue types both as `object` (L135-136), annotation values as any JSON type
(L167-169) and `version` as a free map of strings (L143, L475); the proto summary
gives the parameters as `google.protobuf.Struct` and annotation values as
`google.protobuf.Value` (L207-208, L219). Against that, at `7c3c731`:

- KSA has no float and no null, and its integers stop at ±(2^53 − 1)
  (`SPEC-0002`:220, :227-229; `ADR-0004`:38-42).
- An attribute's value must be a valid assignment of one of twelve base kinds
  (`SPEC-0003`:265-278; `SPEC-0004`:258-264). None is a list and none is a byte
  string. The one map, `record`, holds only the fields its definition declares
  (`SPEC-0003`:275), named in the label grammar `[a-z][a-z0-9-]{0,62}`
  (`SPEC-0003`:202-205, :236). The source's own field names are lowerCamelCase
  (L197), so even a fixed record must rename them.
- Whether one `has` may carry two attributes of one type, which is how a list
  could be spelled, is not said: `SPEC-0002` §8.5 and `SPEC-0003` §7.1 have no
  rule on it (searched at `7c3c731` for repeat, duplicate and once).

So structured carriage needs a definition per build type (D-02) and still loses
floats, null, large integers, keys outside the label grammar, keys no definition
lists, and every list (§3). Opaque carriage, the JSON as one text value, keeps
the bytes and gives the evaluator nothing to scope on (§3.1). R-0022 recommends
string values, the case both carry. §7 states this as option 5's cost.

**C-02 — the digest set, and R-M-07.** The cue names three digest keys and admits
any other (L157-162). `SPEC-0002` registers SHA-256, SHA-384 and SHA-512
(`SPEC-0002`:848-854), so a subject's digest becomes a target `[2, alg, bytes]`
(`SPEC-0002`:454) only through one of those, and two of the cue's three named
keys qualify. The only digest value anywhere in the source is a `gitCommit`
(L349), in its one worked dependency (L342-351), and it has no native code.
Dependencies are recorded where known (L84-87) and completely only on a
best-effort basis (L318-319, L391-394), and the source calls recording both a
URI and a digest valuable where practical (L391-393), so a dependency may carry
one without the other *(inferred)*. Three consequences:

- a subject whose digests are all outside `SPEC-0002` §12.5 cannot be a digest
  target; it can still be targeted by a description (type 6, `SPEC-0002`:458,
  :473-477), whose canonical encoding is then what R-M-07 binds (`ARCH-0001`:430),
  and nothing native binds the artifact's own bytes;
- a dependency lifted into a native statement of its own needs a registered
  digest to be targeted by content; one with only a URI is a target only as a
  description, a statement about the name and not about what it serves
  (`SPEC-0002`:457, :479-486, :951-954);
- a dependency kept inside the predicate's value is not bound by R-M-07, which
  binds `this`.

mofn report R-0006 already says an import must name the algorithms it accepts,
or a `gitCommit` meets R-M-07 in form and not in substance (`MECH`:288-294).
This source's worked example is that case. The source does not say how a digest
value is written (each is typed `string`, L158-161), so an export that re-spells
a native byte string as text chooses the spelling.

**C-03 — a set in an array.**

<!-- q L318-319 "Unordered" .. "L3." -->
> Unordered collection of artifacts needed at build time. Completeness is best effort, at least through SLSA Build L3.

A KSA array is ordered and its order is signed (`SPEC-0002`:224). Condition (5),
a canonical order for set-valued fields carried in arrays, is owed to
`SPEC-0002` (`ADR-0004`:105-108) and P5.1 does not address it
(`ARCH-0002`:474-477). This is a foreign case of it: an importer either sorts,
so equal sets have equal bytes and the producer's order is gone, or keeps the
order, so one set imported from two producers differs in bytes. SLSA gives the
order no meaning, so sorting loses nothing it means; it loses only the bytes
(§6). `byproducts` and `builderDependencies` are arrays too, and the source says
nothing about their order (L423-433, L467-472).

**C-04 — time, to the second.** `startedOn` and `finishedOn` are typed as in-toto
Timestamps (L524-532); the informative cue's comment spells a whole-second UTC
time ending in `Z` (L172), and the informative proto imports
`google.protobuf.Timestamp` (L194, L236-237). KSA time is whole seconds since
2026-01-01, with no leap second (`SPEC-0002`:268-279), and its human form is
the cue's pattern exactly (`SPEC-0002`:280-282). A whole-second UTC value maps
exactly, to the time base kind (`SPEC-0003`:276). A fraction or a leap second
has no native form, and the source does not settle whether either may occur
(open question 4). Neither time is a validity bound (S-04).

**C-05 — one provenance, many outputs; one statement, one target.**

<!-- q L96-97 -->
> - Finally, the build process outputs one or more artifacts, identified by `subject`.

A statement has one `this` (`SPEC-0002`:436). Import therefore fans out to one
attestation per subject, each carrying the predicate, and the native form no
longer says those outputs came from one invocation unless an attribute carries
it. `invocationId` could, but nothing in BuildMetadata is required (R-0041,
L511) and its uniqueness is a SHOULD (R-0042). A subject with several digests
keeps one as its target; the rest have nowhere to go, since `aliases` has no KSA
form (`ARCH-0001`:481). The Statement's own fields are in-toto's (L245-246) and
T-051's to map.

**C-06 — not every field is the signer's claim.**

<!-- q L311-313 "There is no need" .. "practical to do so." -->
> There is no need to [verify][Verification] these parameters because the build platform is already trusted, and in many cases it is not practical to do so.

<!-- q L463-464 "Any fields" .. "`subject`." -->
> Any fields that are generated by the tenant-controlled build process and not verified by the trusted control plane, except for the `subject`.

So one signed provenance carries three kinds of content: what the platform sets
and vouches for (internal parameters, L77-80), what it received and relays
(external parameters, untrusted, L73-75), and fields the tenant's build wrote
and the control plane did not check, which only the builder's documentation
lists. A native attestation has no such gradation: its speaker asserts that the
target has each attribute (`SPEC-0002`:585). An importer that re-attests every
field asserts, under its own key, what the source's signer did not vouch for.
*(inferred)* An import profile either drops the tenant-written fields, which it
can tell apart only from documentation (X-03), or types them so that they mean
*reported by the build*, not *true of the build*.

**C-07 — export needs fields DV-1 does not have.** The fields the source requires
at Build L1 are `buildDefinition` and `runDetails` (R-0011, L250), `buildType`
and `externalParameters` (R-0012, L272), `builder` (R-0032, L407) and its `id`
(R-0035, L441), with the builder REQUIRED even when the signer implies it
(R-0040, read as `runDetails.builder`, SD-8). The native supply-chain vocabulary,
DV-1, has two enum types of three values each, `build-provenance` and `outcome`,
and a template, and none of these fields (`SPEC-0003`:565-610; TV-4 assigns
`reproducible`). `build-provenance`'s first value, `reproducible`, has no v1
field to come from or go to:

<!-- q L631 -->
> - `metadata.reproducible`: Now implicit from `builder.id`.

So `ARCH-0001` §6's export mark for SLSA provenance v1 (`ARCH-0001`:499) is
reachable only for statements that carry an imported predicate, or that are
issued under a SLSA-shaped native definition (D-02). No DV-1 statement exports
as SLSA provenance; it can export, at most, as an in-toto Statement with a
predicate type of its own *(inferred)*. What URI an export writes for
`builder.id` and `buildType`, when the native speaker is a key and the native
type a `DefinitionId`, is open question 9.

**C-08 — a predicate without a signature.** Provenance is an attestation
(L42-43), carried in an in-toto Statement (L126-131); it has no signature, key,
algorithm or signer field, and the source's only examples of signers are
organisations (L496-499). Its only cryptographic content is digests (L157-162).
§8 draws the post-quantum consequences.

**C-09 — JSON, always.**

<!-- q L197 "provenance is always" .. "lowerCamelCase." -->
> provenance is always serialized using JSON with lowerCamelCase.

A KSA-CBOR rendering of a provenance is therefore a translation and never a
provenance: no SLSA consumer reads it. With R-0039, which makes acceptance
depend on the signer (D-01), this decides what a round trip can keep (§6), for
T-052 (`BACKLOG`:189), the I4 demo (`PLAN-0001`:487) and M5 (`PLAN-0002`:391).

**C-10 — completeness is granted, never shown.**

<!-- q L292-295 "They MUST be complete" .. "best effort.)" -->
> They MUST be complete at SLSA Build L3, meaning that there is no additional mechanism for an external party to influence the build. (At lower SLSA Build levels, the completeness MAY be best effort.)

Dependency completeness is best effort even at L3 (L318-319, L391-394), and the
accuracy and completeness of the whole build definition are implied by
`builder.id` (L258-259). So when a template over imported parameters passes
(D-04), what it shows is that the parameters recorded are the expected ones.
Whether they are all the inputs is what the relying party grants the builder by
trusting its id, at L3, and is not promised below it (R-0015). No byte of the
provenance evidences it. That is the verdict's limit line, applied to
completeness (`SPEC-0004`:613-615), and `LIMITATIONS`:20-21's statement that we
do not verify builds.

### 2.5 Conflicts

**K-01 — ignore-unknown inside an imported payload.** Argued in §4.

**K-02 — one identifier, a growing type.**

<!-- q L106-107 "The `predicateType` URI" .. "incompatible change." -->
> The `predicateType` URI includes the major version number and will always change whenever there is a backwards incompatible change.

<!-- q L108-109 "Minor version" .. "`predicateType`." -->
> Minor version changes are always backwards compatible and "monotonic." Such changes do not update the `predicateType`.

The first half agrees with us: an incompatible change takes a new identifier, as
a KSA registry entry is never reassigned (`SPEC-0002`:817-822). The second half
does not. A native definition is never edited: a change is a new
`DefinitionId`, linked by `supersedes` from the same definer
(`SPEC-0003`:495-501; `ARCH-0003`:744). A template is closed
(`SPEC-0003`:366-367), and an unknown field is an error (P5). So an import
definition is written against one minor version, and a provenance from a later
one, carrying a field that version added under the same predicate type, fails at
import if the importer is strict (K-01) or at acceptance if the field reaches a
closed template. The source's answer is that minor versions are monotonic, so a
consumer may ignore what it does not know: K-04. T-052's version note is this
row's live case (§6).

**K-03 — the signer and the builder.**

<!-- q L415-416 -->
> Identifies the build platform that executed the invocation, which is trusted to have correctly performed the operation and populated this provenance.

P2 has one party: the key that signs is the speaker, with no authority above it
(`ARCH-0002`:146-148). The source has two: a signer, and a URI-named platform
trusted to have run the build and written the provenance, kept distinct so one
signer can serve several builders (L501-505). Resolved in mapping, not in
principle: the signer's key is A and `builder.id` is part of C (D-01). What the
mapping cannot carry is any trust in a builder apart from its signer: natively
a builder is trusted only as a value that some trusted key attests to.

**K-04 — monotonic, or must-understand.**

<!-- q L551-553 "Extension fields SHOULD follow" .. "ALLOW." -->
> Extension fields SHOULD follow the [monotonic principle][parsing rules], meaning that deleting or ignoring the extension SHOULD NOT turn a DENY decision into an ALLOW.

P5's case for must-understand is that a reader who skips a field may accept what
the writer meant to refuse, and it cites a real authorization bypass of that
shape (`ARCH-0002`:398-403). SLSA answers the same hazard from the other side:
ask writers, at SHOULD strength, never to write an extension whose loss turns a
DENY into an ALLOW, and skipping is then safe. The two agree on a monotonic
extension. They part on a non-monotonic one, which an ignoring SLSA consumer
accepts and P5 rejects. And the property SLSA relies on cannot be checked by the
party it protects: monotonicity is a fact about a field's meaning, and a
consumer skipping the field is, by definition, one that does not know its
meaning. *(inferred)* Under SLSA the safety of every ignoring consumer rests on
every producer keeping a SHOULD.

### 2.6 Silent

**S-01 — envelope and signer.** No signature, envelope or signer identity is
defined (C-08). R-I-03's envelope (`ARCH-0001`:443) and DEC-005, which is open
(`ARCH-0001`:633-635; `ADR-0004`:51-52), get nothing from this source.

**S-02 — digest algorithm policy.** No algorithm is required, none is excluded,
no strength is stated (L157-162). An import profile names its own (C-02;
`MECH`:288-294).

**S-03 — verification.** §5 points elsewhere (L555-560). Matching a subject to
the SLSA artifact in hand, checking the predicate type and checking the builder
are not in this source. `ARCH-0001`'s statement acceptance (`ARCH-0001`:400)
and `SPEC-0004`'s rule that a digest subject is computed from the relying
party's own copy (`SPEC-0004`:513-516) have no counterpart here.

**S-04 — lifetime.** No expiry, validity window or revocation. `startedOn` and
`finishedOn` say when the build ran (L527, L532). A native import chooses `valid`
itself, or omits it, which `SPEC-0002` allows since `valid` is only RECOMMENDED
there (`SPEC-0002`:437). R-O-02's preference for short validity
(`ARCH-0001`:454) has nothing in the source to start from.

**S-05 — words for people.** Field meanings are English prose in tables
(§4.2–§4.6), not language maps. A conforming definition needs names and a short
text for every type, and names and a description for every record field
(`SPEC-0003`:433-435); the definer of an import profile writes them, and nothing
ties them to the source's prose. P3 requires more than one language
(`ARCH-0002`:222-224).

---

## 3. Field by field onto an ArtifactStatement (R-I-01, T-051, T-053)

### 3.1 Two ways to carry a predicate

`ARCH-0001` says SLSA provenance travels as a predicate, not as native types
(`ARCH-0001`:196-197), and maps it to an ArtifactStatement predicate
(`ARCH-0001`:499). A predicate is an attribute, a type and a value
(`ARCH-0001`:341; `SPEC-0002`:503-521), and the value must be an assignment of a
base kind (C-01). That leaves two forms; the table gives both.

- **Structured (S).** Each field the profile knows becomes its own attribute,
  typed by an import definition, and the parameters become a record under a
  per-build-type definition (D-02). Trust can be scoped on `builder-id` (D-01)
  and a template can fix parameters (D-04). Everything the definitions do not
  declare is lost.
- **Opaque (O).** The Statement's JSON, exactly as signed, becomes one text value
  (byte-exact, `SPEC-0002`:222), or its SHA-256 becomes a digest value, by
  reference. Nothing is lost and nothing inside is evaluated: P5 is met only
  because the verifier understands *a text*. A verifier must accept a TBS of at
  least 65,536 octets and may reject a larger one (`SPEC-0002`:926-928),
  and the source bounds no list.

*(inferred)* The useful form is both: (O) for fidelity, (S) for what trust and
acceptance read. Then one value has two places, and only the importer's
signature says they agree. `ARCH-0002` P1.1, still draft, met that shape for a
COSE key identifier and chose rejection on disagreement (`ARCH-0002`:113). Open
question 10.

### 3.2 The table

A path is a JSON path in the Statement; *req* is the source's REQUIRED marking
(L1 = REQUIRED for SLSA Build L1); *round trip* is under (S). Under (O) every row
round-trips byte for byte, within `SPEC-0002`:926-928.

| path | in the source | req | native home under (S) | round trip | lost under (S) |
|---|---|---|---|---|---|
| `_type` | in-toto constant (L127) | — | none; implied by the import profile | written back as the constant | nothing here; the Statement is T-051's |
| `subject[]` | ResourceDescriptors for the outputs (L96-97, L128, L245-246) | — | one attestation per element, `this` = `[2, alg, bytes]` (`SPEC-0002`:454) | its digest, for SHA-256, SHA-384 or SHA-512 only (`SPEC-0002`:848-854) | the grouping, `name`, a subject's other digests (C-05); a subject with no registered digest is not importable (C-02) |
| `predicateType` | URI constant (L17, L131) | — | the `type-ref` of an import definition (`ARCH-0001`:196, :496) | written back from the profile | the URI's authority (X-02); which minor version (K-02) |
| `predicate.buildDefinition` | object (L255-259) | L1 (R-0011) | no node of its own | through its fields | — |
| `buildDefinition.buildType` | TypeURI (L277-287) | L1 (R-0012) | a text attribute; or the key that selects a per-build-type definition (D-02) | the URI string | its meaning (X-03) |
| `buildDefinition.externalParameters` | object, arbitrary JSON (L289-303, L330-333) | L1 (R-0012) | a record under a per-build-type definition (D-02); otherwise none | only under that definition, and only string, boolean and integer leaves under listed keys | floats, null, integers past ±(2^53 − 1), unlisted or non-label keys (C-01); an unknown key is rejected, as R-0018 also asks (A-01) |
| `buildDefinition.internalParameters` | object, arbitrary JSON (L305-313) | OPTIONAL (R-0006) | as `externalParameters` | as `externalParameters` | as `externalParameters`; may be dropped without touching SLSA verification (L311-313), at the cost of R-0007's and R-0019's uses |
| `buildDefinition.resolvedDependencies[]` | ResourceDescriptors, unordered (L315-322) | — | none, for want of a list base kind (`SPEC-0003`:265-278); or one attestation per dependency that has a registered digest | no | the list; its order (C-03); `gitCommit`-only and URI-only entries (C-02) |
| `predicate.runDetails` | object (L261-264) | L1 (R-0011) | no node of its own | through its fields | — |
| `runDetails.builder` | object (L412-416) | L1 (R-0032) | no node of its own | through its fields | the room for future fields it is an object to keep (L504-505) |
| `builder.id` | TypeURI (L446-465) | L1 (R-0035; R-0040 if *the field* of L503 is the id, SD-8) | a text attribute, and the scope of trust (D-01) | the URI string | its meaning: scope, level, guarantees (X-03, D-05) |
| `builder.builderDependencies[]` | ResourceDescriptors (L467-472) | — | none, as `resolvedDependencies` | no | as `resolvedDependencies`; order not stated |
| `builder.version` | map of strings (L474-477) | — | none: the keys are the platform's (C-01) | no | every pair |
| `runDetails.metadata` | object (L418-421) | none (R-0041) | no node of its own | through its fields | — |
| `metadata.invocationId` | string, opaque, case-sensitive (L516-522) | — | a text attribute (A-03) | yes | nothing |
| `metadata.startedOn`, `metadata.finishedOn` | Timestamp (L524-532) | — | time attributes (`SPEC-0003`:276) | at whole-second UTC, yes | a fraction, a leap second (C-04) |
| `runDetails.byproducts[]` | ResourceDescriptors (L423-433) | — | none, as `resolvedDependencies` | no | as `resolvedDependencies`; order not stated |
| descriptor `uri`, `downloadLocation` | strings (L156, L164) | — | text attributes, never a target (`SPEC-0002`:479-486) | where the descriptor has a home | — |
| descriptor `digest` | map of algorithm to string (L157-162) | — | a digest value or target, three algorithms (`SPEC-0003`:272) | registered algorithms, re-spelt from bytes | `gitCommit` and every other key (C-02); the value's spelling |
| descriptor `name`, `mediaType` | strings (L163, L165) | — | text attributes | where the descriptor has a home | — |
| descriptor `content` | bytes, base64 in JSON (L166, L218) | — | none, for want of a bytes base kind | no | the bytes |
| descriptor `annotations` | map to any JSON value (L167-169, L219) | — | none | no | all of it |
| extension fields, in any object | named `<vendor>_<fieldname>` (L540-553) | — | none (`SPEC-0002`:440-444; `ADR-0003`:47) | no | the field, and its builder-given meaning (L465); K-01 |
| fields of a later minor version | ignored by rule (L105, L108-109) | — | none | no | K-01, K-02 |

### 3.3 What round-trips, what is lost, what has no home

Over the 24 rows of §3.2, under (S), classified by hand:

- **4 are containers** with no node of their own: `buildDefinition`,
  `runDetails`, `builder`, `metadata`.
- **5 round-trip as values:** `_type`, `predicateType`, `buildType`,
  `builder.id`, `invocationId`. Three of them lose what the value meant (X-02,
  X-03, K-02).
- **7 round-trip in part:** `subject[]` (registered digests only),
  `externalParameters` and `internalParameters` (only under a per-build-type
  definition), the two times (whole seconds), and the descriptor's `digest`,
  `uri`/`downloadLocation` and `name`/`mediaType` (only where the descriptor is a
  subject or a lifted dependency).
- **8 have no structured home:** the three descriptor lists, `version`,
  `content`, `annotations`, extension fields, and later-minor-version fields.

Under (O) all 24 keep their bytes, and none can be scoped or fixed by a
template.

### 3.4 A loss cell for `ARCH-0001` §6 (Ours, for T-053's owner)

Offered as text for the empty cell at `ARCH-0001`:499, decided by nobody here:

```text
Structured: subject digest as target (SHA-256/384/512 only), one statement per
subject; buildType, builder.id, invocationId as text; times at whole seconds;
parameters only under a per-buildType definition. No native home: the three
ResourceDescriptor lists, version, annotations, content, extension fields,
later-minor fields. Opaque: the signed JSON as one text value, kept byte for
byte, evaluated not at all. predicateType, buildType, builder.id URIs <->
key-relative types, lossy (P1). Moved out of band by the source, not dropped
by us: level, accuracy, completeness, reproducibility (builder.id). Unknown
fields inside the payload vs P5: open (P5.2 covers the envelope exterior).
```

---

## 4. The parsing rules against P5 and P5.2 (K-01, X-01, K-02, K-04)

<!-- q L103 -->
> This predicate follows the in-toto attestation [parsing rules]. Summary:

<!-- q L105 "Consumers" .. "noted." -->
> Consumers MUST ignore unrecognized fields unless otherwise noted.

<!-- q L540-541 "Implementations" .. "standard field." -->
> Implementations MAY add extension fields to any JSON object to describe information that is not captured in a standard field.

<!-- q L547-550 "Extension fields MUST NOT" .. "extension field." -->
> Extension fields MUST NOT alter the meaning of any other field. In other words, an attestation with an absent extension field MUST be interpreted identically to an attestation with an unrecognized (and thus ignored) extension field.

Natively none of this has anything to act on (X-01). The question is import,
and mofn has answered it for one layer only. P5.2 scopes the DSSE collision to
the envelope exterior, the siblings of `payload`, `payloadType` and
`signatures`, and treats the payload interior as ours to govern
(`ARCH-0002`:498-501); its clause then has P5 govern the interior in both
directions (`ARCH-0002`:503-505). mofn report R-0006 reached the same scope
(`MECH`:1243-1246). Both assume the interior is a native statement. An imported
provenance's interior is an in-toto Statement, and the rules above are its
rules. So which reading the interior gets on import is stated nowhere, and it is
the reading that decides whether a real provenance imports at all.

The readings available, none chosen here:

1. **P5 on the interior.** Reject any field the profile does not know: P5.2's
   import rule carried inward. Our importer is then a non-conforming SLSA
   consumer by R-0009 and R-0046, a documented deviation of the kind P5.2
   already accepts at the exterior (`ARCH-0002`:509). The cost is concrete: a
   valid provenance carrying one extension field, or one field a later minor
   version added (K-02), does not import.
2. **SLSA's rule on the interior.** Skip unknown fields. P5 allows skipping when
   it is opt-in and explicit (`ARCH-0002`:394-396), so a profile that declares it
   does not breach P5 in principle. But nothing in `SPEC-0002` or `SPEC-0003` can
   declare a field skippable (`SPEC-0002`:440-444), and DEC-008's proposed answer
   keeps what *valid* means in the fixed core, out of key-local definitions
   (`ARCH-0002`:576-580). So the declaration would sit in a specification,
   `MAP-0002`, not in a definition. The cost is K-04.
3. **Opaque carriage.** P5 is met because the verifier understands the one text
   value; the fields inside are never evaluated, so nothing is skipped and
   nothing is checked (§3.1).
4. **Both.** (S) for what the profile knows, (O) for the rest; reading 1 or 2
   still governs the fields (S) extracts from (O).

One part of the source agrees with P5 outright: unknown fields inside
`externalParameters` (A-01). One part makes the line hard to draw: the
underscore rule that says which fields are extensions (open question 1).

P5.2's export rule extends without strain *(inferred)*: an export that writes no
extension field, and nothing a SLSA consumer would have to ignore, is a
conforming producer, since the source permits extension fields and requires none
(R-0043).

P5.2 says its deviation belongs in the R-I-01 table rather than in prose
(`ARCH-0002`:519-521). So does this one: T-053.

## 5. Trust in `builder.id` (D-01, D-05, K-03, X-03, C-06, C-10)

The source puts nearly all of a consumer's trust in one URI. The build level is
meant to be a function of it alone (L449-451); the accuracy and completeness of
the build definition are implied by it (L258-259); v0.2's `completeness` and
`reproducible` became implicit in it (L630-631); and control-plane traffic the
provenance does not record is implied by it (L89-92). What makes the URI
trustworthy is the signer-builder pair (L496-499), and what makes the pair mean
anything is the documentation at the URI (L458-465).

Mapped onto mofn, that trust splits three ways:

- the pair is **authorization**: a trust statement or anchor scoped by a
  `builder-id` range (D-01), read on the authorization line (`SPEC-0004`:577);
- what the documentation says is a set of **claims about the builder**, which
  natively someone must sign (D-05) or no verdict can name it;
- what the tenant asked for is **acceptance**: a template over
  `externalParameters` (D-04), read on the acceptance line (`SPEC-0004`:578),
  apart from authorization as R-O-06, a Should, asks (`ARCH-0001`:402, :458).

Trust in `builder.id` alone cuts against that split in one place. A verifier
that stops at the pair has checked the platform and not the request. The source
itself does not let it stop there (R-0005), and mofn survey R-001 records a
2026 compromise whose provenance named the right builder, so that a builder
check would have passed (`SURVEY`:1336-1346). It cuts against nothing in another place:
SLSA scopes trust below the signer, because one signer may sign for several
builders (L501-505), which is `ADR-0003` D4's point that a key trusted for one
purpose gains nothing elsewhere (`ADR-0003`:50). And it leaves completeness where no mapping can
reach it: the relying party grants it by trusting the id, and nothing in the
bytes shows it (C-10).

## 6. T-052: what a round trip can keep

T-052 asks to round-trip a real SLSA provenance from a public release
(`BACKLOG`:189); I4's demo is that a real SLSA attestation imports as an
`ArtifactStatement` and round-trips (`PLAN-0001`:487; `PLAN-0003`:48); M5 asks for
at least five public examples (`PLAN-0002`:391). None says what must survive. The source
admits two answers.

**Byte-faithful.** The provenance is always JSON (C-09), so no KSA-CBOR
translation reproduces it. The exact Statement bytes travel opaquely (§3.1), and
for a SLSA consumer to accept the result, the original envelope and signature
travel with them, because acceptance is per signer (R-0039). lane-a's sample 3
already keeps every layer of a real provenance (`LANE-A 03`:1, :13-14), the
Statement as the signed octets (`LANE-A 03`:102); the bundle and envelope files
are re-serialised (`LANE-A 03`:96-101), so besides the Statement only the registry
response is as received (`LANE-A 03`:51-52). It checks its signature only as the leaf
certificate's key over DSSE's pre-authentication encoding
(`LANE-A README`:27, :32), and leaves it unchanged because the key is not ours
(`LANE-A README`:62). Its output is untracked; at `7c3c731` only the digests and an environment
record are tracked, the Statement's digest among them (`LANE-A .gitignore`:4-6;
`LANE-A SUMS`:32).
This pass did not read those bytes.

**Meaning-faithful.** The source lets an exporter drop null and empty values
(R-0010) and, for consumers that do not recognise them, extension fields
(R-0046), so a re-encoded provenance can be read identically by such consumers.
But it needs a signature, and if the importer signs it, every SLSA consumer
configured for the original signer and builder rejects it (R-0039).
*(inferred)* A meaning-faithful round trip yields a provenance that SLSA
consumers read the same way and accept from nobody but the importer.

So *(inferred)* the round trip a SLSA consumer still accepts is the one that
never re-encodes. Either way the native statement's speaker is the importer
*(inferred)*: the original signer never signed a KSA TBS, and R-I-02 says an
import must not require the foreign object to become a native anchor
(`ARCH-0001`:442). The importer checks the pair at import and says so under its
own key: *(inferred)* the shape of a verification summary, whose record,
`slsa-vsa-1-2`, T-053 already names as an input (`BACKLOG`:190) and this pass
did not read. Open question 11.

**The version note: noted, not reconciled.** T-052 says v1.1, the library holds
1.2, and the row leaves it to its owner (`BACKLOG`:189; `DL-0047`:16-20). What
this source says that bears on it:

- the predicate type carries only the major version (L17, L106-107), and minor
  versions do not change it (L108-109); lane-a's fifth finding observed the same
  of v1.0 and v1.1 (`LANE-A README`:52);
- the change history has entries for v1.2, v1.0, v0.2, the rename, v0.1.1 and
  v0.1, and none for v1.1 (L633-697); the v1.2 entry is one note about a diagram:

<!-- q L637-638 "Note the difference" .. "diagram." -->
> Note the difference between the *provenance* build model diagram and the general SLSA build model diagram.

- the page still names the SLSA v1.0 provenance requirements as what the
  predicate satisfies (R-0002), and its migration targets v1.0 (L582, L619).

None of that says a v1.1 provenance is field-for-field a v1.2 one. A change
history can be incomplete, and K-02 is how a later minor version's field would
bite.

## 7. MD-3 and `ADR-0004`: what a JSON predicate costs option 5

This is not a COSE, CBOR or envelope document, so `docs/extraction.md`'s MD-3
paragraph does not bind it; it is recorded because C-01 and C-03 are option 5's
costs at this boundary. MD-3 narrowed DEC-002 to option 5 (`MEET-0928`:51-54);
`ADR-0004` accepted it and closed the narrowing (`ADR-0004`:36-52, :132-133). It
is `reviewed: false` and changes only by superseding (`ADR-0004`:11, :20).

- **The cost, evidenced.** KSA-CBOR excludes floats and null and bounds
  integers, and `SPEC-0003`'s base kinds hold no list or byte string (C-01).
  SLSA's parameters and annotations are arbitrary JSON, its dependency lists are
  lists, and `content` is bytes. `ADR-0004` item 3 accepts lossy mapping at
  interchange, per R-I-01 (`ADR-0004`:46-50); this source names the loss.
- **Where it cuts against option 5.** The exclusion is option 5's own
  restriction, taken out of a data model that has floats and null
  (`ADR-0004`:38-42). No other option, as `ARCH-0001` lists them, states that
  restriction (`ARCH-0001`:527-531); options 2, 3 and 4 name CBOR or JSON,
  whose data models have both, so they would carry these values as values.
  Whether they would carry their bytes this source cannot show: a canonical
  encoding re-serialises. `ADR-0004`'s scoring has no criterion for fidelity to JSON
  predicates on import (`ADR-0004`:64-72); the nearest, SCITT alignment, scores
  option 5 at the export boundary. Option 3 was withdrawn on four grounds
  (`ADR-0004`:121-124). The cited lines name only the strongest, that RFC 8785
  forbids the array reordering mofn needs; C-03's sorting of an unordered array
  is a case of that need, so this source touches that ground. The other three
  are not named there and were not read. Recorded for
  `ADR-0004`'s reviewer, not as a reason to reopen it.
- **Where it favours option 5.** R-0010 makes null mean nothing in SLSA's own
  fields, so KSA's lack of it costs nothing there; R-0022 recommends string
  values, which KSA carries byte-exact.
- **Condition (5).** C-03 is a foreign set carried in an array: a concrete case
  of what `ADR-0004` left owed (`ADR-0004`:105-108).
- **Not a discriminator.** The predicate prescribes no canonical form, and
  nothing here needs one.

## 8. Post-quantum: a signature-agnostic predicate (C-08, S-02)

- Nothing in the predicate names a signature algorithm or a key (C-08), so a
  move to a post-quantum signature is an envelope event. The predicate's bytes
  do not change, and a provenance re-signed under another algorithm says the
  same thing.
- What changes is the signer half of every accepted pair (R-0039). Natively a
  new algorithm is a new key and so a new `kid` (`ADR-0005`:36-43;
  `SPEC-0002`:833-838), and every trust statement scoped by `builder-id` to the
  old key must be re-issued, or the old key must name the new one by `rotate`
  (`SPEC-0002`:629-638).
- A native re-attestation of an imported provenance under suite 8 is specified
  and provisional, with no published vectors (`SPEC-0002`:409-422); the predicate
  would ride inside it unchanged.
- The predicate's only cryptographic content is digests, under no algorithm
  policy (S-02); `SPEC-0002` admits SHA-256, SHA-384 and SHA-512
  (`SPEC-0002`:848-854). This file makes no claim about any of them after a
  quantum transition.
- The source's signers are organisations (L496-499); which key an organisation
  signs with, and when it changes, is outside it (S-01).

## 9. Open questions

1. **Which fields are extensions?**

<!-- q L543-546 -->
> - Extension fields SHOULD use names of the form `<vendor>_<fieldname>`, e.g. `examplebuilder_isCodeReviewed`. This practice avoids field name collisions by namespacing each vendor. Non-extension field names never contain an underscore.

   The Statement in the same summary has a standard field whose name begins with
   an underscore:

<!-- q L127 -->
> "_type": "https://in-toto.io/Statement/v1",

   And `externalParameters` is an arbitrary object whose keys the build type, or
   its caller, chooses (L292-293, L330-333). A key there with an underscore meets
   three rules: as an extension it must be read as if absent (R-0046); as a
   parameter it must be verified (R-0005); as an unexpected field it should be
   rejected (R-0018). No precedence is given. Whether the underscore rule reaches
   the Statement's fields, or the keys of maps (`digest`, `annotations`,
   `version`, the parameters), is not said.
2. **Is `{}` a present `externalParameters`?** R-0012 requires the field at L1
   (L272); R-0010 reads an empty value as unset (L110). A build with no external
   parameters must then omit a required field, or present an empty one that is
   read as absent. lane-a's SLSA-shaped sample sets it to `{}`
   (`LANE-A 02`:41).
3. **Validity by level.** Four of the six REQUIRED statements hold for SLSA Build
   L1 only (R-0011, R-0012, R-0032, R-0035); BuildMetadata's (R-0041) and
   R-0040 name no level. The level is meant to come from `builder.id`
   (L449-451), out of band. Whether a provenance's well-formedness can be decided
   from its bytes is not said. A native template's required attributes are
   unconditional (`SPEC-0003`:365).
4. **Timestamp precision.** The cue's comment fixes whole seconds and `Z` (L172);
   the proto imports `google.protobuf.Timestamp` (L194, L236-237); the text links
   to in-toto's Timestamp (L525, L530) and says the text governs both summaries
   (L116-117, L178-179). Whether a fraction or an offset may appear is in a
   document this record does not hold. KSA time cannot carry a fraction (C-04).
5. **`inputArtifacts`.**

<!-- q L582-583 "The `buildType` MUST" .. "`inputArtifacts`." -->
> The `buildType` MUST be updated for v1.0 to describe how to // interpret `inputArtifacts`.

   No other line of the source names `inputArtifacts`. v1's dependency field is
   `resolvedDependencies`, renamed from v0.2's `materials` (L651), and the release
   candidates' renames are listed without it (L669-674). What a v1 build type
   must describe is unclear.
6. **Is `content` the resource's bytes?** The cue gives base64 bytes (L166), the
   proto `bytes` (L218); this page does not define the field. If it is the
   resource, an importer could compute a SHA-256 of it, an *inferred* R-I-01
   entry that would give a descriptor with no digest a native target. Not
   checked.
7. **Order of `byproducts` and `builderDependencies`.** Only
   `resolvedDependencies` is called unordered (L318). Whether the other two
   arrays' order means anything decides whether an importer may sort them (C-03).
8. **The reading an imported interior gets** (K-01, §4): P5, SLSA's rule, opaque,
   or both. Owed to the R-I-01 table (`ARCH-0002`:519-521) and to `MAP-0002`
   (`BACKLOG`:188).
9. **Export identifiers.** An export needs a URI for `builder.id` and one for
   `buildType` (C-07), where the native speaker is a `kid` and the native type a
   `DefinitionId`. lane-a's JSON form for a key-relative name is a placeholder,
   explicitly not a proposal (`LANE-A README`:58). Bears on R-I-03
   (`ARCH-0001`:443).
10. **Two places for one value** (§3.1). With (S) and (O) both carried, does a
    verifier check that they agree, or is the importer's signature the check?
    P1.1, draft, chose rejection on disagreement for a COSE key identifier
    (`ARCH-0002`:113).
11. **What T-052 means by a round trip** (§6): byte-faithful with the original
    envelope, or meaning-faithful and re-signed. And since an import's speaker is
    the importer, is an import a verification summary in SLSA's sense, to be
    specified with `slsa-vsa-1-2` (`BACKLOG`:190)?
12. **Repeated attribute types.** Whether one `has` may carry two attributes of
    one type (C-01) decides whether a dependency list has a structured form at
    all. `SPEC-0002` §8.5 and `SPEC-0003` §7.1 do not say.

## 10. Requirement ids: cited, and statements without one

**Cited: 40 distinct skeleton ids** (occurrences and the method are in §11). Each was emitted from the id table, never typed from memory, and its own text was read beside every claim that cites it. *notes* is the numbering note, which names `R-0006` only to tell it apart from mofn report R-0006, and R-0050 as the end of the skeleton's range. This table is pass 1's; pass 2 added 48 distinct ids the requirements lane appended (R-0051 to R-0170), in the table of keyword-less statements below, six cells of §1 and A-02, and none of them is in this table.

| id | locator | lines | cited in |
|---|---|---|---|
| R-0002 | §1 | L37-38 | §6 |
| R-0005 | §2 | L73-75 | A-01, C-06, §5, §9 |
| R-0006 | §2 | L77-79 | notes, C-06, §3.2 |
| R-0007 | §2 | L79-80 | §3.2 |
| R-0009 | §3 | L105 | X-01, K-01, §4 |
| R-0010 | §3 | L110 | D-03, §6, §7, §9 |
| R-0011 | §4.2 | L250 | C-07, §3.2, §9 |
| R-0012 | §4.3 | L272 | C-07, §3.2, §9 |
| R-0013 | §4.3 | L283-286 | D-02, X-03 |
| R-0014 | §4.3 | L293-295 | C-10 |
| R-0015 | §4.3 | L295 | C-10 |
| R-0016 | §4.3 | L297-298 | D-04 |
| R-0017 | §4.3 | L299-300 | D-04, D-02 |
| R-0018 | §4.3 | L302-303 | A-01, §3.2, §9 |
| R-0019 | §4.3 | L310-311 | §3.2 |
| R-0020 | §4.3 | L319-322 | C-02 |
| R-0022 | §4.3 | L331-333 | D-04, C-01, §7 |
| R-0024 | §4.3 | L336-337 | A-02 |
| R-0025 | §4.3 | L337-339 | A-02, C-02 |
| R-0026 | §4.3 | L339-340 | D-02 |
| R-0027 | §4.3 | L356-357 | D-02 |
| R-0029 | §4.3 | L381-383 | A-02 |
| R-0031 | §4.3 | L396 | A-02 |
| R-0032 | §4.4 | L407 | C-07, §3.2, §9 |
| R-0035 | §4.5 | L441 | C-07, §3.2, §9 |
| R-0036 | §4.5 | L453-455 | D-01 |
| R-0037 | §4.5 | L458 | D-05, X-03, §10 |
| R-0038 | §4.5 | L489 | D-01 |
| R-0039 | §4.5 | L496 | D-01, C-08, C-09, §6, §8 |
| R-0040 | §4.5 | L503-504 | D-01, C-07, K-03, §3.2, §9, §10 |
| R-0041 | §4.6 | L511 | C-05, §3.2, §9 |
| R-0042 | §4.6 | L522 | A-03, C-05, §10 |
| R-0043 | §4.7 | L540-541 | X-01, K-01, §4 |
| R-0044 | §4.7 | L543-544 | X-01, X-04, §10 |
| R-0045 | §4.7 | L547 | X-01, K-01 |
| R-0046 | §4.7 | L547-550 | X-01, K-01, §4, §6, §9 |
| R-0047 | §4.7 | L551-553 | K-04 |
| R-0048 | §7 | L579-583 | A-04 |
| R-0049 | §7 | L584-588 | A-04 |
| R-0050 | §7 | L589-591 | notes, A-04 |

**Not cited: 9** — R-0003, R-0004, R-0008, R-0021, R-0023, R-0028, R-0030, R-0033, R-0034. This file does not cite them. R-0001 is the recital and is not a requirement.

**Statements this file relies on that carry no BCP 14 keyword.** Pass 1 cited
these by line only, the requirements lane ruling on them concurrently. Pass 2
gave each the ids `requirements.yaml` now holds, and wired appended ids into five
empty cells of §1 (X-02, C-03, C-04, C-09, K-02) and into A-03; a statement whose
candidate the lane rejected has no id, and the row says so.

| lines | what | where here | ids |
|---|---|---|---|
| L17, L21-22 | the predicate type string, and what its URI resolves to | K-02, X-03 | R-0051, R-0170 |
| L42-43 | provenance as an attestation | C-08 | R-0053 |
| L53-57 | what `builder.id` identifies | K-03 | R-0054; L53 and L56-57 are C-0004 and C-0006, rejected |
| L65-68 | what `buildType` identifies | D-02 | R-0055; L66-68 are C-0008 and C-0009, rejected |
| L84-87 | dependencies as known | C-02 | R-0064; L85-87 is C-0016, rejected as an example |
| L96-97 | outputs as `subject` | C-05 | R-0068 |
| L103 | the parsing rules are in-toto's | X-01 | R-0069 |
| L106-109 | major and minor versions | K-02 | R-0070, R-0071, R-0072 |
| L116-117, L178-179 | the summaries are informative | C-04 | R-0073, R-0074 |
| L197 | JSON, always | C-09 | R-0158, inferred: the sentence sits in the informative protobuf block (C-0024) |
| L258-259 | accuracy and completeness implied by `builder.id` | X-03, C-10 | R-0077, R-0078 |
| L311-313 | internal parameters need no check | C-06 | R-0087 |
| L318-319 | unordered, best effort | C-03, C-10 | R-0089, R-0090; the order rule is R-0163, inferred |
| L391-394 | purpose, and best effort at L3 | C-02, C-10 | R-0097; L391-393 are C-0034 and C-0035, rejected |
| L415-416 | the builder, trusted to have run the build | K-03 | R-0101 |
| L449-451 | the level from `builder.id` | D-05 | R-0107, R-0108 |
| L460-465 | the items R-0037's SHOULD lists; R-0037's text is L458 alone | D-05, C-06, X-04 | R-0111, R-0112, R-0113, R-0114, R-0115 |
| L501-505 apart from R-0040's sentence (L503-504) | the design rationale | D-01, K-03 | none: C-0045, rejected as rationale |
| L519-521 | the opaque, case-sensitive default; R-0042 is L522 alone | A-03 | R-0123, R-0124 |
| L544-546 | what the prefix is for; no underscore in standard names; R-0044 is L543-544 | open question 1 | R-0129; L544-545 is C-0047, rejected as rationale |
| L555-560 | verification elsewhere | S-03 | none: a pointer, no candidate |
| L576-577 | meaning unchanged unless noted | A-04 | R-0132, R-0133 |
| L619-631 | fields gone or made implicit | A-04 | R-0151, R-0152, R-0153, R-0154, R-0155, R-0156, R-0157 |
| L637-638 | the v1.2 change | §6 | none: C-0061, rejected as change history |

## 11. Method: how each claim here was produced

- **Our documents** were read only with `git show 7c3c731:<path>` in
  `/Users/nfn/Projects/mofn`, whose HEAD was `7c3c731` at the start and the end
  of the pass. Each `DOC:n` was printed with its line numbers from the blob
  before it was written down.
- **The source** is `.cache/slsa-provenance-1-2.txt`, 704 lines, digest as in the
  header. Its input `.bin` matches `content.sha256`, its two includes match the
  digests `render-source.py` pins, and re-running the script reproduced the
  `.txt` byte for byte. `bin/bcp14-count` re-run in this pass: 53. The skeleton
  carries 63; the difference is the ten keywords that R-0001's recital lists,
  which the requirements lane reconciles.
- **Quotations of the source** are `<!-- q -->` markers only; the blockquotes
  were written by `bin/check-quotes --render --only` on this file. The source has
  no page break, aside bar or line-end hyphen (checked by pattern), so a rendered
  span is its lines with whitespace collapsed and nothing healed.
- **Claims that a thing is the only one** were checked by script: the one digest
  value (every hex run of 16 or more characters, L349 the only one in a digest);
  the underscore names (every quoted or backticked name with `_`: `_type` and the
  extension example); the REQUIRED statements (seven lines carry the word, one of
  them the recital, so six, four of them L1); the absent
  `v1.1` (no match for the pattern in the source); `inputArtifacts` (one line).
- **Requirement ids** were emitted from the skeleton's `requirements.yaml` as
  committed at `4c0bd27`, read under both of the library's YAML readers (50
  entries, id, text, lines, locator and verb equal under both), and each cited id
  was printed beside its text and read beside the claim citing it. Before
  reporting they were re-resolved against the working `requirements.yaml`, which
  the requirements lane was editing (§10).
- **Unmarked source text.** Every 8-word window of this file's prose, with
  rendered blockquotes and markers removed, was searched for in the source.

**Counts, measured on the final text of this file** (each says what it
examined; recount after any edit):

| check | examined | result |
|---|---|---|
| `bin/check-quotes --only`, this file | 35 source quotations | 0 mismatched |
| `bin/check-quotes`, whole record | every lane's files, still being written: 809, then 810 at the last run; 812 at pass 3, once the lanes' files had settled | 0 mismatched at each run |
| `bin/check-id-joins --surface` | this record | 0 duplicate-text groups, so no cited id can be wrong and still match its words |
| requirement ids cited | pass 1: 40 distinct, 119 occurrences outside §10's table; pass 2: 48 more distinct appended ids; outside §10 and the numbering note, 132 occurrences of 56 cited ids | 0 unresolved; every pair read; pass 2 resolved each added id by script against the 170 entries and read the pair |
| mofn references `DOC:n` | pass 1: 280, over 139 distinct ranges; pass 2: 285, over 143 | 0 outside their blob. Pass 2 had an independent agent re-read every range at `7c3c731`: 262 clean, 18 defective, all corrected here |
| 8-word prose windows against the source | 11345 exact; 12678 with case and punctuation removed | 0 found; a planted verbatim run was found, so the audit fires; re-run by pass 2 on the edited text, 0 found |
| 6-word runs of mofn's own wording, against the cited blobs (pass 2) | every paraphrase | 22, left unmarked (Things to hold, 1); pass 1's audit searched the SLSA source only |
| italic spans of two words or more, against the source | every one | 1 found, in A-04, and rewritten as a paraphrase |
| rows in §1 | 32 | 4 adopt, 5 adapt, 4 reject, 10 constrains, 4 conflicts, 5 silent |
| rows in §3.2 | 24 | 4 containers, 5 values, 7 partial, 8 with no structured home |

---

## 12. What this file decides

Nothing. It records evidence and maps it. No requirement is added, amended or
withdrawn; no DEC-* is opened, ranked or accepted; `ADR-0004` is not reopened;
P5.2 is not amended; DEC-005 stays open; T-052's version stays with its owner.
Where a row says *adopt* or *adapt*, or a passage says **Ours**, it says what this
source would contribute if a decision were taken, and the decision belongs to an
ADR (`ARCH-0001` §9, R-D-02) or to the task that owns it: T-051, T-052, T-053.

---
record: slsa-1-2
kind: verification
title: "slsa-1-2 — FX-1 pass 2 (verify) and pass 3 (cross-check)"
date: "2026-10-02"
by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# SLSA v1.2: verification report

Passes 2 and 3 of FX-1 (`docs/extraction.md`), run on 2026-10-02 by an agent that did not do the
extraction. Every check was made against the source, never against the record's own summary. The
scripts live in the session scratchpad (`verify/norm.py`, `reqcheck.py`, `kwcover.py`, `typing.py`,
`slsaloc2.py`, `normcheck.py`, `revcheck.py`).

**Sources used:**

- `.cache/slsa-1-2.html`: rendered zonepage, the hashed bytes;
- `.cache/slsa-1-2.md`: single-page Markdown;
- `.cache/lane-e/slsa-v1.2/*.md` plus `schema/`: per-page release-branch Markdown. Verified
  byte-identical to `git archive origin/releases/v1.2 spec` of `.cache/lane-e/slsa-repo` at
  `ae7fc76215004e8fae250c877eff8919bf048e3b`.

**Normalisation used for every verbatim comparison:**

- NFKC;
- smart quotes, dashes and ellipses folded;
- Markdown link, emphasis and code markers and HTML tags stripped;
- blockquote `>` and `//` comment prefixes stripped;
- whitespace collapsed;
- the same transform applied to both sides.

## Pass 2: verify

### 1. Hash and currency

- `shasum -a 256 .cache/slsa-1-2.html` = `d9e2a942…1d052` = `content.sha256`. ✔
- Currency was checked against https://slsa.dev/spec/, which reads "Status: Approved … This is
  Version 1.2" and lists v1.1 as the previous version. The repository branches run up to
  `releases/v1.2`, with no v1.3 or v2.0 branch. `releases/v1.2` HEAD is still `ae7fc762`
  (2026-04-14). Release PR #1516, "content: Release SLSA 1.2", was merged 2025-11-24, matching
  `date`. The working draft (https://slsa.dev/spec/draft/) adds the Build Environment and
  Dependency tracks, as `summary.md` says. **The record tracks the current edition.** ✔

### 2. Verbatim

- All 243 `requirements.yaml` texts are substrings of the source. After normalisation, 243/243
  matched the release-branch Markdown. The 23 first-pass misses were all normaliser artefacts
  (reference-style `[link]`, blockquote `>`, `//` comments), and none survived.
- R-0064 and R-0137 carry lead-in plus table rows. The source rows are contiguous under the
  lead-in.
- **Splice hunt.** Every text that joins list items (`" - "`) was checked against the source list
  indentation.
  - **Defect V-1, fixed:** `R-0175` ("Predicate … MAY contain: - Link …") had also absorbed
    "- Bundle: …" and "- Storage/Lookup: …". In `attestation-model.md` those two are top-level
    siblings of the attestation-model list (indent 0), not members of what a Predicate MAY contain
    (indent 8). This was a scope splice. The text was truncated after the Link item and a note was
    added. The keyword count is unchanged.
- `normative.md`: 925 prose units were checked. Every unit that does not match is editorial
  framing: the header, "Page description (front matter)", table-conversion notes, code-fence
  language tags (`javascript {`, `proto syntax`). After adding the included `schema/*.cue|proto`
  to the corpus, no source-text miss remains.

### 3. Locators

All 243 were checked mechanically, not sampled:

- 243/243 texts occur in the page file the locator names;
- every heading component in every locator exists in that page;
- every `[#anchor]` exists as `id="…"`;
- for anchored rows, the text sits inside that row. The only mismatches were the 4
  `#safe-expunging-process` items, which sit under a `#### Process` heading inside the row, and
  that is correct.

### 4. Completeness

- `bin/bcp14-count .cache/slsa-1-2.txt` gives 268, and per-page counts over the release Markdown
  also sum to 268 (MUST 108, SHOULD 89, MAY 40, MUST NOT 10, RECOMMENDED 7, REQUIRED 7,
  SHOULD NOT 5, OPTIONAL 2). The header's 268 = 268 holds.
- **Occurrence coverage.** Each of the 268 keyword occurrences in the source falls inside some
  requirement text: 0 uncovered.
- **Reverse walk** of the 16 normative pages against `normative.md`:
  - every sentence or table cell of every page is present;
  - the only absences are HTML comments (editors' TODO notes, a documented drop) and threat titles,
    which are reformatted `(Source L4)` → `— Source L4`, as documented;
  - `provenance.md` and `requirements.md` are navigation stubs. They are not listed as normative
    pages, and they carry no keywords.
- **List-member coverage:**
  - **Defect V-2, fixed:** `R-0171` ("Envelope … MUST contain:") lacked its required members,
    Message and Signature. Signature is keyword-free, and appending it would splice past R-0172.
    A `notes` field now names both members, with the source lines.
  - `R-0170` got the same treatment (members R-0171, R-0173, R-0175).

### 5. Typing

- `normativity` matches the strongest keyword in every entry: requirement 121, recommendation 88,
  permission 34. No MUST was typed as weaker. Every `verb` appears in its text.
- Track and level were spot-checked against the ✓ columns of the build and source requirement
  tables for all build-requirements and source-requirements rows. All agree:
  - provenance-exists L1+;
  - authentic L2+;
  - unforgeable and isolated L3;
  - Source org/SCS rows L1+/L2+/L3+/L4.
- **Defect V-3, fixed:** `R-0075` (Untrusted person row) was `testable: no`, "permission only".
  Its last clause, "They MAY NOT approve changes … or perform any privileged actions", is
  prohibitive in effect and checkable in SCS permissions. It is now `testable: partial`, with the
  reason stated. `normativity` is kept as permission because no BCP 14 prohibition keyword is used.

### 6. Object model

- All 80 objects have a locator into an existing page. A name-in-page check found 11 partial
  hits, all camelCase field names (`InternalParameters` and so on). Those were checked by hand
  and are supported.
- **Defect V-4, fixed:** `trusts_up_to.to` was a pseudo-type, `RootOfTrust(BuildPlatform|SCS,
  Level)`. It is now normalised to `RootOfTrust`.
- `same_party_as.to: Party` is a tmodel class with no SLSA object behind it. It is now labelled as
  such; the edge was already `kind: inferred`.
- **Defect V-5, fixed:** 28 objects had no edge. Twenty-five stated structural edges were added,
  each with a locator:
  - Envelope `wraps` Statement and `carries_signature` Signature;
  - Statement `has_subject` and `has_predicate`;
  - Predicate `contains_link`;
  - Bundle `bundles`;
  - Provenance `has_build_definition` and `has_run_details`;
  - BuildDefinition `has_internal_parameters`;
  - RunDetails `has_byproduct`;
  - VSA `reports_level_as` SlsaResult;
  - SourceVSA `asserts_org_property`;
  - Branch and Tag `is_a` NamedReference;
  - ChangeHistory `records_changes`;
  - Approval `approval_of`;
  - Administrator and PlatformAdmin `administers`;
  - Tenant `defines_steps`;
  - Build `comprises`;
  - SafeExpungingProcess `expunges_from`;
  - Monitor `verifies_and_publishes`;
  - AssessmentPrompt `prompt_of`;
  - Threat `has_mitigation`;
  - ExampleControl `instance_of` TechnicalControl (inferred).

  The total is 80 objects and 81 edges. The diagram in `object-model.md` does not yet draw the new
  edges, and the file says so.
- `tmodel_mapping` targets (ARCH-0001 §2b, §3b, §4, §5, R-032, R-036, R-037, DL-0009 R-040..R-044)
  exist in `ARCH-0001-PROPOSAL-v0.2.0.md` and DL-0009.

### 7. Claims in `summary.md` and `design-notes.md`

All of these were checked against the source:

- release date and PR;
- RC history ("No changes" since RC2);
- draft tracks;
- the "measure your efforts toward compliance with the SSDF" quote (`about.md`);
- "each SLSA level implies the levels below it" (`verification_summary.md`);
- "a person or organization may act as more than one role" (`terminology.md`);
- the cue and proto "informative … text is authoritative" notes;
- "Reviews SHOULD cover, at least, security relevant properties of the code";
- every R-range claim, including Build 124 / Source 87 / cross-track 32.

**Defect V-6, fixed.** `summary.md` (Limits) and `design-notes.md` (Q4) said Source L1–L2 VSAs
"MAY" be issued from the SCS's own understanding. R-0098 is internally overlapping at L2. In one
sentence it says "At Source Levels 1 and 2 the SCS MAY …" and "at Level 2+ the SCS MUST use the
SCS-issued source provenance". Both files now state the overlap and that the MUST governs.

## Pass 3: cross-check

- **Schema and examples:**
  - The 9 verbatim example/schema files were each found byte-identical, after dedent, to a fenced
    block of the release Markdown. All fenced blocks in the spec are held. The two `{% include %}`
    blocks are the cue and proto files, which are identical to `spec/v1.2/schema/*`.
  - The 13 schema-validated vectors in `examples/vectors.yaml` were re-run with jsonschema 4.19 and
    `referencing`. All 13 results reproduce, including the documented schema-valid-but-invalid case
    for R-0236.
  - **Defect V-7, fixed:** `source-vsa-v1.derived.schema.json` used `"$ref":
    "vsa-v1.derived.schema.json"`. That is a relative reference against a `urn:` base, which no
    registry can resolve, and validation raised `Unresolvable`. It is now `"$ref":
    "urn:library:slsa-1-2:vsa-v1.derived"`, the target's `$id`.
- **Requirements ↔ messages:**
  - Every back-ticked field named in a requirement text exists in `messages.yaml`, except values
    (`SLSA_SOURCE_LEVEL_n`, `main`, `release`) and `inputArtifacts`.
  - **Source defect recorded:** R-0223 requires the buildType to describe how to interpret
    `inputArtifacts`. That name is not a field of v0.2 or v1 provenance and appears nowhere else in
    the release branch; v0.2 uses `materials`. A note was added to `messages.yaml`
    provenance-v0.2-migration.
- **Protocol:**
  - Every `message:` in the 9 flows is defined in `messages.yaml`.
  - **Defect V-8, fixed:** the role `source repository releases` was used in distribute-provenance
    but never declared, so it was added.
  - Sub-roles such as `scs (control-plane)` are declared as one composite role. This is left as is.
- **State machines:**
  - Every transition endpoint is a declared state except two computed targets:
    `level(builder.id) from verifier roots of trust` and `lower level (inferred)`. Both are
    explicit about being computed or inferred, and are left as residual.
  - Triggers are named events in prose. SLSA defines no message-typed triggers.
- **`maps_to`:** SLSA publishes no crosswalk. No `maps_to` is claimed, and none is needed.
- **`not_applicable`:** empty. All artifact kinds are present.

## Counts after verification

| artifact | count |
|---|---|
| requirements | 243 entries; BCP 14 source 268 = extracted 268 (`bin/validate` recomputes) |
| object model | 80 objects, 81 edges (1 object + 3 edges inferred), 8 gaps |

## Residual open issues

1. The `object-model.md` Mermaid diagram does not draw the 25 edges added here.
2. Two computed pseudo-states in `state-machine.yaml` (see above).
3. Composite SCS sub-roles in `protocol.yaml` are not individually declared.
4. Human review (pass 4) is outstanding: `reviewed_by` is empty on every artifact.

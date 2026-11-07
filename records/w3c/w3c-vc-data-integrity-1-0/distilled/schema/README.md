---
record: w3c-vc-data-integrity-1-0
kind: schema
title: "w3c-vc-data-integrity-1-0 — schemas"
extracted: "2026-11-07"
reviewed_by: ""
---

# Verifiable Credential Data Integrity 1.0 — schemas

The W3C Recommendation (REC-vc-data-integrity-20250515, 15 May 2025) publishes
**no** formal syntax of its own: no CDDL, no JSON Schema, no ABNF, no ASN.1
(the search is below). What it prints as formal displays is a definition list
of the proof properties (§2.1), the proof purpose list (§2.2), two HTML tables
of pinned digests (§2.4), the `cryptosuiteString` datatype definition
(§2.4.4.1), the cryptosuite struct (§3), the `DataIntegrityProof` pattern
(§3.1), the inputs and result structs of the five algorithms (§4.2–§4.6) and
the error list (§4.7). They are copied, by script, into `inline.verbatim.txt`.
Everything else here is **derived**: this library's machine-checkable rendering
of the source's prose, named `*.derived.*`, with `DERIVED` in its first lines
and, for JSON Schemas, an `$id` of `urn:library:w3c-vc-data-integrity-1-0:<artifact>`.

**Multibase, Multihash and Multikey are not defined by this source.** The
revision history says Multikey moved to Controlled Identifiers v1.0 (CID). The
source's own text on Multibase is one clause in §2.1 and one in §2.3 (I-01,
I-03). The `z` (base58btc) and `u` (base64url) prefixes the lane brief names are
Multibase's: the source's examples use `z` only, and no example uses `u`. They
appear here as the anchors `#multibase-base58btc` and `#multibase-base64url`,
marked OUTSIDE-SOURCE.

Source: `.cache/w3c-vc-data-integrity-1-0.bin` (the REC HTML), sha256 `ba5c4baf13fe3bab3ebd95ab6650d6fe83720e254b383bb444b4fbbae7bcf4fe` (equal to
`content.sha256` in `record.yaml`); its plain-text rendering
`.cache/w3c-vc-data-integrity-1-0.txt`, sha256 `2b7725f80e138ef943eff25050eee6a62f8887762ca9e1e03867c55ea5647beb`, 1243 lines, is what line numbers here
count in and what quotations are checked against. Example instances were
decoded from the HTML elements, never from the rendering.

## Files

| file | kind | built from | covers | does NOT cover |
|---|---|---|---|---|
| `inline.verbatim.txt` | **verbatim** | §2.1, §2.2, §2.3, §2.4, §2.4.4.1, §3, §3.1, §4.2–§4.7 | 14 regions, table below | prose (`normative.md`); the 14 examples (examples lane) |
| `proof.derived.schema.json` | **derived**, JSON Schema 2020-12, `$id` `urn:library:w3c-vc-data-integrity-1-0:proof.derived` | §2.1, §3.1, §4.2, §4.4 | one proof object. Root = §2.1 MUST; `#data-integrity-proof`, `#processable`, `#lenient-time`, `#url-strict`, `#multibase-base58btc`, `#multibase-base64url`, `#proof-should` | what a cryptosuite puts in `proofValue`; JSON-LD term mapping of `type` and `proofPurpose`; calendar validity of a date |
| `secured-document.derived.schema.json` | **derived**, `$id` `…:secured-document.derived` | §2.1, §2.1.1, §2.1.2, §2.4.2, §4 | a document with a `proof`: root, `#single-proof`, `#proof-set-or-chain`, `#proof-chain-shape`, `#processable`, `#context-should` | referential rules of a chain (cross-field X-01…X-04) |
| `resource-integrity.derived.schema.json` | **derived**, `$id` `…:resource-integrity.derived` | §2.3 | an object with `id` and `digestMultibase` | the Multihash inside the value (decoded for Example 8 only) |
| `verification-method.derived.schema.json` | **derived**, `$id` `…:verification-method.derived` | §2.1, §2.6, Appendix B | what the source says of a verification method; `#multikey-cid`, `#jsonwebkey-cid` are OUTSIDE-SOURCE | any verification-method type, which belongs to CID |
| `problem-details.derived.schema.json` | **derived**, `$id` `…:problem-details.derived` | §2.4.3, §4.4, §4.7 | ProblemDetails type URL; `#with-referenced-names`, `#problem-details-should` | RFC 9457 members the source does not mention |
| `verification-result.derived.schema.json` | **derived**, `$id` `…:verification-result.derived` | §3, §4.4, §4.5, §4.6 | the four result structs; `#cryptosuite-result`, `#error-raised`, `#combined-as-written`, `#context-validation-result`, `#context-validation-failed` | the algorithms (protocol lane) |
| `proof-options.derived.schema.json` | **derived**, `$id` `…:proof-options.derived` | §4.2, §4.3 | the three options the source names | the rest of a cryptosuite's options |
| `rules.derived.yaml` | **derived**, YAML | all of the above | the rule index (every rule id the schemas cite, with level and requirement ids), the four cross-field rules, the six pinned digests with their source lines | — |
| `schema-tests.derived.json` | **derived**, JSON | the checks below | 298 cases, accept and reject instances, example instances by fixture | — |
| `check-schemas.derived.py` | **derived**, Python | the checks below | the runner: metaschema check, cases, the four cross-field rules | — |

## No grammar of its own — the search

`grammar_search` (scratch, `python3 -I`) read the whole HTML with `<script>` and
`<style>` removed, the rendering (1243 lines) and the 14 `<pre>` blocks, for
CDDL, ABNF, `::=` or ` := `, ASN.1 / `DEFINITIONS`, the phrase JSON Schema,
`$schema`, `"$id"`, `$defs`, `.regexp`, a CDDL-like rule shape, `=>`, `%x..` and
`n*m`. Counts as rendering / `<pre>` / HTML: CDDL 0/0/0; ABNF 0/0/0;
`::=` 0/0/0; ASN.1 0/0/0; `$schema`, `"$id"`, `$defs`, `.regexp`,
`=>`, `%x`, `n*m` and the rule shape all 0/0/0. Only the phrase JSON Schema
occurs (2 times, §2 and §4.1), and in both places the source tells an
application to use JSON Schema or an equivalent to check the document it receives;
it publishes none. HTML census outside `<script>`/`<style>`: 16 `<dl>`, 2 `<table>`, 14 `<pre>`, 22 `<ol>`, 46 `<ul>`, 2 `<figure>`.

## Inline regions (`inline.verbatim.txt`)

Each region is the rendering's lines between its `BEGIN`/`END` markers, byte for
byte (script-copied from the .txt by line number); the sha256 is over the
lines joined by a line feed with no trailing line feed. A table row begins with
`| ` in the rendering and nowhere in the HTML.

| id | section | display | .txt lines | sha256 |
|---|---|---|---|---|
| I-01 | §2.1 | the proof property definitions: id, type, proofPurpose, verificationMethod, cryptosuite, created, expires, domain, challenge, proofValue, previousProof, nonce (a definition list; includes the opening MUST of the section) | 204–227 | `6a46f289cda40497…` |
| I-02 | §2.2 | the commonly used proof purpose values (a definition list) | 374–383 | `3d635d7204e3b790…` |
| I-03 | §2.3 | the digestMultibase property: its scope and its value, a Multibase-encoded Multihash (one paragraph) | 388–388 | `966cb6afe5a7d4fe…` |
| I-04 | §2.4 | the pinned JSON-LD context URLs and their SHA2-256 digests (an HTML table) and the curl command line that confirms them | 407–414 | `41dac0c9b37042d7…` |
| I-05 | §2.4 | the security vocabulary media types and their SHA2-256 digests (an HTML table) | 420–426 | `7ae9f7f8c14e507e…` |
| I-06 | §2.4.4.1 | the cryptosuiteString datatype definition (a definition list) | 463–472 | `606df13ef7b6721d…` |
| I-07 | §3 | the cryptosuite instance struct: createProof, verifyProof and the cryptosuite verification result (a definition list) | 498–507 | `7818e44caa7922aa…` |
| I-08 | §3.1 | the DataIntegrityProof pattern: type, cryptosuite, proofValue (a definition list) | 518–523 | `29e68d906529a390…` |
| I-09 | §4.2 | Add Proof: required inputs and output (one paragraph) | 549–549 | `9e2b2ac270ec6b3e…` |
| I-10 | §4.3 | Add Proof Set/Chain: required inputs and output (one paragraph) | 560–560 | `575895a36e1e084d…` |
| I-11 | §4.4 | Verify Proof: the inputs and the verification result struct (definition lists) | 576–598 | `4600d6d53ca1211a…` |
| I-12 | §4.5 | Verify Proof Sets and Chains: the combined verification result initialisation and combination steps (list items) | 630–635 | `87cbafc48be3fff8…` |
| I-13 | §4.6 | Context Validation: inputs and the context validation result struct | 639–648 | `6d967f1a9fb0b690…` |
| I-14 | §4.7 | Processing Errors: the ProblemDetails rules and the five defined error codes | 662–675 | `a794f1c96003c4f0…` |

Not copied, and why: the two figures (§1.1, images with no text), the table of
contents, the terminology definitions (§1.4, prose; `normative.md`), and the
reference lists (Appendix D).

## Requirement levels, and what binds what

A SHOULD is not a MUST, so the two never share a rule. The roots and every
anchor not ending in `-should` hold MUST and MUST NOT statements only; a
failure there is non-conformance. Anchors ending in `-should` add SHOULD
statements and include the root by reference; a failure there is a warning. A
MAY is never a constraint: the leniency it grants has an anchor named for it
(`#lenient-time`). OUTSIDE-SOURCE anchors bind nothing in this source.
`rules.derived.yaml` gives every rule's level and the requirement ids behind it.

52 of the 78 requirement ids are cited by the files here (counted by
script over this directory, `w3c-vc-data-integrity-1-0#R-NNNN` occurrences). The
26 not cited, by group: conformance, R-0001; context validation and
network loading, behaviour and no shape, R-0029, R-0030, R-0031, R-0027, R-0028;
what a cryptosuite specification must contain, authoring rules with no wire
structure, R-0037 to R-0044, R-0046 to R-0050; the input document may carry a proof
and implementers may add safeguards, R-0055, R-0056; the algorithms' UTF-8 and
error-propagation rules and the optional extra return values, R-0057, R-0058,
R-0062, R-0071, R-0074. The set is asserted equal to the uncited list by the
script that wrote this file. messages.yaml wires 67 ids to a message or field and lists the other 11 with reasons.

## Source tensions (full text and quotations in `messages.yaml`, `source_tensions`)

- **T-01** `verificationMethod` is OPTIONAL in §2.1 and an error to omit in §4.2 and §4.4. Root accepts a proof without it; `#processable` does not.
- **T-02** `proofValue` is MUST in §3.1 and replaceable in §2.1. Optional in the root; required in `#data-integrity-proof`.
- **T-03** a verification method's `revocation` (§2.6) or `revoked` (Appendix B). Both accepted.
- **T-04** `PARSING_ERROR` and `DATA_LOSS_DETECTION_ERROR` are used and not defined in §4.7, whose MUST on the type URL read literally excludes them. Root = five codes; `#with-referenced-names` adds the two.
- **T-05** §4.5 names the combined result's members `status` and `document`, then sets `verified`. `#combined-as-written`.
- **T-06** §4.6 removes a `document` property where the struct has `validatedDocument`, null on failure.
- **T-07** §4.5 runs steps 4–8 of §4.4, which use inputs §4.5 does not take.
- **T-08** `domain` is a set, `previousProof` a list.
- **T-09** typographical errors (`chose`, `an list`, `specifing`, `an map`), left as printed.

## Checks

All run by `check-schemas.derived.py` (`python3 -I`, `jsonschema` 4.26.0, `referencing`).

- **Metaschema**: 7 schemas examined, 0 invalid against JSON Schema 2020-12.
- **Cases**: 298 examined, 298 cases giving 322 verdicts (an example case with several proofs gives one verdict per proof), 0 differing from the expectation. 129 jsonschema accept, 139 jsonschema reject, 17 cross-field accept, 13 cross-field reject; 76 of the cases use an example.
- **Instances each schema must REJECT** (the hazard of a schema that parses and binds nothing): every property of `proof.derived` has at least one rejecting instance (wrong type, absent, malformed time, duplicate set member); `type: DataIntegrityProof` without `cryptosuite`; a `challenge`-less proof with a `domain` under `#proof-should`; a relative `id`; a ProblemDetails with a `#`-less, `http`, lower-case, prefixed or suffixed type URL; a verified-false result that carries a document or media type; a chain with a dangling `previousProof`.
- **Mutation test** (the cases must be able to fail): five mutations of `proof.derived` were run against the unchanged cases, in a scratch copy: dropping the `then` of the cryptosuite rule (1 case failed), loosening `created` to any string (6), loosening `domain` (4), making `proofPurpose` optional (3), and removing the `required: [type]` guard from the `if` of the cryptosuite rule (0 failed). The fifth is equivalent, not a gap: the root already requires `type`, so the guard cannot change a verdict; it is kept so the rule stays correct if `type` is ever made optional.
- **Limitation cases**: 1 (`P-lim-created-feb30`): the lexical pattern accepts a day the calendar lacks; the case records that it does.
- **Cross-check of ids**: `bin/check-id-joins --quote-join` examined 37 quotation/citation pairs, 37 carried by their cited id, 0 to read; `--surface` lists two duplicate-text groups (R-0010/R-0013, R-0057/R-0062) and every citation of those ids was read.

## Foreign documents used

Controlled Identifiers v1.0, fetched 2026-11-07 from `https://www.w3.org/TR/cid-1.0/`, sha256 `c5e9befba602b53de46669cf98067123d1901357a425f8bff621796b2ac4ac4a`, to confirm the members of Multikey (`publicKeyMultibase`) and JsonWebKey (`publicKeyJwk`) and the name `revoked`. Nothing of this record was in the corpus those searches ran over. Quotations of CID are not made here.

## Not done

No cryptosuite document (vc-di-eddsa, vc-di-ecdsa) was read; the signature recipes in `../examples/signatures.derived.json` are from memory of those documents and are not validated against their test vectors.

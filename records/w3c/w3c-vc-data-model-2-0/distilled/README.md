---
record: w3c-vc-data-model-2-0
kind: index
title: "w3c-vc-data-model-2-0 — distilled artifacts"
extracted: "2026-11-07"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not. Source: the W3C Recommendation HTML (`content.sha256`
`a9196a3d…4156f8`); line numbers count in its rendering `.cache/w3c-vc-data-model-2-0.txt`
(5009 lines, sha256 `73d91cc0…d3da548`). Counts below were recomputed by script in
pass 2 (verify), 2026-11-07.

| kind | file | coverage |
|---|---|---|
| normative | normative.md | every stated entry of requirements.yaml except the split parents as a quotation marker in source order (250), with 64 definition, scope and recital blocks; the 8 inferred entries named in place; source defects and tensions SD-1 to SD-26 (54 quotations); 368 markers in all. Not covered: notes, examples and sections marked non-normative, except as accounted for |
| requirements | requirements.yaml | all 165 BCP 14 keywords of the source placed by line; 298 entries: 127 from the skeleton (81 unsplit, 40 split parents, 6 withdrawn: the §11.1 and §11.2 sentences, non-normative by nesting), 83 split children, 37 hunted keyword-less statements, 43 promoted candidates, 8 inferred. All 384 candidates have a verdict (39 stated, 345 rejected). Pass 2 cut two parent texts (R-0012, R-0015) that opened inside a note and an example |
| schema | schema/ | the source prints no grammar (searched): 12 formal displays copied verbatim (inline.verbatim.txt, each region byte-equal to its lines, digests in schema/README.md); 4 JSON-LD files the source pins by URL, verbatim and separately hashed (contexts.yaml); 2 derived JSON Schemas (52 anchors), 21 cross-field rules, 190 test cases (0 unexpected), 21 mutations (0 surviving). Not covered: the members of a proof, the contents of status, schema, refresh, terms-of-use and evidence types, JSON-LD processing |
| messages | messages.yaml | 25 structures (17 structures, 2 concepts, 2 registrations, 2 datatypes, 1 document, 1 table) and 93 fields; 267 citations of 183 requirement ids on 100 of the 118 nodes, re-emitted by selector in pass 2; the 18 empty nodes are listed in its note. Not covered: what the securing specifications define (proof members, JOSE and COSE headers) |
| protocol | protocol.yaml, protocol.md | 13 roles, 19 flows (109 steps, 13 inferred), one Mermaid diagram per flow, 20 error paths, source defects and tensions T-01 to T-31; 400 quotations; the source defines local algorithms and no wire exchange, so deliveries between parties are marked inferred |
| state-machine | state-machine.yaml | 9 machines, 73 states, 87 transitions: the §7.1 verification algorithm, the verifier's receive lifecycle, the validity period, a status entry, refresh, validation, media type precision, the related-resource check and presentation freshness; 106 quotations |
| examples | examples/ | all 40 examples as 175 verbatim fixtures taken from the HTML elements (reproduce.py: 175 examined, 0 different); 40 vectors with 116 citations of 81 requirement ids; 831 checks (550 pass, 21 fail, 12 deviation, 55 unverifiable, 193 na; results.derived.json, recomputed by schema/run_checks.derived.py); findings D-01 to D-09. Not covered: no signature can be verified, the source prints no key |
| design-notes | design-notes.md | adopt, adapt and reject against ARCH-0001, ARCH-0002, ADR-0003 to ADR-0005, SPEC-0001 to SPEC-0004, MD-3 and DEC-002 at m-of-n a56a3c0 (52 mapping rows: 13 adopt, 6 adapt, 16 constrains, 11 silent, 6 reject; 53 m-of-n quotations checked by qm.py, 80 source quotations); MD-3 clause by clause and where the source cuts against option 5; the R-I-06 export of an AuthzCert; 11 open questions; source defects D1 to D14. Decides nothing |

## Defect crosswalk

Five files record the source's defects, each in its own scheme, and the same
defect often appears under several ids. Cite with the prefix: **P:T-nn**
(protocol.yaml `source_defects_and_tensions`, which state-machine.yaml cites),
**N:SD-n** (normative.md), **S:F-nn** and **S:T-nn** (schema/README.md, which
messages.yaml cites), **DN:Dn** (design-notes.md section 9) and **X:D-nn**
(examples/vectors.yaml). The schemes collide: P:T-03 (a gap in §7.1) is not
S:T-03 (the name and description arrays), and X:D-01 (Example 25's digests) is
not DN:D1.

| source defect or tension | P | N | S | DN | X |
|---|---|---|---|---|---|
| §5.13 and §7.1 name the verification result's members differently | T-01, T-02 | SD-4 | T-05 | D1 | |
| §7.1 has no branch for no matching mechanism or unparseable input; PARSING_ERROR and RANGE_ERROR are produced by nothing | T-03, T-04 | SD-5 | | D2 | |
| §7.1 steps 3 and 4, the only statement of when each error is produced, carry no keyword | | | F-09 | | |
| status checking: inside verification by definition, absent from the algorithm | T-07 | SD-7 | | D3 | |
| §1.3 points verifiers at §4.12 for verification | T-06 | SD-8 | | | |
| a conforming document must be secured; the document verification returns is not | | SD-6 | | | |
| a time value without an offset: dateTimeStamp requires one, §5.8 reads it as UTC; the context coerces to dateTime | | SD-9 | F-03 | D5, D8 | |
| §4.6's MUST points at §11.1, a non-normative section, for the language value object | T-11 | SD-1 | T-04 | D6 | |
| §6's arity sentence against single-valued name, description and holder; Example 6 uses arrays | | SD-10 | T-03, T-03b | | D-07 |
| subsections of informative sections without a class of their own (§11.1, §11.2 and others) | T-11 | SD-1 | T-04 | | |
| §4.2 lists `status`; the property is `credentialStatus` | T-13 | SD-2 | F-01 | | |
| B.2 places RefreshService types in `credentialRefresh`; the property is `refreshService` | T-14 | SD-3 | F-02 | D7 | |
| a refresh service in a presentation has no term in the base context | T-12 | SD-14 | | | |
| sha384 is the floor, yet the document pins SHA2-256 digests | T-25 | SD-22 | | D9 | |
| which of several digests must match is not said | T-31 | SD-17 | | | |
| digestSRI: one or more hash-expressions (§5.3) against the whole integrity grammar (B.3.1) | | SD-13 | | | |
| sriString's canonical mapping runs the wrong way | | SD-12 | | | |
| Example 25's digestSRI values carry one base64 character too many | | | F-04 | | D-01 |
| B.2's security vocabulary digest matches no served file, and VC Data Integrity pins the same URL to another | | SD-26 | F-05 | D10 (related) | |
| a MUST and a MAY on the same vocabulary files (B.2) | | | | D10 | |
| self-asserted defined by entity and by value; under the value test R-0054 can never fail | | SD-20 | | | |
| CRYPTOGRAPHIC_SECURITY_ERROR means a modification; step 1.3 raises it for any failure | | SD-21 | | | |
| issuer's object needs a URL id, holder's object only an id | | SD-23 | | | |
| type values: terms and absolute URL strings | | SD-24 | | | |
| the media types are part of conformance; their registrations are non-normative | | SD-25 | | D11 | |
| §5.11 introduces MUST rules as advice | | SD-11 | | | |
| §6.2's SHOULD points at conventions only its non-normative subsection outlines | | SD-18 | | | |
| §2 says the specification requires validation before reliance; nothing normative does | | SD-19 | | | |
| typographical and editorial errors (validUtil, a repeated clause, a missing verb, garbled sentences) | T-15 to T-19, T-26 | SD-15, SD-16 | | D13 | |
| the note under Enveloped Verifiable Credentials names a presentation where the id carries a credential | T-20 | | | | |
| a superseded reference (CBOR as RFC 7049) | | | | D14 | |
| opposite advice on `@json` (§6.1 against B.4) | | | | D12 | |
| examples that are not JSON: ellipses and comments, doubled braces, unquoted names, a template, a missing tilde | | | | | D-02 to D-06 |

Protocol gaps and tensions with no counterpart elsewhere: P:T-08 to T-10 (what
verifying a presentation verifies, the controller never compared with the issuer,
the document kept on the cryptographic failure branch), P:T-21 and T-22 (challenge
and presentation validity named but not modelled), P:T-23, T-24 and T-27 to T-30
(trust, validity evaluation, refresh, requests, status lifecycle, ignorable optional
properties).

## Against the sibling record w3c-vc-data-integrity-1-0

Measured in pass 2; that record was not edited.

- **Agree.** The base context's digest: both records pin `59955ced…92734` and
  both measured the fetched file equal. The Data Integrity terms in the base
  context: `DataIntegrityProof` carries a protected scoped context defining the
  twelve proof properties, and `proof` is a graph container in the
  VerifiableCredential and VerifiablePresentation scopes (schema/contexts.yaml).
  The two files each record measured for the security vocabulary
  (`02c4b488…`, 48622 octets; `8a16b6b5…`, 35407 octets) are the files pass 2
  fetched here.
- **Mirror.** Verification result names: VC Data Integrity's cryptosuite and
  verify-proof results use `verified` and `verifiedDocument` as §5.13 here does,
  and its combined result uses `status`, `document` and `mediaType` as §7.1 here
  does; each record carries the split as a defect of its own source (here
  P:T-01, N:SD-4, S:T-05).
- **Disagree.** (1) The security vocabulary: B.2 here pins its JSON-LD
  serialization to `689af6f3…`, VC Data Integrity §2.4 to `082434d5…`, the same
  URL on the same publication date (N:SD-26). (2) A failed verification: VC
  Data Integrity returns `verifiedDocument` null when `verified` is false and its
  cryptosuite result carries no `mediaType`; §5.13 here types `verifiedDocument`
  as a map and requires `mediaType`, so
  `schema/verification-result.derived.schema.json#SecuringVerificationResult`
  rejects both shapes. Neither source says which governs a mechanism that
  implements both.

## Pass 2 (verify), 2026-11-07

Falsified and fixed:

- messages.yaml was wired against the skeleton: 44 of 112 citations named a split
  parent (two of them the parent of a neighbouring statement: the termsOfUse and
  credentialSchema fields), 6 a withdrawn §11 entry, 3 a requirement about
  something else (R-0102, R-0126, and R-0098 on `verified`), and 23 nodes had
  none, 11 of them with a keyword in their own quote. Re-emitted by selector: 267 citations, no parent, no
  withdrawn id. examples/vectors.yaml likewise (46 citations: 17 parents, 7
  withdrawn, 5 vectors empty) to 116.
- The Appendix C templates had lost three rows (Contact in C.1; Encoding
  considerations and Contact in C.2); added.
- protocol.yaml T-11 said §1.3 carries no class; its tag is
  `section id="conformance" class="normative"`. 30 quote labels in protocol.yaml
  and state-machine.yaml called "unmarked subsection" were relabelled from the
  markup (19 normative in §1.3, 11 non-normative by nesting), four protocol.md step
  headers with them, and F01 step 4 stopped citing the withdrawn R-0118 to R-0121.
  All files now read §11.1 and §11.2 as non-normative.
- requirements.yaml: R-0015's text opened with six lines of Example 4's SD-JWT
  disclosure display and R-0012's with a note's sentence; both cut to their own
  lines. R-0054's testable_reason now records that its condition cannot be shown
  by the value test.
- schema/: 15 `$comment` quotations carried a level the grading does not give
  (MUST on keyword-less sentences, REC levels on withdrawn §11 sentences); three
  cross-field rule levels likewise. run_checks.derived.py reported X-05 as a pass
  for a presentation with no holder, a check that could not fail; it reports na
  now, and the tally moved from 551 pass and 192 na to 550 and 193.
  contexts.yaml counted 74 context terms where 72 exist. Two quotations in
  schema/README.md had their first letter lowered, and one cross-field rule
  carried a paraphrase in quotation marks; reworded.
- The security vocabulary digest (B.2), which pass 1 carried unchecked, matches
  nothing fetchable (N:SD-26).

Checks run, each with what it examined: bin/check-quotes 2017 quotations, 0
mismatched; bin/check-locators 290 locators, 0 misfiled, 8 unresolvable (the 8
inferred entries, whose text is not verbatim); bin/check-id-joins --surface 3
duplicate-text groups of texts of 40 characters or more (requirements.yaml's
note lists all 5), --resolve 1084 qualified citations before the re-wire and 1309 after, 0 dangling,
--quote-join 0 pairs examined (it collects record-qualified quotations, and
quotations here are markers, so the selector scripts above and the design-notes
table join, 66 citations, 0 problems, did the joining); bin/bcp14-count 165;
bin/validate 0 errors, and its FX-1 check run on this record as if it declared
profile full, 0 errors; both YAML readers over the 8 YAML files of distilled/, equal after boolean
spelling (record.yaml, not this pass's, differs by a trailing newline); examples/reproduce.py 175 fixtures, 0 different; run_checks
schema-tests 190, metaschema 52 anchors, examples --check 831 checks, all 0
different; mutation_test 21, 0 surviving; 70 hand-written instances the derived
schema must reject or accept, 69 as expected and 1 (an enveloped credential with
a foreign context) a limit X-15 already states; qm.py 53 m-of-n quotations, 0
mismatched.

Open for pass 3: the schema rejects a credentialSubject object holding only `id`,
which goes beyond the inferred R-0175 (empty object only); the derived schemas
and cross-field rules cite lines, not requirement ids, so the field-to-requirement
join is by line; the four JSON-LD files are the first such files committed to the
library, and whether CLAUDE.md's rule on third-party documents admits them is the
lead's call.

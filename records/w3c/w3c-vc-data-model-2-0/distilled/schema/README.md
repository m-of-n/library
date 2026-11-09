---
record: w3c-vc-data-model-2-0
kind: schema
title: "w3c-vc-data-model-2-0 — schemas"
extracted: "2026-11-07"
reviewed_by: ""
---

# Verifiable Credentials Data Model v2.0 — schemas

The W3C Recommendation (REC-vc-data-model-2.0-20250515, 15 May 2025) publishes **no**
formal syntax of its own: no CDDL, no JSON Schema, no ABNF, no ASN.1 (the search is below).
What it prints as formal displays is a set of tables, one regular expression (Example 32,
the XML Schema 1.1 `dateTimeStamp`), the result maps of two verification algorithms, the
`ProblemDetails` definition and two IANA media type templates. Those are copied unchanged into
`inline.verbatim.txt` by script. Everything else here is **derived**: this library's
machine-checkable rendering of the source's prose, named `*.derived.*`, with `DERIVED` in its
first 12 lines and, for JSON Schemas, an `$id` of `urn:library:w3c-vc-data-model-2-0:<artifact>`.
Four further files are **not** the REC: the JSON-LD contexts and vocabulary the REC points at by
URL, fetched 2026-11-07 and copied byte-exact (`*.verbatim.jsonld`), each its own source with its
own digest (`contexts.yaml`).

Source: `.cache/w3c-vc-data-model-2-0.bin` (the REC HTML), sha256
`a9196a3d0b6601356c4e127bad24f8c7f2c17f6ed22e41b35755a910104156f8` (equal to `content.sha256`
in `record.yaml`); its plain-text rendering `.cache/w3c-vc-data-model-2-0.txt`, sha256
`73d91cc0b6a7d582512eb06d45a5fcfa8c696ab094b3db44f7a1495e9d3da548`, 5009 lines, is what line
numbers here count in (`L123`) and what quotations are checked against. Example bytes come from
the HTML elements, never from the rendering (see `../examples/README.md`).

## Files

| file | kind | built from | covers | does NOT cover |
|---|---|---|---|---|
| `inline.verbatim.txt` | **verbatim** | §4.5, §5.3, §5.8, §5.10, §5.13, §7.1, §7.2, §B.2, §B.3.1, §C.1, §C.2 | 12 regions, table below, copied by script from the rendering | the prose (`normative.md`); the examples (`../examples/`) |
| `vcdm.derived.schema.json` | **derived**, JSON Schema 2020-12, `$id` `urn:library:w3c-vc-data-model-2-0:vcdm.derived` | §1.3, §4.2-§4.13, §5.3, §5.10, §6, §11 | 46 anchors: `#VerifiableCredential`, `#VerifiablePresentation`, `#EnvelopedVerifiableCredential`, `#EnvelopedVerifiablePresentation`, and the members `#issuer`, `#credentialSubject`, `#credentialStatus`, `#credentialSchema`, `#refreshService`, `#termsOfUse`, `#evidence`, `#relatedResource` (`#sriString`, `#digestMultibase`), `#dateTimeStamp`, `#context`, `#typeValue`, `#textValue`, `#languageValueObject`, `#reservedProperty`, `#proof`; MUST at the bare anchor, SHOULD at the `-should` anchor | the members of a proof (Data Integrity lane); the content of status, schema, refresh, terms-of-use and evidence types; JSON-LD processing; the secured envelopes (VC-JOSE-COSE lane) |
| `verification-result.derived.schema.json` | **derived**, `$id` `…:verification-result.derived` | §5.13, §7.1, §7.2 | 6 anchors: `#ProblemDetails`, `#ProblemDetails-should`, `#SecuringVerificationResult`, `#VerificationResult` | what a securing mechanism does inside `verifyProof` |
| `cross-field-rules.derived.yaml` | **derived**, YAML | §1.3, §4.3-§4.13, §5.2, §5.3, §5.8, §5.10, §5.13, §6, §7.1, §11.2, §B.1 | 21 rules X-01 to X-21: what JSON Schema cannot state, each with the quoted sentence, and where it is enforced or why it is not | nothing silently: a rule not enforced says `none:` and why |
| `schema-tests.derived.json` | **derived**, JSON | the checks below | 190 cases (66 accept, 124 reject): one valid baseline with exactly one rule broken, per rule | — |
| `run_checks.derived.py` | **derived**, Python | — | `schema-tests`, `metaschema`, `examples`, `examples --check`; needs `jsonschema` (with `referencing`) and `cbor2` | — |
| `mutation_test.derived.py` | **derived**, Python | — | weakens one constraint at a time and requires the test cases to notice | — |
| `contexts.yaml` | derived metadata, YAML | §4.3, §5.2, §6.3, §B.1, §B.2 | url, size, sha256, pinning sections, printed digest and whether it matches, and the term diff, for the four context files | — |
| `context-credentials-v2.verbatim.jsonld` | **verbatim** (not the REC) | <https://www.w3.org/ns/credentials/v2> | the base context, 10131 bytes | — |
| `context-credentials-examples-v2.verbatim.jsonld` | **verbatim** (not the REC) | <https://www.w3.org/ns/credentials/examples/v2> | the examples context, 84 bytes | — |
| `context-undefined-terms-v2.verbatim.jsonld` | **verbatim** (not the REC) | <https://www.w3.org/ns/credentials/undefined-terms/v2> | the undefined-terms context, 90 bytes | — |
| `vocab-2018-credentials.verbatim.jsonld` | **verbatim** (not the REC) | <https://www.w3.org/2018/credentials/index.jsonld> | the credentials vocabulary, 21677 bytes | — |

The four `.jsonld` files carry no header inside, so they stay byte-identical to the served
bytes; their digests are in `contexts.yaml` and were re-computed from the files in this
directory.

## No grammar of its own — the search

A scratch script (`python3 -I`) read the whole HTML with `<script>` and `<style>` removed
(11296 lines), the rendering (5009 lines, 5010 by `split("\n")`) and the 112 `<pre>` fixtures for: the word CDDL
in any case; ABNF; `::=` or ` := `; ASN.1 or `DEFINITIONS IMPLICIT|EXPLICIT`; the phrase JSON
Schema; `"$schema"`, `"$id"`, `$defs`; the JSON Schema keywords `properties`,
`additionalProperties`, `required` as members; `.regexp`; and two rule shapes (`name = {`, `=>`,
`%x..`, `n*m`). CDDL, `::=`, ASN.1, the schema keywords, `.regexp` and the rule shapes found **0** in
the rendering, **0** in the `<pre>` blocks and **0** in the HTML. ABNF occurs 3 times, each time as a
**reference** to the ABNF of another document (the Subresource Integrity `hash-expression` and
`integrity` grammar: §5.3 L2887, §B.3.1 L4146 and L4150): not reproduced, so none is carried verbatim. The phrase
JSON Schema occurs 9 times in the rendering (13 in the HTML) as the name of the validation
mechanism for `credentialSchema` (and in the revision history and a reference), never as a
schema this source publishes; the two `credentialSchema` entries of Example 14 name
`"type": "JsonSchema"` files that are not given. The one regular expression is Example 32.

## Derivation rules the schemas follow

* MUST and MUST NOT are in the bare anchor. SHOULD, SHOULD NOT and RECOMMENDED are in the
  `-should` anchor, which includes the MUST level by reference. A failure at the SHOULD level is a
  deviation to warn about, never non-conformance.
* A rule the source does not state outright but the schema needs is marked `INFERRED` in the
  anchor's `$comment` and is repeated as a finding below when it is not obvious.
* Every `$comment` quotation (between « and ») was copied from the rendering by the script that
  wrote the file and carries its line number.
* Unknown members are allowed everywhere: the data model is open (§5.2 extensibility).
* Each `$comment` quotation carries the level the sentence has after requirements.yaml's grading, not only the word it prints: `NORMATIVE, NO KEYWORD` for a binding sentence with no BCP 14 keyword (R-0172, R-0183, R-0227, R-0228, R-0257, R-0262, and B.3.1's lexical space), enforced at the bare anchor like a MUST; `ADVICE` or `NON-NORMATIVE` for a §11.1 or §11.2 sentence (withdrawn R-0118 to R-0121); `(as printed)` where §11.1's own keyword is shown applied through R-0165. Pass 2 (verify) relabelled 15 quotations that pass 1 had marked MUST, MAY or SHOULD on these grounds; the constraints did not change, and REQUIRED and OPTIONAL quotations are still labelled MUST and MAY, their BCP 14 equivalents.
* The root of `vcdm.derived.schema.json` is a document that is one of the four top-level forms.

## Findings (source side)

| id | where | finding |
|---|---|---|
| F-01 | §4.2 L375 | the property list names `status`; §4.10 and the examples use `credentialStatus`, which is the term the context and the vocabulary define. |
| F-02 | §B.2 L4132 | the RefreshService base-class row says its types go into a `credentialRefresh` property; the property is `refreshService` (§5.4, the context). |
| F-03 | §4.9 / context | the text demands a `dateTimeStamp` for `validFrom` and `validUntil`; the base context types both as `xsd:dateTime`, which does not require a zone. The MUST is therefore carried by the schema pattern, not by the context (`contexts.yaml`). |
| F-04 | Example 25 | the two `digestSRI` values carry one base64 character too many; without it they equal the SHA-384 of the fetched contexts. See D-01 in `../examples/vectors.yaml`. |
| F-05 | §B.1, §B.2 | the SHA-256 the REC prints for the base context equals the fetched file (`59955ced…92734`); the §B.2 digest for the 2018 vocabulary equals the fetched file too. The §B.2 digest for `https://w3id.org/security#`, `689af6f3…74104`, equals no document pass 2 (verify) could fetch: neither the Resolved Document §B.2 names (`8a16b6b5…`, 35407 octets) nor what the vocabulary URL now redirects to (`02c4b488…`, 48622 octets), nor any of the five versions committed upstream (2022-10 to 2023-01); and VC Data Integrity §2.4 pins the same URL's JSON-LD to `082434d5…`. `contexts.yaml` `checked_not_copied`; `../normative.md` SD-26. |
| F-06 | §5.12 | `VerifiableCredentialGraph` is named as the type of each named graph but is not a term of the v2 context (it is a class of the 2018 vocabulary), so it can never appear as a compact `@type` in a document. |
| F-07 | context | the v2 context defines `proof` and the Data Integrity terms, the JWT/JOSE claim terms (`_sd`, `cnf`, `iat`, `exp`, `iss`, …) and a term literally named `...`; the REC mentions none of them as part of the base context (`contexts.yaml`). |
| F-08 | §5.2 L2876 | the only sentence that names `https://www.w3.org/ns/credentials/undefined-terms/v2`: a document that does not define all its terms MUST put it **last** in `@context`. No digest is printed for that context. |
| F-09 | §7.1 | steps 3 and 4 (`result.status` false → add `CRYPTOGRAPHIC_SECURITY_ERROR`; true → check the document is conforming) carry no BCP 14 keyword. They are the only statement of when each error is produced. |

## Tensions (the source against itself, or a reading this library had to choose)

| id | tension | choice taken |
|---|---|---|
| T-01 | `@context` "MUST be an ordered set where the first item is a URL…" (§4.3): is a bare string the one-item set? | accepted; an array must start with the base URL; `uniqueItems` is inferred from "set". |
| T-02 | `id`, `issuer`, `holder` are "a URL"; the REC defines URL by the URL Standard, which also admits relative references; elsewhere it says "globally unambiguous". | an absolute URL (has a scheme) is required; recorded as INFERRED. |
| T-03 | `name` and `description` "MUST be a string or a language value object" (§4.6 L922, L924, R-0162 and R-0164) against §6's sentence letting every property other than id, issuer, validFrom and validUntil be a single value or an array (L3240, R-0262, no keyword), §11.1's sentence allowing several language value objects as an array (L3961, the withdrawn R-0120, non-normative) and Example 6, which uses arrays. | the bare anchor follows §4.6 (arrays rejected); `#VerifiableCredential-arity` follows §6 and §11.1 (arrays accepted). Both are tested; Example 6 fails the first and passes the second. |
| T-03b | `holder` "MUST be either a URL or an object" (L2477) against the §6 arity sentence that would allow an array. | single value; an array is rejected. |
| T-04 | §11 is marked non-normative, yet §4.6 sends `name` and `description` to §11.1 for the language value object, whose MUST, SHOULD, MAY and MUST NOT sentences (L3941) sit in the non-normative section. | settled with requirements.yaml (pass 2, verify): §11.1 and §11.2 are non-normative by nesting (no normative class of their own inside the informative §11; `../protocol.yaml` T-11), so R-0118 to R-0123 are withdrawn and bind no one. R-0165 lets a test of R-0162 and R-0164 apply §11.1's description as what those MUST statements point at, which is what `#languageValueObject` does, for `name` and `description` only. `#languageValueObject-should` (`@language`, §11.1) and `#textValue-should` (§11.2, which §4.6 does not point at) are advice: their comments say so, and a miss there is not a SHOULD-level deviation from the REC. |
| T-05 | §5.13 calls the three returned items `verified`, `verifiedDocument`, `mediaType`; §7.1 calls the corresponding members `status`, `document`, `mediaType` and lists four more. | two separate anchors (`#SecuringVerificationResult`, `#VerificationResult`); neither accepts the other's names; not reconciled. |

## Inline regions (`inline.verbatim.txt`)

Region digest = sha256 of its lines joined by LF, no trailing LF (hazards.md §9). Lines are the
raw lines of the rendering; the file header says what the rendering's `| ` cell markers are.

| region | content | .txt lines | sha256 |
|---|---|---|---|
| I-01 | §4.5 type table | 890-905 | `0bddef276c201b67a02ed2b6792075380fa2e875a0fbab526cf9172b97dc1c72` |
| I-02 | §5.3 relatedResource table | 2883-2889 | `2d49b1979d7f81e831359ab1bb23bfb146e6d9022961b01f10a5ac90aeb6197a` |
| I-03 | §5.8 Example 32, dateTimeStamp expression | 3172-3178 | `8c92b21de3234a30211409a1fe9c77831ca844da796df66a317af209a5b0c1ea` |
| I-04 | §5.10 reserved properties table | 3191-3193 | `ad0c57c3b9a770d8fa10e38fc8212978c917d515b8b76ad5d675356a1e2a0e3b` |
| I-05 | §5.13 verification result items | 3219-3225 | `d2f3b133e7c0389554d3c5a760db99d9f99a6a9bc8085383ddb07f45bfd312eb` |
| I-06 | §7.1 verification result map | 3358-3365 | `17c9c5e54754b7dd375eb2b6c8bd39c06697fe4b102c09516c70ea8b6ebff1a1` |
| I-07 | §7.2 ProblemDetails and its four types | 3377-3393 | `bb3cfb37f54959fad3d425ce59908758ff2d2c716829a6446b8bd56e1beafd28` |
| I-08 | §B.2 vocabulary documents and hashes | 4115-4123 | `89967091f2b2a2f72b213574f5cbda0b1013cea2b34b4568b4f3e012ab99337c` |
| I-09 | §B.2 base classes table | 4126-4134 | `7ba4a59fccfcd4e7aa1dec81ed8d5a45683f98bf36b691c80a0c23096af30ac1` |
| I-10 | §B.3.1 sriString datatype | 4142-4152 | `91f0ecdd8a6029ab977a453d87f02eca9e623c4366a73ff015fe1ea966aee988` |
| I-11 | §C.1 application/vc template | 4172-4181 | `3beffab78f304de6c1f03dfd68da14aafc99f01fe1297cc47c2ed2c482634618` |
| I-12 | §C.2 application/vp template | 4185-4194 | `8a11f7a671cccb22ad949da1b9241615a4dfb5f1ae0241faac3e27241563eb8f` |

## Checks

Every check reports what it EXAMINED beside what it FOUND.

| check | examined | found |
|---|---|---|
| `run_checks.derived.py metaschema` | EXAMINED 2 schemas against the 2020-12 metaschema and 52 anchors for resolution, FOUND 0 problem(s) | |
| `run_checks.derived.py schema-tests` | EXAMINED 190 cases (66 accept, 124 reject expected), FOUND 0 unexpected verdict(s) | |
| `mutation_test.derived.py` | EXAMINED 21 mutations, FOUND 0 not detected | |
| `run_checks.derived.py examples` | 175 fixtures, 831 checks: 12 deviation, 21 fail, 193 na, 550 pass, 55 unverifiable (pass 2: X-05 on Example 18 was a pass that could not fail) | see `../examples/README.md` |

The mutation test found two real weaknesses in the first version of the test cases and the
cases were extended until none survived: the array branch of `digestSRI` was not exercised (a
`.*` pattern there changed no verdict), and neither branch of the credential-or-enveloped
discrimination in a presentation was exercised; a third, dropping the string-branch
pattern of `typeValue`, survived until a single-string type case was added. Nothing is claimed
about a rule that has no case; `cross-field-rules.derived.yaml` lists those as `none:`.

## Reading these files

* `python3 -I schema/run_checks.derived.py schema-tests` (needs the two packages) re-runs every case.
* The `YAML` files parse with both `bin/_yaml.py` and `bin/_record_yaml.py`; the readers differ only in
  that `_yaml.py` returns every scalar number and boolean as a string (`"true"`, `"9"`) and `_record_yaml.py` as a boolean or integer; compared after that normalisation the values are equal for all four YAML files.

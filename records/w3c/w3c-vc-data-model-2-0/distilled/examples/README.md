---
record: w3c-vc-data-model-2-0
kind: examples
title: "w3c-vc-data-model-2-0 — examples and test vectors"
extracted: "2026-11-07"
reviewed_by: ""
---

# Verifiable Credentials Data Model v2.0 — examples and test vectors

Pass 1 (extract), examples lane, mechanical. Every fixture comes from the W3C Recommendation
HTML, `.cache/w3c-vc-data-model-2-0.bin`, sha256
`a9196a3d0b6601356c4e127bad24f8c7f2c17f6ed22e41b35755a910104156f8` (= `content.sha256` in
`record.yaml`). None comes from the `.txt` rendering, which inserts a space at each `<span>`
boundary of a compact JWS and flattens the SD-JWT Decoded tabs.

## What is here

* **175 verbatim fixtures** (`ex<NN>-<tab>-<block>.<ext>`), in the 40 examples the REC numbers 1 to 40:
  112 `<pre>`, 9 JWS compact (`.jwt`), 9 SD-JWT compact (`.sd-jwt`), 9 COSE hex (`.hex`), 36 SD-JWT
  disclosure displays (`.txt`). Nine examples (3, 4, 5, 7, 8, 9, 11, 22, 35) are respec tabbed
  examples with seven tabs (Credential, ecdsa, ecdsa-sd, bbs, jose, cose, sd-jwt); all seven are
  fixtures. No fixture is derived (`derived_fixture_count: 0`).
* `reproduce.py` — re-extracts every fixture from the `.bin` and diffs: `python3 -I reproduce.py
  PATH/TO/w3c-vc-data-model-2-0.bin` (stdlib only). It checks the source digest, the counts, that an
  independent regex extractor agrees with the HTMLParser extractor on all 112 `<pre>`, and that each
  file here has identical bytes. `--write DIR` writes the fixtures.
* `vectors.yaml` — 40 vectors, one per example: title, section, the example's line in the rendering,
  the expected outcome, the defects (`D-nn`), the requirement ids the example exercises, and for each
  fixture its file, HTML line, size, sha256 and the checks that failed or deviated.
* `results.derived.json` — every check on every fixture, machine-readable; `python3 -I
  ../schema/run_checks.derived.py examples --check` recomputes and diffs it.

## How the fixture text is taken

The text content of the element, `<br>` read as LF, entities decoded, and respec's highlighting
`<span>`s (`hljs-*`, `highlight`, `comment`, `vc-hash`) dropped with their text kept. Nothing else
changes: the SD-JWT Decoded tabs keep their U+00A0 non-breaking spaces (the checks replace them with
spaces in memory), the compact forms keep the LF between their parts. The Example 25 `digestSRI`
values sit inside a `vc-hash` span; the text is what the span holds.

## Checks and verdicts

175 fixtures, 831 checks: 551 pass, 21 fail, 12 deviation (a SHOULD-profile miss), 55 unverifiable, 192 na.
Counted over `results.derived.json` by `run_checks.derived.py examples`.

* Each displayed data-model object was run against the MUST profile and the SHOULD profile of the
  derived schemas and the cross-field rules it can meet (X-01, X-03, X-05).
* Each JWS was decoded and its header and payload compared with the Protected Headers and
  application/vc tabs; each COSE hex was decoded (tag 18, four-element array, protected header map,
  payload bstr = the JSON of the tab, 64-octet signature); each SD-JWT was split, its disclosures
  decoded, every digest recomputed (SHA-256 over the printed disclosure) and found in an `_sd`
  array, the Decoded and Issuer Disclosures tabs compared, and the credential rebuilt by applying
  the disclosures and compared with the Credential tab.
* The 55 signature checks are all **unverifiable**: the REC prints no key for any signature, so no
  signature was verified.
* Examples 25 and 26 were checked against the fetched context files: the `digestMultibase` values of
  Example 26 equal the SHA-256 multihash of the files; the `digestSRI` values of Example 25 do not (D-01).
* Example 32's expression, joined, equals the schema `dateTimeStamp` pattern and accepts and rejects the
  sample values listed in its check.

## Source defects recorded, none repaired (details in `vectors.yaml` `defects:`)

| id | examples | finding |
|---|---|---|
| D-01 | 25 | both `digestSRI` values have one base64 character too many (65 instead of 64 after `sha384-`); without the leading `M` they equal the SHA-384 of the fetched files. Example 26 is exact. |
| D-02 | 17, 20, 21, 29, 35 | ellipsis placeholders or whole-line `//` comments, which §1.3 (L232) acknowledges; for 29 and 35 the checks also ran on the commented view with the comment lines dropped in memory. |
| D-03 | 28 | doubled outer braces; not JSON. |
| D-04 | 31 | unquoted member names and a missing comma; not JSON. |
| D-05 | 16 | the SD-JWT is not tilde-terminated after its last disclosure, unlike the nine tabbed ones. |
| D-06 | 36 | a template with placeholders and a missing comma. |
| D-07 | 6 | name and description are arrays of language value objects; §4.6 allows only a string or one language value object (tension T-03, `../schema/README.md`). |
| D-08 | 1 | a template with no issuer; expected to fail the MUST profile. |
| D-09 | 22 | one type value only: a SHOULD deviation on 9 displays. |

Examples 25, 26 and 36 to 39 are member displays, not documents: they do not parse alone and parse
once wrapped in braces (the check says so); that is by design except for 36.

## Not covered

No example can be run end to end: no key is printed, Examples 18 and 19 elide the payload of their
`data:` URL with an ellipsis, and Examples 17, 20, 21, 28 and 31 do not parse. The Data Integrity
proofs (`ecdsa-rdfc-2019`, `ecdsa-sd-2023`, `bbs-2023`) are checked for shape and for the body
matching the Credential tab only; their proof values belong to the Data Integrity lane.

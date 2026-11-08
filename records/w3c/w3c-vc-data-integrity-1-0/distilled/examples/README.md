---
record: w3c-vc-data-integrity-1-0
kind: examples
title: "w3c-vc-data-integrity-1-0 — examples and test vectors"
extracted: "2026-11-07"
reviewed_by: ""
---

# Verifiable Credential Data Integrity 1.0 — examples and test vectors

Pass 1 (extract), examples agent, mechanical lane. Every fixture comes from the W3C
Recommendation HTML, `.cache/w3c-vc-data-integrity-1-0.bin`, sha256 `ba5c4baf13fe3bab3ebd95ab6650d6fe83720e254b383bb444b4fbbae7bcf4fe`, which is
`content.sha256` in `record.yaml` and was recomputed from the cached file. None
comes from the `.txt` rendering. The 14 numbered examples are all the `<div class="example">`
elements of the document (counted by script: 14 `<pre>` blocks, 14 example divs).

`reproduce.py` re-extracts every fixture from the .bin by a method independent of
the one that wrote them (regular expressions and `html.unescape`, where the
writer used html5lib) and diffs: `python3 -I reproduce.py <path to .bin>` prints
EXAMINED 26 fixtures (14 verbatim + 12 derived), DIFFERENT 0. Appending one byte to a
fixture makes it exit 1 (tested).

`vectors.yaml` lists every fixture and **26 vectors**: 14 example vectors (`EX-NN`), 6 prose
vectors (`EX-P-nn`: the id, the domain and challenge values, the proof purposes,
the error codes, the cryptosuite names) and 6 digest vectors (`EX-CTX-n`: the three
pinned contexts and the three vocabulary documents of §2.4), wired to R-ids by script. Pass 2 re-pointed every
`constrained_by` and `rule` list: pass 1 had cited the skeleton's welded parent sentences (148 of 241 citations) and left
four vectors unwired (EX-01, EX-03, EX-P-04, EX-P-06); each now names the split child or keyword-less entry it means.

Checks: **174** in all: 121 pass, 47 fail, 6 unverifiable; 140 meet their stated expectation and
34 differ from it. Vector outcomes: 9 pass, 17 fail, 0 unverifiable (fail if any check
fails). A fail on a source example is a finding about the source, recorded below and
not repaired. Both YAML readers of `bin/` read `vectors.yaml` (1497 scalar leaves after pass 2's re-wiring, 1401 before) with 0 differences.

## Fixtures (26: 14 verbatim, 12 derived)

An unmarked file name holds the source's own characters (the text of the `<pre>`,
character references decoded, `<wbr>` and highlighting elements dropped, nothing else
changed); `.derived.` marks a file this extraction computed (reproduced by `reproduce.py`).

| example | file | HTML lines | bytes | sha256 | derived |
|---|---|---|---|---|---|
| 1 | `ex01-simple-json-document.json` | 1351-1353 | 50 | `71b62e2ef5f3213a…` | `ex01-simple-json-document.derived.json` |
| 2 | `ex02-simple-signed-json-document.json` | 1367-1377 | 430 | `61a2843265794222…` | — |
| 3 | `ex03-simple-json-ld-document.json` | 1387-1390 | 119 | `f54357ca4cf0a9bf…` | `ex03-simple-json-ld-document.derived.json` |
| 4 | `ex04-simple-signed-json-ld-document.json` | 1404-1418 | 562 | `4dbb4124bd2ae1d0…` | — |
| 5 | `ex05-proof-with-expires.json` | 1438-1454 | 655 | `a1e2c65a3e1072ba…` | `ex05-proof-with-expires.derived.json` |
| 6 | `ex06-proof-set.json` | 1475-1498 | 1027 | `443cb3aa9648a7eb…` | `ex06-proof-set.derived.json` |
| 7 | `ex07-proof-chain.json` | 1516-1541 | 1205 | `fcbb89b7c8006d0c…` | `ex07-proof-chain.derived.json` |
| 8 | `ex08-integrity-protected-image.json` | 1677-1684 | 163 | `26cd287485a98fa3…` | `ex08-integrity-protected-image.derived.json` |
| 9 | `ex09-symbolic-proof.json` | 3812-3819 | 231 | `1cbc697af8d4c427…` | `ex09-symbolic-proof.derived.json` |
| 10 | `ex10-symbolic-proof-set.json` | 3834-3846 | 367 | `7fec6cbda4e6aba4…` | `ex10-symbolic-proof-set.derived.json` |
| 11 | `ex11-symbolic-proof-set-removal.json` | 3861-3870 | 269 | `6d4dc200a3726d60…` | `ex11-symbolic-proof-set-removal.derived.json` |
| 12 | `ex12-symbolic-chain-first-proof.json` | 3893-3900 | 194 | `ddf4d9676c59cac9…` | `ex12-symbolic-chain-first-proof.derived.json` |
| 13 | `ex13-symbolic-chain-two-proofs.json` | 3915-3927 | 365 | `9fe8b503c3901d9b…` | `ex13-symbolic-chain-two-proofs.derived.json` |
| 14 | `ex14-symbolic-chain-three-proofs.json` | 3948-3965 | 534 | `ae1fd4c0b6a1dd7d…` | `ex14-symbolic-chain-three-proofs.derived.json` |

Derivations: Examples 1 and 3, the trailing `;` removed; 5, 6, 7, the `//` comment
lines removed; 8, the `image` object alone (the display elides the rest of the object with `...`);
9 to 14, the comment lines removed and the unquoted `publicXXX` and `signature(...)`
placeholders written as JSON strings. Examples 2 and 4 are valid JSON as printed.
`signatures.derived.json`, `keys.derived.json` and `context-digests.derived.json` hold
the computed evidence below.

## Findings on the examples (not repaired)

- **D-01** Examples 1 and 3 end with `};`: not JSON.
- **D-02** Examples 5, 6, 7, 10–14 carry `//` comment lines: not JSON. Example 7's `@context` closing bracket is at column 0.
- **D-03** Example 8 elides with `...`: a fragment, not JSON.
- **D-04** Examples 9–14 are symbolic: `type`, `cryptosuite`, `created` and `proofPurpose` are omitted by the source's own statement (§A), `verificationMethod` and `proofValue` are placeholders. They fail `proof.derived` for that reason and carry no signature.
- **D-05** The `proofValue` of Example 2 and of both proofs of Example 7 decodes (base58btc after `z`) to **65 octets**; an Ed25519 signature is 64. Examples 4, 5 and 6's decode to 64.
- **D-06** Several `proofValue`s are rearrangements of one another's characters, not independent values: Ex2[0] = Ex6[0], Ex2[0] = Ex7[0], Ex4[0] = Ex5[0], Ex6[0] = Ex7[0], Ex6[1] = Ex7[1]. Example 5's is a rearrangement of Example 4's although its proof differs only by `expires`.
- **D-07** The second verification-method key of Examples 6 and 7 (`z6MkGskx…`) is a rearrangement of the characters of the first (`z6MkjLrk…`) and decodes to multicodec prefix `ecff`, not `ed01` (Ed25519 public key).
- **D-08** None of the 7 proofs verifies under its printed key (0 verified): 2 fail on signature length (Example 2, Example 7 proof 0), 2 on the key prefix (Examples 6 and 7, second proof), 3 fail the signature check itself (Examples 4 and 5, Example 6 proof 0). D-05 to D-07 explain the first four; Examples 4 and 5 (ECDSA P-256 over RDFC) and Example 6 proof 0 fail for no reason found in the examples themselves, other than D-06.
- **D-09** §2.4's three vocabulary digests (`application/ld+json`, `text/turtle`, `text/html`) equal none of the documents served on 2026-11-07, by every route tried (`https://w3id.org/security` with the `Accept` header; the `www.w3.org/2025/credentials/vcdi/vocab/v2/` location it now redirects to; the `w3c.github.io` URLs in the HTML). The three context digests equal the fetched files exactly. The REC is frozen and the vocabulary is a living document, so this is drift, not necessarily an error at publication; the text tells a reader to compare against the live URL.
- **D-10** Example 3 differs from Example 4 minus its proof in `@context` only: Example 4 adds the Data Integrity v2 context (§2.4.2 context injection). Example 1 equals Example 2 minus its proof.
- **D-11** (pass 2) The `verificationMethod` key of Examples 4 and 5, `zDnaepBuvsQ8…`, is the P-256 test-vector key of vc-di-ecdsa A.1, whose secret key that document publishes (`z42twTcN…`; its public key recomputes to the fragment). The examples could have carried genuine signatures; neither verifies.

## Signature attempts

Each proof is verified with the key in its own `verificationMethod` fragment, by the recipe of the cryptosuite document
(`eddsa-jcs-2022`, `eddsa-rdfc-2022`, `ecdsa-rdfc-2019`): `hashData` = SHA-256 of the canonical proof configuration followed by SHA-256 of the
canonical document; JCS is sorted keys and no whitespace; RDFC is URDNA2015 by pyld with the Data Integrity v2
context from the file whose digest the source prints; Ed25519, or ECDSA P-256 with SHA-256, over `hashData`. For a chain, a proof
with `previousProof` is verified over the document carrying the proof it names. **The recipe is not this source's.** Pass 1 wrote it from memory; pass 2 read it in the cryptosuite Recommendations
(`vc-di-eddsa` and `vc-di-ecdsa`, W3C Recommendation 15 May 2025, fetched 2026-11-07, sha256 `d404f372…` and `790f86ce…`)
and `verify-signatures.derived.py` reproduces their own test vectors with it: 11 checks examined, 0 failing
(eddsa-jcs-2022 B.3: both hashes, `hashData`, verification, and a re-signature equal to Example 37 byte for byte;
eddsa-rdfc-2022 B.1: verification; ecdsa-rdfc-2019 A.1: both canonical N-Quads forms, both hashes, verification).
So a fail below is a property of the example, not of the harness. The same script re-runs the seven proofs
(7 examined, 0 verify, 0 differing from the table). The harness is self-consistent: for each of the three suites
a fresh signature made by the same code verifies, fails with one bit of the signature flipped, and fails when the document is altered
(eddsa-jcs-2022, eddsa-rdfc-2022, ecdsa-rdfc-2019: [('pass', 'fail', 'fail'), ('pass', 'fail', 'fail'), ('pass', 'fail', 'fail')]).

| example | proof | suite | result | why |
|---|---|---|---|---|
| 2 | 0 | eddsa-jcs-2022 | fail | signature is 65 octets, Ed25519 needs 64 |
| 4 | 0 | ecdsa-rdfc-2019 | fail | signature does not verify under the printed key (SHA-256) |
| 5 | 0 | ecdsa-rdfc-2019 | fail | signature does not verify under the printed key (SHA-256) |
| 6 | 0 | eddsa-rdfc-2022 | fail | signature does not verify under the printed key (SHA-256) |
| 6 | 1 | eddsa-rdfc-2022 | fail | key multicodec prefix ecff and length 34: not an ed25519-pub multikey (ed01, 34 octets) |
| 7 | 0 | eddsa-rdfc-2022 | fail | signature is 65 octets, Ed25519 needs 64 |
| 7 | 1 | eddsa-rdfc-2022 | fail | key multicodec prefix ecff and length 34: not an ed25519-pub multikey (ed01, 34 octets) |

## Not done

No example signature verifies. The RDFC path is pyld's URDNA2015, which reproduced vc-di-ecdsa A.1's canonical
N-Quads exactly (pass 2); it was not run against the RDF Dataset Canonicalization test suite. Examples 9–14 have no values to verify.
`verify-signatures.derived.py` needs the two cryptosuite HTML files and the three context files (paths as arguments,
none in the repository) and PyLD and cryptography.

---
record: w3c-vc-jose-cose
kind: examples
title: "w3c-vc-jose-cose — examples and test vectors"
extracted: "2026-11-03"
reviewed_by: ""
---

# Securing Verifiable Credentials using JOSE and COSE — examples and test vectors

Pass 1 (extract), examples agent, effort max. Every fixture comes from the W3C
Recommendation HTML, `.cache/w3c-vc-jose-cose.bin`, sha256
`6c70cf8d7de9d8a3ff28a743fea9d569a67a402111c3245fdafbaa2ad6709af9`, which is
`content.sha256` in `record.yaml` and was recomputed from the cached file on
2026-11-04. None comes from the `.txt` rendering, whose compact tokens carry a
space before each separator (P-01).

`vectors.yaml` lists every fixture (file, locator, HTML line range, media type,
expected result, sha256) and **56 vectors** wired to R-ids in
`requirements.yaml`:

- **32 example vectors**: one per tab of the 6 tabbed credential and
  presentation examples (6 jose, 6 sd-jwt, 6 cose) and one per untabbed example
  (Examples 10 to 17 and 21 to 26).
- **23 data: URL vectors** (`EX-DU-nn`): every distinct data: URL in the
  examples, whether printed (8.4), inside a signed payload or disclosure, or
  inside a display.
- **1 prose vector**: the kid printed in 4.2 as an example of R-0073.

Checks: **592** in all — 347 pass, 166 fail, 77 unverifiable, 2 not run. Vector
outcomes: 51 fail, 3 unverifiable, 2 pass (fail if any check fails, else
unverifiable if any check is). A fail on a source example is a finding about
the source, recorded below and not repaired. Pass 1 counted 588 checks (349,
172, 65, 2) and 49, 5, 2 outcomes; the cross-check pass graded the old typ and
cty of EX-DU-04 and EX-DU-06 (4 checks more), failed the one-token check of
EX-DU-01 and EX-DU-15, and regraded the 12 R-0072 and R-0073 checks of six tab
vectors as unverifiable, since §4.2 binds only where controlled identifier
documents are used (D-09).

## Fixtures (105: 80 verbatim, 25 derived)

An unmarked file name holds the source's own characters; `.derived.` marks a file
this extraction computed. Names are `exNN-<tab>-<block>.<ext>`: `.json` for a
display the source shows as JSON (whether or not it parses), `.jwt` for a JWS
Compact Serialization, `.sd-jwt` for an SD-JWT, `.hex` for COSE hex, `.diag` for
CBOR diagnostic notation, `.txt` for anything else.

| example | section | verbatim fixtures | derived |
|---|---|---|---|
| 1 | §3.1.1 | `ex01-credential.json`, `ex01-jose-protected-headers.json`, `ex01-jose-application-vc.json`, `ex01-jose-vc-jwt.jwt` | `ex01-jose-vc-jwt.derived.json` |
| 2 | §3.1.2 | `ex02-presentation.json`, `ex02-jose-protected-headers.json`, `ex02-jose-application-vp.json`, `ex02-jose-vp-jwt.jwt` | `ex02-jose-vp-jwt.derived.json` |
| 3 | §3.1.2 | `ex03-presentation.json`, `ex03-jose-protected-headers.json`, `ex03-jose-application-vp.json`, `ex03-jose-vp-jwt.jwt` | `ex03-jose-vp-jwt.derived.json` |
| 4 | §3.2.1 | `ex04-credential.json`, `ex04-sd-jwt-encoded.sd-jwt`, `ex04-sd-jwt-decoded-header.txt`, `ex04-sd-jwt-decoded-payload.txt`, `ex04-sd-jwt-issuer-disclosures.txt` | `ex04-sd-jwt-encoded.derived.json` |
| 5 | §3.2.2 | `ex05-presentation.json`, `ex05-sd-jwt-encoded.sd-jwt`, `ex05-sd-jwt-decoded-header.txt`, `ex05-sd-jwt-decoded-payload.txt`, `ex05-sd-jwt-issuer-disclosures.txt` | `ex05-sd-jwt-encoded.derived.json` |
| 6 | §3.2.2 | `ex06-presentation.json`, `ex06-sd-jwt-encoded.sd-jwt`, `ex06-sd-jwt-decoded-header.txt`, `ex06-sd-jwt-decoded-payload.txt`, `ex06-sd-jwt-issuer-disclosures.txt` | `ex06-sd-jwt-encoded.derived.json` |
| 7 | §3.3.1 | `ex07-credential.json`, `ex07-cose-application-vc.json`, `ex07-cose-vc-cose.hex` | `ex07-cose-vc-cose.derived.diag` |
| 8 | §3.3.2 | `ex08-presentation.json`, `ex08-cose-application-vp.json`, `ex08-cose-vp-cose.hex` | `ex08-cose-vp-cose.derived.diag` |
| 9 | §3.3.2 | `ex09-presentation.json`, `ex09-cose-application-vp.json`, `ex09-cose-vp-cose.hex` | `ex09-cose-vp-cose.derived.diag` |
| 10 | §4.2 | `ex10-issuer-cid-identifier.json` | — |
| 11 | §4.2 | `ex11-kid-vm-identifier.json` | — |
| 12 | §4.2 | `ex12-holder-cid-identifier.json` | — |
| 13 | §4.2 | `ex13-kid-vm-identifier.json` | — |
| 14 | §8.1 | `ex14-minimal-cid.json` | — |
| 15 | §8.1 | `ex15-cid-verification-method.json` | — |
| 16 | §8.1 | `ex16-cid-verification-relationships.json` | — |
| 17 | §8.1 | `ex17-vc-cid-document.json` | — |
| 18 | §8.2 | `ex18-credential.json`, `ex18-jose-protected-headers.json`, `ex18-jose-application-vc.json`, `ex18-jose-vc-jwt.jwt`, `ex18-cose-application-vc.json`, `ex18-cose-vc-cose.hex`, `ex18-sd-jwt-encoded.sd-jwt`, `ex18-sd-jwt-decoded-header.txt`, `ex18-sd-jwt-decoded-payload.txt`, `ex18-sd-jwt-issuer-disclosures.txt` | `ex18-jose-vc-jwt.derived.json`, `ex18-sd-jwt-encoded.derived.json`, `ex18-cose-vc-cose.derived.diag` |
| 19 | §8.2 | `ex19-credential.json`, `ex19-jose-protected-headers.json`, `ex19-jose-application-vc.json`, `ex19-jose-vc-jwt.jwt`, `ex19-cose-application-vc.json`, `ex19-cose-vc-cose.hex`, `ex19-sd-jwt-encoded.sd-jwt`, `ex19-sd-jwt-decoded-header.txt`, `ex19-sd-jwt-decoded-payload.txt`, `ex19-sd-jwt-issuer-disclosures.txt` | `ex19-jose-vc-jwt.derived.json`, `ex19-sd-jwt-encoded.derived.json`, `ex19-cose-vc-cose.derived.diag` |
| 20 | §8.3 | `ex20-presentation.json`, `ex20-jose-protected-headers.json`, `ex20-jose-application-vp.json`, `ex20-jose-vp-jwt.jwt`, `ex20-cose-application-vp.json`, `ex20-cose-vp-cose.hex`, `ex20-sd-jwt-encoded.sd-jwt`, `ex20-sd-jwt-decoded-header.txt`, `ex20-sd-jwt-decoded-payload.txt`, `ex20-sd-jwt-issuer-disclosures.txt` | `ex20-jose-vp-jwt.derived.json`, `ex20-sd-jwt-encoded.derived.json`, `ex20-cose-vp-cose.derived.diag` |
| 21 | §8.4 | `ex21-uri-encoded-sd-jwt-vc.txt` | `ex21-uri-encoded-sd-jwt-vc.derived.json` |
| 22 | §8.4 | `ex22-uri-encoded-sd-jwt-vp.txt` | `ex22-uri-encoded-sd-jwt-vp.derived.json` |
| 23 | §8.4 | `ex23-uri-encoded-cose-vp.txt` | `ex23-uri-encoded-cose-vp.derived.hex`, `ex23-uri-encoded-cose-vp.derived.diag` |
| 24 | §8.5 | `ex24-cose-sign1-protected-header-vc.diag` | — |
| 25 | §8.5 | `ex25-cose-sign1-protected-header-vp.diag` | — |
| 26 | §8.5 | `ex26-cose-sign1-attached-payload.diag` | — |
| all | — | — | `data-urls.derived.json`, `keys.derived.json`, `signatures.derived.json` |

**What the verbatim fixtures are.** Each is the textContent of its element after
HTML5 tree construction (html5lib 1.1), so character references are decoded.
Nothing else is changed except, and each is counted in `vectors.yaml`:

- compact JWS and SD-JWT displays: the HTML puts each `<span>` on its own line,
  so an LF precedes every `.` and `~` (and follows the last `~`). Those LFs are
  removed; they are source layout, not token characters;
- COSE hex: the one LF on each side of the digits is removed;
- the Decoded tab writes each line break as `<br>`; each is written as one LF;
- the Issuer Disclosures tab is written block by block: the `<h3>` and the three
  `<p>` of each disclosure, one per line (each `<br>` inside Contents written as
  one LF, as in the Decoded tab), blocks separated by an empty line.

U+00A0 is kept where the source has `&nbsp;` (the 18 Decoded and Issuer
Disclosures files); no fixture has any other non-ASCII character. A file ends
with LF only where its element does (18 do).

**Derived files.** `*.derived.json` for each JWS and SD-JWT: header, payload,
signature, every disclosure decoded with its recomputed digest and where it
occurs, and the claims after SD-JWT processing. `*.derived.diag` for each
COSE_Sign1: diagnostic notation that the strict reader reads back and cbor2
re-encodes to exactly the source octets (asserted for all 7).
`ex23-uri-encoded-cose-vp.derived.hex` is Example 23's base64 data decoded.
`data-urls.derived.json`, `keys.derived.json` and `signatures.derived.json` are
the tables the data: URL, key and signature checks produced.

## Checks that ran (each with what it examined)

Scripts and a venv in scratch (`/tmp/lib89s/ex-v6`), not committed: Python 3.14,
html5lib 1.1, cryptography 50.0.2, cbor2 6.2.0.post2, jwcrypto 1.6.1, pycose
1.1.0, all installed into a fresh venv. From the scratch of the earlier
attempts (v4, v5), reviewed and reused: the base64url, strict-JSON and RFC 2397
helpers, the signature-attempt and RFC 7515 control code, and the diagnostic
notation reader. Everything else is new, and every result here was re-run.

1. **Byte fidelity.** A second extraction with regular expressions and
   `html.unescape` over the raw bytes, sharing no code with the DOM one,
   reproduces **80 of 80** verbatim fixtures byte for byte. Every `<pre>`,
   compact display, COSE hex and disclosure list in the document lies inside an
   example (56, 6, 6, 6, 6 found document-wide). Mutating two fixtures made it
   report exactly those two.
2. **JSON.** 38 fixtures shown as JSON were parsed strictly (RFC 8259, duplicate
   names rejected): 33 parse, 5 do not (`ex10-issuer-cid-identifier.json`, `ex11-kid-vm-identifier.json`, `ex12-holder-cid-identifier.json`, `ex13-kid-vm-identifier.json`, `ex14-minimal-cid.json`).
3. **JWS.** 22 JWS decoded, counted per enclosing example (6 jose tabs, 13
   SD-JWT issuer-signed JWTs, 1 KB-JWT, and 2 JWS inside data: URLs); 19
   distinct, since the 13 issuer-signed JWTs are 10 distinct: all 3-part, all canonical unpadded
   base64url, header and payload all JSON.
   **Tab against tab**, as JSON values: Protected Headers against the decoded
   header 6/6 equal; application/vc|vp displays against the decoded payload
   10/12 (every equal display, header or payload, is byte for byte the 2-space
   pretty-print plus LF: 16 files); unsecured tab against each signed payload
   or processed SD-JWT 9/18; Decoded tab, U+00A0 read as U+0020, against the
   decoded header or payload 12/12; COSE payload octets against the same
   example's JWS payload 2/3.
4. **SD-JWT.** 13 SD-JWTs, counted per enclosing example (6 tabs, Examples
   21 and 22, 5 inside data: URLs); the 5 inside data: URLs are 3 distinct
   tokens (Examples 6 and 9 enclose one presentation, 8 and 23 one credential),
   so 11 are distinct. 35 disclosures in the 6 tabs: every recomputed digest equals the
   hash the Issuer Disclosures tab shows and occurs once in the payload; every
   Contents equals the decoded disclosure. 39 more in the other 7 SD-JWTs,
   counted per enclosing example (27 in the 5 distinct ones; messages.yaml
   TEN-01 counts that way), all referenced except the one in Example 22 that is
   its KB-JWT (D-14).
5. **COSE.** 7 COSE_Sign1 (6 cose tabs and Example 23) decoded by a strict
   decoder written for this pass and by cbor2; both agree, every item uses
   definite lengths and preferred argument encodings, and cbor2 re-encodes each
   to the same octets. Protected-header labels, tag, payload and signature are
   in each `EX-*-COSE` vector.
6. **Keys and kids.** 7 distinct public keys are printed: 5 in 8.1 (Examples
   15 and 16 repeat one P-384 key that Example 17 also lists), the did:jwk in
   Example 17 (the same Ed25519 key as its verificationMethod[1]), and two
   `cnf.jwk` holder keys inside credentials. Every EC point is on its curve with
   full-length coordinates. 23 kid occurrences were compared with the RFC 7638
   thumbprint (SHA-256, SHA-384, SHA-512, and the non-standard all-members
   form) and the verificationMethod ids of every key: the 21 in signed
   objects match nothing; the 2 in Examples 11 and 13 equal the id of the P-384
   verification method in Examples 15 and 16.
7. **Signatures.** 29 signatures, counted per enclosing example (22 JWS,
   SD-JWT and KB-JWT; 7 COSE_Sign1), which are 26 distinct signature and
   message pairs (19 JWS, 7 COSE_Sign1), x 7 keys, ECDSA under SHA-256, SHA-384 and SHA-512 whatever alg says, EdDSA
   where the signature is 64 octets: **458 attempts, 1 verifies** — the
   Example 22 KB-JWT under the `cnf.jwk` of its own credential (key 7). A
   non-standard probe over each bare COSE payload added 112 attempts and no
   success. Controls through the same code: RFC 7515 A.3 (ES256) and A.4
   (ES512) from `.cache/rfc-7515.txt`, fresh ES256, ES384 and Ed25519
   signatures, and pycose-made COSE_Sign1 messages all verify, and all fail
   with one bit flipped (11 controls, all as expected). jwcrypto agrees on all
   132 JWS/key pairs it can run (1 VALID, the same one) and pycose on all 21
   COSE/P-384 pairs (none valid); it refuses the other 14 pairs, P-256 or P-521
   keys with alg -35.
8. **data: URLs.** 23 distinct values checked against the RFC 2397 grammar
   (`data:` [mediatype] [`;base64`] `,` data, data in RFC 2396 uric):
   11 break the grammar (3, 4, 5, 7, 10, 11, 12, 13, 17, 19, 20); 7 are two URLs welded
   with `;` (1, 5, 8, 9, 12, 13, 17); 9 carry spaces (3, 4, 5, 11, 12, 13, 17, 19, 20); 3 use
   `;base64url` (7, 10, 11); 1 has a media type outside the six of 6.1 (17); 5
   decode, as printed, to the token their media type names (2, 6, 14, 16, 18).
   1 and 15 fail that check: 1 decodes only part by part, after the split at
   `;data:`, since as a whole its data is two tokens (D-15), and 15 only if its
   last `~` is read as closing the KB-JWT, which a strict parser does not do
   (D-14). Occurrences, as distinct from values: 41 in the display tabs, each
   printed in a display or nested in a token a display carries (46 with the 5
   that the Issuer Disclosures tabs reprint), 30 of them EnvelopedVerifiableCredential
   ids.
9. **Diagnostic notation.** Examples 24 to 26 read with a strict reader (RFC
   8949 §8 and RFC 8610 Appendix G, external) that records every defect and
   recovers: 6, 6 and 4 defects. Its controls: a well-formed rendering of
   Example 24 reads clean, and each defect class planted alone is reported.
   Example 26's 6 hex fragments and the 2 of the kid in Examples 24 and 25
   were searched in 115 octet strings decoded from the examples (headers,
   payloads, signatures, keys, thumbprints, kids): none occurs.
10. **YAML.** `vectors.yaml` is read by both `bin/_yaml.py` and
    `bin/_record_yaml.py`; every leaf value of both equals what was written.
    `vectors.yaml` and this file hold no backslash; no verbatim fixture holds
    one; 16 derived JSON files hold JSON's own escaped quotation mark (196 of
    them) and no other escape. No file holds the marker string the validator
    rejects.

## Claims made by other agents, checked independently

| claim | verdict | what the source shows |
|---|---|---|
| all 7 COSE examples have alg -35 (ES384) with 64-octet signatures | **confirmed** | 7 of 7 COSE_Sign1 (Examples 7, 8, 9, 18, 19, 20 and 23) have protected `{1: -35}` and a 64-octet signature; ES384 needs 96 (RFC 9053 §2.1, external). No key verifies any of them. |
| no example kid matches any printed key, and the outer JOSE kids are not absolute URLs | **confirmed for signed objects; refuted for Examples 11 and 13** | none of the 21 kids in signed objects is the thumbprint or verificationMethod id of a printed key, and none is an absolute URL (`ExHk…` in all 12 outer JOSE and SD-JWT headers, `SI3RH…` in Examples 21 and 22, `UQM__…` inside Examples 6 and 9). The kid of Examples 11 and 13, `https://university.example/issuers/565049#key-123`, is the id of the P-384 verification method of Examples 15 and 16. The COSE examples carry no kid at all. |
| Example 17's type is JsonWebKey2020 and its key-id thumbprint doesn't match its key | **half confirmed** | verificationMethod[1] has type `JsonWebKey2020` (against R-0070). Its `publicKeyJwk.kid` thumbprint `FfMbzOjMmQ4e…` **does** match its key. The mismatches are elsewhere: verificationMethod[0]'s id embeds `NzbLsXh8uDCc…`, which is not its P-521 key's (`GOwvnQ44eBJY…`) but the RFC 7638 §3.1 example RSA key's (external, recomputed); and verificationMethod[1]'s id `#z6Mkh…` decodes to an Ed25519 key other than its `x`. |
| Examples 10–14 are not valid JSON (`// ...`) | **confirmed, cause half right** | none of the five parses, but `// ...` is the cause only in 10 and 12; in 11 and 13 the kid string is never closed; in 14 a comma follows the last member. |
| Examples 24–26 are not valid CBOR diagnostic notation | **confirmed** | 24 and 25: unquoted text (3 each), elided hex in `h''`, 2 trailing commas; 26: elided hex in 3 `h''`, a missing comma. |
| Example 20 has `;base64url` data URLs and double/triple encoding | **confirmed** | the unsecured tab has `data:application/vc+cose;base64,0oREo...+Q==` (elided, not decodable). The jose payload has `;base64url,` + base64url of the text `base64,0oREo...+Q==` (two encodings); the cose payload and the sd-jwt disclosure base64url that once more (three), the disclosure with a leading space. `;base64url` is not RFC 2397 syntax, against R-0051. |
| Examples 6, 9, 21 and 22 carry the old `+ld+json` typ/cty values | **confirmed, with a location correction** | in 21 and 22 the SD-JWT header itself has typ `vc+ld+json+sd-jwt` and cty `vc+ld+json` (22 too, though labelled vp). In 6 and 9 the outer headers have no typ or cty; the values (`vp+ld+json+sd-jwt`, `vp+ld+json`) are in the SD-JWT presentation inside the EnvelopedVerifiablePresentation id, which in 6 begins with a space. Appendix A: "Changed media types from application/{vc,vp}+ld+json+{jwt,sd-jwt,cose} to application/{vc,vp}+{jwt,sd-jwt,cose}." |
| Example 22 carries Example 21's credential JWT byte for byte, and a `~` follows its KB-JWT | **confirmed** | the issuer-signed JWTs are identical (1338-character signing input and the same signature); 4 of Example 21's 6 disclosures follow, then the KB-JWT, then `~`. Also: the KB-JWT has no `sd_hash`, and its signature verifies under the credential's `cnf.jwk` — the only signature in the document that verifies. |
| Examples 8 and 9 (vp+cose) envelope SD-JWT content | **confirmed** | Example 8's enclosed credential is `data:application/vc+sd-jwt,…` (two copies joined by `;`, and a space before a `~` in each); Example 9's EnvelopedVerifiablePresentation id is `data:application/vp+sd-jwt,…`. Example 23 (vp+cose) does the same with `application/vc-ld+sd-jwt`. For 8 and 23 that is against the second sentence of R-0059 ("These credentials are secured using COSE in this case."); 9 encloses a presentation, for which the source names no mechanism (R-0058, the Enveloped type, is met). |
| COSE payloads are JSON bytes identical to the JWS payloads | **partly refuted** | all 7 COSE payloads are JSON. Example 7's is octet-identical to Example 1's JWS payload, and 18's and 19's to their own JWS payloads; Example 20's is not (679 vs 670 octets: one more base64url layer, D-17). Examples 8, 9 and 23 have no JWS with the same payload: 8 and 9 envelope SD-JWT where 2 and 3 envelope JWS; 23 is Example 8's payload with `vc-ld+sd-jwt` for `vc+sd-jwt`. |

## Findings (recorded, not repaired)

Defects in the examples (D) and in their presentation (P). Each is a fail in the
vectors named, except D-09, which is conditional and graded unverifiable there.
"external" marks a rule from another document.

| id | where | finding | vectors |
|---|---|---|---|
| D-01 | Ex 10, 12 | line 5 is `// ...`; JSON has no comments, so neither parses. | EX-10, EX-12 |
| D-02 | Ex 11, 13 | the kid string `"https://university.example/issuers/565049#key-123` has no closing quotation mark; neither parses. | EX-11, EX-13 |
| D-03 | Ex 14 | a comma after the last member; does not parse. | EX-14 |
| D-04 | Ex 17 | verificationMethod[1] has type `JsonWebKey2020`; R-0070 says MUST be `JsonWebKey`. | EX-17 |
| D-05 | Ex 17, §4.2 | verificationMethod[0]'s id embeds the JWK Thumbprint `NzbLsXh8…`, the RFC 7638 §3.1 example RSA key's (external), not its own P-521 key's `GOwvnQ44…`; §4.2's example kid embeds the same value. | EX-17; EX-4.2-P1 records it in a check that passes (R-0073 is met) |
| D-06 | Ex 17 | verificationMethod[1]'s id `#z6Mkh…` (base58btc, multicodec 0xed01) is an Ed25519 key other than its `publicKeyJwk.x`. | EX-17 |
| D-07 | Ex 7, 8, 9, 18, 19, 20, 23 | every COSE_Sign1 says alg -35 (ES384) and has a 64-octet signature; ES384 is 96 (RFC 9053 §2.1, external). | EX-07-COSE, EX-08-COSE, EX-09-COSE, EX-18-COSE, EX-19-COSE, EX-20-COSE, EX-23 |
| D-08 | all signed examples | no issuer signature verifies with any key the document prints (458 attempts over all 29 signatures, 26 distinct, whose one success is the Ex 22 KB-JWT, a holder signature). The signers' kids name no printed key. The ES384 credentials whose issuer is `https://university.example/issuers/565049` (inside Ex 2, and Ex 21, 22) do not verify under the P-384 key Ex 15 and 16 publish for that identifier, though Ex 11 and 13 point a kid at it. | EX-15, EX-16, and every vector with a signature |
| D-09 | Ex 1, 4, 7, 18 | iss is absent and the issuer is a URL, so wherever controlled identifier documents are used, the condition §4.2 opens with for all its requirements, R-0072 requires the kid to be an absolute URL to a verification method (and R-0073 recommends a thumbprint URI): the JOSE and SD-JWT kids are `ExHk…`, the COSE ones absent. No example says whether a controlled identifier document is used, so the 6 R-0072 and 6 R-0073 checks are unverifiable, not fail. | EX-01-JOSE, EX-04-SDJWT, EX-07-COSE, EX-18-JOSE, EX-18-SDJWT, EX-18-COSE (unverifiable) |
| D-10 | Ex 2 | the credential inside Ex 2 is signed ES384 under the kid `ExHk…` that the outer JWS uses with ES256: one kid, two curves (ES256 is P-256, ES384 is P-384: RFC 7518 §3.4, external). | EX-DU-01 |
| D-11 | every tab, Ex 23 | no header in the 18 jose, sd-jwt and cose tabs has typ, and none of the 7 encoded COSE protected headers (Ex 23 included) has typ (16) or content type (3): R-0013, R-0018, R-0028, R-0034, R-0048, R-0049, R-0054 and R-0055 are unmet wherever they apply (SHOULD). Ex 21 and 22 have typ, with the D-12 values; the diagnostic headers of Ex 24 and 25 have content type (3) and no typ (16); Ex 26's protected header is printed elided after its first entry, so it cannot be checked. | every EX-*-JOSE, -SDJWT, -COSE, EX-23 |
| D-12 | Ex 6, 9, 21, 22 | typ `vc+ld+json+sd-jwt` / `vp+ld+json+sd-jwt` and cty `vc+ld+json` / `vp+ld+json`, the names Appendix A says were changed; in 6 and 9 only inside the enclosed presentation. | EX-21, EX-22 (R-0028/R-0029, R-0034/R-0035); EX-DU-04, EX-DU-06 (R-0034/R-0035) |
| D-13 | Ex 22 | labelled `application/vp+sd-jwt` but holds a credential: Example 21's issuer-signed JWT, byte for byte, with typ `vc+ld+json+sd-jwt`. | EX-22 |
| D-14 | Ex 22 | a `~` follows the KB-JWT, so a strict parser reads it as a disclosure that does not decode; the KB-JWT has no `sd_hash` (both external: SD-JWT). Its signature does verify, under the credential's `cnf.jwk`. | EX-22, EX-DU-15 |
| D-15 | Ex 2, 3, 8, 20, 23 | 7 distinct data: URLs are two identical URLs joined by `;` (`data:M,T;data:M,T`), so the data is not one token (18 of the 41 occurrences). The unsecured tabs of 2, 8 and 20 show single URLs. | EX-DU-01, EX-DU-05, EX-DU-08, EX-DU-09, EX-DU-12, EX-DU-13, EX-DU-17 |
| D-16 | Ex 5, 6, 8, 20, 23 | 9 distinct data: URLs contain spaces (after the comma, or before a `~`), which RFC 2397 does not allow (external); the token parses only with them removed. They sit inside signed content in 5, 6, 8, 20 and 23, and in the unsecured tabs of 5 and 8. | EX-DU-03, EX-DU-04, EX-DU-05, EX-DU-11, EX-DU-12, EX-DU-13, EX-DU-17, EX-DU-19, EX-DU-20 |
| D-17 | Ex 20 | the COSE credential is `;base64url,` with one (jose) or two (cose, sd-jwt) base64url layers over the text `base64,0oREo...+Q==`, against R-0051 and RFC 2397; the other enclosed credentials are elided placeholders `eyVjV...RMjU`. | EX-DU-07, EX-DU-10, EX-DU-11, EX-DU-21, EX-20-JOSE, EX-20-COSE, EX-20-SDJWT |
| D-18 | Ex 2, 3, 5, 6, 8, 9, 20 | signed payload and displays disagree: Ex 2's unsecured tab differs from its payload in `@context`, `id` and `type` of the enclosed credential; Ex 3 and 9 sign a `verifiableCredential: []` neither display shows; Ex 5, 6, 8, 20 differ by D-15 to D-17; Ex 20's COSE payload is not its JWS payload. | EX-02-JOSE, EX-03-JOSE, EX-05-SDJWT, EX-06-SDJWT, EX-08-COSE, EX-09-COSE, EX-20-* |
| D-19 | Ex 8, 20, 23 | a presentation encloses credentials secured by another mechanism (the COSE presentations of 8 and 23 enclose SD-JWT; each tab of 20 encloses all three kinds), against the second sentence of R-0023, R-0039 and R-0059. Ex 9 (COSE) encloses an SD-JWT presentation, which those sentences do not cover. | EX-08-COSE, EX-20-*, EX-23 |
| D-20 | Ex 23 | the enclosed credential's media type `application/vc-ld+sd-jwt` is not one of the six 6.1 registers. | EX-DU-17, EX-23 |
| D-21 | every SD-JWT | `type` is selectively disclosable in all 13, counted per enclosing example (the 6 tabs, Ex 21 and 22, and the 5 inside data: URLs, 3 distinct), and members of `credentialSchema` or `credentialStatus` in Ex 4, 18, 19, 21, 22 and in the credentials enclosed in Ex 5, 8 and 23: against R-0031 and R-0040 (SHOULD). In Ex 5 and 20 even the EnvelopedVerifiableCredential `type` is. | every EX-*-SDJWT, EX-21, EX-22 |
| D-22 | every SD-JWT | every `exp` printed is before the Recommendation's date: 2025-05-09 (the six sd-jwt tabs), 2025-01-29 (inside Ex 6 and 9), 2024-10-14 (Ex 21, 22). A verifier checking exp rejects them (RFC 7519 §4.1.4, external). | every EX-*-SDJWT, EX-21, EX-22 |
| D-23 | Ex 24, 25, 26 | not valid diagnostic notation; Ex 26's payload begins `0f be`, so it is not the credential or presentation the sentence after it says it can be; none of the labels 3, 4 or 15 shown in 24 and 25 occurs in any of the 7 real COSE examples. | EX-24, EX-25, EX-26 |
| P-01 | every compact display | an LF precedes each separator in the markup, and the inline styles give the compact displays no white-space rule (the external W3C-REC style sheet was not examined), so under the CSS default each LF renders as a space: the `.txt` rendering shows `eyJ… .eyJ… .xbp…`, and a token copied that way does not parse. The fixtures drop these LFs. | every .jwt and .sd-jwt fixture |
| P-02 | Decoded and Issuer Disclosures tabs | every space in the JSON they print (the Decoded tab, and each Contents of the Issuer Disclosures tab) is U+00A0; the labels (`Claim:`, `SHA-256 Hash:`, `Disclosure(s):`, `Contents:`) use U+0020. So the Decoded tab is not JSON as printed (RFC 8259 §2, external); read with U+0020 it is the 2-space pretty-print of the decoded value. | every EX-*-SDJWT |
| P-03 | Ex 8 | the title reads "secured withCOSE". | EX-08-COSE |

## Signature results

- **Verifies:** the Example 22 KB-JWT, ES384, under key 7 (the `cnf.jwk` in the
  credential it presents), and under no other key.
- **Unverifiable:** the other 28 (25 distinct). The document prints no key for any
  of their kids, and the COSE ones have no kid; every printed key was still tried.
- **Not attempted:** Example 26, whose signature is elided; the X25519 key,
  which cannot verify signatures.

With only the printed keys, then, every secured example ends in status false
under 5.1, 5.2 or 5.3, and the SD-JWT ones are also expired (D-22). The
source states no verification result for any example, so no vector claims one.

## What is not a vector, and why

- **The Credential and Presentation tabs** are fixtures of every tab vector of
  their example (compared with each signed payload); they add no vector.
- **Normative prose that says "for example"** (3, 3.1.3, 5.2, 5.4) names rules,
  not values; those rules are checked where an example exercises them. The one
  value printed in prose, the 4.2 kid, is EX-4.2-P1.
- **Sections with no example:** 1, 2, 4.1, 5 (the algorithms are exercised by
  the expected results), 6 (the IANA templates print no message), 7, and the
  appendices.
- **Not run:** R-0080 (well-formed compact JSON-LD; no JSON-LD processor here),
  and R-0081/R-0083 for Examples 18 and 19 (the schema and status resources are
  at example domains).
- **External rules** (RFC 7518, 7519, 7638, 8259, 8949, 8610, 9052, 9053, 2397,
  SD-JWT) are context for a harness, never this source's statements. RFC 7638
  was fetched once into scratch to recompute its §3.1 example thumbprint
  (D-05); it is not committed.

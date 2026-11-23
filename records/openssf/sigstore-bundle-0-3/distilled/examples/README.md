---
record: sigstore-bundle-0-3
kind: examples
title: "sigstore-bundle-0-3 — examples and test vectors"
extracted: "2026-11-20"
reviewed_by: ""
---

# sigstore-bundle-0-3 — examples and test vectors

The source's examples are the nine fenced code blocks of the docs page §5
(`.cache/sigstore-bundle-0-3.include/bundle.md`, sha256 `8d112700...`). Each is a fixture
cut **by line** from those original bytes, never from the rendering. In the rendering the
page starts at line 872, so a `bundle.md` line N is rendering line N + 871 (verified line by line).
Fixtures are named `*.verbatim.json` when the block is valid JSON as it stands, `*.verbatim.txt` when it is not.

| fixture | page section | bundle.md lines | rendering lines | parses as JSON | note |
|---|---|---|---|---|---|
| `verification-material-certificate.verbatim.txt` | 5.1.1.1.1 | 38-42 | 909-913 | no: a member, parses wrapped in `{}` | placeholders (`<Base64(DER bytes)>`) |
| `verification-material-public-key.verbatim.txt` | 5.1.1.1.2 | 51-55 | 922-926 | no: parses wrapped | placeholder hint |
| `verification-material-tlog-entries.verbatim.txt` | 5.1.1.2 | 66-97 | 937-968 | no, even wrapped | **SD-S-1** trailing commas at L71 and L95; **SD-S-4** `(hashrekord \| dsse)` |
| `verification-material-timestamp.verbatim.txt` | 5.1.1.3 | 105-113 | 976-984 | no, even wrapped | **SD-S-2** trailing comma at L110 |
| `content-message-signature.verbatim.txt` | 5.1.2.1 | 128-134 | 999-1005 | no: parses wrapped | placeholders |
| `content-dsse.verbatim.txt` | 5.1.2.2 | 142-151 | 1013-1022 | no, even wrapped | **SD-S-3** `"dsseEnvelope": { {` (L142-143) |
| `bundle-message-signature.verbatim.json` | 5.1.3.1 | 165-203 | 1036-1074 | yes | complete bundle, Rekor `hashedrekord` 0.0.1, no timestamp |
| `bundle-dsse.verbatim.json` | 5.1.3.2 | 211-265 | 1082-1136 | yes | complete bundle, Rekor `intoto` 0.0.2, RFC 3161 timestamp |
| `embedded-attestation.verbatim.json` | 5.1.3.2 | 271-317 | 1142-1188 | yes | the in-toto Statement printed after the bundle |

Exactly which parse and why not, with the parser's message, is in `fixtures.derived.json`,
and each fixture's first and last line carry `source_lines` + `quote` for `bin/check-quotes`
(a count that includes the rendering line ranges recorded there). **Source defects found here (SD-S-n),
unified in `../normative.md` (Source defects):** SD-S-1, SD-S-2, SD-S-3 are the three blocks that are not JSON
(SD-23); SD-S-4 the misspelled kind placeholder (SD-14); SD-S-5 to SD-S-9 are in `../messages.yaml`
`source_defects`, with locators. SD-S-10 (the intoto body's `content.hash` not reproducible) is withdrawn: the
verify pass reproduced it (table below).
Placeholder blocks (1, 2, 5) also fail the derived schema's base64 patterns on purpose: `<...>` is not base64.

## What `reproduce.py` does (stdlib plus the `openssl` command; 86 checks)

`python3 -I reproduce.py [--write] [--cross]` re-runs `../render-source.py` into a scratch dir and compares the rendering
byte for byte with `.cache/sigstore-bundle-0-3.txt`, re-extracts every fixture with two independent
extractors (a line scanner and a whole-file regex must agree on 9 blocks), compares the fixture files, the index
and the expected-result files, runs the two bundles through every check below and then the schema checker
(251 cases, 337 mutants). Exit 1 on any difference. Eight of the 44 bundle checks (3 of 19 and 5 of 25) are also run on a
damaged copy, a **negative control** that must fail; the expected-results files mark them `negative_control`.

## Expected results for the two complete bundles

`message-signature-bundle.expected.derived.json` and `dsse-bundle.expected.derived.json`. `pass` = verified here; `NOT VERIFIABLE`
= the source does not contain what the check needs.

| check | message-signature (5.1.3.1) | DSSE (5.1.3.2) |
|---|---|---|
| parse; decode every base64 field | pass (19 fields) | pass (8 fields) |
| canonicalizedBody is JSON; apiVersion/kind equal kindVersion | pass (hashedrekord 0.0.1) | pass (intoto 0.0.2) |
| DSSE payload decoded vs the printed attestation block (L271-317) | n/a | **pass: byte-identical**, incl. the final newline (control: without it they differ) |
| messageDigest equals the hashedrekord body hash | pass (sha256 `5be26f17...`) | n/a |
| body binds the same signature and certificate (R-0067) | pass (hashedrekord: signature, PEM publicKey) | pass (intoto: sig and publicKey, **both double-base64**; payloadHash = SHA-256 of the statement) |
| intoto `content.hash` | n/a | **pass**: `c8ef87a3...` is SHA-256 of the sorted, compact JSON of `{payload, payloadType, signatures: [{publicKey, sig}]}`, with payload and sig in the bundle's base64, publicKey the certificate PEM the body carries, and keyid left out because it is empty (control: keeping the empty keyid gives another hash). The source does not state this scheme; pass 1 tried 8 other serialisations and reported it not reproducible (F-S-1, withdrawn) |
| X.509 leaf parsed (own DER reader); P-256 key | pass | pass |
| Fulcio OID extensions 1.3.6.1.4.1.57264.1.N | pass: N = 1-6, 8-22 | pass: N = 1, 8 |
| integratedTime in notBefore..notAfter | pass (18:44:36 in 18:44:34..18:54:34, control: a day later is outside) | pass (00:00:00 = notBefore: the boundary, inclusive) |
| RFC 3161 genTime in validity; messageImprint = SHA-256(DSSE signature) (R-0003) | n/a (no timestamp) | pass (genTime = notBefore, boundary) |
| ECDSA signature, cert key, via `openssl` | pass over messageDigest (control: flipped bit rejected). Analysis only: R-0038 forbids a client using messageDigest to verify | pass over PAE(payloadType, payload) (control: altered payloadType rejected) |
| messageDigest vs the artifact (`sigstore-java-1.0.0.jar`) | **NOT VERIFIABLE**: third-party file, not in the source | n/a |
| checkpoint text: tree size and root hash equal inclusionProof | pass (3775939, `nEpjeg...`) | pass (1, `pc42ie...`; a non-standard extra `Timestamp:` line) |
| checkpoint signature key hint (4 bytes) vs logId.keyId prefix | observation: equal (`c0d23d6a`) | observation: equal (`f726caa3`) |
| checkpoint signature | **NOT VERIFIABLE**: the log key is not in the source | **NOT VERIFIABLE** |
| signedEntryTimestamp | **NOT VERIFIABLE**: same | **NOT VERIFIABLE** |
| RFC 3161 TSA signature | n/a | **NOT VERIFIABLE**: the timestamp carries no certificate, the source none; the signedAttrs messageDigest = SHA-256(TSTInfo) does check |
| Merkle inclusion proof (RFC 9162 2.1.3.2; leaf = SHA-256(0x00 \|\| canonicalizedBody)) | pass (index 3775938 of 3775939, 12 hashes; control: altered leaf rejected) | pass (index 0 of 1, no hashes; control: altered leaf rejected) |
| tlog logIndex vs inclusionProof.logIndex | 125680200 vs 3775938 (different, unrelated by the source) | 4288993 vs 0 |
| derived schema `Bundle` and `BundleV03` accept | pass | pass |
| certificate chain verified to a root | **NOT VERIFIABLE**: issuer `sigstore-intermediate` is not in the bundle | the leaf's issuer is not in the bundle either |

Facts the examples show that the prose does not say: both leaves have an empty subject (`openssl x509`, printed by
`../protocol-evidence.derived.py`), and the first a critical SAN (the second was not inspected for that); the DSSE bundle's `keyid` is `""`; both log entries have a `canonicalizedBody` although it is optional; the
RFC 3161 token is the mock TSA's (`CN=tsa, O=sigstore.mock`) and the DSSE example is a mock-CA, localhost log: it is a test vector,
not a trust-rooted bundle.

---
record: in-toto-attestation-v1
kind: examples
title: "in-toto-attestation-v1 — examples and test vectors"
extracted: "2026-11-09"
reviewed_by: ""
---

# Examples and test vectors

Every example in the 12 files the record reads (rendering
`.cache/in-toto-attestation-v1.txt`, built by `../render-source.py` from
in-toto/attestation @ df02077bf97218a8860a5c534eff1f1381f56984).

```
python3 -I reproduce.py                    # needs the rendering: .cache/ is not in CI
python3 -I reproduce.py --archive DIR      # also compare with the Markdown files and .proto bytes
python3 -I reproduce.py --write-derived    # rewrite the *.derived.* fixtures from vectors.derived.json
```

`reproduce.py` prints how many of each kind it examined. It re-cuts every
`.verbatim.` fixture from the rendering (byte for byte), re-derives every
`.derived.` fixture from its recipe, re-checks every expected result, runs the
schema checker (`../schema/check-schemas.derived.py`, 1403 cases), and exits 1
on any failure. `vectors.derived.json` holds the locators, hashes, recipes and
expected results; it is the single index.

Naming: `*.verbatim.*` is the source's bytes (a code block's content, between
its fences, nothing else); `*.derived.*` is ours (an expansion of an
abbreviated example, or a whole Statement/Envelope built around one). Nothing
here is an example the source does not print, except where a derived fixture
says so.

## Result of reading the examples against the schemas

- The source's JSON examples are **illustrations**, and most do not validate
  as printed: digests are abbreviated (`7f4714fd...`), payloads and signature
  arrays are placeholders (`a...`, `[w...]`). Their expected result below is
  *reject* or *unrecognized*, and a `.derived.` twin with the placeholder made
  valid is *accept*. That is a finding about the source, not a defect in a
  fixture.
- Only **EX-04** (uri-only descriptor) and **EX-05** (Tekton, full) are valid
  descriptors as printed. EX-04 is not a valid Statement subject (no digest,
  DX-06).
- **EX-05**: the printed `digest.sha256` is *not* the sha256 of the decoded
  `content`; the source says only that the digest SHOULD match one of `name`,
  `uri`, `content`, `downloadLocation` and leaves the choice to the predicate
  type. The decoded content is a JSON object with the keys result, timestamp,
  successes, failures, warnings.
- **IN-08** (`{"dirHash1": ...}`): the section defines `dirHash`; the example
  writes `dirHash1`. Under the source's own rule that is a custom algorithm
  name. Source defect; the converted value is correct (EX-11 and the
  arithmetic in `reproduce.py`).
- **EX-09..EX-12** are arithmetic examples: `reproduce.py` recomputes the
  sha256 of the file listing, the dirHash, the base64 `h1:` conversion and the
  gitBlob SHA-1 of the 5 bytes `Hello`.
- `docs/validation.md` has pseudocode but no fixtures. Its OR/AND defect is
  normative.md SD-2 (messages.yaml SD-02, protocol.yaml SD-01).

## Verbatim fixtures (17)

| id | file | § | rendering lines | expected result |
|---|---|---|---|---|
| EX-01 | `rd-pointer-to-file.verbatim.jsonc` | §4.4 | 354-358 | parses as JSONC; resource-descriptor: reject — digest value abbreviated ('7f4714fd...'): not lowercase hex, so a strict DigestSet rejects it; illustrative |
| EX-02 | `rd-pointer-to-git-repo.verbatim.jsonc` | §4.4 | 364-368 | parses as JSONC; resource-descriptor: reject — digest value abbreviated ('d61b27b8395512...'); illustrative |
| EX-03 | `rd-pointer-to-attestation.verbatim.jsonc` | §4.4 | 374-379 | parses as JSONC; resource-descriptor: reject — digest value abbreviated ('abcdabcde...'); leading/trailing spaces are in the source |
| EX-04 | `rd-pointer-to-build-service.verbatim.jsonc` | §4.4 | 385-387 | parses as JSONC; resource-descriptor: accept — uri only: a valid ResourceDescriptor, but NOT a valid Statement subject (no digest) |
| EX-05 | `rd-tekton-taskrun.verbatim.jsonc` | §4.4 | 393-400 | parses as JSONC; resource-descriptor: accept; arithmetic checked — full descriptor; the digest is NOT sha256 of the decoded content (it may be of the resource at uri - the source does not say) |
| EX-06 | `dirhash-command.verbatim.sh` | §5.2.1.2 | 459-459 | none (not an instance) — shell command defining dirHash; not an instance of anything |
| EX-07 | `dirhash-gomodule-lookup.verbatim.sh` | §5.2.1.2 | 473-476 | none (not an instance) — transcript of a go module lookup; the h1: value is converted to dirHash hex in EX-11 |
| EX-08 | `dirhash-fetch-module.verbatim.sh` | §5.2.1.2 | 483-486 | none (not an instance) — shell commands; not an instance |
| EX-09 | `dirhash-file-listing.verbatim.sh` | §5.2.1.2 | 493-496 | arithmetic checked — per-file sha256 listing; its sha256 is the dirHash (EX-10) |
| EX-10 | `dirhash-final.verbatim.sh` | §5.2.1.2 | 502-503 | arithmetic checked — output of the dirHash pipeline: 2a1bb6...cb8f |
| EX-11 | `dirhash-h1-conversion.verbatim.sh` | §5.2.1.2 | 509-510 | arithmetic checked — hex -> base64 gives the h1: value in EX-07 |
| EX-12 | `gitblob-hello.verbatim.sh` | §5.2.1.3 | 541-544 | arithmetic checked — gitBlob of the 5 bytes 'Hello' = 5ab2f8a4... |
| EX-13 | `bundle-fooly-build.verbatim.jsonl` | §9.4.1 | 931-932 | bundle lines recognized/unrecognized/unparseable = 0/0/2 — JSON Lines with the placeholders a... and [w...]: not valid JSON, so every line is unparseable; illustrative |
| EX-14 | `bundle-fooly-vulnscan.verbatim.jsonl` | §9.4.2 | 947-949 | bundle lines recognized/unrecognized/unparseable = 0/0/3 — as EX-13, three lines |
| EX-15 | `bundle-fooly-sbom.verbatim.jsonl` | §9.4.3 | 960-963 | bundle lines recognized/unrecognized/unparseable = 0/0/4 — as EX-13, four lines |
| EX-16 | `bundle-fooly-publish.verbatim.jsonl` | §9.4.5 | 984-986 | bundle lines recognized/unrecognized/unparseable = 0/0/3 — as EX-13, three lines |
| EX-17 | `bundle-jq-view.verbatim.sh` | §9.5 | 998-1018 | JSON stream objects recognized/unrecognized/other = 0/4/0 — jq-pretty-printed objects; payload 'a...' is not base64, so all four objects are unrecognized lines under the strict schema |

## Derived fixtures (12)

| id | file | from | expected result | note |
|---|---|---|---|---|
| DX-01 | `rd-pointer-to-file.expanded.derived.jsonc` | EX-01 | resource-descriptor: accept; digest-set-lengths: accept at digest | EX-01 with the abbreviated digest padded to 64 hex |
| DX-02 | `rd-pointer-to-git-repo.expanded.derived.jsonc` | EX-02 | resource-descriptor: accept; digest-set-lengths: accept at digest | EX-02 with the sha1 padded to 40 hex |
| DX-03 | `rd-pointer-to-attestation.expanded.derived.jsonc` | EX-03 | resource-descriptor: accept; digest-set-lengths: accept at digest | EX-03 with the sha256 padded to 64 hex |
| DX-04 | `statement-tekton.derived.json` | EX-05 | statement: accept | EX-05 as the subject of a Statement; predicateType is a placeholder, not from the source |
| DX-05 | `envelope-tekton.derived.json` | DX-04 | envelope: accept; payload decodes to a valid Statement | DX-04 serialized, base64 as payload, in a DSSE-shaped envelope with a dummy signature |
| DX-06 | `statement-build-service-subject.derived.json` | EX-04 | statement: reject | EX-04 (uri only) as a subject: a Statement subject MUST have digest |
| DX-07 | `statement-pointer-to-file.derived.json` | DX-01 | statement: accept | DX-01 as a Statement subject |
| DX-08 | `bundle-fooly-build.instantiated.derived.jsonl` | EX-13 | bundle lines recognized/unrecognized/unparseable = 2/0/0 | EX-13 with placeholders replaced by valid base64 payloads and one-entry signature arrays |
| DX-09 | `bundle-fooly-vulnscan.instantiated.derived.jsonl` | EX-14 | bundle lines recognized/unrecognized/unparseable = 3/0/0 | EX-14 with placeholders replaced by valid base64 payloads and one-entry signature arrays |
| DX-10 | `bundle-fooly-sbom.instantiated.derived.jsonl` | EX-15 | bundle lines recognized/unrecognized/unparseable = 4/0/0 | EX-15 with placeholders replaced by valid base64 payloads and one-entry signature arrays |
| DX-11 | `bundle-fooly-publish.instantiated.derived.jsonl` | EX-16 | bundle lines recognized/unrecognized/unparseable = 3/0/0 | EX-16 with placeholders replaced by valid base64 payloads and one-entry signature arrays |
| DX-12 | `bundle-jq-view.instantiated.derived.sh` | EX-17 | JSON stream objects recognized/unrecognized/other = 4/0/0 | EX-17 with payload placeholders replaced by valid base64; signatures [] kept |

`bundle-fooly-*.instantiated`, `bundle-jq-view.instantiated`: the JSON-Lines examples with each placeholder replaced by a valid base64 payload and a one-entry signature array (jq-view keeps `[]`).

## Inline examples (22): no file, checked in `vectors.derived.json`

Each is a quotation inside one rendering line; `reproduce.py` asserts the quotation occurs in the cited line (and how often it occurs in the rendering).

| id | § | line | example | expected |
|---|---|---|---|---|
| IN-01 | §6.1 | 655 | `"pkg:deb/debian/stunnel@5.50-3?arch=amd64"` | field-types: accept |
| IN-02 | §6.2 | 676 | `"https://in-toto.io/Statement/v1"` | field-types: accept |
| IN-03 | §6.3 | 689 | `"1985-04-12T23:20:50.52Z"` | field-types: accept |
| IN-04 | §5.3 | 601 | `{"sha256": "abcd", "sha512": "1234"}` matches `{"sha256": "abcd"}` | dsmatch; digest-set: accept |
| IN-05 | §5.3 | 602 | `{"sha256": "abcd"}` does not match `{"sha256": "fedb", "sha512": "abcd"}` | dsmatch; digest-set: accept |
| IN-06 | §5.3 | 603 | `{"somecoolhash": "abcd"}` uses a non-predefined algorithm | digest-set: accept; stdname |
| IN-07 | §5.3 | 604 | `{"arn": "arn:aws:ec2:region:123:image/ami-123abcd"}` | digest-set: accept; statement: accept |
| IN-08 | §5.2.1.2 | 464 | `{"dirHash1": "2a1bb6127fb481c60f67692e22285fb306f3c6ffe62075e0ccf674d7c3adcb8f"}` | digest-set: accept; stdname — SOURCE DEFECT: the example key dirHash1 is not the standard name dirHash defined in the same section |
| IN-09 | §8.4.1 | 834 | `application/vnd.in-toto.provenance+dsse` | pattern; envelope: reject — a storage media type, not an Envelope payloadType |
| IN-10 | §8.4.1 | 835 | `application/vnd.in-toto.spdx+dsse` | pattern; envelope: reject — a storage media type, not an Envelope payloadType |
| IN-11 | §8.4.1 | 836 | `application/vnd.in-toto.vsa+dsse` | pattern; envelope: reject — a storage media type, not an Envelope payloadType |
| IN-12 | §9.3 | 903 | `application/vnd.in-toto.bundle` | pattern |
| IN-13 | §8.3 | 807 | `<step-name>.json` | pattern — template; instantiated as build.json |
| IN-14 | §8.3 | 810 | `<env-name>.json` | pattern — template |
| IN-15 | §8.3 | 814 | `<step/env-name>.<keyid[0:8]>.json` | pattern — template; <keyid[0:8]> is the first 8 characters of the keyid |
| IN-16 | §9.2 | 891 | `<filename>.intoto.jsonl` | pattern — template |
| IN-17 | §9.2.1 | 898 | `foo-1.2.3.tar.gz.intoto.jsonl` | pattern |
| IN-18 | §9.4.1 | 928 | `fooly.apk.intoto.jsonl`. | pattern |
| IN-19 | §1.1.1 | 59 | `https://in-toto.io/Statement/v2` | statement: reject; field-types: accept — a v2 Statement is a valid TypeURI but not a v1 Statement |
| IN-20 | §11.3 | 1101 | `https://slsa.dev/provenance/v1` | field-types: accept |
| IN-21 | §9.4.1 | 926 | `predicateType=https://fooly.app/Builder/v1` | field-types: accept |
| IN-22 | §9.4.3 | 956 | `predicateType=https://spdx.dev/Document` | field-types: accept |

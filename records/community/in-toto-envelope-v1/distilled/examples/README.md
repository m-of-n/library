---
record: in-toto-envelope-v1
kind: examples
title: "in-toto-envelope-v1 — examples and test vectors"
extracted: "2026-11-16"
reviewed_by: ""
---

# in-toto-envelope-v1 — examples and test vectors

The source has **no code block and no figure**. Its examples are three media
types in §4.1 (lines 94-96). They are the three **verbatim** fixtures; the
source states no expected verification result (it states no vector at all), so
`expected` in `index.yaml` is what `schema/envelope.derived.schema.json` says,
and is derived.

| file | what | provenance |
|---|---|---|
| `media-type-slsa-provenance.verbatim.txt` | `application/vnd.in-toto.provenance+dsse`, no trailing newline | **verbatim**, line 94 |
| `media-type-spdx.verbatim.txt` | `application/vnd.in-toto.spdx+dsse` | **verbatim**, line 95 |
| `media-type-vsa.verbatim.txt` | `application/vnd.in-toto.vsa+dsse` | **verbatim**, line 96 |
| `index.yaml` | per fixture: line, quote (checked by `bin/check-quotes`), sha256, expected result (valid `StorageMediaType`: yes; valid DSSE `payloadType`: no, a storage type is not a payloadType); also the four other backticked media-type spans of the source and why they are not examples | written by `reproduce.py --write` |
| `cases.derived.json` | 93 accept/reject instances for the schema: minimal DSSE envelopes, generic envelopes, bad media types and file names, payload content faults. **DERIVED, written by this library, never presented as source.** `basis` says which are the source's and which are ours | derived |
| `reproduce.py` | re-extracts the fixtures from `.cache/in-toto-envelope-v1.bin` (sha256 checked) with two independent extractors, compares bytes, rebuilds `index.yaml`, checks that every id the cases cite exists, then runs `../schema/check-envelope.derived.py` | `python3 -I reproduce.py` |

Embedded Statements in the derived cases use placeholder values
(`urn:example:...`). The source does not define the value of `_type`.

---
record: secure-systems-lab-dsse
kind: examples
title: "secure-systems-lab-dsse — examples and test vectors"
extracted: "2026-11-20"
reviewed_by: ""
---

# secure-systems-lab-dsse — examples and test vectors

The source has **one test vector**: protocol.md 1.4 (rendering lines 146-180) —
a body, a type, the PAE, an ECDSA P-256 / RFC 6979 key and the signed JSON
envelope. It has two envelope templates (envelope.md 2.1, 2.1.1) and, in the
attack notebook, four narrative blocks. Every one of the 13 fenced blocks of the
source is a fixture. Every `*.verbatim.*` file is cut by `reproduce.py` from the
pinned archive and compared with a second, independent extractor; nothing else
is named verbatim.

**Convention.** A fixture is the content lines between the fences joined by LF,
**no final newline**, the opening fence's indentation removed. The no-newline
reading is proved, not assumed: PAE with `hello world` (11 bytes) equals the
printed PAE line, and the printed signature verifies over that PAE and over no
variant with a newline (`reproduce.py` check e).

| file | what | provenance |
|---|---|---|
| `signature-formula.verbatim.txt`, `pae-definition.verbatim.txt` | `SIGNATURE = Sign(PAE(...))` (line 19); the PAE definition block (lines 64-68), the source of `../schema/pae.derived.abnf` | verbatim; definitions, not vectors |
| `serialized-body.verbatim.txt`, `payload-type.verbatim.txt`, `pae.verbatim.txt` | `hello world` (11 bytes), `http://example.com/HelloWorld` (29 bytes), the printed PAE line (54 bytes) | verbatim, lines 149, 155, 161 |
| `keys.verbatim.txt` | algorithm, signature encoding, and X, Y, d as decimal integers | verbatim, lines 167-171 |
| `result-envelope.verbatim.json` | the signed JSON envelope | verbatim, lines 177-179 |
| `envelope-template.verbatim.json`, `envelope-template-multi.verbatim.json` | the §2.1 and §2.1.1 templates with `<...>` placeholders. **Expected: not valid envelopes as-is**: the `payload` and `sig` placeholders (`<Base64(SERIALIZED_BODY)>`, `<Base64(SIGNATURE)>`, `<SIG_n>`) are not base64 (they contain `<` and `>`); the `payloadType` and `keyid` placeholders are legal strings. Valid as a shape | verbatim, lines 211-218, 233-243 |
| `notebook-*.verbatim.*` (4) | the legitimate and the forged in-toto link file, the CBOR diagram, the crafted build-command shape, from the 2020 attack notebook. **Not DSSE vectors**: a pre-DSSE wrapper, no PAE | verbatim, lines 568-573, 579-584, 1058-1063, 1082 |
| `pae-section-1-4.derived.hex` | the 54-byte PAE in hex (`44535345763120…`) | **derived**, recomputed by script |
| `pae-vectors.derived.json` | 17 build vectors (the §1.4 one as PAE-V00; empty type and body; multi-byte UTF-8 types; body lengths 9, 10, 99, 100, 1000; 0x20 inside the type; binary body; a trailing-newline body) with hand-typed expected bytes, and 19 byte strings the grammar must reject | **derived**; PAE-V00 is the source's |
| `cases.derived.json` | 61 accept/reject instances for `../schema/envelope.derived.schema.json` | **derived** |
| `index.yaml` | per fixture: `source_lines` + `quote` (checked by `bin/check-quotes`), sha256, byte length, expected result | written by `reproduce.py --write` |
| `reproduce.py` | the checks below | `python3 -I -B reproduce.py` |

## What `reproduce.py` proves about the §1.4 vector

PAE recomputed two ways equals the printed line byte for byte; `d·G == (X, Y)`
and (X, Y) is on P-256; the printed `sig` is 64 bytes `r||s`, verifies over the
PAE, and **equals the RFC 6979 deterministic signature recomputed from d**; the
payload base64-decodes to `hello world`. The ECDSA / RFC 6979 code (stdlib
integers) first reproduces RFC 6979 Appendix A.2.5 (SHA-256, "sample" and
"test": k, r, s). Negatives that must fail (19, the count `reproduce.py` prints): signature over
the bare body, a changed type, a changed body, a body with a trailing newline,
the printed PAE line with a trailing newline, an empty type, the PAE of the
base64 text, type and body swapped, version `DSSEv2`, four flipped signature
bits, the wrong key, r and s swapped, r = 0, s = 0, r = n, an off-curve key.

Observations (not source claims): the printed signature is low-s; the printed
vector is standard-alphabet base64 (`+` appears, no `-` or `_`), padded.

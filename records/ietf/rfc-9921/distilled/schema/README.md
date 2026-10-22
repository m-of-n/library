---
record: rfc-9921
kind: schema
title: "rfc-9921 — schemas"
extracted: "2026-10-20"
reviewed_by: ""
---

# Schemas

**RFC 9921 ships no formal grammar of any kind.** Measured over all 1056 lines
of `.cache/rfc-9921.txt`, whole-word and case-insensitive: `CDDL` **0**,
`ABNF` **0**, `ASN.1` **0**, `JSON Schema` **0**, `schema` **0**, `grammar`
**0**. `canonical` and `deterministic` are **0** as well. So this directory is
one verbatim capture and four derived files, and the split is the finding: a
document that adds two parameters to a CBOR envelope format states their syntax
in two English sentences and a six-column table.

| file | kind | what it is |
|---|---|---|
| `source-renderings.txt` | **verbatim** | the twelve places the document renders a structure by printing it — §6's Table 1, **six** ASN.1 value dumps, **three** CBOR diagnostic objects and **two** byte listings, counted by the file's own per-region captions and corrected by pass 2 from "four … and four" — as exact runs of source lines, each with its line range and its own `sha256` |
| `cose-headers.derived.cddl` | derived | the two labels, the opaque value, the two bucket constraints, and the three imprint preimages written out octet by octet |
| `header-parameters.derived.yaml` | derived | §6's two registrations as data, reassembled from the column-wrapped table |
| `timestamp-token.derived.outline.txt` | derived | what the 5453 octets actually contain, produced by **decoding** Appendix A.1's hex with a DER parser written for this pass |
| `cose-headers.derived.schema.json` | derived | a JSON projection, `$id: urn:library:rfc-9921:cose-headers.derived` |

## Why the reassembly in `header-parameters.derived.yaml` is derived

Table 1's rows are **column-wrapped across five source lines each**, so no
single cell — not even `3161-ttc` — is a contiguous span of the
whitespace-normalised source. A quotation of a cell would be a splice. The
verbatim table is in `source-renderings.txt` with its digest; the cell values
are reassembled in the YAML and the reassembly is this library's.
`requirements.yaml` quotes each row as **the row's own column-wrapped lines**
(R-0091 to R-0093), which is ugly and verbatim, rather than readable and
invented.

## What no schema here can check

The 5453 octets inside the byte string. §3.1 and §3.2 give the value as *"a
DER-encoded TST [RFC3161] wrapped in a CBOR byte string (Major type 2)"* and
§6 gives **Value Registry `-`**. A CDDL or JSON Schema validator that accepts
either parameter has established that the value is a byte string and nothing
else. `timestamp-token.derived.outline.txt` is this library's answer to that —
not a schema, a **measurement** of one instance — and it exists because an
implementer otherwise has to acquire RFC 5652 and RFC 3161 to learn what the
field holds. **Neither is in this library.**

## The JSON projection, and why it is thin

RFC 9921 defines no JSON form, so the projection in
`cose-headers.derived.schema.json` is ours: labels as decimal-string object
keys, values as lower-case base16. It encodes two real constraints —
`3161-ttc` only in `protected`, `3161-ctt` only in `unprotected` — and refuses
the other placement with `not: {required: [...]}`. That is the whole of what is
checkable, and it is checkable only because §3.1 and §3.2 each spend a MUST on
the bucket.

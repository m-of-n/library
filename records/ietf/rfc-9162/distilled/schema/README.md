---
record: rfc-9162
kind: schema
title: "rfc-9162 — schemas"
extracted: "2026-11-07"
reviewed_by: ""
---

# Schemas

RFC 9162 ships **no CDDL and no JSON Schema**. It has three formal notations, and
the filename says which files are the RFC's and which are ours.

## Verbatim (copied from the source)

| file | source | content |
|---|---|---|
| `tls-structures.verbatim.txt` | §4.4, §4.5, §4.6, §4.7, §4.8, §4.9, §4.10, §4.11, §4.12, §6.3 (the ten `<sourcecode type="tls-presentation">` blocks, L953, L971-995, L1019-1026, L1048-1055, L1090-1095, L1121-1128, L1164-1168, L1189-1194, L1212-1217, L1796-1800) | every enum, struct and vector of the wire format, in the TLS presentation language of RFC 8446 §3 (RFC 9162 §1.2) |
| `rfc-9162-01.verbatim.asn1` | §7.1, L1864 | `TransparencyInformationSyntax ::= OCTET STRING` |
| `rfc-9162-02.verbatim.asn1` | Appendix B, L2852-2928 | the informative ASN.1 module `CertificateTransparencyV2Module-2021` |

Each block is the source lines named in its locator with the 3-column RFC margin
removed and nothing else changed (checked byte-for-byte against `.cache/rfc-9162.txt`).
The prose around the blocks is in `../normative.md`; the field-by-field reading is in
`../messages.yaml`.

`bin/fx1-skeleton` headed the Appendix B module "Appendix A". The module is Appendix B
(Appendix A is the v1/v2 coexistence text); the fixture header here says Appendix B
(`messages.yaml` SD-08).

## Derived (written by this library from §5 prose)

§5 gives the JSON API bodies only as prose. Each file below is a JSON Schema
(2020-12) for **one** message, `$id: urn:library:rfc-9162:<name>.derived`. A GET query
is validated as the decoded query string, a JSON object whose values are strings.

| file | message | source |
|---|---|---|
| `submit-entry-request.derived.schema.json` | POST body | §5.1 |
| `submit-entry-response.derived.schema.json` | 2xx body | §5.1 |
| `get-sth-response.derived.schema.json` | 2xx body | §5.2 |
| `get-sth-consistency-query.derived.schema.json`, `get-sth-consistency-response.derived.schema.json` | query / 2xx body | §5.3 |
| `get-proof-by-hash-query.derived.schema.json`, `get-proof-by-hash-response.derived.schema.json` | query / 2xx body | §5.4 |
| `get-all-by-hash-query.derived.schema.json`, `get-all-by-hash-response.derived.schema.json` | query / 2xx body | §5.5 |
| `get-entries-query.derived.schema.json`, `get-entries-response.derived.schema.json` | query / 2xx body | §5.6 |
| `get-anchors-response.derived.schema.json` | 2xx body | §5.7 |
| `error-response.derived.schema.json` | 4xx/5xx body (RFC 7807 problem details) | §5 |

What a schema **cannot** say is in `../messages.yaml` (`constrained_by` and notes per
field): start <= end, tree_size_1 equal to `first`, the TransItem body and its
signature, and which error token an endpoint may return.

### Readings the source forces (each is marked inferred in the schema header)

- **`type` of submit-entry is 1 or 2**, as §5.1 and the `badType` text print it, though
  §4.5 gives x509_entry_v2 the value 0x0100 (SD-01).
- **get-entries `sth`.** The Outputs list indents `sth` inside each `entries` object,
  yet §5.6 says the log MUST return the latest STH "In any case", including for an
  empty `entries` array. The schema requires a top-level `sth` and allows a per-entry
  one (SD-04).
- **get-anchors `max_chain_length`** is "in decimal"; the schema accepts a JSON number
  or a decimal string (SD-05).
- **`{}` for get-all-by-hash** when no Table 5 case is true ("an empty response").
- **Error `type`** admits any alphabetic token after `urn:ietf:params:trans:error:`
  because the Error Types registry can grow; the 14 standard tokens (Table 18: the
  generic `malformed` and the 13 endpoint-specific ones) are in `$defs.standardToken`.
- **TransItem prefix patterns.** A TransItem field is base64 whose first two decoded
  octets are the VersionedTransType (0x01 0xTT); the pattern `^AQ[...]` binds exactly
  the codes the field may carry (entry 0x0100-0x0101, SCT 0x0102-0x0103, STH 0x0104,
  consistency 0x0105, inclusion 0x0106). The check below probes every two-octet code.
  The patterns describe what a v2 log emits and are **not a client acceptance test**: a v2
  client MUST NOT construe a non-v2 SCT (§5.1, rfc-9162#R-0069) or an unrecognized TransItem
  type (§5.6, rfc-9162#R-0079) as an error, so a client that rejected a response on a prefix
  mismatch (the MUST-REJECT case `sct is a v1-range type 0x0001`, for one) would break them.

## Do the schemas reject what they must?

`check-schemas.derived.py` (stdlib only; there is no `jsonschema` in this library)
runs every schema against `schema-tests.derived.json`, against
`../examples/api-samples.derived.json`, and the verbatim error body
`../examples/ex-10.verbatim.json` against `error-response` (the last added by pass 3, which
found the examples README claiming that acceptance with no check behind it):

```sh
python3 -I records/ietf/rfc-9162/distilled/schema/check-schemas.derived.py
```

Result when written: 13 schemas, **28 instances that must be accepted and 169 that must
be rejected**, 9 samples accepted (the 8 in api-samples.derived.json and ex-10), 2 752 512 prefix probes over 14 definitions, 0
failures. The validator implements only the keywords these schemas use and **raises on
any other keyword**, so an unsupported keyword cannot silently constrain nothing.

Mutation check (done once, not kept): weakening five schemas in a copy — dropping a
`required`, the `dependentRequired`, the `anyOf`, a TransItem prefix pattern and the
error `type` pattern — made `check-schemas.derived.py` report 9 failures, so the reject cases bind.

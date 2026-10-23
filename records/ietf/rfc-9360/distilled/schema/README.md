---
record: rfc-9360
kind: schema-index
title: "rfc-9360 — schema artifacts"
extracted: "2026-10-20"
reviewed_by: ""
---

# `distilled/schema/` — RFC 9360

**RFC 9360 ships two lines of CDDL and nothing else.** Measured over all 614
lines: `ABNF`, `ASN.1`, `JSON Schema`, `schema` and `grammar` occur **zero**
times; `CDDL` occurs twice (line 308's lead-in and the RFC 8610 reference at
line 589); `syntax` occurs once, inside a reference title. So the two files
below with no `.derived.` infix are the complete set of structures the document
renders, and everything else here is ours.

| file | kind | what it is |
|---|---|---|
| `cose-x509.cddl` | **verbatim** | source lines 311–312, byte for byte, with the source's three-column margin. The whole wire format of RFC 9360 |
| `source-renderings.txt` | **verbatim** | Table 1, the CDDL block with the DER sentence, Table 2, and the §4.3 media-type template — 4 regions, each with its line range and sha256 |
| `x5-headers.derived.cddl` | derived | the grammar the document does not ship: the four labels and three algorithm-scoped labels as header-map entries, plus this library's narrowing |
| `x5t-hashalg-policy.derived.yaml` | derived | all eight of `rfc-9054`'s hash identifiers with a per-value PERMIT/REFUSE verdict for the binding position |
| `cose-cert-hash.derived.schema.json` | derived | `$id: urn:library:rfc-9360:cose-cert-hash.derived`; a JSON projection for fixture validation only |
| `cddl-parse.derived.txt` | derived | the output of running RFC 8610 Appendix B's grammar against this document's CDDL |

## What the parse check established

A recursive-descent parser for RFC 8610 Appendix B's grammar was written for
this pass, transcribed production for production from
`records/ietf/rfc-8610/distilled/schema/cddl-dedented.derived.abnf` and gated
first on RFC 8610's own 40-rule prelude and on three deliberate negatives.

1. **Both of RFC 9360's rules parse as printed**, with the indentation intact —
   CDDL whitespace is free-form (`S = *WS`), unlike ABNF's continuation rule.
   That is why this directory has no `*-dedented.derived.cddl` and
   `rfc-8610`'s does.
2. **Both parse as *type* rules**, so both are usable as the root of a model.
   Contrast `rfc-9054`'s `COSE_Hash_V`, which can only be parsed as a group and
   which RFC 8610 §2.2.4 therefore forbids as a root —
   `records/ietf/rfc-9054/distilled/schema/cddl-parse.derived.txt` has that.
3. **The `2*` is a choice, not a necessity.** `X = bstr / [ 1*certs: bstr ]`
   parses too, so RFC 9360 could have admitted the one-element array and
   deliberately did not: one certificate has exactly one encoding.
4. **`certs`, `hashAlg` and `hashValue` are bareword member keys, not
   undefined type names.** The report's own "undefined names" list over-reports
   them, because a member key is first tried as a `type1` and the reference is
   logged before the parse backtracks; the report says so.

## What no schema here can check, and why that is the finding

Four things, three of them carried as comments in
`x5-headers.derived.cddl` and as conditions in `../messages.yaml`:

- **that the `bstr` holds DER.** The content is ASN.1, so even CDDL's `.cbor`
  control operator would be wrong. This is the `DEC-002` cut: a reduced-CBOR
  profile does not reach inside a byte string.
- that −27/−28/−29 mean anything only under five named algorithms — IANA's
  *(algorithm, label)* scoping, which CDDL cannot express;
- that the end-entity certificate is integrity protected, which is a property
  of the whole COSE object rather than of a header;
- which `hashAlg` values are fit for the position — that is
  `x5t-hashalg-policy.derived.yaml`, and it exists because the wire format
  cannot carry the distinction `rfc-9054`'s registry draws.

**A fifth item was on this list until pass 3 and did not belong:** *that label
34 carries a `COSE_CertHash`*. **RFC 9360** does not say it in a grammar — the
labels are in a prose table — but **CDDL** can, and `x5-headers.derived.cddl`
exists to say it. What the grammar needed was RFC 8610 §3.5.4's **cut**: an
optional entry followed by a `* label => any` wildcard binds nothing, because
the wildcard matches the member the optional entry rejected. §3.5.4's own
worked example says of `{ "optional-key": "nonsense" }` that it *"does match
this specification"*. `x5-headers.derived.cddl` carried that shape through
passes 1 and 2, so `{ 34: "nonsense" }` matched `x5-signature-header`; pass 3
added `^ =>` to each x5 entry, re-parsed the file (whole-input parse, same
twelve rules, same kinds) and corrected this list and
`cddl-parse.derived.txt`.

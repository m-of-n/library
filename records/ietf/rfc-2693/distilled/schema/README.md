---
record: rfc-2693
kind: schema
title: "rfc-2693 — schemas"
extracted: "2026-10-11"
reviewed_by: ""
---

# RFC 2693 — schemas

## RFC 2693 prints no formal grammar

**RFC 2693 contains no ABNF, no ASN.1, no CDDL, no JSON Schema and no BNF.**
That is a property of the document, not a gap in this extraction, and the
Abstract says so: *"This document gives the theory behind SPKI certificates
and ACLs without going into technical detail about those structures or their
uses."* The concrete S-expression structure is deferred to what §5.7.2 calls
*"the SPKI structure definition"* — `draft-ietf-spki-cert-structure`, a
separate record — and the key-usage tags to *"the examples document"* (§6.5.7).

What the source does print, it prints in five informal notations:

- **numbered definition lists**: the 5-tuple (§6.1), the Name 4-tuple (§6.2),
  the three input entity kinds (§6), the timed-CRL conditions (§5.2);
- **S-expression templates with `<placeholders>`**: the `*`-forms (§6.3.1),
  the fully qualified X.509 names (§2.9);
- **tuple and arrow notation**: `<I1,S1,D1,A1,V1> + <I2,S2,D2,A2,V2>` (§6.3),
  `[(name K1 N) -> K2]` (§6.4), `[Kroot, (name <leaf-name>), K1, validity]`
  (§6.5.1);
- **glossary definitions** (§1.1);
- **concrete examples**, which for several forms are the only evidence of
  their shape: `(hash …)`, `(tag …)`, `(k-of-n …)`.

So this directory holds two kinds of file. The **verbatim** files hold those
passages byte for byte, with digests, and nothing else. The **derived** file is
ours: a JSON Schema that renders the structures machine-checkably, every
production tied to the source sentences it encodes. Nothing in the derived file
may be quoted as RFC 2693's own schema.

## Files

| file | kind | covers | regions · source lines |
|---|---|---|---|
| `names.verbatim.txt` | **verbatim** | SDSI names (basic, compound, fully qualified); the X.509 fully-qualified-name templates; a key as an identifier; group names | 7 · §2.6.1–2.6.2 539–555; §2.7 587–594; §2.8 604–611, 623–634; §2.9 638–653; §2.10 657–659; §7.3 1867–1883 |
| `subjects.verbatim.txt` | **verbatim** | principals; the Subject alternatives; the threshold (`k-of-n`) subject and its reduction form; a hash as a subject | 8 · §1.1 219–221, 235–238, 245–252; §6.3.3 1498–1510; §6.4.1 1583–1592; §7.5 1938–1949; §7.7 2000–2013, 2023–2038 |
| `tags.verbatim.txt` | **verbatim** | the authorization (tag) language: what an authorization is, the `*`-form templates, the tag forms of §6.3.1, §6.5.3 and §6.5.7 | 8 · §6.3.1 1356–1368, 1370–1389, 1391–1398, 1407–1428, 1430–1452; §6.5.3 1649–1661; §6.5.7 1695–1729, 1743–1778 |
| `tuples.verbatim.txt` | **verbatim** | the scope statement; glossary ACL, CERTIFICATE, ISSUER, S-EXPRESSION; the ACL entry; boolean delegation; the input kinds; the 5-tuple and 4-tuple; the reduction notation; the name 4-tuple classes; the certificate translations | 21 · Abstract 37–51; §1.1 192–212, 240–243; §3.4 793–809; §4.1.4 867–870; §6 1205–1213, 1249–1260; §6.1 1264–1286, 1295–1298; §6.2 1302–1320; §6.3 1324–1340, 1351–1352; §6.4 1537–1562, 1575–1579; §6.4.2 1596–1602; §6.5.1 1613–1621, 1631–1634; §6.5.2 1638–1645; §6.5.4 1665–1671; §6.5.5 1675; §6.5.6 1689–1691 |
| `validity.verbatim.txt` | **verbatim** | validity dates and conditions; the online tests; timed CRLs, delta-CRLs and revalidations; the one-time revalidation; the ruled-out anti-matter CRL; VIntersect; where the source counts the online-test kinds | 13 · §5 976–987; §5.1 1015–1038; §5.2 1042–1062, 1071–1076; §5.3 1080–1087; §5.4 1091–1100; §5.5 1108–1115, 1127–1133; §5.6 1147–1149; §5.7.2 1190–1194; §6 1221–1223; §6.3.2 1465–1494; §7 1817–1825 |
| `spki-theory.derived.schema.json` | **derived** | JSON Schema 2020-12: 63 productions covering every structure above, plus one findings entry (`NOT-EXPRESSIBLE`) | §1.1, §2.6.1–2.10, §3.4, §4.1.4, §5–5.6, §5.7.2, §6–6.5.7, §7, §7.3, §7.5, §7.7 |

Every verbatim file opens with a header giving the locator, the source digest
(`6822d668195c3d9b391f0c4f2b023341ba0e5a72e59d63c366a520de42c99098`) and the
digest convention. Then come its regions, each with an id (`V-NAM-01` …), its
section, its line range and its own sha256, between `---- BEGIN VERBATIM <id>
----` and `---- END VERBATIM <id> ----`. A region's digest covers the bytes
between its marker lines — the source lines with their line feeds — exactly as
in `rfc-9804`'s schema files. **No region crosses a page break.** A passage
that does is split into two regions; V-TAG-03/V-TAG-04, for instance, is one
§6.3.1 sentence broken by the page 25/26 boundary. So no region contains a page
footer, a form feed or a running header. The files were generated from the
cached source by script, not typed.

Naming: `.derived.` follows `rfc-8949`'s convention, and `.verbatim.` marks the
other kind the same way. Each file also says what it is in its first lines.

## Using the derived schema

**Two levels.**

1. *S-expression forms the source prints*: the names, `(hash …)`, `(tag …)`
   and the `*`-forms, `(k-of-n …)`, `(null)`. They are validated as JSON
   under the mapping below.
2. *Abstract records the source defines by enumeration but never encodes*: the
   5-tuple, the Name 4-tuple, validity, the online tests and the instruments
   they fetch, the certificate bodies, the ACL entry. Their JSON shape (array
   positions for the tuples, member names for the rest) is this project's
   rendering of the enumerated elements. Member names are the source's element
   names wherever it has them.

**The mapping (project convention, not from RFC 2693).** An S-expression list
becomes a JSON array, in order. An octet string becomes a JSON string of the
same length whose *i*-th character is the code point equal to the *i*-th octet
(U+0000–U+00FF, i.e. ISO-8859-1 decoding). So printable atoms map to
themselves, `#03#` becomes `"\u0003"`, and `|TLCgPLFlGTzgUbcaYLW8kGTEnUk=|`
becomes a 20-character string. This is a bijection on S-expressions without
display hints, and the source prints none. Example:

```
(tag (* range numeric ge #30# le #39# ))
  =>  ["tag", ["*", "range", "numeric", "ge", "0", "le", "9"]]
```

**Roots.** The schema root is `five-tuple` (§6.1). Validate anything else by
reference to its entry, e.g. `{"$ref":
"spki-theory.derived.schema.json#/$defs/tag"}`. Sixteen entries are referenced
by nothing else and are meant as roots in their own right:

- the certificate and ACL records: `acl`, `authorization-certificate-body`,
  `name-certificate-body`;
- the validity instruments: `current-crl`, `timed-revalidation`,
  `one-time-revalidation-request`, `one-time-revalidation`;
- the threshold reduction form: `threshold-subordinate-tuples`;
- the name refinements: `basic-sdsi-name`, `compound-sdsi-name`,
  `fully-qualified-x509-name`;
- the tuple refinements: `four-tuple-defining-key`,
  `four-tuple-defining-name`, and the three `entity-*` refinements of §6's
  input kinds.

The seventeenth unreferenced entry, `NOT-EXPRESSIBLE`, holds findings and is
not a schema (`"not": {}`).

**Open and closed.** The tuples and `tuple-validity` are closed, because §6.1
and §6.2 enumerate their elements (*"The elements of a 5-tuple are:"*). Every
other record is open, because the source states only minimum content (*"It
contains at least an Issuer and a Subject"*, *"a request containing a nonce"*)
and says it leaves out technical detail.

**Traceability is in the file, and it is checked.** Every entry carries:

- `x-status`, one of `derived` (48 productions, plus the `NOT-EXPRESSIBLE`
  findings entry), `derived-from-example` (4), `inferred` (5), `opaque` (5)
  and `project-convention` (1);
- `x-quotes`: the source text the entry encodes, with section, line range and
  region id — 171 quotes in all, counting the bases of the findings;
- `x-inferred`, on 26 entries: the 5 `inferred` ones, and 21 that are not
  `inferred` overall but rest partly on an inference or a project choice. It
  names each keyword affected, so no inference is marked only in prose.

Quotes are verbatim modulo line-wrapping: each run of whitespace in the source,
including a line break and the next line's indent, is one space. So a word the
source hyphenates across a line break appears as `LISP- like`. No quote crosses
a page break.

**Opaque leaves.** The source gives no form for a public key, a date, a
location, a nonce, a certificate identifier or a delta-CRL; those entries
accept any value. `public-key` is further constrained by an *inference*: it
must be a list whose type is none of this source's own (`name`, `hash`,
`k-of-n`, `null`, `tag`, `*`). Without that, relative and fully qualified names
collide, `Self` collides with a key, and `subject` can reject nothing. Its
`$comment` gives the argument.

**`(* range …)` operators are closed by design.** The template's
`<lower-limit>` and `<upper-limit>` are undefined. The only evidence is the one
example, `ge #30# le #39#`, so the operator set is closed to `ge` and `le`, and
a range written with another operator fails here on purpose. Widen it only
from a source that defines more.

## Index of productions

| entry | status | form | sections |
|---|---|---|---|
| `byte-string` | project-convention | an atom: a JSON string, every character ≤ U+00FF | Abstract, §6.2, §6.3.1 |
| `s-expression` | derived | `[type, item*]`, non-empty | §1.1 |
| `sexp-item` | derived | byte-string or s-expression | §6.3.1 |
| `public-key` | inferred | opaque list whose type is not one of the source's own | Abstract, §1.1, §2.7, §7.7 |
| `hash` | derived-from-example | `["hash", alg, value]` | §2.7, §2.8, §7.5 |
| `key-hash` | derived | = `hash` | §6.1 |
| `object-hash` | derived | = `hash` | §1.1, §6.1 |
| `principal` | derived | public-key or key-hash | §5.2, §6.1, §6.2 |
| `name-string` | derived | byte-string | §2.8, §6.2 |
| `relative-sdsi-name` | derived | `["name", n+]` | §2.6.1, §2.6.2, §2.8 |
| `basic-sdsi-name` | derived | `["name", n]` | §2.6.1 |
| `compound-sdsi-name` | derived-from-example | `["name", n, n+]` | §2.6.2, §2.8 |
| `fully-qualified-sdsi-name` | derived | `["name", principal, n+]` | §2.8, §7.3 |
| `fully-qualified-x509-name` | derived | = `fully-qualified-sdsi-name` | §2.9 |
| `sdsi-name` | derived | relative or fully qualified | §2.10, §6.1 |
| `threshold-number` | derived-from-example | byte-string of at least one octet | §6.3.3, §7.7 |
| `threshold-subject` | derived | `["k-of-n", K, N, subject+]` | §1.1, §6.3.3, §6.4.1, §7.7 |
| `subject` | derived | principal, name, object hash or threshold | §1.1, §6.1 |
| `name-definition-subject` | derived | principal, name or threshold | §6.2 |
| `null-subject` | derived | `["null"]` | §6.3.3 |
| `tag` | derived-from-example | `["tag", tag-expr]` | §6.3.1, §6.5.3, §6.5.7, §7.7 |
| `authorization` | derived | = `tag` | §6.1, §7.7 |
| `tag-expr` | derived | byte-string, tag-list or star-form | §6.3.1 |
| `tag-list` | derived | `[type, tag-expr*]`, type not `*` | §6.3.1 |
| `star-form` | derived | one of the four below | §6.3.1 |
| `star-all` | derived | `["*"]` | §6.3.1 |
| `star-set` | derived | `["*", "set", tag-expr*]` | §6.3.1 |
| `star-prefix` | derived | `["*", "prefix", bytes]` | §6.3.1 |
| `star-range` | derived | `["*", "range", ordering, ("ge", v)?, ("le", v)?]` | §6.3.1 |
| `range-ordering` | derived | `alpha`, `numeric`, `time`, `binary`, `date` | §6.3.1 |
| `date` | opaque | any | §6.1, §6.3.2 |
| `tuple-validity` | derived | `{not-before?, not-after?, online-tests?}`, closed | §6, §6.1, §6.2, §6.3.2 |
| `validity-conditions` | derived | the same members, open | §5 |
| `dated-interval` | inferred | `{not-before, not-after}` | §5.2, §5.4 |
| `online-test` | derived | one of the four tests, by `kind` | §5, §6 |
| `crl-test` | derived | `{kind: "crl", issuer, locations?}` | §5.2 |
| `revalidation-test` | inferred | `{kind: "revalidation", issuer, locations?}` | §5.3 |
| `one-time-test` | inferred | `{kind: "one-time", issuer, locations?}` | §5, §5.5 |
| `replacement-test` | derived | `{kind: "replacement", locations}` | §5.6 |
| `location` | opaque | any | §5.2 |
| `certificate-identifier` | opaque | any | §5.1, §5.2 |
| `timed-crl` | inferred | `{validity, certificates}` | §5.1, §5.2, §5.3 |
| `delta-crl` | opaque | any | §5.2 |
| `current-crl` | derived | `[timed-crl, delta-crl*]` | §5.2 |
| `timed-revalidation` | derived | `{validity, certificates+}` | §5.3, §5.4 |
| `nonce` | opaque | any | §5.5 |
| `one-time-revalidation-request` | derived | `{nonce, …}` | §5.5 |
| `one-time-revalidation` | derived | `{nonce, certificates?}`, no validity | §5.5 |
| `delegation` | derived | boolean | §4.1.4, §6.1 |
| `five-tuple-issuer` | derived | principal or `"Self"` | §1.1, §6.1 |
| `five-tuple` | derived | `[issuer, subject, delegation, authorization, validity]`; **root** | §6.1, §6.3 |
| `four-tuple` | derived | `[issuer, name, subject, validity]` | §6.2, §6.4, §6.5.1, §6.5.2 |
| `four-tuple-defining-key` | derived | class (1): the subject is a principal | §6.4 |
| `four-tuple-defining-name` | derived | class (2): the subject is a fully qualified name | §6.4 |
| `entity-name-key` | derived | input kind 1: a four-tuple | §6 |
| `entity-authorization-name` | derived | input kind 2: a five-tuple with a name subject | §6 |
| `entity-authorization-key` | derived | input kind 3: a five-tuple with a principal subject | §6 |
| `subordinate-five-tuple` | derived | a five-tuple whose subject may be `(null)` | §6.3.3 |
| `threshold-subordinate-tuples` | derived | a list of those, or of bare `(null)` | §6.3.3 |
| `authorization-certificate-body` | derived | `{issuer, subject, authorization, delegation?, validity?}` | §1.1, §6.5.6 |
| `name-certificate-body` | derived | `{issuer, name, subject, validity?}`, no authorization | §6.2, §6.4.2, §6.5.6 |
| `acl-entry` | derived | `{subject, authorization, delegation?, validity?}`, no issuer | §1.1, §3.4 |
| `acl` | derived | `[acl-entry*]` | §1.1 |

## What no schema here can express

These are collected in the schema as `$defs/NOT-EXPRESSIBLE`, with a verbatim
basis on every item. **A green result from this schema does not mean the data
is valid SPKI.** In particular, `(k-of-n #08# #07# …)` — K greater than N —
validates, and so do a threshold with fewer subjects than N and `(k-of-n #00#
…)`. That was checked, not assumed.

Constraints a validator must check in code (16 stated, 3 inferred):

| id | applies to | rule | basis |
|---|---|---|---|
| SC-01 | `threshold-subject` | 0 < K ≤ N | stated, §6.3.3 |
| SC-02 | `threshold-subject` | the number of subordinate subjects is N | stated, §6.3.3 |
| SC-03 | `threshold-number` | K and N are read as unsigned big-endian integers | inferred, §7.7 (one-octet values only) |
| SC-04 | `hash` | the algorithm is a collision-free hash and the value is its output (20 octets for sha1) | inferred, §2.7 |
| SC-05 | `name-definition-subject` | a 4-tuple Subject is never an object hash; this cannot be decided from the data | stated, §6.2 |
| SC-06 | `relative-sdsi-name` | inside a certificate, a relative name resolves in the issuer's name space | stated, §2.8 |
| SC-07 | `tuple-validity` | an omitted not-before is −∞ and an omitted not-after is +∞ | stated, §6.1, §6.2 |
| SC-08 | `timed-crl`, `timed-revalidation` | not-before < not-after | stated as "non-0" in §5.4; the strict order is inferred |
| SC-09 | `timed-crl`, `timed-revalidation` | the intervals of successive instruments do not intersect; whether intervals sharing only an endpoint intersect is undetermined (`SPKI-52-04`) | stated, §5.2 condition 3, §5.3 |
| SC-10 | the three instruments | each is signed by the issuer the certificate's online test names | stated, §5.2 condition 1 |
| SC-11 | `one-time-revalidation` | its nonce equals the request's | stated, §5.5 |
| SC-12 | `one-time-revalidation` | it is valid only in the computation that requested it | stated, §5.5 |
| SC-13 | `current-crl` | the full CRL plus its deltas meets all three §5.2 conditions | stated, §5.2 |
| SC-14 | `five-tuple` | the reduction rule — an operation, listed for pass 3 | stated, §6.3 |
| SC-15 | `date` | dates have a monotonic representation | stated, §6.3.2 |
| SC-16 | `tag-list` | a longer list restricts; a design duty, not checkable | stated, §6.3.1 |
| SC-17 | `threshold-subordinate-tuples` | the list has N slots; reduction ends at N−K `(null)` slots and K slots with equal Subjects | stated, §6.3.3 |
| SC-18 | `five-tuple-issuer`, `acl-entry` | a tuple derived from an ACL entry has Issuer `Self` | inferred, §1.1 |
| SC-19 | `four-tuple`, `name-certificate-body` | do **not** require (issuer, name) to be unique | stated, §2.10 |

Gaps, where the source is silent and a schema needs an answer:

- **G-01** what an absent delegation means;
- **G-02** the concrete S-expression of every record;
- **G-03** range-ordering and limit semantics;
- **G-04** where a one-time request is sent;
- **G-05** what the one-time request and response carry besides the nonce;
- **G-06** the §5.6 kind's name and signer, and whether §5's issuer rule covers
  it;
- **G-07** delegation intersection;
- **G-08** where `(null)` goes;
- **G-09** multi-octet K and N;
- **G-10** the form of a public key;
- **G-11** whether an Authorization must be a `(tag …)`;
- **G-12** what a timed CRL contains;
- **G-13** what a delta-CRL contains;
- **G-14** nested thresholds;
- **G-15** delegation on name certificates;
- **G-16** display hints and the canonical encoding.

## Template closure

This is the analogue of ABNF rule closure for the verbatim notation. The
notation uses twelve placeholders, and **the source defines none of them by a
production**.

| placeholder | where | what the source gives | derived entry |
|---|---|---|---|
| `<tag-expr>` | §6.3.1, `(* set <tag-expr>*)` | nothing; bodies are shown by example | `tag-expr` |
| `<byte-string>` | §6.3.1, `(* prefix <byte-string>)` | "byte string" is used throughout and never defined | `byte-string` |
| `<ordering>` | §6.3.1, `(* range …)` | an enumeration in prose: alpha, numeric, time, binary, date | `range-ordering` |
| `<lower-limit>`, `<upper-limit>` | §6.3.1, `(* range …)` | nothing; one example shows `ge #30#` and `le #39#` | `star-range` |
| `<root key>` | §2.9 | a key | `principal` |
| `<leaf name>` | §2.9 | nothing | `name-string` |
| `<CA(1)>`, `<CA(2)>`, `<CA(k)>` | §2.9 | nothing; §6.5.1 spells them `CA1 CA2 ... CAk` | `name-string` |
| `<leaf-name>` | §6.5.1 | the §2.9 placeholder, spelt differently (D-06) | `name-string` |
| `<domain-name>` | §6.5.7, `(tag (dns <domain-name>))` | "a DNS name parameter", undefined | a byte-string inside `tag-expr` |

The tuple and pair notations (`<I1,S1,D1,A1,V1>`, `<name,key>`,
`<authorization,name>`, `<authorization,key>`) and the symbols (`K1`…`K7`,
`Kroot`, `Ki`, `N`, `N1`…`Nk`, `Na Nb Nc`) are notation, not placeholders.

## How this was checked

Every check was mechanical, by a script run in this session's scratchpad. The
script is not part of the record; pass 2 should re-derive the checks, not trust
them.

1. **Region digests.** All 57 regions hash to the digests in their headers.
2. **Verbatim fidelity.** Each region is byte-identical to its source lines in
   `.cache/rfc-2693.txt` (sha256 `6822d668…c42c99098`), contains no form feed
   and lies within one page. The region table was kept independently of the
   files, and the two match.
3. **JSON Schema syntax.** `jsonschema` 4.10.3 (Python) is installed.
   `Draft202012Validator.check_schema` passes, and `iter_errors` against the
   full 2020-12 metaschema reports **0 errors**. A duplicate-key detector run
   over the raw JSON found none.
4. **`$ref` closure.** 127 references to 47 distinct targets, all local and
   all defined. The 17 unreferenced entries are the intended roots listed
   above.
5. **Quotes.** All 171 `x-quotes` and finding bases were checked:
   - each is a verbatim substring of its cited lines (modulo line-wrapping);
   - each line range is tight, so dropping either end line loses the quote;
   - each cited region covers the quote's lines;
   - each section label matches the heading the lines sit under.

   The 22 single-quoted source fragments inside `$comment` and `x-inferred`
   text passed the same check. A `$comment` that says INFERRED must belong to
   an `inferred` entry or one with `x-inferred`. That rule caught one omission
   (`five-tuple-issuer`), since fixed.
6. **Examples.** All 44 `examples` values validate against their own entries.
7. **The forms the source prints.** A small parser read 46 printed
   S-expressions (45 distinct) from their advanced-transport text. Printed
   placeholders were substituted: `<root key>` and `K1`…`K7` by the source's
   own hash form, the others by tokens. That gave 74 positive checks against
   the entries the forms instantiate, plus 12 constructed positives for the
   abstract records. **48 negative controls** (29 S-expression, 19 JSON) were
   each rejected for their stated reason, among them:
   - `()`, `((a) b)`, `(name)`, `(tag a b)`, `(* foo)`;
   - `(* range numeric gt #30#)` and `(k-of-n #03# #07#)`;
   - a 5-tuple whose delegation is the string `"true"`, and a 4-tuple issued
     by `Self`;
   - a one-time revalidation carrying validity dates, an ACL entry with an
     issuer, a name certificate with an authorization;
   - both §6.5.1 4-tuples read literally (D-02).
8. **The checker was itself tested.** Eight faults were injected, and each was
   caught: a changed word, a widened line range, a wrong section label, a
   wrong region id, a quote spliced across a page break, two non-adjacent
   fragments spliced into one quote (the vCon failure mode), a bad example
   and a dangling `$ref`.
9. **Cross-references.** All 20 section references in the source were
   resolved against its headings. One dangles (D-01).

**CDDL was not checked, and none was written.** No CDDL tool is installed here
(`cddl`, `cddlc` and `pycddl` are all absent), and none was installed. The
derived schema is therefore JSON Schema, which can be validated here, and it is
in one language only, because two derived renderings would be two things to
keep in sync.

## Source defects — recorded, never repaired

Schema-relevant:

- **D-01 A dangling cross-reference.** §6.4.1 (line 1592) has
  *"Certificate Result Certificates [see 6.7]"*. There is no §6.7; Certificate
  Result Certificates is §6.6.
- **D-02 §6.5.1 puts a non-byte-string in the 4-tuple's Name slot.** §6.2
  says *"Name: a byte string"* (line 1312). §6.5.1 writes the slot as an
  S-expression, `[Kroot, (name <leaf-name>), K1, validity]` (line 1616), and
  for per-CA uniqueness as a compound name, *"[Kroot, (name CA1 CA2 ... CAk
  <leaf-name>), K1, validity]"* (line 1631). Read literally, neither
  validates against `four-tuple`. The first can be read as notation for its
  one name; the second cannot be read that way. Whether a name 4-tuple may
  define a compound name is an open question for `design-notes.md`.
- **D-03 The name 4-tuple classes leave out the threshold.** §6.2 admits
  *"a threshold function of subordinate subjects"* as a 4-tuple Subject (lines
  1314–1315). §6.4 says *"There will be name 4-tuples in two different
  classes"* — key and name (lines 1537–1539) — with no class for the threshold.
- **D-04 Are a threshold's members keys, or subjects?** The glossary entry
  SUBJECT has *"a set of keys arranged in a threshold function"* (line 238).
  §6.1 has *"a threshold function of subordinate subjects"* (lines 1277–1278),
  and §6.4.1 says *"Some of a threshold subject's subordinate subjects might be
  names."* (line 1583). The schema follows §6.1.
- **D-05 Three kinds of online test, then four.** §5: *"Three kinds of on-line
  tests are envisioned: CRL, re-validation and one-time."* (lines 980–981). §6
  (lines 1222–1223) and §7 (lines 1823–1824) list the same three. §5.6 then
  defines *"a kind of online test statement to tell the user of the certificate
  where a replacement short-lived certificate might be fetched"* (lines
  1147–1149). The schema admits all four.
- **D-06 One placeholder, two spellings.** §2.9's `<leaf name>` and `<CA(1)>
  … <CA(k)>` become `<leaf-name>` and `CA1 CA2 ... CAk` in §6.5.1.
- **D-07 Where does `(null)` go?** §6.3.3 sets the unselected *subjects* to
  `(null)` (line 1502), then speaks of the *list* having *"(N-K) (null)
  entries"* (lines 1507–1508). The schema admits both readings.
- **D-08 Delegation intersection is never defined.** §6.3.3 has
  *"validity-, authorization- and delegation- intersected"* (line 1509).
  VIntersect and AIntersect are defined; a delegation intersection is not.
- **D-09 Zero-length validity, both ways.** §5.5 opens with *"Validity
  intervals of length zero are not possible."* (line 1108) and ends with a
  protocol that *"represents a validity interval of zero"* (line 1132). The
  text explains it — the one-time protocol replaces dates rather than carrying
  them — but the two sentences contradict each other as written.
  `one-time-revalidation` encodes the second.
- **D-10 The numeric range example decides nothing.** In §6.3.1 (lines
  1450–1452), `(* range numeric ge #30# le #39# )` against `(tag #26#)`
  *"fails to intersect"*. It fails under the integer reading (38 is not in [48,
  57]) and under the character reading (`&` is not between `0` and `9`), so
  the one example cannot fix how `numeric` reads a byte string.
- **D-11 The tag wrapper is never defined.** `(tag …)` appears in 27 printed
  forms, every one with exactly one body element. Yet the first three
  authorizations of §6.3.1 are printed without it, and no sentence introduces
  it.
- **D-12 The definition says "a public key"; the example uses its hash.** §2.8
  defines the fully qualified name as *"a public key followed by one or more
  names"* (lines 625–626), and its example uses the hash form,
  `(hash sha1 |TLCgPLFlGTzgUbcaYLW8kGTEnUk=|)` (line 630).
- **D-13 A three-element "pair".** §2.9 (lines 643–646) calls `(name
  <root key> <leaf name>)` *"the pair"*.

Noticed in passing, outside this artifact (for `normative.md` and pass 2):

- §6.4 (lines 1546–1547) says 4-tuples *"should be delivered in the order
  needed by the prover"*. §6.3.4 has the prover *providing* the order (*"All
  reduction operations are in the order provided by the prover."*), so this
  reads as a slip, probably for "the verifier".
- The reference [ELIEN] stops mid-bracket at *"[also .pdf and"* (line 2118).
- Typos: *"these signer would be corrupt"* (line 367); *"leaving a copies of
  itself"* (line 1027); *"the rules for that particular X.509 hierarchy is"*
  (line 1618).

## What is not here, and why

- **No verbatim grammar.** The source has none; see the top of this file.
- **No concrete structure for any record.** That covers certificates, keys,
  signatures, dates, online tests, CRLs, revalidations, one-time requests and
  responses, locations, nonces and certificate identifiers. The source defers
  them to the Abstract's omitted *"technical detail"*, to *"the SPKI structure
  definition"* (§5.7.2) and to *"the examples document"* (§6.5.7).
  `draft-ietf-spki-cert-structure` is a separate record (`see_also`), and
  nothing was imported from it. Where the schema needs an answer the source
  does not give, the entry is `opaque` and the question is a gap.
- **No canonical form, transport encoding or display hint.** The Abstract
  says SPKI defines *"a canonical form for those S-expressions"*, but the
  definition is not in this document. `rfc-9804` holds it, with its own
  verbatim ABNF.
- **No semantics.** AIntersect, VIntersect, 5-tuple reduction, threshold
  reduction, name 4-tuple reduction and certificate path discovery are
  operations, not shapes. Their source text is in the verbatim files, and
  SC-14 lists the reduction rule for the cross-check. The executable
  semantics belong to the protocol, state-machine and examples artifacts.
- **No schema for the foreign certificate formats** of §6.5 (X.509v1, PGP,
  X.509v3, X9.57, SDSI 1.0, SSL). The source defines only how they translate
  into tuples, and `four-tuple` and `five-tuple` cover that.
- **No separate Certificate Result Certificate.** §6.6 makes it a new
  certificate issued by the entity doing the computation — an
  `authorization-certificate-body`.
- **No anti-matter CRL.** *"SPKI has ruled out the use of wandering
  anti-matter CRLs for its certificates."* (§5.1). Its stated contents are
  recorded in G-12 only.
- **Nothing for §5.7 or §8.** Micali's hash chains and Rivest's reversal (§5.7)
  are *"not reflected in the SPKI structure definition"*. The six mapping
  classes of §8 are a classification, not a structure.
- **No requirement ids on the productions.** RFC 2693 contains no BCP 14 keywords
  (`bin/bcp14-count` reports 0). This artifact was extracted from the source
  alone, in parallel with `requirements.yaml` (whose entries all carry verb
  `none`), so everything here cites a section, a line range and verbatim text
  instead. Each SC and G item now names its requirements in `x-requirements`
  (pass 3); SC-03 and G-16 name none, because their only basis, the §7.7
  k-of-n example and the Abstract, is excluded from `requirements.yaml`.

## Open for the later passes

- **Pass 2 (verify, 2026-10-12): done.** Checks 1–7 above were re-derived by
  independent scripts from the cached source, and all hold: the 57 regions
  and their digests, the metaschema, the `$ref` closure, the 171 quotes, the
  44 `examples`. Every concrete S-expression in `examples/vectors.yaml`
  validates against the entry it instantiates, and the two §6.5.1 forms fail
  `four-tuple` (D-02). The single-quoted fragments in `$comment` and
  `x-inferred` are all verbatim (18 by this pass's delimiting). Two counts in
  this file were corrected: the `x-status` tally and the `x-inferred` one.
- **Pass 3 (cross-check, 2026-10-12): names reconciled.** messages.yaml
  renamed its fields to this file's member names (`validity`, `certificates`,
  `issuer`), and its note (12) gives the full crosswalk, including the word
  *principal*, which this file uses for a key or its hash and messages.yaml
  for the key alone.
- **Examples:** every fixture should validate against the entry
  `examples/README.md` names for it (*Schema entry per vector*). The two
  §6.5.1 4-tuples must *fail* `four-tuple` read
  literally (D-02); that failure is the source defect showing, not a fixture
  error.
- **Design notes:** D-02, D-03, D-07 and D-08, and gaps G-01, G-07 and G-11,
  are the questions most likely to bear on this project's 5-tuple (R-M-05)
  and tag algebra (R-M-08, DEC-004).

---
record: w3c-vc-jose-cose
kind: schema
title: "w3c-vc-jose-cose — schemas"
extracted: "2026-11-03"
reviewed_by: ""
---

# Securing Verifiable Credentials using JOSE and COSE — schemas

The W3C Recommendation (REC-vc-jose-cose-20250515, 15 May 2025) publishes
**no** formal syntax of its own: no CDDL, no JSON Schema, no ABNF, no ASN.1
(the search is below). What it does print as formal displays is six media
type registration templates (§6.1.1–§6.1.6, one HTML table each, in a
section marked non-normative), the input and output definitions of the §5
verification algorithms, and the §1.1.2.2 list that describes the SD-JWT
format. Those are copied verbatim into `inline.verbatim.txt`. It prints no
normative table. Everything else here is **derived**: this library's
machine-checkable rendering of the source's prose, named `*.derived.*`, with
`DERIVED` in its first 12 lines and, for JSON Schemas, an `$id` of
`urn:library:w3c-vc-jose-cose:<artifact>`.

Source: `.cache/w3c-vc-jose-cose.bin` (the REC HTML), sha256
`6c70cf8d7de9d8a3ff28a743fea9d569a67a402111c3245fdafbaa2ad6709af9` (equal to
`content.sha256` in `record.yaml`); its plain-text rendering
`.cache/w3c-vc-jose-cose.txt`, sha256
`f02bd4966800863d533746c6c39ad267ada1b8bfcbb92186c204b617bb46c126`, 1980 lines,
is what line numbers here count in and what quotations are checked against.
Example instances were decoded from the HTML elements, never from the
rendering, which inserts a space at each `<span>` boundary of a compact JWS.

## Files

| file | kind | built from | covers | does NOT cover |
|---|---|---|---|---|
| `inline.verbatim.txt` | **verbatim** | §1.1.2.2, §5, §5.1–§5.3, §6.1.1–§6.1.6 | 11 regions, table below: the six templates, the §5 inputs and outputs, the §1.1.2.2 list | prose (`normative.md`); the 26 examples (examples lane); the §5 step lists (protocol lane) |
| `jose-header.derived.schema.json` | **derived**, JSON Schema 2020-12, `$id` `urn:library:w3c-vc-jose-cose:jose-header.derived` | §1.1.2.1, §3, §3.1.1, §3.1.2, §3.2.1, §3.2.2, §4.1.1–§4.1.3, §4.2; RFC 7515, RFC 9901 | the JOSE Protected Header of vc+jwt, vp+jwt and of an SD-JWT's Issuer-signed JWT: `alg`, `typ`, `cty`, `kid`, `iss`, `cnf`. Root = MUST; `#vc-jwt-should`, `#vp-jwt-should`, `#vc-sd-jwt-should`, `#vp-sd-jwt-should`; conditional `#kid-present`, `#kid-absolute-url` (MUST), `#kid-thumbprint-url` (RECOMMENDED) | `crit` and every other registered parameter (left open); anything from §3.1.3, which is non-normative; JWE headers; signatures |
| `payload.derived.schema.json` | **derived**, `$id` `…:payload.derived` | §1.1.2.1, §3.1.2, §3.2.2, §3.3.2, §5.1, §5.4; VC-DATA-MODEL-2.0 | the unsecured credential or presentation (decoded JWS payload, rebuilt SD-JWT claims, COSE payload as JSON); `#jwt` adds the JWT Claims Set rules | the data model beyond `@context`/`type` presence; JSON-LD well-formedness; `iss`↔`issuer` (cross-field YAML) |
| `sd-jwt.derived.schema.json` | **derived**, `$id` `…:sd-jwt.derived` | §1.1.2.2, §3.2.1, §3.2.2; RFC 9901 | a decoded SD-JWT: compact form, Issuer-signed JWT, disclosures, KB-JWT; `#vc-should`, `#vp-should` | digest computation and placement (X-08); `sd_hash` value; the JSON serialization |
| `cose-sign1.derived.cddl` | **derived**, CDDL (RFC 8610) | §3.3, §3.3.1–§3.3.3; RFC 9052, RFC 9596, draft-ietf-cose-cwt-claims-in-headers-10 (label from RFC 9597), RFC 8392, RFC 8747 | COSE_Sign1, both header buckets, typ (16), content type (3), CWT Claims (15) with claim types; roots `vc-cose`, `vp-cose`, `vc-cose-should`, `vp-cose-should`, `protected-must`, `vc-protected-should`, `vp-protected-should` | algorithm, key and signature-length consistency; a URL `kid` (a bstr in COSE); a label repeated across buckets; the payload's content |
| `enveloped.derived.schema.json` | **derived**, `$id` `…:enveloped.derived` | §3.1.2, §3.2.2, §3.3.1, §3.3.2, §8.4; VC-DATA-MODEL-2.0 §4.13; RFC 2397 | EnvelopedVerifiableCredential `#vc`, EnvelopedVerifiablePresentation `#vp`, their `data:` URLs per media type `#data-uri-vc`, `#data-uri-vp`, `#data-url`; SHOULD anchors `#data-uri-vc-should`, `#data-uri-vp-should` | the secured object inside the URL (decode it and apply the schema for its media type: X-10); whether `@context` defines the terms |
| `data-uri.derived.abnf` | **derived**, ABNF (RFC 5234) | §3.3.1, §8.4; RFC 2397 §3, RFC 2396 §2, RFC 9901 §4 | the same `data:` URL grammar: six media-type rules and RFC 2397 `dataurl` | the credential/presentation kind check only the JSON Schema states |
| `cid-verification-method.derived.schema.json` | **derived**, `$id` `…:cid-verification-method.derived` | §4.2; RFC 7517 | a verification method used with this specification; `#document` for every method a document lists | retrieval; the Controlled Identifiers 1.0 rules themselves |
| `verification-result.derived.schema.json` | **derived**, `$id` `…:verification-result.derived` | §5, §5.1–§5.3, §5.4 | the outputs `status`, `document`, `mediaType`; `#jose`, `#sd-jwt`, `#cose` | the algorithms (protocol and state-machine lanes) |
| `cross-field-rules.derived.yaml` | **derived**, YAML | §1.1.2.1, §3.1.2, §3.2.1, §3.2.2, §3.3.2, §4.1.1–§4.1.3, §4.2 | X-01–X-11: rules relating two fields, or a field and a condition outside the object; each carries its requirements' text, locator and level, copied by script, and an outcome computed over the examples | — |
| `schema-tests.derived.json` | **derived**, JSON | the checks below | 438 cases, 513 verdicts: every instance the checks ran, with its expected verdict; synthetic instances inline, example instances by example and view | — |

## No grammar of its own — the search

`grammar_search` (scratch, `python3 -I`) read the whole HTML, markup included
(5035 lines), the rendering (1980 lines) and every `<pre>` block outside
`<script>`/`<style>` (56), for: the word CDDL in any case; ABNF; `::=` or ` := `;
ASN.1 or `DEFINITIONS IMPLICIT|EXPLICIT`; the phrase JSON Schema; `$schema`,
`"$id"`, `$defs`; `.regexp`; and two rule shapes (`name = {`/`[`/`(`/`#`, or
`=>`; `%x..`, `n*m`, `*(`). Every pattern found **0** in the rendering and **0**
in the `<pre>` blocks. In the HTML, only the CDDL-like rule shape matched, 13
lines, and all 13 lie inside `<script>` or `<style>` (JavaScript arrow
functions). The §6 templates are HTML tables, not a grammar.
`credentialSchema` entries of `"type": "JsonSchema"` in the examples name the
data model's validation mechanism, not a JSON Schema this source publishes.

## Inline regions (`inline.verbatim.txt`)

Each region is the rendering's lines between `---- BEGIN VERBATIM I-nn ----`
and `---- END VERBATIM I-nn ----`, byte for byte; the sha256 is over those
lines joined by a line feed, with no trailing line feed. The HTML range is the
`.bin` line range of the element the region renders, where every cell of the
region was found again, markup removed (215 of 215 cells).

| id | section | display | .txt lines | HTML lines | sha256 |
|---|---|---|---|---|---|
| I-01 | §6.1.1 | media type registration template, application/vc+jwt | 934–956 | 2906–2998 | `c0dec03a9f028d1d4b49b2d79cb0b70ccf4cff8b49e956910661439156b7c38d` |
| I-02 | §6.1.2 | media type registration template, application/vp+jwt | 960–982 | 3002–3095 | `95262190da28ea0c0045ca468a93b8767b4eee2447565c4929490f020cd217b0` |
| I-03 | §6.1.3 | media type registration template, application/vc+sd-jwt | 986–1008 | 3099–3192 | `c03ff8cec64a5b23438a8db25c88b672f3e5b394e137b2e42baad525002256f2` |
| I-04 | §6.1.4 | media type registration template, application/vp+sd-jwt | 1012–1034 | 3196–3292 | `bc81f395f0ff5690271c8dce6af865f265677e289c088c65f53ac7bc5e7c7ad3` |
| I-05 | §6.1.5 | media type registration template, application/vc+cose | 1038–1060 | 3296–3386 | `40bd3df2cefc5d73f5f4d724afe78217454e320139c1173cb5409b98dab8cd26` |
| I-06 | §6.1.6 | media type registration template, application/vp+cose | 1064–1086 | 3390–3481 | `5cf7eec90138a25e2226b172a0eed1cc351ab66cfdf318a30d9e24af83a9ccac` |
| I-07 | §5 | outputs of the verification algorithms (status, document, mediaType) | 859–862 | 2670–2683 | `91c92f618064148da03b180efaf646c7158af4fc150d0b06e8b63b72a407f509` |
| I-08 | §5.1 | inputs of the JOSE verification algorithm | 866–868 | 2687–2696 | `0fb5a771f9476b455257646613638e3d58afafa50e8fc30ed4b9395cff62ea42` |
| I-09 | §5.2 | inputs of the SD-JWT verification algorithm | 884–886 | 2745–2754 | `7d5d31bfe7a104d0b29fc28fffa0c59eb20389a987d1c79160552f508c6e1e8d` |
| I-10 | §5.3 | inputs of the COSE verification algorithm | 902–904 | 2809–2820 | `28529bdc9270d17a5bf5397f516fe5660d62d3de00884bc5941997a5c4f2e44e` |
| I-11 | §1.1.2.2 | the SD-JWT format, a four-item list | 153–156 | 1327–1344 | `007140d2e8d35034bf6419a08d5482666c07cdcc10abd2ef541e8f7fdda01633` |

I-01 to I-06 differ only in the subtype, the identifying sentence and the
security reference; none carries a BCP 14 keyword. The template's "Additional
information" is an `<ol type="1">` whose numbers are not text, so neither
the rendering nor the copy carries them.

## Coverage — every formal display, by line

Census of the HTML outside `<script>`/`<style>`: 2 `<dl>`, 2 `<dl class="bibliography">`, 1 `<dl class="termlist">`, 15 `<ol>`, 16 `<ol class="toc">`, 32 `<pre>`, 12 `<pre class="header-value">`, 12 `<pre class="nohighlight vc">`, 6 `<table>`, 21 `<ul>`, 6 `<ul class="sd-jwt-tabs">`, 12 `<ul class="vc-tabs">`, 26 example blocks. Every display is
accounted for below (the `<ul>`/`<ol>` of the tabbed example widgets, the
table of contents and the reference back-links are navigation):

| .txt lines | section | display | where it is |
|---|---|---|---|
| 48–100 | ToC | table of contents | not formal; not copied |
| 130–135 | §1.1.2 | definition list: JWT, SD-JWT, COSE | prose (`normative.md`); not formal |
| 137–139 | §1.1.2 | list: what each mechanism encodes | prose; not formal |
| 153–156 | §1.1.2.2 | the SD-JWT format list | **I-11**; `sd-jwt.derived.schema.json`, `data-uri.derived.abnf` |
| 161–168 | §2 | terminology | prose (`normative.md`); not formal |
| 188–266, 279–355, 382–506, 520–616, 632–703, 716–778 | §3.1.1–§3.3.2 | Examples 1–9 | examples lane; decoded here as test instances |
| 821–852 | §4.2 | Examples 10–13 | examples lane; not JSON (Findings F-18) |
| 859–862, 866–868, 884–886, 902–904 | §5, §5.1–§5.3 | algorithm outputs and inputs | **I-07–I-10**; `verification-result.derived.schema.json` |
| 869–880, 887–898, 905–916 | §5.1–§5.3 | algorithm steps | protocol lane; their outcomes are `verification-result.derived.schema.json` |
| 934–956, 960–982, 986–1008, 1012–1034, 1038–1060, 1064–1086 | §6.1.1–§6.1.6 | media type registration templates | **I-01–I-06** |
| 1098–1100 | §7.1 | privacy considerations list | prose; not formal |
| 1123–1238 | §8.1 | Examples 14–17 | examples lane; 15–17 are instances of `cid-verification-method.derived.schema.json` |
| 1242–1790 | §8.2, §8.3 | Examples 18–20 | examples lane; decoded here as test instances |
| 1794–1804 | §8.4 | Examples 21–23, data: URLs | examples lane; instances of `enveloped.derived.schema.json`, `data-uri.derived.abnf`, and (23) `cose-sign1.derived.cddl` |
| 1809–1842 | §8.5 | Examples 24–26, CBOR diagnostic notation | examples lane; cannot be encoded (F-23) |
| 1850–1858 | App. A | revision history list | not formal |
| 1869–1921 | App. C | references | not formal |

## Requirement levels, and what binds what

A SHOULD is not a MUST, so the two never share a rule. The JSON Schema roots,
the CDDL rules `vc-cose`/`vp-cose`/`protected-must` and every anchor not
ending in `-should` hold MUST and MUST NOT statements only; a failure there is
non-conformance. Anchors and rules ending in `-should` add SHOULD, SHOULD NOT,
RECOMMENDED and NOT RECOMMENDED statements and include the MUST level by
reference; a failure there is a warning. Conditional MUSTs whose condition
lies outside the object are separate anchors, applied when
`cross-field-rules.derived.yaml` says their condition holds.

**Non-normative sections.** §3.1.3 opens with “This section is non-normative.” (§3.1.3), line 361, and §6 with
“This section is non-normative.” (§6), line 928. No constraint is drawn from §3.1.3's keywords (lines 365, 366,
368, 369, 370): the JOSE `nbf` advice, the JOSE registry advice and the rule
to ignore JOSE header parameters that are not understood have no normative
statement, while their COSE twins w3c-vc-jose-cose#R-0062, w3c-vc-jose-cose#R-0063 and w3c-vc-jose-cose#R-0064 do and are in the CDDL; the
`vc`/`vp` MUST NOT is the normative w3c-vc-jose-cose#R-0006. The §6 templates are verbatim only,
and no level is drawn from them either: a `data:` URL may carry media type
parameters at every level, though their Required parameters and Optional
parameters rows say N/A (E-09 accepts one), and the two readings that cite them,
the credential or presentation kind of each media type and the JWT behind
vc+jwt and vp+jwt, rest on §3.1.1 to §3.3.2 and on §5.1, the templates only
corroborating. Until the cross-check pass the six data: URL rules rejected any
parameter but `;base64` on the templates' word alone.

| level | where | cited (as a constraint, or as the reason for one or for its absence) |
|---|---|---|
| MUST | JOSE header root (`alg`); SD-JWT root; COSE `vc-cose`; payload root and `#jwt`; Enveloped objects and their `data:` URLs; verification method; verification result | R-0004, R-0005, R-0006, R-0011, R-0012, R-0017, R-0021, R-0022, R-0023, R-0025, R-0027, R-0030, R-0033, R-0036, R-0037, R-0038, R-0039, R-0042, R-0047, R-0050, R-0051, R-0053, R-0056, R-0057, R-0058, R-0059, R-0064, R-0066, R-0067, R-0070, R-0071, R-0079, R-0080 |
| MUST, conditional | `#kid-present`, `#kid-absolute-url` | R-0065, R-0072, R-0074 |
| SHOULD | `#*-should` (typ, cty, content type); SD-JWT `#vc-should`/`#vp-should` | R-0007, R-0009, R-0010, R-0013, R-0014, R-0018, R-0019, R-0028, R-0029, R-0031, R-0034, R-0035, R-0040, R-0046, R-0048, R-0049, R-0054, R-0055 |
| RECOMMENDED / NOT RECOMMENDED | `#data-uri-*-should`; `#kid-thumbprint-url`; CDDL `cwt-claims-should` (nbf); X-07 | R-0008, R-0044, R-0062, R-0063, R-0069, R-0073 |
| MAY | no constraint: each is cited as the permission a structure rests on | R-0016, R-0024, R-0043, R-0045, R-0061, R-0068 |

Of the 85 requirements, 66 are cited by the files here. The 19 not cited, and why:

- R-0001, R-0002, R-0003 (§1.1.1): conformance classes; they bind implementations to the §3
  statements, which the files carry one by one.
- R-0015, R-0020: the verifier twins of the issuer MUSTs that import RFC 7515; the import
  is made by w3c-vc-jose-cose#R-0012 and w3c-vc-jose-cose#R-0017, and checking a verifier is behaviour, not shape.
- R-0026 (JWS JSON serialization NOT RECOMMENDED): no instance model here holds
  the JSON serialization, so no instance can show the deviation.
- R-0032, R-0041, R-0052, R-0060: permissions to encrypt in transit; the source defines no structure.
- R-0075, R-0076, R-0077, R-0078, R-0081, R-0082, R-0083, R-0084, R-0085 (§5 and §5.4): verifier behaviour against its own policy. w3c-vc-jose-cose#R-0077
  names claims a `typ` expects without saying which, so it cannot be a
  schema rule.

## How the imports bind

A rule marked *imported* is a MUST of another document. It is in a schema only
because a clause of this source makes it bind; the clause is named. Copies of
every foreign document were fetched from rfc-editor.org (the draft from
ietf.org; the data model from `.cache/w3c-vc-data-model-2-0.bin`, whose digest
equals its record's), each quotation was resolved inside the section it is
attributed to, and nothing of this record was in that corpus.

| document | what is imported | the clause that makes it bind |
|---|---|---|
| RFC 7515 §4.1.1, §4.1.4, §4.1.9, §4.1.10 | `alg` required and a string; `kid` a string; `typ`/`cty` spelling | w3c-vc-jose-cose#R-0012 and w3c-vc-jose-cose#R-0017 (issuers MUST use [RFC7515]); their verifier twins R-0015, R-0020 |
| RFC 7519 §1, §4.1, §4.1.1, §5.3 | JWTs are compact; registered claim types; `iss` replicated in the header | §5.1: “Follow the algorithm defined in Validating a JWT [RFC7519].” (§5.1); the §6.1.1/§6.1.2 registrations identify a JWT (non-normative) |
| RFC 9901 §4, §4.1, §4.1.1, §4.2.1, §4.2.2, §4.2.4.1, §4.2.4.2, §4.3 | SD-JWT compact grammar, payload digests, disclosures, KB-JWT | w3c-vc-jose-cose#R-0027, w3c-vc-jose-cose#R-0030, w3c-vc-jose-cose#R-0033, w3c-vc-jose-cose#R-0036 (MUST use [SD-JWT]); w3c-vc-jose-cose#R-0042. [SD-JWT] is an Internet-Draft with no revision (C.1); RFC 9901 is read as its published form (inferred) |
| RFC 9052 §1.5, §3, §3.1, §4.2 | COSE_Sign1, the two buckets, Generic_Headers | w3c-vc-jose-cose#R-0047, w3c-vc-jose-cose#R-0050, w3c-vc-jose-cose#R-0053, w3c-vc-jose-cose#R-0056; §3.3.3 paragraph 2 |
| RFC 9596 §2 | typ (16): uint / tstr, protected bucket only | w3c-vc-jose-cose#R-0048 and w3c-vc-jose-cose#R-0054 cite it by title; [RFC9596] is a normative reference |
| draft-ietf-cose-cwt-claims-in-headers-10 §2; RFC 9597 §2 for the label | CWT Claims (15): a map, in one bucket only; RECOMMENDED protected | w3c-vc-jose-cose#R-0061; §3.3.3 paragraph 2, which links revision 10 |
| RFC 8392 §2, §3.1, §4 | claim keys 1–7 and their types; NumericDate untagged | §3.3.3 paragraph 2 |
| RFC 7800 §3.1; RFC 8747 §3 | `cnf` an object (JOSE), a map (COSE claim 8) | w3c-vc-jose-cose#R-0068 names both |
| VC-DATA-MODEL-2.0 §4.3, §4.5, §4.13 | `@context` and `type` present; the Enveloped objects; `id` a `data:` URL | w3c-vc-jose-cose#R-0021 and twins (the types are “defined by the [VC-DATA-MODEL-2.0]” (w3c-vc-jose-cose#R-0021)); w3c-vc-jose-cose#R-0080 |
| RFC 2397 §2, §3; RFC 2396 §2; RFC 2045 §6.8 | the `data:` URL grammar, `uric`, the base64 alphabet | w3c-vc-jose-cose#R-0051; VC-DATA-MODEL-2.0 §4.13 |
| RFC 6838 §4.2 | media type names compare case-insensitively | §1: “It uses content types [RFC6838] to distinguish between the data types of unsecured documents conforming to [VC-DATA-MODEL-2.0] and the data types of secured documents conforming to [VC-DATA-MODEL-2.0].” (§1) (inferred) |
| RFC 7517 §4.1 | a JWK has `kty` | w3c-vc-jose-cose#R-0071 ([RFC7517] is normative) |
| RFC 7638, RFC 9278 §3 | the thumbprint URI form | w3c-vc-jose-cose#R-0073 names RFC 7638, which has no URI; the form is RFC 9278's (F-06) |

Foreign copies used (sha256 of the file as fetched):

| document | sha256 |
|---|---|
| RFC 2045 | `9bb251635dd37fda97dcce6c08dea019432117a0f1e389051d2ecbf7b76350b0` |
| RFC 2396 | `67866c0aaa65b29372b4c7ca80ffdfa6caee825088593f4b8b296bff3c05cdc7` |
| RFC 2397 | `17fe861cb0fea6b96948cf985cfb4df052d9d26c02d804a1a922b862c74657bf` |
| RFC 3986 | `3102dae4b68cebe40337730312fcb612297b8928547267e8b3d1ee6002b2d683` |
| RFC 4648 | `84e14418f795d503be5f34bf23ce4ebaa119e9ec7c9f667d8caeb111385b178f` |
| RFC 6838 | `b08ccba7e5116e61085f2e1fe447d90eee785fb0efaa448a4b4ef6ea48b03b80` |
| RFC 7515 | `ecbf84674118e62526511c1237e1deaa86aada86d25b247623a2a7e04ae62e40` |
| RFC 7516 | `722cfcddc15f58e746891ba4b846853d3711153a774e4dd55ad6db100474a21f` |
| RFC 7517 | `681c19b92a85068716b7e89c5815aa821bd3f11c755ff1c641b40ae9851bb33c` |
| RFC 7518 | `9a9ae524b09ea700ad3f189bac115df95ba69af84b26ffdbe3cdfb8d2152b1fc` |
| RFC 7519 | `fecd930e9ccf2276b95c0017c6c4ff5d09352e4bc3c7629946447894e0f97248` |
| RFC 7638 | `98b29ab9652070e6a5fec748d43e221bbedc66b6b22e05903fb5366c04ef3110` |
| RFC 7800 | `051514a781038027c2ac07c26ebe8533556012b2353cdaec8f3baeac53a7c919` |
| RFC 8392 | `9021ff7c4d274cf34873fe4f4fb17c4fe323247dd0f96bfcab54909bfcdc5f13` |
| RFC 8610 | `3713f2a50e23a2bea0a6147ad6c4433605a00c3d00a868bfa86a42b204997089` |
| RFC 8747 | `9b695379f119f9675828d054f1b0e76014c06c9a59dccef8bb417e0420272dda` |
| RFC 9052 | `01eecd7f646537600e7aad665b1fa581ce6ec33dae4ef4add0997aaf38cd0a45` |
| RFC 9053 | `3d470615875620375f8453ba25b8dce7e4d0271e76b0b79a46df34ccb2d56ab0` |
| RFC 9278 | `c84d83e485a078599b4a022602ce336910b6d7c166fb9072a72ad8d923414816` |
| RFC 9596 | `4beb37fe8cb3eec78cec2445c65dcf2db4866ba99a72e7b1e54e23e5bfa69b5e` |
| RFC 9597 | `b6baaec655bc86606602a6f6e93f0103db6e6f98460f1e43437e74a6a5e02bdd` |
| RFC 9901 | `fd4cb79184162fa7ef95f4f63abab8ee6d03c9a04c19b8f83758946464b284eb` |
| VC-DATA-MODEL-2.0 | `73d91cc0b6a7d582512eb06d45a5fcfa8c696ab094b3db44f7a1495e9d3da548` |
| draft-ietf-cose-cwt-claims-in-headers-10 | `a01d44dfd384e655948b076e27d5bf7ac9cc82fd4d040eba23738ef96f27b3b6` |

VC-DATA-MODEL-2.0 is the rendering of `.cache/w3c-vc-data-model-2-0.bin`
(sha256 `a9196a3d0b6601356c4e127bad24f8c7f2c17f6ed22e41b35755a910104156f8`)
by the same renderer as this record's `.txt`.

## How to apply

1. **vc+jwt / vp+jwt.** Split the compact JWS; decode the header and apply
   `jose-header.derived` (MUST) and `#vc-jwt-should` or `#vp-jwt-should`
   (warnings); decode the payload and apply `payload.derived#jwt`.
2. **vc+sd-jwt / vp+sd-jwt.** Split on `~`; build the instance model of
   `sd-jwt.derived` (`compact`, `issuerSignedJwt`, decoded `disclosures`,
   `keyBindingJwt`) and apply its root and `#vc-should`/`#vp-should`; rebuild the
   claims set (RFC 9901 processing, §5.2) and apply `payload.derived#jwt`.
3. **vc+cose / vp+cose.** Validate the CBOR against `cose-sign1.derived.cddl`
   root `vc-cose` (MUST) and `vc-cose-should` / `vp-cose-should`; decode the
   payload bytes as JSON and apply `payload.derived`.
4. **Presentations.** For each `verifiableCredential` member, `payload.derived`
   applies `enveloped.derived#vc`; then decode each `data:` URL and repeat 1–3
   by its media type (X-10). An EnvelopedVerifiablePresentation payload is
   checked by `enveloped.derived#vp`, and its URL decoded the same way.
5. Apply `cross-field-rules.derived.yaml` X-01 to X-11 to each decoded object,
   then, on a verifier's output, `verification-result.derived` and its anchor
   for the mechanism.

JSON Schema `$ref`s between files are by `$id`: load all six into one registry.
The CDDL tool takes the first rule as the root; prepend `root = <rule>` to a
copy to pick another.

## Instances each schema must REJECT (hazards.md, section 7)

A schema that parses is not a schema that binds. For every derived schema the
instances it must reject are written down in `schema-tests.derived.json`, with
the ones it must accept beside them, and every one gave its expected verdict:

| schema | must reject (synthetic) | ids | must accept (synthetic) |
|---|---|---|---|
| `cid-verification-method.derived` | 4 | VM-01, VM-02, VM-03, VM-04 | 1 |
| `enveloped.derived` | 19 | E-01, E-02, E-03, E-04, E-05, E-06, E-07, E-08, E-10, E-11, E-12, E-13, EO-01, EO-02, EO-03, EO-04, EO-05, ES-02, ES-04 | 15 |
| `jose-header.derived` | 20 | J-01, J-02, J-03, J-04, J-05, J-06, J-07, J-08, JK-01, JK-03, JK-06, JK-08, JS-01, JS-02, JS-03, JS-04, JS-05, JS-06, JS-07, JS-08 | 12 |
| `payload.derived` | 9 | PL-01, PL-02, PL-03, PL-04, PL-05, PL-06, PL-07, PL-08, PL-09 | 6 |
| `sd-jwt.derived` | 21 | SD-01, SD-02, SD-03, SD-04, SD-05, SD-06, SD-07, SD-08, SD-09, SD-10, SD-11, SD-12, SD-13, SD-14, SD-15, SD-16, SDS-01, SDS-02, SDS-03, SDS-04, SDS-06 | 6 |
| `verification-result.derived` | 7 | VR-01, VR-02, VR-03, VR-04, VR-05, VR-06, VR-07 | 3 |
| `cose-sign1.derived.cddl` | 44 verdicts | N01–N24, S01–S10, H03 | 61 verdicts |
| `data-uri.derived.abnf` | 10 | E-01, E-02, E-03, E-04, E-05, E-06, E-07, E-10, E-11, ES-08 | 11 |

**Mutation check.** Deleting the one constraint each of 18 JSON Schema
negatives was written for turned every one of them into an accept (18 of 18), so
each is caught by the rule meant and not by a neighbour. In the CDDL, widening
the explicit `kid` entry to `any` made N05 pass, and widening `other-label` to
`label` made N01 (typ unprotected) and N02 (crit unprotected) pass: the
exclusions bind. N04 and N12 still failed with the wildcard widened,
because each has an explicit entry written with `:`, which carries the cut.
N08 did not: `protected-no-claims` has no entry for label 15, so there the
widened wildcard takes the CWT Claims whatever they hold, and N08 is
rejected only because `other-label` excludes 15 (re-run in the verify pass:
the cddl gem 0.12.14 and an independent evaluator both accept N08 with
`other-label = label`).

**The CDDL tool cannot show a wildcard swallowing a constraint.** The cddl gem
0.12.14 rejected `{16: 5}` against `{ ? 16 => tstr, * int => any }`, which RFC
8610 §3.5.4 says matches (the wildcard takes the entry). So a reject from that
tool is no evidence that a grammar binds. The structural check is: every
wildcard in the file is written over a key type that excludes every integer
label its map lists explicitly (11 maps, 11 wildcards, 0 admitting a listed
label), verified by script.

## The known example defects, and what each schema does with them

- **Example 20's `;base64url` URLs** (5, one per view that prints the
  enclosing presentation): `enveloped.derived#data-uri-vc` rejects all 5,
  as do `data-uri.derived.abnf` `vc-cose-data-uri` and RFC 2397's own
  `dataurl` (a parameter needs `=`). Its three secured presentations (the JWS
  payload, the COSE payload, the rebuilt SD-JWT claims) fail
  `payload.derived#jwt` / `payload.derived` on them.
- **Examples 10–14 are not JSON as printed** (Example 10, Example 11, Example 12, Example 13, Example 14): no schema can be applied
  to them, and they are not repaired here. Examples 15–17 parse and are run
  against `cid-verification-method.derived.schema.json`; Example 17's
  JsonWebKey2020 method fails it, and so does Example 17 under `#document`.
- **The `+ld+json` typ and cty of Examples 6, 9, 21 and 22**: the MUST-level
  `jose-header.derived` root accepts all 6 headers (it fixes no typ value);
  the SHOULD profiles `#vc-sd-jwt-should` / `#vp-sd-jwt-should` reject all 6.
  Example 22's SD-JWT also fails the `sd-jwt.derived` root (KB-JWT followed by
  `~`; no `sd_hash`).
- **alg -35 with 64-octet signatures**: no schema here sees a signature's
  length or the key behind it; the CDDL accepts all seven COSE objects at the
  MUST level (14 verdicts) and rejects them at the SHOULD level (14 verdicts),
  for the missing typ, not for the algorithm. RFC 9053, which defines the
  lengths, is not a reference of the source; F-16 records the mismatch.

## Findings — source defects and observations

Recorded, never repaired. Quotations are verbatim from the rendering; a
number is the `.txt` line. Facts about the examples were measured on the
instances decoded from the HTML.

**In the normative text**

- **F-01** §3.1.2 (line 273) and §3.2.2 (line 513), sections about
  presentations, both say the content type can express a more specific media
  type “than application/vc when one is available” (§3.1.2); the COSE presentation twin says “than application/vp when one is available” (§3.3.2) (line 710). The JOSE and SD-JWT
  presentation sentences name the credential type. The `#vp-jwt-should` and
  `#vp-sd-jwt-should` comments say so where they quote it.
- **F-02** The SD-JWT verifier MUSTs w3c-vc-jose-cose#R-0030 and w3c-vc-jose-cose#R-0036 (lines 379, 514) verify
  “conforming JWS documents” (w3c-vc-jose-cose#R-0030); §1.1.1 calls what an SD-JWT verifier verifies “A conforming SD-JWT verifier implementation verifies conforming SD-JWT documents” (§1.1.1).
- **F-03** §3.2.1, the SD-JWT section, opens “This section details how to use JOSE to secure verifiable credentials” (§3.2.1) (line 376); §3.2.2 says
  “This section details how to use [SD-JWT] to secure verifiable presentations” (§3.2.2) (line 511).
- **F-04** “JWK claim iss SHOULD NOT be set to a value which conflicts with the value of verifiable credential property issuer.” (§3.1.3) (line 368, §3.1.3): iss is a JWT claim (RFC 7519 §4.1.1), not a
  JWK one. Also noted in `requirements.yaml`.
- **F-05** §1.1.2.2 (line 155) describes disclosures as arrays containing “the digest of the disclosed claim, the claim name, and the claim value” (§1.1.2.2).
  The first element is a salt, as the next list item says (“Each disclosable claim is combined with a salt value before hashing to prevent dictionary attacks.” (§1.1.2.2)) and RFC 9901
  §4.2.1 requires. Measured: all 35 printed disclosures have three elements,
  the first a 22-character base64url string equal to none of the 35 digests.
- **F-06** “a JWK Thumbprint URI as defined in [RFC7638]” (w3c-vc-jose-cose#R-0073) (line 820): RFC 7638 defines the JWK Thumbprint and no URI
  (0 occurrences of `jwk-thumbprint` or `urn:ietf` in it); the URI form in the
  example after the sentence is RFC 9278's, which the source does not cite
  (normative.md SD-34).
- **F-07** §5.2 covers credentials only: “inputMediaType: vc+sd-jwt” (§5.2) (line 885), “inputDocument: the verifiable credential secured with [SD-JWT]” (§5.2) (line 886), “Set mediaType to vc” (§5.2)
  (line 891), under a heading and a lead-in (line 887) that name credentials
  or presentations, while §3.2.2 defines vp+sd-jwt. §5.1's “inputDocument: the verifiable credential secured as a JWT [RFC7519]” (§5.1) (line 868)
  names only a credential, under “inputMediaType: vc+jwt or vp+jwt” (§5.1) (line 867). `verification-result#sd-jwt`
  follows §5.2 as printed.
- **F-08** w3c-vc-jose-cose#R-0049 and w3c-vc-jose-cose#R-0055 carry no When present, unlike the JOSE cty twins, and
  the next sentence says “The content type (3) header parameter is optional” (§3.3.1) (lines 628, 710). The CDDL's SHOULD level reads
  the parameter as optional and constrains it only when present (inferred).
- **F-09** §3.3 (line 622) permits COSE for credentials only (“Verifiable credentials MAY be secured using COSE [RFC9052]” (w3c-vc-jose-cose#R-0045)); §3.3.2
  secures presentations with COSE too.
- **F-10** §3.1.3 is marked non-normative yet carries MUST NOT, MUST,
  RECOMMENDED, NOT RECOMMENDED, SHOULD and SHOULD NOT (lines 365–370). For
  JOSE, nothing normative states the `nbf` advice, the registry advice or the
  rule to ignore header parameters that are not understood; RFC 7515
  §4.1.11 makes a `crit`-listed parameter that is not understood invalid,
  the opposite. §1.1.1 still defines a conforming JWS document by the MUST
  statements of §3.1, which contains §3.1.3 (`requirements.yaml`,
  reconciliation (b)).
- **F-11** §3.3.3 (line 783) cites I-D.ietf-cose-cwt-claims-in-headers, which
  is in neither reference list (C.1, C.2); the HTML links revision 10, whose
  table gives the label as TBD with assignment 15 requested. RFC 9597 assigned
  15 in June 2024, before this Recommendation (15 May 2025). [SD-JWT] is cited
  as an Internet-Draft with no revision; RFC 9901 (November 2025) is its
  published form, and is what the schemas import.
- **F-12** §4.1.2 and §4.1.3 name iss and cnf “If iss is present in the JOSE Header, the JWT Claims, or the COSE Header” (§4.1.2) / “If cnf is present in the JOSE Header, the JWT Claims, or the COSE Header” (§4.1.3): COSE has no header
  parameter of either name. The CDDL reads them as CWT Claims (15) keys 1 and
  8 (inferred).
- **F-13** §6.1.1–§6.1.4, Encoding considerations: “application/jwt values are a series of base64url-encoded values (some of which may be the empty string) separated by period ('.').” (§6.1.1). That admits the empty
  signature of an unsecured JWT, which w3c-vc-jose-cose#R-0005 and w3c-vc-jose-cose#R-0023 exclude; the schemas reject an
  empty segment (inferred).
- **F-14** Typography: “secured withCOSE” (§3.3.2) (line 716, the Example 8 title); “a controlled identifier documents” (§4.2) (line 819); “evaluated according the verifier's validation policies” (w3c-vc-jose-cose#R-0078)
  (line 920); “Applications that will use this media:” (§6.1.1) in all six templates (lines 945, 971, 997, 1023, 1049, 1075).
  Lines 380 and 518 write “are NOT selectively disclosable” (§3.2.1), a capitalised NOT outside any BCP 14 phrase.

**In the examples** (non-normative, by §1.1)

- **F-15** No outer header of a secured example carries a typ: 12 of 12 JOSE
  headers (6 JWS, 6 SD-JWT) have none, and every encoded COSE protected header
  (7 of 7, Examples 7, 8, 9, 18, 19, 20, 23) decodes to `{1: -35}` alone, with no
  typ (16) and no content type (3); Example 26's is printed elided after its
  first entry. The typ values carried inside data: URLs, by the presentation
  Examples 6 and 9 envelope and by Examples 21 and 22, are F-19 and F-20. Each deviates from the typ SHOULDs (w3c-vc-jose-cose#R-0013, w3c-vc-jose-cose#R-0018, w3c-vc-jose-cose#R-0028, w3c-vc-jose-cose#R-0034, w3c-vc-jose-cose#R-0048, w3c-vc-jose-cose#R-0054).
- **F-16** The COSE examples declare alg -35, ES384 (“| ES384 | -35 | SHA-384 | ECDSA w/ SHA-384 |” (RFC 9053 §2.1)), with 64-octet
  signatures (7 of 7); RFC 9053 suggests SHA-384 only with P-384, whose
  signature is 96 octets. The JOSE examples' ES256 signatures are 64 octets and
  Example 2's enclosed ES384 credential's is 96. This lane verified no
  signature: the source prints no public key for `kid` ExHkBMW9fmbkvV266mRpuP2sUY_N_EWIN1lapUzO8ro.
  examples/README.md tried every printed key against every signature: of the 26
  distinct signatures only Example 22's KB-JWT verifies (D-08).
- **F-17** Of 30 EnvelopedVerifiableCredential `data:` URLs in the
  presentation examples (every view but the Issuer Disclosures tab, every
  depth), 1 decodes, Example 2's
  Presentation tab. Example 2's secured payload and its application/vp view,
  and the presentation enclosed in Example 3, carry that URL twice joined by
  `;`; Examples 5 and 8 put a space inside the SD-JWT (`... ~WyJ...`), Example 8
  also doubled; Example 20 elides (`eyVjV...RMjU`), doubles, and labels its COSE
  credential `;base64url` with data that decodes to the text
  `base64,0oREo...+Q==` (in its COSE view, to the base64url of that text);
  Example 23 encloses `data:application/vc-ld+sd-jwt,...`, a media type the
  source does not register, with the same space, doubled. The disclosed `id`
  values of Examples 5, 6 and 20 add a space after the comma. Examples 8, 20 and 23
  enclose credentials secured by another mechanism than the presentation's,
  which the second sentence of w3c-vc-jose-cose#R-0023 and its twins do not foresee.
- **F-18** Examples 10 and 12 carry `// ...` and are not JSON; Examples 11
  and 13 are identical, title and text, and leave the `kid` string unclosed
  (`"https://university.example/issuers/565049#key-123`); Example 14 has a
  trailing comma. The 12 decoded views of the SD-JWT examples indent with
  U+00A0 (12 of 12), so they are not JSON as printed; all parse once it is
  read as a space.
- **F-19** Examples 6 and 9 envelope a presentation whose SD-JWT header has
  typ `vp+ld+json+sd-jwt` and cty `vp+ld+json`, media types Appendix A says
  were replaced (line 1852), and whose presentation embeds an unsecured credential object,
  not an EnvelopedVerifiableCredential (w3c-vc-jose-cose#R-0037, w3c-vc-jose-cose#R-0039).
- **F-20** Examples 21 and 22 carry typ `vc+ld+json+sd-jwt`, cty `vc+ld+json`.
  Example 22, “A simple URI-encoded SD-JWT Verifiable Presentation” (§8.4), is a `data:application/vp+sd-jwt` URL whose payload is a
  VerifiableCredential under a credential typ, whose KB-JWT is followed by a
  further `~` (not RFC 9901 §4's compact form), and whose KB-JWT payload has no
  `sd_hash`, which RFC 9901 §4.3 marks REQUIRED.
- **F-21** The SD-JWT examples disclose selectively what w3c-vc-jose-cose#R-0031 and w3c-vc-jose-cose#R-0040 ask to keep
  disclosed: the top-level `type` in 6 of 6, `credentialSchema` members in
  Examples 4 and 19, `credentialStatus` members in Example 18.
- **F-22** Example 19's issuer is a DID (`did:web:contoso.example`): its JOSE
  and SD-JWT forms carry a `kid`, its COSE form none (w3c-vc-jose-cose#R-0065; X-03).
- **F-23** Examples 24 and 25 (CBOR diagnostic notation) write text unquoted
  (`3: application/vc`, `1: urn:example:123`) and elide bytes
  (`h'177f12cb...1933d554'`); Example 26 also omits the comma after `{}`.
  None can be encoded. Examples 24 and 25 carry content type (3) and CWT
  Claims (15) and no typ (16).
- **F-24** Example 2's Presentation tab writes the enclosed credential's type
  as the array `["EnvelopedVerifiableCredential"]`, its secured payload as the
  string; VC-DATA-MODEL-2.0 says “The type value of the object MUST be EnvelopedVerifiableCredential.” (VC-DATA-MODEL-2.0 §4.13) The schema accepts the one-element array
  (inferred).

**In imported documents** (not defects of this source; recorded because the
schemas import them)

- **F-25** RFC 9052 §3.1: Table 3 types content type `tstr / uint`, the CDDL
  fragment after it `tstr / int`; the CDDL here follows the fragment.
- **F-26** RFC 8392: §3.1.3 admits an `aud` array, its Table 1 lists `aud` as
  text string; the CDDL follows §3.1.3.
- **F-27** The RECOMMENDED on CWT Claims placement reads “It is RECOMMENDED that the CWT Claims header parameter is used only in a protected header” (draft-ietf-cose-cwt-claims-in-headers-10 §2) in revision 10 and
  “It is RECOMMENDED that the CWT Claims header parameter only be used in a protected header” (RFC 9597 §2) in RFC 9597; the CDDL quotes the revision the source links.

## Checks

Run 2026-11-03 in a scratch directory outside the repository (scripts not
committed), with `python3 -I` and `bin/` on the path explicitly. Every check
names what it examined.

- **Source digests.** `.bin` and `.txt` re-hashed before every run; both equal
  the values above.
- **Grammar search.** As above: 0 grammar in 1980 rendering lines and 56 `<pre>`
  blocks; 13 HTML rule-shape matches, all in `<script>`/`<style>`.
- **Verbatim.** Each of the 11 regions equals its `.txt` line range byte for
  byte; 215 of 215 region cells found in the HTML of their own display.
- **Example decoding.** 26 example blocks; 56 `<pre>`, 33 of them JSON as
  printed; 6 compact JWS and 6 SD-JWT rebuilt from their `<span>` parts, each
  equal to its `.txt` line with the span-boundary spaces removed (6 and 6);
  35 of 35 printed disclosure digests recomputed; 6 COSE hex objects and
  Example 23's base64 decoded (cbor2); 41 `data:` URL occurrences walked at
  every depth, in every view but the Issuer Disclosures tab, whose 5 reprints
  make 46 (23 distinct values); 29 secured objects and 30 enclosed credential
  URLs measured for the cross-field rules. Re-run in the cross-check pass
  (2026-11-05) against the edited schemas: the 375 JSON Schema and ABNF
  verdicts as expected, 18 of 18 mutations still flipping their negative.
- **JSON Schema.** 6 schemas, each valid against the 2020-12 metaschema
  (`jsonschema` 4.26.0, `Draft202012Validator.check_schema`); 46 `$ref`s, all
  resolved through one registry; `$id` of each is `urn:library:w3c-vc-jose-cose:<name>.derived`.
  150 verdicts on example instances and 123 on synthetic ones, every one as
  expected (117 accepts, 156 rejects; with the ABNF's 48 and 54 below, 165
  and 210; before the cross-check pass dropped the §6 parameter rule, E-09
  and E-09-abnf were rejects: 116 and 157, 47 and 55, 163 and 212). Two of the expectations written
  before the run were wrong, and in both the instance, not the schema, was
  what the expectation had missed: Examples 6 and 9 enclose an unsecured
  credential (F-19), and an elision or a doubled `;data:` is a valid RFC 2397
  shape. 18 of 18 mutations flipped their negative.
- **ABNF.** Loaded by the Python `abnf` library 2.9.1 (RFC 5234 parser).
  Structural: 32 rules, 56 references (50 before the six media-type rules
  took a parameter list), every one defined here or an RFC 5234
  core rule, every rule reachable from the seven top rules. 81 verdicts on example `data:`
  URLs and 21 on synthetic strings, all as expected; on the 58 strings both the
  JSON Schema and an ABNF media-type rule judged, they agree 58 times of 58.
  RFC 2397 `dataurl` alone accepts 27 of the 41 example URLs.
- **CDDL.** The cddl gem 0.12.14 (Ruby 2.6) validated 63 instances against the
  roots each names, 138 verdicts, 0 mismatches; `generate` ran from four roots
  (12 runs, all produced output). Structural: 33 rules, 0 references
  undefined; 11 maps, 11 wildcards, 0 admitting a listed label. Mutations and
  the cut probe as above.
- **YAML.** `cross-field-rules.derived.yaml` read by `bin/_yaml.py` and
  `bin/_record_yaml.py`; leaf values compared, 0 differences; each of its
  requirement entries has text, locator and level equal to
  `requirements.yaml`.
- **Quotations.** Every quotation was asserted by script when written, as a
  whole span of the text it is attributed to: 42 sites of requirement texts,
  53 of one `.txt` line of the attributed source section (never joined across
  lines), 73 of the attributed section of a foreign document, across the
  derived files and this README. The audit after writing re-extracted every
  delimited quotation from the finished files, longest first, and resolved
  each against its attribution: 190 examined, 190 resolved exactly, 0 through a
  relaxation channel, 0 unresolved. The audit counts printed spans, the
  generators calls: 190 spans less 2 names quoted inside a CDDL quotation (Initialization Vector, Partial Initialization Vector) is 188, the 168 calls plus 20 reuses of a quotation defined once and printed again (the four JOSE profiles each print the same RFC 7515 sentences; the two data: URL definitions share theirs); 0 runs of ten or more words of our
  prose occur verbatim in the source outside a quotation; the 14 YAML `text:`
  values, whole-scalar quotations, each equal their requirement. Planted
  into a copy, an elision splice, a healed line-break hyphen and an
  undelimited sentence were each reported (unresolved with its splice
  prefix, the named heal channel, and the sweep).
- **Ids.** Every requirement id was selected from `requirements.yaml` by a
  selector that raises unless exactly one entry matches; 66 distinct ids are
  cited across the files, every one exists, and each citation's resolved text
  was printed and read.
- **Headers.** For every file but this one, the first of `derived` /
  `verbatim` in its first 12 lines agrees with its name; no file contains
  the string the gate rejects.


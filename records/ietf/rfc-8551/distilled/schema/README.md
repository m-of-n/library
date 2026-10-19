---
record: rfc-8551
kind: schema
title: "rfc-8551 — schemas"
extracted: "2026-10-19"
reviewed_by: ""
---

# RFC 8551 — schemas

RFC 8551 publishes **one** piece of formal syntax: the 1988-syntax ASN.1
module `SecureMimeMessageV3dot1` in Appendix A. It prints **no** ASN.1, OID
assignment, ABNF or other grammar inline in its body (§2.5.2 and §2.5.3
describe `SMIMECapabilities` and `SMIMEEncryptionKeyPreference` in prose
only). What the body does print is a set of tables, a definition list, a
displayed rule and two IANA registration templates; those are copied verbatim
into `inline.verbatim.txt`. Everything else here is **derived**: this
library's machine-checkable rendering of prose, named `*.derived.*`.

| file | kind | source | source lines | lines removed | what it does NOT cover |
|---|---|---|---|---|---|
| `SecureMimeMessageV3dot1.asn1` | **verbatim** | Appendix A, "ASN.1 Module" | 3152–3243 | 3194 (page footer), 3195 (form feed), 3196 (running header); uniform 3-space margin removed | the CMS types it imports (`SubjectKeyIdentifier`, `IssuerAndSerialNumber`, `RecipientKeyIdentifier`, from `CryptographicMessageSyntax`); the Appendix A heading and Note (3143–3150), which are prose; any modern-syntax module (the Note points to [RFC6268]) |
| `inline.verbatim.txt` | **verbatim** | 13 regions, §1.3 – §5.3; region table below | per region | none: no region crosses a page break; margin kept | prose; the sample messages (examples lane); the Step lists (protocol lane) |
| `smime-media-types.derived.schema.json` | **derived** (JSON Schema 2020-12, `$id` `urn:library:rfc-8551:smime-media-types.derived`) | §3.2, §3.2.1, §3.2.2, §3.3–§3.8, §3.5.3.2, §3.10, §5.1, §5.2 | — | — | raw header syntax (quoting, folding, case): see the ABNF; CMS content inside the entity (eContent absent, signerInfos empty, content-type OIDs: R-0021–R-0024, R-0115, R-0122, R-0123), which is ASN.1/CMS and belongs to `messages.yaml`; the inner MIME entity (canonicalization, transfer encoding §3.1) |
| `multipart-signed-content-type.derived.abnf` | **derived** (ABNF, RFC 5234) | §3.5.3.2, lines 1876–1938 | — | — | the rest of the multipart/signed Content-Type (RFC 2045 / RFC 1847 rules `token`, `quoted-string`, `parameter` are imported by name, not defined); parameter order and the presence rule (stated in a comment) |
| `algorithm-requirements.derived.yaml` | **derived** (YAML table) | §1.3, §2.1–§2.3, §2.7, §2.7.1.2, §4.1–§4.5, §6 | — | — | algorithm OIDs (the source prints only one, AES-128 CBC, line 1559); Appendix B historic algorithms (informative); §2.4–§2.6 content-type, attribute and SignerIdentifier rules (in `requirements.yaml`) |

Source: `.cache/rfc-8551.txt`, sha256
`dac39f749a08d3422bd78d4e492195067e7bc03f5fc2d0dac515f0d7ed884ae2`,
3531 lines, 63 pages, 63 form-feed lines. RFC 8551 as published, April 2019.

## The module

`SecureMimeMessageV3dot1.asn1` opens with a 12-line `--` header (the
provenance, the edits, and the line `-- END HEADER`), then the module from its
identifier line to `END`, byte for byte with the source after the two edits
the header names. Digests: the module body (everything after
`-- END HEADER`, 89 lines, 2634 bytes) has sha256
`01776a78e65ec682418274e58d0e1130b6d158ea0b80da5f68ab660a2561ebda`; the same
89 source lines with the RFC margin kept have sha256
`a3fa6df52b34a76fda9183d3ffd75aed4a7c203b951ed41e5c3249138c157930`. To feed
the module to an ASN.1 tool, drop the first 12 lines.

| | as printed |
|---|---|
| module reference | `SecureMimeMessageV3dot1` (line 3152) |
| module identifier | `{ iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) modules(0) msg-v3dot1(21) }` (lines 3154–3155) |
| dotted (ours, read off the arcs) | 1.2.840.113549.1.9.16.0.21 |
| tag default | `DEFINITIONS IMPLICIT TAGS ::=` (line 3157) |
| ASN.1 version | 1988 (Note, lines 3149–3150); uses `ANY DEFINED BY` (line 3185) |
| exports | none stated (no EXPORTS clause) |
| imports | `SubjectKeyIdentifier, IssuerAndSerialNumber, RecipientKeyIdentifier FROM CryptographicMessageSyntax { ... modules(0) cms-2001(14) }` (lines 3161–3168) |

Assignments, live (not commented): `id-aa`, `smimeCapabilities`,
`SMIMECapability`, `SMIMECapabilities`, `id-aa-encrypKeyPref`,
`SMIMEEncryptionKeyPreference`, `id-smime`, `id-cap`,
`id-cap-preferBinaryInside`, `SMIMECapabilitiesParametersForRC2CBC` — 10.
Commented out (inside `--`): `md2WithRSAEncryption` (3227–3229) and
`signingTime` (3234–3236) — 2. The OID values, dotted (ours, read off the
printed arcs): `id-aa` 1.2.840.113549.1.9.16.2; `smimeCapabilities`
1.2.840.113549.1.9.15; `id-aa-encrypKeyPref` 1.2.840.113549.1.9.16.2.11;
`id-smime` 1.2.840.113549.1.9.16; `id-cap` 1.2.840.113549.1.9.16.11;
`id-cap-preferBinaryInside` 1.2.840.113549.1.9.16.11.1.

The module comment at lines 3176–3178 carries a BCP 14 keyword and is
requirement **rfc-8551#R-0150**. The `OPTIONAL` at line 3185 is the ASN.1
keyword, not BCP 14.

**Compilation.** No ASN.1 compiler is installed here (`asn1c` absent; python
`asn1tools` and `pyasn1` absent), so the module was not compiled. A compile is
expected to fail on the import of `CryptographicMessageSyntax` unless that
module is supplied, and some modern compilers reject the 1988 `ANY DEFINED
BY` form. Neither would be a defect of the extraction.

## Inline regions

Each region in `inline.verbatim.txt` has an id, its section, its line range,
and sits between `---- BEGIN VERBATIM I-nn ----` and `---- END VERBATIM I-nn ----`.
The digest covers the source lines with their line feeds, margin kept.

| id | section | display | source lines | sha256 |
|---|---|---|---|---|
| I-01 | §1.3 | requirement levels SHOULD+, SHOULD-, MUST- | 401–414 | `6ccbc41ade3ef9262b938a3078ff07c7345ed7691608713f69d9107a842348a7` |
| I-02 | §2.5.1 | UTCTime two-digit year rule (R-0034) | 852–853 | `d06ebdd11d96cae73f3ecb667a93f80b9f5f99320610fd467a047b12d9e0be88` |
| I-03 | §3.2.1 | media type → file extension table (R-0104) | 1488–1496 | `dd324cab4e706af0a906634cd61358eaaae787fee497f29d030a410058e36097` |
| I-04 | §3.2.2 | smime-type table | 1535–1541 | `9fc47cb3e188529e43175e49cb2e5b241817d61ab76744909596fc2035cb97c5` |
| I-05 | §3.5.3.2 | micalg table and footnote (R-0119) | 1919–1931 | `bf4b77543bd7f17815480117c19c815af205ad833168bf7202edd585b633e668` |
| I-06 | §3.10 | S/MIME identification table | 2149–2157 | `0b139b92fea8799e6c077a10a5298cbc600829f3bd47a0aa6a552abd3b99a1cd` |
| I-07 | §4.2 | signature generation key sizes (R-0130–R-0132) | 2212–2217 | `4e31f91410a4de5ace00683fffb70e9aa9888778e28e48752132b84b3bde38f5` |
| I-08 | §4.3 | signature verification key sizes (R-0133–R-0135) | 2226–2231 | `e4f4b65b9a64d53761db75d8430b66e04a7ba068f5f22eeeb7507298f24d7f12` |
| I-09 | §4.4 | encryption key sizes (R-0136–R-0138) | 2253–2258 | `4e31f91410a4de5ace00683fffb70e9aa9888778e28e48752132b84b3bde38f5` |
| I-10 | §4.5 | decryption key sizes (R-0139–R-0141) | 2268–2273 | `8d43cd51ce93629e1b723ce12000f89cd16177d8dc6595a6a072dd6831a3d615` |
| I-11 | §5.1 | media type template, application/pkcs7-mime | 2305–2342 | `6eaa1a163b19fc2106ba1299ff987953a576b796a046cd2eeb53cb908e2eeff6` |
| I-12 | §5.2 | media type template, application/pkcs7-signature | 2361–2397 | `90fd0a7bc79c0f6cd2dece7f6ddb1f6d6bf575f8e41b777e77fa9fdb4141fb11` |
| I-13 | §5.3 | smime-type registry entry | 2420–2422 | `57952abe853a2f9bb61cf6bcec05ae262036e22978ee21cfde00ce99a199169b` |

I-07 and I-09 have the same digest: §4.2 and §4.4 print identical tables.

## Coverage reconciliation — every formal display, by line

Every display in the source — anything set off from running prose as a
table, list of definitions, rule, template, code or sample — is accounted
for below. Mechanically: every line of the source containing `::=` lies inside
3152–3243 (checked; there are none outside the module).

| lines | section | display | where it is |
|---|---|---|---|
| 119–202 | ToC | table of contents | not formal; not copied |
| 320–379 | §1.2 | definitions list | prose definitions → `normative.md`; not formal syntax |
| 383–387 | §1.3 | BCP 14 boilerplate | not copied |
| 401–414 | §1.3 | requirement levels SHOULD+, SHOULD-, MUST- | **I-01**; used as the `levels` of `algorithm-requirements.derived.yaml` |
| 643–647, 659–668, 679–687, 693–705, 1037–1046 | §2.1, §2.2, §2.3, §2.7 | algorithm bullet lists | prose lists → `algorithm-requirements.derived.yaml` (each entry's text verbatim) |
| 805–813 | §2.5 | list of signed attributes | prose list → `requirements.yaml` R-0027; not formal |
| 852–853 | §2.5.1 | UTCTime year rule | **I-02** |
| 1243–1249, 1589–1603, 1645–1658, 1770–1779, 1857–1874, 2008–2027, 2095–2104 | §3.1, §3.3, §3.4, §3.5.2, §3.5.3.2, §3.6, §3.8 | Step 1–n procedures | procedures → protocol lane; not formal syntax |
| 1409–1437 | §3.1.4 | sample canonical MIME entity | examples lane |
| 1488–1496 | §3.2.1 | media type → file extension table | **I-03**; `smime-media-types.derived.schema.json` |
| 1535–1541 | §3.2.2 | smime-type table | **I-04**; `smime-media-types.derived.schema.json` `$defs/smimeTypeDefined` |
| 1547–1559 | §3.2.2 | smime-type assignment guidelines 1–3 | prose → `requirements.yaml` R-0109–R-0111 |
| 1611–1621, 1689–1713, 1801–1824, 2035–2040 | §3.3, §3.4, §3.5.2, §3.6 | sample application/pkcs7-mime messages | examples lane; their headers are the positive test instances of the JSON Schema (see *Checks*) |
| 1919–1931 | §3.5.3.2 | micalg table and footnote | **I-05**; JSON Schema and ABNF |
| 1969–1992, 1997–1998 | §3.5.3.3 | sample multipart/signed message; digested bytes in hex | examples lane; its headers are test instances of the JSON Schema and the ABNF |
| 2149–2157 | §3.10 | S/MIME identification table | **I-06**; JSON Schema `$defs/identifiesAsSmime` |
| 2212–2217, 2226–2231, 2253–2258, 2268–2273 | §4.2–§4.5 | RSA key-size tables | **I-07–I-10**; `algorithm-requirements.derived.yaml` `key_sizes` |
| 2305–2342 | §5.1 | media type template, application/pkcs7-mime | **I-11** |
| 2361–2397 | §5.2 | media type template, application/pkcs7-signature | **I-12** |
| 2420–2422 | §5.3 | smime-type registry entry | **I-13** |
| 2438–2444, 2567–2596 | §6 | attack list; preconditions list | prose → `normative.md`; not formal |
| 2671–3130 | §7 | reference conventions and references | not formal; not copied |
| 3152–3243 | App. A | ASN.1 module | **`SecureMimeMessageV3dot1.asn1`** |
| 3269–3437 | App. B | historic algorithm lists | informative prose; not copied (R-0151 is in `requirements.yaml`) |

## Derived artifacts — how to use them

- **`smime-media-types.derived.schema.json`.** The instance is a *parsed*
  entity header: `{mediaType, parameters, contentDisposition?}`, names
  lower-cased, values unquoted (this instance model is ours). Validate
  against the root for MUST-level conformance; against
  `urn:library:rfc-8551:smime-media-types.derived#should` for the
  sending-agent SHOULD rules (report as warnings); against `#identifies` for
  the §3.10 classifier. Every constraint carries a `$comment` with its lines
  and R-id. Received messages are *not* held to the `#should` micalg check:
  R-0120 asks receivers to recover gracefully.
- **`multipart-signed-content-type.derived.abnf`.** The only place R-0117
  (the protocol value must be quoted) is checkable, since the JSON Schema sees
  unquoted values. It imports RFC 2045 `token` by name.
- **`algorithm-requirements.derived.yaml`.** One entry per algorithm
  requirement, keyed by R-id, with the source's own text; `test_as` maps
  MUST- to MUST and SHOULD+ to SHOULD per §1.3. Key-size rows give inclusive
  `[min, max]` bit ranges.

Inferences are marked in the files with the word *inferred*; each one is a
reading this library made, not a statement of the RFC.

## Findings — source defects and observations

Recorded, never repaired. Quotes are verbatim, line breaks read as one space.

1. **§7.1 swaps the [SMIMEv3.1] and [SMIMEv3.2] reference sets.** Lines
   2695–2699: “[SMIMEv3.1] refers to [RFC2634], [RFC5035], [RFC5652],
   [RFC5750], and [RFC5751].” and “[SMIMEv3.2] refers to [RFC2634],
   [RFC3850], [RFC3851], [RFC3852], and [RFC5035].” §1.4, lines 433–437, says
   the opposite: v3.1 “is described in RFC 2634, RFC 3850, RFC 3851, RFC 3852,
   and RFC 5035” and v3.2 “is described in RFC 2634, RFC 5035, RFC 5652,
   RFC 5750, and RFC 5751”.
2. **The Appendix A Note mis-tags RFC 5751.** Lines 3145–3146: “unchanged from
   RFC 5751 [SMIMEv2] and RFC 3851 [SMIMEv3.1]”. [SMIMEv2] is RFC 2311–2315
   (lines 2680–2681; §1.4 lines 427–428), and RFC 5751 is v3.2 (§1.4 line
   437). By §7.1 as printed (finding 1), RFC 3851 would be [SMIMEv3.2], not
   [SMIMEv3.1]; by §1.4 it is v3.1.
3. **`id-aa` names arc 840 `usa`, every other OID in the module `us`.** Line
   3173 `{iso(1) member-body(2) usa(840)` against lines 3154, 3167, 3210 (and
   the commented 3228, 3235) `us(840)`. The number is the same, so the OID
   value is unaffected; a strict compiler may warn on the name (inferred).
4. **`receipentKeyId` is misspelled** (line 3203). The source says so itself
   and keeps it (lines 3207–3208).
5. **Imported module identity is not checkable from this source.** The module
   imports from `CryptographicMessageSyntax { ... modules(0) cms-2001(14) }`
   (lines 3166–3168), while [CMS] is defined as RFC 5083 and RFC 5652 (line
   2673). Whether RFC 5652 publishes a module of that name and identifier is
   outside RFC 8551 and is not checked here (open question for the
   cross-check pass).
6. **The OID list at line 3221 is empty.** “-- The following is a list of
   OIDs to be used with S/MIME v3.” is followed only by commented-out
   definitions (`md2WithRSAEncryption`, `signingTime`). No live OID follows.
7. **The capability comment is narrower than §2.5.2.** Lines 3176–3177:
   “S/MIME Capabilities provides a method of broadcasting the symmetric
   capabilities understood.” §2.5.2 (lines 860–863) says the attribute
   “includes signature algorithms ..., symmetric algorithms ..., authenticated
   symmetric algorithms ..., and key encipherment algorithms”.
8. **RC2 survives in the module.** `SMIMECapabilitiesParametersForRC2CBC`
   (lines 3240–3241) remains, while §2.7.2 (line 1139) calls RC2 weak and the
   §1.6 change log (lines 539–540) says “References to RC2/40 removed” from
   Appendix A. The type concerns RC2 key length generally, not RC2/40 only, so
   this is an observation, not a contradiction.
9. **smime-type guideline 1 vs the defined value.** Guideline 1 (lines
   1547–1549) says the three values to assign are “"signed-*", "authEnv-*",
   and "enveloped-*"”; the value this document defines and registers is
   `authEnveloped-data` (lines 1541, 1661, 2420), not `authEnv-data`.
10. **application/pkcs7-signature: template vs sample.** §5.2 (line 2367):
    “Optional Parameters: N/A”. The §3.5.3.3 sample nevertheless sends
    `name=smime.p7s` (line 1980), and the §3.2.1 table (I-03) gives `.p7s` an
    extension. The JSON Schema accepts the parameter (inferred).
11. **RSA-OAEP / RSAES-OAEP.** §4.4 line 2250 “RSA and RSA-OAEP”; §4.5 line
    2265 and §2.3 line 705 “RSAES-OAEP”. Same algorithm, two names.
12. **application/pkcs7-signature is not a §3.10 criterion.** Table I-06
    lists application/pkcs7-mime, multipart/signed with the protocol
    parameter, and application/octet-stream with a suffix. A detached
    signature part is identified only through its multipart/signed parent
    (or as octet-stream with `.p7s`); the JSON Schema's `#identifies`
    reflects the table as printed.
13. **Typographical:** “File extensions(s)” in both templates (lines 2330,
    2385).

## Checks

Run 2026-10-19 from the session scratchpad, outside the repository, with
`python3 -I` (scripts not committed; they read `.cache/rfc-8551.txt` and
check its digest first).

- **Verbatim, exact.** The module body equals source lines 3152–3193 and
  3197–3243 with the 3-space margin removed, line for line (every one of
  those lines starts with the margin or is empty, and none is a page
  artifact). Each of the 13 inline regions equals its source line range
  exactly. All pass. Independently, `grep -v -x -F -f` of the source
  against `inline.verbatim.txt` leaves only header, marker and blank lines.
- **Every `::=` in the source** lies inside 3152–3243. 13 lines carry it:
  the `DEFINITIONS` line, 10 live assignments, 2 commented out.
- **Claims.** The first of *derived* / *verbatim* in each file's first 12
  lines agrees with its name, for all five files.
- **JSON Schema.** Parses; valid against the draft 2020-12 metaschema
  (`jsonschema` 4.10.3); `$id` is `urn:library:rfc-8551:smime-media-types.derived`.
  The headers of the six source samples (§3.3 lines 1611–1614, §3.4
  1689–1692, §3.5.2 1801–1804, §3.5.3.3 1969–1972 and 1980–1982, §3.6
  2035–2038) pass the root and `#should`; the five application/pkcs7-mime
  and multipart/signed ones are identified by `#identifies`, and the
  application/pkcs7-signature part is not (finding 12). Three MUST-level
  negatives (wrong protocol, no micalg, empty micalg element) fail the root;
  five SHOULD-level negatives (no smime-type, certs-only named `.p7m`,
  9-character base, `rsa-sha1`, no Content-Disposition) pass the root and
  fail `#should`.
- **ABNF.** No ABNF tool is installed; the two rules were hand-translated
  to regular expressions and matched against the sample's own parameters
  (line 1970 `micalg=sha-256`, line 1972
  `protocol="application/pkcs7-signature"`) and against the unquoted
  protocol and the unquoted comma list, which are rejected.
- **YAML table.** Parses. Each of its 26 `text` values equals the text of
  the requirement it names in `requirements.yaml` and is a substring of the
  unwrapped source; each key-size row's source line equals its
  requirement's text; every R-id cited in a derived file exists (39 cited
  in the table).
- **ASN.1 compile.** Not run: no compiler available (see *The module*).

---
record: pics-dsig-1-0
kind: schema
title: "pics-dsig-1-0 — schemas"
extracted: "2026-11-12"
reviewed_by: ""
---

# PICS Signed Labels (DSig) 1.0 — schemas

The source publishes **no CDDL, JSON Schema or ASN.1**. It prints its formal syntax as three
"modified BNF" displays (HTML `<pre>`), copied here verbatim. Everything else in this directory is
**derived**: a recogniser this library wrote, named `*.derived.*`.

Source: `.cache/pics-dsig-1-0.bin` (the REC HTML, `content.sha256` in `record.yaml`); line numbers
count in its rendering `.cache/pics-dsig-1-0.txt`. The source has no section numbers: the
`§` ordinals below are the renderer's structural ordinals, given with the heading title.

## Verbatim

| file | section | `<pre>` no. / HTML line | rendering lines | content |
|---|---|---|---|---|
| `resinfo-syntax.verbatim.txt` | §7.2.1 (Detailed Syntax of the resinfo Extension in a PICS 1.1 Label) | 5 / L738 | 220-255 | `resinfo-extension`, `resinfo-data`, `HashAlgoID`, `quotedURL`, `resource-hash`, `hash-date`, `quoted-ISO-date` with its key and two notes |
| `field-list-syntax.verbatim.txt` | §7.3.4.7 (The "include" and "exclude" tokens: modifying the canonicalized form of the label) | 18 / L1072 | 393-396 | `field-list`, `option-list`, `ratings-list`, `extension-list` |
| `sigblock-syntax.verbatim.txt` | §7.4.2 (Detailed Syntax of the sigblock Extension in a PICS 1.1 Label) | 20 / L1143 | 439-495 | `SignatureExtension`, `Certificate`, `Signature`, `SigData`, `SigInfo`, `quotedName`, `urlChar`, `number`, `quoted-ISO-date` (repeated) |

Each file has a header (a `#` comment block ending at the `BEGIN VERBATIM` line); every line after it is
the `<pre>` block. One normalisation, applied to all of them and to the fixtures: tags (`<B>` and
`<I>`, which mark nonterminals) dropped, character references decoded, U+00A0 written as U+0020,
CRLF as LF. `../examples/reproduce.py` re-reads the HTML with `html.parser` (the files were cut with a
regular expression) and checks all three byte for byte, and the lines against the rendering.

These are the only grammars in the source. There is **no** grammar for the `include`/`exclude`
SigData values beyond the `field-list` display, none for the signature suites, and none for
`ByKey`, `ByHash`, `ByName`, `ByCert`, `on`, `SigCrypto` beyond the `SigData` production.

## Derived

| file | what it is |
|---|---|
| `check-grammar.derived.py` | a recogniser for a PICS 1.1 label list that carries the two DSig extensions, built from the three displays above and the PICS 1.1 label grammar. `python3 -I check-grammar.derived.py` runs **46 cases** (17 accept, 29 reject) and prints the reason each reject is made. Two profiles (`pics11`, `dsig`) and two strictnesses (strict, placeholder). |
| `mutate-grammar.derived.py` | removes one rule at a time from a scratch copy and runs the cases: **13 mutations, 12 killed, 1 equivalent, 0 survived**. The equivalent one drops the base64 length test alone; `b64decode(validate=True)` rejects the same strings, so no case can tell them apart (dropping both is killed by R-16). |

### What the recogniser answers

- **`pics11`**: is the text a valid PICS 1.1 label list, with extension data read by PICS 1.1's own
  `data` production (`quoted-ISO-date | quotedURL | number | quotedname | '(' data* ')'`)?
- **`dsig`**: the PICS 1.1 structure, plus section 7.2.1 and 7.4.2 applied to the two DSig extensions,
  plus the rules the prose states and the BNF cannot (at most one include or exclude; two hashes with one
  algorithm are invalid; resinfo not in a generic label; a sigblock only as a label option; both
  extensions `optional`; one extension URL at most once per option set).
- **strict**: `base64String` is RFC 1521 base64. The source's placeholders (`"base64 hash"`,
  `"base64-x.509-cert"`) and two printed values of length 13 and 17 are then rejected.
- **placeholder**: any quotedName is also accepted at a base64 position. **Not the source's
  grammar**; every use is reported.

Where the BNF is ambiguous the file picks one reading and lists it in `AMBIGUITIES` (A1 to A7); the
reading is the lane's, not the standard's. Not modelled, and an input that needs it raises
`Unmodelled` rather than being accepted: the `error` forms of PICS 1.1, the HTTP request extension, URL
syntax beyond `scheme:` plus URL characters (RFC 1738, not in hand).

### Instances the derived grammar must REJECT (a schema that parses binds nothing)

Each is a case with a stated reason; the recogniser must refuse it **for that reason** (checked by
reading the reasons, then by mutation).

| case | text | rule |
|---|---|---|
| R-01 | resinfo with no hash | `resinfo-data+` |
| R-02 | two hashes, one algorithm | §7.2 usage notes |
| R-03, R-16 | hash or ByHash that is not base64 / length not a multiple of four | `resource-hash`, RFC 1521 |
| R-04, R-05, R-06 | month 13; no time zone; minute 60 | `quoted-ISO-date` |
| R-07 | `mandatory` resinfo | both DSig extensions are `optional` |
| R-08 | resinfo in a generic label | §6.2 |
| R-09 | sigblock with no `("AttribInfo")` | `AttributionInfo` has no `?` |
| R-11, R-12 | a Signature with no SigData; suite id that is not a URL | `SigData+`, `SignatureSuiteID` |
| R-13 | include and exclude together | §7.3.4.7 |
| R-14, R-23 | a SigData with two SigInfo (the shape of the §7.3.4.2 DSA example) | `SigData` |
| R-15 | `on` that is not a date | §7.3.4.6 |
| R-18 | sigblock as a service option | §7.3.1 |
| R-19, R-20 | certificate family that is not a URL; certificate data that is neither base64 nor a URL | `Certificate` |
| R-21 | the same extension URL twice | PICS 1.1 |
| R-22, R-24, R-25 | empty exclude; field-list out of order; extension-list entry that is not a URL | `field-list` vs `SigData` |
| R-26, R-27 | no ratings; version other than PICS-1.1 | PICS 1.1 label list |

## DSig's grammar against PICS 1.1's — verified from both sources

The PICS 1.1 grammar is the `<pre>` of pics-1-1-labels, section "General Format of PICS Labels"
(`.cache/pics-1-1-labels.bin`, HTML line 419; `.cache/pics-1-1-labels.txt` lines 150-219). Compared with
the two displays here:

| item | PICS 1.1 | DSig 1.0 |
|---|---|---|
| extension data | `data :: quoted-ISO-date \| quotedURL \| number \| quotedname \| '(' data* ')'` | adds `quotedBase64String` (`resource-hash`, `CertificateData`, `SigInfo`) |
| `urlchar` | `transmit-name-char \| '(' \| ')'`, **no `/`** | `urlChar` lists `'/'` (L461) |
| `quotedname` | `'"' urlchar-or-space+ '"'` | `quotedName ::= '"' ( urlChar \| ' ')+ '"'`, so wider by `/` |
| date | `YYYY.MM.DDThh:mmStz`; separator `.`; minutes 00-60 | separator `.` or `-`; optional seconds and fraction; minutes 00-59 |
| `sign` | `'+' \| '-'` | `'+' / '-'` |

So DSig 1.0's own note (L437) that its extension "is not a valid PICS 1.1 extension because Base64
encoding uses a '/'" is shown by case **P-02**: base64 with `/` is rejected under `pics11`,
accepted under `dsig`. The note sits under sigblock only; the same holds for a resinfo hash that contains
`/` (**P-06**; our arithmetic: about 35 percent of 20-byte digests). The note's reason is itself
inconsistent with DSig's own grammar, whose `quotedName` accepts `/` (**N-01**, **N-02**).
`quotedURL` "as described and extended in Rating Services and Rating Systems" is a third document, not
read here: the source's claim that `quotedURL` allows `/` is taken as stated. The derived `pics11`
profile uses a URL reading of `scheme:` plus URL characters. Findings F-01 and F-02 in `../messages.yaml`.

Lexical leniency the cases also show: a hyphenated DSig date, `"1996-12-02T22:20-0000"`, is not a PICS 1.1
date but **is** a PICS 1.1 `quotedname` (P-04), and base64 without `/` is too (P-03). So a PICS 1.1
parser reads most DSig labels, and fails only on `/`.

## Checks

`python3 -I check-grammar.derived.py` prints `CASES 46: 17 accept, 29 reject; DIFFERING from expectation 0`.
`python3 -I mutate-grammar.derived.py` prints `MUTATIONS 13: 12 killed, 1 equivalent, 0 survived`.
`python3 -I ../examples/reproduce.py` parses the eight example fixtures with this recogniser.

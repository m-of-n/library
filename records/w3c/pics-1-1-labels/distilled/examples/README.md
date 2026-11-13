---
record: pics-1-1-labels
kind: examples
title: "pics-1-1-labels — examples and test vectors"
extracted: "2026-11-12"
reviewed_by: ""
---

# PICS 1.1 Label Distribution — examples and test vectors

FX-1 pass 1, examples lane (mechanical, smaller model). Every fixture is the
text of a `<pre>` block of the W3C Recommendation HTML, `.cache/pics-1-1-labels.bin`
(sha256 equal to `content.sha256` in `record.yaml`, recomputed). None comes from
the `.txt` rendering; its line numbers are only used to say where each example sits.
**The source has no section numbers**: `§11.1` below is the renderer's structural
ordinal (`bin/render-w3c --ordinal`), given with the heading title.

The HTML has 24 `<pre>` blocks (counted by script). 19 are fixtures here, 4 are the
grammars in `../schema/*.verbatim.txt`, and block 15 is the Acknowledgments list.
The source prints **no test vector**: no MD5 or signature value, no byte-level
example, no hex. What it has is label lists, the headers that carry them, and
bureau queries and answers. There are no vectors with a computed expected result
beyond those below.

`reproduce.py` re-extracts every `<pre>` by a method independent of the writer
(regular expressions and `html.unescape`; the writer used `html.parser`), diffs each
fixture and each verbatim grammar file, then parses each example against the derived
grammar in `../schema/` and compares the outcome with the EXPECTED one in this file:

```sh
python3 -I distilled/examples/reproduce.py [path/to/pics-1-1-labels.bin]
```

It prints `EXAMINED 212 checks, 0 FAILED` and exits 0 only if every fixture is
byte-identical and every outcome is the expected one. Appending one byte to a
fixture makes it exit 1 (tested on `ex02`).

## Fixtures (19)

A fixture is the `<pre>` text as the browser would show it: tags dropped, character
references decoded (so `&amp;#39;` in the HTML is `&#39;` here, the entity the
section means to show), the newline right after `<pre>` removed, nothing else
changed. There is **no derived fixture**: where a repair is needed to make an
example parse, `reproduce.py` applies it to a copy and reports it, and the fixture
stays as printed.

| id | file | where | `<pre>` | .txt lines | bytes | sha256 |
|---|---|---|---|---|---|---|
| ex01 | `ex01-general-form-template.txt` | §5 General Format | 0 | L61-70 | 407 | `eefbf84adddb49d1…` |
| ex02 | `ex02-label-list-long.txt` | §6 Example | 1 | L111-119 | 394 | `a10743ed221ac69c…` |
| ex03 | `ex03-label-list-compact-full.txt` | §6 Example | 2 | L123-127 | 228 | `ee519473a8e6acf6…` |
| ex04 | `ex04-label-list-minimal.txt` | §6 Example | 3 | L131-133 | 117 | `7152a6adbefa28f8…` |
| ex05 | `ex05-multi-value.txt` | §8 Semantics of PICS Labels and Label Lists | 5 | L229-230 | 97 | `de5812816f2a760e…` |
| ex06 | `ex06-pics-label-header-template.txt` | §9 RFC-822 Headers | 6 | L238 | 24 | `bafda11bb21dd7c0…` |
| ex07 | `ex07-html-meta-template.txt` | §10 Embedding Labels in HyperText Markup Language (HTML) | 7 | L246 | 58 | `ec1866df15d68dae…` |
| ex08 | `ex08-html-escape-table.txt` | §10 Embedding Labels in HyperText Markup Language (HTML) | 8 | L250-252 | 152 | `61564194449e4af6…` |
| ex09 | `ex09-http-request.txt` | §11.1 Example | 9 | L267-269 | 124 | `9a90c55089c0ae5a…` |
| ex10 | `ex10-http-response.txt` | §11.1 Example | 10 | L273-286 | 424 | `b06ec11511a3f6c9…` |
| ex11 | `ex11-bureau-sample-query.txt` | §12.1 Sample Query | 13 | L331-334 | 158 | `348a5b05b17476ad…` |
| ex12 | `ex12-appb1-generic-request.txt` | Appendix B, §18.1 Generic request | 16 | L561-567 | 312 | `8fe064aa893cc4df…` |
| ex13 | `ex13-appb1-generic-response.txt` | Appendix B, §18.1 Generic request | 17 | L571-608 | 1180 | `49e4e1f5688f81fa…` |
| ex14 | `ex14-appb2-normal-request.txt` | Appendix B, §18.2 Normal query | 18 | L615-621 | 311 | `0026e3f4ed6499e9…` |
| ex15 | `ex15-appb2-normal-response.txt` | Appendix B, §18.2 Normal query | 19 | L625-657 | 987 | `5978cc4cb69c45ca…` |
| ex16 | `ex16-appb3-tree-request.txt` | Appendix B, §18.3 Tree query | 20 | L664-670 | 309 | `7c7e82acfaa3225c…` |
| ex17 | `ex17-appb3-tree-response.txt` | Appendix B, §18.3 Tree query | 21 | L674-726 | 1536 | `a9611249bc09b299…` |
| ex18 | `ex18-appb4-generic-tree-request.txt` | Appendix B, §18.4 generic+tree | 22 | L733-740 | 320 | `a36c0eb6fecfa9ba…` |
| ex19 | `ex19-appb4-generic-tree-response.txt` | Appendix B, §18.4 generic+tree | 23 | L744-787 | 1129 | `6bd16e4cfa9f5397…` |

`ex19` is the one fixture that is not the whole `<pre>` element: the source never
closes that `<PRE>` before the page footer (D1), so the element runs on through the W3C
copyright paragraph to the end of the document. The fixture stops at the `<P>` that starts the footer; its
last bytes are the end of the last label list and two newlines.

## Expected results

| fixture | grammar rule | expected | why |
|---|---|---|---|
| ex01 | none | n/a | a template: placeholders `<service url>`, `[option...]`, `...` |
| ex02, ex03, ex04 | `labellist` | accept | the three forms of section 6 (long, compact with `full` URLs, minimal) |
| ex05 | `labellist` | accept | multi-value `(0.5:1.5 2)` |
| ex06 | none | n/a | `PICS-Label: <labellist>` is a template |
| ex07 | none | n/a | the META template; checked separately below |
| ex08 | table | three rows | `'`, `&`, `>` are the entities `&#39;`, `&amp;`, `&gt;` (each decoded by script) |
| ex09 | `request-header` on the `Protocol-Request` header | accept | the request line is not part of any grammar of the source |
| ex10 | `protocol-header`, `label-header` | accept, accept | the folded `PICS-Label:` header is unfolded per RFC 822 |
| ex11 | `request-line` after unfolding | accept | the section 12.1 sample |
| ex12, ex14, ex16, ex18 | `request-line` | **reject** raw (D2) | `&` inside the closing quote |
| ex12, ex14, ex16 | same, after repair R1 | accept | `&"` moved to `"&` (5 per query) |
| ex18 | same, after R1 and R2 | accept | R2 writes the option as `generic+tree` |
| ex13, ex15, ex17 | `labellist` on the body | **reject** raw (D7) | `;` comments |
| ex13, ex15, ex17 | same, `;` to end of line removed | accept | 9, 4 and 4 comment runs; no `;` falls inside a quoted string (checked) |
| ex19 | `labellist` | accept raw | no comments in 18.4 |

## Findings about the source (not repaired in any fixture)

| id | where | finding | evidence |
|---|---|---|---|
| D1 | Appendix B, §18.4 (generic+tree), HTML | The last `<PRE>` is closed only after the footer; its element contains the W3C copyright paragraph. | `reproduce.py` checks that exactly one `<pre>` (the last) contains a `<P>`; the rendering shows the copyright line at L789 |
| D2 | Appendix B (all four queries) L562-567, L616-621, L665-670, L734-740 vs §12.2 `and` and `encodedURL` | The `&` between parameters is written inside the closing quote of the URL before it. Five of the six parameters of each query. Under the grammar `&` is not an `encodedURL` character and the separator is missing. | raw query rejected, repaired (R1) query accepted |
| D3 | same four queries | The first `u=` value ends with `+` (`...%2F+`). Decoded as a URL it is `http://www.w3.org/pub/WWW/+`, not the URL the Appendix B prose lists; as form data a trailing space. The responses are labels for the URL without it. | decoded by `urllib.parse.unquote`, compared with the three URLs of the prose list; mismatch exactly the `+` in all four |
| D4 | Appendix B §18.2, §18.3, §18.4 responses | No blank line between the headers and the label list (§18.1 has one). Read strictly the label list is a malformed header line. | `ex15`, `ex17`, `ex19` have no `\n\n(`; `ex13` has |
| D5 | Appendix B §18.4 query L733 vs §12.2 `option` L351 | The grammar's option is `generic+tree`; the example sends `generic%2Btree`. The example is the correct one on the wire; the grammar would send a space. | repair R2 |
| D6 | §12.3 (Response to Query ...) L382-383 vs §7 L217 | The prose says `no-label` and `simple-labels`; the grammar defines `not-labeled` and `single-label`. | schema/README.md A19 |
| D7 | Appendix B L554, L578-608, L633-651, L682-701 | The responses contain `;` comments the label grammar does not admit, and not only on lines that begin with `;` as the source says; `;` is itself a transmit-name character. | schema/README.md A15; first failing token of each raw response printed by `reproduce.py` |
| D8 | Appendix B Content-Length 550, 569, 1075, 872 | The printed lengths cannot be reproduced. The label list as printed is 1054, 862, 1410 and 1003 bytes (LF line ends; 1085, 889, 1457, 1041 with CRLF). With comments removed and every run of whitespace collapsed to one space, none inside parentheses, it is 568, 585, 1095, 892, each 16 to 20 bytes above the printed value. The source says the responses were pretty-printed, so the printed value is not the length of anything shown; no reading of the layout was found that equals it. | computed by `reproduce.py`; not a proven defect, a finding that the numbers carry no checkable information |
| D9 | Appendix B §18.3 tree response, `http://www.rsac.org/v1.0`, second URL | `error (not-labeled ...)` for `http://www.w3.org/pub/WWW/TheProject.html`, though the server holds a specific label for exactly that URL (L551) and returns it in the same response inside the first URL's set (L710). §12.3 defines descendants by prefix and never says whether a URL is its own prefix (normative.md SD-19): if it is, the minimum response (opt=normal for each known child) includes that label; if it is not, the answer is consistent. Reading-dependent: the minimum response is defined through the known children of the URL. | stated as an inconsistency candidate, low confidence |
| D10 | §11.1 example vs §11.4 grammar | The `PICS-Label:` header is folded onto the next line, where the grammar has one space. Allowed by RFC 822 continuation (§9) but absent from the grammar. | schema/README.md A13 |

The other contradictions between the grammars and the prose (completeness values,
`[and]`, the extension production, the `by` option that cannot hold base64, the case
rule) are properties of the text, not of an example, and are in `../schema/README.md`
as A1 to A26.

## What reproduce.py computes beyond the grammar

* The three decoded parameters of the section 12.1 sample are `http://www.questionable.org/images`
  and `http://www.gcf.org/v2.5`, the URLs the prose names.
* Appendix B positional rules of §12.3, per response: one service-info per
  requested service in the query's order (the third is `error (no-ratings ...)`),
  one label, set or error per requested URL (3), every label of a tree or
  generic+tree answer carries `for`, every generic label carries `for`, a generic
  or generic+tree answer holds only generic labels, every `(for, generic)` pair is
  a label the server is said to hold (L539-553), and a normal or generic label's
  URL applies to the URL requested. All hold.
* The section 10 escape table is decoded row by row, and a label with `&` and `'`
  is shown to survive `content='...'` with the three escapes (derived check, not
  an example of the source).
* MD5 is 16 bytes and its base64 24 characters ending `==`; the grammar accepts it
  as `md5 "..."` and as `MIC-md5 "..."`, and a 60-character-line signature. The
  source prints **no** base64 value (0 found by script), so there is nothing printed to
  check these lengths against: they are computed, not verified against the source.
* The mutation sweep over 9 label lists, 370 single-edit mutants, none accepted.

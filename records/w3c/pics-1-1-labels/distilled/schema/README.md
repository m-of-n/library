---
record: pics-1-1-labels
kind: schema
title: "pics-1-1-labels — schemas"
extracted: "2026-11-12"
reviewed_by: ""
---

# PICS 1.1 Label Distribution — schemas

FX-1 pass 1, schema lane (mechanical, smaller model). The source is the W3C
Recommendation REC-PICS-labels-961031 (31 October 1996), cached as
`.cache/pics-1-1-labels.bin` (digest in `record.yaml`), and its plain-text
rendering `.cache/pics-1-1-labels.txt` (792 lines, sha256
`469de99e9845669cd4445879f7272d0513b8e94cd4760490ba3df408edba94f8`), which is
what every `L123` below counts in. **The source has no section numbers.** A
`§7` here is the renderer's structural ordinal (`bin/render-w3c --ordinal`) and
is always given with the heading title the first time.

The source publishes **four grammars**, each in modified BNF in a `<pre>` block
of the HTML, and nothing else formal: no ABNF, no ASN.1, no schema language. All
four are copied verbatim. Everything that makes them checkable is derived.

## Files

| file | kind | built from | covers | does NOT cover |
|---|---|---|---|---|
| `labels-s07-detailed-syntax.verbatim.txt` | **verbatim** | §7 (Detailed Syntax), `<pre>` 4, L150-219 | label list, service-info, label, option, rating, date, number, transmit-name, quotedname, errors | the semantics of the options (prose of §5, §8, §13) |
| `http-request-s11-3.verbatim.txt` | **verbatim** | §11.3 (Detailed Syntax of HTTP Requests for Labels With Document), `<pre>` 11, L297-306 | the `Protocol-Request` header | the rest of the HTTP request |
| `http-response-s11-4.verbatim.txt` | **verbatim** | §11.4 (Detailed Syntax For HTTP Response Headers For Labels With Document), `<pre>` 12, L318-319 | the `Protocol` and `PICS-Label` headers | other response headers |
| `bureau-query-s12-2.verbatim.txt` | **verbatim** | §12.2 (Detailed Syntax of HTTP Query for Labels Separate From Documents), `<pre>` 14, L343-373 | the GET and POST query to a label bureau | the form-encoded body of POST, defined only by reference to HTML 2.0 |
| `labels.derived.abnf` | **derived**, ABNF subset, executed | §7 | the label list, in two layers (token, character) | what ABNF cannot say (A25) |
| `http-headers.derived.abnf` | **derived**, ABNF subset, executed | §9 (RFC-822 Headers), §11.3, §11.4 | `Protocol-Request`, `Protocol`, `PICS-Label` | |
| `bureau-query.derived.abnf` | **derived**, ABNF subset, executed | §12.2 | the request line of a bureau query, in the source's reading and in the corrected reading | the POST body |
| `check-grammar.derived.py` | **derived**, Python | the three `.abnf` files | an RFC 5234 subset interpreter, the entry points `parse_labellist`, `parse_request_header`, `parse_protocol_header`, `parse_label_header`, `parse_request_line`, and the accept and reject corpora | |

No `.json` schema: the source defines text grammars over US-ASCII, and a JSON
Schema would describe a parse tree this format does not have.

Each `.verbatim.txt` begins with a header naming the section, the HTML block
number (counting from 0) and the one transformation applied (the `<B>`, `<I>`
and `<A>` tags of the `<pre>` removed, character references decoded), then a
marker line, then the block. `examples/reproduce.py` compares the part after the
marker line with the HTML.

## How to run

```sh
python3 -I distilled/schema/check-grammar.derived.py   # the grammar's own tests
python3 -I distilled/examples/reproduce.py             # every source example against it
```

The ABNF is **executed, not just written**: `check-grammar.derived.py` parses
the `.abnf` files and matches input against them by end-position sets (exact for
any context-free grammar, no backtracking order to get wrong). So a rule that
cannot match anything fails a test, and an undefined or unused rule is reported
by `lint`.

Measured by the script at the time of writing: the label grammar has 52 rules
(`labels` plus `http-headers`, token layer), the query grammar 25; the runner
**examined 288 checks, 0 failed**: 79 label-list REJECT cases (each paired with
the minimal edit that makes it acceptable, 158 checks), 23 ACCEPT cases, 12 + 4
header cases, 3 `Protocol` cases, 22 + 6 query cases, the lint, the prose-vs-grammar
readings, and a mutation sweep of 60 single-edit mutants over the four label lists
of section 6 and section 8 (delete a parenthesis, delete a quotation mark, drop the
last letter of a keyword, drop the version, drop the last character), all
rejected. `reproduce.py` repeats the sweep over 9 lists and 370 mutants.

## Two layers, and why

Section 7 says whitespace is ignored except in quoted strings and does not say where a
token ends (A1). The derived reading cuts the input into tokens first: `(` and
`)` one token each, a quoted string one token, a word a maximal run of anything
else; a quoted string or parenthesis needs no whitespace beside it, two words do.
The syntax rules (no `lex-` prefix) then match whole tokens, case-insensitively,
which is what the source's note on case says of option names. The character rules
(`lex-*`) match the text of one token: dates, numbers, transmit-names, quoted strings,
base64. The `:` of a range is a transmit-name character, so a range is one token
with no spaces (A4). The same machinery with `{` `}` as delimiters reads the
headers.

## Hazard check: a grammar that parses is not a grammar that binds

Every REJECT case in `check-grammar.derived.py` is a pair (bad, good): the bad
instance must be rejected **and** its one-edit repair must be accepted, so the
rejection is shown to be for the reason named and not for some unrelated flaw
(a wrong version, a missing paren). The reject list covers each constraint
the grammar states: the version, balanced parentheses and strings, every
date range (month 00 and 13, day 00 and 32, hour 24, minute 61, lower-case `t`,
missing zone, missing time, hyphens, two-digit year, `Z`), the number forms
(`.5`, `1e3`, `--1`, a bare sign), the range forms (`1:`, `1:2:3`, spaces around
the colon), transmit-names (leading and trailing `/`, a bad `%zz`, a quote), quoted
names (empty, `/`, `'`, newline), the boolean, base64 (bad character, bad padding
length, padding in the middle, empty, unquoted), extensions (no `optional` or
`mandatory`, no URL, a bare word as data, unbalanced data), the error forms, the
tree set, adjacency of two words (`labelsr`, `tfor`, `rsuds`), and the
query and header constraints. Two constraints the ABNF cannot say are applied as a named exclusion hook (`EXCLUDE`):
the first item of an extension in `Protocol-Request` is not `services`, and an
extension parameter of a query is not named `opt`, `format`, `u` or `s`. The runner proves the hook is needed: with `EXCLUDE` emptied the four bad instances (one header, three queries) are accepted, and with it restored they are rejected.

## Where the grammar is ambiguous, or contradicts the prose or the examples

Locators are the ordinal and heading title, then `.txt` lines. **A** entries are
properties of the source text (a reader must choose); **D** entries are defects the
examples show (listed in `examples/README.md` with their evidence).

| id | where | what | derived reading, and test |
|---|---|---|---|
| A1 | §7 (Detailed Syntax) L140 | Whitespace is ignored outside quoted strings, but no rule says where a token ends, so `PICS-1.1error`, `labelsr`, `tfor` have no stated reading. | token layer above; `labelsr`, `tfor`, `rsuds` rejected, `"url"l r(a 1)` accepted |
| A2 | §7 L152 | `'(no-ratings'` is one quoted literal with the parenthesis glued on, inconsistent with whitespace insensitivity everywhere else. | two tokens, whitespace between accepted |
| A3 | §7 L157, L145 | `single-label` needs `rating+`, so `r ()` is not a label; the note on multi-value says a category with no value may be sent as an empty list, which `rating` allows, but never a label with no categories. A tree set (`'(' single-label* ')'`, L156) may be empty. | `r ()` rejected, `l ()` accepted |
| A4 | §7 L198, L205 | `:` is both the range separator and a transmit-name character; whether `1 : 2` is a range is open. | a range is one token; spaces around the colon rejected |
| A5 | §7 L203, L211 vs §5 (General Format) L84 | `quotedname` has no `/` (and no quotation mark), yet the text of the `by` option says it may carry base-64 certificates, and base64 uses `/`. So `by` cannot hold what its description says it may hold, and a `comment` cannot hold a URL with a path. `(` and `)` are allowed raw in a quotedname (`urlchar`), while the note under the character rules lists parentheses among the characters to write as `%hh`. | `by "a/b"` rejected |
| A6 | §7 L159, §12.2 L347 | `URL` is defined elsewhere (PICS Rating Services and Rating Systems, not held), and `url-fragment` only by description. | ASSUMED: URL is 1 or more printable ASCII except `"` and space; url-fragment the same without `?` |
| A7 | §7 L214, §13 L404 | `base64-string` is by reference to RFC 1521, written inside double quotes; a signature is sent in 60-character lines, which whitespace-insensitivity and the quoted-string rule do not obviously allow. | ASSUMED: whitespace allowed inside the quotes between any two characters; at least one quantum |
| A8 | §7 L164 vs §12.2 L362 | `boolean` is used in §7 and defined only in §12.2. | one rule used by both |
| A9 | §7, §11.3, §12.2 | `option` means two things (a label option; the `opt=` values), `extension` two things (§11.3, §12.2) plus a literal in §7, `token`, `token-or-quoted-string` and `form`/`completeness` are defined twice (the last two identically). | the §12.2 rules carry a `bq-` prefix |
| A10 | §11.3 L301, L310; §12.2 L353, L386 | The grammar lists four values for `completeness` and `form`; the prose says any alphanumeric string may be used and an unrecognised value means `minimal` (headers) or `full` (bureau). | the strict rule rejects `verbose`; `request-header-prose` accepts it; tested both ways |
| A11 | §12.2 L360-364 | `[and]` is optional in the grammar; the note under `and` says it is required except right after the `?`. | derived: exact, first parameter has none, later ones have one |
| A12 | §12.2 L354-357 | `extension` has no `[and]`, so as written an extension can be the first parameter of the query or be glued to the previous parameter with no `&`, and cannot follow `&`; and its token must not be `opt`, `format`, `u` or `s`, which BNF cannot say. | derived adds `&`; `get-as-written` keeps the source's reading and rejects `?opt=tree&x=1&...`; the exclusion is the `EXCLUDE` hook |
| A13 | §12.2 L344; §11.4 L319; §11.1 L277-278 | `'get' url-fragment` has no space and no HTTP version, though every example has both. The query examples are folded across lines "for presentation"; the header example folds after `PICS-Label:` where the grammar has one space. | `request-line` adds the space and `HTTP/n.n`; the unfold rule is this file's (`unfold_request`: delete the break and its indentation, keep a space before `HTTP/`); headers are unfolded per RFC 822 |
| A14 | §12.2 L365-370 | `encodedURL` is a quoted URL: double quotes (every one of 8 examples) or `%xx`-quoted (the explanation that follows)? | both accepted |
| A15 | Appendix B (Sample Label Bureau Queries and Responses) L554, L578-608 | The responses carry comments that begin with `;`, which the source describes as comment lines. They are not in the grammar of §7, `;` is a transmit-name character, and the comments trail tokens on the same line as well as starting lines. | the raw responses 18.1 to 18.3 are rejected (first failing token reported); the same text with `;` to end of line removed is accepted (9, 4, 4 runs removed); 18.4 has none |
| A16 | §12.2 L351 vs Appendix B 18.4 L733 | The grammar's option is the literal `generic+tree`; the example sends `generic%2Btree` (correct on the wire, where an unescaped `+` is a space). | the grammar keeps the literal; reproduce.py applies the repair `%2B` to `+` to a copy and reports it |
| A17 | §12.2 L360-366 vs Appendix B L562-567 | In every Appendix B query the `&` that separates parameters sits **inside** the closing double quote of the previous URL, not after it. | rejected raw; accepted after moving 5 `&` per query |
| A18 | §7 L217 | `request-denied [quotedURL explanation*]` has no explanation without a URL, and a lone quoted string with no space is a valid quotedURL, so a bare explanation is read as the URL. | `request-denied "why not"` rejected, `request-denied "http://x/" "why not"` accepted |
| A19 | §12.3 (Response to Query ...) L382 vs §7 L217 | The prose tells a bureau to send a `no-label` message; the grammar has `not-labeled`, `no-ratings`, `request-denied`, no `no-label`. §12.3 L383 also says `simple-labels` for what §7 calls `single-label`. | the grammar's names are used |
| A20 | §8 L224 vs §7 L152 | The prose reads as though `error (no-ratings ...)` is the whole list; the grammar (`service-info+`) and Appendix B put it among other services. | the grammar's reading |
| A21 | §8 L225 vs §7 L156 | The prose confines the parenthesised set of labels to a tree request; the grammar allows it anywhere a label may be. | the grammar's reading |
| A22 | §7 L179-196 | Ranges are given as digits only: any day 01-31 in any month, minutes 00-60, and a zone of four digits with no range (`9999`). The text says it is based on ISO 8601:1988. | digits and the listed ranges, no calendar check |
| A23 | §7 L177-178 | In `data` the three quoted alternatives overlap: a date is a valid quotedname, a URL with no `/` is too, so an item's type cannot be recovered from its text. | acceptance is unaffected |
| A24 | §7 L197, L199-200 | The digits, sign and `.` are transmit-name characters, so `0.5` is lexically a transmit-name; `rating` is told apart by position only. | `(0.5 1)` accepted |
| A25 | §5 L89, L146; §7 L147; §12.3 L383 | Constraints the grammar cannot express and the recogniser does not check: a generic label must carry `for`; an option occurs once except `comment` and `extension`; extension URLs distinct; `for` required in tree, generic+tree and `format=` answers; category names distinct within a rating system; numbers within IEEE single range. | `bin/validate`-style checking of these needs a tree, which this grammar does not build; they are requirements, not grammar |
| A26 | §7 L141 vs §13.1 L416 | Quoted strings are case sensitive, option names and grammar tokens are not; the special form says strings are written lower case if they are case insensitive, without saying which are. | keywords insensitive, quoted-string contents exact |

## Quoted source wording

Quotations are markers rendered by `bin/check-quotes --render`; nothing is typed.

<!-- q L141 "Transmit-names and quoted strings" .. "are case insensitive." -->
> Transmit-names and quoted strings are case sensitive. Option names and other tokens in the BNF grammar are case insensitive.

<!-- q L84 "it may be used" .. "on the label." -->
> it may be used to contain a (base-64 encoded) set of certificates and other information used to verify the signature on the label.

<!-- q L310 "For future extensibility" .. "completeness option." -->
> For future extensibility, any alphanumeric string may be used for a value of the completeness option.

<!-- q L363-364 "this must be included" .. "in the query." -->
> this must be included unless it immediately follows the ? in the query.

<!-- q L554 "Comment lines" .. "the responses." -->
> Comment lines, beginning with ';' have been added to explain the responses.

<!-- q L382 "If no such generic label" .. "specific label." -->
> If no such generic label is available, the server should include the "no-label" message rather than sending back a specific label.

<!-- q L416 "strings are output" .. "case insensitive." -->
> strings are output in lower case if they are case insensitive.

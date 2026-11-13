---
record: pics-dsig-1-0
kind: examples
title: "pics-dsig-1-0 — examples and test vectors"
extracted: "2026-11-12"
reviewed_by: ""
---

# PICS Signed Labels (DSig) 1.0 — examples and test vectors

Source: `.cache/pics-dsig-1-0.bin` (REC HTML, `content.sha256` in `record.yaml`); line numbers count in
`.cache/pics-dsig-1-0.txt`. The source has no section numbers; `§` ordinals are the renderer's
structural ordinals, given with the heading title.

The document has **27** `<pre>` blocks. **All 27** are fixtures here: 8 examples (this directory), 16 structural
templates (`templates/`), 3 grammar displays (`../schema/`). `reproduce.py` accounts for each block exactly once.

Normalisation, the only one: tags dropped, character references decoded, U+00A0 written as U+0020,
CRLF as LF. A fixture is otherwise the block's characters, including trailing spaces and the lack of a final
line feed. Fixtures are pure US-ASCII.

## The examples

"Verdict" is the derived grammar's (`../schema/check-grammar.derived.py`): PICS 1.1 profile | DSig strict | DSig
placeholder (see that README). "n/a" means the fixture is a fragment that is not an extension, so the PICS 1.1 profile does not apply.

| fixture | source | HTML / rendering lines | bytes | parsed as | verdict | expected result |
|---|---|---|---|---|---|---|
| `ex01-resinfo-extension.txt` | §7.2.1 (Detailed Syntax of the resinfo Extension in a PICS 1.1 Label), "valid DSig 1.0 resinfo extension with two hashes" | L776 / 259-263 | 287 | resinfo-extension | ACCEPT \| REJECT \| ACCEPT | Valid in shape. Strict rejects `"base64 hash"`: it has a space and is not base64. Hash values are placeholders, nothing to verify. |
| `ex02-attribinfo.txt` | §7.3.2 (Attribution Information), "an example Attribution Information section" | L889 / 306-312 | 388 | AttributionInfo | n/a \| REJECT \| ACCEPT | Valid in shape. Strict rejects `"base64-x.509-cert"` and `"base64-pgp-signed-key"` (hyphens, not base64). The URL members are valid. |
| `ex03-bykey-dsa-sigdata.txt` | §7.3.4.2 ("ByKey"), the DSA example | L990 / 348-352 | 172 | SigData | n/a \| REJECT \| REJECT | **Not valid under the source's own grammar**: four sibling pairs inside one SigData (finding F-03). Rejected in every mode, placeholders or not. |
| `ex04-sigblock-extension.txt` | §7.4.1 (An example sigblock extension:) | L1115 / 415-433 | 1039 | sigblock-extension | ACCEPT \| REJECT \| ACCEPT | Valid in shape with one RSA-MD5 and one DSS signature, an `exclude` of one extension. Strict rejects the two certificate placeholders. Writes `"byKey"` where 7.3.4.2 names `"ByKey"` (F-05). `"abcdefghijklmnop="` (17 characters) is not base64. |
| `ex05-step1-label.txt` | §8.2 (An Example), Step 1 | L1306 / 545-550 | 201 | label | ACCEPT \| ACCEPT \| ACCEPT | A plain PICS 1.1 label. Input of the example. |
| `ex06-step2-label-resinfo.txt` | §8.2 (An Example), Step 2 | L1314 / 554-564 | 498 | label | ACCEPT \| ACCEPT \| ACCEPT | Step 1 plus a resinfo extension with a SHA1 and a dated MD5 hash. Both values are valid base64 of 8 bytes, which no SHA1 (20) or MD5 (16) digest is (F-10). |
| `ex07-step3-canonical-form.txt` | §8.2 (An Example), Step 3 (canonicalize) | L1329 / 569-575 | 417 | label | ACCEPT \| ACCEPT \| ACCEPT | The text a signature suite signs, printed with display line breaks that the source says are not in the real text. See "Canonical form" below. |
| `ex08-step4-signed-label.txt` | §8.2 (An Example), Step 4 | L1337 / 579-603 | 1304 | label | ACCEPT \| ACCEPT \| ACCEPT | Called "a valid DSig-1.0 label" (L605): Step 2 plus a sigblock extension. Valid in shape. The N value `"aba212412412="` is 13 characters, not base64, but a SigInfo accepts any name. |

No example in the source states an expected verification result: the source says how to sign and never how
to verify (`../messages.yaml`, applicability). The "expected result" column is what this library can check.

### Canonical form (`ex07`, section 8.1.2 and 8.2)

`reproduce.py` part (c) implements the recipe as written (`../messages.yaml` MSG-13, rules C-01 to C-14) and
recomputes the canonical form from **Step 2** and, separately, from **Step 4** (where the recipe removes the
sigblock). Result:

- Step 2 and Step 4 reduce to the **same** canonical form (the sigblock is not part of what is signed).
- That form is **identical** to the printed Step 3 when the header symbol is left as `PICS-1.1` and the
  outer parentheses are spaced like other tokens.
- It **differs** where the recipe is followed to the letter: C-03 and C-08 say the header is the lower-case
  `pics-1.1` symbol; the printed text has `PICS-1.1` (F-08). C-05 reads two ways; under the reading that keeps the
  printed spacing, the case of `PICS-1.1` is the only difference.
- The two resinfo hashes are printed MD5 then SHA1; Step 2 has SHA1 then MD5. The recipe sorts options and
  extensions and says nothing about the entries inside one extension. The printed order equals sorting them by
  identifier URL; that is the lane's reading, not the source's.
- Transmit-names keep their received case in part (c): one reading of `../messages.yaml` F-11
  (`../normative.md` SD-20), the other being that a transmit-name is a symbol and is lower-cased. Every
  transmit-name in the example is lower case, so the comparison does not depend on it.

### Hashes and signatures — what cannot be verified, and why

- **Resource hashes** (`SHA1-1_0`, `MD5-1_0` in ex01, ex06 to ex08) are over the document
  `http://www.w3.org/PICS/DSig/Overview`, whose bytes the source does not give.
- **Signatures** (`SigCrypto`) are over the canonical form, but no key is given: `"N"`, `"E"` and the DSA
  values are placeholders; of 18 key, signature and certificate values in the examples (counted per fixture;
  16 distinct strings), **10 are not RFC 1521 base64** (8 distinct) (`reproduce.py` (d)). And though Step 3 prints
  the canonical text, no source defines how `RSA-MD5-1_0` or `DSS-1_0` turns it into the input of RSA or DSA
  (`../normative.md` SD-17).
- **Hash lengths** can be checked and fail: the eight resinfo hash entries in four fixtures do not
  decode to the digest size of the algorithm named (8 bytes against 20 and 16, or not base64 at all). The
  digest sizes are facts about SHA-1 and MD5; the source states none.

Nothing is faked: no signature or hash is reported verified.

## Structural templates (`templates/`)

The 16 `<pre>` blocks that show a form with placeholders (`<service 1 url>`, `"CertificateFamilyIdentifierURL"`,
`...`). They are not instances and are not parsed. Each is wired to a message in `../messages.yaml`.

| fixture | source | rendering lines | message |
|---|---|---|---|
| `t00-label-list-service-sections.txt` | §5.1 (PICS 1.1 labels and label lists) | 92-95 | MSG-01 |
| `t01-service-section.txt` | §5.1 | 99-102 | MSG-01 |
| `t02-general-label-list.txt` | §5.1 | 106-115 | MSG-01 |
| `t03-label-4-equivalent.txt` | §5.1 | 119-122 | MSG-12 |
| `t04-resinfo-hash-entry.txt` | §7.2 (Resource Reference Information Extension) | 208 | MSG-03 |
| `t07-sigblock-structure.txt` | §7.3.1 (Format Specification) | 288-290 | MSG-05 (F-06) |
| `t08-attribinfo-structure.txt` | §7.3.2 (Attribution Information) | 299-302 | MSG-06 |
| `t10-signature-syntax.txt` | §7.3.3 (Signatures) | 318 | MSG-08 |
| `t11-bykey-template.txt` | §7.3.4.2 ("ByKey") | 344 | MSG-10 |
| `t13-byhash.txt` | §7.3.4.3 ("ByHash") | 358 | MSG-10 |
| `t14-byname.txt` | §7.3.4.4 ("ByName") | 366 | MSG-10 |
| `t15-bycert.txt` | §7.3.4.5 ("ByCert") | 372 | MSG-10 |
| `t16-on.txt` | §7.3.4.6 (The "On" token: Time of Signature generation) | 379 | MSG-10 |
| `t17-include-exclude.txt` | §7.3.4.7 (The "include" and "exclude" tokens: modifying the canonicalized form of the label) | 387-388 | MSG-10, MSG-11 |
| `t21-signing-label-list.txt` | §8 (Signing) | 501-515 | MSG-01 |
| `t22-standalone-label.txt` | §8.1.1 (Creating an equivalent standalone label) | 525-528 | MSG-12 |

## Reproducing

```sh
python3 -I records/w3c/pics-dsig-1-0/distilled/examples/reproduce.py [.cache/pics-dsig-1-0.bin]
```

Prints five parts and `FAILURES n`; exit status 1 when (a) a fixture differs from its `<pre>` block or (b) a
verdict differs from the table above. Parts (c) to (e) report **source defects** and do not fail.

- (a) **27 files against 27 `<pre>` blocks, 0 different, 0 rendering-line differences, no block without a file.**
  Appending a byte to a fixture makes it exit 1 (tested).
- (b) 8 fixtures: 8 verdicts as expected; the token-case audit lists `"byKey"` in ex04 and ex08.
- (c) canonical form, above.
- (d) hash lengths, above; also the full list of the 18 key, signature and certificate values.
- (e) Appendix 3 spells two of four identifiers with `//TR` (F-09).

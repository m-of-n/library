---
record: draft-ietf-spki-cert-structure
kind: examples
title: "draft-ietf-spki-cert-structure — examples and test vectors"
extracted: "2026-11-09"
reviewed_by: ""
---

# Examples

Every S-expression the draft prints is a fixture here: 31 files named
`eNN-<section>-<what>.verbatim.txt`. The draft has no other test vectors and
prints no expected verification results; the "expected result" below is what
`reproduce.py` observes, and is this library's, not the draft's.

**Fixture bytes.** Each file is the source lines it names, one per line, indentation kept,
trailing blank lines dropped. Three fixtures cross a page break (E08 L853-859,
E10 L910-916, E18 L1081-1087); the page footer, running header and the blank runs round
them are left out, exactly as `schema/verbatim_files.derived.py` leaves them out of
the BNF files. E20-E23 are a substring of one source line (found exactly once). Nothing else is altered: a hyphen at a line end, `|...|` base64
with its line breaks and the draft's own typographical spaces are as printed.

```sh
python3 -I distilled/examples/reproduce.py          # check, exit 1 on any unexpected result
python3 -I distilled/examples/reproduce.py --write  # rewrite the fixtures from the source
```

`reproduce.py` (derived; stdlib only) re-cuts every fixture from
`.cache/draft-ietf-spki-cert-structure.txt` by line range and compares bytes, parses
each with `schema/spki_sexp.derived.py` in the form the draft prints it (advanced,
`{base64}` transport, canonical), matches it against section 9.2 with
`schema/spki_bnf.derived.py`, then runs the conversion checks below. Last run: 31
fixtures, 12 conversion checks, 0 unexpected.

## Expected result per fixture

`ok` = parses and matches the named production of section 9.2. `REJECT` = parses as
an S-expression but the production does not match (a recorded source defect, see below).

| id | file | section | source lines | form | result |
|---|---|---|---|---|---|
| E01 | `e01-s2-name-local.verbatim.txt` | §2 | L405 | adv | <relative-name> ok |
| E02 | `e02-s2-name-fq.verbatim.txt` | §2 | L407 | adv | <fq-name> ok |
| E03 | `e03-s3-4-canonical.verbatim.txt` | §3.4 | L639 | canonical | <s-expr> ok |
| E04 | `e04-s3-4-advanced.verbatim.txt` | §3.4 | L646 | adv | <s-expr> ok |
| E05 | `e05-s3-4-transport.verbatim.txt` | §3.4 | L656-657 | transport | <s-expr> ok |
| E06 | `e06-s3-8-1-1-rsa-public-advanced.verbatim.txt` | §3.8.1.1 | L815-821 | adv | <pub-key> ok |
| E07 | `e07-s3-8-1-1-rsa-public-transport.verbatim.txt` | §3.8.1.1 | L826-829 | transport | <pub-key> ok |
| E08 | `e08-s3-8-1-1-rsa-private-advanced.verbatim.txt` | §3.8.1.1 | L834-868 | adv | parsed; no BNF rule (object defined nowhere in the draft) |
| E09 | `e09-s3-8-1-1-rsa-private-transport.verbatim.txt` | §3.8.1.1 | L872-887 | transport | parsed; no BNF rule (object defined nowhere in the draft) |
| E10 | `e10-s3-8-1-2-dsa-public-advanced.verbatim.txt` | §3.8.1.2 | L899-923 | adv | <pub-key> ok |
| E11 | `e11-s3-8-1-2-dsa-public-transport.verbatim.txt` | §3.8.1.2 | L929-939 | transport | <pub-key> ok |
| E12 | `e12-s3-8-1-2-dsa-private-elided.verbatim.txt` | §3.8.1.2 | L944-958 | elided | not parseable (expected): base64 contains a character outside the RFC 2045 a |
| E13 | `e13-s3-8-2-hash-md5-advanced.verbatim.txt` | §3.8.2 | L1004 | adv | <hash> ok |
| E14 | `e14-s3-8-2-hash-md5-transport.verbatim.txt` | §3.8.2 | L1005 | transport | <hash> ok |
| E15 | `e15-s3-8-2-hash-sha1-advanced.verbatim.txt` | §3.8.2 | L1007 | adv | <hash> ok |
| E16 | `e16-s3-8-2-hash-sha1-transport.verbatim.txt` | §3.8.2 | L1008 | transport | <hash> ok |
| E17 | `e17-s3-8-3-2-signature-rsa.verbatim.txt` | §3.8.3.2 | L1052-1066 | adv | <signature> ok |
| E18 | `e18-s3-8-3-2-signature-dsa.verbatim.txt` | §3.8.3.2 | L1068-1097 | adv | <signature> ok |
| E19 | `e19-s3-8-3-1-dsa-sig-params-template.verbatim.txt` | §3.8.3.1 | L1043 | template | not parseable (expected): advanced form, char 18: trailing text after the S- |
| E20 | `e20-s4-1-version-default.verbatim.txt` | §4.1 | L1172 | adv | <version> ok |
| E21 | `e21-s4-8-tag-all.verbatim.txt` | §4.8 | L1391 | adv | <tag> ok |
| E22 | `e22-s4-9-1-date-1.verbatim.txt` | §4.9.1 | L1450 | date | date format ok |
| E23 | `e23-s4-9-1-date-2.verbatim.txt` | §4.9.1 | L1451 | date | date format ok |
| E24 | `e24-s5-1-name-cert-template.verbatim.txt` | §5.1 | L1630-1634 | adv | <name-cert> REJECT (stops at token 6 of 13: expected "(") |
| E25 | `e25-s5-3-name-cert-advanced.verbatim.txt` | §5.3 | L1698-1702 | adv | <name-cert> REJECT (stops at token 23 of 27: expected "comment" | "valid") |
| E26 | `e26-s5-3-name-cert-transport.verbatim.txt` | §5.3 | L1704-1707 | transport | <name-cert> REJECT (stops at token 23 of 27: expected "comment" | "valid") |
| E27 | `e27-s5-3-name-before.verbatim.txt` | §5.3 | L1717-1718 | adv | <subject> ok |
| E28 | `e28-s5-3-name-after.verbatim.txt` | §5.3 | L1722-1723 | adv | <subject> ok |
| E29 | `e29-s5-3-name-cert-trouble.verbatim.txt` | §5.3 | L1731-1735 | adv | <name-cert> REJECT (stops at token 23 of 27: expected "comment" | "valid") |
| E30 | `e30-s6-1-acl-advanced.verbatim.txt` | §6.1 | L1801-1812 | adv | <acl> ok |
| E31 | `e31-s6-1-acl-transport.verbatim.txt` | §6.1 | L1814-1820 | transport | <acl> ok |

Two rows are not S-expressions on purpose. E12 is the DSA private key whose `y` and `x`
are the literal text `(y |...|)` and `(x |...|)`, an elision; the base64 reader rejects
the dots. E19 is the template `(r <integer>) (s <integer>)`, two S-expressions in a row
with placeholders. E22 and E23 are dates and are checked against `YYYY-MM-DD_HH:MM:SS`.
E08 and E09 are a `private-key` object that no BNF rule describes.

## Requirements each fixture exercises

Each fixture is the printed instance of rules stated in `../requirements.yaml`. The ids below are the
requirements a reader checks the fixture against: the production it must match, the prose that says
what the object means, and the inferred entries that fill what the draft leaves open. The join is by
hand, read against each requirement's text, and `bin/check-id-joins --resolve` prints every pair.

| fixture | requirements |
|---|---|
| E01 | `draft-ietf-spki-cert-structure#R-0013`, `draft-ietf-spki-cert-structure#R-0226`, `draft-ietf-spki-cert-structure#R-0229`, `draft-ietf-spki-cert-structure#R-0441` |
| E02 | `draft-ietf-spki-cert-structure#R-0007`, `draft-ietf-spki-cert-structure#R-0008`, `draft-ietf-spki-cert-structure#R-0227`, `draft-ietf-spki-cert-structure#R-0441` |
| E03 | `draft-ietf-spki-cert-structure#R-0036`, `draft-ietf-spki-cert-structure#R-0037`, `draft-ietf-spki-cert-structure#R-0059` |
| E04 | `draft-ietf-spki-cert-structure#R-0033`, `draft-ietf-spki-cert-structure#R-0061`, `draft-ietf-spki-cert-structure#R-0062`, `draft-ietf-spki-cert-structure#R-0065` |
| E05 | `draft-ietf-spki-cert-structure#R-0035`, `draft-ietf-spki-cert-structure#R-0063`, `draft-ietf-spki-cert-structure#R-0391` |
| E06 | `draft-ietf-spki-cert-structure#R-0090`, `draft-ietf-spki-cert-structure#R-0091`, `draft-ietf-spki-cert-structure#R-0093`, `draft-ietf-spki-cert-structure#R-0390` |
| E07 | `draft-ietf-spki-cert-structure#R-0063`, `draft-ietf-spki-cert-structure#R-0090`, `draft-ietf-spki-cert-structure#R-0391` |
| E08 | `draft-ietf-spki-cert-structure#R-0095`, `draft-ietf-spki-cert-structure#R-0096`, `draft-ietf-spki-cert-structure#R-0390`, `draft-ietf-spki-cert-structure#R-0395` |
| E09 | `draft-ietf-spki-cert-structure#R-0063`, `draft-ietf-spki-cert-structure#R-0095`, `draft-ietf-spki-cert-structure#R-0391` |
| E10 | `draft-ietf-spki-cert-structure#R-0090`, `draft-ietf-spki-cert-structure#R-0093`, `draft-ietf-spki-cert-structure#R-0390` |
| E11 | `draft-ietf-spki-cert-structure#R-0063`, `draft-ietf-spki-cert-structure#R-0090`, `draft-ietf-spki-cert-structure#R-0391` |
| E12 | `draft-ietf-spki-cert-structure#R-0097` |
| E13 | `draft-ietf-spki-cert-structure#R-0099`, `draft-ietf-spki-cert-structure#R-0100`, `draft-ietf-spki-cert-structure#R-0396` |
| E14 | `draft-ietf-spki-cert-structure#R-0063`, `draft-ietf-spki-cert-structure#R-0099`, `draft-ietf-spki-cert-structure#R-0396` |
| E15 | `draft-ietf-spki-cert-structure#R-0099`, `draft-ietf-spki-cert-structure#R-0100`, `draft-ietf-spki-cert-structure#R-0396` |
| E16 | `draft-ietf-spki-cert-structure#R-0063`, `draft-ietf-spki-cert-structure#R-0099`, `draft-ietf-spki-cert-structure#R-0396` |
| E17 | `draft-ietf-spki-cert-structure#R-0101`, `draft-ietf-spki-cert-structure#R-0102`, `draft-ietf-spki-cert-structure#R-0107`, `draft-ietf-spki-cert-structure#R-0397`, `draft-ietf-spki-cert-structure#R-0398`, `draft-ietf-spki-cert-structure#R-0399` |
| E18 | `draft-ietf-spki-cert-structure#R-0101`, `draft-ietf-spki-cert-structure#R-0108`, `draft-ietf-spki-cert-structure#R-0397`, `draft-ietf-spki-cert-structure#R-0398`, `draft-ietf-spki-cert-structure#R-0399` |
| E19 | `draft-ietf-spki-cert-structure#R-0105`, `draft-ietf-spki-cert-structure#R-0108` |
| E20 | `draft-ietf-spki-cert-structure#R-0115`, `draft-ietf-spki-cert-structure#R-0116`, `draft-ietf-spki-cert-structure#R-0117`, `draft-ietf-spki-cert-structure#R-0400` |
| E21 | `draft-ietf-spki-cert-structure#R-0156`, `draft-ietf-spki-cert-structure#R-0157`, `draft-ietf-spki-cert-structure#R-0458` |
| E22 | `draft-ietf-spki-cert-structure#R-0171`, `draft-ietf-spki-cert-structure#R-0172`, `draft-ietf-spki-cert-structure#R-0174`, `draft-ietf-spki-cert-structure#R-0408` |
| E23 | `draft-ietf-spki-cert-structure#R-0171`, `draft-ietf-spki-cert-structure#R-0172`, `draft-ietf-spki-cert-structure#R-0174`, `draft-ietf-spki-cert-structure#R-0408` |
| E24 | `draft-ietf-spki-cert-structure#R-0210`, `draft-ietf-spki-cert-structure#R-0211` |
| E25 | `draft-ietf-spki-cert-structure#R-0168`, `draft-ietf-spki-cert-structure#R-0211`, `draft-ietf-spki-cert-structure#R-0212`, `draft-ietf-spki-cert-structure#R-0213`, `draft-ietf-spki-cert-structure#R-0235`, `draft-ietf-spki-cert-structure#R-0416` |
| E26 | `draft-ietf-spki-cert-structure#R-0063`, `draft-ietf-spki-cert-structure#R-0168`, `draft-ietf-spki-cert-structure#R-0211`, `draft-ietf-spki-cert-structure#R-0212`, `draft-ietf-spki-cert-structure#R-0213`, `draft-ietf-spki-cert-structure#R-0235`, `draft-ietf-spki-cert-structure#R-0391` |
| E27 | `draft-ietf-spki-cert-structure#R-0227`, `draft-ietf-spki-cert-structure#R-0235`, `draft-ietf-spki-cert-structure#R-0415` |
| E28 | `draft-ietf-spki-cert-structure#R-0227`, `draft-ietf-spki-cert-structure#R-0235`, `draft-ietf-spki-cert-structure#R-0415` |
| E29 | `draft-ietf-spki-cert-structure#R-0238`, `draft-ietf-spki-cert-structure#R-0239`, `draft-ietf-spki-cert-structure#R-0240`, `draft-ietf-spki-cert-structure#R-0417` |
| E30 | `draft-ietf-spki-cert-structure#R-0242`, `draft-ietf-spki-cert-structure#R-0243`, `draft-ietf-spki-cert-structure#R-0244`, `draft-ietf-spki-cert-structure#R-0247` |
| E31 | `draft-ietf-spki-cert-structure#R-0063`, `draft-ietf-spki-cert-structure#R-0242`, `draft-ietf-spki-cert-structure#R-0243`, `draft-ietf-spki-cert-structure#R-0244`, `draft-ietf-spki-cert-structure#R-0391` |

## Conversion checks (12)

The draft prints several objects twice, in advanced and in another form, and says
the hash of the key "given above" is printed. `reproduce.py` checks:

1. E04 and E03: advanced and canonical forms of the §3.4 example have the same canonical bytes.
2. E04 and E05: the base64 transport of §3.4 decodes to those bytes.
3. E06 and E07: public RSA key, advanced and transport.
4. E08 and E09: private RSA key, advanced and transport.
5. E10 and E11: public DSA key, advanced and transport.
6. E13 and E14: md5 hash, advanced and transport.
7. E15 and E16: sha1 hash, advanced and transport.
8. E25 and E26: name certificate, advanced and transport.
9. E30 and E31: ACL, advanced and transport.
10. The canonical bytes of E04 are exactly
    `(4:test26:abcdefghijklmnopqrstuvwxyz5:123455::: ::)` (length prefixes, 3.4).
11. md5 of the canonical bytes of E06 equals the value printed as E13 (3.8.2: "the
    public key given above has the following hashes").
12. sha1 of the canonical bytes of E06 equals the value printed as E15.

E17 and E18 are then checked cryptographically (see below). The base64 width the
draft uses for transport is 60 characters per line with the opening brace on the
first line, except that E07's last line (L829) holds 61 base64 characters and the
closing brace; the draft does not state a width, so a reader must not require one.

## Source defects the examples show

- **E25, E26, E29 do not match `<name-cert>`.** The section 5.3 name certificates put
  `(not-after "2001-01-01_00:00:00")` directly in the certificate. `<name-cert>` takes
  `<valid>?` and `<valid>` is `(valid ...)`. The parser stops at token 23 of 27. E26 is the
  base64 of E25 (same canonical bytes). (messages.yaml SD-08.)
- **E24 is a template, not an instance**: it holds `<principal>` and `<name>` as
  bare tokens. It parses as an S-expression and is rejected by `<name-cert>`.
- **E20 is `(version "0")`**, the draft's stated default; under `<version>::
  "(" "version" <integer> ")"` the string `0` is the byte 0x30, which is the integer 48
  (messages.yaml SD-01).
- **E17, the RSA sample signature, does not verify as PKCS#1 v1.5 (messages.yaml SD-14).** With the
  printed key (e = 0x11) the signature recovers a 128-octet block that starts 0x02, not
  00 01 ff..., and holds `003021300906052b0e03021a05004014` before the printed 20-octet
  hash, where a SHA-1 DigestInfo ends `05000414`. The block does end with the printed
  hash. The draft does not say why. **E18, the DSA sample,
  verifies** under DSA with the printed key, over the printed hash taken as an integer,
  and does not verify over the sha1 of its canonical `(hash ...)` object; `reproduce.py`
  checks both. So the samples were computed over the hash value
  (`draft-ietf-spki-cert-structure#R-0398`), which the draft's prose never says.
- **E18's algorithm name is `dsa-sha1`**, as `<sig-val>` and `<pub-sig-alg-id>` have it, not
  the `dsa-sha1-sig` that the unreferenced `<dsa-sig-val>` has (messages.yaml SD-02).
- **Six binary examples have no base64 form**, though §3.6 (L715-717) promises one for
  every example whose canonical form is binary: E02, E17, E18, E27, E28 and E29 carry hash or
  signature octets and are printed in advanced form only. The eight transport fixtures above
  are the draft's whole base64 output (`normative.md` SD-33, a pass-2 finding).

## What is not here

The draft prints no canonical-form key or certificate bytes in hex, no signature
over a certificate, no CRL, delta-CRL, revalidation reply, one-time reply, k-of-n
subject, online test, tag with a `*` form other than `(*)`, range, set or prefix
example, and no sequence. The messages file carries a minimal instance of each
object (derived, checked against 9.2) so those have a fixture-like vector, but they
are this library's and are not in `examples/`.

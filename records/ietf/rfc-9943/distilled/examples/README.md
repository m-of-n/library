---
record: rfc-9943
kind: examples
title: "rfc-9943 — examples and test vectors"
extracted: "2026-09-30"
reviewed_by: ""
---

# Examples and test vectors

**Not applicable — the source contains no reproducible example.** Recorded in
`record.yaml` under `distillation.not_applicable`. This file holds the finding;
there are no fixtures to hold.

## What the RFC actually ships

Eleven figures. Six are EDN examples and every one of them is cryptographically
inert:

| figure | § | what it shows |
|---|---|---|
| Figure 4 | §6.1 | EDN Signed Statement, detached payload |
| Figure 5 | §6.1 | EDN decoded protected header — `1: -7` (ES256), `3: application/example+json`, `4: h'…'`, `15: {1: software.vendor.example, 2: vendor.product.example}` |
| Figure 8 | §7 | EDN Transparent Statement with two Receipts under label 394 |
| Figure 9 | §7 | EDN Receipt with `396: {-1: [...]}` |
| Figure 10 | §7 | EDN Receipt protected header with `395: 1` |
| Figure 11 | §7 | EDN inclusion proof — `[8 /tree size/, 7 /leaf index/, [3 intermediate hashes]]` |

Figures 1, 2 and 6 are ASCII diagrams; Figures 3 and 7 are the normative CDDL,
extracted to `../schema/`.

## Why there is nothing to extract

**Every hex literal in the document is elided.** Fourteen `h'…'` byte strings
appear, and all fourteen are written in the truncated form `h'a4012603...6d706c65'`.
Mechanically:

```sh
grep -c "[0-9a-f]\{32\}" .cache/rfc-editor-org-rfc-rfc9943-txt.bin   # 0
grep -o "h'[^']*'" .cache/rfc-editor-org-rfc-rfc9943-txt.bin | wc -l # 14
```

Zero complete 32-hex runs. There is no base64, no complete CBOR encoding, and
no key material. Not one signature, inclusion proof or digest in this RFC can
be recomputed, and nothing in it can be turned into a fixture that a test
harness would run.

The six EDN figures are structurally informative — together with the §7 prose
that introduces them, they are where labels 395, 396, `-1`, `-2`,
`RFC9162_SHA256 = 1` and the inclusion-proof tuple
`[tree_size, leaf_index, [hashes]]` appear at all, since none of those is in
the normative CDDL. Which of the two — figure or prose — carries each one is
worth stating exactly, because `messages.yaml` distinguishes them and a reader
should not have to re-derive it:

| item | where it actually appears |
|---|---|
| `394` receipts | *for contrast:* §7 prose (line 1150) **and** Figure 8, **and** both CDDL figures — the only label here that this RFC defines normatively |
| `396` proofs | Figure 9's unprotected header, and §7 prose "The unprotected header contains VDP" |
| `-1` inclusion proofs | Figure 9, inside the `396` map; also named in §7 prose |
| `395` VDS algorithm | Figure 10's protected header; §7 prose "The VDS (395) uses 1 from RFC9162_SHA256" |
| `-2` consistency proofs | **§7 prose only (line 1177) — no figure in this RFC shows one** |
| `RFC9162_SHA256 = 1` | **§7 prose only (lines 1174–1176) — Figure 10 shows the value `1`, never the name** |
| inclusion-proof tuple | Figure 11, decoded; Figure 9 carries it elided as `h'83080783…32568964'` |

All of it is carried in `../messages.yaml` under `example_derived_labels`,
whose `status` reads `EXAMPLE-DERIVED - not normatively defined in RFC 9943`
and whose `authority` is `rfc-9942`. Neither this file nor `messages.yaml`
treats any of these labels as an RFC 9943 requirement, and none of them has a
`constrained_by` entry, because no requirement in `../requirements.yaml` quotes
them. What cannot be carried is bytes.

## Two defects the figures do contain

Both are recorded as INC-2 and INC-3 in `../messages.yaml`:

- **Figure 10 is mislabelled in the prose.** §7 calls it "the protected header
  of the Transparent Statement in Figure 8", but the caption says a Receipt's
  protected header and the contents — `iss: transparency.vendor.example` and
  label 395 — are a Receipt's. The caption is right.
- **Figure 8's second Receipt opens `h'c624…'`.** `0xc6` is CBOR tag(6), not
  tag(18); the first Receipt's `h'd284…'` is correct. It reads as a typo inside
  bytes that are elided anyway.

## If fixtures are wanted later

They must come from outside this document. `rfc-9942`'s `record.yaml` records a
lead on SCITT WG receipt-verification vectors; that is a separate fetch and a
separate record, not an extraction of this RFC.

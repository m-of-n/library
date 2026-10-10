---
record: rfc-9942
kind: examples
title: "rfc-9942 — examples and test vectors"
extracted: "2026-09-30"
reviewed_by: ""
---

# Examples and test vectors

**Not applicable — the source contains no reproducible example.** Recorded in
`record.yaml` under `distillation.not_applicable`. This file holds the finding.

## What the RFC ships

Nine figures. Six are CDDL and are extracted verbatim to `../schema/`. Three
are EDN examples, and all three are cryptographically inert:

| figure | § | line | what it shows |
|---|---|---|---|
| Figure 2 | §4.3 | 398 | "An Example COSE Signature with Multiple Receipts" — a `COSE_Sign1` with two nested receipts |
| Figure 6 | §5.2.1 | 551 | "Receipt of Inclusion" — detached payload |
| Figure 9 | §5.3.1 | 663 | "Example Consistency Receipt" — a 6-element consistency path |

Note Figure 2 is introduced by the source itself as informative.

## Why there is nothing to extract

**Every hex literal in the document is elided.** Twenty-one `h'…'` byte strings
appear, and not one is complete — all are written in the truncated form
`h'bc297b51...e4edf0de'`. Mechanically:

```sh
grep -o "h'[^']*'" .cache/rfc-editor-org-rfc-rfc9942-txt.bin | wc -l        # 21
grep -o "h'[^']*'" .cache/rfc-editor-org-rfc-rfc9942-txt.bin | grep -vc '\.\.\.'  # 0
grep -c "[0-9a-f]\{32\}" .cache/rfc-editor-org-rfc-rfc9942-txt.bin          # 0
```

Zero non-elided literals, zero complete 32-hex runs. There is no base64 and no
key material. **Not one Merkle root, inclusion proof, consistency proof or
signature in this RFC can be recomputed**, so nothing here can become a fixture
a test harness would run.

This matters more for RFC 9942 than for most documents, because this RFC is
where the proof *encodings* live. A reader can learn the shape of an inclusion
proof from Figure 3's CDDL; nobody can confirm their implementation computes
one correctly using anything in this document.

## Where fixtures would have to come from

Two places, both outside this record:

- **RFC 9162**, which defines the one verifiable data structure
  (`RFC9162_SHA256`) and the Merkle arithmetic this RFC delegates entirely. The
  library holds `rfc-9162` only as a `stub` whose bytes have **never been
  fetched** — `date` and `content.sha256` are both empty. It is the highest-value
  next fetch in this topic.
- The **SCITT WG receipt-verification vectors** lead already recorded in this
  record's `record.yaml`. That is a separate fetch and a separate record, not an
  extraction of this RFC. One source reports vectors covering `vds=2` for
  Microsoft CCF, which if true means the registry has already grown past the
  single value this RFC defines — **unverified**, and unverifiable from here,
  since the library holds no record of either subregistry §8.2 creates.

---
record: rfc-9596
kind: examples
title: "rfc-9596 — examples and test vectors"
extracted: "2026-10-20"
reviewed_by: ""
---

# Not applicable, and the absence is the finding

**RFC 9596 prints not one byte.** No hex, no CBOR diagnostic notation, no
figure, no complete COSE object, no `typ` value in a worked setting.

Measured over all 232 lines of `.cache/rfc-9596.txt`, whole-word and
case-insensitive:

| token | occurrences | note |
|---|---|---|
| `Figure` | **0** | |
| `hex` | **0** | |
| `vector` / `test vector` | **0** | |
| `diagnostic notation` | **0** | |
| `example` | **1** | line 89 — *"An example of a COSE object is a COSE_Sign1 structure, as described in Section 4.2 of [RFC9052]."* A **definition**, not a fixture |
| `examples` | **0** | |

The only structural rendering in the document is §4.1's Table 1, an IANA
registration, which is captured verbatim in `../schema/source-renderings.txt`.

## What that costs us specifically

**Not one `typ` value is named anywhere in the document.** §2 says the value
is an unsigned integer from the CoAP Content-Formats registry or a string
content type value — **glossed here rather than quoted**, because the source
**breaks the registry name across lines 116/117** (`"CoAP Content-` then
`Formats" registry`) and this directory does not heal line breaks. The
obligation-bearing half, quoted whole and unhealed: *"or a string content type
value. Content type values have a media type name [MediaTypes] and MAY include
media type parameters."* The byte-exact span is in
`../schema/source-renderings.txt`. Either way, the document then gives **no
instance of either branch.**

**[correction, found by this pass's own quote audit]** An earlier draft of this
file quoted that sentence with *"CoAP Content-Formats"* written as one token,
which **silently healed the line break** — the second of the five transcription
defect classes this lane's audit was built to catch, and the one this directory
declares three times that it does not commit. Caught here and corrected.

So:

- there is **no reference fixture** for the mechanism;
- there is **no worked example of the equality problem** the mechanism has —
  the same type has two wire spellings (`typ: 61` and
  `typ: "application/cwt"`, from `rfc-8392` §9.3.1 and §9.2.1) and the
  document never puts them side by side;
- and **every fixture we build is ours**, under `R-O-03`, with nothing to cite.

**The contrast inside this one lane is the useful measurement:**

| record | printed vectors | verified in pass 1 |
|---|---|---|
| `rfc-8392` | **five complete CWTs**, nine figures | all five — signature, both MAC tags, both decryptions |
| `rfc-9597` | **none** | — |
| `rfc-9596` | **none** | — |

The base document of the lane supplies reference bytes for the envelope and
**neither of the two header parameters we would actually rely on supplies
any.** `records/ietf/rfc-9942` §4.4 points at `typ` and prints nothing;
`records/ietf/rfc-9943` §6 requires `rfc-9597`'s label 15 and makes
`content_type` (3) optional, and names no `typ` value either.

`examples` is therefore declared `not_applicable` in `record.yaml` with this
measurement as its reason. This file exists so the measurement is readable from
inside the artifact set, not only from `record.yaml`.

---
schema: "library-summary/v1"
id: iana-cbor-simple-values
record: iana-cbor-simple-values
type: summary
updated: "2026-10-16"
---

# IANA Concise Binary Object Representation (CBOR) Simple Values Registry

|  |  |
|---|---|
| **Type** | dataset |
| **Maturity** | informational — a live allocation table, not a work with RFC 2026 standing |
| **Authors** | — (a registry has none; maintained by IANA under RFC 8949 §9.1) |
| **Published** | snapshot of 2026-10-16 |
| **Identifier** | https://www.iana.org/assignments/cbor-simple-values/cbor-simple-values.xhtml |
| **Source** | https://www.iana.org/assignments/cbor-simple-values/cbor-simple-values.xhtml |
| **Digest** | `d1733d66c866…` (sha-256 of the .xhtml, retrieved 2026-10-16) |

## Overview

CBOR's second extension point, and much the smaller of the two. Major type 7
carries "simple values" — values that are identified by a number but carry no
payload — and RFC 8949 §3.3 delegates that number space to IANA. The registry
is nearly empty and almost entirely spoken for by the base specification:
**`20` False, `21` True, `22` Null, `23` Undefined**, with `24-31` Reserved
(the two-byte encoding form RFC 8949 forbids an encoder from emitting) and
essentially everything else Unassigned.

Exactly one non-base allocation exists in this snapshot: **`59`**, a
`sd-cwt` redaction marker from `draft-ietf-spice-sd-cwt-06` §5.1, registered
2025-12-16 — and it is `TEMPORARY`, expiring 2026-12-16.

The extracted table is in `distilled/tables.yaml`. Like its sibling
`iana-cbor-tags`, this record is **not** an FX-1 extraction: it is a
`type: dataset` held to the summary bar, as library#39 scoped both registries.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Naming | supporting | The same governance shape as the tag registry — a globally shared, centrally allocated namespace — so the R-M-12 argument has to cover it, but the stakes are far smaller. |
| Encoding | supporting | Decides which of major type 7's code points a reduced profile admits. |

**Why we hold it, given how little is in it.** The record's own reason says it
plainly: the second CBOR extension point, *"governed the same way, so the
R-M-12 argument must cover it."* An argument that CBOR's extensibility is
registry-dependent would be incomplete if it addressed only tags.

**The practical finding is an absence, and it is good news for option 5.**
Because the registry is almost entirely Unassigned, excluding it costs us
nothing — unlike the tag registry, where exclusion gives up date/time,
bignums, nested CBOR and binary UUIDs. A reduced profile needs `20`, `21` and
`22`; dCBOR §2.6 admits exactly those three plus the floats, and rejects every
other major type 7 value including `23` Undefined. **So on this registry,
option 5's exclusion and dCBOR's narrowing agree,** and the only live question
is whether `23` Undefined is admitted — which dCBOR answers no.

Entry `59` is also a small, concrete illustration of the governance point: a
draft that has not been published as an RFC holds a code point in the shared
space on a timer, and if the draft stalls the allocation evaporates.

## Implementations

A registry is consumed, not implemented. Every CBOR library hard-codes `20`
through `23` because they are the base specification; *searched on 2026-10-16
for a library that consults this registry dynamically, none found*, which is
unsurprising given it has one non-base entry.

## Limits

- **Live, and already drifted.** The digest previously on this record
  (`bcd0848a…`, retrieved 2026-09-22) no longer matched when re-fetched three
  weeks later. Counts here are true as of 2026-10-16 only.
- **The one interesting entry is temporary.** `59` expires 2026-12-16 unless
  `draft-ietf-spice-sd-cwt` advances.
- The snapshot's row list is sparse by construction — ranges such as `0-19`,
  `24-31` and `60-255` are kept exactly as the page expresses them and are not
  expanded, because the shape of the unassigned space is part of what the
  registry says.

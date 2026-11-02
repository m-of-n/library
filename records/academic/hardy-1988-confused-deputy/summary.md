---
schema: "library-summary/v1"
id: hardy-1988-confused-deputy
record: hardy-1988-confused-deputy
type: summary
updated: "2026-11-01"
---

# The Confused Deputy (or why capabilities might have been invented)

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_: the enum has no value for a journal paper |
| **Authors** | Norm Hardy |
| **Published** | 1988-10 |
| **Identifier** | DOI 10.1145/54289.871709 |
| **Source** | https://web.archive.org/web/20251201085711id_/https://dl.acm.org/doi/pdf/10.1145/54289.871709 |
| **Digest** | `sha256:124c9e46…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Venue** | ACM SIGOPS Operating Systems Review 22(4), 36-38 |

## Overview

A compiler holds authority to write its home directory, and a user supplies the name of the billing file as the debug output file. The operating system sees authority and lets the write happen (p. 36). Hardy's diagnosis: the compiler carries authority from two sources and has no way to say which one it means for a given action, which is why it is a confused deputy (p. 37). Adding hat-switching system calls did not scale. The capability answer merges designation and authority: the compiler refers to a capability, not a textual name, and that one reference both identifies the file and authorizes the write (p. 37).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The canonical statement of the confused-deputy failure |
| Cryptography | `none` | No cryptography |
| This project | `adjacent` | A test for our model, not a requirement |

- **R-M-04**: ARCH-0001 keeps name bindings and authorization bindings as distinct object kinds. Hardy's lesson points the other way at first sight, since he treats separate mechanisms for choosing a target and authorizing it as a sign of poor design (p. 37). The two meet if the subject of an `AuthzCert` is a key, because a key designates and proves together. A design that resolves a name and then checks authority against the result reintroduces the gap Hardy describes. Worth checking when R-O-06's separate results are specified.

## Implementations

Not searched. The paper names KeyKOS, a historical system, and the patent US 4,584,639 (p. 38).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `paper` record owes FX-1 only if someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **One anecdote.** The argument is a single incident with "inessential details" changed (p. 36). The closing claims about KeyKOS size and performance are the author's and carry no measurements.
- **It does not show that capabilities suffice.** Hardy points at KeyKOS for the wider claim. A capability system with bearer tokens can still be confused by a caller who passes the wrong capability.
- **Later citations stretch it.** ZCAP uses CSRF as its confused-deputy example, and agent-token drafts apply it to prompt injection. Those are analogies that this paper does not make.
- **Read scope.** Read whole, from an OCR text layer of ACM's scanned PDF via an Internet Archive capture. Quoted text was checked against the cap-lore transcription as well.

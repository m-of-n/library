---
schema: "library-summary/v1"
id: iana-cbor-tags
record: iana-cbor-tags
type: summary
updated: "2026-10-16"
---

# IANA Concise Binary Object Representation (CBOR) Tags Registry

|  |  |
|---|---|
| **Type** | dataset |
| **Maturity** | informational — a live allocation table, not a work with RFC 2026 standing |
| **Authors** | — (a registry has none; maintained by IANA under RFC 8949 §9.2) |
| **Published** | snapshot of 2026-10-16; page created 2013-09-19, last updated 2026-10-08 |
| **Identifier** | https://www.iana.org/assignments/cbor-tags/cbor-tags.xhtml |
| **Source** | https://www.iana.org/assignments/cbor-tags/cbor-tags.xhtml |
| **Digest** | `5f3570cfb43b…` (sha-256 of the .xhtml, retrieved 2026-10-16) |

## Overview

This is the allocation table for CBOR's single extension point. RFC 8949 §3.4
defines major type 6 as a tag — a number prefixed to a data item that says how
to interpret it — and delegates the entire number space to IANA. The registry
is therefore the place where CBOR's semantics, as opposed to its syntax, are
actually defined: `0` and `1` are the two date/time forms, `2` and `3` are
bignums, `24` is an encoded CBOR data item nested inside a byte string, `18` is
`COSE_Sign1`, `61` is a CWT, `1001` is RFC 9581 extended time, and `55799` is
the self-describing CBOR magic number.

The snapshot holds **358 rows** in the tag space itself, plus two RFC 9581
sub-registries on the same page (Timescales, 3 rows; Time Tag Map Keys, 29
rows) and the page's Range / Registration Procedures table. Allocation policy
varies by range: the low, cheap-to-encode numbers are the scarce ones and are
governed by Standards Action or Specification Required, while the space above
32768 is First Come First Served and runs to 2^64-1.

The extracted table is in `distilled/tables.yaml`, row-for-row and complete.
This record is **not** an FX-1 extraction and is not an unfinished one: it is a
`type: dataset` held to the summary bar, as library#39 scoped it — *"registries,
not FX-1 types; extract the tables as data, because option 5 is defined by what
it excludes."* A registry states no requirements and specifies no protocol, so
most of the FX-1 artifact set has no subject here. See `distilled/README.md`.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | supporting | Tags carry semantics into the signed bytes. Tag 18 is the COSE signature envelope itself, so what this registry says is inside the thing we sign. |
| Naming | **core** | This is the strongest single piece of evidence for R-M-12: CBOR's extension point is a globally shared, centrally allocated namespace, so a native model built on tags is registry-dependent by construction. |
| Encoding | **core** | MD-3 narrows DEC-002 to option 5, *"reduced CBOR, no IANA tags, COSE export only"*. This registry is precisely the thing option 5 excludes, so it is the measure of what that exclusion costs. |

**What option 5 gives up, concretely.** Excluding tags means giving up the
registered meanings, not just the registry. The ones that would otherwise have
been load-bearing for us:

- **`0` / `1` — date/time.** Every attestation has a validity window. Without
  tags, time becomes an ordinary map entry whose format we define and must
  specify, test and defend ourselves.
- **`2` / `3` — bignums.** The escape hatch for integers outside the 64-bit
  range. RFC 8949 §3.4.3's preferred-serialisation rule for them is a known
  determinism trap, so losing them is partly a relief — but it is also the
  only standard answer to "this number does not fit".
- **`24` — encoded CBOR data item.** The standard way to nest an opaque,
  independently-signed blob inside a structure. Directly relevant to carrying
  one statement inside another.
- **`37` — binary UUID.** Note its Reference column: a GitHub URL and a
  personal name, not an RFC. A code point in the shared namespace whose
  authority is one person's repository. That is the governance argument for
  R-M-12 in a single row.
- **`18` — `COSE_Sign1`.** Unavoidable if we export to COSE at all, which
  option 5 explicitly does. **Option 5 does not escape this registry; it only
  stops using it natively.** That tension belongs in the encoding ADR.
- **`201` — "enclosed dCBOR".** dCBOR's own conformance marker is a registered
  tag. The profile closest to option 5 announces itself using exactly the
  mechanism option 5 refuses, so a key-relative substitute has to be designed.
  Its Reference reads `draft-mcnally-deterministic-cbor-10` while the current
  draft is -18 — the registry is already stale against its own source.

## Implementations

Not applicable in the usual sense: a registry is consumed, not implemented.
Every general-purpose CBOR library ships a partial, hard-coded subset of these
tags — typically `0`, `1`, `2`, `3`, `24` and `55799` — and treats the rest as
opaque. That partiality is itself a finding: *searched for a library that
implements the registry completely on 2026-10-16, none found*, and there is no
reason to expect one, because the registry grows and libraries do not.

## Limits

- **It is live, and it moved under us.** The digest previously recorded on this
  record (`0d338a17…`, retrieved 2026-09-22) no longer matched the page three
  weeks later. Pinning a sha-256 to a living document does not make it stable;
  it only makes the drift detectable. Every count here is true as of
  2026-10-16 and must be re-checked, not cited as settled.
- **Three `TEMPORARY` registrations (tags 58, 60, 62) expire in 2026 and 2027**
  and will simply vanish from the table.
- The page's Contact Information table — registrant names and obfuscated
  e-mail addresses — is deliberately not captured. It is personal contact data,
  not a registry assignment.
- A registry records *what was allocated*, never *what is used*. Nothing here
  says whether a tag has a single deployed implementation.

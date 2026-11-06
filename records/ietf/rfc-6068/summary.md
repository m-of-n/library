---
schema: "library-summary/v1"
id: rfc-6068
record: rfc-6068
type: summary
updated: "2026-11-04"
---

# The 'mailto' URI Scheme

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc6068.json` 2026-11-01 |
| **Authors** | M. Duerst, L. Masinter, J. Zawinski |
| **Published** | 2010-10 |
| **Identifier** | RFC 6068 · DOI 10.17487/RFC6068 |
| **Source** | https://www.rfc-editor.org/rfc/rfc6068.txt |
| **Digest** | `sha256:a450492a…` (full value in `record.yaml`), fetched 2026-11-01, rechecked 2026-11-04 |

## Overview

RFC 6068 defines the `mailto` URI as a name for a mailbox, optionally with a template for a message to it (§2, §3). Unlike an `http` URI, resolving one causes no immediate interaction with a server: the client composes a message the user may edit, send or drop (§3). So most of the document's weight is on what must not be trusted in the URI. Originator, routing, trace and MIME header fields must be ignored (§3), and the client should show the full message and get approval before sending (§7). This revision adds UTF-8 percent-encoding, and reserves percent-encoding in the local part for internationalised addresses (§2, §9).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §4 and §7: unsafe headers, hidden URIs, address harvesting |
| Cryptography | `none` | §5 notes that, lacking variable substitution, a mailto URI cannot carry a public-key signature or other variable information |
| This project | `none` | Bears on no `DEC-*` or `R-*` |

**Bears on no `DEC-*` or `R-*`.** It is held because `draft-ietf-vcon-vcon-core-04` §4.2.4 lets the party `mailto` value be an address in "any common form", such as a bare address or a mailto URL, with the `mailto:` prefix optional.

That optionality has a cost the draft may not state: the same mailbox has more than one valid string. §2 adds percent-encoding on top, and §2's rule on applying encoding only once shows the risk. Comparing party mailboxes would need normalisation. We did not check whether the draft addresses that.

## Relations

- `see_also: draft-ietf-vcon-vcon-core-04`: that draft cites this RFC as `[MAILTO]` for the party `mailto` parameter (§4.2.4). The edge is authored only here. `rfc-8551` authors its own edge to this record.

## Implementations

**Searched 2026-11-01.** One GitHub repository search for `rfc6068 mailto` returned no results. That is one query against repository metadata, not a survey, and mailto handling normally sits inside mail clients and URI libraries.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `rfc` record owes FX-1 when someone extracts it, and no issue owns that for this record yet: the 2026-10-25 decision on #45 moved extraction to per-set issues, and neither #69 nor #89 covers it. No keyword count is given because none has been reconciled.

## Limits

- **It says nothing about ownership.** A mailto URI names a mailbox, not a person, and does not show that anyone controls it.
- **Address syntax is RFC 5322's**, excluding comments (§2). That is not held here.
- **§2 reserves the local-part encoding for a future specification.** Whether later work (§1 names only the then-ongoing effort) changed it was not checked.
- **Errata.** `errata.json` retrieved 2026-11-01, recounted 2026-11-04, lists 2 verified, 2 held, 1 reported and 1 rejected. Their text was not reviewed.
- **Read scope.** Whole document, from the RFC Editor `.txt`.

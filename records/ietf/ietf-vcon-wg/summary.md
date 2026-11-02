---
schema: "library-summary/v1"
id: ietf-vcon-wg
record: ietf-vcon-wg
type: summary
updated: "2026-11-01"
---

# IETF Virtualized Conversations (vcon) Working Group

|  |  |
|---|---|
| **Type** | consortium |
| **Maturity** | _unset_: a working group, so RFC 2026 levels do not apply |
| **Authors** | _none: a working group_ |
| **Published** | _not established (see Limits)_ |
| **Identifier** | vcon · charter-ietf-vcon-01 |
| **Source** | https://datatracker.ietf.org/wg/vcon/about/ |
| **Digest** | `sha256:c8b1c1a4…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The vcon WG exists to standardise a container for conversational data, between two forces its charter names: privacy of personal data and the wish to use conversations, for example in AI analysis. It is chartered for a Standards Track JSON container and media type, for the use of an existing mechanism for integrity and optional authenticity, and for the use of an existing mechanism for encryption. Key management, transport, storage, APIs and analysis methods are out of scope, as is a new object security model, on the expectation that JOSE or other existing IETF technology suffices. Its members are the two drafts held here, `draft-ietf-vcon-vcon-core-04` and `draft-ietf-vcon-overview-02`.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Charters integrity and confidentiality for conversation data |
| Cryptography | `adjacent` | Charters use of an existing mechanism. A new object security model is out of scope |
| This project | `adjacent` | Bears on no `DEC-*` or `R-*` directly. Its documents do |

**Bears on no `DEC-*` or `R-*` directly.** `draft-ietf-vcon-vcon-core-04` carries DEC-005 and R-M-11. This record supplies the mandate to judge that draft against. Both points the stub flagged were checked against the charter text:

1. **Layering.** The charter's wording is "Define/specify the use of an existing mechanism for proving integrity and optionally authenticity". That cuts both ways, as the stub expected: it rules out inventing a signature format, and it still leaves the WG owing the placement rules that core §5.2 attempts. So charter deference does not excuse those choices.
2. **Selective disclosure.** Encryption is chartered "such that some parts of the vCon may be disclosed to different parties", and of "the objects enclosed in the vCon". Core -04 §5.3 encrypts the whole signed form, and `rfc-7516` §7.2.1 gives all recipients one ciphertext. So per-part disclosure is chartered and not delivered by that construction. The overview also lists redaction methods and Merkle-style redaction validation as out of its scope (`draft-ietf-vcon-overview-02` §1.4.1).

## Implementations

**Not applicable: this is an organisation.** Implementations of its drafts are on `draft-ietf-vcon-vcon-core-04`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This record is an organisation and its charter, which is not an extraction target.

## Limits

- **The charter is not the output.** It records intent, and the milestones below show it has been overtaken.
- **Milestones are stale.** The page lists draft submissions to the IESG for Jun 2024. Later status was not established beyond the revisions below.
- **Core has moved.** Datatracker shows `draft-ietf-vcon-vcon-core` at -05, dated 2026-10-31. This library holds -04, and that revision is a matter for a separate batch.
- **The charter's date is unknown.** Datatracker's document timestamp for charter-ietf-vcon is 2026-03-18, but whether that is the approval date was not established, so `date` stays empty.
- **Read scope.** The whole About page as served 2026-11-01, including charter, personnel and milestones. The WG's mailing list, meetings and document list were not read.

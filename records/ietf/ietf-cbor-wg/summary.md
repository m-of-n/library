---
schema: "library-summary/v1"
id: ietf-cbor-wg
record: ietf-cbor-wg
type: summary
updated: "2026-11-01"
---

# IETF Concise Binary Object Representation Maintenance and Extensions (CBOR) Working Group

|  |  |
|---|---|
| **Type** | consortium (IETF working group, Applications and Real-Time Area) |
| **Maturity** | unset: a charter has no RFC 2026 standing |
| **Authors** | IETF working group charter. Chairs Barry Leiba, Christian Amsüss, Paul E. Hoffman. AD Andy Newton, as listed 2026-11-01 |
| **Published** | charter-ietf-cbor-03, datatracker last updated 2025-04-09 |
| **Identifier** | charter-ietf-cbor-03 |
| **Source** | https://www.ietf.org/charter/charter-ietf-cbor-03.txt |
| **Digest** | `sha256:f2938e93…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Errata** | not applicable |

## Overview

The CBOR working group's charter gives it three main jobs: maintain CBOR itself, evolve CDDL as a sequence of editions, and take on tag and media type specifications case by case. A fourth item, evaluating developer guidance, is expected to be a wiki rather than an RFC. The last one is the governance answer the topic asks about. The charter says the group evaluates such proposals individually, and that those it deems out of scope, *"for example because they are too narrow in purpose"*, may still be published as individual submissions or in other groups. So the group is a reviewer of the CBOR extension space, not its gatekeeper. The charter says nothing about deterministic encoding, and it never mentions IANA.

The charter text has aged. It still describes `draft-ietf-cbor-7049bis` as in the RFC Editor queue, while the group's documents page lists RFC 8949 as published. Live work is on that page, not in the charter: the only open milestone is an updated CDDL to the IESG by June 2027.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Owns the format we decode, but its documents carry the security content, not the charter |
| Cryptography | `none` | Publishes no cryptography |
| This project | `adjacent` | DEC-002 rests on its RFC 8949, and it sits beside the extension points R-M-12 refuses |

- **DEC-002**: accepted by `ADR-0004` as RFC 8949 §4.2.1 under a restricted profile. Determinism work continues here, on documents KSA-CBOR does not depend on: `draft-ietf-cbor-serialization` reads *Publication Requested* (moved to *AD Evaluation* 2026-11-03, per its history page read 2026-11-05), and `draft-ietf-cbor-cde` reads *Expired*, both on the group's documents page 2026-11-01. A change to the determinism text in this group would be a change to what `ADR-0004` cites.
- **R-M-12** (relocated to `ARCH-0002` P1 by `ADR-0001`): this group reviews tag specifications, which are the kind of centrally allocated extension point P1 excludes from the native model. The charter sets no allocation policy. That is out of this record's reach.

## Implementations

**Not applicable, 2026-11-01.** A working group is not software. Its RFCs carry their own implementation lists. The about page links a CBOR playground and a content collection, which were not assessed.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** A working group charter is not an `rfc`, `draft`, `spec` or `ietf` type record, so FX-1 does not reach it. No `maturity` is set: a charter has no RFC 2026 standing and no value in the schema's enum fits it. The digest is of the charter text, because the about page cannot hold one.

## Limits

- **It does not settle who allocates tags.** The charter is silent on IANA. Allocation policy is RFC 8949 §9.2 and the `iana-cbor-tags` record, neither read for this record.
- **It does not describe current work.** The charter text predates RFC 8949's publication, as above. Draft states here are a reading of one page on one date.
- **Membership.** The documents page lists 12 RFCs, and the records marked `part_of` this group are exactly those 12 plus five of its drafts (checked 2026-11-05). `rfc-7049` (a non-WG document) and `rfc-9781` (from RATS) are not marked `part_of` it.
- **Read scope.** The whole charter text. The about page and the documents page, as text. The history page was checked only for charter events. Mailing list, wiki and repositories not read.

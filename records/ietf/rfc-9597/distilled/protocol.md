---
record: rfc-9597
kind: protocol
title: "rfc-9597 — protocol model"
extracted: "2026-10-20"
reviewed_by: ""
---

# Not applicable, and here is the measurement

**RFC 9597 defines no protocol.** It registers one COSE header parameter
(label 15) and states three rules about it. There is no exchange to draw and no
Mermaid diagram in this file, because drawing one would invent parties the
document does not have.

Measured over all 265 lines of `.cache/rfc-9597.txt`, whole-word and
case-insensitive: `protocol`, `exchange`, `handshake`, `negotiate`, `sender`,
`receiver`, `verifier`, `response`, `transport`, `party`, `producer`,
`consumer`, `step` and `steps` each occur **zero** times.

Four near-misses, none of them a role in a flow:

| token | occurrences | where |
|---|---|---|
| `recipients` | **1** | line 108 — the subject of the `MUST NOT` |
| `request` | **1** | line 6 — the RFC masthead |
| `parties` | **1** | line 167 — §3's privacy sentence |
| `application` / `applications` | 9 | the party that decides what the format does not |

## The one receiver-side check, and why it is not a flow

§2 carries a single predicate an application must evaluate:

> In cases where CWT claims are present both in the payload and the header of a
> CWT, an application receiving such a structure MUST verify that their values
> are identical, unless the application defines other specific processing rules
> for these claims.

**No failure action, no ordering, no error path, no counterparty.** It is one
check, and it is carried in `requirements.yaml` (R-0019) and in `messages.yaml`
as a constraint on the payload claim — which is where a check belongs when
there is no flow to put it in.

*[correction 2026-10-21, pass 3 — cross-check] This read `R-0020` here and in
`protocol.yaml`. R-0020 is §2's RECOMMENDED protected placement; the
duplication `MUST` quoted above is `R-0019`.*

**It is also a step that another document's procedure does not contain.**
`rfc-8392` §7.2's seven validation steps say nothing about header claims, and
RFC 9597 carries no `Updates: 8392` header. An implementer working from
RFC 8392 alone never learns the rule exists.

`records/ietf/rfc-9052` holds the signing and verification procedures, and
`records/ietf/rfc-8392` holds the CWT creation and validation procedures — that
record's `protocol.yaml` is **applicable** and models all three of its flows.

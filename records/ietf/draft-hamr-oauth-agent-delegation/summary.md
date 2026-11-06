---
schema: "library-summary/v1"
id: draft-hamr-oauth-agent-delegation
record: draft-hamr-oauth-agent-delegation
type: summary
updated: "2026-11-05"
---

# An Attenuated Delegation Profile for Automated Agents

|  |  |
|---|---|
| **Type** | draft (individual) |
| **Maturity** | `draft`: individual Internet-Draft, Active, no working group, per datatracker 2026-11-01, re-checked 2026-11-05 |
| **Authors** | A. Hassan |
| **Published** | 2026-10-22 |
| **Identifier** | draft-hamr-oauth-agent-delegation-03 |
| **Source** | https://www.ietf.org/archive/id/draft-hamr-oauth-agent-delegation-03.txt |
| **Digest** | `sha256:79273784…` (full value in `record.yaml`), fetched 2026-11-01, re-verified 2026-11-05 |

## Overview

This draft adds an `Agent-Delegation` HTTP field to `rfc-9421`, carrying a chain of links, each of which can only narrow scope, floors and expiry (§1, §7). Its scope rule is the bluntest possible: capability strings are opaque, containment is exact octet-for-octet set membership, and §6 forbids wildcards, hierarchy, case folding and any canonicalization, because a verifier using a richer rule could accept a chain that another rejects. Everything else is deliberately coarse. Each call has a class of r, w or x, read as in chmod, and a signed menu assigns classes (§9.4). Floors add yes-or-no attestations about the person behind the agent (§8, §11). Its motivating claim is that a limit a model enforces on itself is no limit, so the check has to sit outside the model (§1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Verifier placement outside the model, with explicit non-goals |
| Cryptography | `adjacent` | Uses RFC 9421 and leaves link format open |
| This project | `adjacent` | Bounds the design space, does not fit our object model |

- **DEC-004**: §6 is the minimal end of the tag design space, and matches ARCH-0001's starting idea of an opaque byte-string tag under a bytes-equal profile.
- **R-M-08**: set containment of opaque strings is defined completely and trivially. §6 calls wildcards and hierarchy future work, which is the price.
- **R-O-02**: no revocation. A short expiry is the only limit on a link's life (§1, §17).

## Implementations

**Checked 2026-11-01.** Both repositories are named by §16 and were confirmed through the GitHub API. §16 itself says all are single-author with no external review, and that no code at this revision implements action classes, a signed menu or budgets. §16 also lists a third, bareguard, which was not checked.

| Name | Kind | License | URL |
|---|---|---|---|
| justabit | open source, Node.js proof of concept of the attestation side | Apache-2.0 | https://github.com/hamr0/justabit |
| rwxmap | open source; builds a menu from an OpenAPI description | Apache-2.0 | https://github.com/hamr0/rwxmap |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `draft` record owes FX-1 when someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **Not end to end.** §16 says the proof of concept has no RFC 9421 signatures, no HTTP header and no chain over two links.
- **rwxmap's accuracy is self-reported.** It was scored once on 4279 calls and reproduced from a clean copy by the same author (§1, §16), against truth labels that §16 says were written by language-model agents, with the author ruling disputes.
- **No replay protection, revocation or shared budgets.** §1, §10.4 and §11.2 say so.
- **It defines no credential format** (§4), so two conforming systems need not interoperate.
- **The parent-stays-valid problem is declared unsolved** in §3, with a pointer to `draft-asor-wimse-agent-delegation-chain` §9.1.
- **Relations.** This draft cites `rfc-9421` and `draft-asor-wimse-agent-delegation-chain`, so no `see_also` is needed.
- **Read scope.** Abstract, §1, §3, §4, §6, §7, §15, §16 and §17 were read, and §13's steps were listed. §5, §8 to §12, §14 and Appendices were not read in full, and statements on those sections come from §1 and §17.

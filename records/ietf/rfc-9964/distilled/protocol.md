---
record: rfc-9964
kind: protocol
title: "rfc-9964 — protocol model"
extracted: "2026-10-19"
reviewed_by: ""
---

# Protocol model — none

**RFC 9964 defines no protocol.** There is no diagram here because there is
nothing to draw: no counterparties, no messages, no ordering and no error paths.
`protocol.yaml` carries the measurement; `record.yaml` carries the same
reasoning under `distillation.not_applicable`.

Written out by the verify pass (2026-10-20), which found this file holding the
ingest scaffold's unedited placeholder participant while `distilled/README.md`
described it as a deliberate stub.

## Why there is no sequence to draw

Three measurements, re-counted over all 2906 source lines:

| word | occurrences |
|---|---|
| `verifier`, `sender`, `recipient`, `protocol`, `exchange`, `handshake`, `negotiate` | **0** each |
| `signer` | **1** — line 298, §7.1, in "attackers could impersonate the legitimate signer" |
| `request` | **1** — line 6, the RFC masthead |

**The document hands the envelope to RFC 9052 in its own words** (§5, source
lines 227–229):

> When producing COSE signatures, no encoding is needed; see Section 4 of
> [RFC9052] for more details on how COSE signatures are created.

**And it names no verification algorithm at all.** §5 cites FIPS 204
"Algorithm 2" for producing signatures; nothing anywhere cites Algorithm 3, and
"verify" appears in the prose once, in §7.2's "As the verify routines are
different". A document that specifies no verification procedure has no verifier
side to model.

## What this record carries instead

The signing protocol is RFC 9052's — see `records/ietf/rfc-9052`. What RFC 9964
contributes is the *content* of three fields, and that is where this record's
value is:

- the AKP `COSE_Key` and both §6 thumbprint inputs — `messages.yaml`, `schema/`
- the tag-18 `COSE_Sign1` and `Sig_structure` as Appendix A.2 instantiates them,
  all three verified cryptographically by the verify pass — `examples/`
- the `KeyId` consequence of `alg` being inside the digest — `design-notes.md`

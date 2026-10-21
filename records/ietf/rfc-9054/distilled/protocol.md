---
record: rfc-9054
kind: protocol
title: "rfc-9054 — protocol model"
extracted: "2026-10-20"
reviewed_by: ""
---

# Protocol model — none

**RFC 9054 defines no protocol.** There is no diagram here because there is
nothing to draw: no counterparties, no messages, no media type, no ordering
and no error path. `protocol.yaml` carries the measurement; `record.yaml`
carries the same reasoning under `distillation.not_applicable`.

## Why there is nothing to draw

Counts over all 498 source lines, as whole words, case-insensitively:

| word | occurrences |
|---|---|
| `sender`, `recipient`, `receiver`, `verifier`, `exchange`, `handshake`, `negotiate`, `negotiation`, `response`, `server`, `client`, `retrieve`, `GET`, `intermediary`, "relying party" | **0** each |
| `protocol` | **1** — line 148, in "SHOULD trigger protocol maintainers and users to review" |
| `party` | **1** — line 403, in "is it the originator that is the attacker or a third party?" |
| `verify` | **1** — line 162, in "If the fingerprint is used to verify that it is the correct certificate" |
| `request` | **1** — line 6, the RFC masthead |

## The two candidates, and why neither is a flow

**§1's indirect signing** is the closest. The document describes it fully:

> Rather, the signature can be validated on all of the hash values and
> pointers to the associated contents; those associated parts can then be
> downloaded, then the hash value of that part can be computed and compared to
> the hash value in the signed content.

That is a validation *sequence*, and it names no parties, no messages, no
media types, no ordering obligation and no failure action. It is an
explanation of why the eight identifiers are worth registering. The only
worked instance it points at is **§5.4 of an Internet-Draft**
(`[SUIT-MANIFEST]`, `draft-ietf-suit-manifest-19`).

**§2's filtering argument** is a procedure at a single party, two sentences
long: sort a collection of certificates by fingerprint, then confirm that the
public key validates the signature and discard the false positives. No
counterparty, no message. That procedure is carried in `design-notes.md`
rather than here, because where it does work is as the **precondition
`rfc-9360` §2's protected `x5t` configuration does not satisfy**.

## And the document says the carrier does not exist

§1, source lines 75–80:

> It also does not define a structure syntax that is used to encode a digested
> object structure along the lines of the DigestedData ASN.1 structure in
> [CMS].  This omission was intentional, as a structure consisting of just a
> digest identifier, the content, and a digest value does not, by itself,
> provide any strong security service.

A document with no structure, no parties and no messages has no protocol.

## The obligations it does state are about other documents' protocols

§5: *"Protocols need to perform a careful analysis of the properties of a hash
function that are needed and how they map onto the possible attacks"* and
*"Algorithm agility needs to be considered a requirement for any use of hash
functions"*. Both are addressed outward. **RFC 9054 itself defines no
negotiation, no deprecation mechanism and no way for an endpoint to express
which hash functions it accepts** — which is exactly the gap `rfc-9360` §2's
`MUST support SHA-256` half-fills, in the other document, from the other side.

## The split with `rfc-9360` is real

These two records were extracted as one lane and they divide on this verdict.
`rfc-9360` has four parties, a GET with a transport-security `SHOULD`, an
active intermediary it admits itself, and a two-check join — `protocol`
**applicable**, three flows, five error paths. `rfc-9054` has one occurrence
of the word `protocol` and it means "the people who maintain protocols". The
difference is in the documents, not in how hard each was looked at.

## Where the protocol lives instead

- the signing envelope → `records/ietf/rfc-9052`
- the one position in COSE where these identifiers are consumed →
  `records/ietf/rfc-9360` §2's `x5t`, and its `protocol.yaml`
- the digest carrier `R-M-07` needs → **nowhere**, which is this record's
  whole finding

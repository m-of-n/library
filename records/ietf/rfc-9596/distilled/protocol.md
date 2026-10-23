---
record: rfc-9596
kind: protocol
title: "rfc-9596 — protocol model"
extracted: "2026-10-20"
reviewed_by: ""
---

# Not applicable, and here is the measurement

**RFC 9596 defines no protocol.** It registers one COSE header parameter
(label 16) and states one prohibition about it. There is no exchange to draw
and no Mermaid diagram in this file, because drawing one would invent parties
the document does not have.

Measured over all 232 lines of `.cache/rfc-9596.txt`, whole-word and
case-insensitive: `protocol`, `exchange`, `handshake`, `negotiate`, `sender`,
`receiver`, **`recipient`**, `verifier`, `response`, `transport`, `party`,
`parties`, `producer`, `consumer`, `step` and `steps` each occur **zero**
times. One near-miss: `request` occurs once, at line 6, in the RFC masthead.

**This is the only record in the lane where even `recipient` is absent.**
`rfc-8392` has 8 occurrences and `rfc-9597` has one; this document has none.

## The document says there is nothing to model

> The "typ" (type) header parameter is ignored by COSE implementations
> (libraries implementing [RFC9052] and this specification), other than being
> passed through to applications using those implementations. Any processing of
> this parameter is performed by the COSE application using
> application-specific processing rules.

A parameter whose processing is *defined* as application-specific has no flow of
its own. `application` and `applications` occur **12** times between them, and
that is the finding rather than the exception: the application is the party that
does everything this document declines to do.

## The one check it describes is lowercase and illustrative

§2 offers it as an example — *"For instance, an application might verify that
the "typ" value is a particular application-chosen media type and reject the
data structure if it is not."* §3 repeats it twice as lowercase `should
reject`. Under §1.1's *"when, and only when, they appear in all capitals, as
shown here"*, **neither binds anybody**, so there is no required step, no
ordering and no error path.

**A conformant implementation of RFC 9596 performs no check whatsoever.** That
is not a reading of the silence; it follows from §2's instruction to ignore the
parameter plus §3's choice of lower case.

`records/ietf/rfc-9052` holds the signing and verification procedures, and
`records/ietf/rfc-8392` holds the CWT creation and validation procedures — that
record's `protocol.yaml` is **applicable** and models all three of its flows.

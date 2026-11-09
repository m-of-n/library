---
record: rfc-9162
kind: index
title: "rfc-9162 — distilled artifacts"
extracted: "2026-11-07"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

| kind | file | coverage |
|---|---|---|
| normative | normative.md | every requirement text of requirements.yaml with source lines, verbatim under its section (markers rendered by `bin/check-quotes --render`); the 28 inferred entries listed, not quoted; source defects SD-1 to SD-22 with a table joining them to the ids of the other artifacts; the 2 ASN.1, 11 example and 12 figure code blocks and where each fixture is. Not quoted: the §1.1 BCP 14 recital, which binds nothing |
| requirements | requirements.yaml, inferred-candidates.yaml | 491 entries (125 skeleton BCP 14 sentences, 30 split children, 154 keyword-less statements promoted from candidates, 154 hunted — 151 by pass 1, 3 by pass 2 — and 28 inferred, in our words); all 138 BCP 14 keywords reconciled with `bin/bcp14-count`; every one of the 341 keyword-less candidates has a verdict (154 stated, 3 inferred, 184 reject). §1 to §11, including the §10 IANA registries |
| schema | schema/ | the source's two ASN.1 fragments and its TLS presentation blocks verbatim; 13 derived JSON Schemas for the §5 request, query and response bodies and the error body; `check-schemas.derived.py` runs 28 must-accept and 169 must-reject instances, 9 samples and 2,752,512 prefix probes. The TLS structures of §4 and §6 are exercised as bytes by `examples/reproduce.py`, not as JSON Schema |
| messages | messages.yaml | 37 messages (MSG-01 to MSG-37: every TLS structure, the 7 endpoints with request, response and error codes, the two TLS extension carriers, the X.509 and OCSP carriers, the CMS precertificate profile, the log parameters), 7 encoding rules, 9 registries, 11 source defects; 435 constrained_by links to 355 requirement ids, 12 ids listed unwired with a reason |
| protocol | protocol.yaml, protocol.md | 11 roles, 28 flows (every §5 endpoint, submission, STH issuance, TLS handshake delivery, client validation, monitoring, auditing, freezing, the §2.1 algorithms), 162 steps, every Error Type raised by a named step, 13 source defects and 12 open issues; a Mermaid sequence diagram per flow in protocol.md. Not modelled: the IANA registrations other than Log IDs, the ASN.1 module, §11 discussion that names no step |
| state-machine | state-machine.yaml | 12 machines (the three proof-verification algorithms, log lifecycle, submission to incorporation, STH cadence, TLS handshake, SCT validation, client evidence and compliance, monitor, MMD audit, STH audit), 152 states, 188 transitions, every trigger a message or a defined event. Not modelled: front-end skew selection, client retry, proof generation, gossip |
| examples | examples/ | 23 verbatim fixtures (11 code blocks, 12 figures of §2.1), 5 derived fixtures (the 7-leaf tree, inclusion and consistency proofs, wire vectors, API samples) and `reproduce.py`, 25,501 checks over every tree of 1 to 65 leaves; RFC 9162 prints no values, so every derived value follows from the inputs chosen there |
| design-notes | design-notes.md | 31 rows mapped to our decisions (8 adopt, 4 adapt, 4 reject, 7 constrains, 3 conflicts, 5 silent), the checked proof guarantees, the MD-3 and DEC-002 analysis, the STH and SCT signing-input analysis, 11 open questions |

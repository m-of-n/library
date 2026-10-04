---
schema: "library-summary/v1"
id: rfc-9804
record: rfc-9804
type: summary
updated: "2026-10-04"
---

# Simple Public Key Infrastructure (SPKI) S-Expressions

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | informational — IETF stream, *"not an Internet Standards Track specification"* |
| **Authors** | R. Rivest (MIT CSAIL), D. Eastlake 3rd (Independent) |
| **Published** | June 2025 |
| **Identifier** | RFC 9804 · DOI 10.17487/RFC9804 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9804.txt |
| **Digest** | `0db36cc4bb9d…` (sha-256 of the .txt, retrieved 2026-10-04) |
| **Keywords** | 12 BCP 14 occurrences — 7 MUST, 2 MAY, 2 RECOMMENDED, 1 OPTIONAL |

## Overview

RFC 9804 specifies the S-expression data representation devised for SPKI
certificates (RFC 2692) and published, thirty years later, as a standalone
format *"with the intent that it be more widely applicable."* Its substance is
a **four-way split of representations over one abstract data type**: a
**canonical** form (§6.2) for signing, a **basic transport** form (§6.3) which
is the canonical form or its base-64 wrapper, an **advanced transport** form
(§6.4) for human reading, and a base-64 form for S-expressions (§6.1). Octet
strings may be written verbatim, quoted, as tokens, in hex or in base-64 (§4),
with an optional **display-hint** carrying type information.

The canonical form is length-prefixed and blank-free — `(6:issuer3:bob)` — and
§6.2 states its design goals directly: it is *"used for digital signature
purposes"*, is *"uniquely defined for each S-expression"*, and is *"intended to
be very easy to parse, reasonably economical, and unique for any
S-expression."*

Unlike RFC 8785, **this document ships its own ABNF** — three grammars in §7,
one each for advanced transport, canonical, and basic transport.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | §6.2 is a canonical-form-for-signing definition, and §10 ties it to signature verification directly. |
| Cryptography | adjacent | Defines no primitives. It is the byte representation a signature covers. |
| This project | core | **DEC-002 option 1** ("canonical S-expressions as canonical; JSON as diagnostic"). The §6.2 / §6.4 split is the architectural ancestor of **R-O-05**. |

Bears on **DEC-002**, **R-O-03**, **R-O-05**, and — through §4.7 and §10 —
**R-M-02**.

## Why this record matters even though option 1 is not selected

ARCH-0001 §3.1 records RFC 9804 as not selected and the v0.2.0 proposal records
it as historical. That is a judgement about *adoption*, and it does not make
the document uninformative — it is the only candidate that **solves the
problem this project actually has**, which is why its design keeps resurfacing:

- **Uniqueness is a stated goal, not an emergent property.** §6.2 asserts the
  canonical form is unique for any S-expression. RFC 8949 §4.2 offers
  determinism and leaves fourteen decisions open; RFC 8785 reaches uniqueness
  for maps and prohibits it for arrays. This document claims it outright.
- **The canonical/display split is architectural.** §6.2 is for signatures,
  §6.4 is *"for documentation, design, debugging, and (in some cases) user
  interface."* Two forms, one data type, and only one of them is ever signed.
  That is R-O-05's discipline, stated in 2025 and designed in the 1990s.
- **No verification-ordering mandate.** §10 says only that *"a canonical form
  is required for the consistent creation and verification of digital
  signatures. This is provided in Section 6.2."* There is **no** parse-then-verify
  procedure of the kind RFC 8785 §5 imposes, so nothing here conflicts with
  R-O-05.

## Implementations

Appendix A names seven, *"likely incomplete"*; surveyed 2026-10-04 and listed
as the source gives them.

| Name | Kind | URL |
|---|---|---|
| GNU Libgcrypt | open source | https://gnupg.org/software/libgcrypt/ |
| Ribose RNP (`sexpp`, C++) | open source | https://github.com/rnpgp/sexpp |
| `SexpCode` (C) | open source | J. P. Malkiewicz, GitHub |
| Inferno implementation | open source | — |
| SFEXP — Small Fast S-Expression Library | open source | — |
| SEXPP — S-expression Processor (Ruby) | open source | — |
| Canonical S-expressions (OCaml) | open source | — |

**This is a correction to the received view in this project.** The
`canonical-encoding` topic answer as committed says RFC 9804's cost is
"ecosystem" with "essentially no maintained libraries". That overstates it:
**Libgcrypt is GNU's general-purpose crypto library and RNP is a maintained
OpenPGP implementation**, both of which ship S-expression parsers in active use.
What is genuinely absent is not parsers but an *attestation stack* — nothing
here supplies an envelope, a signing profile, or the tooling ecosystem that
CBOR/COSE and JSON/DSSE bring. The ecosystem argument is real but must be made
about the layer above the parser, not about parsers.

## Limits

- **No authenticated type indicator.** A leading token is convention, not an
  authenticated field, so option 1 needs an envelope just as option 3 does.
- **Octet-string equivalence is RECOMMENDED and application-variable** (§4.7):
  two octet strings are equivalent *"if and only if they have the same
  display-hint and the same data octet-strings"*, but *"a particular
  application might need a different criterion."* Comparison is byte-wise and
  **case-sensitive**, with no Unicode normalisation rule anywhere — so
  condition (6) of the `canonical-encoding` topic is unmet here too, and
  equivalence itself is softer than a canonical form wants.
- **A cross-application display-hint hazard** (§10): untyped octet strings
  represented under one application's default display-hint *"may be treated as
  if they had a different display-hint"* by another. That is a semantics
  divergence reachable without any byte changing.
- **Informational, not standards track** — though, unlike RFC 8785, it is on the
  IETF stream rather than the Independent stream.
- **`display-hint` is an extension point**, and R-M-12 has something to say
  about how its values are allocated. Now assessed, and the answer is a
  prohibition rather than an allocation rule: §4.6 states that a display-hint's
  purpose *"is to provide information on how to display an octet-string to a
  user. It has no other function."* Pressing it into service as the
  authenticated type indicator condition (4) needs would use a field against
  its specified meaning, which is the kind of silent reinterpretation R-O-03
  exists to prevent. `distilled/design-notes.md` condition 4 records it as a
  trap, because it will be proposed.
- **Read scope:** this summary is written from §1, §4.6–§4.7, §6, §7 (structure
  only), §10, §11 and Appendix A. **The FX-1 artifacts under `distilled/` have
  now landed** — all three passes complete, `record.yaml` declares
  `distillation.profile: full` — and they, not this summary, are the citable
  detail. Where the two differ, the artifacts win. Two things found during
  extraction that this summary does not cover: the §4.6 UTF-8 example is
  defective (it prints `\xC3\xB7`, U+00F7, where its prose says *ö*), and the
  §6.2 canonical form has an injectivity crack on the identity path via the
  never-written default display-hint. Both are in `distilled/`.

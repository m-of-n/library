---
schema: "library-summary/v1"
id: rfc-8610
record: rfc-8610
type: summary
updated: "2026-10-18"
---

# Concise Data Definition Language (CDDL)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | standard — Proposed Standard |
| **Authors** | H. Birkholz, C. Vigano, C. Bormann |
| **Published** | June 2019 |
| **Identifier** | RFC 8610 · DOI 10.17487/RFC8610 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8610.txt |
| **Digest** | `3713f2a50e23…` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

CDDL is a notation for saying what shape a CBOR or JSON data item must have:
rules, types, groups, occurrence indicators, and control operators such as
`.size`, `.cbor` and `.regexp`. A schema is a set of rules; an instance
*matches* if the rules allow it. That is the whole semantics — Appendix C
states it as a matching relation between one specification and one instance,
and nothing in the language concerns roles, messages or state.

Two things are worth knowing before relying on it. First, **CDDL deliberately
says nothing about bytes.** Four independent statements forbid reading a schema
as a serialisation constraint (§2.2.3 "CDDL does not provide any language means
to restrict the choice of serialization variants"; §3.2 on definite versus
indefinite length; §3.8.1 that `.size` "is not a representation constraint";
and Appendix E). A CDDL schema alone cannot make an encoding deterministic.
Second, **its extension point is a registry**: new control operators arrive
only "by new versions of this specification or by registering them according to
the procedures in Section 6.1", and the standard prelude "is deemed to be
fixed".

The document is unusual in how its normativity is carried. It has exactly
**two** all-capitals BCP 14 occurrences in 125 KB, and neither binds a CDDL
implementer — one is a `SHOULD` addressed to a *downstream specification
author* (§3.8.3.1), and the other is RFC 8610 quoting RFC 7071 in order to call
it ambiguous, inside an appendix its own first line marks "for information
only". The normative force lives in the grammar and the matching rules instead,
which is why six of the eight appendices open "This appendix is normative."

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Encoding | **core** | library#39 calls CDDL "the schema language for D4's encoding-neutral types", and the extraction assesses it for exactly that. |
| Naming | supporting | CDDL compares text "bytewise identical" and does no Unicode normalisation, which is a second source for the `canonical-encoding` topic's condition (6). |
| Security | supporting | §5 disclaims security relevance for the language itself; the relevance is indirect, through what a schema can and cannot be trusted to check. |

**The verdict, from `distilled/design-notes.md`: competent for representation,
not sufficient for D4 as currently scoped.** `ARCH-0001` §4.1/§4.2 goes across
cleanly in structure, and ARCH-0002 P1's `(defining key, local label)` is
trivially expressible — it is two ordinary fields and CDDL has no opinion about
them. But six things we need cannot be said in CDDL, and the source states each
absence itself. The sharpest:

- **`Threshold` is inexpressible.** `1 ≤ k ≤ n` and `n = len(members)` have no
  construct, and Appendix A confirms CDDL has neither PEG's NOT nor AND, so it
  cannot be smuggled in as an exclusion. **DEC-002's own acceptance test names
  this invariant** — "round-trip fixtures for NameCert, AuthzCert (including
  threshold subject), ArtifactStatement" — so the acceptance fixture asks a
  schema language to check the one thing it cannot. That is a defect in the
  acceptance test, not in CDDL, and the ADR must either move the invariant into
  expected results or name the verifier component that owns it.
- **No sets, and no ordering vocabulary at all** (§3.5). ARCH-0002 P4's domain
  of discourse is a *set*, so P4's hash-as-identity cannot be made well defined
  by a CDDL schema under any DEC-002 option.
- **No semantic layer.** Comments are whitespace and annotations do not exist.
  **So D4's deliverable is not "a CDDL file" but a container that carries one**
  — a scope statement D4 does not presently make.

**Where it cuts against MD-3**, which narrowed DEC-002 to option 5 and is not
an acceptance of it:

- **Option 5 is registry-reduced, not registry-free.** It drops the CBOR tag and
  COSE header registries and adopts a third — CDDL control operators, under
  Specification Required or IETF Review. And the dotted-name rule prices the
  *namespaced* form above the global one, which is precisely the pattern
  ADR-0001 is about.
- **Option 5's defining exclusion cannot be stated in CDDL, only linted.** There
  is no negation, `any = #` includes tags, and the fixed prelude ships **19**
  names that are or reach major type 6 — 16 direct `#6.` productions plus
  `bigint`, `integer` and `unsigned` — none of which can be removed. So "no IANA
  tags" is a lint rule over our own schema sources, forever. Options 1 and 3 pay
  nothing here, and option 2 is the only one for which the prelude's tag
  vocabulary is an asset.
- **Appendix E is a documented two-serialisation story for one schema — that is
  DEC-002 option 4** — and the same appendix documents why the bijection is
  lossy. Option 4 is the only option whose schema story RFC 8610 actually
  tells, so the ADR should say why it is not taking the one the schema language
  was built for.

## Implementations

Appendix F names tool capabilities informatively; the RFC itself registers no
implementation list. Several CDDL validators exist in the wild, but **none is
installed in this environment**, so nothing in `distilled/schema/` has been run
through a real CDDL or ABNF parser — the checks performed were closure,
collision and byte-exactness, not a parse. *Searched on 2026-10-18; no parser
available locally.*

## Limits

- **This record is not the current state of CDDL.** `rfc-9165` (control
  operators), `rfc-9682`, `rfc-9741` and `draft-ietf-cbor-cddl-modules` are all
  still `status: fetched`, and `rfc-9682`'s own note says "both remain current,
  so an implementation must read them together". Nothing here may be cited as
  current CDDL until those four are read. They are library#39 Tier 2.
- **`CRLF` is redefined to admit a bare LF** (`%x0A / %x0D.0A`, against
  RFC 5234's `%x0D %x0A`), and it hides among four core rules redefined
  *identically*, so the block reads as a harmless restatement.
- **Appendix G.2 names four EDN byte-string prefixes while §3.1 and the ABNF
  admit two.** Both normative, never reconciled — and since #39 assigns EDN the
  test-vector role, a vector written `b32'…'` is valid EDN that will not parse
  as a CDDL literal.
- **§3.8.1's only pointer at "format constraints outside of CDDL" is stale**,
  citing RFC 7049 §3.9 where RFC 8949 §4.2 now lives with materially different
  content. That parenthetical is the hinge between CDDL and any determinism
  profile.
- The prelude's tag set is frozen at RFC 7049, so every tag registered since
  2013 must be redeclared per file.
- Surrogates are admitted though §3.1 mandates UTF-8; no horizontal tab exists
  anywhere in the language, which no sentence states; Table 1 disagrees with the
  grammar three times; and Appendix H's own generated instance does not satisfy
  its own schema on a strict reading.
- The extraction is at **pass 1 of 3** — verify and cross-check have not run,
  and no human has signed anything off, so these artifacts are readable but not
  buildable-on.

---
record: rfc-9943
kind: schema
title: "rfc-9943 — schemas"
extracted: "2026-09-30"
reviewed_by: "davidhsiaotw 2026-10-05 — Figure 3 compared against source lines 931-963, byte-identical;"
---

RFC 9943 contains **exactly two CDDL blocks**. Together they are the entire
formal syntax of the document — roughly 38 lines out of 1772. Everything else
in the RFC is prose, EDN examples, or deferred to another specification.

Both files are copied **verbatim** from the source, including the RFC's
three-column left margin, the internal column alignment of `COSE_Sign1`, and
the two spaces before `=>` on the `receipts` entry. No rule was added,
removed, reordered, or realigned. CDDL ignores leading whitespace, so the
retained margin does not affect parsing.

## Files

| File | Source | Lines | Rules defined |
|---|---|---|---|
| `signed-statement-receipt.cddl` | §6.1, Figure 3, "CDDL Definition for Signed Statements and Receipts" | 931–963 (caption 965) | `Signed_Statement`, `Receipt`, `COSE_Sign1`, `Protected_Header`, `CWT_Claims`, `Unprotected_Header`, `label` |
| `transparent-statement.cddl` | §7, Figure 7, "CDDL Definition for a Transparent Statement" | 1141–1145 (caption 1147) | `Transparent_Statement`, `Unprotected_Header` (redefined) |

The RFC labels both blocks **normative**: Figure 3 is "a normative CDDL
definition [RFC8610]", Figure 7 "a normative CDDL definition of Transparent
Statements".

## What the schemas cover

**CBOR tag 18 is mandatory on all three envelopes.** `Signed_Statement`,
`Receipt`, and `Transparent_Statement` are each `#6.18(COSE_Sign1)`. There is
no untagged form in this RFC. A Receipt is structurally identical to a Signed
Statement — the distinction is carried by header claims, not by shape.

**A detached payload is schema-legal and first-class.** `COSE_Sign1` declares
`payload : bstr / nil`. `nil` is not an error path and not an edge case: §6.1
prose states that "Detached payloads support large Statements and ensure
Signed Statements can integrate with existing storage systems", Figure 4
illustrates a Signed Statement with a detached payload, and Figure 8 does the
same for a Transparent Statement. An implementer who reads `payload` as
always-`bstr` will build the wrong envelope and will be unable to interoperate
with the RFC's own examples.

**Mandatory vs. optional in `Protected_Header`.** Only `&(CWT_Claims: 15)` is
required. `alg` (1), `content_type` (3), `kid` (4), `x5t` (34), and `x5chain`
(33) are all marked `?`. Note that the CDDL alone is weaker than the RFC's
prose: §6 requires `kid` to be present when neither `x5t` nor `x5chain` is,
and the CDDL does not express that dependency.

**`CWT_Claims` requires both `iss` (1) and `sub` (2)**, as `tstr`. Neither is
optional.

**Every header map in Figure 3 is open-ended.** `Protected_Header`,
`CWT_Claims`, and `Unprotected_Header` each end with `* label => any`, where
`label = int / tstr`. This is the extension socket, and it is what §6.1 means
by "The SCITT architecture specifies the minimal mandatory labels.
Implementation-specific Registration Policies may define additional mandatory
labels." Figure 7 is the exception — see the defects below.

**Figure 7's intended change is that label `394` becomes mandatory.** In
Figure 3 the receipts entry is `? &(receipts: 394) => [+ bstr .cbor Receipt]`;
in Figure 7 the `?` is gone. That single bit — the presence of at least one
Receipt in the unprotected header — is the whole *semantic* distinction
between a Signed Statement and a Transparent Statement. The array is
`[+ ...]`, so at least one Receipt is required and multiple are permitted
(Figure 8 shows two). Each element is a `.cbor`-embedded `Receipt`, i.e. a
nested tagged `#6.18(COSE_Sign1)` inside a byte string. It is **not** the only
textual difference between the two rules: Figure 7 also drops two entries
Figure 3 has. See defect 2 below, which is the accurate statement of the delta.

## What the schemas do NOT cover

- **Registration Policies.** There is no schema of any kind. §5.1.1 states
  outright: "This specification leaves implementation, encoding, and
  documentation of Registration Policies and trust anchors to the operator of
  the TS." Policies are required to be maintained, made transparent, and
  registered as Signed Statements, but their encoding is entirely unspecified
  here.
- **Any request or response.** The RFC defines no wire protocol, no endpoint,
  no message envelope for submitting a Signed Statement or retrieving a
  Receipt. Nothing of the Registration exchange is in CDDL.
- **The Verifiable Data Structure.** The VDS is named and constrained in prose
  only; its structure is defined in RFC 9942.
- **Proof structures.** Inclusion proofs and consistency proofs have no CDDL
  here. They are deferred to RFC 9942, which §7 also names as the source of
  "the COSE header parameter semantics for label 394".
- **Receipt-side labels 395 and 396.** These appear in this RFC **only in
  prose EDN examples** — 396 (Proofs) at source line 1183 in Figure 9, and 395
  (Verifiable Data Structure) at lines 1197 and 1202 in Figure 10. Neither
  label occurs in either CDDL block. Likewise the inclusion-proof tuple shown
  in Figure 11 is illustrative EDN with no CDDL counterpart anywhere in this
  document. Do not treat these figures as schema; take them from RFC 9942.
- **`COSE_CertHash` and `COSE_X509`.** Used in `Protected_Header` and
  `Unprotected_Header` but never defined, and there is no CDDL import
  directive. They come from RFC 9360, cited only in §5.1.1.1 prose.

## Defects and ambiguities in the source CDDL

Kept verbatim in the files; recorded here.

1. **Figure 7 redefines `Unprotected_Header`.** The same rule name carries a
   different definition in Figure 3 and Figure 7. RFC 8610 does not permit a
   rule to be redefined, so concatenating the two blocks into one CDDL model
   is an error. The reader must treat Figure 7 as a replacement scoped to
   Transparent Statements, which the RFC states only implicitly.

2. **Figure 7's `Unprotected_Header` is a closed map.** It drops the
   `* label => any` socket that all three Figure 3 maps have, and it also
   drops the optional `? &(x5chain: 33) => COSE_X509` entry. Read literally, a
   Transparent Statement may carry *nothing* in its unprotected header except
   label 394 — no `x5chain`, no extensions. This contradicts §6.1's statement
   that Registration Policies may define additional mandatory labels, and it
   contradicts §5.1.1.1, which explicitly allows an `x5chain` in the
   unprotected header when `x5t` is in the protected header. The narrowing is
   almost certainly unintended; the mandatory `394` is the intended change.
   So it is not accurate to say Figure 7's only difference from Figure 3 is
   that 394 becomes mandatory — two entries are lost as well.

3. **The CDDL is weaker than the prose it accompanies.** The
   `kid`-required-when-no-`x5t`-or-`x5chain` rule (§6), the requirement that
   `iss` be a URI-shaped string of 1–8192 characters when `x5t` or `x5chain`
   is present (§6), and the Receipt's "additional Claims in its protected
   header" (§6, deferred to RFC 9942) are all unexpressed in CDDL. Validating
   against these schemas alone does not establish conformance.

4. **Inconsistent spacing before `=>`.** The `receipts` entry uses two spaces
   (`&(receipts: 394)  => ...`) in both figures, where every other entry in
   the document uses one. Cosmetic, preserved as-is.

5. **`Receipt` is referentially circular by construction.**
   `Unprotected_Header` embeds `[+ bstr .cbor Receipt]`, and
   `Receipt = #6.18(COSE_Sign1)` whose own `unprotected` is an
   `Unprotected_Header`. The recursion is well-founded in practice only
   because a Receipt's own unprotected header omits label 394; the CDDL does
   not bound the nesting.

---
schema: "library-summary/v1"
id: w3c-vc-data-model-2-0
record: w3c-vc-data-model-2-0
type: summary
updated: "2026-10-23"
---

# Verifiable Credentials Data Model v2.0

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` — W3C Recommendation of 15 May 2025 (status section: published by the Verifiable Credentials Working Group "as a Recommendation using the Recommendation track"). The RFC 2026 ladder does not apply to W3C documents; this is a mapping, not a quotation. The W3C history page (checked 2026-10-23) lists this REC as the latest 2.0 entry and links a separate `vc-data-model-2.1` line, not read here. The header says "Errata exists"; the errata were not read. |
| **Authors** | Authors: Manu Sporny (Digital Bazaar), Dave Longley (Digital Bazaar), David Chadwick (Invited Expert), Ivan Herman (W3C). Editors: Manu Sporny, Ted Thibodeau Jr (OpenLink Software), Ivan Herman, Gabe Cohen (Block), Michael B. Jones (Invited Expert) |
| **Published** | 2025-05-15 (W3C Recommendation; this version `REC-vc-data-model-2.0-20250515`) |
| **Identifier** | https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/ |
| **Source** | https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/ |
| **Digest** | `a9196a3d0b6601356c4e127bad24f8c7f2c17f6ed22e41b35755a910104156f8` (re-verified 2026-10-23 against the cached fetch) |

## Overview

VC DM 2.0 defines what a verifiable credential **is** — a compacted JSON-LD
document of claims by an issuer about one or more subjects — and deliberately
**not** how it is secured. A credential becomes *verifiable* only by being
secured (§1.3; the note at the head of §3), and the securing is delegated
wholesale: §4.12 names two classes, *enveloping* proofs ("wraps a
serialization of this data model", RECOMMENDED mechanism VC-JOSE-COSE) and
*embedded* proofs ("the proof is included in the serialization of the data
model", RECOMMENDED mechanism VC Data Integrity 1.0). What DM 2.0 keeps for
itself is the envelope-independent layer: the `@context` rule (§4.3), the
required properties (§4.5, §4.7, §4.8), validity (§4.9), digests over
**linked** resources (§5.3), the contract a securing specification must meet
(§5.13), media types (§6.2), and a verifier algorithm that calls into the
securing mechanism and then checks the result is a conforming document (§7.1).
It defines no hash, signature, or canonicalization of its own.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | adjacent | Defines the verifier's obligations (§1.3, §7.1) and the integrity rule for linked resources (§5.3, Appendix B.1), but the security of the credential itself is wholly the securing mechanism's (§4.12, §5.13). |
| Cryptography | none | No algorithm, signature construction or canonicalization is specified. Its only cryptographic content is digest *formats* for related resources (§5.3) and published SHA2-256 digests of its own context and vocabulary files (Appendix B.1, B.2). |
| This project | adjacent | It is the target data model of **R-I-06** and the import side of the `ARCH-0001` §6 *W3C VC* row. It is not a candidate for anything native. |

Bears on **R-I-06** (export a subset of `AuthzCert` as a VC "using a
documented context"), **R-I-01** (the §6 *W3C VC* import row needs a mapping
table) and **R-M-07** (an imported VC binds a content digest only through the
§5.3 mechanism or a type-specific claim — Limits 5). It does not bear on
DEC-002, DEC-005 or condition (3): DM 2.0 has no encoding or envelope of its
own, so those questions belong to `w3c-vc-data-integrity-1-0` and
`w3c-vc-jose-cose`.

### Answers to the R-0006 cells, as far as the data model goes

**What a VC is.** A conforming document is compacted JSON-LD, MUST be a VC
with media type `application/vc` or a VP with `application/vp`, and MUST be
secured by at least one securing mechanism (§1.3). Required: `@context`, an
ordered set whose first item is `https://www.w3.org/ns/credentials/v2` (§4.3);
`type`, including `VerifiableCredential` (§4.5 table), where "If more than one
value is provided, the order does not matter" (§4.5); `issuer`, a URL or an
object with a URL `id` (§4.7); `credentialSubject` (§4.8). Optional: `id`
(§4.4), `name`/`description` (§4.6), `validFrom`/`validUntil` as
`dateTimeStamp` strings (§4.9 — renamed from v1.1's `issuanceDate`/
`expirationDate`, Appendix E), `credentialStatus` (§4.10), `credentialSchema`
(§4.11), `refreshService`, `termsOfUse`, `evidence` (§5.4–§5.6). The base
context is to be treated as already retrieved and its SHA2-256 is printed in
the spec (Appendix B.1). A document whose contexts do not define all its terms
must end `@context` with the `undefined-terms/v2` context (§5.2).

**What it hashes, signs, and what the proof carries.** DM 2.0 itself: none of
the three. It does not even define the `proof` property — §5.13 says "The
proof property as defined in [VC-DATA-INTEGRITY] MAY be used by the embedded
securing mechanism", and Appendix E records "Remove duplicated statements
regarding proof between Data Integrity and this specification". Example 15's
proof fields (`type`, `cryptosuite: eddsa-rdfc-2022`, `created`,
`verificationMethod`, `proofPurpose`, `proofValue`) illustrate Data Integrity;
they are not DM 2.0 normative text. What DM 2.0 **delegates**, and to whom
(§4.12, §5.13): the normative integrity algorithms; a verification algorithm
taking `inputMediaType` and `inputData` and returning `verified`,
`verifiedDocument` and `mediaType`, where the returned information is the
secured content "in isolation, without including any securing mechanism
information"; and, for a new embedded proof type, the property linking to the
proof graph, the definitions of all its terms, and coverage of all graphs
except the proof graph securing the document itself (§5.13). §5.13's closing
note names exactly two WG-standardised mechanisms — VC Data Integrity 1.0 and
VC-JOSE-COSE — and says the spec "does not mandate any particular securing
mechanism".

**Canonicalization, and when.** DM 2.0 is silent. §6 says only that "all
serialization syntaxes have to be deterministically translated to the data
model for processing, validation, or comparison" — a requirement on
translation, not a canonical byte form. Whether a verifier canonicalises
depends on the securing route: the enveloping class wraps a serialization,
the embedded class places the proof inside one (§4.12). The R-0006 condition
(3) cell is therefore owned by `w3c-vc-data-integrity-1-0` and its
cryptosuites, not by this record.

**Content binding — `relatedResource`, `digestSRI`, `digestMultibase`
(§5.3).** An issuer MAY add `relatedResource`: objects with a required unique
`id`, an optional `mediaType`, and at least one of `digestSRI` (the SRI
hash-expression grammar) or `digestMultibase` (which §5.3 attributes to "Section 2.6: Resource
Integrity" of VC Data Integrity; in the Data Integrity REC it is §2.3). Separately, any object that has an `id` MAY carry `digestSRI` or
`digestMultibase` directly. A conforming verifier that makes use of a
resource listed with a digest MUST compute the digest and produce an error on
mismatch; sha384 "SHOULD be considered the minimum strength hash algorithm"
(§5.3). The motivating case is JSON-LD contexts (§5.3 opening; §9.3 notes that
linked content is otherwise outside the securing mechanism's protection).

**Verification vs validation (§2).** *Verification* evaluates whether a VC or
VP "is an authentic and current statement of the issuer or presenter" —
conformance, securing mechanism satisfied, and the status check if present —
and "does not imply evaluation of the truth of claims". *Validation* is the
verifier's business-rule assurance; "the means for such validation vary widely
and are outside the scope of this specification". Appendix A (non-normative)
places the validity period after verification: it "is always considered a
component of validation, which is performed after verification" (A.7).

**The verifier procedure (§7.1).** Inputs: `inputMediaType` and a byte
sequence `inputData`. Steps: select a `verifyProof` function from the media
type via the VC Extensions *Securing Mechanisms* section or other mechanisms
known to the implementation; call it with the bytes or, if it expects a map,
with the parsed JSON; on `status` false add `CRYPTOGRAPHIC_SECURITY_ERROR`; on
true, check `result.document` is a conforming document, else fail with
`MALFORMED_VALUE_ERROR`. The result carries status, document, media type, the
verification method's `controller` and its controlled identifier document,
warnings and errors (ProblemDetails, §7.2). The closing paragraph of §7.1
permits the two checks in a different order provided the same invalid inputs
produce errors.

**Media types (§6.2, Appendix C).** `application/vc` and `application/vp`,
which "do not imply any particular securing mechanism". Appendix C says the
section "will be submitted" to the IESG; registration status was not checked
here. §6.2 *Media Type Precision* (non-normative) suggests inferring the
precise type from a payload labelled `application/json` by checking the first
`@context` item and a top-level `type`. Contexts linked via an HTTP Link
header are ignored (C.1).

**Enveloped vs embedded (§4.12, §4.13).** Embedded: a `proof` inside the
document (Example 15). Enveloping: the whole serialization wrapped (Example 16,
SD-JWT). Inside a VP an enveloped VC is an object of type
`EnvelopedVerifiableCredential` whose `id` is a `data:` URL carrying the
secured credential; `EnvelopedVerifiablePresentation` is the VP analogue
(§4.13). The two classes "are not mutually exclusive" (§4.12).

## Implementations

The W3C *VC v2.0 Interoperability Report*
(https://w3c.github.io/vc-data-model-2.0-test-suite/, test run dated
2026-09-27, retrieved 2026-10-23) names eleven implementations as column
headers. It gives no home pages, licences or summary pass counts — per-test
marks only — and this pass read only its first 100k characters.

| Name | Kind | License | URL |
|---|---|---|---|
| apicatalog.com | not stated | not checked | via the report |
| Digital Bazaar, Inc. | not stated | not checked | via the report |
| Gen Digital | not stated | not checked | via the report |
| Kataru Content VC | not stated | not checked | via the report |
| MakoLab | not stated | not checked | via the report |
| OpSecId | not stated | not checked | via the report |
| Procivis One Core | not stated | not checked | via the report |
| SpruceID | not stated | not checked | via the report |
| Trential | not stated | not checked | via the report |
| TrustVC | not stated | not checked | via the report |
| VC Issuer Mock | not stated | not checked | via the report |

**Licences and the open/commercial split are deliberately unfilled.** The
report tests issuer/verifier endpoints, not libraries; sorting them would mean
opening eleven vendors. Nothing here is a dependency we would take — R-I-06 is
a *Could*, and the securing-mechanism libraries are the ones worth surveying,
under the sibling records. Searched 2026-10-23.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

**No `distilled/`, and none owed by this pass.** library#87 claims the
**summary bar**: the record is `summarized`, declares no `distillation` block,
and adds nothing to `distilled/`, so FX-1 does not fire. This is a `spec`, so
it remains a candidate for FX-1 extraction; that extraction is owned by the
library#89. **What makes it worth doing** is R-I-06
moving from *Could* to scheduled: the export would then have to meet §1.3,
§4.3, §4.5, §4.7, §5.11 and §7.1 as text someone implements, and would owe
`requirements.yaml` with keyword counts and the interoperability test suite as
`examples/`.

**No `supersedes` edge.** DM 2.0 succeeds the VC Data Model v1.1
Recommendation (Appendix E, "Changes since the v1.1 Recommendation"), but the
library holds no v1.1 record, so `supersedes` is empty rather than pointing at
nothing.

**No verbatim normative text here.** Quoted fragments above are short and
locator-bearing; under FX-1 the normative text belongs in
`distilled/normative.md`.

## Limits

1. **It cannot answer the byte-level cells.** What is hashed, what is signed,
   and whether canonicalisation runs at verification are all delegated
   (§4.12, §5.13). Reading this record as if it answered R-0006 condition (3)
   would be wrong in either direction.
2. **§5.9 cautions against R-I-06's chosen subset.** It states that
   "Authorization is not an appropriate use for this specification without an
   accompanying authorization framework". Exporting `AuthzCert` as a VC is an
   authorization use the spec disclaims unless the export supplies that
   framework — which R-I-06's "documented context" would have to carry. The
   §5.1 note adds that the data model "does not imply a transitive trust
   model": "a verifier either directly trusts or does not trust an issuer".
   SPKI-style delegation chains (`ARCH-0001` §4) have no native counterpart.
3. **§5.11 binds our export, not just foreign formats.** A specification for
   transforming another format into this data model MUST say whether it is
   one-way or round-trippable, preserve `@context` values on round trip,
   produce a conforming document, and name a registered media type for its
   input. An R-I-06 export profile is such a transformation, and that list
   overlaps the R-I-01 mapping table's columns.
4. **`issuer` must be a URL (§4.7).** A `KeyId` can be exported only through a
   URL form of it, which routes R-I-06 through DEC-003; the RECOMMENDED
   dereference target is a controlled identifier document, not a bare key.
5. **R-M-07 is not met by a VC as such.** DM 2.0 defines no subject digest.
   An imported VC binds a content digest only if its type defines one or an
   `id`-bearing object carries `digestSRI`/`digestMultibase` (§5.3) — and the
   §5.3 verifier MUST applies only to resources listed in `relatedResource`,
   and only when the verifier makes use of them. The `ARCH-0001` §6 mapping *"ArtifactStatement or NameCert
   depending on type"* has to say which.
6. **"Context must be pinned" is supported but optional.** The base context is
   pinned by digest (Appendix B.1); every other context is pinned only if the
   issuer adds `relatedResource` (§5.3) or the consumer pins it itself (§6.3's
   advisory rule for type-specific processing). §4.3 says other
   specifications MAY require context integrity. The `ARCH-0001` §6 note is
   therefore something our profile must require; DM 2.0 does not.
7. **Status sits on both sides of the line.** The §2 definition of
   verification includes the status check if present, yet §7.1's algorithm
   has no status step, §4.10 calls reconciling conflicting status entries
   "part of the validation process", and Appendix A.8 describes status
   evaluation under validation. A verifier built from §7.1 alone would not
   check status. Recorded here, not as `contradicts` — it is internal to one
   document.
8. **Its hash-strength guidance is not applied to its own digests.** §5.3
   sets sha384 as the minimum to consider, while Appendix B.1 and B.2 publish
   SHA2-256 digests for the base context and vocabularies, and Example 26 uses
   SHA2-256 in `digestMultibase`.
9. **§7.1 parses before verifying when the mechanism wants a map.** The
   algorithm hands `verifyProof` the parsed JSON if it expects a map, and the
   proof check and conformance check may run in either order. Whether that
   reintroduces DSSE's parse-before-authenticate objection depends on the
   mechanism — the sibling records' question.
10. **Set semantics are left to JSON-LD.** §6.1 notes that "a JSON-LD array is
    not ordered unless that array uses the @list keyword", and `type` order
    does not matter (§4.5). DM 2.0 supplies no canonical order for set-valued
    fields; for R-0006 condition (5) it is neither help nor obstacle.

---
schema: "library-summary/v1"
id: w3c-vc-jose-cose
record: w3c-vc-jose-cose
type: summary
updated: "2026-10-23"
---

# Securing Verifiable Credentials using JOSE and COSE

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` — W3C Recommendation ("W3C Recommendation 15 May 2025"; status section: "published by the Verifiable Credentials Working Group as a Recommendation"), the W3C's terminal maturity level. The RFC 2026 ladder does not apply to W3C documents; this is a mapping, not a quotation. |
| **Authors** | Editors: Michael Jones (Self-Issued Consulting), Michael Prorock (Mesur.io), Gabe Cohen (Invited Expert). Appendix B thanks Orie Steele for "substantive intellectual and content contributions" |
| **Published** | 2025-05-15 (W3C Recommendation; this version `REC-vc-jose-cose-20250515`). An errata page exists; the one issue labelled Errata in w3c/vc-jose-cose (#345, closed) concerns leftover CR text in the status section, not technical content |
| **Identifier** | https://www.w3.org/TR/2025/REC-vc-jose-cose-20250515/ (latest: https://www.w3.org/TR/vc-jose-cose/) |
| **Source** | https://www.w3.org/TR/2025/REC-vc-jose-cose-20250515/ |
| **Digest** | `6c70cf8d7de9d8a3ff28a743fea9d569a67a402111c3245fdafbaa2ad6709af9` (retrieved 2026-10-23; re-verified against `.cache/` the same day) |

## Overview

VC-JOSE-COSE secures a VC Data Model 2.0 credential or presentation with an
**enveloping** proof: the whole JSON document becomes the payload of an
existing IETF envelope — a compact JWS (`vc+jwt`), an SD-JWT (`vc+sd-jwt`) or a
COSE_Sign1 (`vc+cose`) — and the envelope's own signature is the proof (§1.1.2).
It adds almost no cryptography of its own. Its contribution is six media types
(§6.1), the `typ`/`cty` values that name them (§3.1–§3.3), rules for how
JWT/CWT claims coexist with VC properties (§3.1.3, §3.3.3, §4.1.2),
key-discovery hints (§4), and verification algorithms that each amount to one
step: run RFC 7519 JWT validation, the SD-JWT verification algorithms, or RFC
9052's COSE_Sign1 verification, and return the decoded payload (§5.1–§5.3).
The design claim is §3's: payloads "can be made to conform directly to
[VC-DATA-MODEL-2.0] without any mappings or transformation".

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | It *is* a securing mechanism: it says what is signed, what a verifier runs, and where the key comes from. |
| Cryptography | adjacent | Defines no primitive, no to-be-signed construction and no algorithm list; everything cryptographic is delegated to RFC 7515/7519, SD-JWT and RFC 9052. |
| This project | adjacent | The mechanism an R-I-06 (*Could*) VC export would cite. Not the KSA core's envelope and not an R-I-03 target. |

Bears on **R-I-06** (export of an `AuthzCert` subset as a VC — this is one of
the two ways that VC could be secured, the other being
`w3c-vc-data-integrity-1-0`) and **DEC-003** (§4.1.2 binds a present `iss` to
the VC `issuer`; §4.2 recommends a `kid` carrying an RFC 7638 JWK Thumbprint
URI — the two wire slots any DEC-003 identifier must survive in on export).

### The R-0006 ∅ cells, answered for the enveloping route

R-0006 `unverified.md` §2 and `report.md` §2.2 leave the VC row's mechanism and
verifier cells ∅. For **this** route (not Data Integrity) the source answers:

- **What is signed.** The VC JSON itself, as an opaque payload. §3.1.1: "The
  unsecured verifiable credential is the unencoded JWS payload." §3.3.1: "The
  unsecured verifiable credential is the unencoded COSE_Sign1 payload." The
  bytes under signature are therefore RFC 7515's JWS Signing Input or RFC
  9052's `Sig_structure` — this spec adds nothing to either. For SD-JWT the VC
  is the *input* JWT Claims Set, which the issuer "converts … into an [SD-JWT]
  payload" (§3.2.1), so what is signed is the SD-JWT payload with digests in
  place of the selectively disclosable claims, not the VC as written.
- **Canonicalised, and when.** **Never.** The words *canonical* and
  *canonicalization* do not occur in the document. A verifier hands back "the
  decoded JWS payload" / "the decoded COSE_Sign1 payload" (§5.1, §5.3) — the
  verified bytes, decoded once. This is condition (3) of `report.md` §3.2 met
  the cheap way, as DSSE and COSE meet it (§2.3 there).
- **What the envelope carries.** JOSE: `alg`, `kid`, and SHOULD-level `typ`
  (`vc+jwt` / `vp+jwt` / `vc+sd-jwt` / `vp+sd-jwt`) with optional `cty` (`vc` /
  `vp`) (§3.1.1, §3.1.2, §3.2.1, §3.2.2). COSE: `alg`, `kid` (4), `typ` (16)
  SHOULD be `application/vc+cose` / `application/vp+cose`, content type (3)
  SHOULD be `application/vc` / `application/vp` (§3.3.1, §3.3.2); CWT claims
  MAY travel in a header per RFC 9597 (§3.3.3; Example 24 puts `iss` and `sub`
  in label 15 of the protected header). `iat`/`exp` are the *signature's*
  issuance and expiry, distinct from `validFrom`/`validUntil`; `nbf` is NOT
  RECOMMENDED (§3.1.3, §3.3.3). Compact JWS serialization MUST be supported;
  JSON serialization is NOT RECOMMENDED (end of §3.1.2).
- **How the verifier proceeds** (§5). Key discovery is outside the algorithm —
  it "is assumed to have succeeded prior to beginning the verification
  process", and verifiers SHOULD minimise processing of untrusted header and
  payload while doing it. §5.1: follow RFC 7519 *Validating a JWT*; on success
  return `status` true, `mediaType` vc or vp, `document` the decoded payload.
  §5.2: follow SD-JWT verification, then reverse the SD-JWT transformation to
  recover the JWT Claims Set. §5.3: RFC 9052's COSE_Sign1 process. Then §5.4
  *Validation*: "All claims expected for the typ MUST be present", understood
  claims evaluated by verifier policy, not-understood ones ignored, the
  document MUST be well-formed compact JSON-LD, `credentialSchema` and
  `credentialStatus` SHOULD be checked. Claims sets with no integrity
  protection (`alg: none`) MUST be ignored (§1.1.2.1).
- **Key discovery** (§4). Hints, not a mechanism: `kid` (§4.1.1; MUST be
  present when the issuer's or subject's key is expressed as a DID URL); `iss`
  to obtain a JWK (§4.1.2); `cnf` per RFC 7800 / RFC 8747 for a holder
  proof-of-possession key, whose use for holder binding is RECOMMENDED
  (§4.1.3). With controlled identifier documents (§4.2) the verification
  method type MUST be `JsonWebKey` with material in `publicKeyJwk`; with `iss`
  absent and a URL issuer, `kid` MUST be an absolute URL to a verification
  method; a `kid` including a JWK Thumbprint URI is RECOMMENDED. §4.2 concedes:
  "At the time of writing, there is no standard way to retrieve a public key in
  JWK format from a DID URL or controlled identifier documents."
- **JWT claims vs VC properties.** Duplication is **not** required. If `iss`
  is present it "MUST match" `issuer` (or `issuer.id`) (§4.1.2). For the other
  pairs — `jti`/`id`, `sub`/`credentialSubject.id` — §3.1.3 says only that
  implementers SHOULD avoid conflicting values, and §3.1.3 is headed "This
  section is non-normative" despite its keywords. The `vc` and `vp` claims of
  the VC 1.1 JWT encoding MUST NOT appear (§1.1.2.1, repeated in §3.1.3).
- **Enveloped proofs inside presentations.** A credential secured inside a
  presentation MUST use the VC Data Model's `EnvelopedVerifiableCredential`
  type (a nested presentation, `EnvelopedVerifiablePresentation`), and such
  credentials MUST be secured (§3.1.2, §3.2.2, §3.3.2). The envelope is a
  `data:` URL in `id` — `data:application/vc+jwt,<compact JWS>` (Example 2);
  COSE credentials so enveloped MUST be base64-encoded per RFC 2397 (§3.3.1;
  Example 23, `data:application/vp+cose;base64,…`).
- **The authenticated type indicator — condition (4).** *Present as a
  mechanism, absent as an obligation.* A compact JWS header is integrity
  protected, and RFC 9596 forbids COSE `typ` in unprotected headers, so a `typ`
  that is present is authenticated. But it is a SHOULD everywhere (§3.1.1,
  §3.1.2, §3.2.1, §3.2.2, §3.3.1, §3.3.2), none of §5.1–§5.3 checks it, and §5
  does not say from what `mediaType` is set. No example carries a registered
  value: every JWS example header decodes to `{kid, alg}` only, every hex
  COSE_Sign1 example's protected header is `{1: -35}` only, Example 24's
  diagnostic header has content type, `kid` and CWT claims but no `typ`, and the
  SD-JWT examples carry the **withdrawn** `vc+ld+json+sd-jwt` /
  `vp+ld+json+sd-jwt` (decoded by us from the example headers; Appendix A
  records the change away from `+ld+json`). A verifier conforming to this spec
  can accept a VC that carries no type indicator at all.

## Implementations

The W3C implementation report (https://w3c.github.io/vc-jose-cose-test-suite/,
run dated 2026-10-18, retrieved 2026-10-23) has three columns and 35 tests —
16 JOSE, 10 SD-JWT, 9 COSE. It records no organisation, licence or repository;
the suite's `implementations/compose.yml` supplies the container images.

| Name | Kind | License | URL |
|---|---|---|---|
| vc-jose-cose-go (Gabe Cohen, spec editor; "decentralgabe" in the report) — 35/35 | Go library | Apache-2.0 | https://github.com/thereisnogabe/vc-jose-cose-go |
| Tradeverifyd — 35/35 | container image `ghcr.io/tradeverifyd/vc-jose-cose-test-suite`; no public source found | not checked | https://w3c.github.io/vc-jose-cose-test-suite/ |
| Mavennet — 24 pass, 1 fail, 10 skipped (no SD-JWT; COSE test 35, a presentation with invalid credentials, returned success) | container image `mavennet/mavennet-vc-cli` | not checked | https://w3c.github.io/vc-jose-cose-test-suite/ |

`compose.yml` also lists Trential (`ghcr.io/trential/vc-jose-cose-cli`), which
does not appear in the published report. **The picture is thin**: one public
implementation, by an editor, last pushed 2024-12-16; the others are opaque
images, whose licences are unchecked because there is no source to read them
from. Underneath, any JOSE/COSE/SD-JWT library does the cryptography — the
spec-specific layer is small. Searched 2026-10-23.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

**No `distilled/`.** This pass (library#87) claims the **summary bar**: the
record is `summarized`, declares no `distillation` block and adds nothing to
`distilled/`, so FX-1 does not fire. FX-1 extraction is owed eventually — this
is a `spec` that R-I-06 would cite normatively — and is owned by library#89. **What would make it urgent** is R-I-06 moving from
*Could* to being built: §5's algorithms and §4's key-discovery MUSTs would then
be text we implement and test, owing `requirements.yaml` (keyword counts
across §1.1–§5.4, including those inside non-normative §3.1.3) and `examples/`
(the inputs at https://github.com/w3c/vc-jose-cose-test-suite are ready-made
fixtures).

**No verbatim normative text here.** Under FX-1 it belongs in
`distilled/normative.md` with locators; the fragments quoted above are short
and section-cited by design.

**Library gaps this record exposes.** §5.1 is entirely RFC 7519 (JWT), §5.2 is
entirely SD-JWT (cited as an undated Internet-Draft; published since as RFC
9901, November 2025), §4.2 leans on RFC 7638 (JWK Thumbprint) and Controlled
Identifiers v1.0, and §3.3.1 on RFC 2397 (`data:` URLs). None of the five has a
record. JWT and SD-JWT matter most: without them the verifier cell is answered
only to the depth of *follow the other spec*.

## Limits

1. **It does not say what a VC *means* once verified.** §3.1.3 (non-normative):
   the security it provides is "independent of the data secured and semantics
   provided by the [VC-DATA-MODEL-2.0]". Whether the signer is entitled to the
   claims is left to verifier policy (§5.4) — R-001 §11.3's
   provenance-versus-entitlement split again, with nothing in the bytes a
   verifier could reduce to *"this signer may say this"*.
2. **Condition (4) is optional, unchecked and un-exemplified** (above). For
   R-0006 this is the substantive finding: the enveloping VC route is
   DSSE-like on condition (3) and weaker than the proposed R-O-05 on condition
   (4). A mofn VC export that wants (4) must make `typ` mandatory in its own
   profile and check it before parsing; this spec will not do it for us.
3. **§1.1.2 and the COSE examples disagree on the COSE payload.** §1.1.2:
   "When using COSE, the Verifiable Credential or Presentation is encoded as a
   CBOR data structure." Every COSE_Sign1 example (hex in Examples 7–9 and
   the COSE tabs of 18–20; base64 in Example 23) carries the VC as JSON text in
   a CBOR byte string (payload bytes begin `{"@context"`; decoded by us), which matches §3.3.1's "unencoded COSE_Sign1 payload" and
   not §1.1.2. We read normative §3.3.1 plus the examples as controlling —
   `vc+cose` signs JSON bytes inside a CBOR envelope — but the text does not
   resolve it.
4. **§3.3.2 says credentials in COSE presentations are "secured using COSE in
   this case"; its own Examples 8 and 9 envelope `vc+sd-jwt` and `vp+sd-jwt`.**
   Mixed securing mechanisms inside one presentation are shown, though the
   prose implies otherwise.
5. **§5.2 is under-specified for presentations.** Its inputs list only
   `vc+sd-jwt` and it sets `mediaType` to `vc`, while §3.2.2 defines
   `vp+sd-jwt`. Key-binding JWT checking is not mentioned in §5; it is reached
   only through "the algorithms defined in SD-JWT".
6. **The claim/property consistency rule is mostly non-normative.** Only `iss`
   vs `issuer` is a MUST (§4.1.2). `sub` vs `credentialSubject.id` and `jti` vs
   `id` sit in non-normative §3.1.3 as a SHOULD — and that paragraph's own
   example reads "JWK claim iss SHOULD NOT be set", a slip for *JWT*. A JWT
   `sub` naming someone other than the credential subject is not a
   conformance failure.
7. **Strict-JSON rejection is advice, not conformance.** §7.2 says inputs not
   conforming to RFC 7159 JSON-text be "rejected in their entirety", but §7 is
   non-normative, and duplicate member names are not addressed. Condition (2)
   has nothing to bite on, since nothing is canonical; the parsing-ambiguity
   risk it guards against is not closed either.
8. **Key discovery is admitted unsolved** for DIDs and controlled identifier
   documents (§4.2). The spec defines hints, not resolution.
9. **No algorithm requirements.** No mandatory-to-implement `alg`; examples use
   ES256 and ES384. Algorithm choice and agility are inherited from the JOSE
   and COSE registries.
10. **Two references are stale drafts.** SD-JWT is cited as an undated I-D and
    CWT-claims-in-headers as `I-D.ietf-cose-cwt-claims-in-headers`; both are
    RFCs now (9901, 9597). A reader must make that mapping.

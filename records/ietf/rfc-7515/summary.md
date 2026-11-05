---
schema: "library-summary/v1"
id: rfc-7515
record: rfc-7515
type: summary
updated: "2026-11-04"
---

# JSON Web Signature (JWS)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc7515.json` 2026-11-01 |
| **Authors** | M. Jones, J. Bradley, N. Sakimura |
| **Published** | 2015-05 |
| **Identifier** | RFC 7515 · DOI 10.17487/RFC7515 |
| **Source** | https://www.rfc-editor.org/rfc/rfc7515.txt |
| **Digest** | `sha256:ecbf8467…` (full value in `record.yaml`), fetched 2026-11-01, rechecked 2026-11-04 |

## Overview

RFC 7515 protects an arbitrary octet sequence with a signature or MAC, using JSON structures for the metadata (§1). What is signed is exact and needs no canonicalisation: the ASCII of the base64url-encoded protected header, a period, and the base64url-encoded payload (§5.1). Everything outside that input is unauthenticated, including the whole `header` member of the JSON serialization (§7.2.1). A JWS may carry several signatures, and which of them must validate is left to the application, provided at least one does (§5.2). The specification therefore fixes the bytes and leaves acceptance policy, key trust and algorithm choice to the application (§5.2, §6, §10.3).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The signature carried by every signed vCon. Its parse-first order and header rules are attack surface (§5.2, §10.12) |
| Cryptography | `core` | Defines exactly what is signed, and how multiple signatures and algorithm choice work (§5.1, §5.2, §10.7) |
| This project | `adjacent` | Not an option for DEC-005, but the only outside check on vCon §5, and a worked contrast to R-O-05 |

**This RFC and `rfc-7516` are the only checks on vCon's §5 from outside the draft.** The 2026-10-15 comment on #45 said §5's objects rest on §2.2's mandatory-by-default rule and that neither of the draft's appendices covers the signed or encrypted forms. The second half does not hold for -04. Appendix B's JSON Schema is titled "vCon - Unsigned Form" and has no `signatures` member, but Appendix C's CDDL defines `signed_vcon_type`, `signature_object_type` and `signed_header_object_type`, and marks the header `uuid` optional (checked 2026-11-04 against the -04 `.txt`). That is a second rendering by the same draft, not an independent witness, so the names and locators still need this RFC. Read against it:

| vCon §5.2 says | This RFC | Result |
|---|---|---|
| `payload`, `signatures[]` of `header`, `protected`, `signature` | §7.2.1 defines all five | Names corroborated |
| Signature Object MUST contain `header`, `protected`, `signature` | §7.2.1 requires `protected` and `header` to be **absent** when empty, and at least one present | vCon is narrower: both must be non-empty. Allowed, but §5.2 never says what `protected` must hold |
| `alg` in the Header Object | §4.1.1 requires it, §7.2.1 allows either location | Allowed, but see §10.7 below |
| `x5c`, `x5u` at §4.1.6, §4.1.5 | Both sections exist with those parameters | Locators corroborated |
| x5c or x5u MUST be in the unprotected header | §6: key-identifying parameters MUST be integrity protected if used in a trust decision | **Disagreement, conditional. See below** |
| `uuid` header | Not defined here. §4.2 allows new names | Corroboration comes from vCon's own registration only |

**The disagreement.** §6 exempts these parameters from integrity protection only when the only information used in the trust decision is a key. A verifier that uses the chain for anything else, such as the signer's name, needs them protected, and vCon §5.2 mandates the opposite placement. So the draft is conforming only for a verifier that takes nothing but the key from the chain. Reported erratum 7767 (not verified) would delete the exemption altogether, which would turn this into a plain conflict. No `contradicts` edge is set: that relation is symmetric and `draft-ietf-vcon-vcon-core-04` is outside this batch. library#9's design notes already record the placement as a choice, and the §7.2.1 disjointness defect in vCon appendices A.6 and A.7.

**What it corroborates is names and locators, not meaning.** It cannot show the table is complete for vCon's purposes, since §7.2.1 tells implementations to ignore unknown extra members.

**Decisions.**

- **DEC-005** (open): the options are DSSE, COSE_Sign1 or both (`ARCH-0001` §7), so JWS is **not a candidate**. It bears as the envelope vCon chose, the one we must map from if vCon is a test of our statement form.
- **R-O-05** (proposed): the signed payload is carried verbatim, which is the half R-O-05 wants. The other half fails: §5.2 parses the protected header as JSON at step 3 and acts on it at step 5, before validating at step 8. `alg` may also sit in the unprotected header (§7.2.1), and §10.7 names carrying it in the protected header as one mitigation, not a rule. There is no required authenticated type indicator in what was read.
- **R-M-12** (accepted by `ADR-0001`, now `ARCH-0002` P1): §4.2 asks new names to be registered with IANA or collision-resistant. `crit` (§4.1.11) makes understanding opt-in by the producer, while any unlisted parameter not defined here must be ignored (§4), which is the default ARCH-0002 P5 inverts.
- **DEC-002** (accepted 2026-10-25, ADR-0004, after the #45 comment): JOSE was never an option. Kept as a closed input: §4 and §10.12 let a parser keep the last duplicate name, a tolerance the KSA-CBOR rejecting decoder forbids.

**R-M-06.** Multi-signature here is not threshold semantics, since §5.2 leaves acceptance to the application.

## Relations

- `see_also: rfc-8259`: this RFC rests on RFC 7159 (§1, §5.2 step 3, §10.12), which `rfc-8259` replaced, and §10.12 tightens that document's SHOULD on unique names. The edge is authored only here; `rfc-8259` no longer repeats it.
- `see_also: draft-ietf-vcon-vcon-core-04`: that draft's signed form is a General JWS JSON Serialization of this RFC (§5.2), checked in the table above. The draft also authors this edge, without a stated reason; it is kept here because the reason is here.
- `rfc-7516` authors the edge to this record (JWE takes its security considerations and header registry from here). `rfc-7518` and `w3c-vc-jose-cose` also author theirs, so none is repeated here.

## Implementations

**Searched 2026-11-01.** Only these two projects were checked, and only for existence and their stated scope. This was not a survey, and conformance was not tested. The `draft-ietf-vcon-vcon-core-04` record lists vCon libraries. Whether they use these was not checked.

| Name | Kind | License | URL |
|---|---|---|---|
| jose | open source, JavaScript | MIT | https://github.com/panva/jose |
| jwcrypto | open source, Python | LGPL-3.0 | https://github.com/latchset/jwcrypto |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `rfc` record owes FX-1 when someone extracts it, and no issue owns that for this record yet: the 2026-10-25 decision on #45 moved extraction to per-set issues, and neither #69 nor #89 covers it. No keyword count is given because none has been reconciled.

## Limits

- **It does not define the algorithms.** That is `rfc-7518` (JWA). `RS256`, vCon's SHOULD, is defined there.
- **It does not say whom to trust.** Key origin is the application's problem (§6, §10.3).
- **Nothing here prevents replay.** §10.10 leaves it to the application.
- **It rests on RFC 7159**, since replaced by `rfc-8259`, and on ECMAScript 5.1 for duplicate handling (§4).
- **Errata.** `errata.json` retrieved 2026-11-01 lists 1 reported and 3 rejected, none verified. Erratum 7767 on §6 was read, because it matters above. The rejected ones were not. Counts and 7767 rechecked 2026-11-04.
- **Read scope.** §1, §3 to §3.2, §4 opening, §4.1.1, the openings of §4.1.5 and §4.1.6, §4.1.11, §4.2, §4.3, §5, §6, §7.2.1, §10.1 to §10.4, §10.6, §10.7, §10.10 and §10.12, from the RFC Editor `.txt`. §2, the other §4.1 parameters, §7.1, §7.2.2, §8, §9, the other §10 subsections and Appendices A to F were not read. **vCon was checked against -04.** Revision -05 appeared on 2026-10-31 and was not compared.

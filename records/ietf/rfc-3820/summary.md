---
schema: "library-summary/v1"
id: rfc-3820
record: rfc-3820
type: summary
updated: "2026-11-03"
---

# Internet X.509 Public Key Infrastructure (PKI) Proxy Certificate Profile

|  |  |
|---|---|
| **Type** | rfc (IETF PKIX WG, from `draft-ietf-pkix-proxy-10`) |
| **Maturity** | `standard`: Category Standards Track on the title page; Proposed Standard in the RFC Editor metadata (`rfc3820.json`), checked 2026-11-03 |
| **Authors** | S. Tuecke (ANL), V. Welch (NCSA), D. Engert (ANL), L. Pearlman (USC/ISI), M. Thompson (LBNL) |
| **Published** | 2004-06 |
| **Identifier** | RFC 3820 · DOI 10.17487/RFC3820. No updates, updated_by, obsoletes or obsoleted_by |
| **Source** | https://www.rfc-editor.org/rfc/rfc3820.txt |
| **Digest** | `sha256:4a41b362…` (full value in `record.yaml`), fetched 2026-11-03 |
| **Errata** | 2 editorial, both Held for Document Update: 2954 (§5.1.2 "ECC" → "EEC") and 4039 (§7 IANA table) |

## Overview

RFC 3820 standardises the Globus GSI practice of letting an **end entity sign certificates**. It is careful to say this happens as a *Proxy Issuer*, not a CA (§1, §2.6), so the `keyCertSign` restriction is not breached. A Proxy Certificate (PC) has its own fresh key pair. Its subject is the issuer's DN with one CN appended (§3.4). It cannot be a CA or sign an end-entity certificate (§2.6, §3.7). It is marked by a critical `ProxyCertInfo` extension, which carries an optional `pCPathLenConstraint` and a mandatory `proxyPolicy` (§3.8). The policy is a `(policyLanguage OID, optional policy OCTET STRING)` pair. Two languages are reserved: `id-ppl-inheritAll`, which inherits everything, and `id-ppl-independent`, which inherits nothing. Every other language is defined by whoever uses it (§3.8.2). Path validation (§4.1) runs *after* RFC 3280 validation of the end-entity certificate. It walks the PC chain and checks signatures, name chaining, validity and path length. It returns a `proxy_policy_list` to the application, which alone can enforce the policies (§3.8.2, §4.2). The argument is that delegation can ride on unmodified TLS and on DN-based authorisation systems (§2.7), at the cost of trusting every Proxy Issuer in the chain (§6.3).

## How it answers the topic question

The `authorization-reduction` topic asks: *"How do 5-tuple reduction and tag intersection compose?"* RFC 3820 is the X.509 world's one Standards Track answer to the same problem, and it composes differently from SPKI (`rfc-2693` §6.3 as paraphrased in ARCH-0001 §3.1).

1. **Rights along a chain.** §3.8.2 gives the rule in prose. A PC's rights are *the union of* the rights granted directly to the PC's own identity, for example by an attribute certificate, and the inherited rights. The inherited rights are "the intersection of the rights granted to the PI identity intersected with the proxy policy in the PC". The rule applies recursively: condition 3(b) re-checks the Proxy Issuer's own inheritance. The worked example (Steve, files A–D) shows both halves. **This differs from SPKI reduction in one structural way.** SPKI composes a chain into one 5-tuple whose tag is the intersection of the chain's tags. RFC 3820 adds a union with rights the *intermediate* identity holds in its own name. That is possible only because each PC has a unique DN (§2.5, §3.4), so a third party can grant to it. Reduction is therefore not a pure function of the chain. It also depends on whatever the relying party knows about each intermediate identity.
2. **Tag intersection is delegated, not defined.** The policy language is opaque, and the RFC "does not define a policy language" (§3.8.2). Intersection is well defined only if the relying party understands every language in the chain (§3.8.2 condition 1). If it does not, it must deny, or ignore the whole chain (§3.8.2), or stop trusting DNs above the first unrecognised policy (§4.2). `id-ppl-anyLanguage` (§4.1.1(c), Appendix A) lets path validation postpone the language check to the authorisation layer.
3. **Two intersections the RFC does define.** Validity: every certificate must be valid at the time in question (§4(d), §4.1.3(a)(2)), so effective validity is the intersection of the windows. Key usage and EKU (§4.2, §6.2): the effective functions are the PC's own usage intersected with the issuer's effective usage, "key usage can only be decreased in PC chains". `id-ppl-independent` resets that intersection.
4. **The delegation gate is a counter, not a bit.** `pCPathLenConstraint` (§3.8.1) bounds further delegation depth. A value of 0 forbids it. **If the field is absent, depth is unlimited**, and end-entity certificates have unlimited depth too. SPKI's delegation boolean defaults the other way.
5. **Order of operations.** Name chaining (DN of issuer = subject of the previous certificate, plus a CN, §4.1.3(a)(3)–(4)) and authorisation inheritance are checked in one walk over one object kind. Path validation verifies the DN-to-key binding, and the application does the rights reduction afterwards from the returned list (§4.1.6, §4.2).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Defines restricted delegation and the relying party's MUST-checks for it (§3.8.2, §4.2, §6) |
| Cryptography | `none` | No primitive. Signature algorithms come from RFC 3280 path state (§4.1.2) |
| This project | `adjacent` | Prior art for authorisation reduction under X.509. A contrast case, not a model |

- **R-M-08** (tag intersection defined for every claimed tag profile). RFC 3820 is the counter-example: an extensible policy slot whose intersection is defined by no one. §3.8.2 and §4.2 resolve it by refusal (deny, or ignore the chain). That is the failure mode R-M-08 exists to prevent at design time.
- **R-M-10** (delegation an explicit boolean on `AuthzCert`). `pCPathLenConstraint` is explicit but optional, and absent means unlimited (§3.8.1). This is evidence for making the delegation flag mandatory and default-deny, not default-open.
- **R-M-05** (deterministic composition given an ordered cert set and ACL). §6.3 concedes that, because PC subject names are not enforced unique, two PCs "with identical names and keys, but different rights" can be substituted in path validation and change the rights of a PC further down the chain. The result depends on which PC was presented. The union with directly granted rights (point 1 above) also brings in inputs from outside the chain.
- **R-M-04** (name and authorisation bindings distinct). A PC is both at once: a derived DN, and a policy carried in the same certificate. This is the conflation R-M-04 forbids, and RFC 3820 §5.1 argues the trade-off against attribute certificates.
- **R-O-02** (short-lived validity preferred, revocation still representable). §4 states "there is no mechanism defined for revoking proxy certificates". §6.1 relies on short lifetimes plus restriction to bound a compromise. That is the R-O-02 stance, adopted by necessity.

**Relations.** `see_also`: `rfc-2693` (the SPKI reduction this section contrasts with), `rfc-5280` (the PKIX profile that obsoleted RFC 3820's base, RFC 3280, which is under `cites`), and `macaroons-2014` (caveat attenuation is intersection-only along the chain, the contrast to §3.8.2's union with rights held by the intermediate identity).

## Implementations

**Searched 2026-11-03.** We web-searched for RFC 3820 implementations and checked the OpenSSL documentation and the GitHub licence and activity data.

| Name | Kind | License | URL |
|---|---|---|---|
| OpenSSL proxy certificates | open source, library | Apache-2.0 | https://docs.openssl.org/master/man7/proxy-certificates/ |
| Grid Community Toolkit (GSI) | open source | Apache-2.0 | https://github.com/gridcf/gct |
| VOMS | open source | Apache-2.0 | https://github.com/italiangrid/voms |

OpenSSL accepts proxy certificates only when the application opts in with `X509_V_FLAG_ALLOW_PROXY_CERTS`. Its man page says "it is up to the application to interpret and combine these policies". Its example callback treats independent as "clear rights", inheritAll as "unchanged", and anything else as "parse and intersect": the §3.8.2 rule, written by the application. The Grid Community Toolkit carries on the Globus GSI that §2.2 describes, after Globus Toolkit's end of life. It still distinguishes legacy, draft and RFC 3820 proxies. We found no commercial product claiming RFC 3820. Every use the search turned up was in grid computing; we did not search beyond that.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, implementations survey, `cites` from §8 |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed.** This is an `rfc` record at the summary bar, written for the `authorization-reduction` topic. A full FX-1 extraction would cover the §3.8 and Appendix A ASN.1, the §4.1 algorithm as a protocol model, and BCP 14 keywords reconciled (note §4.2's lowercase "MUST not"). It would be owed if one is wanted, and **it needs its own issue**. None owns it yet. No keyword count is given because none has been reconciled. The `.cache/` copy is local and gitignored.

## Limits

- **The §4.1 algorithm has variable-name defects.** §4.1.2(c) initialises `working_public_key_parameters` but calls it `proxy_issuer_public_key_parameters` in the same sentence. §4.1.5(c)–(d) then assigns to `proxy_issuer_public_key_parameters` and `proxy_issuer_public_key_algorithm`, which are never initialised. Meanwhile §4.1.6 outputs the `working_*` variables, which wrap-up never updates for the final certificate's algorithm and parameters. Read literally, the output key algorithm and parameters are the last *issuer's*, not the validated PC's. The intent is plainly the PC's. §4 says implementations need only match the external behaviour, which makes the ambiguity matter. Also §4.1.3(c) has "policyPolicy" for `proxyPolicy`. None of this is in the errata.
- **Revocation contradicts itself.** §4 says there is "no mechanism defined for revoking proxy certificates". §6.2 says the end-entity certificate "could use the CRL Distribution Points extension and/or OCSP" to revoke PCs it issued. Neither the validation algorithm (§4.1) nor any input checks revocation.
- **The IANA table and the ASN.1 disagree** (§7 vs Appendix A). The table lacks `id-ppl-anyLanguage` and spells `id-ppl-inheritALL`. This is erratum 4039, held for document update.
- **Stale base.** RFC 3820 is profiled on RFC 3280, which RFC 5280 obsoleted, and was never re-based. §3.3 offers a SHA-1 hash of the PC public key as one way to assign serial numbers.
- **Delegation tracing was left out** (§5.4). A relying party cannot learn to whom each hop delegated, only the chain of DNs.
- **The AC-holder question is open** (§5.1.4). The RFC notes that a PI could reissue a PC with the same name to someone else, "effectively stealing the AC". This is the same uniqueness gap as §6.3.
- **No post-quantum or algorithm content.** Algorithms flow from RFC 3280 path state (§4.1.2). The document contributes nothing to the PQ question.
- **Read scope.** The whole RFC was read, including Appendix A. RFC 3280 and RFC 3281 were not re-read for this record.

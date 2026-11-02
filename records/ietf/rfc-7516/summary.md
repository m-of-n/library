---
schema: "library-summary/v1"
id: rfc-7516
record: rfc-7516
type: summary
updated: "2026-11-01"
---

# JSON Web Encryption (JWE)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc7516.json` 2026-11-01 |
| **Authors** | M. Jones, J. Hildebrand |
| **Published** | 2015-05 |
| **Identifier** | RFC 7516 · DOI 10.17487/RFC7516 |
| **Source** | https://www.rfc-editor.org/rfc/rfc7516.txt |
| **Digest** | `sha256:722cfcdd…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

RFC 7516 encrypts and integrity-protects an arbitrary octet sequence, with JSON structures for the metadata and the option of encrypting one content to many parties (§1). All recipients share one ciphertext, IV and tag, and differ only in a per-recipient wrapped key, so anything governing the plaintext must be the same for all (§7.2.1). Header parameters come from three places whose names must be disjoint, and only the protected header is authenticated, unless `aad` is added (§5.1 step 14, §7.2.1). JWE is therefore all-or-nothing per object: it gives each recipient the whole plaintext, and it shares its security considerations and header registry with `rfc-7515` (§11).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | vCon's confidentiality form. §11.4 and §11.5 name oracle and timing attacks |
| Cryptography | `core` | Defines the authenticated data and the per-recipient key structure (§5.1, §7.2.1) |
| This project | `adjacent` | Not an option for DEC-005 and no requirement of ours asks for it. The only check on vCon §5.3 |

**This RFC is the other half of the check on vCon's §5.** See `rfc-7515` for why nothing else corroborates that table. Read against §7.2.1:

| vCon §5.3 says | This RFC | Result |
|---|---|---|
| `unprotected`, `recipients`, `iv`, `ciphertext`, `tag` | §7.2.1 defines all five | Names corroborated |
| (no mention of `protected` or `aad`) | §7.2.1 defines both | vCon's list is incomplete, as library#9 settled (D3) |
| Recipient `header`, `encrypted_key` | §7.2.1 defines both | Corroborated |
| `enc`, `cty`, `uuid` in the Unprotected Object | Allowed. `enc` must be present (§4.1.2) | Legal, but **see below** |
| `cty` of `application/vcon+gzip` | §4.1.3 has `zip`, whose defined value is DEFLATE, and which must be in the protected header | vCon does not use `zip`. Compression is a media-type convention, in an unauthenticated location |

**The consequence for integrity.** §5.1 step 14 makes the authenticated data the encoded protected header, which is the empty string if there is none, plus `aad` if present. vCon's Unprotected Object carries `enc`, `cty` and `uuid`, and its list names neither `protected` nor `aad`. A vCon that follows that list leaves those three values outside the authentication tag. The draft's own appendix A.7 example does carry `protected`, so the list and the example differ, as library#9 recorded. Since the plaintext is a signed vCon, the content stays protected by the inner JWS. The labels do not, and §5.3.1 acknowledges this for `uuid` with only a SHOULD to verify it after decryption.

**Selective disclosure.** §7.2.1 gives all recipients one ciphertext. So the charter's aim that some parts may be disclosed to different parties (`ietf-vcon-wg`) cannot be met by one JWE over the whole vCon, which is what §5.3 specifies.

**Decisions.**

- **DEC-005** (open): JWE is not a candidate, and DEC-005 concerns signing envelopes. It bears only through vCon, and the #45 comment's link is kept on that footing.
- **DEC-002** (accepted 2026-10-25, ADR-0004): closed, and the bearing is thin. It shares the JOSE header rules set out in `rfc-7515`.
- No `R-*` in `ARCH-0001` asks for confidentiality, so this bears on none.

## Implementations

**Searched 2026-11-01.** Only these two projects were checked, and only for existence and their stated scope. This was not a survey, and conformance was not tested.

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

- **It does not define the algorithms.** `rfc-7518` does, including vCon's SHOULD values `RSA-OAEP` and `A256CBC-HS512`.
- **Key distribution is out of scope**, and vCon's charter also excludes key management (`ietf-vcon-wg`).
- **§11.4's advice has force on `alg`.** A mutable `alg` is the attack it describes, and vCon's per-recipient `alg` sits in an unprotected header. Whether the mitigation of restricting a key to one algorithm is required is left to the implementer.
- **Key commitment.** Reported erratum 7719 questions whether changing key-identifying parameters must cause failure for encryption, unless the algorithm is key-committing. It is unverified, and it was read but not assessed.
- **Errata.** `errata.json` retrieved 2026-11-01 lists 3 reported, none verified. All three notes were read at least in part.
- **Read scope.** §1, §4.1.2, §4.1.3, §5.1 steps 13 and 14, §7.2.1, §9 in part, and §11, from the RFC Editor `.txt`. §2, §3, the remaining §4 and §5, §7.1, §7.2.2, §8, §10 and the appendices were not read. **vCon was checked against -04.** Revision -05 appeared on 2026-10-31 and was not compared.

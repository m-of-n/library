---
schema: "library-summary/v1"
id: draft-ietf-lamps-pq-composite-sigs
record: draft-ietf-lamps-pq-composite-sigs
type: summary
updated: "2026-11-03"
---

# Composite ML-DSA for use in X.509 Public Key Infrastructure

|  |  |
|---|---|
| **Type** | draft (IETF LAMPS WG), revision **-19**, the revision read |
| **Maturity** | `draft`: an active Internet-Draft, intended Proposed Standard. IESG state "RFC Ed Queue", RFC Editor state "In Progress", no RFC number yet (datatracker, checked 2026-11-03) |
| **Authors** | M. Ounsworth, J. Gray (Entrust), M. Pala (OpenCA Labs), J. Klaussner (Bundesdruckerei), S. Fluhrer (Cisco) |
| **Published** | 2026-04-21 (-19) |
| **Identifier** | draft-ietf-lamps-pq-composite-sigs-19 · successor of draft-ounsworth-pq-composite-sigs-00..13 (2019–2024) |
| **Source** | https://www.ietf.org/archive/id/draft-ietf-lamps-pq-composite-sigs-19.txt |
| **Digest** | `sha256:b4ee0441…` (full value in `record.yaml`), fetched 2026-11-03 |

## Overview

The draft defines **18 composite signature algorithms** (§6; OIDs 1.3.6.1.5.5.7.6.37–.54, early-allocated 2025-10-20 per §8.1.2). Each pairs one ML-DSA parameter set with one traditional algorithm (RSASSA-PSS, RSASSA-PKCS1-v1.5, ECDSA, Ed25519 or Ed448) under a single OID, with one public key and one signature value. The argument is **protocol backwards compatibility** (§1.1, §1.3): because a composite presents itself as one atomic algorithm, X.509, CMS, PKCS#10 and CMP can carry it with no hybrid-awareness. The post-quantum migration of a PKI then becomes an algorithm substitution rather than a protocol change.

The mechanics are compact. Both components sign the same message representative `M' = Prefix || Label || len(ctx) || ctx || PH(M)` (§2.2). The per-algorithm Label is also passed as ML-DSA's context (§3.2). Verification is a strict AND: "Valid signature" if and only if all components validate (§3.3). Keys, private keys and signatures are plain concatenations with ML-DSA first (§4).

What it buys is **EUF-CMA if either component holds** and PH is collision-resistant (§9.2.1). What it gives up is SUF-CMA against quantum adversaries (§1.3, §9.2.2), and with it **application** backwards compatibility. §10.3: only upgraded systems understand these OIDs.

For the topic question this is the **X.509 hybrid path**. It is the stated post-quantum route for anything that consumes PKIX certificates. It is not a dual-certificate or "OR" migration: §9.1 says composites *operate in a strict "AND" mode*, and §10.3 says only upgraded systems will understand the OIDs.

## What it settles, by locator

- **Key reuse is forbidden in both directions.** KeyGen MUST generate fresh material for both components, and parties MUST NOT use, import or export component keys used elsewhere (§3.1, §5.3, §9.3). A deployed RSA key cannot be "upgraded" by pairing it with a new ML-DSA key.
- **Revocation by key hash breaks.** CAs often detect re-submission of a compromised key by hashing it. A composite hash will not match a revoked component, so CAs SHOULD check both component keys independently (§9.3).
- **Non-separability is weak, not strong.** The fixed Prefix leaves evidence when the traditional half is stripped. The Label-as-ctx makes the ML-DSA half fail under plain ML-DSA verification (§9.2.3). §9.4 offers a Prefix guard for traditional verifiers.
- **Deprecation becomes policy-shaped.** A composite can stay valid after its traditional component is deprecated for standalone use, so policy has to remove standalone OIDs while keeping composite ones (§9.5).
- **No mandatory-to-implement algorithm.** §10.4 RECOMMENDS `id-MLDSA65-ECDSA-P256-SHA512` as the general default and names others for RSA, bandwidth-sensitive, Level-5 and "SUF-CMA" settings.
- **Pre-hash can be externalised** (§10.5), unlike pure ML-DSA. That is the same pressure `tuf-tap-21` resolves differently.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Defines what a hybrid signature guarantees and loses (§9.2), plus key-reuse, stripping and revocation hazards (§9.3–§9.5) |
| Cryptography | `core` | A signature combiner, its domain separation (§2.2) and 18 concrete instantiations (§6) |
| This project | `adjacent` | Our native encoding is not X.509 (R-M-01), but X.509 import is in scope, and this is what post-quantum X.509 will look like |

- **R-I-05** (import X.509 only as a foreign identity assertion about a key): a composite certificate's subject key is two keys under one OID (§5.1, §6). An importer has to decide whether "the key" is the composite or either component. §3.1 and §5.3 forbid the components having any standalone life, which argues for the composite as the unit.
- **R-I-01** (publish a mapping table per foreign format): the X.509 row needs entries for the 18 composite OIDs (§6), what is preserved (the composite `pk`, a 1344–3118-byte concatenation per Appendix A), and what cannot be inferred (component keys never stand alone).
- **DEC-003** ("canonical key bytes before hashing"): §4.1 defines the composite public key as raw `mldsaPK || tradPK` with fixed component encodings (§4). Those are canonical bytes, but §9.3 shows the consequence. A digest-of-key identifier over a composite is unrelated to the digests of its components, so a `KeyId` scheme has to say which one it means.

A contrast worth recording, without a `bears_on` claim: `mofn` research R-0003 §4.5 warns that "A pair is agility hiding inside the object that was supposed to end agility". A composite is a pair, but it is a pair fixed under one OID and verified with AND semantics. That removes the negotiation R-0003 objects to and keeps the size cost.

## Implementations

**Searched 2026-11-03** (web search; GitHub issue search on bcgit/bc-java and openssl/openssl).

| Name | Kind | License | URL |
|---|---|---|---|
| Bouncy Castle (bc-java) | open source, Java; composite ML-DSA with CMS and CertPath tests | MIT-style | https://github.com/bcgit/bc-java |
| OpenSSL | open source, C; **not released**, PR #32886 open | Apache-2.0 | https://github.com/openssl/openssl/pull/32886 |

No commercial product was confirmed in this search. Which draft revision Bouncy Castle tracks was not checked, and that matters here: §8.1.2 notes the OIDs were early-allocated only on 2025-10-20, between -12 (2025-10-10) and -13 (2025-10-31).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata pinned to -19, relations, `bears_on`, implementations survey, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar for the `post-quantum-migration` topic (library#45). As a `draft` record it would owe FX-1 if extracted, and **no issue owns that extraction yet**. The sensible trigger is publication as an RFC, which would be a new record linked by `supersedes`, rather than extracting -19 while it sits in the RFC Editor queue. An extraction would cover the §7 ASN.1 module, the 18 algorithm definitions, keyword reconciliation (our raw grep finds 26 lines containing "MUST", not reconciled), the Appendix D message-representative examples and the Appendix E test vectors.

**Relations.** Each `see_also` edge is a specification the draft builds directly on: `fips-204` and `rfc-9881` (the ML-DSA component, as §2 specifies it, and `rfc-9881`'s security considerations, which §9 imports), `rfc-5280` (the certificate profile composites drop into, §5), and `fips-186-5` and `rfc-8032` (the ECDSA and EdDSA traditional components, §2 and §4.1). No `supersedes` edge: when the RFC is published, that new record carries `supersedes` pointing here.

## Limits

- **Not final.** -19 is in the RFC Editor queue. Text and even OIDs could still change in AUTH48, although §8.1.2 says the OIDs are already early-allocated. This record will be superseded, not edited, when the RFC appears.
- **It does not solve application backwards compatibility** (§10.3). A relying party that does not know the OID cannot verify at all, so the migration needs either flag days or parallel certificates. That second mechanism is out of scope here.
- **CMS is deferred** to a separate specification (§5), which is not held.
- **Internal tension on SUF-CMA.** §9.2.2 says composite "will not be SUF-CMA secure … against quantum adversaries" and that applications where SUF-CMA is critical SHOULD NOT use it. §1.3 says it is NOT RECOMMENDED unless EUF-CMA has been shown acceptable. Yet §10.4 RECOMMENDS `id-MLDSA65-Ed25519-SHA512` "In applications that require the signature primitive to provide SUF-CMA". The likely reconciliation is classical-only SUF-CMA with a deterministic Ed25519 half, but the text does not say so. Not set as `contradicts`: it is within one document.
- **Source defects.**
  - Three sites refer to a "Signature Label Values" section that does not exist (Label values are in §6).
  - §4.3's deserialisation steps are numbered 1, 3.
  - §8 names the module "id-mod-composite-mldsa-2025" while §8.1.1 describes it as "Composite-Signatures-2025 - id-mod-composite-signatures".
  - Typos include "private exponen d" and "RSASSA-PCKS1-V1_5-SIGN" (§4), "particilar" (§10.6) and "Note also that also that" (§10.2).
  - §1's sentence on EUF-CMA says "is acceptable" twice.
- **FIPS guidance is self-declared.** §10.2 says it "is not authoritative and has not been endorsed by US NIST".
- **Read scope.** §1–§10 and Appendices A–B were read. The §7 ASN.1 module and the Appendix C–E vectors were not checked. The datatracker revision history was read from `doc.json`, but the mailing-list Last Call record was not.

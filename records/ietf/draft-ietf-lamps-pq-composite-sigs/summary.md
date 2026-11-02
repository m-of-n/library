---
schema: "library-summary/v1"
id: draft-ietf-lamps-pq-composite-sigs
record: draft-ietf-lamps-pq-composite-sigs
type: summary
updated: "2026-11-01"
---

# Composite Module-Lattice-Based Digital Signature Algorithm (ML-DSA) for use in X.509 Public Key Infrastructure

|  |  |
|---|---|
| **Type** | draft (IETF LAMPS WG) |
| **Maturity** | `draft`: intended Proposed Standard, IESG state RFC Ed Queue in Datatracker, checked 2026-11-01. Not yet an RFC |
| **Authors** | M. Ounsworth, J. Gray (Entrust), M. Pala (OpenCA Labs), J. Klaussner (Bundesdruckerei), S. Fluhrer (Cisco) |
| **Published** | 2026-04-21 (-19) |
| **Identifier** | draft-ietf-lamps-pq-composite-sigs-19 |
| **Source** | https://www.ietf.org/archive/id/draft-ietf-lamps-pq-composite-sigs-19.txt |
| **Digest** | `sha256:b4ee0441…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The draft packages ML-DSA and one traditional algorithm (RSA, ECDSA, Ed25519 or Ed448) as a single signature algorithm with one public key, one signature value and one OID, so that X.509, CMS and CMP can use a hybrid without becoming hybrid-aware (§1, §1.3). It defines 18 algorithm identifiers (§6) with no mandatory-to-implement set, and §10.4 shortlists a few. The combiner signs `M' := Prefix || Label || len(ctx) || ctx || PH(M)` with both components (§2.2), so a per-algorithm label and a static prefix leave evidence if a component is stripped. The ML-DSA component stays "pure", so no HashML-DSA implementation is needed (§2.1).

The security claim is deliberately limited. A composite is EUF-CMA secure if one component is, and PH is collision resistant (§9.2.1). None of the combinations is SUF-CMA secure against a quantum adversary (§1.3, §9.2.2), so §1.3 calls replacing ML-DSA with a composite a reduction in security. The operation is a strict AND (§9.1): it gives codebase migration flexibility, not application backwards compatibility (§10.3).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Sets out what a hybrid signature does and does not guarantee, including stripping and key reuse (§9.2 to §9.3) |
| Cryptography | `core` | Defines a signature combiner and 18 concrete instantiations |
| This project | `adjacent` | NG3 defers the suite, and the draft is scoped to X.509/PKIX. Three things below still touch open questions |

- **DEC-003**: a key-digest identifier must specify canonical key bytes. Composite keys are serialized by §4, and §9.3 warns that a CA hashing only the combined key misses a revoked component. A digest of the composite does not identify its components.
- **R-M-02**: identification solely by key gets costly at these sizes. Appendix A puts ML-DSA-87 composites at about 2.6 to 3.1 KB of public key and 4.7 to 5.1 KB of signature.
- **R-I-05**: an imported X.509 identity may carry a composite key. An import must not assume that the same RSA or ECC key also appears alone, because §9.3 forbids that reuse.

**Disagreement on the record, not a `contradicts` edge.** `cnsa-2-0` says NSS should not put multiple algorithms in one certificate and should stand up a parallel PKI instead (FAQ pp. 29 to 30). This draft motivates itself with jurisdictions that want ML-DSA only inside a hybrid (§1). `nistir-8547` §3.2.2 sits between them. These are different scopes and policies rather than incompatible assertions, so the edge is `see_also`.

## Implementations

**Searched 2026-11-01.** Web search and a GitHub code search of bc-java.

| Name | Kind | License | URL |
|---|---|---|---|
| Bouncy Castle (`compositesignatures` provider) | open source, library | MIT-style | https://github.com/bcgit/bc-java |
| oqs-provider | open source, OpenSSL provider | not checked | https://src.opensuse.org/c_cpp/oqs-provider/raw/branch/main/oqs-provider.changes |

Revision tracking was not checked for Bouncy Castle. The oqs-provider packaging notes show an early draft revision. Appendix E carries test vectors, which we did not run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `draft` record owes FX-1 when someone extracts it, and no issue owns that yet. The natural trigger is RFC publication, which would be a new record linked by `supersedes`. No keyword count is given because none has been reconciled.

## Limits

- **Not an RFC.** The text may still change in the RFC Editor queue, and the OIDs in §6 are as of -19.
- **§10.2's FIPS guidance is unendorsed.** The draft says so itself: it is not authoritative and has not been endorsed by NIST.
- **It does not settle hybrid versus pure.** §9.1 concedes that the case for dual-algorithm security rests on policy outside the primitives.
- **X.509 only.** It says nothing about a non-PKIX signed format like ours beyond the general warning in §9.2.
- **Read scope.** §1 to §2.2, §6 (identifiers, skimmed), §9 and §10.2 to §10.4 were read, plus the sizes in Appendix A. §3 to §5, §7, §8 and the test vectors were not read line by line.

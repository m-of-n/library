---
schema: "library-summary/v1"
id: rfc-4122
record: rfc-4122
type: summary
updated: "2026-11-04"
---

# A Universally Unique IDentifier (UUID) URN Namespace

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc4122.json` 2026-11-01. **Obsoleted by RFC 9562** (May 2024), not held here |
| **Authors** | P. Leach, M. Mealling, R. Salz |
| **Published** | 2005-07 |
| **Identifier** | RFC 4122 · DOI 10.17487/RFC4122 |
| **Source** | https://www.rfc-editor.org/rfc/rfc4122.txt |
| **Digest** | `sha256:3825a334…` (full value in `record.yaml`), fetched 2026-11-01, rechecked 2026-11-04 |

## Overview

RFC 4122 defines a URN namespace for 128-bit identifiers that need no central registration process (§1); because no centralized authority is required to administer them, generation on demand can be completely automated (§2). It specifies five versions by how the bits are obtained: time-based, DCE security, MD5 name-based, random, and SHA-1 name-based (§4.1.3). Name-based versions give the same UUID for the same name in the same namespace, with the namespace itself identified by a UUID (§4.3). Its security section is blunt: a UUID cannot be assumed hard to guess, should not be used as a capability, and cannot be checked by eye for transposition (§6).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §6: UUIDs are not capabilities and cannot be integrity-checked by eye |
| Cryptography | `adjacent` | v3 and v5 use MD5 and SHA-1 as name-to-id functions, not as digests we could bind |
| This project | `adjacent` | R-M-11: a UUID is a label, and does not meet the digest rule |

**This RFC is obsolete, and `draft-ietf-vcon-vcon-core-04` does not cite it.** That draft's `[UUID]` is `draft-peabody-dispatch-new-uuid-format-04`, dated 23 June 2022, an individual draft by two of RFC 9562's authors. Its §4.1.2 says the `uuid` SHOULD be a version 8 UUID generated like a version 7 one, and neither version exists in this RFC, whose §4.1.3 stops at 5. It is filed in this topic all the same, and its value is limited to what follows.

- **R-M-11** (proposed, `ARCH-0001-PROPOSAL-v0.2.0` §7): an ArtifactId must bind at least one content digest. A random or time-based UUID has no relation to content, and a name-based one hashes a name, not the artifact, using an MD5 or SHA-1 output cut to UUID size (§4.3). So mapping vCon's `uuid` to an ArtifactId would supply a label and not satisfy R-M-11, whichever version is used.

## Relations

No `see_also` is authored. The draft that might link here cites a different document, as above, and RFC 9562, the successor, is not held.

## Implementations

**Searched 2026-11-01.** Only the one project below was checked. This was not a survey.

| Name | Kind | License | URL |
|---|---|---|---|
| google/uuid | open source, Go | BSD-3-Clause | https://github.com/google/uuid |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `rfc` record owes FX-1 when someone extracts it, and no issue owns that for this record yet: the 2026-10-25 decision on #45 moved extraction to per-set issues, and neither #69 nor #89 covers it. No keyword count is given because none has been reconciled.

## Limits

- **Read RFC 9562 for anything current.** It was not read. Its metadata (title, date, obsoletes, authors) was checked, nothing more. It should be ingested. That is out of scope for this batch.
- **Distributed generation rests on the random source.** §6 says applications generating UUIDs at many hosts must be willing to rely on the random number source at all of them, and should use the namespace variant if that is not feasible. Nothing lets a verifier check either.
- **Layout text has known defects.** `errata.json` retrieved 2026-11-01 lists 8 verified, 4 held and 1 rejected (recounted 2026-11-04), several on §4.1 and §4.3. The status, section and note of each were scanned, the replacement text was not reviewed.
- **Read scope.** §1, the start of §2, §4.1.3, §4.3 and §6, from the RFC Editor `.txt`. The rest of §2, §3, the remainder of §4, and Appendices A to C were not read.

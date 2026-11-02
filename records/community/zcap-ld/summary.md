---
schema: "library-summary/v1"
id: zcap-ld
record: zcap-ld
type: summary
updated: "2026-11-01"
---

# Authorization Capabilities v0.4.0

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `draft`: W3C CCG work item, not standards track |
| **Authors** | C. Lemmer-Webber, M. Sporny, M. S. Miller; editors C. Lemmer-Webber, D. Zagidulin, M. Sporny, B. Goering |
| **Published** | 2026-10-20 |
| **Identifier** | no number; version 0.4.0 |
| **Source** | https://w3c-ccg.github.io/zcap-spec/v0.4.0/ |
| **Digest** | `sha256:1721f406…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

ZCAP encodes object capabilities as chains of linked-data documents. Authority starts at a root zcap for an invocation target, and each delegated zcap names its parent, a controller key and an expiry, and is signed by a controller of the parent (§Root Capability, §Delegated Capability). Narrowing is **containment at each hop**: the §Delegated Capability rules make the verifier check that a child's expiry and `allowedAction` are not less restrictive than its parent's, and that its `invocationTarget` matches or extends its parent's by a path or query suffix. So attenuation is defined by URL structure and a few fields, not a tag language. The spec also argues a separation: credentials for reasoning about who should receive authority, and capabilities for exercising it (§Relationship to Verifiable Credentials).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Capability chain with explicit verifier obligations |
| Cryptography | `adjacent` | Delegates signing to Data Integrity proofs; `eddsa-jcs-2022` in examples |
| This project | `adjacent` | Studied, not adopted; useful as the containment end of the design space |

- **DEC-004, R-M-08**: containment over fields replaces a tag language. A URL suffix rule needs no intersection operator, but it can express only what a URL hierarchy can.
- **R-M-09**: a child's expiry cannot exceed its parent's, and §Delegated Capability notes that a root zcap has no expiry.
- **R-M-10**: there is no delegation flag. A controller may both invoke and delegate.
- **R-O-02**: expiry is mandatory on delegated zcaps, with a SHOULD for at most three months, because a verifier must store revoked zcaps until they expire.

## Implementations

**Checked 2026-11-01.** The spec's backlog links Digital Bazaar's `zcapld` and `ezcap-express`. `zcapld` resolves to `digitalbazaar/zcap`, and both were confirmed through the GitHub API. No wider survey was done.

| Name | Kind | License | URL |
|---|---|---|---|
| zcap | open source, JavaScript | BSD-3-Clause | https://github.com/digitalbazaar/zcap |
| ezcap-express | open source, Express middleware | BSD-3-Clause | https://github.com/digitalbazaar/ezcap-express |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **"v0.4.0" names two different texts.** Git tag `v0.4.0` (`109ab03`, 2026-10-07) keeps a MUST limit on chain length with a SHOULD limit of 10. The page served at `/v0.4.0/` was replaced on 2026-10-20 and carries a later commit, `75255e8`, that leaves only a SHOULD to limit the length. The spec's change log says all changes in the release are non-normative, which holds for the tag but not for the page. Cite the digest, not the version. This record tracks the served page.
- **The caveat text and the attenuation text disagree.** §Caveats still defines a `caveat` property, while §URL Path- or Query-based Attenuation says vocab-based caveats have been removed, and the examples use `caveat`. Which is normative is unclear.
- **Algorithms are unspecified.** The backlog lists delegation-proof and invocation-proof algorithms, and revocation behaviour, as future work.
- **Confused-deputy claims are qualified.** §Capabilities Are Safer says less vulnerable, not immune.
- **Editorial damage.** §Delegated Capability has a paragraph that opens with "A root zcap MUST have an" and then sets rules for delegated zcaps, and attenuation is described as a "greater limit" on actions.
- **Read scope.** The v0.4.0 source text was read whole, excluding the included change log, of which the first part was read from the repository. rc.6 was compared by diff, not read separately. No implementation was run.

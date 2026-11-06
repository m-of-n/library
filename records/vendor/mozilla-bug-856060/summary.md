---
schema: "library-summary/v1"
id: mozilla-bug-856060
record: mozilla-bug-856060
type: summary
updated: "2026-11-04"
---

# Name Constraints ignored by libPKIX verification engine (in both intermediate and toplevel CA certificates)

|  |  |
|---|---|
| **Type** | web (bug report) |
| **Maturity** | unset: a bug thread; no body assigns it a standing |
| **Authors** | Kai Engert, Ryan Sleevi |
| **Published** | 2013-03-29 |
| **Identifier** | Bugzilla 856060 |
| **Source** | https://bugzilla.mozilla.org/show_bug.cgi?id=856060 (via REST) |
| **Digest** | `sha256:55534885…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Kai Engert found that NSS's libPKIX engine accepted a certificate outside a permitted `.de`/`.com` constraint. Ryan Sleevi's analysis was that libPKIX's build path, which NSS uses, never applied the name-constraints checker that the unused validate path had. He then found that the bug only triggers without a `subjectAltName`, since SAN names were already constrained and only the CN path was missed. The fix landed on 2013-06-12, with tests, and the bug was rated sec-low at most.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | real, narrow |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | a test-coverage lesson for R-M-08 |

- **R-M-08**: the check existed in one code path and not the other, and NSS's tests did not catch it, though comment 9 says PKITS covers name constraints. A tag profile needs vectors at the level of the code path a deployment uses.

## Relations

- `see_also: go-nameconstraint-cves`: the same failure in another widely used verifier, a name constraint the chain carries but the checker does not apply (here a permitted subtree via the CN path; there excluded subtrees against wildcard SANs).
- `see_also: rfc-5280`: comment 17 says the behaviour at issue is "something not found in any RFC": the missed case is the CN without a SAN, which RFC 5280's name-constraint rules (§4.2.1.10) do not cover for DNS names.
- The earlier `see_also` to `openssl-2022-email-overflow` was removed on 2026-11-04: no reason was stated, and that is a memory-safety bug, not a missed constraint. `go-nameconstraint-cves` and `rfc-9549` carry their own edges to it.

## Implementations

NSS. Fixed in 3.15.1.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** all 22 comments and the bug metadata. The patches were not read.

- **R-001 §4.5 overstates this.** It says NSS "shipped a period in which libPKIX silently did not enforce constraints at all". Per comments 13 and 17 the case fell only where no SAN was present; comment 17 says the normal case was and is checked, and comment 18 rates it sec-low at most. Firefox's default classic engine enforced intermediates (comment 5).
- The title says top-level CA too; comment 2 treats root constraints as separately expected behaviour. The two were not untangled.

---
schema: "library-summary/v1"
id: rfc-6749
record: rfc-6749
type: summary
updated: "2026-11-05"
---

# The OAuth 2.0 Authorization Framework

|  |  |
|---|---|
| **Type** | rfc (IETF stream) |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc6749.json` 2026-11-01 |
| **Authors** | D. Hardt, Ed. |
| **Published** | 2012-10 |
| **Identifier** | RFC 6749 · DOI 10.17487/RFC6749 |
| **Source** | https://www.rfc-editor.org/rfc/rfc6749.txt |
| **Digest** | `sha256:f204fc86…` (full value in `record.yaml`), fetched 2026-11-01, re-verified 2026-11-05 |

## Overview

OAuth 2.0 lets a client obtain limited access to an HTTP service, either for a resource owner or for itself, by way of an authorization server that issues access tokens (Abstract, §1.1). A token is a string representing an authorization, usually opaque to the client, and representing specific scopes and durations (§1.4). Scope is a list of space-delimited strings defined by the authorization server, and the server may ignore part of what was asked for (§3.3). So narrowing exists, but only at issuance and only at the server. §1.4 notes that tokens can be more restrictive than the grant that produced them, and §10.3 says the client should ask for minimal scope. Nothing lets a holder narrow a token and pass it on.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The deployed authorization framework |
| Cryptography | `none` | Defines no token cryptography; §1.4 leaves format to companion specifications |
| This project | `adjacent` | Baseline and foil for the delegation drafts |

- **DEC-004**: scope strings are the baseline tag language: server-defined, with no structure.
- **R-M-08**: §3.3 defines no semantics for comparing or intersecting scopes beyond what the server chooses to grant. This is the gap R-M-08 exists to close, and `rfc-9396` §6.1 says the same of its richer form.

## Implementations

**Checked 2026-11-01.** These two repositories were confirmed through the GitHub API, and each README names this RFC. No wider survey was done, and OAuth implementations are numerous.

| Name | Kind | License | URL |
|---|---|---|---|
| Authlib | open source, Python; README lists RFC 6749 | BSD-3-Clause | https://github.com/authlib/authlib |
| Ory Hydra | open source, Go; README lists RFC 6749 | Apache-2.0 | https://github.com/ory/hydra |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **It is a framework.** §1.4 leaves token format and the methods of use to companion specifications. It does not say how a resource server learns what a token permits.
- **No sender constraint.** §10.3 says it gives the resource server no way to confirm that a presented token was issued to the presenting client. `rfc-9449` and `rfc-7800` respond to this.
- **Superseded in practice on security.** RFC 9700 updates it. We do not hold RFC 9700, so §1.3.3 and the wider §10 should not be taken as current advice.
- **Errata: 31 entries, none verified as technical** (checked 2026-11-05). 5 verified, all editorial; 23 reported and 2 held for document update, not assessed here; 1 rejected, 3880 on §10.16.
- **Relations.** This RFC cites `rfc-6750` (`cites`), and `rfc-9396` cites this RFC, so neither needs a `see_also` edge. RFC 9700, which updates this RFC, is recorded in `content.note` and not as a citation, since this document cannot cite it.
- **Read scope.** Abstract, §1.1, §1.3.3, §1.4, §3.3 and §10.3 were read, and the §10 headings were listed. Grant flows, endpoints and the rest of §10 were not read, which includes §10.16, which `macaroons-2014` relies on.

---
schema: "library-summary/v1"
id: pypi-trusted-publishers
record: pypi-trusted-publishers
type: summary
updated: "2026-11-01"
---

# Publishing to PyPI with a Trusted Publisher

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | informational |
| **Authors** | PyPI maintainers |
| **Published** | 2026, Python Package Index (PyPI) documentation |
| **Identifier** | https://docs.pypi.org/trusted-publishers/ |
| **Source** | https://docs.pypi.org/trusted-publishers/ |
| **Digest** | `sha256:3bb9ea16…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Trusted Publishing replaces long-lived PyPI API tokens. A project registers an OIDC configuration, such as GitHub repository, workflow and environment. CI presents an OIDC token, PyPI verifies it and matches its claims against registered publishers, and PyPI mints an API token that expires in 15 minutes. The security page is careful about what this is: it does not assert the safety of the code or the trustworthiness of its authors, and it concedes that weakness in a trusted workflow can be equivalent to credential compromise.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Removes a stored secret, and moves the trust boundary to the CI identity provider |
| Cryptography | `adjacent` | OIDC JWTs exchanged for macaroon-based API tokens (*Internals*) |
| This project | `adjacent` | This is who may publish, decided at a registry, and it is invisible downstream |

- **R-O-02**: a clean case of short-lived credentials over stored ones. `slsa-2026-mini-shai-hulud` shows the limit: a short-lived token stolen from memory is still usable.
- **Topic**: this is an entitlement decision that exists only inside PyPI. A consumer cannot see or verify it.

## Implementations

**Searched 2026-11-01.** GitHub repository metadata checked.

| Name | Kind | License | URL |
|---|---|---|---|
| warehouse | open source, PyPI server | Apache-2.0 | https://github.com/pypi/warehouse |
| gh-action-pypi-publish | open source, publishing action | BSD-3-Clause | https://github.com/pypa/gh-action-pypi-publish |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A web source has no FX-1 obligation, and nothing here needed a further artifact.

## Limits

- **Authentication, not integrity.** *General considerations* says Trusted Publishing does not address modification before or after a build, and defers to attestations.
- **Scope can be wider than it looks.** *Internals* says a minted token covers every project with a matching publisher.
- **Publishers outlive people.** The page warns that removing a user does not remove publishers that user registered.
- **Read scope.** The index, security model and internals pages were read, the last up to the many-to-many Q&A. The quickstart and provider configuration pages were not read.

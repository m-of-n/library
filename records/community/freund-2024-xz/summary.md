---
schema: "library-summary/v1"
id: freund-2024-xz
record: freund-2024-xz
type: summary
updated: "2026-11-01"
---

# backdoor in upstream xz/liblzma leading to ssh server compromise

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | unofficial |
| **Authors** | Andres Freund |
| **Published** | 2024-03-29, oss-security mailing list (Openwall) |
| **Identifier** | `20240329155126.kjjfduxw2yrlxgzm@awork3.anarazel.de` |
| **Source** | https://www.openwall.com/lists/oss-security/2024/03/29/4 |
| **Digest** | `sha256:1a117fd0…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The disclosure itself, sent by a developer who noticed slow SSH logins and valgrind errors on Debian sid. One part of the backdoor existed *solely in the distributed tarballs*: a modified `build-to-host.m4` absent from the git tree. The rest sat in the repository as binary test files. A build-time script injected code into liblzma only under narrow conditions: x86-64 Linux, gcc with the GNU linker, and a Debian or RPM package build. At runtime it redirected `RSA_public_decrypt` in sshd through an audit hook. Freund concludes the committer was either directly involved or badly compromised, and thinks the former likelier.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A pre-authentication backdoor in sshd by way of a compression library, with the mechanism traced |
| Cryptography | `adjacent` | It hooks RSA verification. The cryptography is the target, not the method |
| This project | `adjacent` | The bytes shipped were not the bytes in the repository. `tukaani-xz-backdoor` says those tarballs were signed by the release account |

- **R-M-07**: binding a digest binds the tarball, not the repository it claims to come from. The tarball half of the attack lived in that gap. R-M-07 is necessary and not sufficient.
- The conditional trigger also matters: the script injected only in Debian or RPM package builds, so another build of the same tarball would not have shown the change. Bears on no `DEC-*`.

## Implementations

None applicable: this source describes an incident, not something to build on. No search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A web source has no FX-1 obligation, and nothing here needed a further artifact.

## Limits

- **The author says the analysis is partial.** The message states they are not a security researcher or reverse engineer, and that most of it comes from observation.
- **Early claims have aged.** The message guesses at the payload. `cox-2024-xz-timeline` gives the later understanding: unauthenticated, targeted remote code execution.
- **Read scope.** The whole message was read through Openwall's rendering, except that long shell lines were truncated on screen. The attachments were not fetched or read.

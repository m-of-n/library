---
schema: "library-summary/v1"
id: event-stream-issue-116
record: event-stream-issue-116
type: summary
updated: "2026-11-01"
---

# I don't know what to say.

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | unofficial |
| **Authors** | FallingSnow (issue author), dominictarr (maintainer replies) |
| **Published** | 2018-11-20, GitHub (dominictarr/event-stream issue tracker) |
| **Identifier** | https://github.com/dominictarr/event-stream/issues/116 |
| **Source** | https://api.github.com/repos/dominictarr/event-stream/issues/116 |
| **Digest** | `sha256:1c2c79d3…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The thread where the event-stream compromise surfaced. A user asks why a new account was given the repository, after it added `flatmap-stream`, a dependency whose minified source contained an injection absent from its unminified source. The maintainer replies that the requester emailed asking to maintain the module and was given it, because the maintainer no longer used it and gained nothing from it. The thread then argues over responsibility, with others tracing what the payload did. Its value is that the entire authorisation event fits in one sentence.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Real-world maintainer transfer as an attack vector |
| Cryptography | `none` | Mentions an encrypted payload only |
| This project | `adjacent` | Publish authority moved by email, with nothing for a consumer to see or check |

- **R-M-10**: the clearest example of delegation with no delegation object. The maintainer no longer held publish rights, and the transfer was invisible to every downstream consumer.
- Bears on no `DEC-*`. It is evidence for the topic question, not an input to a design.

## Implementations

None applicable: this source describes an incident, not something to build on. No search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A web source has no FX-1 obligation, and nothing here needed a further artifact.

## Limits

- **Most of the thread was not read.** Only the issue body and the first 30 of 666 comments were retrieved.
- **Early understanding was wrong or partial.** The issue body's analysis was revised by its 26 November edit. `npm-event-stream` is the settled account.
- **The issue carries embedded obfuscated payload data.** It was read as text only, and no part of it was decoded or run. Do not copy it.
- **Read scope.** Issue body and comments 1 to 30, through the GitHub API.

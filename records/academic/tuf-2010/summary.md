---
schema: "library-summary/v1"
id: tuf-2010
record: tuf-2010
type: summary
updated: "2026-11-01"
---

# Survivable key compromise in software update systems

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | white-paper (peer-reviewed; the library has no closer value) |
| **Authors** | Justin Samuel, Nick Mathewson, Justin Cappos, Roger Dingledine |
| **Published** | 2010-10-04, ACM |
| **Identifier** | `10.1145/1866307.1866315` |
| **Source** | https://theupdateframework.io/papers/survivable-key-compromise-ccs2010.pdf |
| **Digest** | `sha256:1b3774a2…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The paper's premise is that software update systems treat a single key compromise as fatal, and that this is a design choice. It identifies three kinds of information an updater must authenticate: the content of updates, their availability, and the consistency of what describes them. It then derives design principles from key compromise: responsibility separation, multi-signature trust, explicit and implicit revocation, and minimising per-key risk (§6). TUF applies them with root, targets, release and timestamp roles, keeping the most valuable keys offline (§7).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Survivability under partial key compromise is the paper's whole subject (§2, §6) |
| Cryptography | `adjacent` | (t, n) threshold trust, realised as multiple signatures. Metadata uses canonical JSON (§7.2) |
| This project | `core` | Our threshold and revocation requirements restate its principles |

- **R-M-06**: multi-signature trust as a property of a role, with no CA hierarchy. The paper warns against third-party CA PKI in update systems.
- **R-O-02**: §6.3's split between implicit revocation (expiry) and explicit revocation is the distinction R-O-02 assumes.
- **R-O-03**: §7.2 cites canonical JSON, and footnote 2 says the format itself is unimportant so long as data has a canonical form.
- §6.2 distinguishes threshold signatures within a role from responsibility shared between roles. These are different things, and `R-M-06` names only the first.

## Implementations

**Searched 2026-11-01.** The paper's design lives on in `tuf-spec`, where implementations are listed.

| Name | Kind | License | URL |
|---|---|---|---|
| python-tuf | open source, Python | Apache-2.0 | https://github.com/theupdateframework/python-tuf |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A paper has no FX-1 obligation, and nothing here needed a further artifact.

## Limits

- **A superseded format.** Roles and files here (`release.txt`, `root.txt`) are not current TUF. `tuf-spec` governs, and its snapshot role does the job release does here.
- **The word "threshold signature".** The paper uses it for t of n independent signatures, not a threshold cryptosystem. Do not read it as FROST-style signing.
- **Risk cannot be quantified.** §6.4 says so plainly, which leaves key threshold choices as judgement.
- **Read scope.** Abstract, §1, §2 opening, §6, §7.1 to the timestamp role in §7.3, and §10 were read through text extraction. §3 to §5 (the survey of update systems), the compromise analysis in §7.4 onward, §8 (recommendations) and §9 were not read closely, so no recommended threshold or expiry is given.

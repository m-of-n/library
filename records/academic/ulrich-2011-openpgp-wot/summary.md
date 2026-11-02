---
schema: "library-summary/v1"
id: ulrich-2011-openpgp-wot
record: ulrich-2011-openpgp-wot
type: summary
updated: "2026-11-01"
---

# Investigating the OpenPGP Web of Trust

|  |  |
|---|---|
| **Type** | paper (peer-reviewed conference) |
| **Maturity** | `white-paper`, the nearest enum value for a conference paper |
| **Authors** | Alexander Ulrich, Ralph Holz, Peter Hauck, Georg Carle |
| **Published** | September 2011, ESORICS 2011 |
| **Identifier** | DOI 10.1007/978-3-642-23822-2_27 |
| **Source** | https://www.net.in.tum.de/fileadmin/bibtex/publications/papers/Investigating_the_OpenPGP_Web_of_Trust_Ulrich_Holz_ESORICS_2011.pdf |
| **Digest** | `sha256:a345fbc8…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

A graph analysis of a December 2009 keyserver snapshot. Of about 2.7 million keys, the real web of trust was 325,410 keys and 816,785 valid signatures, split into 240,283 strongly connected components (§3.1, §4.1). Only the largest component, about 45,000 keys, can use the web of trust properly (§8). Inside it the picture is good: short chains, a small-world effect, and about 40,000 of the 45,000 reachable within GnuPG's five-hop limit. It is also robust to key removal. The conclusion is that the web of trust works within smaller neighbourhoods for active signers, and does not reach most users.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Measures the actual reach of decentralised certification |
| Cryptography | `adjacent` | Reports algorithms in use (§6); MD5 and 1024-bit advice |
| This project | `adjacent` | Bounds what importing OpenPGP certifications can buy |

`R-I-04`: imported OpenPGP identity signatures become `NameCert` or `Endorse`. This paper shows how sparse that graph is, so an import gives little without a local policy. It is also evidence for mofn R-001 §5.2.

## Implementations

None applicable: a measurement. Its tooling (a modified SKS) is described, not released in the text read. Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this file |

No `distilled/`: a summary-bar fill, and a `paper` record is outside FX-1 scope.

## Limits

Read: abstract, §§1-3, §4.1 and the start of §4.2, §7 in part, and §8, from the author-hosted PDF. §4.3 (robustness), §5 (communities) and §6 (algorithms) are known here only through §8's summary. The figures and the appendix definitions were not read.

The snapshot is 2009, before the 2019 keyserver collapse (`cve-2019-13050`). Published keys only: the authors say they cannot count unpublished keys. "Usefulness" is an upper bound, because introducer trust is not stored in signatures (§4.2). It measures keys, not people.

---
schema: "library-summary/v1"
id: vu-2020-typosquatting
record: vu-2020-typosquatting
type: summary
updated: "2026-11-01"
---

# Typosquatting and Combosquatting Attacks on the Python Ecosystem

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | white-paper (peer-reviewed; the library has no closer value) |
| **Authors** | Duc-Ly Vu, Ivan Pashchenko, Fabio Massacci, Henrik Plate, Antonino Sabetta |
| **Published** | 2020-09, IEEE |
| **Identifier** | `10.1109/EuroSPW51379.2020.00074` |
| **Source** | https://conferences.computer.org/eurosp/pdfs/EuroSPW2020-7k9FlVRX4z43j4uE2SeXU0/859700a508/859700a508.pdf |
| **Digest** | `sha256:bf91c7e9…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

PyPI's limited automated controls let attackers publish packages with names close to popular ones, either by edit (typosquatting) or by rearranging hyphen-separated elements (combosquatting). The paper tabulates 36 known malicious packages, then proposes a filter: a package is suspect if its name is within Levenshtein distance 2 of a standard library module or of a package whose name matches its GitHub repository. Run over 216,548 packages, this treats 79,933 as safe and leaves 67,005 for further checks. It is a filter for human review, not a detector of malice.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Describes a real attack class on one registry. The defence is a coarse heuristic |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Same argument as `ohm-2020-backstabbers`, with weaker evidence |

- **R-M-03**: more evidence that registry-global names invite impersonation. It adds nothing beyond `ohm-2020-backstabbers`, so the usefulness verdict is `marginal`.

## Implementations

None applicable: this source describes a study, not something to build on. No search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A paper has no FX-1 obligation, and nothing here needed a further artifact.

## Limits

- **Internally inconsistent counts.** The method section says distance 2 catches 21 of 36 known attacks, and the results say 21 of 28. The introduction's 79,933 and 67,005 are followed by 61,522 and about 65,000 in §V. These are not reconciled in the paper.
- **Its trust anchor is weak.** §VI concedes that a GitHub repository name is not unique, that a repository need not contain the package's code, and that an attacker can create a matching repository.
- **Short names are out of reach.** §VI says the method fits only names longer than the threshold.
- **The ground truth is only assumed.** Same-named repository means safe by assumption, and the safe count is therefore not a measured result.
- **Read scope.** The whole paper was read in the conference-site copy, except the reference list. The published IEEE Xplore page was not consulted.

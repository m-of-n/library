---
schema: "library-summary/v1"
id: ohm-2020-backstabbers
record: ohm-2020-backstabbers
type: summary
updated: "2026-11-04"
---

# Backstabber's Knife Collection: A Review of Open Source Software Supply Chain Attacks

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed conference paper |
| **Authors** | Marc Ohm, Henrik Plate, Arnold Sykosch, Michael Meier |
| **Published** | 2020, Springer |
| **Identifier** | `10.1007/978-3-030-52683-2_2` · `2005.09535` |
| **Source** | https://arxiv.org/pdf/2005.09535 |
| **Digest** | `sha256:a4e53919…` (full value in `record.yaml`), fetched 2026-11-01, re-verified 2026-11-04 |

## Overview

A manually curated dataset of 174 malicious packages from real attacks on npm, PyPI and RubyGems, dated November 2015 to November 2019, with two attack trees covering how malicious code gets injected and how it gets executed. The numbers carry the argument: 61% of packages used typosquatting, 56% triggered on installation, 41% used further conditions, 55% aimed at data exfiltration, and 49% used obfuscation. The paper's conclusion is that countermeasures exist already, and that they need to be more accessible and enforced by default.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A measured base rate for package attacks, with named techniques |
| Cryptography | `none` | No cryptographic content in what was read |
| This project | `adjacent` | Evidence about the threat, not a design input for any object |

- **R-M-03**: the 61% typosquatting share is a measurement of what global flat names cost. A name interpreted relative to an issuing principal cannot be typosquatted in the same way, although a key can be mistaken in its own way.
- It bears on no `DEC-*`. Most of the dataset is attack on package identity and install hooks, which is below the layer our objects sit at.

## Implementations

None applicable: this source describes an incident, not something to build on. No search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A paper has no FX-1 obligation, and nothing here needed a further artifact.

**Relations.** No `cites`: none of the paper's references is a record we hold. No `see_also` is authored here. The link to `vu-2020-typosquatting` is authored on that record, and the link to `npm-event-stream` on that one. The paper does not cite `in-toto-2019`, and no reason to relate them was found, so that edge was removed.

## Limits

- **Known sample bias.** §6.2 says the dataset leans heavily towards npm, and that no Java or PHP packages were obtained. The percentages describe this sample, not the ecosystems.
- **Second stages are missing.** About 34% are droppers whose payloads may no longer be available (§6.2).
- **Injection technique is often unknown.** §5.5 says the exact infection method often could not be determined, and such packages are filed as *infect existing package*.
- **The preprint is not the published text.** The arXiv copy was read; differences from the Springer chapter were not checked.
- **Read scope.** Abstract, §1, §2, §5.5 and §6 were read through text extraction. The attack trees in §4 and the rest of §5 were not read closely, so the trees are named here but not described. No sample code from the paper was run.

---
schema: "library-summary/v1"
id: c2pa-conformance-program
record: c2pa-conformance-program
type: summary
updated: "2026-11-05"
---

# C2PA Conformance Program and Trust List

|  |  |
|---|---|
| **Type** | web, with program documents |
| **Maturity** | unset: version 0.2, no enum equivalent |
| **Authors** | C2PA Technical Working Group Conformance Task Force |
| **Published** | Program v0.2, 2026-07-31 |
| **Identifier** | https://github.com/c2pa-org/conformance-public @ `f58b10a3` |
| **Source** | https://c2pa.org/conformance/ |
| **Digest** | `sha256:582ea699…` landing page, fetched 2026-11-01; document digests in `content.note` |

## Overview

The specification alone cannot make a signed claim trustworthy, so C2PA runs a governance program over it (Program §1, §3). A Governing Authority and its Conformance Task Force evaluate generator products, validator products and certification authorities, and place those that pass on public machine-readable lists: the Conforming Products List and Trust Lists (§3). Generator products get a Max Assurance Level from their security architecture, and each instance gets a level at certificate enrolment, carried in an X.509 extension (§2.6, §5). The Program calls this risk-based. `c2pa-2-4` §14.4.1 requires validators to include the C2PA Trust List among their anchors for that EKU, so the state called Trusted rests on this program.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The enforcement layer for signer trust, with assurance levels and attestation evidence |
| Cryptography | `adjacent` | X.509 policy and an assurance-level extension; the Certificate Policy itself was not read |
| This project | `adjacent` | A worked central-governance model. The contrast is the value |

- **DEC-007**: conformance shapes what may be said, not only who may say it. The Companion Guide defines `disallowedSignals`, signals a generator product is explicitly disallowed from emitting. In the list at the pinned commit, many entries bar source claims such as `capturedMedia`. That is governance over a predicate value, external to the signature. **DEC-007** is proposed, not accepted: it exists only in ARCH-0001-PROPOSAL v0.2.0 §5, and mofn's DECISIONS-0001 item 5d asks whether it survives at all.
- **R-I-02**: `c2pa-2-4` §14.4.1 requires this list as an anchor set for validators. Importing C2PA must not make it a native trust anchor, so a mapping has to treat it as foreign evidence.
- **R-I-05**: C2PA identity is X.509 throughout, so an imported signer is a foreign identity assertion about a key.

## Relations

- `see_also: c2pa-2-4`: that spec's §14.4.1 requires validators to include the C2PA Trust List this program governs, and Program v0.2 accepts spec v2.2 and v2.4 (§6.7.5). Authored only here; `c2pa-2-4` no longer repeats it.
- `see_also: c2pa-ux-2-2`: that guidance defines Trusted as the signer being "found on a supported Trust List" (§4.5), which is this program's list. Authored only here.
- `see_also: nsa-2025-content-credentials`: its p. 17 reports the early flaw of self-signed certificates shown as trusted, fixed by checking against a list of known certificates. Authored only here.

## Implementations

The list itself is the implementation record. At the pinned commit, `conforming-products-list.json` has 290 entries: 258 generator products and 32 validator products, all `conformant`. Of the 258 generators, 247 have Max Assurance Level 1 and 11 have level 2. Google LLC has the most entries at 50. These are our counts from one snapshot, and they will drift. Who the products are was not reviewed further.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. This is a `web` record, so FX-1 does not apply unless someone chooses to extract the program documents.

## Limits

- **The trust lists themselves were not read.** `C2PA-TRUST-LIST.json` and the TSA list were seen in the repository tree only. The record title promises more than this record covers on that point.
- **Early program.** It is version 0.2. §6.1.1 says complete conformance to the 300+ generator and 150+ validator requirements is something applicants will be held to eventually.
- **Moving target.** The landing page links spec 2.3. The first read (2026-11-01) recorded `docs/current` links that did not resolve; the 2026-10-19 Internet Archive capture and the 2026-11-05 refetch both link `docs/v0.2` instead, and the page's digest changed between reads (`content.note`). The Program's minimum spec level is v2.2 (§6.1.1). Table 1 gives v0.1 a sunset of 2026-10-09 and says v0.2 supports spec v2.2 and v2.4, so 2.5 is not covered by this version.
- **No claim of truth.** Conformance covers how a product behaves, not whether its assertions are accurate.
- **Read scope.** The landing page; Program v0.2 §1, part of the §2 glossary, §3 to §6.2, and headings to §6.7; Governance Framework section headings only; the Companion Guide's `disallowedSignals` definition; and scripted counts over the products list. Certificate Policy and Generator Product Security Requirements were not read. The Program was read as extracted text.

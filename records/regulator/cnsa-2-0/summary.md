---
schema: "library-summary/v1"
id: cnsa-2-0
record: cnsa-2-0
type: summary
updated: "2026-11-01"
---

# Commercial National Security Algorithm Suite 2.0 (CNSA 2.0) Algorithms and FAQ

|  |  |
|---|---|
| **Type** | spec (NSA Cybersecurity Information Sheet, FAQ) |
| **Maturity** | `best-practice`: binding on NSS through CNSSP 15, and guidance elsewhere (p. 6) |
| **Authors** | National Security Agency, no individuals named |
| **Published** | October 2026, Ver. 2.2. First issued September 2022 |
| **Identifier** | U/OO/6072712-26, PP-26-3194 |
| **Source** | https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF (read by archive copy, see `content.note`) |
| **Digest** | `sha256:bc430341…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

CNSA 2.0 is the public-algorithm suite for US National Security Systems, chosen from NIST standards with one parameter choice per job: AES-256, ML-KEM-1024, ML-DSA-87 and SHA-384 or SHA-512. LMS and XMSS are allowed for firmware and software signing, with LMS SHA-256/192 recommended, and SHA3-384 or SHA3-512 for internal hardware integrity only (pp. 7 to 8). The dates come from CNSSP 15: required for new acquisitions from 2027-01-01, unsupportable equipment phased out by 2030-12-31, and CNSA 2.0 mandated by 2031-12-31 (p. 17). Firmware comes first because a verifier in firmware is often locked for a system's life (p. 13). Everything else in the document narrows the field: multi-tree HSS and XMSS^MT, SLH-DSA, FN-DSA, HashML-DSA and the on-ramp results are all out (pp. 11, 15, 16, 27).

The strongest argument is against hybrids. NSA does not require them for security, says they add a second transition and complexity that can weaken security (pp. 28 to 29), and directs PKI migration to a parallel PKI, adding that NSS should not use novel mechanisms to carry multiple algorithms in one certificate (pp. 29 to 30). IKEv2 is the named exception, and only for an NSA-identified solution (p. 29).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | States dated requirements and argues the hybrid question |
| Cryptography | `core` | Picks specific parameter sets |
| This project | `adjacent` | Binds NSS only, and NG3 defers the suite. It marks what our most demanding possible users could accept |

- **R-M-06**: threshold signatures are on the list with no generally approved solution (p. 26). A threshold principal built on threshold cryptography could not be used in NSS. One built from separate signatures and a policy, which R-M-06 allows, avoids this.
- **R-I-05**: X.509 imports will meet parallel chains, with some devices holding a credential from each (p. 30), and not a single dual-algorithm certificate in NSS.

**Disagreement on the record.** See `draft-ietf-lamps-pq-composite-sigs` and `nistir-8547`, where the positions on hybrids differ. Not `contradicts`, because NSA speaks only for NSS.

## Implementations

Not applicable and not searched: it specifies a selection. Primitives have their own records. A note for anyone checking compliance: CMVP or NIAP validation is what counts here, not library support (pp. 9 to 12).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. It is a FAQ without BCP 14 keywords, so an FX-1 extraction would be unusual. No issue owns it. The PDFs stay in `.cache/` and are not committed.

## Limits

- **It defers to documents we do not hold.** CNSSP 15, CNSSP 11, NSM-10 and EO 14412 are described only as the FAQ describes them, and CNSSP 15 is the operative policy.
- **Internal slips in the source.** P. 22 cites "NISTIR 8647" for the 2035 disallowance, which is almost certainly IR 8547 (`nistir-8547`). P. 20 calls the CNSSP 15 change the 2024 update, while p. 24 speaks of its signing in 2025.
- **It moves in place.** Archive captures show four distinct files at this URL. Citations need the version, and this record tracks 2.2.
- **"No plans" is not "never".** P. 16 says circumstances could change.
- **Archive copy.** We did not verify the bytes from the origin.
- **Read scope.** The whole of Ver. 2.2 was read. The 2022 advisory was read only for its opening and the software-signing section. Earlier FAQ versions were not compared.

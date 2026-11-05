---
schema: "library-summary/v1"
id: sigstore-2022
record: sigstore-2022
type: summary
updated: "2026-11-04"
---

# Sigstore: Software Signing for Everybody

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed conference paper |
| **Authors** | Zachary Newman, John Speed Meyers, Santiago Torres-Arias |
| **Published** | 2022-11-07, ACM |
| **Identifier** | `10.1145/3548606.3560596` |
| **Source** | https://web.archive.org/web/20250717035128id_/https://dl.acm.org/doi/pdf/10.1145/3548606.3560596 |
| **Digest** | `sha256:85519305…` (full value in `record.yaml`), fetched 2026-11-01, re-verified 2026-11-04 |

## Overview

Signing adoption stayed low because key management is hard, so Sigstore removes keys from the developer's view. A client gets an OIDC identity token, generates a one-time key pair, and Fulcio issues a short-lived certificate binding it to that identity and logs it. The client signs once, discards the key, and records the signature in Rekor. The transparency log severs artifact lifetime from certificate lifetime: a verifier checks that the signature was logged while the certificate was valid (§4.2.1). Trust roots are distributed through TUF.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Binds artifacts to identities with public logs. Under an OIDC provider compromise it neither prevents nor detects an attack (§6.6), and depends on the impersonated user noticing |
| Cryptography | `adjacent` | Ephemeral keys and short-lived certificates. Classical signatures only in what was read |
| This project | `core` | The largest deployed test of short-lived credentials, and the contrast case for key-relative identity |

- **R-O-02**: the cleanest deployed case for short-lived validity. §4.2 gives certificates a 10 minute validity, and §6.5 limits a pipeline compromise to one run.
- **R-O-04**: the logs are what make misbehaviour detectable, and monitors are what make the logs matter.
- **R-M-02**: a direct contrast. Here a principal is an OIDC identity, and the key is disposable. Trust in Sigstore terminates in OIDC issuers and Fulcio, and R-M-02 needs neither.
- §7.4 is worth reading on its own: signed does not mean trusted, and humans eyeballing identities invites typosquatting.

## Implementations

**Searched 2026-11-01.** GitHub repository metadata checked.

| Name | Kind | License | URL |
|---|---|---|---|
| cosign | open source, client | Apache-2.0 | https://github.com/sigstore/cosign |
| fulcio | open source, CA | Apache-2.0 | https://github.com/sigstore/fulcio |
| rekor | open source, log | Apache-2.0 | https://github.com/sigstore/rekor |
| rekor-monitor | open source, monitor | Apache-2.0 | https://github.com/sigstore/rekor-monitor |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A paper has no FX-1 obligation, and nothing here needed a further artifact.

**Relations.** `cites` lists the held records in the reference list: [67] `tuf-2010`, [74] `in-toto-2019`, [34] `rfc-6749`, [46] `rfc-6962`, [7] `rfc-8555`, [47] `rfc-9162`. [4] cites the TUF GitHub repository, not a spec version. [17] is not listed because it contradicts itself: its authors and title (Cooper et al., *Certification Path Building*, 2005) are RFC 4158, but its title also says RFC 5280 and its URL is rfc5280. One `see_also`: `tuf-spec`, because §4.1 makes TUF Sigstore's root of trust, and `tuf-spec` is the current statement of TUF. `sigstore-threat-model` cites this paper, so that edge lives there.

## Limits

- **It does not say who is entitled.** §7.4 is explicit that users still must decide which identities may sign what, and recommends TUF for that. §5 covers the package repository case, which was not read in detail.
- **Terminology differs from `sigstore-threat-model`.** The paper calls Rekor's timestamped promise an SCT (§4.2.2). The threat model uses SCT for the Fulcio CT log and SET for Rekor. Follow the threat model.
- **Odd wording.** §9 uses "symmetric signatures" and "symmetric signing keys" in a way that appears to mean long-lived asymmetric keys. Sigstore's signatures are public-key.
- **The numbers are from April 2022.** Usage figures in §7.2 describe an early system.
- **Identity disclosure is a real cost.** §9.1 concedes that identities are public in a tamper-evident log.
- **Read scope.** The copy read is an Internet Archive capture of ACM's PDF. Abstract, §1, §3, §4.2, §4.3, §6, §7.2 to §7.4, §9 and §10 were read through text extraction. §2, §4.1, §5, §7.1 and §8 were not read closely.

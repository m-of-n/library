---
schema: "library-summary/v1"
id: sigstore-fulcio-oids
record: sigstore-fulcio-oids
type: summary
updated: "2026-11-06"
---

# Sigstore Fulcio certificate extension OIDs

|  |  |
|---|---|
| **Type** | dataset — a directory page in the Fulcio repository |
| **Maturity** | _unset_ — project documentation, no standards-track standing |
| **Publisher** | Sigstore (OpenSSF) |
| **Version** | commit `4d394f41b281f65bed55e5dad5c78956078fec3b` (2026-07-15) |
| **Identifier** | https://github.com/sigstore/fulcio/blob/main/docs/oid-info.md |
| **Source** | https://raw.githubusercontent.com/sigstore/fulcio/4d394f41b281f65bed55e5dad5c78956078fec3b/docs/oid-info.md |
| **Digest** | `sha256:5a99266663bee303d16575ca10f05f16fd6876e25d64e9f2b5a126550e6603d3` |

## Overview

Sigstore's directory of the X.509 extension OIDs that Fulcio writes into its
short-lived code-signing certificates. They record the OIDC identity behind a
signature: issuer, build signer URI and digest, runner environment, source
repository, ref, trigger, and so on. All sit under **1.3.6.1.4.1.57264**,
Sigstore's IANA Private Enterprise Number. On 2026-11-06 IANA's
enterprise-numbers registry lists 57264 as "Sigstore a series of LF Projects
LLC". That makes **three tiers of allocation**: IANA's arc, Sigstore's PEN, and
the sub-arcs `.1` (Fulcio) and `.2` (the Timestamp Authority policy), which
Sigstore allocates without asking anyone. A verifier still has to know
Sigstore's table.

The real SLSA provenance lane-a pulled (mofn#13, `03_slsa_provenance.py`, npm
`sigstore@2.3.1`) has a Fulcio leaf certificate carrying **21 of these OIDs**:
`.1.1`–`.1.6` and `.1.8`–`.1.22`.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Verifiers decide trust from these values, e.g. which workflow built and signed an artifact |
| Cryptography | `none` | Identity metadata, not algorithms |
| This project | `adjacent` | A working delegated namespace that is not IANA's, met by any export to Sigstore-signed SLSA (R-I-03) |

Bears on **R-M-12**, **R-I-03** and **DEC-005**. This is the nearest real
example of allocation delegated by *who holds the arc*, not by a registry's
review. But the arc is held by an organisation, not by a key, so it is not
R-M-12's `(defining key, local label)` form.

## Implementations

Searched GitHub code for `1.3.6.1.4.1.57264.1.9` (Build Signer URI) on
**2026-11-06**. Consumers hard-code the OIDs; a selection:

| Name | Kind | License | URL |
|---|---|---|---|
| sigstore/cosign | signer and verifier | Apache-2.0 | https://github.com/sigstore/cosign |
| pypi/pypi-attestations | PyPI attestation verifier | Apache-2.0 | https://github.com/pypi/pypi-attestations |
| rubygems/rubygems.org | registry (trusted publishing) | MIT | https://github.com/rubygems/rubygems.org |
| docker/buildx | build tool | Apache-2.0 | https://github.com/docker/buildx |
| microsoft/did-x509 | DID method over X.509 | MIT | https://github.com/microsoft/did-x509 |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, with the pinned-commit digest |
| `summary.md` | this document |

**No committed copy.** The page is cached in `.cache/`, which is gitignored.
**No `distilled/`:** a `dataset` is outside FX-1.

## Limits

- **Fixing an allocation means minting a new one.** `.1.1`–`.1.6` are raw
  strings with no DER encoding, and `.1.8` onward are DER-encoded. Correcting
  that took new OIDs: Issuer (V2) `.1.8` replaces `.1.1`, and the
  GitHub-specific `.1.2`–`.1.6` gave way to provider-neutral ones. The lane-a
  leaf certificate still carries **both** sets, because older verifiers know
  only the old numbers. That is the price of a number that can't be
  redefined.
- **Sigstore translates names, provider by provider.** The page's "Mapping
  OIDC token claims to Fulcio OIDs" table maps each CI provider's own claim
  (GitHub `job_workflow_ref`, GitLab `ci_config_ref_uri`, and so on) onto one
  Fulcio OID. This is the local agent that `zooko-2001-names` says
  key-relative names would need, run here by a central party.
- **No allocation process is stated.** The page lists values and their meaning
  but says nothing about how a new sub-arc is assigned. Its MUST and SHOULD
  text addresses OIDC providers and consumers, not allocation.
- **Lane-a lists these OIDs but does not test them.** The real provenance is
  signed by a Fulcio key we don't hold, so it can't be changed (lane-a README,
  "Not tested"). The leaf certificate is in mofn's `prototype/lane-a/out/`,
  which is gitignored; `run-all.sh` regenerates it. `.1.7`, `.1.23` and
  `.1.24` are absent from that certificate.
- **The page lives on `main`.** The digest pins one commit. The identifier URL
  moves.

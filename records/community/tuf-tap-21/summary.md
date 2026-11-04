---
schema: "library-summary/v1"
id: tuf-tap-21
record: tuf-tap-21
type: summary
updated: "2026-11-03"
---

# TAP 21: ML-DSA signing scheme for TUF metadata

|  |  |
|---|---|
| **Type** | spec (TUF Augmentation Proposal, Type: Standardization) |
| **Maturity** | _unset_. The TAP header says Status: Accepted, confirmed by PR #199 "Accept TAP 21" merged 2026-10-06. An accepted TAP does not map to any of the schema's maturity levels, so we do not assert one |
| **Authors** | Fredrik Skogman |
| **Published** | Created 2026-04-29; Last-Modified 2026-09-30; Version 1 |
| **Identifier** | TAP 21 · `theupdateframework/taps` commit `21efd976` |
| **Source** | https://github.com/theupdateframework/taps/blob/master/tap21.md (bytes identical at `21efd976`) |
| **Digest** | `sha256:0e62f9af…` (full value in `record.yaml`), fetched 2026-11-03 |

## Overview

TAP 21 adds an `ml-dsa` keytype to TUF. Its argument is about the signing interface, not the algorithm. Pure ML-DSA needs the whole message at the signer. TUF targets metadata can be large, and HSMs bound message size (Motivation). So the TAP never signs the metadata itself. It signs a short **pre-signing byte string**, `0x74 0x75 0x66 ("tuf") || version || H(MSG)`, with pure ML-DSA and an empty context (Specification). It rejects HashML-DSA and leans on FIPS 204 §5.4's allowance for application-level hashing (Rationale; Appendix, *Notes on application level hashing*).

The design idea worth keeping is that **the version byte names the whole suite**. v1 fixes SHA-512 as H, TUF canonical JSON as the canonicalisation, and ML-DSA-44/65/87 as MUST-support parameter sets (Protocol versions, v1). The scheme string `ml-dsa-<set>/<version>` carries it. The verifier MUST take the version from trusted metadata, not from the signature, and must reconstruct the signed bytes itself, with no fallback, no alternative interpretations, and no acceptance under HashML-DSA (Verification steps 3–5).

For the topic question, TUF has a **stated, accepted post-quantum path**: ML-DSA alone, with no hybrid. It is implemented in securesystemslib 1.5.0 and go-tuf. What it lacks is any migration plan. Backwards Compatibility only says that old clients cannot verify `ml-dsa` signatures. Nothing addresses rotating a root from ECDSA to ML-DSA keys, or mixing keytypes inside a role's threshold. The mofn mini-report H records that in-toto has no spec-level path and depends on this ecosystem work. TAP 21 is the nearest thing to that path.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Domain separation, version binding and the verifier's no-fallback rules are the security content (Specification; Verification steps; Security Analysis) |
| Cryptography | `adjacent` | Uses FIPS 204 and SHA-512 and defines no primitive. Its one cryptographic claim, that SHA-512 is enough for ML-DSA-87 with "zero margin", rests on FIPS 204 §5.4 |
| This project | `adjacent` | A worked precedent for a citable signing suite over canonical bytes. Not a format we adopt |

- **R-O-03** ("Canonicalization algorithm for each concrete encoding SHALL be cited, not invented silently"): v1 does exactly this. The canonicalisation scheme is a named field of the protocol version, pointing to TUF canonical JSON, and it is bound into the signed bytes through the version byte. A canonicalisation change is a new version, never a silent change.

Not claimed in `bears_on`, but recorded: this lines up closely with `mofn` research R-0003 §1 ("One suite is one immutable record. It has an identifier a statement can cite … and the exact bytes that are signed (or a pointer to that rule)") and §4.5 (the verifier's policy, not the statement, must pick the suite). The TAP's rationale says the version is "an all-or-nothing approach". R-0003 is a draft memo, not a requirement, so it is not listed as `bears_on`.

## Implementations

**Searched 2026-11-03** (GitHub API and repository changelogs).

| Name | Kind | License | URL |
|---|---|---|---|
| securesystemslib 1.5.0 | open source, Python | MIT | https://github.com/secure-systems-lab/securesystemslib/blob/main/CHANGELOG.md |
| go-tuf (PR #780, merged 2026-09-14) | open source, Go | Apache-2.0 | https://github.com/theupdateframework/go-tuf/pull/780 |
| tuf-conformance | open source, test suite | MIT | https://github.com/theupdateframework/tuf-conformance |

go-tuf #805, "Validate the ML-DSA public-key PEM envelope", was still open on 2026-11-03. tuf-conformance's ML-DSA tests are as claimed by the TAP and were not checked.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata pinned to commit `21efd976`, relations, `bears_on`, implementations survey, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar for the `post-quantum-migration` topic (library#45). As a `spec` record it would owe FX-1 if extracted, and **no issue owns that yet**. The document is short (264 lines) and has a small requirement set: the v1 MUST-supports, the empty-context MUST, and the verification MUST NOTs. Extraction would mostly cost the reconciliation of its mixed-case keywords (see Limits). No keyword count is given here.

**Relations.** `see_also` edges: `tuf-spec` (the specification this TAP augments, and the source of its canonical JSON), `fips-204` (the ML-DSA it signs with, §5.4 and §7.2 cited), `rfc-9881` (the `SubjectPublicKeyInfo` encoding `keyval.public` uses), and `draft-ietf-lamps-pq-composite-sigs` (the opposite, AND-hybrid answer; see Limits).

## Limits

- **No migration or hybrid.** It does not address rotating existing ECDSA/Ed25519 roots to ML-DSA, a transitional period, or composite/dual signatures. Compare `draft-ietf-lamps-pq-composite-sigs`, which takes the opposite (AND-hybrid) route for X.509.
- **No stateful option.** LMS/XMSS are not considered, although CNSA 2.0 allows them for software and firmware signing alongside ML-DSA-87 (`cnsa-2-0`, pp. 7–8). ML-DSA alone is CNSA-compatible only at ML-DSA-87.
- **Size is measured, not mitigated.** The Appendix shows root metadata growing 7.0x (ML-DSA-44) to 12.8x (ML-DSA-87) on the Sigstore root-signing example, and per-signature growth of 33.6x to 64.3x over ECDSA in hex encoding. Hex doubles the raw FIPS 204 sizes (2420 → 4840 bytes for ML-DSA-44). No compact encoding is proposed.
- **Normative language is loose.** Only some requirements are capitalised. "Version must be a single byte", "Any other version must be rejected" and "It should not accept a caller-supplied digest/prefix blindly" are lower-case, so whether they bind under BCP 14 is unclear, and the TAP cites no RFC 2119.
- **Points at an older TUF spec.** The canonical-JSON reference links TUF specification v1.0.34; the library's `tuf-spec` record is v1.0.36. Not checked for changes to canonical JSON between them.
- **Security analysis is brief.** Three bullets, no proof. The length-extension and domain-collision claims are plausible but unargued. The pre-signing string has no length prefix and relies on the fixed 3-byte domain plus 1-byte version.
- **A correction to the parent project's research, not to the TAP.** mofn mini-report H says TAP 21 was "merged May 2026". The GitHub API shows PR #195 opened 2026-05-04 and merged 2026-07-29, and acceptance came with PR #199 on 2026-10-06.
- **Read scope.** The whole document was read. The linked implementations were checked only by changelog or PR state, not by code.

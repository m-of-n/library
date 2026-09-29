---
schema: "library-summary/v1"
id: rfc-9943
record: rfc-9943
type: summary
updated: "2026-09-27"
---

# An Architecture for Trustworthy and Transparent Digital Supply Chains

|  |  |
|---|---|
| **Type** | rfc (IETF, Standards Track) |
| **Maturity** | `standard` — Standards Track, IESG-approved. **Not an STD**; it depends on STD 94 and STD 96 |
| **Authors** | H. Birkholz (Fraunhofer SIT), A. Delignat-Lavaud, C. Fournet (Microsoft), Y. Deshpande (ARM), S. Lasker |
| **Published** | 2026-06 |
| **Identifier** | RFC 9943 · DOI 10.17487/RFC9943 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9943.txt |
| **Digest** | `sha256:204aea02…` — full value in `record.yaml`, re-verified 2026-09-27 |

## Overview

SCITT's claim is that a signature proves *who issued* a statement and nothing more, and that the missing half is **non-equivocation**: an Issuer must not be able to tell different Relying Parties different things about the same Artifact and later shred the evidence. The architecture supplies that half by having a **Transparency Service** register a Signed Statement (a `COSE_Sign1` envelope whose CWT Claims header carries `iss` and `sub`, §6) into an append-only **Verifiable Data Structure**, then return a **Receipt** — a signed inclusion proof, defined not here but in COSE Receipts [`rfc-9942`]. A Signed Statement plus its Receipts in the unprotected header (label 394) is a **Transparent Statement**, and the RFC is explicit that this is notarization, not verification: registration proves a statement was made and logged, never that it is true (§9.2).

The design decision that gives the document its reach is that the **payload is opaque** (§3, *Statement*). The TS checks the envelope, the Issuer identity and its Registration Policy; it does not parse SBOMs, scan results or attestations. SCITT is therefore positioned as the generalisation of Certificate Transparency — §4 rewrites CT in SCITT's own vocabulary, CAs as Issuers, logs as TSs — with the content-specific part removed.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | **`core`** | Defines the threat model (§9.7) and states the residual guarantees when Issuers *and* TSs are compromised |
| Cryptography | `adjacent` | Invents none. Signing is `COSE_Sign1` (STD 96); proofs and VDS algorithms are entirely [`rfc-9942`] |
| This project | **`core`** | It is the fully-worked version of the shape we are designing, ratified and with a live deployment |

`bears_on` reads as follows, and each warrant is checkable in the text:

- **DEC-007** — the strongest of the three. SCITT's answer to *how a claim about an artifact is rendered* is: identity in `iss`, the thing spoken about in `sub`, the assertion itself an opaque tagged payload. Compare [`w3-org-pics`], which put the predicate vocabulary in the protocol and is on the same decision; SCITT puts it outside and keeps only the binding.
- **R-M-12** — this RFC is a clean specimen of the registry-allocated identifier pattern. It burns two media types (`application/scitt-statement+cose`, `application/scitt-receipt+cose`), two CoAP Content-Format numbers (277, 278, §10.3), and leans on COSE header labels 394/395/396 and CWT Claim labels 1 and 2. Nothing in the architecture works without a registry entry someone had to be granted.
- **DEC-002** — the weakest, and worth stating narrowly. The only canonicalization requirement in the document is §6.3: the unprotected header **MUST** be emptied before a Signed Statement enters the Statement Sequence. That one rule is where byte-level determinism bites, because the leaf an inclusion proof is computed over must be re-derivable by an Auditor. The RFC does not cite CDE or dCBOR; it inherits whatever determinism COSE's to-be-signed bytes give it.

## What it settles, and what it costs

The topic question is `topics/scitt.yaml`. The record's contribution to it:

**Settles.** Three properties a lone signature does not have (§9): statements are attributable and authenticable; their provenance and history are *independently auditable* by a party who trusts neither the Issuer nor the operator of the log; and an Issuer can prove cheaply that a statement was logged. Registration Policies and trust anchors are themselves registered as Signed Statements on the VDS (§5.1.1.1), so the rules in force at registration time are replayable — an Auditor can reproduce a past decision. A Receipt is verifiable offline (§4), so the log is not in the verification path.

**Costs.** Four, all named by the RFC itself:

1. **The trust anchor moves; it does not disappear.** A TS's identity *is* a public key that Relying Parties must already know (§3), and §4 permits its key, algorithm and claims to change on *every* Receipt issuance. The Issuer PKI problem is replaced by a TS key-distribution problem the document leaves out of scope.
2. **Completeness is unprovable.** An Issuer can simply not register (§9.3). The RFC's mitigation is an instruction to Relying Parties not to accept statements whose Receipts they cannot discover — but discovery is explicitly out of scope (§1), so this obligation has no mechanism inside this RFC.
3. **Order is registration order, not issuance order** (§9.1), so the log times the notarization, not the claim.
4. **A ledger entry per statement, forever.** Append-only means no deletion; §8 notes a TS may log only a hash to limit exposure, which then requires an Adjacent Service to hold the bytes and reintroduces metadata leakage.

## Implementations

**Searched 2026-09-27.** The result is thinner than the RFC's status suggests, and that is the finding.

| Name | Kind | License | URL |
|---|---|---|---|
| DataTrails SCITT API | commercial | not stated | https://docs.datatrails.ai/developers/developer-patterns/scitt-api/ |
| `datatrails/scitt-action` | open source | not stated | https://github.com/datatrails/scitt-action |
| vCon Conserver SCITT link | open source | not stated | https://github.com/vcon-dev/vcon-server/tree/main/server/links/scitt |
| `CSOAI-ORG/csoai-scitt-ts` | open source | MIT | https://github.com/CSOAI-ORG/csoai-scitt-ts |
| `achamayou/scitt-for-phi` | open source (demo) | not stated | https://github.com/achamayou/scitt-for-phi |

Three observations, in descending order of importance to us:

- **The WG's own implementation list (https://scitt.io/implementations.html) is pinned to "Draft Version: 10"** — it has not been updated to the published RFC. The DataTrails Action describes itself as Preview, pending adoption of SCRAPI. An RFC three months old with a stale implementation index is exactly the uptake pattern `topics/uptake-failure.yaml` exists to characterise.
- **One of the implementations is a vCon link.** The vCon Conserver ships a SCITT integration, and we hold [`draft-ietf-vcon-vcon-core-04`], whose distillation found that *a vCon has no speaker*. SCITT requires `iss` in the protected header. Someone has already wired the container with no asserter to the architecture that mandates one; what `iss` gets set to in that link is a concrete, readable answer to a question we raised abstractly.
- `csoai-scitt-ts` is the only thing found claiming RFC 9943 conformance outright. It is an unvetted MVP from an organisation we know nothing about. Recorded because the search found it, not because it is credible.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `quotes.md`, no `distilled/`. Nothing here is built on yet — the section locators above are the substitute, and a reader checking a claim should open the RFC at the cited §. If this record is ever used to *extract requirements* (its MUSTs are dense and mostly in §5.1.1.1, §6 and §6.3), that is a `distill` job and needs its own artifact.

## Limits

- **The document contradicts itself on the property it sells.** §1 calls the ledger "a linear and irrevocable history"; §5.1.3 requires the Statement Sequence to be unmodifiable, undeletable and unreorderable. Then §9.4.2 says a TS whose signing key is compromised "can roll back their Statement Sequence to a point before compromise, establish new credentials, and use the new credentials to issue fresh Receipts." A sanctioned rollback is a fork, and a fork is the equivocation the architecture exists to prevent. The RFC gives no mechanism by which a Relying Party learns a rollback happened, nor any status for Receipts issued over the discarded prefix. **This is the single most important thing in the document for us**, because our own design will face the same question and cannot answer it the same way.
- **It settles no VDS.** §5.1.3 states requirements (append-only, non-equivocation, replayability) and defers every instantiation and its security analysis to [`rfc-9942`] and RFC 9162. The security of a SCITT deployment is decided in documents this one does not contain.
- **RFC 9162 (Certificate Transparency 2.0) is not in the library**, though §4 and §5.1.3 lean on it and the default VDS algorithm is `RFC9162_SHA256`. That is a frontier gap, not an oversight to fix in this record.
- **No API, no discovery, no revocation.** Registration is described as five steps (§6.3) with the wire protocol absent; that is SCRAPI (`draft-ietf-scitt-scrapi`), also not held. Key revocation strategies are out of scope (§9.4.2).
- **Client authentication and authorization are out of scope** (§6.3 step 1), and a Client need not be the Issuer (§7) — so *who may register a statement on whose behalf* is unspecified by the architecture.
- **`part_of` is unset.** RFC 9943 is a product of the IETF SCITT WG and we hold no consortium record for it, unlike [`ietf-cose-wg`] and [`ietf-cbor-wg`]. The edge is missing because the parent does not exist yet.

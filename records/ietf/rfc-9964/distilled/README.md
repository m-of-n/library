---
record: rfc-9964
kind: index
title: "rfc-9964 — distilled artifacts"
extracted: "2026-10-19"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what it
does not.

RFC 9964 is a short document with one load-bearing section. **§6 answers a
question RFC 9679 §4.6 asks and declines to answer** — which parameters are
required for an AKP COSE Key Thumbprint — and `records/ietf/rfc-9679` is at
`profile: full` with that dependency recorded. This extraction's job was to make
the consequence measurable rather than argued. It is.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | every normative sentence of §3–§7 with its locator. **Written by the parallel pass-1 agent**, which owns it together with `requirements.yaml`; not described further here. |
| requirements | `requirements.yaml` | every BCP 14 requirement with reconciled keyword counts. **Parallel pass-1 agent.** |
| schema | `schema/` | **RFC 9964 ships no grammar of any kind** — `CDDL`, `ABNF`, `ASN.1` and `JSON Schema` each occur zero times. One verbatim file carries the four places the document renders a structure itself (Figures 1 and 2, Table 1, §6's bullet lists); the other five are the library's own and carry `.derived.`. 45 CDDL rules across three files, two JSON artifacts. Does **not** constrain map order, encoding determinism, key validity, `pub`/`priv` agreement, or `ctx`. `schema/README.md` has the per-file table. |
| messages | `messages.yaml` | 9 structures, 36 fields, with the actual code points and octet-level layouts: the AKP and ML-DSA `COSE_Key`, **both §6 thumbprint inputs**, the JWK, the tag-18 `COSE_Sign1`, the `Sig_structure`, the header parameters and the JWS. `constrained_by` is **deliberately absent everywhere** — the requirement ids belong to the parallel pass and R-O-03 forbids guessing them; every field carries `locator` instead, which is what a later pass needs to add the links mechanically. |
| protocol | `protocol.yaml`, `protocol.md` | **NOT APPLICABLE — stubs, deliberately.** RFC 9964 defines no protocol: `verifier`, `sender`, `recipient`, `protocol` and `exchange` each occur **zero** times, `signer` once (in a §7.1 sentence about impersonation) and `request` once (the RFC masthead). §5 defers the envelope outright: "When producing COSE signatures, no encoding is needed; see Section 4 of [RFC9052] for more details on how COSE signatures are created." The signing protocol is RFC 9052's; see `records/ietf/rfc-9052`. |
| state-machine | `state-machine.yaml` | **NOT APPLICABLE — stub, deliberately.** `state`, `lifecycle`, `revoke` and `revocation` each occur **zero** times. The only ordered procedure is §7.3's key validation (seed length check, then `pkDecode`/`skDecode` range checks) and it is a precondition list, not a lifecycle: no states, no transitions, no terminal condition. |
| examples | `examples/` | **12 vectors, and the document prints real cryptographic test vectors** — six complete worked examples (Appendix A, Figures 3–8) with real FIPS 204 keys of 1312/1952/2592 octets, real signatures of 2420/3309/4627 octets, the exact signed bytes, and `kid` values that all six reproduce. Plus the hazard fixture: three `KeyId`s from one byte-identical `pub`, one leg printed by the RFC itself. These are the library's **first post-quantum fixtures**. Signatures are **not** verified cryptographically — no FIPS 204 implementation was available; every vector says so. |
| design-notes | `design-notes.md` | what our post-quantum export must carry with code points; **the `KeyId` consequence** and the four mitigations that exist; six cuts against `MD-3` naming `DEC-002` options 1–5, `DEC-003` and `DEC-005`; five open questions; the sibling records' claims checked; six source defects and ambiguities. |

## The one result

`alg` (label 3) is **inside** the AKP COSE Key Thumbprint, because §3 makes it
REQUIRED for all AKP keys and §6 then states the thumbprint set outright. For
one byte-identical 1312-octet ML-DSA-44 public key:

| `alg` | `KeyId` | provenance |
|---|---|---|
| −48 | `b8969ab4…d3a8059a` | **printed by RFC 9964** as the `kid` of Figure 6 |
| −49 | `f507c417…f187315d` | computed by this extraction |
| −50 | `de68d5ec…e128f62b` | computed by this extraction |

Three 1322-octet inputs differing in two octets; three digests sharing no
prefix. Under `ARCH-0002` P1 (accepted by `ADR-0001`) a post-quantum parameter
change is therefore a **namespace rename**, not a re-signing.

## Verification in pass 1

A CBOR encoder/decoder written for this pass (RFC 8949 §4.2.1) plus
`hashlib.sha256`. **No CBOR, COSE, JOSE or JWT library was used.** All three
COSE Key Thumbprints and all three JWK Thumbprints reproduce the printed `kid`
values exactly; `vectors.yaml` round-trips through the library's own YAML reader
under 121 re-derived assertions with zero failures; 45 CDDL rules close with no
undefined reference and no prelude collision. Details in
`schema/README.md` and `examples/README.md`.

## Source defects found

Reported, never repaired. Six, in `design-notes.md`; the two that cost a reader
something are **Figure 2's `pub` prefix differing from the key it illustrates**
(19th hex digit `9` where the key has `f`) and **§6 naming no hash function**
(the string `SHA-256` occurs zero times in RFC 9964; SHA-256 is established only
by the Appendix A `kid` values reproducing under it).

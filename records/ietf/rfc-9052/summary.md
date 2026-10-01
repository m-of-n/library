---
schema: "library-summary/v1"
id: rfc-9052
record: rfc-9052
type: summary
updated: "2026-09-30"
---

# CBOR Object Signing and Encryption (COSE): Structures and Process

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | standard — Internet Standards Track; **Internet Standard**, and **STD 96** jointly with RFC 9338 |
| **Authors** | J. Schaad (August Cellars) |
| **Published** | August 2022 |
| **Identifier** | RFC 9052 · DOI 10.17487/RFC9052 · STD 96 · obsoletes RFC 8152 (together with RFC 9053) |
| **Source** | https://www.rfc-editor.org/rfc/rfc9052.txt |
| **Digest** | `01eecd7f6465…` (sha-256 of the .txt, retrieved 2026-09-22; re-verified against `.cache/` on 2026-09-30) |

**On STD 96, precisely.** STD 96 is RFC 9052 **plus RFC 9338** and nothing else.
Both documents carry `STD: 96` on their front page (RFC 9052 p.1; RFC 9338 p.1,
which also reads `Updates: 9052`). RFC 9053 ("Initial Algorithms") and RFC 9054
("Hash Algorithms") were published the same month but as **Informational**, and
are **not** part of STD 96 — even though RFC 9052 §13.1 lists RFC 9053 as a
*normative* reference and even though RFC 9052 + RFC 9053 are jointly what
obsoletes RFC 8152 (§1, abstract). So STD 96 is an Internet Standard whose
mandatory algorithm document sits outside the standard. That asymmetry is the
detail most write-ups collapse, and it matters to us: citing "STD 96" does not
cite any algorithm.

## Overview

COSE does for CBOR what JOSE did for JSON — signatures, MACs and authenticated
encryption over a CBOR-serialised payload — but only for store-and-forward or
offline use (§1). Its structural argument is uniformity: all six message types
are CBOR arrays whose first three elements are always the same (protected header
bytes, unprotected header map, content), so one parser and one dispatch path
serve signing, MACing and encryption, with type identified by CBOR tag (18 =
`COSE_Sign1`, 98 = `COSE_Sign`, 16/96 = Encrypt0/Encrypt, 17/97 = Mac0/Mac), by
the `cose-type` parameter of `application/cose`, by CoAP Content-Format, or by
context (§2). The protected/unprotected split exists to dodge canonicalisation:
the protected map is CBOR-encoded, wrapped in a `bstr`, and transported as
opaque bytes, so verifiers re-use the bytes that were signed instead of
re-serialising a map — §3 states the motive outright, that this "avoids the
problem of all parties needing to be able to do a common canonical encoding of
the map for input to cryptographic operations". The unprotected bucket carries
only hints whose corruption is either harmless or self-detecting (`kid`, `IV`,
`Partial IV`); attributes MUST be read from the protected bucket first, and a
label repeated within one map MUST make the message malformed. The
`Sig_structure` indirection is the same argument applied to the whole object:
nothing signs the transmitted array. A verifier rebuilds a separate, never-
transmitted array — a context string (`"Signature"` or `"Signature1"`), the body
protected bytes, the signer protected bytes (omitted for `COSE_Sign1`),
`external_aad`, and the full payload — encodes it under §9's restricted rules,
and *that* byte string is signed (§4.4). The context string is what makes
`COSE_Sign` and `COSE_Sign1` non-convertible (§4), i.e. domain separation is
carried in the signed bytes rather than trusted to the envelope; `Enc_structure`
(§5.3) and `MAC_structure` (§6.3) repeat the pattern for AAD and for
to-be-MACed bytes. COSE deliberately defines **no** digest structure, arguing
that each protocol wants different adjacent fields (§1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The protected/unprotected split, the §4.4 `Sig_structure`, and §3's protected-first precedence and duplicate-label rejection *are* the integrity model — a verifier that gets them wrong verifies the wrong bytes with a strong primitive. §12 adds the key-reuse, direct-recipient-leakage and message-length traffic-analysis failure modes. |
| Cryptography | core | It defines no primitives (§1 defers to RFC 9053 and RFC 8230; §8 is an explicitly non-exhaustive taxonomy), but it does define the cryptographic *constructions*: what bytes enter Sign/MAC/AEAD, how AAD is built, the `COSE_Key` representation with `kty`/`alg`/`key_ops` (§7), and the rule that a key's `alg` MUST match the operation. Those are the parts where a design error survives any primitive choice. |
| This project | core | `COSE_Sign1` is one of the two candidate envelopes in **DEC-005**, and PLAN-0003 **D-3** selects COSE as the *export* form only. The §4.4 construction is what an interoperable export must reproduce byte-for-byte. |

Bears on **DEC-005** (envelope for `ArtifactStatement`: DSSE or `COSE_Sign1`,
both over a single unsigned payload schema). RFC 9052 gives `COSE_Sign1` its
concrete advantage — `external_aad` (§4.3) lets us bind context that is not in
the statement, which DSSE has no slot for — and its concrete cost, which is that
`COSE_Sign1` is tagged, labelled and typed entirely out of IANA registries.

Bears on **DEC-002 / D-3** (encoding). D-3 reads "Option 5: reduced CBOR, no
IANA tags, COSE export only", and this document is the reason that sentence has
two halves. COSE is unusable as a *native* model under our own rules, because
every extension point it has is registry-allocated; it is entirely usable as an
export envelope, because at an interchange boundary registry identifiers are
allowed and the mapping is documented as lossy (ADR-0001 consequences, R-I-01).

Bears on **R-M-12** (ADR-0001, accepted 2026-09-22: native extension points are
`(key, local label)` pairs, dependent on no central registry). RFC 9052 is the
clean counter-example. It defines only six common header parameters — `alg` 1,
`crit` 2, `content type` 3, `kid` 4, `IV` 5, `Partial IV` 6 (§3.1 Table 3) — and
five common key parameters (§7.1 Table 4); everything else, including every
`alg` value, comes from the IANA "COSE Header Parameters", "COSE Algorithms",
"COSE Key Types" and "COSE Key Type Parameters" registries, which §11 does not
create but merely re-points from RFC 8152. §11.6 then hands allocation to
Expert Review with instructions to discourage "point squatting" — the exact
governance dependence ADR-0001 rejects for the native model, and exactly the
kind of dependence it permits at an export boundary.

## Implementations

`searched: not re-searched on 2026-09-30; see rfc-8949 record for the CBOR-layer
survey` (that record's `implementations` block is dated 2026-09-22 and covers
the encoders these COSE libraries sit on). This record's own `record.yaml` has
no `implementations` block. The entries below are named for orientation only;
none was version-checked, licence-checked or built on 2026-09-30, so no licence
is asserted.

| Name | Kind | License | URL |
|---|---|---|---|
| veraison/go-cose (Go) | open source | licence not verified | https://github.com/veraison/go-cose |
| google/coset (Rust) | open source | licence not verified | https://github.com/google/coset |
| t_cose (C, companion to QCBOR) | open source | licence not verified | https://github.com/laurencelundblade/t_cose |
| cose-wg/COSE-C (C/C++) | open source | licence not verified | https://github.com/cose-wg/COSE-C |
| libcose (constrained C) | open source | licence not verified | https://github.com/bergzand/libcose |
| cose-wg/Examples (test corpus, not a library) | open source | licence not verified | https://github.com/cose-wg/Examples |

Two things are verifiable from the source rather than from a search, and both
bear on a build-on-it decision:

- **The real test corpus is not in the RFC.** Appendix C names
  `cose-wg/Examples` explicitly, at **commit 3221310, 3 June 2020**, as holding
  "not only the examples presented in this document, but a more complete set of
  testing examples as well", including deliberate failure cases. Every COSE
  implementation's conformance claim traces to that repository, so it — not
  RFC 9052 — is the artefact to pin and digest if we want a shared vector set.
- **The COSE layer inherits its determinism from the CBOR layer.** §9 aligns its
  restrictions with RFC 8949 §4.2.1, which means the caveat recorded against the
  CBOR libraries (that "RFC 8949 compliant" says nothing about whether the
  §4.2.1 form can be produced) propagates upward: a COSE library is only as
  byte-stable as the encoder under it.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, identifiers, digest, typed relations (`supersedes: rfc-8152`, `part_of: ietf-cose-wg`) and `bears_on` |
| `summary.md` | this document |
| `distilled/README.md` | FX-1 index: one line per artifact, what it covers and what it does not |
| `distilled/normative.md` | every normative statement verbatim with its section locator, in the source's own section order |
| `distilled/requirements.yaml` | each requirement as an addressable row (`rfc-9052#R-NNNN`) with object/field/verb/actor, reconciled against the BCP 14 keyword count |
| `distilled/schema/` | the source's own CDDL, verbatim, per section — currently only `README.md` (no `.cddl` file has been written yet) |
| `distilled/messages.yaml` | the six message structures plus `COSE_Key`/`COSE_KeySet` and the three internal types, field by field |
| `distilled/protocol.yaml` | roles and flows; for this source that means the §4.4 / §5.3 / §5.4 / §6.3 procedures |
| `distilled/protocol.md` | the same model as a diagram |
| `distilled/examples/` | Appendix C examples as fixtures with expected results — currently only `README.md` (no fixture files yet) |
| `distilled/design-notes.md` | what we adopt, adapt and reject, mapped to DEC-005, D-3 and R-M-12 |
| `distilled/state-machine.yaml` | state machines; **expected to close as not-applicable** — see below |

**These are scaffolds, not an extraction.** As of 2026-09-30 every file under
`distilled/` is `bin/extract-scaffold` output still carrying unfilled
placeholder markers (49 of them, in all ten files), the whole directory is
untracked on `topic/cbor-extraction`, and `record.yaml` still reads
`status: fetched` with no
`distillation.profile`. `bin/validate` fails such a record on those
placeholders, and it should. Anyone reading this table as a description of completed work will
be wrong; read it as the work plan. Two concrete notes for whoever fills it:
`bin/bcp14-count .cache/rfc-9052.txt` returns **53**, which is the number
`requirements.yaml` must reconcile to; and the `state-machine` slot has nothing
to hold, because COSE is a single-shot object format with procedures, not a
protocol with roles exchanging messages over time — the honest outcome is an
explicit not-applicable declaration, and the same strain shows in
`protocol.yaml`'s `roles`/`flows` shape.

## Limits

- **It defines no algorithms.** §1: "This document does not contain the rules
  and procedures for using specific cryptographic algorithms." They are in
  RFC 9053 (Informational) and RFC 8230, and RFC 9864 (2025-10, Standards Track)
  now **updates** RFC 9053 with fully-specified algorithms. So the answer to
  "which `alg` value do I put in the protected header" is not in STD 96, is not
  standards-track where STD 96 points, and has moved since 2022.
- **Header parameters and algorithm values are registry-allocated, not
  document-allocated.** §11 creates no registry; it re-points RFC 8152's
  registries at itself. The document defines six header labels and five key
  labels; every other label, every `alg` value, every `kty`, and the CBOR tags
  and `cose-type` strings in §2 Table 1 are IANA entries under Expert Review
  (§11.6). This is the R-M-12 collision, and it is structural, not incidental.
- **It carries no complete test vectors.** Appendix C is CBOR *diagnostic
  notation*, not bytes — you need `diag2cbor.rb` to get an octet string, and the
  RFC tells you so. There are no negative cases in the document; the failure
  vectors live in `cose-wg/Examples`, whose named commit predates publication by
  two years and is outside the RFC's change control. Even the positive cases
  are verification-only fixtures: ECDSA is randomised, so C.1/C.2 signatures
  cannot be reproduced by re-signing with the C.7 private keys, only checked.
- **Countersignatures are absent by design, and the removal is incomplete on the
  wire.** §1 records that COSE's original countersignature was found to have the
  wrong security properties for `COSE_Sign1` during advancement, so all of it
  moved to RFC 9338. But §3.1 still requires new implementations to *understand*
  label 7 for `crit` purposes, and §11.1 leaves "counter signature" and
  "CounterSignature0" pointing at RFC 8152. Endorsing somebody else's signed
  statement — the primitive nearest to what we want — is therefore RFC 9338's
  subject, not this document's.
- **§9 is much narrower than "deterministic COSE".** Its restrictions apply
  *only* to encoding `Sig_structure`, `Enc_structure` and `MAC_structure`:
  definite lengths, minimum-length arguments, no duplicate labels. Nothing
  constrains how the transmitted array or the unprotected map is encoded, and no
  map-key ordering is required anywhere. A COSE object is not a deterministic
  encoding; only its to-be-signed byte string is, in two properties. Any
  requirement for byte-stable COSE objects is ours to add.
- **The CDDL is informational; the prose is normative** (§1.4, stated outright,
  because CDDL was unpublished when COSE was written). Our `schema/` extraction
  must therefore mark the CDDL as transcribed-not-authoritative, and any
  disagreement between grammar and prose resolves to the prose.
- **It profiles nothing.** §10 defers to the application which messages are
  used, which algorithms are mandatory, how algorithms are negotiated or
  discovered, and how `external_aad` is constructed; §4.3 lists the injectivity,
  ordering and stability hazards of `external_aad` without defining a
  construction. §12 adds that COSE provides no padding, so message length leaks.
  A specification that says only "sign it with COSE" has specified nothing.
- **Thin BCP 14 surface.** The whole document contains 53 BCP 14 keyword
  occurrences, and Appendix A deliberately uses none ("This specification can
  provide recommendations, but it cannot enforce them"). Much of the behaviour
  an implementer needs is prose without RFC 2119 force, which is why
  `normative.md` will under-represent the document unless `kind: implied` rows
  are used generously.

**Read scope.** Read closely: §1–§9 in full (including §1.4–§1.6 terminology,
every structure definition, §4.4, §5.3–§5.4, §6.3, and §9), §10–§12 in full,
§13 references, Appendix A in full, Appendix B's layering argument and its
triple-layer example, Appendix C's preamble, C.1, and C.7.1–C.7.2. **Not** read
line by line: the example bodies of C.2 through C.6 (the enveloped, encrypted
and MACed fixtures) — those are precisely the bytes `distilled/examples/` needs,
so they must be read before any fixture is committed. Also not done: no
intermediate value in Appendix C was recomputed, and §8.5's recipient-class
rules were not cross-checked against the algorithm definitions in RFC 9053.

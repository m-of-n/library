---
schema: "library-summary/v1"
id: in-toto-attestation-v1
record: in-toto-attestation-v1
type: summary
updated: "2026-10-23"
---

# in-toto Attestation Framework v1

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset._ A versioned specification of a CNCF project, not an SDO document; it has no ratification step that maps to RFC 2026, and the repo README's *Disclaimer* says the framework "is still under development". Left unset rather than guessed. |
| **Authors** | No byline in the spec. Maintainers at the tag (`MAINTAINERS.md`): Aditya Sirish A Yelgundhalli (Bloomberg), Adolfo Garcia Veytia (Carabiner Systems), Marcela Melara (Intel), Parth Patel (Kusari). Release published by `marcelamelara` |
| **Published** | 2026-03-18 — release `v1.2.0`; `spec/v1/README.md` declares "Version: v1.2" |
| **Identifier** | https://github.com/in-toto/attestation/tree/v1.2.0/spec/v1 — lightweight tag `v1.2.0` → commit `df02077bf97218a8860a5c534eff1f1381f56984`; Statement type `https://in-toto.io/Statement/v1` |
| **Source** | https://codeload.github.com/in-toto/attestation/tar.gz/df02077bf97218a8860a5c534eff1f1381f56984 |
| **Digest** | `c66cbb44b115cd0745e0f22dfedb069729a081a7f56372e3fca8ead667795d91` (sha256 of the source archive at the commit; retrieved 2026-10-23) |

**Digest convention.** A specification spread over several files has no single
digest. `content.sha256` is the sha256 of the GitHub source archive *at the
commit* the tag names — the same convention as `secure-systems-lab-dsse`.
GitHub does not guarantee archive bytes stay stable, so the commit id is the
durable pin, and the per-file sha256 of what was read (from that archive) is:

| File (at `df02077`) | sha256 |
|---|---|
| `spec/v1/README.md` | `2c1b2b94b23a10783f7c3a7f69e092f1dd704f1bb9b54e0c36174612ec5653c3` |
| `spec/v1/statement.md` | `cbe684a18b812b8b613d9202eb43b2ea24477f91a2ad6ca5be935185a455ebea` |
| `spec/v1/resource_descriptor.md` | `bee71bedd6a957771233cbbe6494144157b865992e53cc91d607a8e02a34c58a` |
| `spec/v1/digest_set.md` | `0b1889fdea7f6d623b41555632aedf04ee4398cf02a32002060608c75ebb038e` |
| `spec/v1/field_types.md` | `7c14b278a5d14191b7284bac3b05565b91940ca619fedd5f08f3a3498e9a37aa` |
| `spec/v1/predicate.md` | `e8bbe65af30d7a94ed9c5eabd698cf3781ca5bbb66377a584eed8e64d52d0a99` |
| `spec/v1/envelope.md` | `c02c65880ccc117bbdecc6c916d5108541c1a864de67f8f9082efbaf15265d11` |
| `spec/v1/bundle.md` | `e90a4419c8913f91ad8ec34ce810404130400faf8f22866607c5083bcacee690` |
| `spec/v1/CHANGELOG.md` | `de802e332c58f6e1617738ac7c7035e1746607dbaedfa91d3538ebff19c1451e` |
| `spec/versioning.md` | `623a7446e6584bc09496832902aca44dda3eec46381f6b44410966aa3b53b7fc` |
| `docs/validation.md` | `dfd52035ca5e08557c113465237b723c24f52c7258516a68b73515cf9bdfbab4` |

**Versions fold into this record** (`docs/scope.md` §4–§5): the line is
`Statement/v1`; minor releases do not change the type URI (`spec/versioning.md`).
`spec/v1/CHANGELOG.md`: v1 initial; v1.1 subjects assumed immutable and
non-cryptographic digests acceptable; v1.2 `payloadType` widened to
`application/vnd.in-toto.<predicate>+json`. The v1.2.0 release notes add that
non-cryptographic digests may use a custom value encoding (PR #517, now in
`digest_set.md`). On 2026-10-23 `main` was 76 commits ahead of the tag with
**no change** under `spec/v1/` or to `docs/validation.md`.

## Overview

The Attestation Framework defines a signed claim about software artifacts in
three layers (`spec/v1/README.md`): an **Envelope** that authenticates bytes
(DSSE RECOMMENDED), a fixed-schema **Statement** that binds the claim to a set
of digest-identified subjects and names its type, and an open-schema
**Predicate** carrying the type-specific content. The argument
(`docs/background.md`, *Reasons for separate Statement and Predicate layers*)
is that a policy engine can then answer "does an attestation exist that is
signed by X having predicate type T, with subject Y/Z?" and look attestations up by subject without predicate-specific
logic — so `subject` and `predicateType` are fixed and `predicate` is not.
Evolution rests on a **monotonic principle** — ignoring an attestation or a
field must never turn DENY into ALLOW — which is why consumers *ignore* rather
than reject what they do not recognise (README §Parsing rules). It deliberately
defines no signing construction, no canonicalisation, no key model and no
threshold: those are the envelope's and the policy engine's. Supply-chain
**layouts** are not part of it; they belong to the in-toto specification (item
8 below).

## What this record answers — the R-0006 ∅ cells

mofn `research/0006-mechanism/unverified.md` §4 lists in-toto's own `DigestSet`
specification and the layout verification procedure as ∅, and `report.md` §2.2
took the Statement fields second-hand from `slsa-1-2`. Locators are at
`df02077`.

1. **Statement** (`spec/v1/statement.md` §Schema, §Fields). A JSON object with
   `_type` (TypeURI, required, always `https://in-toto.io/Statement/v1`),
   `subject` (array of ResourceDescriptor, required), `predicateType`
   (TypeURI, required) and `predicate` (object, optional; "Unset is treated the
   same as set-but-empty"). On `subject`, §Fields: "Each element MUST have
   `digest` set"; it is a "Set of software artifacts"; `name` and `uri` SHOULD
   be unique within it; and an IMPORTANT note that subjects are "matched purely
   by digest, regardless of content type". R-0006 §2.2's field list is
   **confirmed against the primary source**.
2. **ResourceDescriptor** (`spec/v1/resource_descriptor.md`). Seven optional
   fields — `name`, `uri`, `digest`, `content`, `downloadLocation`,
   `mediaType`, `annotations` — with a minimum of one of `uri`, `digest` or
   `content` that a context may add to but not override (§Fields). §Semantics:
   a descriptor with a `digest` is assumed immutable, and which field the
   digest is matched against is decided by the predicate type.
3. **DigestSet** (`spec/v1/digest_set.md`) — the ∅ cell, now filled.
   *Shape* (§Fields): a JSON object mapping algorithm name to a string encoding
   of the digest; usually one pair, several MAY be used for agility. *Names and
   encoding* (§Supported algorithms): `sha256` … `md5` use the NIST names
   lowercased with `-`→`_` and lowercase hex values; `dirHash` (Go `h1:`
   dirhash, rendered in hex); `gitCommit`/`gitTree`/`gitBlob`/`gitTag` (40-char
   SHA-1 or 64-char SHA-256 git object id, with the hashed framing spelled out).
   *Immutability* (§Fields): every entry MUST be an immutable reference; a
   cryptographically secure digest is STRONGLY RECOMMENDED. *Non-cryptographic
   digest types* (§*Use cases for non-cryptographic, immutable, digests*):
   allowed when "the risk of the object being mutated is acceptable for the
   application", example a cloud VM image id; "the value encoding for
   non-cryptographic digests is identifier-specific" (the v1.2 change);
   §Examples shows `{"arn": "arn:aws:ec2:…"}`. *Consumer rules* (§Guidelines):
   "Consumers MUST only accept algorithms that they consider secure and MUST
   ignore unrecognized or unaccepted algorithms"; new algorithms MUST document
   their value encoding. *Matching* (§Guidelines): "Two DigestSets SHOULD be
   considered matching if ANY acceptable field matches", with one matching and
   one non-matching pair in §Examples.
4. **How a Statement is wrapped** (`spec/v1/envelope.md`). §Schema: DSSE v1.0
   is RECOMMENDED; any other envelope must meet ITE-5, whose list includes
   "SHOULD avoid depending on canonicalization for security".
   §Alternative Envelope schemas: `COSE_Sign` is ITE-5 compliant; the Sigstore
   Bundle and `COSE_Sign1` are not, each being limited to a single signature.
   §Fields: `payloadType` MUST be signed with the payload; with DSSE it MUST be
   `application/vnd.in-toto+json` or `application/vnd.in-toto.<predicate>+json`;
   "`payload` MUST be a base64-encoded JSON [Statement]."
5. **What is signed.** This spec defines no signing input. The DSSE
   construction — `PAE(UTF8(payloadType), SERIALIZED_BODY)` over the
   Statement's serialized bytes — is DSSE's `protocol.md`, held and extracted
   in `secure-systems-lab-dsse`, and not restated here. Nothing in `spec/v1/`
   constrains *how* the Statement JSON is serialized: no canonical form, no
   duplicate-key rule, no I-JSON reference; only the ITE-5 SHOULD above
   addresses canonicalisation. (Grep of `spec/v1/` at the tag for "duplicate",
   "I-JSON", "8259", "unicode": no hits.)
6. **Authenticated type indicator.** Three layers: DSSE `payloadType`
   (authenticated through PAE), the Statement's `_type`, and `predicateType` —
   the last two inside the signed payload. `envelope.md` §Fields tells
   consumers not to trust the media type's predicate part and to "only rely on
   the `predicateType` field in the [Statement] layer", and that they MUST parse
   and verify the payload to obtain authenticated predicate information. For
   condition (4) of R-0006 §3.2: yes, by construction — every type indicator a
   consumer is told to rely on is inside the signed bytes.
7. **Processing model.** Normative: `spec/v1/README.md` §Parsing rules —
   "Consumers MUST ignore unrecognized fields unless otherwise noted in the
   predicate specification"; producers MAY add extension fields, which MUST NOT
   influence the meaning of any other field; major versions live in the
   TypeURI, minor versions follow the monotonic principle. So **reject unknown
   fields? No — ignore them**; likewise `bundle.md` §Data structure (ignore
   unrecognized lines and attestations) and DigestSet (ignore unaccepted
   algorithms). The *validation model* is `docs/validation.md` — pseudocode in
   `docs/`, not `spec/v1/`: decode the envelope (reject on failure); collect
   names of recognized attesters whose signature verifies (reject if none);
   check `payloadType`; decode the Statement and check its type URI; keep the
   subjects with at least one digest under an acceptable algorithm equal to the
   artifact's hash (reject if none); output `predicateType`, `predicate`,
   matched subjects and attester names to a policy engine. It carries a TODO
   for multiple artifacts or attestations and has no threshold. Its defects
   are Limits 1–2.
8. **Layout verification is not in this document.** Layouts, steps,
   thresholds, artifact rules and the verification procedure belong to the
   **in-toto Specification v1.0.0** (`in-toto/docs`, tag `v1.0`, dated "Jun 02,
   2023"): step `threshold` §4.3.1, artifact-rule processing §4.3.3.1,
   *Verifying the final product* §5.2; its §4.2.3 hash object is DigestSet's
   ancestor, and §4.1 used canonical JSON for digests of metadata objects while
   stating implementations "are not required to use this flavor of CJSON". The
   Attestation Framework links that document only for KEYID and functionaries
   (`envelope.md`). The bridge is the Link predicate: `spec/predicates/link.md`
   says that for every step in the layout "one (or more, depending on the
   threshold) signed link attestations must be presented", and defers the rest
   to the in-toto spec. `in-toto-2019` is the USENIX paper, not that
   specification, and **no library record holds the in-toto Specification** —
   the cell stays ∅ in this library until one is ingested; it is named in
   `cites` so it reaches the frontier. (Fetched only to locate these sections:
   sha256 `17d3326e4cf58234619dbfe821cdc5187e55e2c89f7b63f03699c46588322097`,
   raw `in-toto-spec.md` at tag `v1.0`; not read critically.)

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Defines what a consumer of a signed supply-chain claim must check and what it may ignore. |
| Cryptography | adjacent | No algorithm or signing construction of its own — delegated to DSSE / ITE-5; DigestSet sets hash-algorithm acceptance rules. |
| This project | core | One of the two R-I-03 export targets. |

Bears on **R-I-03** (export to in-toto Statement + DSSE — this is the primary
source for that target); **R-I-01** (the §6 in-toto row says *"predicate_type
preserved"*; items 3, 6 and 7 are the material losses); **R-M-07** (Statement
`subject` MUST carry a digest, so R-M-07 is met *in form* — but a DigestSet may
hold a non-cryptographic, non-hex identifier); **R-M-11** (proposed in
ARCH-0001-PROPOSAL v0.2.0, not yet in ARCH-0001 v0.1.2 — ResourceDescriptor's
`uri` / `digest` / `content` minimum is a close relative of R-M-11's
locator / digest / description modes, with the digest required where the
descriptor is a Statement subject); **R-M-12** (`field_types.md` §TypeURI:
"TypeURIs are not registered. The natural namespacing of URIs is sufficient to
prevent collisions." — registry-free but DNS-relative, not key-relative, so the
R-M-12 mapping at this boundary is lossy, as R-M-12 anticipates); **R-O-05**
(proposed; the in-toto half of the sign-bytes, canonicalise-nothing position).

**Corrections to mofn R-0006 against the primary source.** (a) §2.2's "digest
map, algorithm → hex" holds only for the named algorithms; since v1.2
non-cryptographic entries use an identifier-specific encoding
(`digest_set.md`). (b) §2.3 "Fourth" follows its non-cryptographic-digest sentence with
`gitCommit` as the entry that satisfies R-M-07 "in form and not in substance",
readable as treating it as non-cryptographic. in-toto does not class it so: `gitCommit` is a SHA-1
or SHA-256 git object id over a defined framing (§Supported algorithms); the
spec's own non-cryptographic examples are cloud image ids such as `arn`. The
R-M-07 point survives and is stronger with the right example — an `arn:` entry
binds no content at all; `gitCommit` under SHA-1 is a *collision-weakened*
digest, a different problem. An import must still name its acceptable
algorithms, as §2.5 says. (c) §2.2's verification column cites DSSE for
"Reject if PAYLOAD_TYPE is not a supported type"; in-toto's own corresponding
check is the `docs/validation.md` step, which as written rejects everything
(Limit 1).

Against the six conditions of R-0006 §3.2: (1) not addressed. (2) **inverted**
— unknown fields are ignored and there is no canonical form to reject against.
(3) met by avoiding canonicalisation (ITE-5 SHOULD). (4) met (item 6). (5) not
met — `subject` is called a set and carried in an array with no defined order;
`bundle.md` likewise says processing "MUST NOT depend on the order of the
attestations". (6) partly — `field_types.md` §ResourceURI and §TypeURI carry a
case-normalisation MUST (scheme and authority lowercase, RFC 3986 §6.2.2.1);
no Unicode rule and no consumer-side rejection.

## Implementations

Searched 2026-10-23. Licences from each repo's GitHub licence metadata; where
GitHub reports `NOASSERTION` (in-toto/attestation, in-toto-golang, in-toto) the
`LICENSE` file was read and carries Apache 2.0 text.

| Name | Kind | License | URL |
|---|---|---|---|
| in-toto/attestation bindings (Go, Python, Rust, Java) | library | Apache-2.0 | https://github.com/in-toto/attestation |
| in-toto-golang | library / CLI | Apache-2.0 | https://github.com/in-toto/in-toto-golang |
| in-toto (python, reference; `in-toto-verify`) | library / CLI | Apache-2.0 | https://github.com/in-toto/in-toto |
| cosign | CLI (Sigstore) | Apache-2.0 | https://github.com/sigstore/cosign |
| witness | CLI | Apache-2.0 | https://github.com/in-toto/witness |

GUAC ingests in-toto attestations but has its own record (`guac`, held as
`see_also`). slsa-verifier is not listed: its README does not say in-toto in
terms, and it is covered under `slsa-1-2`. in-toto-rs and in-toto-java (both
MIT) were not checked for attestation v1 coverage. No commercial product
assessed; they exist and none was checked.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata — pinned source, per-file read list in `content.note`, cites, relations |
| `summary.md` | this document |

**No `distilled/`, no `distillation` block.** library#87 is this pass and it
claims the **summary bar**: the record is `summarized`, declares no
`distillation`, and adds no file under `distilled/`, so FX-1 does not fire. The
record is type `spec`, so it **owes an FX-1 extraction** when one is taken on —
owned by library#89. That extraction would produce
`normative.md` / `requirements.yaml` over `spec/v1/*.md` and
`spec/versioning.md` (BCP 14 keywords plus the non-BCP "STRONGLY RECOMMENDED"
in `digest_set.md`), `schema/` from `protos/` and the jsonc schemas,
`examples/` from the DigestSet and ResourceDescriptor examples, and a
`protocol.yaml` of the `docs/validation.md` model with its defects recorded.

**No verbatim normative text beyond short locator-bearing fragments** — under
FX-1 it belongs in `distilled/normative.md`.

**`in-toto-envelope-v1` is the same text as this record's
`spec/v1/envelope.md`**, held as a separate stub at the unpinned `main` URL.
Not touched by this pass; it is a candidate for `part_of:
in-toto-attestation-v1` or `duplicate_of`, for whoever owns that record.

## Limits

1. **`docs/validation.md`'s payload-type check is unsatisfiable as written.**
   It reads "Reject if (`envelope.payloadType` != `application/vnd.in-toto+json`
   OR `envelope.payloadType` does not match
   `application/vnd.in-toto.<predicate>+json`)" — no value both equals the
   first and matches the second, so the OR should be an AND. The next step
   tests `statement.type`; the field is `_type`. The model is also
   non-normative in placement (`docs/`, not `spec/`), ends in a TODO, and treats
   any one verifying recognized key as sufficient — no `k`-of-`n`, which is
   left to "a policy engine". A consumer building from this page alone has no
   normative verification procedure.
2. **Envelope requirements disagree inside `envelope.md`.** §Schema's ITE-5
   list makes an authenticated payload type a SHOULD; §Fields makes
   "`payloadType` (or equivalent) MUST be signed". §Fields' general rule
   requires the form `application/vnd.in-toto+<encoding>`, while its
   DSSE-specific rule (v1.2) also allows
   `application/vnd.in-toto.<predicate>+json`, which does not take that form.
   For R-I-03 export, the safe reading is the stricter one in each case.
3. **DigestSet matching is ANY-of.** Two sets "match" if any acceptable
   algorithm agrees; nothing addresses a pair where one acceptable algorithm
   agrees and another acceptable algorithm *disagrees*, so the weakest accepted
   algorithm decides. Internal inconsistency: the §Supported algorithms heading
   names `dirHash`, but its worked example emits the key `dirHash1`.
4. **The bindings do not implement the spec text exactly** (checked at the
   tag). `go/v1/statement.go` `Validate()` and the Python `statement.py`
   `validate()` both reject a Statement with no `predicate`, which
   `statement.md` makes optional; the Go one also accepts
   `https://in-toto.io/Statement/v0.1`, the Python one does not.
   `go/v1/resource_descriptor.go` accepts a descriptor with `name` alone and
   does not count `content` — the spec's minimum is `uri` / `digest` /
   `content`. It decodes digests with Go's `hex.DecodeString`, which accepts
   upper-case hex where the spec says lowercase. Interop claims should name
   the implementation, not "in-toto".
5. **The JSON byte layer is unspecified.** DSSE makes that safe for
   *verification* (bytes are verified, never re-encoded), but anything that
   derives an identifier from a Statement has no canonical form to rely on —
   the R-0006 Group B gap, which in-toto neither closes nor claims to.
6. **Trust placement is out of scope.** `recognizedAttesters` is an input to
   the validation model; who may attest which `predicateType` is not expressed
   in any signed structure here. For layouts it is the project owner's key
   (in-toto Specification §5.2 step 1), which this library does not yet hold.

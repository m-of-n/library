---
record: rfc-9052
kind: index
title: "rfc-9052 — distilled artifacts"
extracted: "2026-09-30"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). Extracted from `.cache/rfc-9052.txt`, whose
sha-256 matches `content.sha256` in `record.yaml` (`01eecd7f6465…`), so every
locator below resolves against the exact bytes this record commits to.

**Read this first:** RFC 9052 §1.4 states that CDDL "could not be used as the
data description language to normatively describe the CBOR data structures
employed by COSE. For that reason, the CBOR data objects defined here are
described in prose." **The CDDL in this record is therefore informative and the
prose is normative.** Anything built from `schema/` alone will be
under-constrained.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 245 located statements + 82 verbatim blocks across 47 headings, §1.4–§12 plus Appendices A and B. All 30 CDDL rules in 23 fenced blocks, all five tables (1–5), and the `Sig_structure`/`Enc_structure`/`MAC_structure` field lists and step lists complete. All **53/53** BCP 14 occurrences present. §11.3's three IANA media-type registration templates and §4.1's quoted [RFC5652] passage are reproduced in full. §C examples excluded — they are in `examples/`. |
| requirements | `requirements.yaml` | 99 entries, `rfc-9052#R-0001`…`R-0099`. **53 `stated`** (one BCP 14 keyword each) + **46 `inferred`** (lowercase-normative prose and the numbered procedures, each declaring in `field` that no BCP 14 keyword backs it). `extracted_keyword_count` 53 = `source_keyword_count` 53, `reconciliation` empty. §10/§11/§12 contain zero BCP 14 keywords and Appendix A says outright that they are "deliberately not used" there. `R-0099` was added by the cross-check pass: §8.5.2's "Failing to decrypt that specific recipient is an acceptable way of dealing with it. Failing to process the message is not" is the consequence half of `R-0074` and existed only inside `protocol.yaml`'s `on_error` text. It carries no BCP 14 keyword, so the keyword reconciliation is unaffected. |
| schema | `schema/` | `cose.cddl` — all 24 fragments / 30 rules **verbatim** in source order, each marked with its section; every non-comment line verified byte-for-byte against the source. `structures.derived.cddl` — 14 rules, standalone-closed, covering `COSE_Sign1`, `Sig_structure`, `COSE_Key`, plus a derived `Sig_structure_strict` encoding §4.4's prose that the source's own CDDL does not enforce. Every constraint in `Sig_structure_strict` and its two arms now cites the requirement id it traces to, line by line (`R-0034`…`R-0040`); the cross-check confirmed it asserts nothing the §4.4 prose does not. Dangling value spaces (`alg`, `kty`, content type, `crit` entries) are marked `; DANGLING:` and delegate to RFC 9053 and the IANA registries — re-verified against §11, which only re-points registry references from RFC 8152 and defines no value. Not run through a CDDL parser — none installed here; the subset the fixtures exercise was checked by a purpose-written validator instead. |
| messages | `messages.yaml` | 25 structures: all six message types with their tags, both header buckets, `header_map`, `empty_or_serialized_map`, `Generic_Headers` (labels 1–6), `COSE_Key`/`COSE_KeySet`, the three `*_structure` forms, the three derived byte strings they encode to (`ToBeSigned`, `ToBeMaced`, `AAD` — added by the cross-check pass, because `protocol.yaml` names all three in 14 steps and `messages.yaml` defined none of them), and §9's encoding restrictions. Records the traps: `COSE_Mac` puts `tag` at index 3 **before** `recipients`; `Sig_structure`'s `sign_protected` is omitted for `COSE_Sign1`, shifting `external_aad` and `payload`; empty protected is `h''` (SHOULD) with `h'a0'`-in-a-bstr MUST-accept. **`constrained_by` is populated: 63 of the 74 fields carry at least one requirement id, 11 carry none** — see limits for which and why. |
| protocol | `protocol.yaml`, `protocol.md` | 11 flows / 81 steps, all `kind: local-procedure` — **RFC 9052 defines no wire protocol**; §1.4's `Internal_Types` are "used for security computations but are not emitted for transport". Roles: signer, verifier, sender, recipient, application (each a term the source uses). One Mermaid sequence diagram per flow. **51 of 81 steps have `on_error: unspecified in this document`** — the RFC specifies checks, not consequences, and never says what a verifier does when verification fails. Every one of those 51 was adjudicated against all 99 requirements in the cross-check pass; two steps that had been marked unspecified (the AEAD and AE decryption calls) do have a stated consequence in §8.3 and now cite `R-0066`. The five mandatory error behaviours in the document each appear both as a requirement and in the governing step's `on_error`, with the id cited. See `design-notes.md` S1 for what this costs a verifier. |
| examples | `examples/` | **17 complete tagged COSE messages** as `fixtures/*.diag` (§B triple-layer, §C.1.1–C.1.3, §C.2.1, §C.3.1–C.3.3, §C.4.1–C.4.2, §C.5.1–C.5.4, §C.6.1, §C.7.1–C.7.2), in RFC 8610 extended diagnostic notation, with §C.7 supplying full public **and private** key material. Plus 6 partial fragments. All 17 re-encode to exactly the byte count the RFC declares, and all 22 inline `protected h'…'` annotations reproduce byte-for-byte. `hex` is empty throughout: the source gives no hex dumps, so computed bytes sit in a labelled `derived_hex`. **No populated `Sig_structure` instance and no ToBeSigned byte string exists anywhere in the document** — the signing-input construction cannot be tested from this source alone. Defers to `cose-wg/Examples` @ 3221310 (2020-06-03), which is outside RFC change control. The cross-check pass validated all 17 fixtures structurally against `cose.cddl` and against their `messages.yaml` entry (element count, order, which bucket is a `bstr`): **zero findings**, all 17 sizes equal the declared byte count, all 17 `derived_hex` values reproduce. `examples/README.md` now carries the gap list — 8 of 25 structures, 25 of 74 fields and 23 of 85 `testable: yes` requirements that no fixture reaches. |
| design-notes | `design-notes.md` | Adopt / adapt / reject against ARCH-0001, ARCH-0002 P1/P5/P6, ADR-0001 and **D-3**, with a field-by-field export mapping to `COSE_Sign1`, 12 pinned determinism items for the Oct 28 D5 package, and 11 open questions with owners. Every inference itemised in a closing table. |

## Declared not applicable

| kind | reason |
|---|---|
| state-machine | COSE is a single-shot object format, not a role-based protocol with a lifecycle: no states persist between messages, and the only ordered processes are the per-message procedures captured in `protocol.yaml`. §7 key objects are structure plus rules with no ordered steps. |

## Findings that bear on our design

Recorded here because they are conclusions about the source, not extraction notes:

- **The signature does not port.** `Sig_structure` is not our canonical byte
  sequence, and there is no unsigned `COSE_Sign1`, so an export must either
  re-sign with the speaking key or wrap with an exporter key. A consumer tells
  the two apart by *which key verifies*, so neither needs a new header
  parameter. Which one we choose is open and blocks the D5 fixture package.
- **`(defining key, label)` is inexpressible as a COSE label.** §1.5 fixes
  `label = int / tstr`. This is a structural bar, not merely a registry
  objection — stronger than the R-M-12 argument alone.
- **§9 scopes determinism to the `*_structure` encodings only**, not the
  transmitted object, and mandates no map-key ordering. "Deterministic COSE" is
  not a settled thing; our native rule is strictly stronger, so export→import
  is not byte-stable without our own sort.
- **ES256 is not byte-reproducible** (randomised ECDSA), so the primary D5
  fixture should be Ed25519.
- **Note for ARCH-0001:** the §3.2 comparison table row for CWT claims cites
  RFC 8392 for "COSE protected header 15". Label 15 is real but is registered by
  **RFC 9597** (§2, "CWT Claims"), which this library already holds as
  `rfc-9597`. The row should cite it. The label number is correct.

## Known limits of this extraction

- **`constrained_by` in `messages.yaml` is populated** — this was the deliverable
  of the cross-check pass and the limit is now a narrower one. 63 of 74 fields
  carry at least one requirement id; every id resolves (checked, zero dangling
  references). The linking rule applied was: *a requirement is linked to every
  field whose value, presence or encoding it constrains, in every structure where
  that field occurs.* **11 fields carry no link**, and in each case the source
  states no requirement about them: `COSE_message_identification`'s "by context",
  "by CBOR tag" and "CoAP Content-Format" rows; `COSE_Key`'s `key_ops`;
  `COSE_Mac`'s and `COSE_Mac0`'s `payload`; and `Enc_structure`'s and
  `MAC_structure`'s `context`, `protected` and `payload`. The last two groups are
  our own coverage gap rather than the source's: §5.3's and §6.3's numbered field
  lists carry the same kind of prose that §4.4's does, and §4.4's became
  `R-0034`…`R-0039` while §5.3's and §6.3's did not. §6.1 likewise repeats §4.1's
  detached-payload sentence verbatim and only §4.1's became a requirement
  (`R-0031`). Those seven or eight further `inferred` entries are a requirements
  job, deliberately not done here, and `normative.md` carries all of the prose
  under §5.3, §6.1 and §6.3 meanwhile.
- **10 of the 99 requirements are referenced by no field**, and all ten are
  legitimately field-free: `R-0001` (the CDDL is informational, a statement about
  the document); `R-0042`, `R-0044`, `R-0049` and `R-0051` (procedure steps that
  describe a *call* — the arguments passed to an algorithm — which
  `protocol.yaml` models and no field holds); `R-0045` and `R-0097` (trust and
  authorization decisions left to the application); `R-0093` (that a profile
  ought to exist); `R-0094` (IANA registration process); and `R-0098` (that
  applications document content padding, for which COSE defines no mechanism).
  Stated rather than papered over: nothing was linked to make the number look
  better.
- **`structures.derived.cddl` is unvalidated by a real parser.** No CDDL tool is
  installed here. The cross-check pass wrote a diagnostic-notation reader, a
  deterministic CBOR encoder and a hand-transcribed validator for the `cose.cddl`
  subset the 17 fixtures exercise, and all 17 pass — but that validator is not a
  CDDL implementation and does not check the rules no fixture reaches
  (`Sig_structure`, `Enc_structure`, `MAC_structure`, `Sig_structure_strict`).
- **Five source discrepancies recorded, not fixed:** §C.5.4 prose says "128-bit
  key" while `alg` 5 is HMAC 256//256; §C.3.3 writes a recipient protected
  bucket as literal `h'a101381f'` with backslash-delimited comments instead of
  `<< {…} >>` (bytes are unaffected in both cases); §8.5.1–§8.5.5 spell the
  recipient structure `COSE_Recipient` while its own CDDL rule is
  `COSE_recipient`; §3.1's Table 3 types `content type` as `uint` while the CDDL
  in the same section types it `int`; and the document states checks without
  consequences in 51 of 81 procedure steps. The last three are written up in
  `design-notes.md` as S1–S3.

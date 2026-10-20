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

**State: all three passes complete, `distillation.profile: full`.** Extract
(2026-10-19, two parallel agents), verify (2026-10-20, one adversarial agent,
independent) and cross-check (2026-10-20, a third agent that did neither of the
first two), each at effort max, each reading only `.cache/rfc-9964.txt`. No
human has reviewed any of it — every `reviewed_by` in this directory is empty,
deliberately, so the artifacts are readable and citable but not buildable-on.

RFC 9964 is a short document with one load-bearing section. **§6 answers a
question RFC 9679 §4.6 asks and declines to answer** — which parameters are
required for an AKP COSE Key Thumbprint — and `records/ietf/rfc-9679` is at
`profile: full` with that dependency recorded. This extraction's job was to make
the consequence measurable rather than argued. It is.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | every normative sentence of §3–§7 with its locator. **Written by the parallel pass-1 agent**, which owns it together with `requirements.yaml`; not described further here. |
| requirements | `requirements.yaml` | every BCP 14 requirement with reconciled keyword counts. **Parallel pass-1 agent.** |
| schema | `schema/` | **RFC 9964 ships no grammar of any kind** — `CDDL`, `ABNF`, `ASN.1` and `JSON Schema` each occur zero times. One verbatim file carries the four places the document renders a structure itself (Figures 1 and 2, Table 1, §6's bullet lists); the other five are the library's own and carry `.derived.`. 45 CDDL rules across three files (a per-file sum: **36 distinct** names, nine of them defined in two files and byte-identical in both), two JSON artifacts. Does **not** constrain map order, encoding determinism, key validity, `pub`/`priv` agreement, or `ctx`. `schema/README.md` has the per-file table. |
| messages | `messages.yaml` | 9 structures, 36 fields, with the actual code points and octet-level layouts: the AKP and ML-DSA `COSE_Key`, **both §6 thumbprint inputs**, the JWK, the tag-18 `COSE_Sign1`, the `Sig_structure`, the header parameters and the JWS. `constrained_by` **is wired**, by the cross-check pass: 25 of the 36 fields carry at least one `rfc-9964#R-NNNN`, 66 of the 88 requirements are cited, and the 11 empty lists are a finding rather than an omission — every one of those fields belongs to RFC 9052, RFC 7515 or RFC 7517, not to this document. Pass 1 left the key out deliberately (the ids belonged to a parallel agent and R-O-03 forbids guessing them) and carried `locator` on every field so a later pass could add them mechanically; the file's header records that and the matching rule used. |
| protocol | `protocol.yaml`, `protocol.md` | **NOT APPLICABLE, with the measurement written out** — they were unedited ingest scaffold until the verify pass replaced them with real statements, and the cross-check pass re-measured every count in them from the source. RFC 9964 defines no protocol: `verifier`, `sender`, `recipient`, `protocol` and `exchange` each occur **zero** times, `signer` once (in a §7.1 sentence about impersonation) and `request` once (the RFC masthead). §5 defers the envelope outright: "When producing COSE signatures, no encoding is needed; see Section 4 of [RFC9052] for more details on how COSE signatures are created." The signing protocol is RFC 9052's; see `records/ietf/rfc-9052`. |
| state-machine | `state-machine.yaml` | **NOT APPLICABLE, with the measurement written out** — same history as `protocol.yaml`, same re-measurement at cross-check. `state`, `lifecycle`, `revoke` and `revocation` each occur **zero** times. The only ordered procedure is §7.3's key validation (seed length check, then `pkDecode`/`skDecode` range checks) and it is a precondition list, not a lifecycle: no states, no transitions, no terminal condition. |
| examples | `examples/` | **12 vectors, and the document prints real cryptographic test vectors** — six complete worked examples (Appendix A, Figures 3–8) with real FIPS 204 keys of 1312/1952/2592 octets, real signatures of 2420/3309/4627 octets, the exact signed bytes, and `kid` values that all six reproduce. Plus the hazard fixture: three `KeyId`s from one byte-identical `pub`, one leg printed by the RFC itself. These are the library's **first post-quantum fixtures**. **All six signatures verify cryptographically and all six public keys re-derive from the all-zeros seed** — closed by the verify pass with a FIPS 204 implementation gated on 75/75 ACVP keyGen and 90/90 ACVP sigVer vectors. |
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

Three 1322-octet inputs differing in **one octet** (offset 5: `2f`, `30`, `31`);
three digests sharing no prefix. Under `ARCH-0002` P1 (accepted by `ADR-0001`) a
post-quantum parameter change is therefore a **namespace rename**, not a
re-signing.

## Verification

**Pass 1.** A CBOR encoder/decoder written for that pass (RFC 8949 §4.2.1) plus
`hashlib.sha256`. **No CBOR, COSE, JOSE or JWT library was used.** All three
COSE Key Thumbprints and all three JWK Thumbprints reproduce the printed `kid`
values exactly; `vectors.yaml` round-trips through the library's own YAML reader
under 121 re-derived assertions with zero failures; 45 CDDL rules close with no
undefined reference and no prelude collision (45 is the per-file sum; 36 distinct
names — re-derived at pass 3, see `schema/README.md`). Details in
`schema/README.md` and `examples/README.md`.

**Pass 2 (verify), re-derived independently rather than re-read.** A *second*
CBOR codec, written from RFC 8949 without reference to pass 1's:

- **All six thumbprints reproduce again** — three COSE Key Thumbprints as
  `sha256(enc({1:7, 3:alg, -1:pub}))` over inputs of 1322 / 1962 / 2602 octets,
  three JWK Thumbprints over inputs of 1790 / 2643 / 3496 octets.
- **The hazard fixture reproduces**, including both computed legs, and neither
  computed digest occurs anywhere in the source. One correction: the three
  inputs differ in **one** octet, not two (see below).
- **The signature gap is closed.** FIPS 204 `KeyGen_internal` and
  `Verify_internal`, implemented for this pass and **gated on NIST ACVP known
  answers before being used** (75/75 keyGen, 90/90 sigVer of which 72
  expected-reject): all six printed public keys re-derive from the all-zeros
  seed and all six printed signatures verify.
- **88/88 requirement texts** are contiguous substrings of the
  whitespace-normalised source and **88/88 locators** resolve inside their
  stated section; **79/79** `normative.md` quotations likewise; **18/18** fences
  are byte-exact runs of source lines. The 9 BCP 14 keywords each map to exactly
  one `stated` entry, and **none of the 9 is in §6 or §8**.

## Corrections made by the verify pass

One, and it is a byte-level claim rather than a judgement. The hazard fixture's
three thumbprint inputs were described as differing in "**two octets**,
`382f`/`3830`/`3831` at offset 4". They differ in **one** octet, at offset 5:
`0x38` at offset 4 is the shared major-type-1 one-byte-argument head of all
three `alg` values. The finding is thereby **stronger** — a single octet of
algorithm identifier relocates the whole digest. Corrected in place in
`design-notes.md`, `examples/README.md` and above, with the falsified wording
recorded rather than silently replaced.

## Corrections made by later maintenance

**2026-10-20, a maintenance pass (library#39 Tier 2), prompted by
`records/ietf/rfc-8778`.** Two judgements in `design-notes.md`, both **narrowed,
neither deleted**; no file was added to this directory, no pass was recorded and
no `profile` is claimed by it.

1. **§2 item 2's option-1 immunity claim was AKP-specific and stated as
   general.** It read "A raw `pub` is `alg`-independent, so `DEC-003` option 1
   is immune to this hazard". True for AKP, where FIPS 204's public key carries
   no code point and the parameter set shows only in its length. **False for
   HSS-LMS**, whose `pub` *begins* with two parameter-registry code points
   (RFC 8778 §2.2, `u32str(lms_algorithm_type) || u32str(otstype)`). The
   immunity is a property of a key type's public-key encoding, not of option 1.
   **The record's general proposition is strengthened by this, not weakened** —
   for HSS-LMS the allocation sits in the key material, where no digest-input
   choice removes it, so registry-independence now fails on two independent
   instances by two different mechanisms.
2. **Cut B's labels-against-values distinction from `rfc-9679`'s Cut A does not
   hold, and Cut B NARROWS rather than fails.** RFC 9679 §4 requires the IANA
   `kty` **value** for every key type, so every COSE Key Thumbprint already
   contains a digest-changing allocation; Cut A's own text names that registry
   first. The surviving distinction is coarse-and-constant (`kty`) against
   fine-and-varying (`alg`, varying over identical key material). Cut B's
   conclusion survives intact and its `(kty, pub)` escape clause is refuted
   twice over.

Both are written out in place in `design-notes.md` with the falsified wording
quoted, as the verify pass's correction is.

## Corrections made by the cross-check pass

**2026-10-20, pass 3 of 3.** An agent that did neither the extract nor the
verify pass. Nothing it found is a source defect; all six are our own text or
our own completeness. **Nothing earlier was unscoped or withdrawn** — the
verify pass's one-octet-at-offset-5 correction and the maintenance pass's two
narrowings (AKP-scoped option-1 immunity; Cut B narrows) were re-derived and
stand, and the sweep below confirms each reached **every** artifact stating it.

1. **`constrained_by` was missing from all 36 fields of `messages.yaml`**, which
   `docs/extraction.md` specifies the messages artifact as carrying. Pass 1
   deferred it correctly and in terms; a `profile: full` record cannot ship
   without it. Now wired: 25 fields carry ids, 66 of 88 requirements are cited,
   0 dangling, and the file states the matching rule, the coverage and the 22
   unwired requirements with a reason for each.
2. **Six elision counts in `vectors.yaml` were each one too high** (2632/4839,
   3912/6617, 5192/9253 → 2631/4838, 3911/6616, 5191/9252). Measured: each
   rendering keeps the printed diagnostic's first 91 and last 70 characters, so
   the marker replaces `len(printed) − 161`. "The elision marker states the
   character count removed" is the whole content of that convention, so an
   off-by-one falsified it. Also now stated: the space before each retained
   suffix is ours, and `key_diagnostic_elided` is **not** parseable as CBOR
   diagnostic notation because the elided span ends inside the final entry's key.
3. **One 56-octet fixture payload was spelled three different ways across four
   artifacts.** `messages.yaml` had the character U+2019; `vectors.yaml`'s three
   `jws_payload_utf8` fields had the YAML escape `’`, which **neither of
   the library's YAML readers decodes**, so the fixture read back as a
   59-character string with a literal backslash and disagreed with
   `jws_payload_hex` in the same vector; `examples/README.md` and
   `design-notes.md` quoted it with an **ASCII** apostrophe — 54 octets — in
   the same sentence as asserting 56. All five now carry the character.
4. **The rule census was right and one clause of its reason was over-general.**
   45 per-file / 36 distinct / 9 duplicated / all 9 byte-identical all
   re-derive exactly. But "a CDDL file must define every rule it references" is
   the reason for **eight** of the nine: `ml-dsa-alg` is an unreferenced
   entry-point rule in `akp-key.derived.cddl`. Narrowed in `schema/README.md`.
5. **The census correction had not propagated.** `schema/README.md` carried the
   corrected "45 is a per-file sum, 36 distinct"; this file said "45 CDDL rules"
   flatly, twice — the exact wording pass 2 had to fix elsewhere. Both now carry
   the distinct count. This is the failure mode three sibling cross-checks found
   three for three, which is why the whole record was swept for it.
6. **"The word "hash" occurs six times" was falsifiable as written** — a
   word-boundary grep returns **one**. Re-measured: six as a case-insensitive
   substring, five of them inside the single token `HashML-DSA` and the sixth
   the standalone word in RFC 9054's reference title. Count stands,
   characterisation corrected, and the finding is sharper for it.

Two further additions rather than corrections: `design-notes.md` now marks the
`mofn` quotation class (`ARCH-*`, `ADR-0001`, `DEC-00n`, `MD-3`, `R-M/O/I-*`)
as **unverifiable from this standalone repository**, following
`records/ietf/rfc-9741`; and `summary.md`, which said the extraction was "in
progress", now states the artifact set.

## Source defects found

Reported, never repaired. Six, in `design-notes.md`; the two that cost a reader
something are **Figure 2's `pub` prefix differing from the key it illustrates**
(19th hex digit `9` where the key has `f` — **now confirmed against FIPS 204
itself**, since `KeyGen_internal(0^32)` yields `ba71f9f64e11baeb58fa…`, so
Appendix A is right and Figure 2 alone is wrong) and **§6 naming no hash
function** (the string `SHA-256` occurs zero times in RFC 9964 — re-counted;
`SHA256`, `SHA-2` and `sha256` are zero too, and the string `hash` occurs six
times, none of them in §6 — **[correction] 2026-10-20, pass 3 (cross-check):**
this read "the **word** "hash" occurs six times", which a word-boundary grep
falsifies, returning **one**. Re-measured case-insensitively as a substring:
six, of which **five are inside the single token `HashML-DSA`** (lines 61, 301,
303, 305, 307 — §7.2's heading, its ToC entry and its three sentences) and the
sixth is the standalone word in RFC 9054's reference title "Hash Algorithms"
(line 599). So the count stands, the characterisation did not, and the finding
is sharper than it was: **not one of the six is the document choosing a hash
function** — five name the pre-hash variant it refuses and one is a reference
title. SHA-256 is established only by the Appendix A `kid`
values reproducing under it, which this pass reproduced twice).

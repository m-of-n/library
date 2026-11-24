---
record: in-toto-attestation-v1
kind: design-notes
title: "in-toto-attestation-v1 — bearing on our design"
extracted: "2026-11-09"
reviewed_by: ""
---

# in-toto Attestation Framework v1.2 — bearing on our design

**The source.** Twelve Markdown files of `in-toto/attestation` at tag v1.2.0,
commit `df02077bf97218a8860a5c534eff1f1381f56984` (`record.yaml`
`identifiers.git`), rendered by `distilled/render-source.py` into
`.cache/in-toto-attestation-v1.txt`: 1162 lines, sha256
`87260bf00f01cbbe4e9c85795f29043ffc8801416958a8bde232139cb1ed13d0`. That is the
`source_digest` in `requirements.yaml`. In this pass the archive was re-extracted
and re-rendered, and the output was byte-identical. The archive's sha256,
`c66cbb44b115cd0745e0f22dfedb069729a081a7f56372e3fca8ead667795d91`, matches
`content.sha256` in `record.yaml`; it was recomputed from
`.cache/in-toto-attestation-v1.bin` in this pass. `§i.j` means file *i*,
heading *j* of the rendering, per the `render-source.py` docstring.
`spec/predicates/*` and `spec/v0.1.0` are out of scope. File 8,
`spec/v1/envelope.md`, has the same sha256 (`c02c6588…`) as the separate record
`in-toto-envelope-v1`, so both records hold one text.

**Our side.** m-of-n at commit `bb005ed`
(`bb005ed9e94b7aa9936c9a82077829e7b85d3eae`, 2026-11-07). Each quotation of
ours carries `path@bb005ed`. Each was checked by script, as a whole span with
whitespace normalised, against `git show bb005ed:<path>`. At that commit
**DEC-002 is accepted as option 5 by `ADR-0004`** (2026-10-25), and that
acceptance closes MD-3's narrowing. `docs/extraction.md` still says that *no
DEC-002 ADR exists*. That sentence predates `ADR-0004`. **DEC-005**, the
envelope for `ArtifactStatement`, is open. So are DEC-004, DEC-008 and DEC-009.

**How it reaches us.** The record's `bears_on` names six ids: R-M-07, R-M-11,
R-M-12, R-I-01, R-I-03 and R-O-05. R-M-12 is now only a pointer: *"Relocated:
native extension points are key-relative."*
(`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.1). Its content is
`ARCH-0002` P1, accepted by `ADR-0001`. Beyond those six ids:

1. **R-I-03** names this source as an export target, *"Export to in-toto
   Statement + DSSE OR COSE_Sign1 + CWT claims (at least one envelope in v1)."*
   (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.2). §8 of this
   file shows the envelope layer constrains that sentence.
2. **R-I-01** and the in-toto row of `ARCH-0001` §6. mofn#110 owns that table's
   rows, and WP3 owns the mapping spec. §11 drafts the row's R-I-01 table.
3. **DEC-002 / `ADR-0004` / MD-3.** in-toto signs a JSON Statement through DSSE
   and never canonicalises. That bears on what a canonical encoding is for. §5
   covers it, including where it cuts against `ADR-0004`.
4. **DEC-005** (open). §8.1.1 rules `COSE_Sign1` non-compliant as an in-toto
   envelope.
5. **mofn report R-0006** read in-toto only second-hand. Its §2.2 in-toto row
   cites `[@slsa-1-2]` for the digest map
   (`research/0006-mechanism/report.md`@bb005ed, §2.2). Its §8 lists
   *in-toto Attestation v1 (stub)* among the sources to ingest. This record is
   the primary source for those cells.

**What it is not.** The rendering was searched with `grep -o`. There is **no
trust model**: attesters are an input (L1126). There is **no threshold**
("threshold" occurs 0 times), **no revocation** ("revoc" 0) and **no issuer
field** ("issuer" 0). The Statement has no validity window. There is **no
canonical form**: "canonical" occurs once, inside *canonicalization*, at L754.
**PAE is not defined here**: "PAE" occurs 0 times. DSSE defines it (library
record `secure-systems-lab-dsse`), and this source only points to DSSE v1.0
(L748, L842).

**Normative weight.** The keywords are RFC 2119 (L63-65). `bin/bcp14-count`
finds 101, all in the skeleton's entries R-0001…R-0087. `requirements.yaml`
holds 218 entries: those 87 (18 of them split, each into `split_of` children
R-0088…R-0123), 75 keyword-less stated entries (R-0124…R-0196, and R-0217 and
R-0218, which pass 2 added) and 20 inferred ones (R-0197…R-0216). This file was written against the skeleton's ids: where it
cites a split parent (R-0007, R-0009, R-0032, R-0052 and others), the statement
meant is one of that parent's children, which `requirements.yaml` names.
**The validation model (file 12) carries no keyword** and sits in `docs/`,
outside the documents §1.2 declares keywords for. This file treats it as
binding nobody by keyword. `requirements.yaml` carries its steps as
keyword-less stated entries, the reference consumer procedure (R-0186…R-0196),
with spec/v1 governing where the two disagree. Several conclusions below rest on
it, and each one says so.

**Conventions.**

- `Lnnn` is a line of the rendering. A source quotation is a
  `<!-- q Lx-y -->` marker. Its words were written by `bin/check-quotes
  --render`, not typed.
- `R-NNNN` is `in-toto-attestation-v1#R-NNNN`. Every cited id was joined to its
  text and lines by script, and each pair was read.
  The one exception is `R-0006` followed by a section sign, by *condition*,
  or by the word *report*. That is mofn's research report
  `research/0006-mechanism/report.md`. This file never cites in-toto's R-0006.
- **Verdicts.** *adopt*, *adapt* and *reject* say what m-of-n takes from this
  source. *constrains*, *conflicts* and *silent* relate the source to one of
  our decisions:
  - *constrains*: one side narrows what the other leaves open.
  - *conflicts*: one object or implementation cannot satisfy both.
  - *silent*: one side does not reach the other's subject.

  Levels are printed as the source prints them: SHOULD is not MUST.

---

## 1. What we adopt

### A-1. Sign the bytes, authenticate the type, never canonicalise in verification

The envelope requirements:

<!-- q L778 -->
> - `payloadType` (or equivalent) MUST be signed along with the `payload`.

<!-- q L753 -->
> - SHOULD include an authenticated payload type

<!-- q L754 -->
> - SHOULD avoid depending on canonicalization for security

<!-- q L756 -->
> - SHOULD NOT require the verifier to parse the payload before verifying

The Statement is decoded from the very bytes that were verified. The
validation model (no keyword) verifies at the envelope layer, and only then
decodes:

<!-- q L1147-1148 -->
> - `statement` := decode `envelope.payload` as a JSON-encoded [Statement]; reject if decoding fails

Ours: R-O-05, *"A verifier SHALL verify the signature before decoding and SHALL
NOT canonicalize input as part of verification."*
(`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.3). And `SPEC-0002`
§3, *"The verifier never re-encodes."* (`spec/SPEC-0002-ksa-core.md`@bb005ed,
§3).

**What is adopted is the practice, and R-O-05 is stricter than this source's
normative text.** R-0050 is a SHOULD NOT on an envelope *format*. It does not
oblige a consumer. The two consumer MUSTs (R-0062, R-0072) mention parsing and
verifying, and state no order:

<!-- q L794-795 -->
> - To obtain predicate information that is authenticated, consumers MUST parse the Envelope's `payload`, and verify it against its `signatures`.

Within this source, the verify-first order appears only in the keyword-free
validation model. DSSE states it as a rule (record `secure-systems-lab-dsse`;
R-0006 §2.2 quotes its verifier procedure). Taken alone, an in-toto consumer that parses the payload before
verifying meets R-0062 and R-0072. R-O-05 forbids that (open question 11).
`requirements.yaml` reads the order in as R-0214, an *inferred* entry (verify
before decoding, from the validation model's order and R-0050); it is the
extraction's reading, not the source's keyword.

### A-2. Two type indicators, and only the inner one decides the predicate

`payloadType` names the encoding and the schema family. `predicateType`,
inside the signed payload, names the predicate. The source does not let the
outer one decide:

<!-- q L791-793 -->
> - Consumers SHOULD NOT rely upon the media type for individual attestations as faithful indicators of predicate type. Consumer SHOULD only rely on the `predicateType` field in the [Statement] layer.

This matches R-0006 condition (4): *"The encoding profile is named by an
**authenticated type indicator** carried inside the signed bytes."*
(`research/0006-mechanism/report.md`@bb005ed, §3.2). Our analogue is the DS
label `KSA-STMT-SIG-v1\0` with the signed `suite` and `kind`, plus the
`type-ref` inside the body. The predicate-specific media type is authenticated
by PAE. It is still a hint, because the source says to rely on `predicateType`
alone (R-0060, R-0061, R-0070, R-0071).

### A-3. The envelope is a layer, not the information model

<!-- q L19 "[Envelope]" .. "serialization." -->
> [Envelope]: Handles authentication and serialization.

Ours: the DSSE row of `ARCH-0001` §6, *"Not an information-model type"*
(`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §6). And `ADR-0004` item
4, *"COSE_Sign1 and DSSE are export envelopes only."*
(`spec/ADR-0004-dec-002-encoding.md`@bb005ed). The two agree.

### A-4. Processing a set of attestations does not depend on order

<!-- q L884 -->
> - Processing of a Bundle MUST NOT depend on the order of the attestations.

Ours: `SPEC-0004` §3, *"no ordering of inputs — may affect the result."*
(`spec/SPEC-0004-ksa-trust-evaluation.md`@bb005ed, §3). R-M-05 is weaker than
both: *"Authorization composition SHALL be deterministic given an ordered cert
set and ACL."* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.1).
Under R-M-05, a verdict that depends on order is still compliant. R-0077 and
`SPEC-0004` both forbid it, and SPEC-0004 governs (`ADR-0003`).

### A-5. A locator is a hint

<!-- q L649 "SHOULD resolve" .. "unresolvable." -->
> SHOULD resolve to the artifact, but MAY be unresolvable.

Ours: R-M-11, *"A locator SHALL be treated as non-authoritative evidence about
a subject, not as its definition."*
(`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.1). And `SPEC-0003`
§4.4, *"a hint for retrieval, never an identity"*
(`spec/SPEC-0003-ksa-definitions.md`@bb005ed, §4.4).

### A-6. The three native digest algorithms export without loss

`SPEC-0002` §12.5 registers SHA-256, SHA-384 and SHA-512 for target type 2.
in-toto says its key names are the NIST names, lowercased, with `-` replaced by
`_`:

<!-- q L446-448 -->
> Standard cryptographic hash algorithms using [the NIST names][] (converting to lowercase and replacing `-` with `_`) as keys and lowercase hex-encoded values, for cases when the method of serialization is obvious or well known.

That rule would give `sha_256`, `sha_384` and `sha_512` (normative.md SD-25,
R-0205); the keys are what the §5.2.1.1 heading lists, and it lists `sha256`,
`sha384` and `sha512`, which cover those three. The values are lowercase hex
(L432). These are 3 of the 19 names §5.2.1.1 predefines; the count was taken by
script over L444. (Pass 2: this paragraph said the keys *are* the NIST names
so transformed; by script, the rule produces the listed key for 6 of the 19
only, the SHA-3 and SHAKE names.) R-0031 recommends `sha256` at least. An export carries the
native digest under its in-toto name, and nothing is lost.

### A-7. Attesters are an input, not a trust anchor the format brings

<!-- q L1126 -->
> - `recognizedAttesters`: collection of (`name`, `publicKey`) pairs

The validation model takes the recognised attesters as a parameter. Its output
goes to a policy engine (L1157-1162). Ours: R-I-02, *"Import SHALL NOT require
the foreign object to become a native trust anchor."*
(`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.2). in-toto never
asks a verifier to trust a key because an attestation names it. The Statement
names no key at all (§2, adapt D-4).

---

## 2. What we adapt, and how

### D-1. `predicateType` ↔ `type-ref`: injective on export, lossy on import

<!-- q L664-666 -->
> A TypeURI is represented as a case sensitive _string_ and MUST be case normalized as per section 6.2.2.1 of RFC 3986, meaning that the scheme and authority MUST be in lowercase.

<!-- q L671-672 "TypeURIs are" .. "collisions." -->
> TypeURIs are not registered. The natural namespacing of URIs is sufficient > to prevent collisions.

<!-- q L1088-1091 -->
> The type ID only includes the major version. This allows implementations to support any major version without having to parse the URI to pull out the version. (Parsing is impossible since we don't mandate the format of the URI.) Implementations just use the URI as an opaque string.

Ours: `ADR-0007`, *"never by URI."*
(`spec/ADR-0007-dec-007-predicate-rendering.md`@bb005ed, Decision). The §6 row
reads *"`predicateType` URI ↔ `type-ref` is a lossy mapping (`ARCH-0002` P1)"*
(`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §6).

- **Export can keep identity.** A TypeURI is any RFC 3986 URI with a
  lower-case scheme and authority. It is unregistered, and the source tells
  implementations to treat it as an opaque string. A `type-ref` is
  (DefinitionId, label), so any injective URI spelling of that pair is a legal
  `predicateType`. lane-a's JSON placeholder `key:<key id>:<label>`
  (`prototype/lane-a/README.md`@bb005ed) is a syntactically valid URI with
  scheme `key` when the label holds no reserved character (our reading of RFC
  3986, which is not a library record), and
  `in-toto-attestation` 0.9.3 accepted it (`DL-0012`,
  `design-log/0012-lane-a-key-relative/produced.md`@bb005ed). The validation
  model never checks `predicateType`. It hands the value to policy (L1159). So
  identity survives an export. What does not survive is resolvability:
  R-0041 asks for a URI that resolves to a human-readable description, and our
  meaning lives in a signed definition, not at a URL.
- **Import loses the definer.** A foreign TypeURI has no defining key. To
  become a `type-ref` it needs a definition, and someone has to author it. The
  only candidate is the importer, as the X.509 row of §6 already does with *"a
  `x509:` namespace of the *importer*"*
  (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §6). The import is
  lossy because who defines the type changes.
- **The versioning models do not meet.** in-toto keeps one TypeURI across
  minor versions (L114-118, L1088). Ours: *"A definition is never edited: any
  change produces a new DefinitionId."*
  (`spec/SPEC-0003-ksa-definitions.md`@bb005ed, §11.3). An export URI built
  from the DefinitionId makes every revision a new in-toto predicate type, so
  in-toto policies keyed on `predicateType` stop matching. A URI built from
  definer, name and major version follows in-toto's convention, but it no
  longer pins a definition. Open question 3.

### D-2. DigestSet ↔ target type 2: one digest out, at most one in

<!-- q L430-434 -->
> A DigestSet is represented as a _JSON object_ mapping algorithm name to a string encoding of the digest using that algorithm. The named standard algorithms below use lowercase hex encoding. Usually there is just a single key/value pair, but multiple entries MAY be used for algorithm agility.

<!-- q L553-554 "Consumers MUST" .. "algorithms." -->
> Consumers MUST only accept algorithms that they consider secure and MUST ignore unrecognized or unaccepted algorithms.

<!-- q L557-558 -->
> Two DigestSets SHOULD be considered matching if ANY acceptable field matches.

Ours: `SPEC-0002` §7.2 type 2 is `[2, digest-alg, bytes]`, one digest with
*"`digest-alg` 1 = SHA-256 (32 octets)"* (`spec/SPEC-0002-ksa-core.md`@bb005ed,
§7.2). §12.5 adds codes 2 and 3, SHA-384 and SHA-512.

- **Export:** one entry, under the target's own algorithm, in lowercase hex
  (A-6). Nothing is lost.
- **Import:** a target holds one digest and a DigestSet holds a set. At most
  one accepted entry can become the target. The rest are *dropped* in R-I-01's
  terms. Which entry is chosen is not specified anywhere of ours.
- **ANY-match is weaker than it looks.** By R-0034, and by the validation
  model's existential test (L1152), a DigestSet whose `sha256`
  matches still matches when its `sha512` does not. This is an inference from
  those two passages, and the source has no example of it. The match is as
  strong as the weakest accepted algorithm, and an internally inconsistent
  DigestSet is never noticed. R-0034 is a SHOULD. An importer that checks every
  entry it can compute is stricter than the source, and nothing in the source
  forbids that. Open question 2.
- **A git key does not name its hash.** `gitCommit`, `gitTree`, `gitBlob` and
  `gitTag` hold SHA-1 or SHA-256, distinguished only by length:

<!-- q L517-518 "The lowercase hex" .. "respectively." -->
> The lowercase hex SHA-1 (40 character) or SHA-256 (64 character) of a git commit, tree, blob, or tag object, respectively.

  An acceptance list keyed on names cannot admit `gitCommit` under SHA-256 and
  refuse it under SHA-1 without also checking length (inference).

### D-3. The `subject` array ↔ one `this`

<!-- q L190 "Set of" .. "applies to." -->
> Set of software artifacts that the attestation applies to.

<!-- q L191 "Each element MUST" .. "set." -->
> Each element MUST have `digest` set.

<!-- q L206 "If set" .. "subject." -->
> If set, `name` and `uri` SHOULD be unique within subject.

<!-- q L208-209 "Subject artifacts" .. "content type." -->
> Subject artifacts are matched purely by digest, regardless of > content type.

Ours: one target per statement, `this` (`SPEC-0002` §7.1, key 4).

- **Export:** one native statement becomes a Statement with a one-element
  `subject`.
- **Import:** a Statement with *N* subjects becomes *N* logical attestations
  under one signature. None of them has a native statement digest, because
  *"A statement is referred to by the SHA-256 of its TBS"*
  (`spec/SPEC-0002-ksa-core.md`@bb005ed, §3) and an import has no TBS. Open
  question 7.
- **`name` is not part of the match.** Its meaning is whatever producer and
  consumer agree (R-0010), and matching is by digest alone. No native field
  corresponds. An import keeps it as display or drops it (§11).

### D-4. The speaker: in-toto authenticates it but never states it

The Statement has four fields: `_type`, `subject`, `predicateType` and
`predicate` (L183, L188, L212, L216). None names a key. The validation model
finds the speaker by trying each recognised key against each signature:

<!-- q L1136-1141 -->
> - For each `signature` in `envelope.signatures`: - For each (`name`, `publicKey`) in `recognizedAttesters`: - Optional: skip if `signature.keyid` does not match `publicKey` - If `signature.sig` matches `publicKey`: - Add `name` to `attesterNames`

Ours: P2, *"the speaker is the key."*
(`spec/ARCH-0002-key-relative-naming.md`@bb005ed, P2). `says` is REQUIRED inside
the TBS (`SPEC-0002` §7.1). P5.2: *"The principal travels in the payload, never
in `signatures[].keyid`."* (`spec/ARCH-0002-key-relative-naming.md`@bb005ed,
P5.2). And `ADR-0005`: *"the principal travels in the payload"*
(`spec/ADR-0005-dec-003-key-identifier.md`@bb005ed, Interchange).

- in-toto authenticates the speaker through the signature check, but the
  speaker is not *in* the signed bytes. Several keys may sign one Statement,
  and R-0006 §5.1 records from DSSE that *"A DSSE envelope carries `n` and
  cannot carry `k`."* (`research/0006-mechanism/report.md`@bb005ed, §5.1). The
  *A* of *A says B has C* sits outside the content.
- **Export.** A plain Statement cannot satisfy P5.2's rule or `ADR-0005`'s.
  There are three places to put it:
  - the predicate, under a predicate specification of ours (D-5);
  - an extension field, which consumers MUST ignore (R-0001). Ignoring it
    loses nothing, because the attester comes from the signature check, so
    the field is harmless and also useless;
  - the envelope only: the verifying key, with `keyid` as a hint. That is
    in-toto's own design, and the signature authenticates it.

  P5.2 and `ADR-0005` wrote their rule for the KSA payload, and neither
  considered a payload with no speaker field. Open question 4.
- **Import.** An envelope with *n* verified signatures yields *n*
  attestations, one per verified signer. Each `says` is the `kid` of the
  verifying key. That needs the key's encoding under one of our suites
  (`SPEC-0002` §4.5), and DSSE leaves the algorithm open. Count distinct kids:
  *"Distinctness is by kid."*
  (`spec/SPEC-0004-ksa-trust-evaluation.md`@bb005ed, §6.4).
  `attesterNames` is a set of *names* (L1135, L1141), so a key listed under two
  names yields two names from one signature. That is an inference from the
  pseudocode. A threshold counted over `attesterNames` could count one key
  twice. `SPEC-0004` §6.4 does not have that hazard.

### D-5. Validity, kind and template go in the predicate, under a must-understand specification

<!-- q L109-110 "Consumers MUST" .. "specification." -->
> Consumers MUST ignore unrecognized fields unless otherwise noted in the predicate specification.

<!-- q L130-132 -->
> The presence or absence of the extension field MUST NOT influence the meaning of any other field, and the field MUST follow the monotonic principle.

<!-- q L134-137 -->
> - **Monotonic principle:** A policy is considered monotonic if ignoring an attestation, or a field within an attestation, will never turn a DENY decision into an ALLOW. A predicate or field follows the monotonic principle if the expected policy that consumes it is monotonic.

Ours: `valid` (`SPEC-0002` §7.3), `kind` (REQUIRED, §7.1) and `template`
(§8.5, *"a statement that names a template MUST conform to it"*,
`spec/SPEC-0002-ksa-core.md`@bb005ed).

- The Statement has no field for any of the three. The only free places are
  extension fields and the predicate.
- **`valid.not-on-or-after` cannot be an extension field.** A consumer that
  ignores it accepts an expired statement, so ignoring it turns a DENY into an
  ALLOW. The field then fails the monotonic principle, which R-0007 requires
  of every extension field. The same holds for `kind`: a `review` read as an
  `approve` (`SPEC-0002` §8.10). It holds for `template` too: a statement that
  names a template it does not conform to would be accepted. This is our
  reasoning, applied to the source's definition at L134-137.
- **The source's own escape hatch is R-0001's exception for predicate
  specifications (L109-110, quoted above).** An export that keeps these fields needs a
  predicate specification of ours that makes them must-understand, and its
  predicate type is ours (D-1). Without one, the fields are dropped, and the
  R-I-01 table must say so. Open question 10.

### D-6. A `description` subject exports as the description document

<!-- q L49-51 "Tagged release v1.1.0" .. "immutable identifier." -->
> Tagged release v1.1.0 (MINOR version) generalizes the semantics of the `DigestSet` field type to support any type of immutable identifier.

<!-- q L337-338 "A descriptor" .. "artifact." -->
> A descriptor that specifies a `digest` is assumed to refer to an immutable resource or artifact.

Ours: R-M-11's third mode. `SPEC-0002` §7.2 type 6 is `[6, type-ref, value]`,
*"the description's canonical encoding is its identity"*
(`spec/SPEC-0002-ksa-core.md`@bb005ed, §7.2). The §6 row reads *"a
`description` subject (R-M-11) has no in-toto digest-set form"*
(`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §6).

- **A form exists.** The `digest` holds the SHA-256 of the description's
  canonical bytes, and `content` carries the bytes themselves. In JSON they
  are base64 (L245), and R-0019 says `content` SHOULD stay under 1KB. A
  `mediaType` is added as well. `SPEC-0002` §7.2 does not say which bytes to
  hash: the whole target array or only its `value`.
- **The meaning does not survive.** A descriptor with a digest refers to an
  immutable artifact (L337-338), and subjects are matched by digest alone
  (L208-209). So an in-toto consumer reads that subject as *the description
  document*, not as the thing described. No in-toto field says that this
  digest identifies a description, and that the description identifies the
  subject. The §6 note is right about meaning. Since v1.1, *"has no in-toto digest-set
  form"* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §6) is too
  strong.

### D-7. A locator-only subject cannot be exported

<!-- q L191 "Each element MUST" .. "set." -->
> Each element MUST have `digest` set.

Ours: `SPEC-0002` §7.2 type 5, *"a resource identified by a URI; weaker than a
digest, and SHOULD be used only where no digest exists"*
(`spec/SPEC-0002-ksa-core.md`@bb005ed, §7.2). The R-M-07 note reads *"a locator
alone does not"* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.1).
`ARCH-0001` §5.5 records the gap as owed by `SPEC-0002` §7.2 (mofn#144).

- in-toto sides with R-M-07 against `SPEC-0002` §7.2's bare locator. An
  `attestation` whose `this` is `[5, text]` has no in-toto subject form. A
  ResourceDescriptor may carry `uri` alone (R-0013, R-0015), but not as a
  subject.
- A non-cryptographic DigestSet entry (R-0036) does not get around this. Each
  entry has to be immutable (R-0029), and a locator names a
  resource that may change. That is inference: the source never applies R-0029
  to a URI.
- This is evidence for mofn#144.

### D-8. `keyid`: export the `kid` as a hint; the import rule needs adapting

<!-- q L774 "A `keyid`" .. "used." -->
> A `keyid` (or equivalent) SHOULD be included for each signing key used.

<!-- q L1138-1139 -->
> - Optional: skip if `signature.keyid` does not match `publicKey`

Ours: `ADR-0005` Interchange. Export: *"The native `kid` may be exported in
COSE's `kid` header or DSSE's `keyid` as a"* hint. Import: *"On import, a
foreign `kid` that disagrees with the `kid` computed from the key is"*
rejected, *"P1.1, amended to reject on 2026-10-25; P5.2 for DSSE"*
(`spec/ADR-0005-dec-003-key-identifier.md`@bb005ed).

- **Export:** adopt as written.
- **Import:** this source gives `keyid` no format. It links KEYID to the
  in-toto specification v1.0 §4.2.1 (L844), and the validation model treats
  the field as an optional hint for skipping keys. The format is left to
  tooling. lane-a's own DSSE sample writes `SHA256:` and then base64
  (`prototype/lane-a/02_dsse_intoto.py`@bb005ed). Read literally, `ADR-0005`
  rejects every envelope whose `keyid` is anything other than a rendering of
  our `kid`, lane-a's own sample among them. For the in-toto verifier,
  `keyid` is only a hint for skipping keys. "Disagrees" needs a
  definition for a foreign `keyid` format. This is a **conflict**; open
  question 5.

---

## 3. What we reject, and why

### J-1. Ignoring unknown fields by default, and producer extension fields

<!-- q L110-112 "This is to allow" .. "monotonic principle." -->
> This is to allow minor version upgrades and extension fields. Ignoring fields is safe due to the monotonic principle.

<!-- q L121-122 "Producers MAY" .. "object." -->
> Producers MAY add extension fields to any JSON object.

<!-- q L138 "Consumers SHOULD" .. "monotonic." -->
> Consumers SHOULD design policies to be monotonic.

Ours: P5, *"an unknown field in a signed payload is an error, not something to
skip."* (`spec/ARCH-0002-key-relative-naming.md`@bb005ed, P5). `SPEC-0002` §7.1:
*"KSA has no namespaced extension fields"*. §13.5: *"an unknown kind or field
is invalid. A verifier MUST NOT skip what it does not understand (ARCH-0002
P5)."* (`spec/SPEC-0002-ksa-core.md`@bb005ed).

**Why reject.** The source argues that ignoring is safe. That argument rests on
two conditions, and no verifier can check either one:

- every extension field is monotonic. R-0007 binds the *producer*;
- the consumer's policy is monotonic. R-0008 is a SHOULD.

P5 cites CVE-2025-59420, where the skipped item was exactly the one that
narrowed. D-5 shows that our own validity window would be such a field. This
confirms P5; it does not test it.

### J-2. Versioning in which the major version alone appears on the wire

<!-- q L114-118 "Each type" .. "monotonic principle." -->
> Each type has a [SemVer2](https://semver.org) version number and the [TypeURI] reflects the major version number. A message is always semantically correct, but possibly incomplete, when parsed as any other version with the same major version number and thus the same [TypeURI]. Minor version changes always follow the monotonic principle.

<!-- q L1093-1094 -->
> The advantage of having minor versions is that we can add new information without requiring consumers to update.

Ours: *"Under our profile a new field is a new definition (`ARCH-0003` W-12), not
a field that old verifiers ignore."*
(`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §3.4), and `SPEC-0003`
§11.3, quoted at D-1.

**Why reject.** First, the wire never says which minor version wrote a message.
`_type` stayed the same through v1.0, v1.1 and v1.2:

<!-- q L54-55 "The `_type`" .. "Statement/v1`" -->
> The `_type` of a `Statement` is still `https://in-toto.io/Statement/v1`

So a consumer cannot tell whether a Statement's DigestSet follows v1.0's
cryptographic-only reading or v1.1's wider one (§9). Second, the compatibility
rules cover the Statement and the predicates only:

<!-- q L1060-1061 -->
> The following rules apply to both Statement and predicate specification versioning.

v1.2 changed the envelope in a MINOR release with no such guarantee (§12,
SD-10).

### J-3. A global type namespace with no registry

<!-- q L668 "SHOULD resolve" .. "unresolvable." -->
> SHOULD resolve to a human-readable description, but MAY be unresolvable.

<!-- q L669 "SHOULD include" .. "revisions." -->
> SHOULD include a version number to allow for revisions.

Ours: `ADR-0001`, *"Native extension points — type identifiers, predicate types,
tags, header parameters — are identified relative to a defining principal"*
(`spec/ADR-0001-key-relative-naming.md`@bb005ed). `SPEC-0003` §13.2: *"Because
statements cite definitions by hash, an attacker cannot change what a value
means after the fact."* (`spec/SPEC-0003-ksa-definitions.md`@bb005ed).

**Why reject.** TypeURIs are not registered (L671), but they are still global:
an `https` TypeURI hangs off DNS. The meaning lives at a URL that MAY be
unresolvable and that no digest binds, and a minor version changes the document
behind the same URI (J-2). That is DEC-007's option 1 plus an unbound pointer.
`ADR-0007` chose option 2. **It is not a registry, though.** Vetting by the
maintainers is a MAY (R-0043). Two of our documents call it one (§12b).

### J-4. A non-cryptographic identifier as the subject binding

<!-- q L571-573 -->
> In these situations, users MAY use a non-cryptographic identifier in a DigestSet so long as the risk of the object being mutated is acceptable for the application.

<!-- q L604 -->
> - `{"arn": "arn:aws:ec2:region:123:image/ami-123abcd"}` for a non-cryptographic VM image digest using an Amazon Resource Name (ARN) in the `subject` field of a Statement

Ours: R-M-07, *"Artifact statements SHALL bind at least one content digest."*
(`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.1). The source
justifies an ARN like this:

<!-- q L586-587 "These IDs" .. "threat profiles." -->
> These IDs can often be treated as immutable and may be perfectly suited to users threat profiles.

That is a judgement about immutability. It is not a digest of content. An export
never produces one, and an import must not count one towards R-M-07 (§9).

### J-5. One meaning with two encodings

<!-- q L218-219 "Unset is" .. "set-but-empty." -->
> Unset is treated the same as > set-but-empty.

Ours: *"Absent optional fields MUST be omitted; they MUST NOT be present with an
empty or placeholder value."* (`spec/SPEC-0002-ksa-core.md`@bb005ed, §7.1), and
R-0006 condition (1), injectivity
(`research/0006-mechanism/report.md`@bb005ed, §3.2).

**Why reject.** in-toto loses nothing by it, because nothing in in-toto is
identified by the hash of a Statement (§5.2). We would lose a statement: its
identity is the SHA-256 of its TBS, so two encodings of one meaning are two
statements. The source permits both an unset `name` and `"_"` (L200). It
treats an unset `predicate` and an empty one alike (L218-219).

### J-6. An unauthenticated collection as the carrier for a statement whose absence matters

<!-- q L864-868 -->
> **NOTE**: The Bundle is not authenticated as a whole. Instead each individual attestation is authenticated using signature formats like [DSSE]. As such, an attacker might be able to delete valid attestations, replay obsolete attestations, and/or inject invalid or irrelevant attestations in a Bundle without being detected.

<!-- q L871-872 -->
> In addition, predicates that follow the [monotonic principle] should not have any issues with deletion attacks.

Ours: `SPEC-0004` §7.1, *"It cannot know of one it has not received"*
(`spec/SPEC-0004-ksa-trust-evaluation.md`@bb005ed), and R-O-02, *"Short-lived
validity preferred over revocation-heavy design; revocation still
representable."* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.3).

**Why reject the Bundle as a revocation channel.** By the source's own
definition (L134-137) a `revoke` is not monotonic: ignoring one turns a DENY
into an ALLOW. R-0008 tells in-toto consumers to avoid policies that depend on
such attestations, and a Bundle cannot protect one from deletion. This is
evidence for R-O-02's preference, which `SPEC-0004` already states. It is not a
new rule.

---

## 4. Mapping to our decisions

One row per decision the source touches. Ours is quoted from `path@bb005ed`;
the source is cited by R-id and level, or by line where no keyword applies.
Verdicts as in the conventions above.

| # | Ours (quoted; path@bb005ed) | Source (R-id, level; line) | Verdict |
|---|---|---|---|
| 1 | **R-O-05, clause 1** *"The signed payload SHALL be the canonical encoding verbatim, carried with an authenticated type indicator."* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.3) | R-0063 MUST: the payload is a base64-encoded JSON Statement; R-0056 MUST: `payloadType` signed with it; R-0047 SHOULD: an authenticated payload type | **constrains.** The type indicator holds (A-2). "Canonical encoding verbatim" cannot hold for an in-toto export, because its signed payload is a JSON Statement, not KSA-CBOR. The export is a second signed object over different bytes (§6) |
| 2 | **R-O-05, clause 2** *"A verifier SHALL verify the signature before decoding and SHALL NOT canonicalize input as part of verification."* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.3) | R-0050 SHOULD NOT and R-0048 SHOULD, both on envelope *formats*; R-0062 and R-0072 MUST, naming parsing and verifying with no order stated; validation model L1132-1148, verify first | **adopt.** R-O-05 is stricter than the source's normative text (A-1) |
| 3 | **R-O-05, clause 3** *"Any human-facing form SHALL be regenerated from verified canonical bytes."* (same) | §9.5 pretty-prints Bundle lines with `jq` (L997-998); those are envelopes, unverified | **silent.** No in-toto counterpart |
| 4 | **§6 in-toto row** *"Subjects = artifacts."* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §6) | R-0009 MUST `digest`; R-0029 MUST immutable reference; R-0036 MAY non-cryptographic | **constrains.** The row says nothing about which digests an import accepts. R-0006 §2.5 proposed adding exactly that (§11) |
| 5 | **§6 in-toto row** *"a `description` subject (R-M-11) has no in-toto digest-set form"* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §6) | R-0036; v1.1 at L49-51; R-0019 `content`; L208-209 | **adapt.** Right about meaning, too strong about form (D-6) |
| 6 | **§6 in-toto row** *"`predicateType` URI ↔ `type-ref` is a lossy mapping (`ARCH-0002` P1)"* (same) | R-0040 MUST case-normalised; L671-672 unregistered; L1088-1091 opaque, major version only | **adapt.** Injective on export, lossy on import, and the versioning models differ (D-1) |
| 7 | **R-M-07** *"Artifact statements SHALL bind at least one content digest."* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.1) | R-0009, R-0029, R-0036; ARN example L604 | **conflicts** on import. An ARN-only subject is a conforming in-toto subject and carries no content digest (§9) |
| 8 | **R-M-07 note** *"a locator alone does not"*; `SPEC-0002` §7.2 type 5 (§5.5, mofn#144) | R-0009 MUST `digest` on every subject | **constrains.** in-toto agrees with R-M-07, against the bare locator `SPEC-0002` §7.2 still allows (D-7) |
| 9 | **R-M-11** *"Plus an `aliases` set binding several identifiers to one subject."* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §4.1) | R-0028 MAY several entries; R-0034 SHOULD match on ANY | **adapt.** A DigestSet works like an alias set restricted to digests of one artifact, under ANY-match (D-2). Aliases have no KSA form yet (§5.5) |
| 10 | **`SPEC-0002` §7.2** *"`digest-alg` 1 = SHA-256 (32 octets)"* and §12.5 (`spec/SPEC-0002-ksa-core.md`@bb005ed) | the 19 names at L444; R-0031 RECOMMENDED `sha256`; R-0032 MUST | **adopt** for export (A-6). On import one entry is taken and the rest dropped (D-2) |
| 11 | **R-M-12 → P1** *"Relocated: native extension points are key-relative."* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.1); `ADR-0001` *"mappings are documented as lossy per R-I-01"* (`spec/ADR-0001-key-relative-naming.md`@bb005ed) | `_type` fixed (L185-186); R-0058 MUST `payloadType`; R-0059 and R-0069 MUST: `<predicate>` is an in-toto predicate filename; DigestSet names (L446-448) with R-0032 | **constrains.** Three identifiers stay global at the boundary. Of the four a consumer acts on, only `predicateType` can be key-relative (§7) |
| 12 | **`ADR-0007`** *"never by URI."* (`spec/ADR-0007-dec-007-predicate-rendering.md`@bb005ed); `SPEC-0003` §13.2 (J-3) | R-0041 SHOULD resolve, MAY be unresolvable, SHOULD carry a version; L1088-1091 | **reject** (J-3). in-toto is DEC-007's option 1 plus an unbound URL |
| 13 | **P5** *"an unknown field in a signed payload is an error, not something to skip."* (`spec/ARCH-0002-key-relative-naming.md`@bb005ed); `SPEC-0002` §7.1, §13.5 | R-0001 MUST ignore; R-0002 MAY extension fields; R-0007 MUST NOT and MUST | **conflicts.** Opposite defaults. Rejected for the native model (J-1) |
| 14 | **P5.2** *"the payload interior is ours to govern"*; *"P5 governs the native model and the payload interior, in both directions."* (`spec/ARCH-0002-key-relative-naming.md`@bb005ed) | R-0001 applies to the Statement itself (L106-107) | **conflicts.** For an in-toto Statement the payload interior is *not* ours. P5.2 does not say which rule our importer applies inside it (§10, open question 1) |
| 15 | **P2** *"the speaker is the key."* (`spec/ARCH-0002-key-relative-naming.md`@bb005ed); `ADR-0005` *"the principal travels in the payload"* (`spec/ADR-0005-dec-003-key-identifier.md`@bb005ed) | the Statement's four fields (L183-220); speaker found by verification (L1136-1141) | **constrains.** A plain Statement cannot carry the principal in the payload (D-4) |
| 16 | **`ADR-0005` import** *"On import, a foreign `kid` that disagrees with the `kid` computed from the key is"* rejected (`spec/ADR-0005-dec-003-key-identifier.md`@bb005ed) | R-0049 SHOULD hint; R-0053 SHOULD; validation model L1138 optional skip; KEYID format not defined here (L844) | **conflicts.** Read literally, this rejects any conforming envelope whose `keyid` uses another format (D-8, open question 5) |
| 17 | **`ADR-0005` export** *"DSSE's `keyid` as a"* hint (`spec/ADR-0005-dec-003-key-identifier.md`@bb005ed) | R-0053 SHOULD; R-0054 MAY nest | **adopt** |
| 18 | **`SPEC-0004` §6.4** *"Distinctness is by kid."* (`spec/SPEC-0004-ksa-trust-evaluation.md`@bb005ed) | validation model: `attesterNames` is a set of names (L1135, L1141) | **adopt ours.** Counting names can count one key twice (D-4, inference) |
| 19 | **R-M-06** *"Threshold principals SHALL be representable without encoding them as a CA hierarchy."* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.1) | R-0046 MUST support several signatures; "threshold" occurs 0 times | **silent.** *n* signatures, never *k*, as R-0006 §5.1 found for DSSE |
| 20 | **`SPEC-0002` §5 envelope** `signed-statement = [ suite, says, tbs, sig, ? pub ]` (`spec/SPEC-0002-ksa-core.md`@bb005ed) | R-0046 MUST: several signatures in one envelope; R-0051 SHOULD NOT require the algorithm | **conflicts**, if the KSA envelope were ever offered as an ITE-5 envelope. It carries one signature, and a second speaker changes `says` and so the TBS. Several signatures over one TBS are impossible by construction (§8) |
| 21 | **DEC-005** *"Options: DSSE (in-toto world), COSE_Sign1 (SCITT world), both with a single unsigned payload schema."* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §7) | R-0044 RECOMMENDED DSSE; R-0045 MAY, under ITE-5; L763-764 `COSE_Sign1` NOT compliant | **constrains.** An in-toto Statement cannot ride compliantly in `COSE_Sign1` (§8) |
| 22 | **R-I-03** *"Export to in-toto Statement + DSSE OR COSE_Sign1 + CWT claims (at least one envelope in v1)."* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.2) | as row 21 | **constrains.** The in-toto disjunct needs DSSE, or `COSE_Sign`, which no document of ours names (§8) |
| 23 | **MD-3** *"CBOR data model, no IANA tags, COSE as export only"* (`project/meetings/2026-09-28.md`@bb005ed) | as row 21 | **constrains.** A COSE-only export could reach in-toto only through `COSE_Sign`, the one COSE structure the source rules compliant. `ADR-0004` item 4 added DSSE, and MD-3 is closed (§5.3) |
| 24 | **`ADR-0004` items 1–2** *"A rejecting decoder."* (`spec/ADR-0004-dec-002-encoding.md`@bb005ed) | L180: a JSON object; R-0063; R-0048 | **silent** on the native encoding. KSA-CBOR never enters an in-toto Statement (§5) |
| 25 | **`ADR-0004` item 3** *"Each may appear at an interchange boundary, mapped lossily per R-I-01."* (`spec/ADR-0004-dec-002-encoding.md`@bb005ed) | `_type`, media types (R-0058, R-0068, R-0081), DigestSet names | **adopt.** The global identifiers sit at the boundary. Item 3's list of excluded registries names no media-type registry (§5.3) |
| 26 | **`ADR-0004`, option 3 rejected** *"Withdrawn on the four grounds of `DECISIONS-0001` item 2"* (`spec/ADR-0004-dec-002-encoding.md`@bb005ed) | R-0048 (SHOULD, on canonicalization) | **constrains.** in-toto's practice is JSON with *no* canonicaliser. That candidate is not in DEC-002's option list (§5.3) |
| 27 | **R-0006 condition (2)** *"non-canonical input rather than normalising it"* (`research/0006-mechanism/report.md`@bb005ed, §3.2); P5.1 | no canonical form exists | **silent.** Vacuous for in-toto (§12b, on `record.yaml`'s wording) |
| 28 | **R-O-02** (J-6); `SPEC-0002` §7.3 `valid`; `SPEC-0004` §7.1 | no validity in the Statement; Bundle L864-868; R-0008 SHOULD; R-0007 MUST monotonic | **constrains.** Validity only travels in a must-understand predicate (D-5). `revoke` is not monotonic (J-6) |
| 29 | **R-M-05** *"Authorization composition SHALL be deterministic given an ordered cert set and ACL."* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.1); `SPEC-0004` §3 (A-4) | R-0077 MUST NOT depend on order | **adopt** `SPEC-0004` §3. R-M-05's wording is weaker than both |
| 30 | **`SPEC-0002` §3** *"A statement is referred to by the SHA-256 of its TBS"* (`spec/SPEC-0002-ksa-core.md`@bb005ed); §8.1 `review`/`approve` targets `[3, statement-digest]` | no attestation identifier; one attestation points to another through a ResourceDescriptor over a stored file (L373-379) | **constrains.** An exported `review` names a digest of KSA bytes that an in-toto consumer cannot compute from the exported JSON (open question 12) |
| 31 | **`SPEC-0002` §7.1** *"Absent optional fields MUST be omitted; they MUST NOT be present with an empty or placeholder value."* (`spec/SPEC-0002-ksa-core.md`@bb005ed) | L218-219; L199-200 | **reject** the source's equivalences (J-5) |
| 32 | **R-I-02** *"Import SHALL NOT require the foreign object to become a native trust anchor."* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.2) | `recognizedAttesters` is an input (L1126) | **adopt** (A-7) |
| 33 | **`ARCH-0001` §4.3 step 3** *"signature valid ∧ issuer authorized for that `PredicateType` ∧ subject digest matches the artifact under consideration"* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed) | validation model output L1157-1162: no check of who may speak about which predicate type | **silent.** in-toto leaves authorization to the policy engine |
| 34 | **`SPEC-0004` §5.1** statement set: only statements verified under `SPEC-0002` §9 (`spec/SPEC-0004-ksa-trust-evaluation.md`@bb005ed) | an imported attestation is verified under DSSE, never `SPEC-0002` §9 | **silent (gap).** §6 marks in-toto **I**, and no specification path takes an import into evaluation (open question 6) |
| 35 | **`SPEC-0002` §13.4** *"Identifiers MUST NOT be truncated in signed or hashed bytes."* (`spec/SPEC-0002-ksa-core.md`@bb005ed) | R-0067 SHOULD: `<keyid[0:8]>` in file names (L811-814) | **silent.** File names are not signed bytes |
| 36 | **R-I-07** *"Emit SPDX or CycloneDX *inside* an `ArtifactStatement` predicate rather than inventing a third SBOM syntax."* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.2) | predicate specifications are out of scope; §9.4.3 uses `https://spdx.dev/Document` (L956) | **silent** here |

---

## 5. MD-3, ADR-0004 and DEC-002

`docs/extraction.md` requires a signing-envelope document to address MD-3, and
to record where the document cuts against it. This source is one: its envelope
layer recommends DSSE, and the layer above carries JSON. At `bb005ed`, MD-3's
narrowing is closed by `ADR-0004`, which accepted option 5. What follows is
evidence for whoever next reads `ADR-0004`, and it reopens nothing.

### 5.1 Structure by structure

| in-toto element | where | KSA counterpart (`SPEC-0002`) | export | import |
|---|---|---|---|---|
| envelope `payloadType` | L785-786, R-0058 | DS label `KSA-STMT-SIG-v1\0` (§6.4) with signed `suite` and `kind` | `application/vnd.in-toto+json`. A predicate of ours has no in-toto filename, so the predicate-specific form is unavailable (§7) | must be one of the two forms (R-0058), or it is not an in-toto Statement |
| envelope `payload` | L798, R-0063 | `tbs` (§5) | a JSON rendering of the statement: new bytes, and a new signature | decoded only after the DSSE signature verifies |
| `signatures[].sig` | L771-772, R-0052 | `sig` over `DS ‖ tbs` (§5, §6) | DSSE's signature over PAE (record `secure-systems-lab-dsse`) | verified under DSSE. No KSA signature exists for an import |
| `signatures[].keyid` | L774, R-0053 | envelope `says`, a hint checked at V6 | the `kid` as a hint (row 17) | a hint only; `ADR-0005`'s import rule conflicts (D-8) |
| `_type` | L183-186 | none. The nearest are the DS label and `kind` | the fixed constant | must equal the constant |
| `subject[]` | L188-209 | `this`, one target (§7.1, §7.2) | one element | *N* subjects become *N* attestations (D-3) |
| `digest` | L278-285 | target type 2 | `sha256`, `sha384` or `sha512` (A-6) | at most one accepted entry (D-2) |
| `uri`, `downloadLocation` | L273-276, L301-307 | target type 5, a locator and a hint | only beside a digest (D-7) | a hint |
| `content`, `mediaType` | L287-299, L309-316 | target type 6, a description | the description's bytes (D-6) | — |
| `name` | L265-271 | none | optional, for display | dropped, or kept for display |
| `annotations` | L318-329 | none. §7.1 maps are closed and there are no extension fields | emit none | dropped (§10, §11) |
| `predicateType` | L212-214 | `type-ref` (§7.4) | a URI spelling of (DefinitionId, label) (D-1) | a definition the importer authors (D-1) |
| `predicate` | L216-220 | `body`: `has`, `template` (§8) | under a must-understand predicate specification (D-5) | mapped, or dropped |
| none | — | `says`, `suite`, `valid`, `kind` (§7.1) | no Statement field (D-4, D-5) | `says` comes from the envelope; the rest is absent |
| Timestamp field type | L684-689 | time (§4.4): seconds, no fraction | RFC 3339 in UTC fits | a fractional second, as in the source's own example at L689, has no KSA time (open question 13) |

### 5.2 What signing JSON through DSSE is evidence for

1. **R-O-05's verifier clauses and its type indicator** (A-1, A-2). The stack
   this source describes verifies the bytes it received and canonicalises
   nothing.
2. **`ADR-0004` item 4.** Its *"export envelopes only"*
   (`spec/ADR-0004-dec-002-encoding.md`@bb005ed, item 4) is in-toto's own
   layering (A-3).
3. **A canonical encoding is for identity, not for signing.** This is the
   strongest point here. in-toto signs and verifies with no canonical form.
   It pays for that exactly where `ADR-0004`'s encoding earns its keep: nothing
   in in-toto has an identity derived from content. The source's only example
   of pointing at an attestation is a ResourceDescriptor over a stored file:

<!-- q L375-378 -->
> "name": "gcc_9.3.0-1ubuntu2_amd64.intoto.json", "digest": { "sha256": "abcdabcde..." }, "downloadLocation": "http://example.com/rebuilderd-instance/gcc_9.3.0-1ubuntu2_amd64.intoto.json", "mediaType": "application/x.dsse+json"

   That reference names one serialisation of one envelope, signatures
   included. Adding a signature, or re-serialising the envelope JSON, changes
   its digest while the Statement stays the same. That is inference: the
   source says nothing about it. Ours: *"A statement is referred to by the
   SHA-256 of its TBS; a definition by the SHA-256 of its body. Both are stable
   across transports."* (`spec/SPEC-0002-ksa-core.md`@bb005ed, §3). So in-toto
   shows that signing the bytes, on its own, leaves identity dependent on
   serialisation. That is R-0006's Group B, *"safe to derive an identifier
   from"* (`research/0006-mechanism/report.md`@bb005ed, §3.2). It supports
   having *a* canonical encoding. **It does not discriminate between options 1
   and 5.**
4. **J-5's equivalences are harmless in in-toto only because of point 3.** The
   source sanctions two spellings of "no name" and two of "no predicate". That
   costs in-toto nothing, and it would cost us a statement per spelling.

### 5.3 Where it cuts against MD-3 and `ADR-0004`

1. **DEC-002's option list never contained this source's practice.**
   Option 3 is *"JSON + RFC 8785 JCS as canonical; DSSE for signed form."*
   (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §7). The in-toto
   practice is JSON with no canonical form at all, and its envelope rule
   (R-0048) says to avoid depending on canonicalisation. `ADR-0004` rejects
   option 3 on the four grounds of `DECISIONS-0001` item 2, which R-0006 §3.4
   sets out.
   - Three of those grounds are about JCS: the array-order prohibition, JCS's
     parse-then-verify, and the number algorithm. They do not reach a JSON
     option with no canonicaliser.
   - The fourth, *"The envelope reintroduces a global type identifier"*
     (`research/0006-mechanism/report.md`@bb005ed, §3.4), does reach it:
     `_type` and `payloadType` are fixed (§7).

   What excludes such an option is our own requirements, not JCS:
   - R-O-05 clause 1, *the canonical encoding verbatim*;
   - `SPEC-0002` §3's content addressing;
   - P5.1's decoder rejection, which needs a canonical form to reject against.

   **That candidate was never scored, and `ADR-0004`'s table has no column for
   it.** Call it *option 3 without JCS*; the label is ours and appears nowhere
   in `ARCH-0001` §7. Scoring it would most likely change nothing: it fails
   the three requirements just listed. But `ADR-0004` rejected a form of the
   in-toto approach that in-toto does not use.
2. **MD-3 named COSE alone. in-toto's envelope layer prefers DSSE and rules
   `COSE_Sign1` out.** MD-3 says *"COSE as export only"*
   (`project/meetings/2026-09-28.md`@bb005ed). The source:

<!-- q L763-764 -->
> - The [COSE_Sign] structure is [ITE-5] compliant, whereas the `COSE_Sign1` format that supports only one signer is NOT compliant.

   Under MD-3's wording, R-I-03's in-toto export could be reached only through
   `COSE_Sign`, and no document of ours names `COSE_Sign`. `ADR-0004` item 4
   repaired this by adding DSSE. *"COSE_Sign1 and DSSE"*
   (`spec/ADR-0004-dec-002-encoding.md`@bb005ed) is right for in-toto
   only through its DSSE half (§8).
3. **`ADR-0004` item 3's no-registry rule is cheap at this boundary, and not
   free.**
   `ADR-0004` item 3 names five registries the native model does not depend
   on. An in-toto export brings three further global identifier spaces:
   - the `application/vnd.in-toto…` media types, in the vendor tree of RFC
     6838, which the source cites for `mediaType` (L314);
   - DNS-rooted TypeURIs: `_type`, and every foreign `predicateType`;
   - the DigestSet algorithm names: in-toto's own list (L444), which it calls
     the NIST names although six of the 19 are not NIST algorithms and most
     are not spelled as the NIST names would give (normative.md SD-25).

   Item 3 allows them at the boundary (row 25), so nothing is inconsistent. But
   the R-I-01 table for in-toto must list them, and item 3's list is no help
   there.
4. **An in-toto export is always a second signature, under every DEC-002
   option.** The native statement form is not an in-toto Statement: `says` sits
   inside the signed bytes (P2), and the maps are closed (P5). So the speaker
   must sign new bytes, either at authoring time or later with the key. Option
   5 adds only a change of encoding to that. This cost is the information
   model's, not the encoding's, and it does not count against option 5.
   **DSSE carrying KSA-CBOR verbatim** keeps the bytes (R-O-05 clause 1) but
   not the signature, since DSSE signs PAE and not `DS ‖ tbs`. It is also not
   an in-toto Statement. §9.4.2 shows exactly that kind of envelope sitting in
   a Bundle:

<!-- q L938-940 "The vulnerability scanner" .. "envelope." -->
> The vulnerability scanner doesn't use in-toto Statements but instead uses their own custom `payloadType=application/vnd.novulz+cbor`, which they put in a [DSSE] envelope.

   It bears on DEC-005, not on DEC-002 (§8).

### 5.4 Net, stated as evidence

- **For `ADR-0004`:** identity needs canonical bytes (5.2, point 3), and in-toto
  shows what goes without them. References depend on serialisation, and one
  meaning has several encodings.
- **Against `ADR-0004`'s reasoning, not its outcome:** the option set was
  incomplete (5.3, point 1). MD-3's COSE-only wording missed in-toto's
  envelope rules (5.3, point 2), and `ADR-0004` item 4 had already repaired
  that.
- **Not a discriminator between options 1 and 5.** in-toto speaks to canonical
  against not canonical, never to which canonical form.
- Nothing here reopens DEC-002. `ADR-0004` changes only by being superseded.

---

## 6. R-O-05: verify the bytes that were signed, never re-serialise

R-O-05 has three clauses, and rows 1–3 grade each one. Only clause 2 has a
full in-toto counterpart. Even that one lives in the validation model and in
DSSE, not in a keyword (A-1). Two further points.

**Authenticated information comes from the verified payload, and from nothing
beside it.** This holds at both layers:

<!-- q L912-913 -->
> - To obtain predicate information that is authenticated, consumers MUST download and parse each line in a Bundle separately.

**The source's own example shows the hazard R-O-05 exists to prevent.** In the
Bundle walkthrough, the line whose payload is `a...` is built with a
predicate-specific type:

<!-- q L931 -->
> { "payloadType": "application/vnd.in-toto.provenance+json", "payload": "a...", "signatures": [w...] }

When Fooly republishes, the same payload and the same signature placeholder
`[w...]` appear under a different type:

<!-- q L984 -->
> { "payloadType": "application/vnd.in-toto+json", "payload": "a...", "signatures": [w...] }

The payload `d...` changes the same way, from L963 to L986. `payloadType` is
signed (R-0056), so the published lines verify only if they were re-signed,
and the walkthrough never says they were. Whatever the cause, the example
shows a publishing step rewriting signed envelope metadata. That is the
re-serialisation R-O-05 forbids. It is listed as a source defect (§12,
SD-5).

**Consequences, inferred.**

- **Export.** The producer writes the JSON Statement once, from a statement
  that has already reached V9 (`SPEC-0002` §9.2), and signs those octets
  through DSSE. No later step re-serialises them. PAE covers `payloadType`
  and `payload` (DSSE, record `secure-systems-lab-dsse`). So an intermediary
  that alters either one breaks every signature, and it should. One that adds
  or drops a signature, or edits a `keyid`, breaks none of the others.
- **Import.** Our verifier checks DSSE over the received payload, and only
  then parses the JSON. It never re-serialises the Statement. Clause 3,
  *"regenerated from verified canonical bytes"*
  (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.3), cannot be met literally for an
  import, because an import has no canonical bytes. The nearest equivalent is
  to render from the verified JSON payload, never from an envelope as received
  (§9.5's `jq` recipe does the latter, row 3). Open question 11.

---

## 7. R-M-12 and `ARCH-0002` P1: the names at the boundary

**Four in-toto identifiers are ones a consumer must act on**, and only one of
the four admits a key-relative value:

| identifier | rule | key-relative value | result |
|---|---|---|---|
| `_type` | L185-186: always the v1 constant. The validation model rejects anything else (L1149, §12 SD-2) | impossible | stays global (DNS-rooted under `in-toto.io`) |
| `payloadType` | R-0058 MUST: one of two forms | not one of the two forms, so not an in-toto attestation | stays global. lane-a's key-relative `payloadType` row was not tested, because the library it used does not read DSSE envelopes (`DL-0012`) |
| DigestSet algorithm name | L446-448 names; R-0032 MUST ignore an unrecognised name | allowed by L603, then ignored. If no other entry matches, the subject matches nothing (L1150-1155), and with no matched subject the attestation is rejected | stays global for interoperability (D-2) |
| `predicateType` | R-0040 MUST case-normalise; unregistered (L671); opaque (L1091) | allowed, and never checked by the validation model (L1159) | **can be key-relative** (D-1) |

That list of four is ours. It counts the fields that the validation model or a
keyword makes a consumer *act* on. The free-form names do not change the
result:

- the ResourceDescriptor `name`;
- `uri`: any URI, with purl and SPDX locations RECOMMENDED (R-0039);
- annotation keys;
- extension field names.

They take key-relative values freely, because no consumer acts on them.
Collision avoidance for annotation and extension names is a naming convention
and nothing more:

<!-- q L122-123 "Extension fields SHOULD" .. "other orgs." -->
> Extension fields SHOULD use names that are unlikely to collide with names used by other orgs.

P1 says private-use ranges give *"escape from a registry, not a namespace"*
(`spec/ARCH-0002-key-relative-naming.md`@bb005ed, P1). This mechanism does not
even reach a registry: no party allocates anything, and no principal is
attached. P5.2's export rule, emit none, applies (§10).

**Media types are the one place a de facto registry appears.** A
predicate-specific media type needs a filename in in-toto's own repository:

<!-- q L789-790 -->
> - `<predicate>` MUST match the [predicate specification filename] without the file extension.

The same rule holds for storage types (R-0069). A predicate type of ours has no
such filename. Its export uses `application/vnd.in-toto+json`, and in storage
`application/vnd.in-toto.<predicate>+dsse` is not available to it (R-0068 is a
SHOULD). The `mediaType` field of a ResourceDescriptor follows RFC 6838's
`x.`, `prs.` and `vnd.` conventions (R-0022). The description bytes of D-6
would need a media type from one of those trees. That is another global name
at the boundary, and `ADR-0001` permits it there.

---

## 8. The envelope: ITE-5, DEC-005 and R-I-03

<!-- q L748-750 -->
> The RECOMMENDED format and protocol for Envelopes are defined per [DSSE v1.0]. Producers MAY use other signature methods and formats that meet the [ITE-5] specification:

<!-- q L752 -->
> - MUST support the inclusion of multiple signatures in a single envelope

<!-- q L757 -->
> - SHOULD NOT require the inclusion of signing key algorithms in the signature

<!-- q L761-762 -->
> - The [Sigstore Bundle], while [supporting DSSE], is not currently [ITE-5] compliant because it requires a _single signature_ in the envelope.[^1]

Five consequences for our documents. Each is inferred from the lines above and
the cited text of ours.

1. **R-I-03's in-toto disjunct needs DSSE.** The source also allows
   `COSE_Sign`, which no document of ours names. An in-toto Statement inside
   `COSE_Sign1` is not a compliant in-toto envelope (L763-764). R-I-03 already
   pairs the in-toto Statement with DSSE and `COSE_Sign1` with CWT claims. That
   pairing is right, and this source is why.
2. **DEC-005's third option** is *"both with a single unsigned payload schema"*
   (`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §7). If that schema
   is an in-toto Statement, its COSE half must be `COSE_Sign`. If it is
   KSA-CBOR, neither half is an in-toto Statement.
3. **The KSA envelope can never be an ITE-5 envelope.** `SPEC-0002` §5 carries
   one signature. Because `says` is inside the TBS, a second speaker makes a
   second TBS. So R-0046 (L752, quoted above, MUST) cannot be met over one
   payload: it is impossible by construction. The `suite`, which names the
   algorithm, is REQUIRED inside the TBS (§7.1) and repeated as a hint in the
   envelope (§5). R-0051 says a format SHOULD NOT require the signing key's
   algorithm *in the signature*; KSA requires it in the signed bytes and the
   envelope instead, which this source neither forbids nor addresses (our
   reading; the source does not define the phrase further). R-0006 §2.5 notes that `ARCH-0001` §6 has no row for the KSA
   envelope. If one is written, this source fills it: not an in-toto envelope,
   by design (row 20).
4. **DSSE carrying KSA-CBOR is a fourth shape that DEC-005 does not list.** The
   payload is the TBS verbatim, and `payloadType` is a type of ours. That
   preserves R-O-05 clause 1, and an in-toto Bundle tolerates it:

<!-- q L882-883 -->
> - Consumers MUST ignore attestations with unrecognized keys, types, subjects, or predicates.

   It is not an in-toto Statement, and DSSE's signature is not the KSA
   signature (5.3, point 4). The source's §9.4.2 is the precedent.
5. **Several signatures carry *n*, never *k*** (row 19). A threshold travels in
   the signed payload under every option, as R-0006 §5.1 already concluded from
   DSSE. "threshold" occurs 0 times in this source.

**The general envelope rule admits encodings that nothing defines:**

<!-- q L779-780 -->
> It MUST take the form `application/vnd.in-toto+<encoding>` to indicate an in-toto [Statement] payload and its serialized `<encoding>` format.

That grammar admits `application/vnd.in-toto+cbor` for a non-DSSE envelope such
as `COSE_Sign`. But the Statement is defined only as a JSON object (L180), and
DSSE's payload MUST be JSON (R-0063). No CBOR form of the Statement appears in
these twelve files. Open question 9.

---

## 9. DigestSet, subject binding and subject matching (R-M-07, R-M-11)

**What v1.1 changed, and why the source calls it compatible.**

<!-- q L1040-1042 -->
> - Clarified that subjects are assumed to be immutable and that it is acceptable to use a non-cryptographic digest (though cryptographic digests are still strongly recommended).

<!-- q L51-53 "This change is" .. "modified semantics." -->
> This change is backwards comptabile because cryptographic digests are strongly recommended to achieve immutability, so any implementations that only support cryptographic `DigestSet` still meet the modified semantics.

**What a subject binds since v1.1:**

<!-- q L436 "Each entry" .. "artifact." -->
> Each entry in a DigestSet MUST be an immutable reference to an artifact.

<!-- q L436-438 "It is STRONGLY" .. "immutability." -->
> It is STRONGLY RECOMMENDED to use a commonly accepted, cryptographically secure digest algorithm to achieve this immutability.

Every subject still MUST have a `digest` (R-0009). That digest is a set of
immutable references, and since v1.1 one of them may be an ARN (L604). **So an in-toto subject binding is an
immutable reference, not necessarily a content digest.** R-M-07 asks for the
latter. Consequences, inferred:

- **The compatibility argument is the import rule.** The source's own argument
  at L51-53 works for a consumer that accepts only cryptographic digests. That
  consumer ignores `arn` (R-0032) and finds no match. An importer that names
  the content-digest algorithms it accepts is in exactly that position. R-0006
  §2.5 proposed the same rule for §6's row: *"the digest map may hold
  non-cryptographic types; import must name the algorithms it accepts under
  R-M-07 (§2.3)"* (`research/0006-mechanism/report.md`@bb005ed, §2.5).
  `ARCH-0001` v0.2.0's row does not carry it (§11).
- **The decision is made per algorithm key, not per Statement version.**
  `_type` does not say whether the producer worked under v1.0's reading or
  v1.1's (J-2).
- **The source's validation model was not updated for v1.1.** It accepts only
  cryptographic algorithms and decodes values as hex:

<!-- q L1127-1128 -->
> - `acceptableDigestAlgorithms`: collection of acceptable cryptographic hash algorithms (usually just `sha256`)

<!-- q L1153-1154 -->
> - `alg` is in `acceptableDigestAlgorithms` AND - `hash(alg, artifactToVerify)` == `hexDecode(value)`

  So it never matches an ARN, and never a value in another encoding. New
  algorithms may use other encodings (L560), and a non-cryptographic value's
  encoding is identifier-specific (L595-596). See §12, SD-3.

**Subject matching.** Matching is by digest alone, and content type plays no
part (L208-209, D-3). The validation model passes `matchedSubjects` to the policy
engine (L1150-1155, L1161). That corresponds to `ARCH-0001` §4.3 step 3's
*"subject digest matches the artifact under consideration"*
(`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §4.3). Outside the
subject, which field a ResourceDescriptor's digest matches is the predicate's
call:

<!-- q L340-342 "The field that" .. "specification." -->
> The field that consumers are expected to match the `digest` against is ultimately determined by the predicate type, and SHOULD be documented by the predicate specification.

A description subject (D-6) needs its predicate specification to say that the
digest matches `content`. That is the same specification of ours that D-5
needs.

**Algorithm agility.** in-toto's agility is several entries for one artifact,
matched on ANY (R-0028, R-0034; D-2). A native target carries one digest with
an algorithm code (`SPEC-0002` §7.2, §12.5). R-M-11's `aliases` set is the
nearest native idea, and it has no KSA form yet (row 9).

---

## 10. Unknown fields, extension fields and versioning (P5, P5.2)

**Where the ignore rule applies:**

<!-- q L106-107 -->
> The following rules apply to [Statement] and any [Predicate] that opt into this model.

So for an in-toto Statement payload, R-0001 binds our importer, as a consumer,
*inside the payload*. P5.2 scoped its collision to the envelope exterior on the
premise that *"the payload interior is ours to govern"*
(`spec/ARCH-0002-key-relative-naming.md`@bb005ed, P5.2). That premise holds
for DSSE carrying a KSA payload. It fails for an in-toto Statement (row 14).
There are two readings, and this file chooses neither:

- **(a) P5 governs inside the foreign payload.** The importer rejects any
  Statement or opted-in predicate that carries an unrecognised field. That is
  the move P5.2 makes for the exterior, where it calls declining to be a
  conforming consumer *"a documented deviation, not a silent one"*
  (`spec/ARCH-0002-key-relative-naming.md`@bb005ed, P5.2). The cost: it
  rejects conforming attestations that carry extension fields (R-0002), and
  attestations written to a later minor version, which R-0085 to R-0087
  promise parse correctly.
- **(b) The foreign rule governs the foreign payload.** The importer ignores
  unknown fields. The cost: our verifier then skips what it does not
  understand. `SPEC-0002` §13.5 forbids that for KSA statements, and it does
  not say whether it reaches a foreign payload.

Open question 1.

**Export.** By P5.2's logic, *emit none*: no extension fields and no
`annotations` in an exported Statement. A field that must be understood goes
into the predicate, under a specification of ours that says so (D-5).

**R-0002 lets extension fields into any JSON object, a DigestSet included.** A key added
there is read as an algorithm name, and is ignored if unrecognised (R-0032).
That is consistent with R-0001, and no special case arises (inference).

**Ignoring at the level of a collection.** A Bundle consumer MUST ignore lines
and attestations it does not recognise (R-0075, R-0076). Ours treats
unverifiable statements the same way and also reports them: *"Unverifiable
statements are reported in the answer's reasons but contribute nothing."*
(`spec/SPEC-0004-ksa-trust-evaluation.md`@bb005ed, §5.1). The two agree, and
ours adds the report.

**Versioning.** J-2 gives the rule we reject. One concrete case shows what a
MINOR release did at the envelope layer:

<!-- q L1035-1036 -->
> - Expanded the allowed values for the envelope's `payloadType` field to `application/vnd.in-toto.<predicate>+json`. See [Envelope Fields].

Since v1.2 widened the allowed values, before v1.2 the only allowed value was the
generic type. A consumer written to v1.1's text that enforced it rejects every
v1.2 envelope that uses a predicate-specific type. It fails closed. But the
compatibility rules never covered the envelope (L1060-1061), so the source
gives no guarantee either way. Ours makes the same event explicit: *"An unknown
suite is unverifiable, never silently accepted; an unknown kind or field is
invalid."* (`spec/SPEC-0002-ksa-core.md`@bb005ed, §13.5). And a registry entry
*"MUST NOT change the canonical bytes of any existing statement"*
(`spec/SPEC-0002-ksa-core.md`@bb005ed, §12).

---

## 11. `ARCH-0001` §6: the in-toto row (R-I-01, R-I-03)

The row today: *"Subjects = artifacts. **Export loss:** a `description` subject
(R-M-11) has no in-toto digest-set form. `predicateType` URI ↔ `type-ref` is a
lossy mapping (`ARCH-0002` P1)"*
(`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §6). R-I-01 asks for
*"what is preserved, dropped, or inferred"*
(`spec/ARCH-0001-authorization-attestation.md`@bb005ed, §5.2). What follows is
a **draft** for mofn#110 and WP3. It decides nothing.

**Export: a native `attestation` becomes an in-toto Statement in DSSE.**

| native (`SPEC-0002`) | in-toto | status |
|---|---|---|
| `kind` 4, `attestation` | the predicate type of ours (D-1) | inferred: the kind is carried by `predicateType` |
| `kind` 6, 9, 10, 11 (`revoke`, `review`, `approve`, `aggregate`) | — | open question 12. `revoke` is not monotonic (J-6) |
| `says` | the DSSE signer, with `keyid` as a hint | preserved by the signature, not in the payload (D-4) |
| `suite` | — | dropped. DSSE does not carry the algorithm, and R-0051 says not to require it |
| `this` type 2 | `subject[0].digest`, under `sha256`, `sha384` or `sha512` | preserved |
| `this` type 5 | — | not exportable (D-7, R-0009) |
| `this` type 6 | `subject[0]`: `digest`, `content` and `mediaType` | form kept, meaning dropped (D-6) |
| `this` types 1, 3, 4 (key, statement, definition) | a subject digest of a `kid`, a TBS or a DefinitionId | in-toto reads it as an artifact digest. For a statement or definition, the referent's bytes are KSA-CBOR, which the export does not carry (row 30). For a key, the digest can be computed only from the key's encoding under our suite |
| `valid` | the predicate, under a must-understand specification, or nothing | D-5 |
| `body.has` | the predicate | preserved, under our predicate specification |
| `template` | the predicate, under a must-understand specification | D-5 |
| `type-ref` | `predicateType` URI | identity preserved, meaning not resolvable (D-1) |
| statement digest | — | dropped. in-toto has no attestation identifier (5.2, point 3) |
| — | `_type`, and `payloadType` `application/vnd.in-toto+json` | added constants |

**Import: an in-toto Statement in DSSE becomes native evidence.**

| in-toto | native | status |
|---|---|---|
| verified signer key | `says` = the key's `kid` | inferred. It needs a suite for the key's algorithm (D-4) |
| *n* verified signatures | *n* attestations; a threshold counts distinct kids | inferred (D-4, row 18) |
| `keyid` | a hint | `ADR-0005`'s import rule conflicts (D-8) |
| *N* subjects | *N* targets, so *N* attestations | inferred (D-3) |
| DigestSet | one of `sha256`, `sha384` or `sha512` becomes target type 2 | the rest dropped. A non-cryptographic entry never satisfies R-M-07 (J-4, §9) |
| `uri`, `downloadLocation` | a locator, as a hint | preserved as a hint, never alone (R-M-11) |
| `name`, `annotations` | — | dropped, or kept for display |
| `predicateType` | a `type-ref` under a definition the importer authors | lossy (D-1) |
| `predicate` | attributes under that definition | lossy. Unknown fields: open question 1 |
| validity | — | none. The Statement has no field, and a predicate may carry one |
| Bundle order | — | irrelevant (R-0077, `SPEC-0004` §3) |
| the attestation itself | statement set | **no path.** `SPEC-0004` §5.1 admits only statements verified under `SPEC-0002` §9 (open question 6) |

**Draft cell for the row, for mofn#110:**

> Subjects are artifacts bound by a DigestSet. Since v1.1 an entry may be
> non-cryptographic, so an import names the content-digest algorithms it accepts
> (R-M-07). One Statement may carry *N* subjects and *n* signatures. The speaker
> is the verifying key, not a Statement field. **Export loss:** a `description`
> subject exports as the description document. `valid`, `kind` and `template`
> need a must-understand predicate specification. A locator-only subject does
> not export. `predicateType` ↔ `type-ref` is injective on export and lossy on
> import. Envelope: DSSE (`COSE_Sign1` is not ITE-5 compliant).

That blockquote is our draft wording, not a quotation of either document. It
carries no marker, because it quotes nothing.

---

## 12. Source defects found in this pass

These are recorded for the verify and cross-check passes, and for anyone
filing upstream. None is fixed here: a source defect is reported, never
papered over. **The numbering is this file's own**: SD-2 here is not
normative.md's SD-2. Each heading names its normative.md entry, and
normative.md's Crosswalk maps all four lanes' lists.

**SD-1** (normative.md SD-2). **The validation model's `payloadType` check rejects every envelope.**

<!-- q L1146 -->
> - Reject if (`envelope.payloadType` != `application/vnd.in-toto+json` OR `envelope.payloadType` does not match `application/vnd.in-toto.<predicate>+json`)

There are three cases:

- the generic type makes the first disjunct false. It does not match the
  predicate-specific pattern, because that pattern needs a `.` after
  `in-toto`, so the second disjunct is true;
- a predicate-specific type makes the first disjunct true;
- any other value makes the first disjunct true.

The condition holds for every input. AND was presumably meant: reject when
neither form matches. The model has no keyword, so this binds nobody. It is
still the source's only verification procedure.

**SD-2** (normative.md SD-3). **`statement.type` should be `_type`.**

<!-- q L1149 -->
> - Reject if `statement.type` != `https://in-toto.io/Statement/v1`

The Statement's field is `_type` (L183). Read literally, a conforming Statement
has no `type`, so this step rejects it too.

**SD-3** (normative.md SD-8, SD-12). **The validation model was not updated for v1.1** (§9). It accepts only
cryptographic algorithms (L1127-1128) and compares hex (L1154). It cannot match
the source's own ARN example (L604), or a value in another encoding (L560,
L595-596).

**SD-4** (normative.md SD-4). **`dirHash` or `dirHash1`?** The heading at L450 names the key
`dirHash`, and the example writes another:

<!-- q L464 -->
> `{"dirHash1": "2a1bb6127fb481c60f67692e22285fb306f3c6ffe62075e0ccf674d7c3adcb8f"}`.

A consumer that accepts one name ignores the other (R-0032). The base64 and hex
forms in the example agree: re-encoding by script gives
`h1:Khu2En+0gcYPZ2kuIihfswbzxv/mIHXgzPZ018Oty48=`, as at L463.

**SD-5** (normative.md SD-5). **The republished Bundle changes signed `payloadType`s under unchanged
signature placeholders** (L931 to L984, and L963 to L986). See §6. R-0056 makes
`payloadType` signed, so either the lines were re-signed, which the text never
says, or the example predates v1.2's predicate-specific types and was half
updated. The source does not say which.

**SD-6** (normative.md SD-12). **A ResourceDescriptor's `digest` is still described as cryptographic:**

<!-- q L280 "A set" .. "artifact." -->
> A set of cryptographic digests of the contents of the resource or artifact.

Since v1.1 the DigestSet's own definition is wider:

<!-- q L415-416 -->
> Set of one or more cryptographic digests, or other immutable references, for a single software artifact or metadata object.

and §5.2.3 allows non-cryptographic identifiers.

**SD-7** (normative.md none; R-0214 inferred). **The consumer MUSTs leave the order unstated** (R-0062, R-0072). R-0050
and the validation model put verification first (A-1).

**SD-8** (normative.md SD-9). **Unclear.** When both `uri` and `name` are set:

<!-- q L346-347 "The `name` SHOULD" .. "universally." -->
> The `name` SHOULD be compared to the `uri` to match the descriptor against the resource or artifact referenced universally.

`name` is local to the attestation (L345-346). It is not clear what comparing
a local name against a global URI achieves. This is R-0027 as written.

**SD-9** (normative.md SD-8). **The validation model covers one artifact against one attestation.**
Its own note at L1120 says that several artifacts, and several attestations,
are not explained. *N*-element subjects, verdicts from several signatures
beyond `attesterNames`, and Bundles have no processing model in the source.

**SD-10** (normative.md SD-27). **v1.2 changed the envelope in a MINOR release** (L1035-1036). The
versioning rules cover the Statement and predicates only (L1060-1061). See
§10.

---

## 12b. Our documents' readings of in-toto, checked against the primary source

Every item is a defect in **our** wording, or a confirmation of it. None
changes a decision.

1. **`record.yaml` `usefulness.reason`** says in-toto's parsing rules
   (*ignore unknown fields*) *"are the opposite of condition (2)"*
   (`records/community/in-toto-attestation-v1/record.yaml`, this library). More
   precisely, they are the opposite of P5's unknown-field clause and of
   `SPEC-0002` §7.1 and §13.5. Condition (2) concerns *"non-canonical input
   rather than normalising it"* (`research/0006-mechanism/report.md`@bb005ed,
   §3.2). in-toto has no canonical form, so condition (2) is vacuous for it
   (row 27). This is for the record's owner. This lane does not edit
   `record.yaml`.
2. **R-0006 §2.3** gives as its example *"or a `gitCommit` entry satisfies
   R-M-07 in form and not in substance"*
   (`research/0006-mechanism/report.md`@bb005ed, §2.3). The source defines the
   git keys as SHA-1 or SHA-256 over a defined object encoding (L517-534), so
   they are cryptographic digests of git objects. What is weak is SHA-1, and
   the key's silence about which hash it holds (D-2). The source's own
   non-cryptographic example is an ARN (L604). §2.3's conclusion stands; its
   example is the wrong one.
3. **R-0006 §2.2 and §2.5** relied on `slsa-1-2` for *"non-cryptographic digest
   types"*
   (`research/0006-mechanism/report.md`@bb005ed, §2.2). The primary source confirms it: R-0036 (L571-573) and the v1.1
   changelog (L1040-1042).
4. **The word "registry".** R-001 §11.4 says *"allocates it from a registry (in-toto
   predicate types, COSE algorithms)"*
   (`research/0001-signatures-and-attestation/report.md`@bb005ed, §11.4).
   `ARCH-0001` §3.2 lists *"Predicate registry: SLSA provenance, VSA, SPDX,
   CycloneDX, link"* (`spec/ARCH-0001-authorization-attestation.md`@bb005ed,
   §3.2). The source says TypeURIs are not registered (L671), and vetting is a
   MAY (R-0043). What in-toto keeps is a list of predicate specifications in
   its own repository. That list governs only the predicate-specific media
   types (R-0059, R-0069). P1's conclusion is unaffected: a TypeURI is still a
   global name (J-3). But P1 says *"Tag numbers, header labels, claim keys and
   predicate-type URIs are all global identifiers handed out by a central
   party"* (`spec/ARCH-0002-key-relative-naming.md`@bb005ed, P1). That does not
   describe in-toto's predicate types, because nobody hands them out.
5. **lane-a finding 4** (`prototype/lane-a/README.md`@bb005ed; `DL-0012`) says
   the renamed digest name passes. That is a property of
   `in-toto-attestation` 0.9.3's `validate()`. Under the specification, a
   renamed digest key is unrecognised (R-0032), and the validation model
   matches no subject (L1150-1155). A verifier that follows the source rejects
   that Statement. The README scopes itself correctly, *"One library per
   format"* (`prototype/lane-a/README.md`@bb005ed). The finding must not be read as in-toto accepting key-relative
   digest names. Its key-relative `payloadType` row breaks R-0058 (§7).
6. **lane-a's DSSE sample** calls `payloadType` a *"registered media type"*
   (`prototype/lane-a/02_dsse_intoto.py`@bb005ed). "IANA" occurs 0 times in
   the source, and the source never says `application/vnd.in-toto+json` is
   registered. That is unverified here, not refuted.
7. **P5.2 and R-0006 §5.2** scope the DSSE collision to the envelope exterior.
   That is true when DSSE carries a KSA payload. It is false for an in-toto
   Statement payload (row 14, §10).
8. **`ARCH-0001` §6's in-toto row** omits the import note R-0006 §2.5 proposed
   (§9, §11).
9. **`docs/extraction.md`** (this library) says no DEC-002 ADR exists. That
   has been stale since `ADR-0004` (2026-10-25).

---

## 13. Open questions

Each names what would settle it. None is settled here.

1. **Unknown fields inside an in-toto payload, on import** (row 14, §10).
   Reading (a) rejects them, P5 governing; reading (b) ignores them, R-0001
   governing. P5.2 and the R-I-01 table own it.
2. **Which DigestSet entries satisfy R-M-07 on import, which one becomes the
   target, and whether every computable entry is checked** rather than R-0034's
   ANY (D-2, §9). Are `sha3_*` or SHA-256 `gitCommit` content digests for
   R-M-07? WP3 and mofn#110.
3. **The `predicateType` URI form for export:** built from the DefinitionId,
   exact but new on every revision, or from definer, name and major version,
   which is stable and pins nothing (D-1). WP3, read against `ADR-0007` and
   `SPEC-0003` §11.3.
4. **Where the speaker travels in an export** (D-4): the predicate, an
   extension field, or the envelope only. The rule in P5.2 and `ADR-0005`, that the principal
   travels in the payload, was written for KSA payloads. WP3, then `ADR-0005`'s successor if
   the rule changes.
5. **`ADR-0005`'s import rule against a foreign `keyid` format** (D-8, row 16).
   An accepted ADR changes only by being superseded.
6. **No path for an imported attestation into evaluation.** `SPEC-0004` §5.1
   admits only statements verified under `SPEC-0002` §9, and an import never
   is. §6 marks in-toto **I** (§11). `SPEC-0004` and WP3.
7. **The identity of an imported attestation.** One envelope, *N* subjects and
   *n* signers, with no TBS and so no statement digest. How does a `review`,
   `revoke` or `aggregate` name one (D-3)? WP3.
8. **DEC-005's scope.** No document of ours names `COSE_Sign`. An in-toto
   Statement in `COSE_Sign1` is non-compliant, and DSSE carrying KSA-CBOR is
   not a listed option (§8). DEC-005.
9. **`application/vnd.in-toto+<encoding>`** admits non-JSON encodings, and no
   CBOR form of the Statement exists in the source (§8). It matters only if a
   CBOR in-toto export is ever wanted (R-I-03).
10. **The must-understand predicate specification** that carries `valid`,
    `kind` and `template` (D-5). Who writes it, and where does it live? It
    cannot be one of in-toto's predicate specifications unless in-toto lists
    it, which decides whether a predicate-specific media type is available
    (§7). WP3.
11. **R-O-05 clause 3 for imports**, which have no canonical bytes. And should
    the R-I-01 table record that an exported attestation's verify-first
    guarantee comes from DSSE, not from in-toto's normative text (A-1, §6)?
    The R-I-01 table.
12. **Exporting kinds whose target is a key, statement or definition**, and
    exporting `revoke` (row 30, J-6, §11). Are they in R-I-03's scope at all?
13. **Timestamps with fractional seconds** in an imported predicate, against
    `SPEC-0002` §4.4's whole-second time (§5.1). WP3, if any imported
    predicate carries a Timestamp.
14. **Which bytes a `description` subject's export digest covers:** the target
    array or its `value` (D-6). `SPEC-0002` §7.2.
15. **R-M-05's "ordered cert set"** is weaker than `SPEC-0004` §3, and weaker
    than this source's R-0077 (A-4). `ARCH-0001` §5.5 is where such a gap is
    recorded.

---

## 14. What this file decides

Nothing. *"Only an ADR accepts a decision."* (`CONTRIBUTING.md`@bb005ed, §5).
Each adaptation and open question names what would settle it. What it holds is
evidence for:

- whoever next reads `ADR-0004`. The option set lacked in-toto's actual
  practice (§5.3);
- `ADR-0005`'s successor, on foreign `keyid`;
- P5.2's scope, on the payload interior;
- DEC-005;
- the in-toto and DSSE rows owned by mofn#110;
- mofn#144, on locator-only subjects;
- WP3's mapping specification.

None of it reopens DEC-002.

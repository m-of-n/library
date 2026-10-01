---
record: rfc-9052
kind: design-notes
title: "rfc-9052 — bearing on our design"
extracted: "2026-09-30"
reviewed_by: ""
---

**Marker convention.** `[9052 §n]` = stated in RFC 9052 at that locator.
`[9338 §n]` = stated in RFC 9338, which updates RFC 9052 and forms STD 96 with
it; it is *not* the source of this record and is cited only where RFC 9052
points outside itself. `[8949 §n]` and `[8392 §n]` = stated in RFC 8949 (CBOR)
and RFC 8392 (CWT), cited only where the tag question reaches outside RFC 9052.
`[ours]` = one of our documents, cited by id.
`[inference]` = analysis by the extractor, not stated in any source and not
decided by anyone. Every `[inference]` is also listed in the last section.

**Decision status, stated once so nothing below over-claims.** D-3
(`project/meetings/2026-09-28.md`) narrowed DEC-002 to option 5 — CBOR data
model, no IANA tags, COSE as export only, type identity `(defining key, label)`
per ARCH-0002 P1, YAML as the human form with a canonical one-way mapping, and
option 2 retained only as a comparison fixture. **The ADR is not written.**
DEC-002 is still listed open in `ARCH-0001` §7, and option 5 exists only as a
*proposal* in `ARCH-0001-PROPOSAL-v0.2.0` §3.3. **DEC-005 (the envelope for
`ArtifactStatement`) is also open**; D-3 constrains it to COSE-as-export but
does not close it. R-M-12 *is* accepted (`ADR-0001`), and ARCH-0002 P1 with it;
P2–P7 are provisional per D-2, and P4 is held. Nothing in this file is
normative. It is the buildable mapping that the DEC-002 ADR and the D5 fixture
package (Oct 28, `PLAN-0003`) should be written against.

---

## What we adopt

1. **`COSE_Sign1` as the shape of the export** `[9052 §4.2]`. Four-element
   array: protected `bstr`, unprotected map, payload `bstr`/`nil`, signature
   `bstr`. One speaker, one signature — which is exactly the arity of *A says B
   has C* `[ours: ARCH-0002 P2]`. We adopt the structure; §4 warns that
   `COSE_Sign` and `COSE_Sign1` are not interconvertible, because the context
   string is inside the signature computation, so the choice is permanent per
   artifact.

2. **`Sig_structure` discipline** `[9052 §4.4]`. The signed bytes are a
   constructed CBOR array with a leading context text string (`"Signature1"`),
   not a concatenation. This is the same defence DSSE's Pre-Authentication
   Encoding provides, and it is the thing `R-O-05` asks for
   `[ours: ARCH-0001-PROPOSAL-v0.2.0 §3.4, §7]`. §4.3 additionally spells out
   the concatenation-ambiguity failure ("AB"+"CDE" vs "ABC"+"DE") that any
   hand-rolled to-be-signed construction walks into. Adopt the rule, adopt the
   reasoning, cite it rather than re-deriving it (`R-O-03`).

3. **Sign the bytes you received; never re-canonicalize to verify**
   `[9052 §3]`. The protected bucket is a `bstr` wrapping an encoded map
   specifically so that "all parties" need not "be able to do a common
   canonical encoding of the map for input to cryptographic operations", and
   §3 notes that an intermediate that decodes and re-encodes "will result in a
   failure to verify unless the re-encoded byte string is identical". This is
   independent standards-track support for `R-O-05`'s ordering — verify first,
   decode second — and we adopt it verbatim as the rule for our own importer:
   **keep the bytes**.

4. **The narrowed deterministic encoding rules** `[9052 §9]`: aligned with the
   Core Deterministic Encoding Requirements of RFC 8949 §4.2.1; definite
   lengths only; the encoded argument at its minimum possible length (`1` is
   `0x01`, not `0x1801`); and applications MUST NOT generate, and MUST NOT
   parse and process, a map with a duplicated label. Adopted for **both** the
   native canonical form and the export. `R-O-03` requires citing a
   canonicalization rather than inventing one; RFC 8949 §4.2.1 narrowed by
   RFC 9052 §9 is that citation, and it is the same rule the
   domain-of-discourse hash needs `[ours: ARCH-0002 P4]`.

5. **Reject, never repair** `[9052 §3, §9]`. A repeated label means the message
   "MUST be rejected as malformed"; an attribute found in the protected bucket
   wins and the unprotected bucket is consulted "only if" it is absent; a
   `crit` entry naming a label that is not in the protected bucket "is a fatal
   error". These are the same posture as `[ours: ARCH-0002 P5]` — three levels,
   none skippable, failure is never repair — and P5's own worked example
   (CVE-2025-59420, ignored `crit`) is a COSE failure. Adopt the posture and
   cite COSE as prior art for it.

6. **The obligation to profile** `[9052 §10]`. RFC 9052 "is designed to provide
   a set of security services but not impose algorithm implementation
   requirements", and it "is intended that a profile of this document be
   created". **Our export mapping is that profile**, and §10's checklist is
   what it has to answer: which messages, which header parameters, how external
   authenticated data is encoded, which algorithms, and how algorithms are
   discovered or preconfigured. §5 below is that answer.

7. **COSE has no digest structure, deliberately** `[9052 §1]`. "One feature
   that is present in CMS that is not present in this standard is a digest
   structure. This omission is deliberate," with the reasoning that each
   protocol wants a different field set, possibly non-adjacent, possibly with a
   locator to where the hashed bytes can be obtained. That is a precise
   description of our `ArtifactId` with its `digest` / `locator` / `description`
   modes `[ours: R-M-11]`. We adopt the conclusion: **`R-M-07`'s content digest
   lives in our payload and has no COSE home**, and that is by COSE's design,
   not an oversight in ours.

8. **COSE says authorization is the application's job** `[9052 §4.4, §12]`.
   §4.4: "the application performs the appropriate checks to ensure that the key
   is correctly paired with the signing identity and that the signing identity
   is authorized before performing actions." §12 asks "What are the permissions
   associated with the key owner?" and leaves it open. We adopt this as the
   framing of what m-of-n is: COSE is the envelope, and the reduction
   `[ours: ARCH-0002, reduction note]` is the part COSE names and declines to
   specify.

---

## What we adapt, and how

| COSE mechanism | our use | how it is adapted |
|---|---|---|
| `kid`, label 4, `bstr` `[9052 §3.1]` | speaking-key identity | **Demoted to a hint.** RFC 9052 is explicit: "Applications MUST NOT assume that `kid` values are unique", "The internal structure of `kid` values is not defined", "This is not a security-critical field." Our speaker *is* the key `[ours: ARCH-0002 P2]`, so identity cannot be a hint. The authoritative `KeyId` stays in the payload; `kid` mirrors it and MUST match or the export is rejected. |
| `content type`, label 3 `[9052 §3.1]` | the authenticated type indicator `R-O-05` requires | Adapted to mean *the native envelope format*, not the statement's vocabulary. It cannot carry `(defining key, label)`; see §1 row 3 below. Requires one registered media type at the boundary. |
| `crit`, label 2 `[9052 §3.1]` | must-understand | Adapted down. `crit` names **header labels only**, and only ones present in the protected bucket. It cannot make a consumer reject an unknown *payload* field, which is what P5 actually demands. We emit `crit` for the protected labels a consumer must process and accept that P5 does not survive the boundary (§4 below). |
| protected / unprotected split `[9052 §3]` | — | Adapted to **everything we emit is protected; the unprotected bucket is present and empty**. §3 requires both buckets to be present, so the empty map is emitted, not omitted. The one exception is a countersignature, which RFC 9338 §2 requires to be unprotected — and §6 below declines to use it. |
| layering `[9052 §3]` | — | COSE's rule is that "one should be able to process any given layer without reference to any other layer". Our statements are not layered. Adapted by flattening: one layer, one speaker, no recipient structures. |
| message identification `[9052 §2]` | — | Adapted to context-determined identification (§2 method 1) inside our own container, with a tagged `#6.18` variant for hand-off to a COSE-native consumer. **Proposed, not decided — it is a DEC-005 call.** See §3. |
| `external_aad` `[9052 §4.3, §4.4]` | — | Adapted to *pinned empty*. §4.3 makes the construction the application's responsibility and enumerates the ways it goes wrong; the cheapest correct answer is to define it as the zero-length byte string and put everything in the payload. |
| `COSE_Key` `[9052 §7]` | key material on the wire | Interchange only. Its labels come from the "COSE Key Common Parameters" registry `[9052 §11.2]` and `kty` MUST be present, so it is registry-dependent by construction and cannot be the native key form under `R-M-12`. Relevant to DEC-003, which is still open. |

---

## What we reject, and why

1. **COSE header parameters as a native extension point.** Rejected by
   `R-M-12` / ARCH-0002 P1, and RFC 9052 supplies two independent reasons of its
   own. First, the label space is *typed*: "label = int / tstr" and "the
   presence a label that is neither a text string nor an integer is an
   error" `[9052 §1.5]` (the missing "of" is the RFC's own typo, kept verbatim). A pair `(defining key, label)` is not an `int` and not
   a `tstr`, so **our extension points are not expressible as COSE header
   labels at all** — this is a structural bar, not only a governance
   objection `[inference]`. Second, the labels are allocated `[9052 §3, §11.1]`
   under policies §11.6 describes as Expert Review with point-squatting
   discouraged. Private-use ranges are no answer for the reason `ADR-0001`
   gives: they are escape from a registry, not a namespace.

2. **CBOR tags in the native form.** Rejected by D-3 — and §3 below shows the
   rejection has to be written as a decoder rule (major type 6 MUST NOT appear)
   rather than as an omission, or an imported tagged object satisfies our decoder
   silently `[8949 §4.2.2]`.

3. **`COSE_Mac0` / `COSE_Mac` and the encryption structures** `[9052 §5, §6]`.
   Rejected as export targets. §8.2: MACs "provide either no or very limited
   data origination" and "cannot be used to prove the identity of the sender to
   a third party." A statement whose whole content is *A says* cannot be carried
   by a structure that does not carry who said it. Encryption is orthogonal: our
   statements are public assertions, and confidentiality is not in ARCH-0001's
   goals.

4. **Signature with message recovery** `[9052 §8.1]`. Rejected. It moves part of
   the message content into the signature, so "the message content is not fully
   available until after a signature has been validated", which contradicts
   `R-O-05`'s "the signed payload SHALL be the canonical encoding, verbatim".
   §4.1 adds that the transmitted payload shrinks by the recovered bytes. No
   such algorithm is defined for COSE yet `[9052 §8.1]`, so this costs us
   nothing today; it is recorded so nobody adopts one later without noticing.

5. **Detached payload** (`nil` in the payload slot, `[9052 §4.1]`). Rejected for
   the D5 fixture package. §4.4 item 5 signs the full payload regardless, so
   detachment would mean a fixture whose bytes do not contain what they attest
   to.

6. **The RFC 8152 countersignature (label 7, and `CounterSignature0`).**
   Rejected. RFC 9052 §1 records that "the description of the security
   properties of countersignatures was incorrect for the `COSE_Sign1`
   structure" and removed the text; §11.1 leaves labels 7 and 9 pointing at
   RFC 8152. §3.1 notes new implementations must still *understand* label 7 for
   backward compatibility — an obligation on a COSE library, not on our model.
   §6 below covers the current primitive.

7. **Exporting a threshold speaker as `COSE_Sign1`** — rejected as impossible,
   not as unwanted. See §1 row 10 and §4.

8. **Using `crit` to carry P5.** Rejected as out of scope for the mechanism; see
   the adapt table and §4.

---

## Mapping to our decisions

### 1. Field-by-field mapping to `COSE_Sign1`

Our statement model is `ARCH-0001` §4.1–§4.2 as constrained by ARCH-0002 P2 and
P6: one form, `A says B has C`, with the five §4.2 kinds as *functions over*
that form, discriminated by a key-relative predicate type. The table maps that
form onto `COSE_Sign1` `[9052 §4.2]`.

| our field (source) | COSE location | COSE label / slot | rule, and what we do when there is no COSE home |
|---|---|---|---|
| the statement itself — native canonical CBOR, signed `[R-O-05]` | **payload** | slot 3, `bstr` `[9052 §4.2]` | The payload **is** the native form, byte-for-byte, including its native signature. COSE carries it; COSE does not restate it. Everything else in the table is a mirror, and every mirror is non-authoritative and MUST equal the payload or the export is rejected `[inference]`. |
| speaker / issuer `Principal`, a `Key` or `KeyId` at signature time `[ARCH-0001 §4.2, R-O-01]` | payload (authoritative) **+** unprotected `kid` (hint) | slot 3 **+** label 4, `bstr` `[9052 §3.1]` | RFC 9052's own example puts `kid` in the unprotected bucket `[9052 C.2.1]`. We follow it, because promoting a hint into the protected bucket would suggest it is identity. **Raw key material has no COSE header home in RFC 9052** — `COSE_Key` is §7, a separate object, not a header parameter — so a `Key`-valued (not `KeyId`-valued) principal travels in the payload only. DEC-003 is open and decides the `KeyId` bytes. |
| statement type identity **`(defining key, label)`** `[ARCH-0002 P1, R-M-12]` | payload, both components, as ordinary map entries | slot 3 | **No COSE home, structurally.** A header label must be `int` or `tstr` `[9052 §1.5]`; a pair is neither. Flattening it to one `tstr` would discard the very distinction P1 exists to make — key *K*'s `build-provenance` and key *K′*'s are different types — unless the flattening is injective and reversible, which means embedding the defining key's digest in the string. We do not do that at the boundary: the pair stays in the payload and the loss is recorded under `R-I-01`. |
| authenticated type indicator `[R-O-05]` | **protected** `content type` | label 3, `tstr` / `uint` `[9052 §3.1]` | Identifies *the native envelope format*, not the vocabulary. Values come from the CoAP Content-Formats or Media Types registries `[9052 §3.1 Table 3]`, so emitting it at all costs **one media-type registration** at the boundary. This is the single cheapest registry dependence we take and the one with the clearest payoff: a COSE consumer learns that the payload is an m-of-n statement rather than arbitrary bytes. §3 of `ARCH-0001-PROPOSAL-v0.2.0` already flags that the type indicator is itself an extension point and so is key-relative natively; the media type is its export mirror, not its definition `[inference]`. |
| subject `B` — `ArtifactId`, modes `digest` / `locator` / `description` `[R-M-11]` | payload | slot 3 | No COSE home. COSE has no subject concept. CWT's `sub` is a token subject in a different document and a different registry and must not be overloaded to mean "the artifact this statement is about" `[inference]`. Total loss to a COSE-only consumer. |
| content digest, at least one, always `[R-M-07]` | payload | slot 3 | No COSE home **by COSE's design** `[9052 §1]`, which points to RFC 9054 for one possible digest structure. We keep ours in the payload. If a COSE-native digest is ever wanted, RFC 9054 is the place to look, and it is outside this record. |
| validity `{not_before?, not_after?, online_check?}` `[ARCH-0001 §4.1, R-M-09]` | payload | slot 3 | **No home in RFC 9052.** §3.1 Table 3 defines labels 1–6 and none is temporal. `exp` / `nbf` / `iat` are CWT claims (RFC 8392) and carrying them in a COSE *protected header* needs the "CWT Claims" header parameter, which is **not defined in RFC 9052** — `ARCH-0001` §3.2's "COSE protected header 15" is a claim about a different document and should be re-cited there `[inference]`. `online_check` has no analogue in COSE, CWT or anywhere adjacent: pure loss. |
| tag / authorization payload, and its intersection semantics `[ARCH-0001 §4.1, DEC-004, ARCH-0002 P7]` | payload | slot 3 | No COSE home, and none is wanted: §4.4 and §12 put authorization outside COSE explicitly. Total loss to a COSE-only consumer, which is why §4 below insists the export is not a security-equivalent form. |
| `delegate` flag, and `(Domain, Topic)` scope `[ARCH-0001 §4.2, ARCH-0002 P2]` | payload | slot 3 | No COSE home. |
| threshold speaker `{k, n, members}` `[R-M-06]` | **not exportable as `COSE_Sign1`** | — | A *k*-of-*n* **subject** is payload data and exports fine. A *k*-of-*n* **speaker** needs `COSE_Sign` with *n* `COSE_Signature` entries `[9052 §4.1]`, and §4 forbids converting between the two structures. D-3 and DEC-005 name `COSE_Sign1`, so in this increment a threshold-spoken statement has no export. Recorded as an interchange gap, not resolved here. |
| domain-of-discourse hash `[ARCH-0002 P4, held per D-2]` | payload | slot 3 | No COSE home. Key-relative and hash-identified by construction. |
| algorithm | **protected** `alg` | label 1, `int` / `tstr` from the "COSE Algorithms" registry `[9052 §3.1 Table 3]` | See §2. `[9052 §3.1]`: this parameter "MUST be authenticated where the ability to do so exists", and for `COSE_Sign1` it does (`body_protected` and `external_aad` are both inside `Sig_structure` `[9052 §4.4]`), so **`alg` may not sit in the unprotected bucket**. The §3.1 example list names `COSE_Sign` and `COSE_Mac0` and not `COSE_Sign1`; reading the MUST as binding for `COSE_Sign1` is our reading of the general clause `[inference]`. |
| must-understand set | **protected** `crit` | label 2, `[+ label]` `[9052 §3.1]` | Emit only for protected labels a consumer must process. §3.1's guidance: integer labels 0–7 SHOULD be omitted, so a `crit` listing only `alg` and `content type` would be empty by rule — meaning in our profile `crit` is normally **absent**, and §3.1 requires that if present the array have at least one value `[inference]`. |
| native signature | inside **payload** | slot 3 | The native signature travels as part of the native bytes. It is **not** the COSE signature. |
| COSE signature | **signature** | slot 4, `bstr` `[9052 §4.2]` | A second, distinct signature over `Sig_structure`. See §1a. |
| — | **unprotected** bucket | slot 2, map | Present and empty (`0xa0`). §3 requires both buckets; ours holds `kid` and nothing else, or nothing at all. |

#### 1a. The signature does not port — the export re-signs

This is the load-bearing consequence of the table and it must be settled before
any fixture is written `[inference throughout this subsection]`.

Our native signature is over our canonical native bytes with our own
authenticated type indicator `[R-O-05]`. The COSE signature is over
`Sig_structure = ["Signature1", body_protected, external_aad, payload]`
`[9052 §4.4]`. These are different byte strings by construction — the context
string alone guarantees it. **A native signature therefore cannot be lifted
into `COSE_Sign1`'s signature slot**, and there is no unsigned `COSE_Sign1`:
§4.2's CDDL makes `signature : bstr` mandatory.

Two ways out, and they differ only in whose key signs the COSE layer:

- **Re-sign with the speaking key.** Genuine interoperability: a COSE-native
  verifier verifies a signature by the key that actually said the thing. Costs:
  the private key must be present at export time, so export is no longer a pure
  function of a verified statement; and the speaker now has two signatures over
  two byte strings carrying one claim. Under ARCH-0002 P2 — "the cryptographic
  act *is* the saying" — that is a second saying, and the model must be clear
  that it is a re-statement of the same claim rather than a new one. The
  authenticated type indicator inside the payload plus COSE's `"Signature1"`
  context string keep the two from being confused for one another.
- **Wrap with the exporter's key.** Export becomes a pure function of bytes and
  needs no private key from the speaker. Costs: a COSE-only verifier learns only
  that *the exporter* vouched for the bytes. The original saying is still
  verifiable, but only by our code.

**A consumer can tell which case it has without any new header parameter**: the
key that verifies the COSE signature either is, or is not, the key whose `KeyId`
the payload names. No new label means no new registry entry — which is the
`R-M-12`-respecting answer, and a small argument that key-centric identity makes
an extension point unnecessary here. Recommended default: **re-sign when the
speaking key is available, wrap otherwise, and never emit both.** Not decided;
Open question 1.

### 2. The `alg` problem

**What RFC 9052 requires.** `alg` is label 1 and "The value is taken from the
'COSE Algorithms' registry" `[9052 §3.1 and Table 3]`; the concrete values live
in RFC 9053 (the RFC's own example is `1:-7`, annotated "ECDSA 256"
`[9052 C.2.1]`). The signature computation takes `alg` as an explicit input
`[9052 §4.4 steps 3]`. So there are **two distinct registry dependences**, and
they must not be argued as one:

- the **label space** — that "algorithm" is named by integer `1` at all — which
  is the "COSE Header Parameters" registry `[9052 §3, §11.1]`;
- the **value space** — that ECDSA-with-SHA-256-on-P-256 is named `-7` — which
  is the "COSE Algorithms" registry `[9052 §3.1]`.

**Does RFC 9052 actually mandate it?** Not absolutely. `[9052 Appendix A]`
records that "the requirement that the algorithm identifier be located in the
protected attributes was relaxed from a must to a should", and lays out how an
application may make the algorithm **implicit**, distributed with the key and
context. But the terms are severe: the application must "require that the
receipt of an explicit algorithm identifier in one of these structures will lead
to the message being rejected", "even if the transported algorithm is the same
as the implicit algorithm"; must define the context set (at minimum key
identifier, key, algorithm, and the COSE structure); and "should define an
application-specific external data structure that includes this value" so the
algorithm is still authenticated. Two consequences for us `[inference]`: the
implicit route **destroys the point of exporting** — a COSE consumer that does
not hold our context cannot process the message, so we would have built a COSE
message only our own code can read — and it forces us into an `external_aad`
construction, which §4.3 shows is the easiest thing in COSE to get wrong. The
implicit route is therefore rejected for the export, and `alg` goes explicitly
into the protected bucket.

**How that squares with `R-M-12`.** It squares, but only if we are precise about
what `R-M-12` covers. Its text enumerates "type identifiers, predicate types,
tags, and header parameters" `[ARCH-0001-PROPOSAL-v0.2.0 §7]`, and it permits
registry identifiers "at interchange boundaries", documented as lossy per
`R-I-01`; `ADR-0001`'s consequences say the same in the other direction ("CBOR
tags and COSE header parameters are IANA allocated, so they are interchange, not
native"). **The label `1` is a header parameter and is squarely within `R-M-12`;
it is permitted here only because the export is not native.** So "export only"
does mean registry dependence is acceptable at the boundary — that is the
explicit text of the requirement, not a reading of it.

**The harder half, which nobody has decided.** The *value* space is a different
question, because the native model needs an algorithm identifier too:
`ARCH-0001` §4.1 defines `Key` as "Public key material + algorithm identifier".
If an algorithm identifier is an `R-M-12` extension point, then natively it must
be `(defining key, label)`, and key *K* and key *K′* would have distinguishable,
non-coordinated names for Ed25519 — which is not a vocabulary disagreement they
are entitled to have, because there is exactly one correct answer about what
Ed25519 is. `DEC-008`'s own boundary already draws this line: "Signature
verification, canonicalization, the reduction algorithm, and the definition of
what 'valid' means must stay fixed", because "if a key may define how its own
statements are validated, it may define them as always-valid"
`[ARCH-0002 DEC-008]`. **An algorithm identifier belongs to that fixed core, not
to the key-relative extension surface** — and note that `R-M-12`'s enumeration
does not list it `[inference]`. That reading makes the `alg` export a *mapping
between two fixed-core namings*, not a concession on key-relativity, and it is
the answer this file recommends. It is analysis, it is not decided, and it
belongs in the DEC-002 ADR or in `ADR-0002`. Open question 2.

**What it costs, itemized.**

1. **Coverage lag.** A native algorithm with no COSE Algorithms registration has
   no export. `[9052 §11.6]` discourages vanity registrations and suggests CFRG
   review, so the lag is real. This bites hardest exactly where the project has
   an interest — post-quantum schemes — and a key-relative native naming could
   name a scheme before IANA does. Trade-off, not a blocker.
2. **A mapping that can be wrong, expensively.** `alg` sits inside
   `body_protected`, which is `Sig_structure` field 2 `[9052 §4.4]`, so it is
   inside `ToBeSigned`. A mistaken mapping is not a cosmetic bug: it changes the
   signature. This is why §5 D9 pins the table by value.
3. **Two names for one thing.** Every algorithm now has a native name and a
   registered name, and a verifier has to check they agree — exactly the "bug
   that will arise if full checking is not done correctly between the different
   places that an algorithm identifier could be placed" that `[9052 Appendix A]`
   warns about, and the risk `[9052 §12]` restates ("strictly enforce the
   matching of algorithms in the key structure to algorithms in the message
   structure").
4. **A rhetorical cost.** Any reviewer may ask why we accept a registry for
   algorithms and refuse one for types. The answer above — one correct answer
   per primitive versus many legitimate vocabularies — has to be *written down*
   in the ADR, or `R-M-12` looks negotiable.

### 3. Where a COSE export actually depends on the CBOR Tags registry

**The exposure is the message-type tags, not tag 24.** A word on that first,
because the distinction is the whole point of this section. It is tempting to
think the protected header is tag-encumbered, since it carries an encoded CBOR
map inside a byte string and RFC 8949 defines tag number 24 for exactly that
pattern `[8949 §3.4.5.1]`. It is not. **"Tag 24" appears zero times in
RFC 9052** (verified by search over the cached source), and RFC 9052 §3 spells out what
the bucket actually is: the value "is obtained by CBOR encoding the protected map
and wrapping it in a bstr object", with the CDDL
`empty_or_serialized_map = bstr .cbor header_map / bstr .size 0` `[9052 §3]` —
a **bare byte string**, where `.cbor` is a CDDL control operator describing
containment `[9052 §1.4]`, not a tag. COSE uses the *pattern* without the *tag*,
and `[9052 §3]` gives its reason on its own terms: the wrapper means the map travels
unaltered and no party has to agree on a canonical map encoding for input to the
cryptographic operation. **So the protected header costs us no tag at all**, and
anyone reasoning from "protected header ⇒ tag 24" is reasoning from a premise the
source does not contain.

The real exposure is narrower and genuine.

#### 3.1 Message-type tags

`[9052 §2, Table 1]` assigns a CBOR tag to each message structure:

| tag | `cose-type` | structure |
|---|---|---|
| 98 | `cose-sign` | `COSE_Sign` |
| **18** | **`cose-sign1`** | **`COSE_Sign1`** |
| 96 | `cose-encrypt` | `COSE_Encrypt` |
| 16 | `cose-encrypt0` | `COSE_Encrypt0` |
| 97 | `cose-mac` | `COSE_Mac` |
| 17 | `cose-mac0` | `COSE_Mac0` |

These are tags from the IANA "CBOR Tags" registry `[9052 §11.5]`, so **a tagged
COSE export does depend on that registry** — `COSE_Sign1_Tagged = #6.18(COSE_Sign1)`
`[9052 §4.2]`. That is the whole of the dependence, and RFC 9338 adds one more of
the same kind: tag **19** for a standalone `COSE_Countersignature` `[9338 §5.1]`,
which §6 below declines to use.

**And it is optional.** `[9052 §4.2]`: "The structure can be encoded as either
tagged or untagged depending on the context it will be used in." `[9052 §2]`
gives four ways to identify which message you are holding, and only one of them
is a CBOR tag:

| method `[9052 §2]` | registry consumed | available to us? |
|---|---|---|
| 1 — known from context: "a marker in the containing structure or by restrictions specified by the application protocol" | **none** | Yes, and only inside a container we define. |
| 2 — CBOR tag `#6.18` | IANA CBOR Tags | Yes, at the cost D-3 names. |
| 3 — media type `application/cose` with `cose-type="cose-sign1"` | IANA Media Types, plus the `cose-type` values fixed in Table 1 | Yes — and §2 makes the parameter **REQUIRED** when the untagged form is used, and OPTIONAL when the tagged form is. |
| 4 — CoAP Content-Format `18` `[9052 Table 2]` | IANA CoAP Content-Formats | Not relevant to us, but a fourth registry rather than an escape. |

So an **untagged export is available**, and the honest framing is: you can avoid
the CBOR Tags registry, but not every registry — methods 3 and 4 substitute a
different one, and method 1 works only inside bytes we wrap ourselves. "No tags"
and "no registry dependence" are different rules, and D-3 states the first.

**Choosing among the four is a DEC-005 decision, and this file does not make
it.** DEC-005 (the envelope for `ArtifactStatement`) is listed open in
`ARCH-0001` §7; D-3 constrains it to COSE-as-export and says nothing about
tagging. §3.4 B2 proposes a default for the D5 fixture package because a fixture
needs one, and that proposal is Open question 4 — not a decision.

#### 3.2 CWT tag 61, if we touch CWT at all

`R-I-03` contemplates "COSE_Sign1 + CWT claims" and `ARCH-0001` §6 carries it as
an interchange row, so this is live. `[8392 §6]` defines tag **61** for a CWT and
attaches a condition that matters here: "If present, the CWT tag MUST prefix a
tagged object using one of the COSE CBOR tags", illustrated as `61(17(...))`.
**So the two tags come as a pair**: a CWT-tagged export is necessarily also a
COSE-tagged export, and "CWT tag but untagged COSE beneath it" is not a
permitted shape `[8392 §6]`. Opting into CWT tagging therefore forfeits the
untagged route of §3.1 in one step.

The same section gives the escapes, and they are the ones we already prefer:
"this information is known from the application context, such as from the
position of the CWT in a data structure", or the `application/cwt` content type.
Its use is "optional and is intended for use in cases in which this information
would not otherwise be known" `[8392 §6]` — which is precisely not our case if
the export sits in a container of ours. Note separately that the CWT *claim keys*
are their own registry, so CWT interchange carries a second, larger registry
dependence than the tag; that is a DEC-003 and DEC-005 matter and is outside this
record.

#### 3.3 "No tags" has to be a positive decoder rule, not an omission

This is the sharpest practical consequence in this section, and it is the one
easiest to get wrong by writing nothing.

`[8949 §4.2.2]` is explicit that tag presence may not be left to convention: if
a protocol "were to provide the same semantics for the presence and absence of a
specific tag", then "the deterministic format would not allow the presence of the
tag, based on the 'shortest form' principle", and "This protocol's deterministic
encoding needs either to require that the tag is present or to require that it is
absent, **not allow either one**." COSE is exactly such a protocol: `[9052 §4.2]` gives
the encoder a free choice between `#6.18(COSE_Sign1)` and a bare `COSE_Sign1`
with identical semantics.

Therefore option 5 cannot discharge "no IANA tags" by simply not emitting any.
It has to state the prohibition as a **decoder** rule:

> **Major type 6 MUST NOT appear anywhere in a native canonical encoding.** A
> native decoder that encounters a tagged data item rejects the input; it does
> not strip the tag, and it does not treat `#6.n(X)` as equivalent to `X`.

Three reasons this is not pedantry.

First, **an imported tagged COSE object otherwise satisfies our decoder
silently.** `[8949 §7.1]`: "Implementations receiving an unknown tag number can
choose to process just the enclosed tag content or, preferably, to process the tag
as an unknown tag number wrapping the tag content." The first of those options is
exactly a silent strip, and `ARCH-0002`'s own CBOR note explains why it is so
cheap: the initial byte separates extent from meaning, so walking past an unknown
item costs nothing. Without a stated rule, both the tagged and the untagged form
parse, and the native model has quietly readmitted the registry it excluded
`[inference]`.

Second, **we are choosing the behaviour RFC 8949 discourages, and should say so
rather than discover it in review.** `[8949 §5.4]` offers a validity-checking
decoder two responses to an unrecognized tag number, and of the error response
says: "Note that treating this case as an error can cause ossification and is
thus not encouraged." Its preferred response is forward compatibility with newly
registered tags. That preference is coherent for a general-purpose CBOR decoder
and is the opposite of what a key-relative model wants, because forward
compatibility *with a registry* is the dependence `R-M-12` rejects. So N1 below is
a deliberate departure from RFC 8949's guidance, taken with its reason: we are not
a generic decoder, and our input is a signed statement, not an evolving document
`[inference]`.

Third, **`ARCH-0002 P5` makes it a validity-level obligation, not a style
preference.** A rule that is not stated is not checked, and P5's one-line form —
"A verifier **may traverse** what it cannot interpret. A verifier **must never
accept** what it cannot interpret" — is enforceable against tags only if "no
tags" is written as something a decoder can fail on. P5 also already argues for
inverting exactly this default so that forgetting is safe.

The same rule is what makes the domain-of-discourse hash safe `[ARCH-0002 P4,
held per D-2]`: two serializations differing only by a tag prefix hash
differently, so admitting an optional tag anywhere in hashed bytes would mean one
vocabulary with two identities.

#### 3.4 The boundary rule, stated

`[inference]` — the clauses are ours; the facts each rests on are cited inline.

- **N1.** **Major type 6 MUST NOT appear in a native canonical encoding**, stated
  as a decoder rejection rule per §3.3 and not as an omission. This binds hardest
  on any bytes whose hash is an identifier `[ARCH-0002 P4]`, because a tag number
  inside hashed bytes puts a registry *inside an identifier* — the failure
  `R-M-12` exists to prevent.
- **N2.** No COSE header label, and no value from a COSE value registry, appears
  in the native model — not as a field, not as an alias, not as a "convenience"
  mirror. A mirror is how registry dependence re-enters.
- **B1.** An export MAY be tagged `#6.18`. When it is, the tag belongs to the
  export artifact and never re-enters the native form: an importer strips it, and
  hashes or stores only what is underneath.
- **B2.** An export MUST identify itself by exactly one of §3.1's four methods,
  and the fixture package MUST record which. **Proposed** default for D5:
  untagged inside our own container (method 1), plus a tagged variant (method 2)
  so both paths are exercised. Subject to DEC-005; Open question 4.
- **B3.** A testable consequence, and the reason B1 is cheap: the tag is
  **outside** `Sig_structure` `[9052 §4.4]`, so tagging changes no signed byte. A
  tagged and an untagged export of one statement share `ToBeSigned` and share the
  signature, and differ by exactly the one-byte prefix `0xd2` (major type 6,
  argument 18, directly encodable because 18 ≤ 23). `[9052 C.2.1]` gives the
  tagged form at 98 bytes. **Assert this in the fixture**: it is the cheapest
  available proof that our tag rule is a boundary rule and not a semantic one,
  and it is also the check that would catch an encoder that folded the tag into
  the signature by mistake.
- **B4.** The protected-header `bstr` bytes are copied verbatim into
  `Sig_structure` field 2 `[9052 §4.4]`, and §3 warns that decode-and-re-encode
  breaks verification. So our importer keeps the bytes it received, and our
  exporter treats its protected-header encoding as a pinned output artifact
  rather than something re-derived at verification time. This is `R-O-05`
  restated in COSE's own terms.

### 4. What the export deliberately does not carry

| stays native | why |
|---|---|
| the tag / authorization value and its intersection semantics `[DEC-004, P7]` | COSE has no authorization layer and says so `[9052 §4.4, §12]`. Exporting an opaque blob under a registered label would misrepresent it as something a COSE consumer can evaluate. |
| delegation, and its `(Domain, Topic)` scope `[P2]` | Same. Delegation is the reduction's input, and the reduction is ours. |
| the resolution of the domain-of-discourse hash `[P4]` | The hash can travel as payload bytes. Its *contents* cannot: P4's point is that the set is identified by hash, and a copy in an envelope is a second source of meaning that the hash no longer covers. The export cites; it never copies. |
| P3's semantic descriptions, human-review tags and multilingual short descriptions | They belong to the type, not to the statement. Copying them into the envelope would put the words a person reads outside the hash that authenticates them. |
| threshold speakers `[R-M-06]` | No `COSE_Sign1` form exists; `COSE_Sign` is a different, non-interconvertible structure `[9052 §4, §4.1]`. |
| `online_check` in `Validity` | No analogue anywhere in COSE. |
| must-understand-by-default `[P5]` | `crit` reaches header labels only `[9052 §3.1]`. **The export cannot make a COSE consumer reject an unknown payload field.** |
| `AclEntry` `[ARCH-0001 §4.2, ARCH-0002 P6]` | Unsigned local policy with no speaker. There is nothing to sign, so there is nothing to export. |
| reduction results / verifier verdicts `[R-O-06]` | An export is a statement, not a verdict. `R-O-06`'s three-part result is a local output. |

**The consequence that has to be written on the fixture package.** Because the
tag, the delegation scope and P5's discipline all stay behind, **a COSE-only
verifier that accepts our export has verified a signature and nothing else.** It
has not performed statement acceptance `[ARCH-0001 §4.3]`, which requires
"signature valid ∧ issuer authorized for that `PredicateType` ∧ subject digest
matches", and it cannot produce `R-O-06`'s separated result. The export is an
interoperability artifact, not a security-equivalent form, and the D5 README
should say so in those words `[inference]`.

### 5. Determinism at the boundary — what the mapping must pin

`PLAN-0003` protects Oct 28 (D5: option-5 fixtures plus the option-2
comparison). A fixture is worthless if two correct implementations disagree on
its bytes. RFC 9052 pins less than one might assume: **§9's restrictions apply
to "the encoding of the `Sig_structure`, the `Enc_structure`, and the
`MAC_structure`"** — not to the message, and **not to the contents of the
protected-header `bstr`**, which §3 deliberately leaves to the sender. So the
following are ours to fix.

| # | pinned | basis |
|---|---|---|
| **D1** | Native canonical encoding: RFC 8949 §4.2.1 Core Deterministic Encoding, narrowed per `[9052 §9]` — definite lengths, minimum-length arguments, no duplicate map labels. Cited, not invented (`R-O-03`). | `[9052 §9]` |
| **D2** | **Protected-header map ordering.** The RFC does not pin it, and §3 says why. We encode the protected map under RFC 8949 §4.2.1 including its deterministic map-key ordering (bytewise lexicographic over encoded keys), definite length, smallest-argument integer labels. Without this clause the export is not reproducible. | `[9052 §3, §9]` + `[inference]` that the gap must be closed by us |
| **D3** | The exact label **set** in the protected bucket: `1` (`alg`) and `3` (`content type`), plus `2` (`crit`) only when non-empty — and nothing else. The map's length and ordering then depend on the statement, not on the encoder. | `[9052 §3.1]` |
| **D4** | Unprotected bucket: `kid` only, or empty; encoded as a definite-length map (`0xa0` when empty). Both buckets must be present `[9052 §3]`. Anything unsigned we ever add must be listed here, because it changes message bytes without changing the signature. | `[9052 §3]` |
| **D5** | **The empty-protected-header case.** If the protected map is empty, emit a **zero-length byte string**, not `h'a0'`: senders SHOULD, "because it is both shorter and the version used in the serialization structures for cryptographic computation", and recipients MUST accept both `[9052 §3]`. `Sig_structure` field 2 is then the zero-length byte string `[9052 §4.4 item 2]`. In our profile the case is unreachable — `alg` and `content type` are always present — so the fixture **asserts** that it does not arise and the importer still accepts both forms. Unreachable-by-construction is a statement to make, not a case to leave undefined. | `[9052 §3, §4.4]` |
| **D6** | **`Sig_structure` shape for `COSE_Sign1`: exactly four elements** — `"Signature1"` (text string), `body_protected` (`bstr`), `external_aad` (`bstr`), `payload` (`bstr`). `sign_protected` **is omitted**, not zero-length `[9052 §4.4 item 3]`. A five-element array with an empty `sign_protected` is a different byte string and a different signature; the fixture asserts the element count. | `[9052 §4.4]` |
| **D7** | `external_aad` = the zero-length byte string `[9052 §4.4 item 4]`. If it is ever used, §4.3 obliges us to define the construction with length-prefixed fields and a fixed order, and §10 obliges us to publish it. Until then: empty, asserted. | `[9052 §4.3, §4.4, §10]` |
| **D8** | Payload: the full native canonical bytes, in `Sig_structure` field 5, "independent of how it is transported" `[9052 §4.4 item 5]`. Detachment excluded (see reject 5). | `[9052 §4.4]` |
| **D9** | The `alg` mapping table, pinned **by value** with its RFC 9053 name (the source's own example is `-7`, "ECDSA 256" `[9052 C.2.1]`). Because `alg` is inside `body_protected` and so inside `ToBeSigned`, a mapping change is a signature change. | `[9052 §3.1, §4.4, C.2.1]` |
| **D10** | The tagging choice per fixture, plus the B3 assertion: tagged and untagged variants share `ToBeSigned` and the signature and differ by the single `0xd2` prefix. | `[9052 §2, §4.2, §4.4]` + `[inference]` |
| **D11** | **Signature determinism.** ECDSA with a random per-signature nonce yields different signature bytes on every run, so with ES256 the reproducible artifact is `ToBeSigned` (and its digest), **not** the whole message. For byte-exact whole-message fixtures, use a deterministic scheme — Ed25519 (RFC 8032, which `[9052 §4.1]` names) or deterministic ECDSA. Recommendation: the primary D5 fixture is Ed25519 for byte-exactness, with an ES256 fixture that pins `ToBeSigned` and verifies rather than reproduces. **RFC 9052 does not discuss nonce determinism; this is `[inference]`, and it is the item most likely to waste a student's afternoon if it is not written down.** | `[inference]`, `[9052 §4.1]` |
| **D12** | The fixture file set per statement: the YAML human form (D-3); the native canonical CBOR in hex; the native statement digest; the `body_protected` bytes; the `Sig_structure` / `ToBeSigned` bytes; the full `COSE_Sign1` in both tagged and untagged form; and the expected verification outcome. `[9052 C.2.1]` is the reference shape to imitate — `18([ h'a10126', {4:'11'}, payload, signature ])` — and `distilled/examples/` should hold it as the first fixture so our encoder is checked against the RFC before it is checked against itself. | `[9052 C.2.1]`, `docs/extraction.md` |

### 6. Counter-signatures and `Endorse`

**Where the primitive lives.** Not in this record. `[9052 §1]` records that the
countersignature text was removed because "the description of the security
properties of countersignatures was incorrect for the `COSE_Sign1` structure",
and `[9052 §11.1]` leaves "counter signature" and `CounterSignature0` pointing
at RFC 8152. The current primitive is RFC 9338, which updates RFC 9052 and forms
STD 96 with it: `Countersignature version 2` at label **11** and
`Countersignature0 version 2` at label **12**, both **unprotected** attributes
`[9338 §2]`; a `Countersign_structure` whose `other_fields` for a `COSE_Sign1`
target is "an array of one element ... containing the signature value"
`[9338 §3.3]`; tag **19** for a standalone `COSE_Countersignature`
`[9338 §5.1]`; and `[9338 §4]` requiring RFC 9052 §9's narrowed deterministic
rules for `ToBeSigned`.

**Is it the right primitive for `Endorse`? No.** Four reasons, the first two
decisive `[inference; the facts are cited]`:

1. **Subject mismatch.** A countersignature's subject is *the existence of a
   signature*: `[9338 §3]` says it "makes a statement about the existence of a
   signature and, when used with a yet-to-be-specified timestamp, a point in
   time at which the signature exists." `Endorse` is about a **principal** —
   "issuer treats subject as introducer at weight *w*" `[ARCH-0001 §4.2]` — and
   has to mean something with no message in hand at all.
2. **It re-creates the taxonomy P6 dissolves.** `[ARCH-0002 P6]` makes `Endorse`
   one *function* over the single `A says B has C` form, discriminated by a
   key-relative predicate type. Giving it a distinct envelope primitive would
   put back the five object kinds P6 argues are one form, and would mean a
   verifier that can read an attestation cannot read an endorsement.
3. **Nowhere to put the weight or the scope.** `COSE_Countersignature0` carries
   "only ... the signature value and nothing else" `[9338 §3]`. The full form
   has its own header buckets, but those are COSE labels, which `R-M-12` bars
   natively — and label 11 itself sits in the *unprotected* bucket `[9338 §2]`,
   so anything we put beside it is unsigned by the primary signer.
4. **Lifetime.** A countersignature is bound to the message it decorates. An
   endorsement must be independently storable, citable, revocable and reducible.

**What it *is* right for.** A **witness or receipt over one exported statement**
— "this exact `COSE_Sign1` existed and passed through me" — because
`other_fields` binds the target's signature bytes `[9338 §3.3]`. That is the
shape of a transparency receipt, which `ARCH-0001` §6 already lists as "evidence
attached to an `ArtifactStatement`" that "does not change meaning of statement",
and `R-O-04` holds at Could priority. Note `[9338 §3]`'s caution that **no COSE
timestamp is defined yet**, so the "when" is not carried by the primitive. For
DEC-009's contract form the full countersignature is *structurally* capable of
carrying a second speaker's protected claim, but its defined meaning is
existence, not agreement, and a *k*-of-*n* multi-speaker statement is better
served by `COSE_Sign`'s *n* `COSE_Signature` entries `[9052 §4.1]`; DEC-009 is
open and this file does not answer it.

**Recommendation:** countersignatures are out of the D5 export mapping. Revisit
when there is a receipt or transparency increment. A COSE library we depend on
must still be able to *verify* label 7 for backward compatibility `[9052 §3.1]`
— that is a library-selection note, not a model change.

---

## Open questions

Each names who decides and what it blocks. Ordered by what blocks Oct 28 first.

1. **Does the export re-sign with the speaking key, or wrap with the exporter's
   key?** (§1a.) **Paul** — this is a model question, not an encoding one,
   because under P2 a signature is a saying. **Blocks D5**: the fixture shape
   differs in both cases.
2. **Is an algorithm identifier an `R-M-12` extension point, or a `DEC-008`
   fixed-core item?** (§2.) **Paul**, in the DEC-002 ADR or `ADR-0002`. Blocks
   nothing mechanically, but leaving it open means the ADR has to defend
   registry dependence without the argument that makes it principled.
3. **Do we register a media type for the native form, and in which tree?** (§1
   row 4.) **Paul.** Until this is answered `content type` cannot be emitted,
   and the protected-header label set (D3) is unsettled — so it touches D5.
4. **Which of `[9052 §2]`'s four identification methods is the default for an
   export?** (§3.1, §3.4 B2.) **This is a DEC-005 call and this file does not
   make it** — §3.4 B2 proposes method 1 plus a tagged variant only because the
   D5 fixtures need a default to be written against. **Paul**, with David.
   *Recorded with it, because it was a live misreading in the brief that framed
   this work:* the tag exposure in a COSE export is the **message-type tags** of
   `[9052 §2]` Table 1 — 18 for `COSE_Sign1`, plus 19 for a standalone
   countersignature `[9338 §5.1]` — **and not tag 24**, which appears nowhere in
   RFC 9052; the protected header is a bare `bstr` `[9052 §3]`. The distinction
   is the whole of the question: tag 24 would have been unavoidable, and the
   message-type tag is optional `[9052 §4.2]`. Anyone re-opening this should read
   §3 before re-deriving it.
5. **Is DEC-005 closed by D-3, or does "COSE as export only" still leave DSSE?**
   `R-I-03` asks for "at least one envelope in v1"; `ARCH-0001` §7 lists DEC-005
   open; D-3 speaks about COSE and is silent on DSSE. **Paul.** Affects whether
   this mapping is *the* export mapping or one of two.
6. **Does the D5 option-2 comparison fixture need its own COSE mapping?** Our
   reading is no — D-3's comparison is about the *native* encoding, and the
   export mapping is the same either way — but that reading is not written
   anywhere. **David**, confirmed by Paul, before he builds two mappings.
7. **Threshold export.** Accept "no export for a *k*-of-*n* speaker" as a
   documented interchange gap, or extend the target to `COSE_Sign`? **Paul.**
8. **Ed25519 or ES256 as the primary D5 fixture algorithm?** (D11.) **David**,
   with Paul on the crypto-suite implication. Byte-exact fixtures need a
   deterministic scheme.
9. **Does the domain-of-discourse hash appear in an export at all?** P4 is held
   per D-2, so the honest answer today is "not until P4 is accepted", which
   means the export mapping will change when it is. **Paul.**
10. **Where does this mapping become normative** — inside the DEC-002 ADR, or in
    a separate interchange-mapping document in the `WP2`–`WP5` series
    `[ARCH-0001 §8]`? **Paul.** `R-D-02` requires an accepted decision to become
    an ADR; an export mapping is bigger than an ADR body.
11. **`ARCH-0001` §3.2 cites "CWT claims ... in COSE protected header 15".**
    That header parameter is not defined in RFC 9052. **Whoever owns
    `ARCH-0001`** should re-cite it to the document that does define it, or drop
    the label number. Editorial, but it is a citation error in a table that
    drives DEC-003 and DEC-005.

### Defects in the source, recorded and not repaired

Three findings of the cross-check pass that belong to RFC 9052, not to this
extraction. None is a decision anyone takes; each is something a reader of the
source will trip over, so it is written down rather than smoothed away.

**S1. RFC 9052 specifies checks, not consequences — and a verifier cannot be
built from it alone.** Of the 81 procedure steps in `protocol.yaml`, **51 have no
stated consequence for failing**, and the adjudication that produced that number
was done requirement by requirement, not by eye: every step marked `unspecified
in this document` was checked against all 99 entries in `requirements.yaml`, and
only two turned out to have one (both the decryption call, both now citing §8.3 /
`rfc-9052#R-0066`). The document has exactly **five** mandatory error behaviours
(§3/§9 duplicate label, §3.1 `crit` not in the protected bucket, §8.5.2
unsupported recipient algorithm, §1.5 non-`int`/non-`tstr` label, §8.3 content
decryption that does not validate). It never says what a verifier does when a
**signature** fails to verify, nor what a recipient does when a **MAC** comparison
fails, nor what happens when either of §5.4's two `protected`/external-AAD
assertions fails. §8.1 and §8.2 give `valid = Verification(...)` and
`valid = MAC_Verify(...)`, but that is the algorithm taxonomy; the `valid` result
is never threaded back into the §4.4 or §6.3 step lists.

The consequence for us is concrete and belongs on the D5 package: **the failure
semantics of a verifier are not inherited from COSE.** RFC 9052 §10 makes that
the profiling application's job, and our export mapping is that profile
(adopt 6). So `R-O-06`'s three-part result, and the rule that a failed check
aborts rather than degrades (`ARCH-0002 P5`), are **ours to state** — we cannot
cite RFC 9052 for them the way we cite it for canonicalization (adopt 4) or for
reject-never-repair at the three places where it does speak (adopt 5). Adopt 5
is still sound; it is just narrower than it looks, and the fixture package should
not imply that a COSE-conformant verifier has defined behaviour on a bad
signature.

**S2. The source names one recipient structure two ways.** §8.5.1–§8.5.5 call it
`COSE_Recipient`; the CDDL rule and the §5.1 prose call it `COSE_recipient`.
There is only one structure. Our artifacts are each faithful to where they quote
from — `requirements.yaml` keeps §8.5's capital R because its text fields are
verbatim, `messages.yaml` and both CDDL files use the rule name — so a query
that joins requirement objects to structure names on the string will silently
miss the 20 §8.5 requirements. The alias is recorded in `messages.yaml` under
`COSE_recipient` and in `schema/README.md`.

**S3. `content type` is `uint` in Table 3 and `int` in the CDDL.** §3.1's Table 3
gives label 3 the CBOR type `tstr / uint`; the CDDL fragment in the same section
writes `? 3 => tstr / int`. The CDDL therefore admits a negative content-type
value the table forbids, and §1.4 says the prose is normative, so the table wins.
This matters to us only slightly — open question 3 may have us emit `content
type` — but if we do, the value is a registered media type or CoAP
Content-Format and is non-negative either way, so **pin it as `uint`** and do not
rely on the CDDL. Recorded because a reviewer comparing our two schema files
against each other will find the difference and should know it is the source's.

### Reasoned beyond the sources — every inference in this file

| where | what was inferred | why it is not in a source |
|---|---|---|
| reject 1, §1 row 3 | That `(defining key, label)` is **structurally** inexpressible as a COSE header label. | RFC 9052 §1.5 states `label = int / tstr`; the conclusion about our pair is ours. |
| §1 row 1, row 2 | The "mirrors are non-authoritative and MUST match the payload" rule. | Our rule. RFC 9052 has a precedence rule between buckets (§3) but says nothing about a payload. |
| §1 row 7 | That COSE protected header label 15 ("CWT Claims") belongs to a document other than RFC 9052, and that `ARCH-0001` §3.2 mis-cites it. | RFC 9052 §3.1 Table 3 defines labels 1–6 only. The identity of the document that defines 15 is outside this record and was not read. |
| §1 row 6 | That RFC 9054 is where a COSE-native digest structure would be found. | RFC 9052 §1 says RFC 9054 "contains one such possible structure"; the name of that structure is not in this record. |
| §1 row 2 | That RFC 9052 provides no header parameter carrying raw public-key material. | Verified absent from §3.1 Table 3; certificate- and thumbprint-carrying headers exist in documents outside this record and were not read. |
| §1 `alg` row | That §3.1's "MUST be authenticated where the ability to do so exists" binds `COSE_Sign1`. | §3.1's example list names `COSE_Sign` and `COSE_Mac0`, not `COSE_Sign1`. The inference rests on §4.4 putting `body_protected` and `external_aad` inside `Sig_structure`. |
| §1 `crit` row | That `crit` will normally be **absent** in our profile. | Derived from §3.1's "integer labels in the range of 0 to 7 SHOULD be omitted" plus our D3 label set. |
| §1a (all) | That the native signature cannot port; the re-sign / wrap choice; and that the two cases are distinguishable from the verifying key with no new header parameter. | The byte-string difference follows from §4.4; the design choice and its consequences are ours. |
| §2 | That an algorithm identifier is a `DEC-008` fixed-core item rather than an `R-M-12` extension point. | `R-M-12`'s enumeration omits it and `DEC-008` names signature verification as fixed core, but no document draws the conclusion. **This is the one inference in this file that changes a principle, and it must not be quoted as decided.** |
| §2 | That the Appendix A implicit-algorithm route defeats the purpose of exporting. | Appendix A states the requirements; the judgement is ours. |
| §3 opening | That the protected header needs no tag, and that "protected header ⇒ tag 24" is a false premise. | Both halves are now sourced, not inferred: `[9052 §3, §1.4]` for the bare `bstr` and the `.cbor` control operator, `[8949 §3.4.5.1]` for what tag 24 actually is, and a search of the cached source for the zero occurrences. Recorded here only because the claim was asserted to the extractor as fact and had to be checked rather than accepted. |
| §3.3 | That an unstated "no tags" rule is silently satisfied by an imported tagged object, and that the prohibition must therefore be a decoder rejection rule. | `[8949 §4.2.2]` requires a deterministic protocol to require the tag or forbid it, "not allow either one"; `[9052 §4.2]` gives exactly that free choice; `[8949 §7.1]` permits processing "just the enclosed tag content". The consequence for our decoder, and the links to `ARCH-0002` P5 and P4, are ours. |
| §3.3 | That N1 is a deliberate departure from RFC 8949's own guidance rather than an application of it. | `[8949 §5.4]` says treating an unrecognized tag as an error "can cause ossification and is thus not encouraged" and prefers forward compatibility. The judgement that its preference is the wrong trade for a key-relative model is ours, and a reviewer may reasonably push back on it. |
| §3 B1–B4 | The four-clause boundary rule. | Ours. The facts each clause rests on are cited inline. |
| §3.4 B3 | That the tagged form's prefix is the single byte `0xd2`, and that tagged and untagged exports share a signature. | The shared signature follows from `[9052 §4.4]` (the tag is outside `Sig_structure`). `0xd2` is CBOR encoding arithmetic (major type 6, argument 18, directly encodable because 18 ≤ 23), not a byte printed in RFC 9052. |
| §3.2 | That opting into CWT tag 61 forfeits the untagged COSE route in one step. | `[8392 §6]` states the condition ("the CWT tag MUST prefix a tagged object using one of the COSE CBOR tags"); reading it as a forfeiture of §3.1 method 1 is ours. |
| §4, closing paragraph | That the export is not a security-equivalent form. | Follows from §4.4 and §12 leaving authorization to the application, plus `ARCH-0001` §4.3; stated by neither. |
| §5 D2 | That we must pin protected-header map ordering ourselves. | §9 scopes its restrictions to `Sig_structure` / `Enc_structure` / `MAC_structure`, and §3 says the `bstr` wrapper exists to avoid a common canonical map encoding. The obligation on us is the inference. |
| §5 D6 | That a five-element `Sig_structure` with an empty `sign_protected` is a live implementation trap. | §4.4 says the field "is omitted for the `COSE_Sign1` signature structure"; that this is a trap worth asserting against is experience, not text. |
| §5 D11 | That ECDSA signatures are non-reproducible run-to-run and that Ed25519 or deterministic ECDSA is needed for byte-exact fixtures. | RFC 9052 does not discuss signature nonce determinism at all. External cryptographic knowledge. |
| §6 | That the COSE countersignature is wrong for `Endorse` and right for a receipt. | The primitive's properties are `[9338 §2, §3, §3.3, §5.1]`; the fit judgement against `Endorse` and `DEC-009` is ours. |

---
record: rfc-8778
kind: design-notes
title: "rfc-8778 — bearing on our design"
extracted: "2026-10-20"
reviewed_by: ""
---

# RFC 8778 — bearing on our design

Voice markers, as `rfc-8949` and `rfc-9964` use them: **unmarked** is the source
or our own decisions as cited; **[analysis]** is this extraction's reasoning;
**[correction]** is a project or sibling-record assumption the sources do not
support; **[inference]** is a judgement of ours that the source does not state
and for which **no `R-*` id is asserted**.

**Which quotations here are checkable from this repository, and which are not.**
This library is **standalone by design** — independently cloneable, forkable and
citable by projects that are not `mofn` (`CLAUDE.md`). The `mofn` documents this
record quotes are **not present in this repository**: `ARCH-0001`,
`ARCH-0001-PROPOSAL-v0.2.0`, `ARCH-0002` (P1, P4, P5), `ADR-0001`,
`DECISIONS-0001`, `MD-3`, and the `DEC-00n` / `R-M-*` / `R-O-*` / `R-I-*` rules.
**Every quotation of those documents — here, in `summary.md`, in
`distilled/README.md` and in `record.yaml`'s `bears_on` commentary — is
reproduced from the extracting agent's context and cannot be verified from this
repository.** Treat each as a citation to re-check against `mofn` before relying
on it; that includes the six identifiers `bears_on` names (`DEC-002`, `DEC-003`,
`DEC-005`, `R-M-02`, `R-O-01`, `ARCH-0002 P1`) and the four more this file
reaches (`R-M-12`, `R-O-03`, `R-O-05`, `R-O-01`). `rfc-9741` adopted this
convention on 2026-10-20 and `rfc-9964` followed it; this record follows both.

What **is** checkable here, and the method each check used — *(rewritten
2026-10-21, FX-1 pass 3. This paragraph read "every quotation of RFC 8778 (194
across this directory, 41 of them in this file) … (25 across this directory)".
Pass 2 found the breakdown those figures belong to sums to 233 rather than its
stated 225 and left them standing with the flaw declared. **No stated method
reproduces 194, 41 or 25, and none can**: a delimited-span count over this
directory is dominated by YAML scalar values that are not quotations at all — a
`name:`, an `encoding:`, a `locator:` — so the denominator is an artifact of the
extractor, not a property of the record. The figures are deleted rather than
re-estimated, and what replaces them is three checks that recompute.)*

1. **Every requirement text, against `.cache/rfc-8778.txt`, digest
   `2d43646b974c…`.** Whitespace-normalise both sides, then substring-test and
   count occurrences: **135 of 135 are contiguous spans of the normalised
   source and each occurs in it exactly once**, so no entry's text can be
   satisfied by a different sentence.
2. **Every markdown blockquote in this directory, against the same source.**
   Take each contiguous `>`-prefixed run as one span, strip the marker and any
   trailing `— R-NNNN` attribution: **11 of 11 resolve verbatim.**
3. **Every quotation attributed to another document, against that document
   only, with this record's own files excluded from the corpus** — the rule
   `.claude/skills/extract/hazards.md` records *because of this record*, whose
   `summary.md` once resolved a wrong `rfc-9964` quotation against
   `record.yaml`'s copy of the same wrong quotation. Corpora: the cached
   sources, the quoted records' own files, `topics/canonical-encoding.yaml`,
   `docs/extraction.md` and the extract skill. Every span resolves in the
   document it names. **No total is recorded, deliberately**: this paragraph
   quotes the quotations it counts, so any edit moves the figure — the same
   reason `README.md` gives for not totalling the bare `R-`/`V-`/`S-`
   references.

**And inline markup inside a quotation is reproduced, never added** — the
convention this pass settled, because the audit above turned on it. `MD-3`'s own
emphasis is carried (`COSE_Sign1 and DSSE remain **export** envelopes`, and the
bold on its no-registry clause), exactly as `rfc-9964` and
`records/community/draft-mcnally-deterministic-cbor` carry it. Two spans here
had markup this record added: `carried as **ordinary map entries**` in §8 and
`` Envelope for `ArtifactStatement` `` in §7, both plain in every other copy in
the library. Both are now plain. A reader cannot tell an added emphasis from the
quoted document's own, which is why the rule has to be *reproduce or nothing*.

Also checkable, and checked: the `canonical-encoding` conditions (1)–(6), which
are stated **in this repository** in `topics/canonical-encoding.yaml` and are
therefore the one group of our own rules this record can cite rather than
reconstruct; and the existence and state of every record named below.

**Nothing in this record's findings rests on an unverifiable quotation.** Every
finding is measured against `.cache/rfc-8778.txt`; the `mofn` ids say which of
our decisions a measured finding bears on.

---

## What we adopt

**§2.1 + §2.2 as the canonical key bytes for an HSS-LMS principal, because
nothing else specifies them.** Verbatim, `R-0024` and `R-0053`:

> The public key for the topmost LMS tree is the public key of the HSS system.

> The LMS public key can be summarized as:
>
>    u32str(lms_algorithm_type) || u32str(otstype) || I || T[1]

`DEC-003`'s one mandatory clause is "Must specify: canonical key bytes before
hashing" (`ARCH-0001` §7). **These two sentences are that specification for
HSS-LMS, and they are the only one anywhere.** RFC 9679 §4.5 requires `kty` and
`pub` for an HSS-LMS COSE Key Thumbprint and cites **neither RFC 8778 nor
RFC 8554** — 0 occurrences of each in RFC 9679. `records/ietf/rfc-9679` is at
`profile: full` with that dependency recorded. Adopting the citation is not a
choice; under `R-O-03` ("Canonicalization algorithm for each concrete encoding
SHALL be cited, not invented silently") there is nothing else to cite.

**The 56 octets, and every width's provenance, because one of them is not in any
document we hold.** `schema/README.md` has the table; the short form:

| field | octets | provenance |
|---|---|---|
| `u32str(lms_algorithm_type)` | 4 | **measured by this pass** — not stated in RFC 8778 |
| `u32str(otstype)` | 4 | **measured by this pass** |
| `I` | 16 | **stated** — §3 `R-0092`, "it is the 16-byte identifier of the LMS public key for the tree" |
| `T[1]` | 32 | **arithmetic** — §2.2 `R-0052` with `R-0039`, "supports only SHA-256 with m=32" |
| **total** | **56** | invariant over all 20 parameter-set combinations RFC 8778 admits |

**[analysis] The u32str width is the interesting one, because "it is called u32"
is not a citation and no document in this library states it.** RFC 8778 never
defines `u32str`: `R-0028` says only "where the notation comes from [HASHSIG]",
and `records/ietf/rfc-8554` is a **stub**. So the width was recovered from the
document's own arithmetic against its own bytes. §2.1 `R-0027`, §2.2 `R-0062`
and §2.3 `R-0079` make a stand-alone-tree signature `4u + n + n·p + m·h` octets
with four `u32str` fields, and `R-0039` and `R-0066` fix `m = n = 32`. Both
printed signatures measure **2512**, and `2512 − 4u − 32` is divisible by 32 for
`u = 4` and for no other `u` in {1, 2, 8}. **[correction] 2026-10-21, FX-1
pass 2.** This clause continued "so `u = 4` uniquely", which does not follow from
a four-candidate table: the congruence reduces to `u ≡ 4 (mod 8)` and `u = 12`,
`20`, `28` satisfy it. `u = 4` is pinned by a **second** leg the pass had
measured and not used — octets 0–3 of both signatures are `00000000`, §2.1
`R-0027`'s `u32str(0)`, and the two first differ at octet 7, the leaf number `q`.
With that, `p + h = 77` falls out, and `h = 10`, `p = 67` follow from where the
type code lands (`examples/vectors.yaml` `V-0003`, `schema/README.md`). **The one
width neither RFC 8778 nor this library states is pinned by a non-normative
appendix.**

**§3's five key checks, as the whole of the conformance surface for a key.**
`R-0086` is the only unconditional obligation about a key in the document and
`kty` occurs exactly once in it. The other four are conditional on presence.

**The three registrations:** `alg` **−46** with "Recommended: **Yes**" (§6.1,
`R-0120`–`R-0122`), `kty` **5** (§6.2, `R-0124`), `pub` at label **−1**, CBOR
type **bstr** (§6.3, `R-0127`). `pub` occurs exactly once in the document, in
that template, and it is the **only** key type parameter registered for `kty: 5`.

---

## What we adapt, and how

**The size trade becomes a budget, and it runs the opposite way to
`rfc-9964`'s.** `R-0007`, the document's own statement:

> The HSS/LMS signature algorithm uses small public keys, and it has low
> computational cost; however, the signatures are quite large.

Measured, both halves (`examples/vectors.yaml` `V-0011`):

| quantity | octets |
|---|---|
| public key (`pub`) | **56** |
| minimal `COSE_Key` `{1: 5, −1: pub}` | 62 |
| RFC 9679 §4.5 thumbprint input | 62 — **byte-identical to the minimal key** |
| `KeyId` (SHA-256) | 32 |
| **key − `KeyId`** | **+24** |
| signature | **2512** |
| payload in both examples | 20 |
| `COSE_Sign` total / `COSE_Sign1` total | 2560 / 2552 |

**The adaptation is that the per-principal cost stops mattering and the
per-object cost starts.** For ML-DSA (`records/ietf/rfc-9964`) a public key is
1312–2592 octets against 32 for its thumbprint, so a 3-of-5 threshold subject
carried as keys is 6560–12 960 octets and `DEC-003` is a size/identity trade.
Here a key is 56 octets. A 3-of-5 threshold subject carried as **minimal
`COSE_Key`s** is 310 octets; carried as `KeyId`s it is 160. **The whole saving is
150 octets, against a signature of 2512.** Our `AuthzCert` sizing question
therefore has a different answer for this suite than for ML-DSA, and the thing
to budget is the number of signed objects, not their principals.

**Condition (3)'s canonicalise-once-at-authoring rule stops being a discipline
and becomes an economic fact.** `R-O-05` (proposed, `ARCH-0001-PROPOSAL-v0.2.0`
§3.4) requires that "A verifier SHALL verify the signature before decoding and
SHALL NOT canonicalize input as part of verification", and
`topics/canonical-encoding.yaml` condition (3) is "Canonicalisation runs once,
at authoring, on trusted input, and never as part of verification."
**[analysis]** Under HSS/LMS, re-authoring a statement **costs a leaf**
irreversibly (`R-0101`). So the pressure that normally pushes an implementation
towards re-canonicalising — "just re-sign it" — is priced. The rule and the
algorithm point the same way for once, and that is worth having in the ADR as an
argument rather than as a coincidence.

**The leaf-usage state becomes a durability requirement on our signer, stated in
our own terms because the source states none.** `R-0097` requires the tracking
data be kept and `R-0099` names how it is lost — "failed writes, virtual machine
snapshotting or cloning, and other operational concerns" — **in lowercase
`must`**, the one sentence in that paragraph with no BCP 14 keyword. `R-0112`
defers the approach to `[HASHSIG]` §9.2 and specifies no ordering between
emitting a signature and committing the state change. `state-machine.yaml`
records that gap under `unspecified`; it is the single operational rule we would
have to write ourselves.

---

## What we reject, and why

**Nothing in this document is adopted as a suite choice, because `NG3` defers
which algorithm we pick.** That is unchanged and is not what this record is read
for.

**The private-key side, as a thing we could ever profile.** `R-0115`:

> A COSE Key Type Parameter for encoding the HSS/LMS private key and the state
> about which tree nodes have been used is deliberately not defined.

There is nothing to reject and nothing to adopt: **no standard private-key format
for HSS-LMS exists, on purpose.** Read `R-0116` for the reason — "to avoid
creating the ability to save the private key and state, generate one or more
signatures, and then restore the private key and state" — and `R-0117` for the
consequence, "disastrous opportunities for tree node reuse".

**[correction] §5 does not forbid software storage, and reading it that way is
the mistake to avoid.** It states no `MUST NOT` at all; the word `MUST` does not
occur in §5 and neither does any other BCP 14 keyword. **It withholds the
format.** That is *stronger* than a prohibition in one way and *weaker* in
another, and both matter to us. Stronger: a `MUST NOT` can be disobeyed
interoperably, and a missing format cannot — no two implementations can agree on
how to move this key, so there is no portable backup, no replication and no
migration. Weaker: nothing stops a single implementation defining its own
private format and doing exactly what §5 is trying to prevent. **The document
removes the interoperable route and nothing else.**
`state-machine.yaml` carries this under `forbidden_transitions`.

**§3's `kid`-as-`I` suggestion, as something to build on without a worked
instance.** `R-0090` permits it and `R-0092` gives the width; **both of the
document's own examples use `'ItsBig'`, six ASCII octets** (`V-0008`). And
nothing in RFC 8778 binds a `kid` to the key's actual `I`, so a mismatch is
unconstrained *and unobservable* — there is no check to write. Adopting the
suggestion means being the first, and owning the binding rule ourselves.

---

## Mapping to our decisions

### 1. What our post-quantum export must carry, if this suite is ever admitted

Every number is from §6 or measured. The interchange surface is remarkably
small.

**The key, as a `COSE_Key` (`messages.yaml` `S-0007`):**

| entry | label | encoded | value |
|---|---|---|---|
| `kty` | 1 | `01 05` | 5 (HSS-LMS) — `R-0086`, `R-0124` |
| `alg` | 3 | `03 382d` | −46 — **optional**, `R-0087`, `R-0120` |
| `kid` | 2 | `02 50 …` | MAY be the 16-octet `I` — `R-0090`, `R-0092` |
| `key_ops` | 4 | `04 81 01` | MUST include the op in use — `R-0088`, `R-0089` |
| `pub` | −1 | `20 5838 …` | the 56 octets — `R-0127`, `R-0053` |

A minimal public key is **62 octets**; with `alg`, 65. **And there is nothing
else.** RFC 8778 registers **no COSE header parameter and no JOSE anything**:
§6 touches three registries (`R-0118`) and "COSE Header Parameters" is not among
them, the word `header` occurs **0** times, and JOSE, JWK and JWS occur 0 times.
`R-I-01`'s mapping table gains **three integers** and no header row.

**The signature, as a `COSE_Sign1` (`messages.yaml` `S-0011`):**

```
d2  84  44 a101382d  a1 04 46 'ItsBig'  54 <20-octet payload>  5909d0 <2512 octets>
```

Tagged **18**; the `COSE_Sign` form in A.1 is tagged **98**. Envelope overhead 40
and 48 octets respectively, measured.

### 2. `DEC-002` — this document **reproduces**, **refutes** and **bounds** `rfc-9964`'s headline result, and that is the sharpest thing in it

`records/ietf/rfc-9964` (at `profile: full`) found that a post-quantum `KeyId`
**contains an IANA allocation inside the digest preimage** — the COSE `alg` value
−48/−49/−50, at offset 5 of a 1322-octet thumbprint input, turning one
byte-identical `pub` into three principals. Three legs follow for HSS-LMS, and
each was re-derived here against `.cache/rfc-8778.txt` rather than taken from
that record.

**Leg 1 — REPRODUCES, by a different mechanism, and the mechanism is worse.**
For HSS-LMS the allocation is not in a map entry. It is in the **key material**.
`R-0053` puts two `u32str` values at the front of the public key, and both index
IANA registries: `R-0046` (§2.2) and `R-0077` (§2.3) say `[HASHSIG]`
"establishes an IANA registry to permit the registration of additional hash
functions and additional tree sizes in the future" and "additional hash
functions and additional parameter sets in the future"; `R-0019` (§2) adds the
one-way-hash-function registry. So **octets 0–7 of every HSS-LMS public key are
two IANA code points**, and `R-0024` makes that the HSS public key as well as the
LMS one. **No choice of digest input removes them.** `DEC-003` option 1 ("raw
COSE key") carries them; option 2 (RFC 9679 §4.5's `{kty: 5, pub}`) digests
them; and `rfc-9964`'s Cut B escape — "digest `(kty, pub)` alone" — digests them
too. **A second independent instance of the general proposition, and this one has
no escape at all.**

**Leg 2 — REFUTES `rfc-9964`'s escape clause, and that record has already been
narrowed.** `rfc-9964`'s design notes conclude that "An AKP `pub` is
`alg`-independent" and therefore "for AKP keys `DEC-003` option 1 is immune to
this hazard"; its own correction block records that the premise was first stated
without naming a key type — "The premise is AKP-specific and was stated as
general." **True for AKP, false for HSS-LMS**, where the raw `pub` is
precisely the thing carrying the code points. The immunity is a property of a
key type's public-key encoding, not of option 1.
**`records/ietf/rfc-9964` and `records/ietf/rfc-9679` were both narrowed on
2026-10-20 on the strength of exactly this, before this extraction ran. This pass
re-derived both narrowings from the source and they stand; neither record was
edited by it.** See *Checks against the sibling records*.

**Leg 3 — BOUNDS the mechanism, and the bound is as useful as the result.**
`rfc-9964`'s *measured* hazard — one byte-identical `pub`, three `KeyId`s,
differing in one octet at offset 5 — **cannot arise for HSS-LMS at all**, for two
independent reasons:

1. **COSE `alg` −46 is not in the preimage.** `R-0087` makes `alg` conditional —
   "If the 'alg' field is present, it MUST be 'HSS-LMS'" — and RFC 9679 §4.5
   requires only `kty` and `pub`. A conforming HSS-LMS COSE key need not carry
   `alg` at all. **[analysis] The offset-5 `alg` mechanism — −48/−49/−50 inside
   the preimage — is AKP-specific.**
2. **There is no "same key material under two algorithms".** Relabelling the
   parameter set changes `lms_algorithm_type`, and it changes `T[1]` with it,
   because `T[1]` is a Merkle root computed under that parameter set
   (`R-0052`, `R-0039`). A different parameter set is a different key, not the
   same key under a different name.

**[analysis] So HSS-LMS is a counter-instance to `rfc-9964`'s *reason* and a
second instance of its *conclusion*.** The surviving general proposition, now
resting on two key types and two mechanisms: **registry-independence is
unavailable for a post-quantum principal under every `DEC-002` option and every
`DEC-003` option.** `MD-3` narrowed `DEC-002` to option 5 partly on
registry-independence; that premise is not available here, and the ADR must state
it rather than inherit it.

**[analysis] And one consequence that runs the other way, in our favour.**
Because the only registry dependence sits inside `pub`, and every option carries
`pub` identically, **an HSS-LMS `KeyId` is the same value under `DEC-002` option
2 and under option 5.** Nothing about the native-versus-export choice moves it.
That is a genuine reduction in the cost of leaving `DEC-002` open, and it is a
second independent instance of `rfc-9679`'s Cut D ("`DEC-003` does not wait on
`DEC-002`"). Recorded as Cut E below.

### 3. `DEC-003` — a sixth answer to "what is a KeyId", and the only one where the identifier is a *field of* the key

`DEC-003`'s options are "raw COSE key; COSE key thumbprint; `did:key`; hash-uri
(`sha256:…`); text KeyId" (`ARCH-0001` §7). §3's fifth bullet adds a sixth
shape, `R-0090` with `R-0092`:

> If the 'kid' field is present, it MAY be used to identify the top of the HSS
> tree.

> it is the 16-byte identifier of the LMS public key for the tree.

and §2.2 `R-0049` puts that value **inside** the key: "The value I is also
available in the public key." **[analysis] Every other answer in the library is a
*function of* the key — a digest, a URI over a digest, a chosen string. This one
is a *projection of* it: 16 of its 56 octets, read off.** No digest, no
canonicalisation, no hash-algorithm agreement, no `R-O-03` citation problem.

**And no binding.** Nothing in RFC 8778 says a `kid` must be the key's `I`, or
that a verifier may rely on it, or what to do if it is not — and the document's
own examples use six ASCII octets instead (`V-0008`). So the shape is available
and the guarantee is not. **[analysis] For P1, which makes a `KeyId` a namespace
root, an unauthenticated projection of the key is strictly worse than a digest of
it: a digest cannot be wrong about which key it names, and a `kid` can.** Our
answer should be the §4.5 thumbprint, with `I` available as a cheap
pre-filter and never as a name.

### 4. `R-M-02` — the size trade inverts, and the expensive option becomes the cheap one

`R-M-02` is "A principal MAY be identified solely by key or key digest." For
ML-DSA `rfc-9964` made this a 41×–81× size trade. **Here it collapses**: the
public key is **56 octets, 24 more than its own SHA-256 thumbprint**, and the
minimal `COSE_Key` carrying it is 62, 30 more.

**[analysis] One measured detail makes "carry the Key" cheaper still, and it is
the same detail `rfc-9964` found for AKP.** A **minimal** HSS-LMS public
`COSE_Key` — `kty` and `pub` and nothing else, in RFC 8949 §4.2.1 order — is
**byte-identical to its RFC 9679 §4.5 thumbprint input**, both 62 octets, for
every admitted parameter set (`messages.yaml` `S-0008`, `V-0010`). So if our
profile fixes that as the wire form of a carried key, a verifier that receives
the key computes its `KeyId` by hashing **the bytes it already has**, with no
re-encoding step and therefore no re-encoding divergence. Two key types now have
this property and it should be a profile rule, not a coincidence we rely on
twice.

**[analysis] The consequence for `DEC-003` is that the trade is not about size at
all for this suite.** 24 octets is not a reason to prefer a `KeyId`. The reasons
left are the ones the `canonical-encoding` topic names: a digest is fixed-width
and opaque, a key is self-describing and lets a verifier check `alg` agreement.
`R-M-02`'s MAY is genuinely free here, which it is not for ML-DSA.

### 5. `ARCH-0002` P1 — a namespace root with a **counted lifetime** and **no backup format**

This is the finding no other record in this lane supplies. P1 (accepted by
`ADR-0001`) roots every name in a key: a type is `(defining key, local label)`.
§5 gives that root three properties no other candidate key type has.

**It is counted.** `R-0109`:

> In the absence of a public key infrastructure [RFC5280], this public key is a
> trust anchor, and the number of signatures that can be generated is bounded by
> the size of the overall HSS set of trees.

**It is not exactly knowable.** `R-0114`:

> As a result, the total number of signatures that can be generated might be
> less than the overall HSS set of trees.

§2.2 `R-0037` gives `2^h` leaves per tree for `h` in {5, 10, 15, 20, 25}
(`R-0036`), and `R-0113` then sacrifices some of them. **[analysis] So a
principal's remaining capacity to speak is a quantity neither a verifier nor
necessarily its own holder can compute from the parameter set.**

**It retires by exhaustion, not by policy.** `R-0110`:

> When all of the LM-OTS signatures have been used to produce a signature, then
> the establishment of a new trust anchor is required.

— in **lowercase `required`**, with no procedure, no cross-signature from the old
root to the new, and no way for a verifier to learn that a principal was
replaced. `state-machine.yaml` records all three gaps under `unspecified`.

**[analysis] And it cannot be backed up, replicated or migrated**, because
`R-0115` withholds the only format that would let it be. A namespace root under
P1 that exists in exactly one place, for a finite and imprecisely known number of
utterances, and then stops.

**[analysis] This forces `rfc-9964`'s and `rfc-9679`'s deferred question.** Both
records leave open whether `KeyId` means "this key, now" or "this principal,
across changes", and `rfc-9679` notes that `R-O-01` reads like the second.
**For ML-DSA the question is deferrable because a key need never change. Here it
is not**: every HSS-LMS principal is *guaranteed* to be replaced, by
construction, and the replacement is not optional and not scheduled by us. If
`KeyId` is the durable identifier, then **every** HSS-LMS principal eventually
becomes a principal nobody can name, and every type it defined and every name in
its chain is relabelled with it. The construct `rfc-9679` identifies as the
answer — a stable `Name` under a stable naming key, resolving to whichever
`KeyId` is current (`ARCH-0001` §4.2's `NameCert`, §4.3's "rewrite `Name` to
`KeyId` via `NameCert` chains") — is **not optional** for this suite. It is a
precondition of using it at all.

**[analysis] Which raises the regress, and it is worth writing down.** A
`NameCert` is a signed object. If the naming key is itself HSS-LMS, the naming
key is also exhaustible, so the continuity construct inherits the problem it
exists to solve. A mixed-suite answer — a long-lived naming key in a stateless
post-quantum suite, short-lived HSS-LMS signing keys beneath it — is the only
shape that closes, and nothing in our documents contemplates two suites at once.

### 6. `R-O-01` — a per-object price no other candidate carries

`R-O-01` is "Every signed object SHALL have an issuer key that can be specified
as `KeyId`." Under this algorithm that `SHALL` costs something per object that no
other suite in this library charges. `R-0101`:

> An implementation MUST ensure that an LM-OTS private key is used to generate a
> signature only one time and ensure that it cannot be used for any other
> purpose.

**[analysis] Three consequences, in order of how much they would change our
code.**

1. **Signing is not idempotent and cannot be retried.** Every signed object
   consumes one leaf irreversibly. A retry after an ambiguous failure either
   wastes a leaf or reuses one, and `R-0112` does not say which ordering to use.
2. **A crash between signing and committing state is a forgery risk rather than a
   transient error.** `R-0098`: "Loss of integrity of this tracking data can
   cause a one-time key to be used more than once." `R-0099` names the causes.
   Nothing in RFC 8778 detects the condition afterwards.
3. **A principal has a maximum number of statements it can ever make.** Combined
   with `R-0109` and `R-0114`: the total count of signed objects attributable to
   one issuer is bounded and imprecise. Any design that assumes an issuer can
   always sign one more thing is wrong under this suite.

### 7. `DEC-005` — a stateful one-time-signature scheme is a **recommended** COSE algorithm

`DEC-005` is "Envelope for ArtifactStatement. Options: DSSE (in-toto world),
COSE_Sign1 (SCITT world), both with a single unsigned payload schema." §6.1
`R-0122` registers `alg` −46 with **"Recommended: Yes"**, and Appendix A
exercises **both** COSE envelope shapes — `COSE_Sign` (tag 98) and `COSE_Sign1`
(tag 18), `V-0001` and `V-0002`.

**[analysis] Second independent instance of `rfc-9964`'s Cut D, and it is
stronger because this algorithm is harder to carry.** COSE has a registered,
interoperable, affirmatively recommended post-quantum signature identifier;
`records/community/secure-systems-lab-dsse` records DSSE as "Deliberately
algorithm-agnostic", with signature algorithm and key management "out of scope".
For a post-quantum `ArtifactStatement`, COSE_Sign1 again is the only option with
a standardised algorithm identifier.

**[analysis] And the cost side, which `DEC-005` does not list and `MD-3` did not
weigh.** The price of admitting a *recommended* algorithm that is stateful is
operational, not cryptographic: a signer that cannot be replicated, a finite
signature budget, and a crash window that is a security property. **`DEC-005` is
a choice about envelopes and this is a constraint on deployment topology.** It
reaches `DEC-005` only because "Recommended: Yes" means an interoperating peer
may legitimately present us with this algorithm — so the *verifier* side of our
`DEC-005` choice must accept −46 whether or not we ever sign with it, and
verification carries none of the cost.

### 8. `R-M-12`, `R-O-03` and the `canonical-encoding` conditions

**`R-M-12` is unsatisfiable for this key type's parameter identification, and
for a structural reason.** `R-M-12` requires an extension point to be a
`(key, local label)` pair, and `MD-3`'s option-5 text has types and tags
"identified key-relatively per R-M-12, carried as ordinary map entries".
**[analysis] The two `u32str` code points in an HSS-LMS public key are not map
entries and cannot be made into any.** They are octets 0–7 of a byte string that
a Merkle root is computed over. `R-M-12`'s mechanism operates at the map layer;
this registry dependence is **below** it. That is Cut B seen from the `R-M-12`
side, and it is the first instance in the library of a registry dependence
`R-M-12` cannot reach even in principle.

**`R-O-03` costs a three-document citation chain with a gap in it.** `R-O-03` is
"Canonicalization algorithm for each concrete encoding SHALL be cited, not
invented silently" (`ARCH-0001` §5.3). To cite an HSS-LMS `KeyId` completely we
need: **RFC 9679** §3 and §4.5 (the computation and the parameter set),
**RFC 8949** §4.2.1 (the encoding, via RFC 9679 §3 step 2), and **RFC 8778**
§2.1/§2.2 (what the `pub` octets are — which RFC 9679 does not cite). To resolve
a parameter-set code point to a name we also need **RFC 8554**, because RFC 8778
prints none. `rfc-9679` found its own chain "thin and clean" at two normative
dependencies; this adds a third, and `records/ietf/rfc-8554` is a **stub**.
**[analysis] So `R-O-03` is satisfiable for the digest and not yet for the
parameter-set names. That is a library gap with an owner, not a design problem.**

**The six `canonical-encoding` conditions, one by one.** These are stated **in
this repository** (`topics/canonical-encoding.yaml`, status `answered`), so this
is the one block of our own rules this record cites rather than reconstructs.

| condition | verdict for an HSS-LMS `KeyId` |
|---|---|
| (1) the encoding is **injective** over the values it encodes | **satisfied, and demonstrably.** The thumbprint input is a two-entry map whose only variable part is a fixed-width 56-octet `bstr`. Under RFC 8949 §4.2.1 the structure admits exactly one encoding, and distinct keys give distinct 56-octet values |
| (2) the **decoder rejects** non-canonical input | **not supplied, as the topic says.** `canonical` and `deterministic` occur **0** times in RFC 8778, and RFC 9679 §3 step 2 is an encoder rule. A non-minimal `bstr` head (`590038` for 56 octets) must be rejected and no cited document says so. **Ours** |
| (3) canonicalisation runs **once, at authoring**, never at verification | **violated by construction, and bounded tighter here than anywhere else.** `rfc-9679`'s Cut H is right that recomputing a `KeyId` from a received key canonicalises untrusted input. **[analysis]** But for this key type the untrusted input is a fixed 56-octet read with no length prefix, no optional field and no variable-length integer, so the parser has no decision to make and no state to be confused about. The hazard condition (3) names is a property of the key type's encoding, and HSS-LMS bounds it as tightly as it can be bounded |
| (4) the encoding profile is named by an **authenticated type indicator inside the signed bytes** | **not supplied for the profile; supplied for the key type.** `kty: 5` is inside the preimage, so the key *type* is self-describing. The encoding *profile* (RFC 8949 §4.2.1) is not named anywhere in the bytes |
| (5) set-valued fields in arrays have a **defined canonical order** | **inert at the identity layer.** The §4.5 thumbprint input has no array at all. `rfc-9679`'s Cut G found this for COSE Key Thumbprints generally and warned that §4.6 delegates the parameter set, so a future key type could bring an array in. **[analysis] For `kty: 5` that door is closed by RFC 8778 itself**: §6.3 registers exactly one parameter and §5 `R-0115` refuses to define the only other one. **But it re-opens if we carry the whole key**: `key_ops` (label 4) *is* an array holding a logical set, so `DEC-003` option 1 with a full `COSE_Key` brings condition (5) back onto the identity path. A reason to fix the minimal form as the wire form |
| (6) identity-bearing **text has a declared Unicode normalisation rule** | **inert.** Every field of the preimage is binary: `kty` is an int (RFC 9679 §4: "The tstr data type is not used with the "kty" element") and `pub` is a `bstr`. No text anywhere |
| **(0)** the key's own byte representation must be **pinned before any encoding rule applies** — `rfc-9679`'s own addition, of which it says "The remaining identity-path hazard today is condition (0)" | **DISCHARGED FOR THIS KEY TYPE, by RFC 8778 §2.1 and §2.2.** Four fields, every one fixed-width, nothing length-prefixed, nothing omittable, no numeric value with a leading-zero choice. There is no representation choice for a normalisation rule to settle. **[analysis] This is the cleanest key representation in the library on condition (0) — cleaner than EC2, which needs §4.2's compressed-point conversion, and cleaner than RSA, whose `n` leading octet RFC 9679 leaves unpinned and which needs RFC 8230 §4.** And RFC 9679 §4.5 does not cite it, so the discharge is reachable only through this record |

**[analysis] Net: the key type with the worst signature size has the best
identity path in the library.** Of the seven conditions, two are inert, two are
satisfied or discharged by the source, one is bounded as tightly as the construct
allows, and two remain ours — (2) and (4), both of which are ours for every key
type. That is not an argument for the suite; it is an argument about where the
risk in this suite is, which is the signature and the state, not the name.

### 9. Where this cuts against `MD-3`, and which `DEC-002` option each cut affects

`MD-3` narrowed `DEC-002` to **option 5** on 2026-09-28 — "CBOR as the canonical
encoding, using the CBOR data model and deterministic encoding rules, but with
**no reliance on the IANA CBOR Tags registry and no native use of COSE header
parameters**", with "COSE_Sign1 and DSSE remain **export** envelopes" — and
**narrowing is not acceptance**: `DECISIONS-0001` tier 1 item 2 says "Still open:
a narrowing is not an acceptance, and no ADR exists." `docs/extraction.md` is
blunt about what that means for an extraction: "**An extraction that can only
confirm is not evidence.**" Six cuts, each naming the option it moves.

**Cut A — the no-tags rule, third instance, now with the overhead measured.
Costs option 5; free under option 2.** Both of this document's examples are
**IANA-tagged** — tag 98 (`d862`) and tag 18 (`d2`) — and the untagged form is
never printed. The word `tag` occurs **0** times, so RFC 8778 exhibits the tagged
envelope without ever discussing the choice. Under **option 5** export must add
the tag and import must strip it; under **option 2** ("CBOR + CDDL as canonical;
COSE for signed form") the tagged bytes are native and there is nothing to strip.
**Measured here for the first time on this path**: the tag costs 2 octets
(`COSE_Sign`) or 1 (`COSE_Sign1`), and the whole envelope costs 48 or 40 octets
around a 2512-octet signature — **1.9% of the 2560-octet `COSE_Sign` and 1.6%
of the 2552-octet `COSE_Sign1`**. *(Corrected 2026-10-21: one figure, 1.6%, was
given for both.)* `rfc-9964` found the same
pattern for ML-DSA and `rfc-9679`'s Cut C was qualified by it. **Third instance,
not a new finding, and the measurement is new: the conformance rule is the cost,
not the bytes.**

**Cut B — option 5's registry-independence rationale fails again, by a mechanism
no option escapes. Affects options 1, 2, 3, 4 **and** 5 equally.** The full
argument is §2 above. Option 5 exists to keep "the native model free of central
allocation"; an HSS-LMS principal's name contains two IANA code points **in the
key material**, where no digest-input choice reaches them. `ADR-0001` rejects
private-use ranges because they give "escape from a registry, not a namespace" —
here there is not even an escape from the registry. **This does not reorder the
options. It removes a claim option 5 makes for itself, for the second time and on
a second key type.** `MD-3` narrowed on the strength of registry-independence;
the ADR must state that it is unavailable for post-quantum principals rather
than inherit the assumption.

**Cut C — option 5's *other* exclusion is inert here, and recording an inert
constraint is the point. Options 2 and 5 score identically.** Option 5 also
excludes "no native use of COSE header parameters". **RFC 8778 registers none**:
§6 `R-0118` names three registries — COSE Algorithms, COSE Key Types, COSE Key
Type Parameters — and COSE Header Parameters is **not** among them; the word
`header` occurs 0 times. `alg` (label 1) and `kid` (label 4) in the examples are
RFC 8152's own common header parameters, which both options use identically.
**[analysis] So for this algorithm the second half of option 5's exclusion list
has nothing to exclude.** Recorded because an extraction that only confirms is
not evidence, and because this is the second record (after `rfc-9679`'s Cut C) to
find one half of the narrowing's headline constraint doing no work.

**Cut D — `DEC-005` is discriminated again, and `MD-3`'s direction is supported,
with a cost `MD-3` did not weigh. Favours option 5's and option 2's COSE export
target; costs DSSE and "both".** §7 above. Recorded with the same weight as the
cuts that do not support the narrowing.

**Cut E — a place where options 2 and 5 provably give the **same** answer, which
is a reason to stop treating `DEC-003` as downstream of `DEC-002`. Neutral
between options 2 and 5; strengthens `rfc-9679`'s Cut D.** `rfc-9679`'s Cut D
argued that `DEC-003`'s mandatory clause is answerable now, in encoding-neutral
form. **[analysis] For HSS-LMS it is answerable *identically* under both live
options, and that is demonstrable rather than argued**: the entire registry
dependence and the entire key content sit inside `pub`, a 56-octet opaque
`bstr` that option 2 and option 5 carry byte-for-byte alike, and RFC 9679 §4.5's
preimage contains nothing else but `kty`. There is no native-versus-export
difference for the `KeyId` of this key type to be sensitive to. Second
independent instance of Cut D, and the first one with no residual.

**Cut F — the determinism table gains no rows, confirming `rfc-9679`'s Cut E on a
sixth key type. No option moves.** `rfc-9679`'s Cut E found that every
required-parameter label in §4 encodes in one octet, so §4.2.1's bytewise key
order and §4.2.3's length-first order coincide, and what §4.2.1 actually buys is
minimal-length `bstr` heads and minimal integer arguments. **Checked here**: the
HSS-LMS preimage has labels 1 (`0x01`) and −1 (`0x20`), one octet each, and its
only non-trivial encoding decision is the `bstr` head for 56 octets — `5838`,
already minimal. **Zero new rows.** Stated as a confirmation, and labelled one.

### 10. **[inference]** Statefulness and a replicated or threshold signer are incompatible — ours, not the document's

**This is a judgement of this extraction. RFC 8778 says nothing about threshold
signing, multi-party signing or replication: `party`, `parties`, `threshold`,
`share` and `quorum` occur 0 times in its 772 lines. No `R-*` id is asserted for
what follows, and `state-machine.yaml` records it under
`forbidden_transitions` with the same marking.**

Two sentences of the document are the premises. `R-0099` names "virtual machine
snapshotting or cloning" as a way the leaf-usage tracking data loses integrity,
and `R-0098` says that loss "can cause a one-time key to be used more than once".
`R-0115` and `R-0116` withhold the private-key-and-state serialisation
specifically "to avoid creating the ability to save the private key and state,
generate one or more signatures, and then restore the private key and state".

**[inference] An HSS-LMS signing key held in more than one place at one time is
the reuse attack**, and the document supplies no format with which to move it
from one place to another even sequentially. For an m-of-n project that is a
first-order constraint, not a deployment detail:

- **A threshold signer cannot hold one HSS-LMS key.** *n* holders of one key is
  *n* copies of the leaf counter, and the one property the algorithm needs is
  that the counter is single-valued.
- **The alternative shape — *n* distinct HSS-LMS keys, one per member, each
  signing independently — works and changes the object.** It is *n* signatures
  of 2512 octets, not one; a 3-of-5 threshold object is **7536 octets of
  signature** before anything else. `R-M-02`'s cheap principals do not help,
  because the cost is per signature.
- **Hot standby and failover are not available.** The warm copy is the attack,
  and there is no format in which to hand the key over cleanly.
- **And the state is not shardable by any mechanism this document defines.**
  Partitioning the leaf space between holders would work and would require
  agreeing a partition out of band, which is a protocol RFC 8778 does not have
  and `[HASHSIG]` §9.2 is cited for rather than specified.

**[inference] So admitting this suite is a decision about our deployment
topology, taken at the algorithm layer.** That is the single most decision-bearing
thing in the document for us, and it is nowhere in `DEC-005`'s option list or in
`MD-3`.

---

## Open questions

Items this document cannot settle, with who must.

1. **Is `KeyId` "this key, now" or "this principal, across changes"?** `rfc-9679`
   and `rfc-9964` both leave this open and note that `R-O-01` reads like the
   second. **This record forces it**: §5 guarantees every HSS-LMS principal is
   replaced. *The `DEC-003` ADR, and it cannot defer past this suite.*

2. **If the answer is `NameCert` continuity, what suite holds the naming key?**
   An HSS-LMS naming key is itself exhaustible, so the continuity construct
   inherits the problem. A mixed-suite answer is the only shape that closes and
   nothing in our documents contemplates two suites at once. *`ARCH-0001` §4.2,
   and whoever owns `NG3`.*

3. **May a `kid` be relied on as a key identifier when nothing binds it to the
   key?** §3 offers `I` as a `kid` and supplies no binding; the document's own
   examples do not take the offer. *One sentence of the `DEC-003` ADR: ours to
   forbid, since nothing stops a peer from doing it.*

4. **Which ordering does our signer use — commit-then-emit or emit-then-commit?**
   `R-0112` defers it to `[HASHSIG]` §9.2 and the two fail differently. *Ours,
   and it is a code rule with a test, like `rfc-9964`'s `ctx` requirement.*

5. **Does the `DEC-002` ADR accept that registry-independence is unavailable for
   post-quantum principals?** Two key types, two mechanisms, no escape under any
   option. *The `DEC-002` ADR, which does not yet exist.*

6. **Is a threshold object *n* independent HSS-LMS signatures, or is this suite
   simply out of scope for `R-M-06`-shaped constructs?** §10 above says the first
   is the only available shape and prices it at 2512 octets per member. *`DEC-005`
   and `R-M-06`'s owner.*

7. **Who extracts RFC 8554?** RFC 8778 defers to it for the `u32str` convention
   this pass had to measure, the parameter-set code points RFC 8778 omits, the
   values of `p` and `ls`, the §9.2 state-management approaches, and the test
   vectors that would turn this record's two templates into fixtures.
   `records/ietf/rfc-8554` is a **stub**, and it is the single highest-value
   follow-on this record identifies. **[flagged 2026-10-21, FX-1 pass 3] Three
   claims this record makes *about* RFC 8554 are unverifiable from this
   repository and are marked at every site where they are made: that its
   Appendix B table gives `p = 67` for `w = 4` and `p = 34` for `w = 8`
   (load-bearing for the W8 refutation in `summary.md`, `examples/README.md`,
   `examples/vectors.yaml` and `schema/parameter-sets.derived.yaml`); that its
   Appendix F prints LMS public keys (`examples/README.md`); and that it states
   the `u32str` width. **`bin/fetch-source` cannot close any of them**: that
   record's `content.sha256` is the empty string, so the tool would have no
   digest to verify fetched bytes against and would write unverified bytes under
   `--no-verify` or nothing at all — and its `content.url` is the HTML page, not
   the `.txt` rendering FX-1 needs. Closing them is an **ingest** of RFC 8554
   under this issue, not a fix a cross-check pass can make from inside this
   record. Nothing this record *measures* depends on any of the three.

---

## Checks against the sibling records

**`records/ietf/rfc-9679` (`FX-1`, `profile: full`) — its narrowing of
2026-10-20 re-derived, and it stands, with one thing to add.** That record's
blocker 2 originally read that "Symmetric `k` and HSS-LMS `pub` are opaque byte
strings with nothing to normalise" and was corrected to the fixed-width
argument. **Both the
correction's conclusion and its reason check out against
`.cache/rfc-8778.txt`**: `R-0053`'s four fields, `R-0092`'s 16, `R-0039` and
`R-0052`'s 32, `R-0024`'s identity, and 4 + 4 + 16 + 32 = 56. **What this record
adds and that one could not**: the corrected text treats the two `u32str` widths
as given from the notation's name, and **no document this library holds states
them**. This pass pins them by measurement (`V-0003`) and thereby closes the one
remaining unsourced width in the chain. **Not edited.**

**`records/ietf/rfc-9679`'s condition (0) — discharged for `kty: 5`, of which
that record says "The remaining identity-path hazard today is condition (0)".** §8 above. This is the
strongest cross-record contribution in this file and it is reachable only through
RFC 8778, which RFC 9679 §4.5 does not cite. **Not edited.**

**`records/ietf/rfc-9964` (`FX-1`, `profile: full`) — both of its 2026-10-20
narrowings re-derived from the source, and both stand.** Item 1 (option-1
immunity is AKP-specific, not general) and item 2 (Cut B narrows rather than
fails, and the `(kty, pub)` escape is refuted) are confirmed by §2 above. **One
refinement, not a correction**: that record's narrowing says the HSS-LMS code
points sit "in its first eight octets", which is right, and adds that for
HSS-LMS "even `pub` alone would not" escape the registry — also right. What it
does not say, and §2 Leg 3 establishes, is **why the measured three-`KeyId`
hazard cannot arise here at all**: relabelling the parameter set changes `T[1]`
with it, so there is no "same key material under two algorithms" for this key
type. The bound makes the general proposition cleaner. **Not edited.**

**`records/ietf/rfc-8554` — a stub, and the gap it leaves is load-bearing.**
RFC 8778 calls it `[HASHSIG]` and defers to it for the `u32str` convention
(`R-0028`), every parameter-set code point, every value of `p` (`R-0072`), the
checksum function (`R-0071`), the `signed_public_key` structure (`R-0030`), the
LM-OTS signature layout (`R-0079`) and the state-management approaches
(`R-0112`). **Seven deferrals, one stub.** Three of them this pass closed by
measurement; the code points it could not. Open question 7.

**`records/ietf/rfc-9052` — the COSE this document is not written against.**
RFC 8778 references **RFC 8152** throughout: the string `8152` occurs 7 times and
`9052` **0** times. §3's five key checks and §2's structures are unaffected by
the supersession, but a conformance statement of ours would have to say which
COSE it means, and §3's "two signature algorithm schemes" (`R-0080`) is a claim
about RFC 8152's text.

**`records/community/secure-systems-lab-dsse` — unchanged, and cited in §7.** Its
recorded position (algorithm-agnostic, key management out of scope, `KEYID`
unauthenticated) is what makes Cut D's second instance work.

---

## Defects and ambiguities in RFC 8778 itself

Reported, never repaired. Nine, listed in document order with their locators in
`normative.md`'s *Observations on the source*. The three that cost a reader
something:

1. **§2.3's definition of `p` contradicts §2.3's own layout.** `R-0070` defines
   `p` as "The number of n-byte string elements that make up the LM-OTS
   signature"; `R-0079` renders that signature as
   `u32str(otstype) || C || y[0] || ... || y[p-1]`, which holds **p + 1** such
   elements. Inherited from RFC 8554 §4.1 and measurable from this one section.
   Measured on the fixtures: `p = 67`, with 32 octets of `C` on top, giving 2180.

2. **§3's parseability claim is true of `[HASHSIG]` and not of this document.**
   `R-0083` and `R-0084` say the byte string "is designed for easy parsing" and
   that its type codes "indirectly provide all of the information that is needed
   to parse the byte string during signature validation". **RFC 8778 prints no
   code point for any of its nine named parameter sets** and defers every value
   of `p`, so a parser built from it alone cannot resolve the `00000003` and
   `00000006` its own Appendix A prints. It can only solve the length equation,
   which this pass did.

3. **Both Appendix A signatures carry the same `C`.** `R-0078` calls `C` "an
   n-byte random value"; octets 12–43 of both are the same 32 octets, over two
   different `Sig_structure` contexts from two different leaves. Not a violation
   of anything the document states, and a test suite built from these two
   fixtures gets no coverage of `C` varying. `V-0005`.

The other six are editorial: the missing space in §2's third component bullet
(`R-0017`); `T[r]` described as "the *i*th node" in one clause (`R-0050`);
"The [HASHSIG] includes" using a reference tag as a noun (`R-0036`); a
subject–verb disagreement in §4 (`R-0107`); a missing definite article in §5
(`R-0108`); and RFC 8610 classified as *informative* while being the only
definition of the notation the examples are printed in (`R-0130`).

**And two structural oddities that are not defects but shape every artifact
here.** The only statement of `I`'s width in the document is in a bullet about
`kid` (`R-0092`), so 16 of the 56 octets of the public key are specified in a
section about something else. And the only place from which the `u32str` width
can be recovered is a **non-normative appendix** — a normative structure
dimensioned by an example.

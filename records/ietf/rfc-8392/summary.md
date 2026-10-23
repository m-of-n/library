---
schema: "library-summary/v1"
id: rfc-8392
record: rfc-8392
type: summary
updated: "2026-10-20"
---

# CBOR Web Token (CWT)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard` — IETF Standards Track |
| **Authors** | M. Jones (Microsoft), E. Wahlstroem, S. Erdtman (Spotify AB), H. Tschofenig (ARM Ltd.) |
| **Published** | 2018-05 |
| **Identifier** | RFC 8392 · DOI 10.17487/RFC8392 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8392.txt |
| **Digest** | `9021ff7c4d274cf34873fe4f4fb17c4fe323247dd0f96bfcab54909bfcdc5f13` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

CWT is JWT re-cut for CBOR, and the re-cut is the whole document: the same
seven claims, keyed by small integers instead of strings, with every
cryptographic obligation delegated to COSE. §1 gives the motive plainly —
JSON "is considered inefficient for some Internet of Things (IoT) systems that
use low-power radio technologies" — so compactness is the argument the rest of
the document is answerable to.

**What it specifies is thinner than its stature suggests.** Seven claims
(`iss` 1, `sub` 2, `aud` 3, `exp` 4, `nbf` 5, `iat` 6, `cti` 7, with 0
RESERVED), and §3.1 says of all of them: *"None of the claims defined below are
intended to be mandatory to use or implement."* §3 adds that *"The set of
claims that a CWT must contain to be considered valid is context dependent and
is outside the scope of this specification."* So a CWT with no registered
claims — or none at all — is conformant. It also defines CBOR **tag 61**, four
IANA registrations, and §7's two procedures, which are pure delegation — §7.1
step 4 says it once per case, e.g. for the MAC branch: *"all steps specified in
[RFC8152] for creating a COSE_Mac/COSE_Mac0 object MUST be followed."*

A CWT is therefore a convention about where claims live, not a security
mechanism. §8 says so: *"The security of the CWT relies upon on the protections
offered by COSE."*

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | `R-I-03` names "COSE_Sign1 + CWT claims" as one of the two v1 envelopes, so this is a shape we may have to produce. |
| Cryptography | `none` | It mandates no algorithm and names none in normative text. See the DEC-005 note below. |
| This project | `core` | `DEC-003`: `iss`/`sub`/`cti` are the slots a `KeyId` would land in, and their CBOR types decide which `KeyId` form is even expressible. |
| Naming | **core** | `ARCH-0002 P1` wants `(key, local label)`; the CWT claim space is one flat global registry plus an unscoped Private Use range. Direct `R-M-12` conflict. |
| Encoding | supporting | Two tag prohibitions that help option 5 (§5, §2) and one tag definition that does not (§6). |

**Quotations of `mofn` documents below cannot be verified from this
repository.** Every quotation of `ARCH-0001`, `ARCH-0002`, `ADR-0001`, a `DEC-*`
or an `R-O-*` / `R-M-*` rule is reproduced from the extracting agent's context;
treat each as a citation to re-check against `mofn` before relying on it.
`distilled/design-notes.md` sets out this convention, which `rfc-9741`'s
cross-check pass established, and this summary now follows it (marker added
2026-10-21, pass 3). What **is** checkable in this worktree, and was checked:
`docs/extraction.md`'s statement of MD-3, `topics/canonical-encoding.yaml`'s
conditions, and the `rfc-9052` / `rfc-9053` / `rfc-9679` records — so the MD-3
gloss quoted further down is not covered by this marker.

### The finding to act on: a thumbprint cannot be an `iss`

`ARCH-0001` §6 carries "COSE_Sign1 + CWT" as an interchange row and asks that
`iss`/`sub` align with the `KeyId` profile. **They do not align, and the
mismatch is a type mismatch, not a policy one.** §3.1.1 and §3.1.2 both require
StringOrURI, which §2 defines as *"a CBOR text string"*. `DEC-003`'s leading
`KeyId` candidate — `rfc-9679`'s COSE Key Thumbprint — is a bare **byte
string**. A thumbprint is not a text string and cannot be an `iss` value.

Three slots exist and none is free:

- **`iss` / `sub`** — text string. Needs an encoding of the digest, and
  `rfc-9679` §5.7 supplies exactly one:
  `urn:ietf:params:oauth:ckt:<hash>:<value>`.
- **`cti`** (§3.1.7) — byte string, and so the only bstr-shaped claim. Wrong
  slot: it is the `jti` equivalent, an identifier *of the token*, not of a key.
- **COSE `kid`** (RFC 9052 §3.1, label 4) — byte string, so the thumbprint fits
  it exactly. But RFC 9052 §3.1 also says *"Applications MUST NOT assume that
  "kid" values are unique"* and *"The internal structure of "kid" values is not
  defined and cannot be relied on by applications."* `kid` is a hint by
  normative construction, so a `KeyId` placed there is identifying to us and to
  nobody else.

**So choosing the CWT envelope decides a question `rfc-9679` left open.** That
record names the choice — *"choosing between the bare digest and the
self-describing URI"* — and records that only the §5.7 URI form names the hash
function H. The CWT path forces the URI form, and with it pins H in the wire
format rather than in a side agreement. That is the one decision a reviewer
should take from this record.

A second, smaller consequence: §3.1.1 inherits JWT's semantics wholesale
(RFC 7519 §4.1.1), so `iss` is a *name of an issuer*, while `R-O-01`'s "issuer
key that can be specified as `KeyId`" is a name of a *key*. Nothing in RFC 8392
says those are the same thing, and `rfc-9679`'s record already flags that
neither `ARCH-0001`, `ARCH-0002` nor `ADR-0001` settles whether `KeyId` means
"this key, now" or "this principal, across changes". The CWT envelope does not
settle it either; it gives you two slots and lets you put a key in one and a
principal in the other without saying which is which.

### Where the key identifier sits in the one signed example, and what signs it

Figure 11 — the document's **only** signed CWT — puts `kid` in the
**unprotected** header. Decoded independently here from Figure 10's hex, the
object is `18([h'a10126', {4: h'…AsymmetricECDSA256'}, h'…', h'…'])`: `alg`
(−7) is protected, the key identifier is not. RFC 9052 §4.4's `Sig_structure`
takes `body_protected` and never the unprotected bucket, so **the key
identifier in RFC 8392's reference signed CWT is outside the signature.** Four
of the five Appendix A CWTs do the same.

That is COSE-conformant and not a forgery route — the signature still verifies
or it does not — but under `R-O-01` it means the statement does not bind its own
issuer key, and a verifier that selects a key by the unprotected `kid` can be
steered into failing. Our profile should put `KeyId` in the protected bucket.
`rfc-9597` is the registered mechanism for doing that with a *claim*, and
`rfc-9943` §6 is the ratified precedent for requiring it.

### `R-M-12`: the claim registry is the wrong shape, and failures are silent

`R-M-12` requires an extension point to be a `(key, local label)` pair. A CWT
claim key is neither: it is a globally-allocated label from a single registry
(§9.1), or an unscoped Private Use integer below −65536. Two issuers that both
reach for a Private Use key collide with nothing to disambiguate them — and §3
makes the collision quiet rather than loud: *"all claims that are not understood
by implementations MUST be ignored."* A conforming verifier drops what it does
not recognise instead of failing closed. There is no mechanism anywhere in the
document for scoping a label to the key that defined it.

### DEC-005: it mandates no algorithm at all

Worth stating because the record is filed against `DEC-005` and the answer is
nothing. RFC 8392 names no algorithm in any normative sentence; §7.1 step 4
hands all three cases to RFC 8152, and the only algorithm identifiers in the
document are inside Appendix A's examples (−7, 4, 10). Its `DEC-005`
contribution is the envelope shape and the claim slots. The algorithm catalogue
is `rfc-9053`'s — and that record's extraction already found that neither COSE
document names a mandatory-to-implement set either, so the whole CWT-over-COSE
stack specifies no algorithm anywhere.

### `R-O-03`: no canonicalization is cited, because none is needed — until it is

§7.1 step 2 is *"Let the Message be the binary representation of the CWT Claims
Set"* and names no canonical form. The Message then travels as an opaque
`bstr`, so determinism is **sidestepped rather than solved**: copying bytes
works and re-encoding does not. For `R-O-03` that is not a violation — there is
no canonicalization algorithm to cite — but it is a trap. The moment any party
rebuilds a claims set rather than forwarding its bytes, the signature dies, and
the document offers no rule that would have prevented it. §4 and §9.1.2 admit
floating-point `exp`/`nbf`/`iat`, and A.7 prints `1443944944.5` as a float64
(`fb41d584367c200000`) — the claim shape most likely to re-encode differently.

## Where it cuts against MD-3 — DEC-002 option 5

`MD-3` (2026-09-28) narrowed `DEC-002` to option 5 — "reduced CBOR, no IANA
tags, COSE as export only" — and is a **narrowing, not an acceptance**; no
`DEC-002` ADR exists.
<!-- [correction 2026-10-21, pass 3 - cross-check] This dropped "as" from the
     gloss, inside quotation marks attributed to MD-3. docs/extraction.md:124
     and this record's own design-notes (twice) have "COSE as export only".
     The lane-wide audit found both wordings in circulation library-wide and
     this was the lane's one live instance; it is the checkable form, because
     docs/extraction.md is in this repository and MD-3 itself is not. -->
 This document cuts both ways, and the cut against is the
more interesting half.

**For option 5, and from 2018.** §5 is a tag prohibition in the same spirit:
*"The claim values defined in this specification MUST NOT be prefixed with any
CBOR tag."* §2 does it again for one tag by name — NumericDate's encoding *"is
modified so that the leading tag 1 (epoch-based date/time) MUST be omitted."*
A Standards Track document stripping tags at the value layer, for exactly
option 5's reason (§5: *"Tagging claim values would only take up extra space
without adding information"*), is independent support worth citing.

**And §5 carries its own escape hatch**: *"this does not prohibit future claim
definitions from requiring the use of CBOR tags for those specific claims."*
So option 5's no-tags rule is not inherited from CWT. It survives only as long
as we control which registered claims we are willing to read, which makes
"no tags" a decoder rule of ours rather than a property of the format — the
positive-decoder-rule point `rfc-9052`'s design-notes §3.3 makes, arriving here
from the claim layer instead of the tag layer.

**Tag 61 is the sharp case, and it settles in option 5's favour.** §6 defines
it, §9.4.1 registers it, and §6 makes it optional in terms: *"Its use is
optional and is intended for use in cases in which this information would not
otherwise be known."* §7.2 step 3 permits the untagged COSE case outright —
*"If the object does not have a COSE CBOR tag, the COSE message type is
determined from the application context."* More to the point, **tag 61 was never
an authenticated signal**, and the document's own step order proves it: §7.1
step 6 prepends the tags *after* the signature exists, and §7.2 step 2 strips
them *before* validation begins. RFC 9052 §4.4 confirms it from the other side —
`Sig_structure` is `[context, body_protected, external_aad, payload]` and no tag
is an input. So dropping tag 61 under MD-3 costs **no authenticated
information**, and `rfc-9596`'s protected-header `typ` is a strictly stronger
replacement.

**What it does cost: fixtures, and the pairing rule.** §6 also says *"If
present, the CWT tag MUST prefix a tagged object using one of the COSE CBOR
tags"* — so CWT tagging and COSE tagging come as a pair, already recorded in
`rfc-9052`'s `distilled/design-notes.md` §3.2. The new observation is
quantitative: **four of the five Appendix A CWTs already carry no tag 61, and
not one of the five carries no tag at all.** Every example starts `18(`, `17(`,
`16(` or `61(17(`. The fully-untagged export that option 5 requires is
permitted by §7.2 step 3 and demonstrated nowhere in the defining document, so
a D5 fixture package has no reference bytes to check itself against.

**The cut against option 5: the registry we would actually depend on is the
expensive one.** `rfc-9052`'s design-notes deferred this explicitly — *"the CWT
claim keys are their own registry, so CWT interchange carries a second, larger
registry dependence than the tag; that is a DEC-003 and DEC-005 matter and is
outside this record."* This is where it lands, and §9.1.1's four policy tiers
price it:

| Claim-key range | Policy (§9.1.1) | CBOR encoding cost |
|---|---|---|
| −256…255, strings of length 1 | Standards Action | **1–2 bytes** |
| −65536…−257, 256…65535, strings of length 2 | Specification Required | 3 bytes |
| > 65535, strings longer than 2 | Expert Review | 5 bytes |
| < −65536 | **Private Use** | **5 bytes** |

Computed here from RFC 8949 §3.1 head encodings, not quoted.
**[narrowed 2026-10-20 by the FX-1 extraction, pass 1; the text-string bound
corrected 2026-10-21, pass 3.]** The Expert Review row
flattens two different costs: an integer above 65535 is **5** octets and a
three-character text key is **4** — `1 + n` **only to n = 23**, then **`2 + n`**,
so a 24-character key costs **26** octets and not 25. (This sentence read
*"`1 + n` thereafter"*, unbounded, until pass 3: pass 2 had corrected the same
cell in `distilled/schema/claim-key-policy.derived.yaml` and not propagated it
here.) The Expert Review and
Private Use integer rows also become **9** octets beyond ±2³². And there is
**no Private Use range for text keys at all**, so "pick a URI-ish label and
avoid the registry" is not an option either. The 5× headline and the 35-vs-7
arithmetic below survive unchanged; `distilled/schema/claim-key-policy.derived.yaml`
carries every tier priced over the boundary values of each range. **The policy-free
range costs five times the cheapest range**, in a format whose stated reason to
exist is byte efficiency on low-power radio. Seven claims of our own in Private
Use pay 35 bytes of keys against 7 for the registered set; the only way to buy
the cheap labels is Standards Action, which means an IETF document on an IETF
timescale.

That is the second independent sample of the regularity `rfc-9165`'s record
named — *the namespace that gets consumed is the one the policy subsidises* —
and it arrives from a different registry, under a different allocation policy,
in a document from a different working group. One sample was an observation; two
is a pattern worth writing into the `DEC-002` ADR when it is finally written.
The honest framing remains `rfc-9052`'s, and **[quotation corrected 2026-10-20
by the FX-1 extraction's own quote audit]** it reads, exactly: *`"No tags"` and
`"no registry dependence"` are different rules, and MD-3 states the first.* This
summary had it with **`only` inserted** — *"MD-3 states only the first"* — which
is the word the three design notes in this lane now add in their own voice,
marked `[analysis]`, rather than attributing it to that record. Adopting CWT
trades the tag registry for a bigger one.

## Implementations

*Searched 2026-10-20.* CWT, unlike the other two records in this lane, has real
implementations; the RFC itself names none and has no implementation-status
section.

| Name | Kind | License | URL |
|---|---|---|---|
| `t_cose` | C, constrained environments; COSE_Sign1 only | BSD-3-Clause | https://github.com/laurencelundblade/t_cose |
| `python-cwt` | Python, CWT + COSE | MIT | https://github.com/dajiaji/python-cwt |
| `ldclabs/cose` | Go, keys + RFC 9053 + RFC 9052 + CWT | MIT | https://github.com/ldclabs/cose |
| `@ldclabs/cose-ts` | TypeScript | MIT | https://www.npmjs.com/package/@ldclabs/cose-ts |

Licenses read from each repository's own metadata on 2026-10-20, not from
memory. `python-cwt` declares compliance with RFC 8392, RFC 9052 and RFC 9053
and is the most complete of the four against this record. No conformance test
suite was found for any of them, and none of the four was run here.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on` (widened to seven ids by the extraction) |
| `summary.md` | this document |
| `summary.html` | GENERATED and untracked — `bin/render-html`, see `docs/generated-views.md` |
| `distilled/` | **the FX-1 artifact set — all eight artifacts, pass 1 of 3 complete** |

**The extraction has landed, and `distilled/README.md` is its index.** Added
2026-10-20 by library#39 Tier 2: `normative.md` (37 verbatim regions,
per-region digests), `requirements.yaml` (110 entries, counts reconciling
9 = 9), `schema/` (1 verbatim + 4 derived, including §9.1.1's four allocation
tiers priced in octets), `messages.yaml` (5 structures, 23 fields,
`constrained_by` wired), `protocol.yaml` + `protocol.md` (three flows with
Mermaid diagrams — **applicable here**, unlike the lane's other two records),
`state-machine.yaml` (two loops, written out), `examples/` (12 vectors) and
`design-notes.md`. `distillation.standard: FX-1` is declared and **no
`profile`** is: passes 2 and 3 have not run and no `reviewed_by` is signed, so
the artifacts are readable and citable but not buildable-on.

**The one result to take from it:** all five of Appendix A's CWTs **verify
cryptographically** — A.3's ECDSA signature verifies, A.4's and A.7's MAC tags
reproduce, A.5 and A.6 decrypt with valid CCM tags, and A.6's plaintext is the
A.3 object byte for byte. The three primitives were implemented for that pass
over `hashlib` alone, with no CBOR, COSE, CWT, EC or AES library. That result
narrows two claims in this summary; both narrowings are recorded in Limits
below rather than edited away.

The CDDL this summary said would have to be ours is now in
`distilled/schema/`, correctly carrying `.derived.` in every filename —
RFC 8392 still contains none of its own, and the extraction measured it:
`CDDL`, `ABNF`, `ASN.1`, `JSON Schema`, `schema` and `grammar` each occur
**zero** times in the source.

## Limits

- **Appendix A.2.2's key is wrong twice, and both errata are still
  unverified.** Decoded independently here with a hand-written CBOR reader:
  Figure 6's hex gives `{−1: k, 1: 4, 2: h'…Symmetric256', 3: 10}`, while
  Figure 7's diagnostic notation prints `kid` at label **4** and
  `alg: 4 / HMAC 256/64 /`. Both differ from the bytes, and **the two reported
  errata push in opposite directions** — 7982 says the `kid` label should be 2
  (believe the hex), 8655 says the `alg` value should be 4 (believe the
  diagnostic). Both are still status *Reported* on the RFC errata site as of
  2026-10-20, eight years on. Figures 5 and 9 both print `kid` at label 2, so
  Figure 7 is the outlier.
- **And as printed, that key fails a conformance check.** It declares `alg` 10
  (AES-CCM-16-64-128) and is then used to MAC Figures 12 and 18, both of which
  declare `alg` 4 (HMAC 256/64) in their protected headers. RFC 9053 §3.1: *"If
  the "alg" field is present, it MUST match the HMAC algorithm being used."*
  **[narrowed 2026-10-20 by the FX-1 extraction, pass 1.]** This bullet
  continued: *"So **two of the five Appendix A CWTs are not reproducible from
  the printed key without applying two unverified errata** — decisive for
  anyone planning to use RFC 8392's vectors as fixtures."* **They are
  reproducible.** Both MAC tags — A.4's `093101ef6d789200` and A.7's
  `b8816f34c0542892` — reproduce exactly from Figure 6's own 32 octets of `k`
  under HMAC-SHA-256 truncated to 64 bits (`distilled/examples/vectors.yaml`
  V-0003, V-0006, V-0009). The two errata concern the key's **metadata** — the
  `kid` *label* and the `alg` *value* — and nothing in an HMAC computation reads
  either. So the finding is narrower and sharper: **A.2.2 is a working fixture
  that fails a conformance check on its own `alg` declaration.** The practical
  advice stands unchanged — use A.2.3's ECDSA key and Figure 10 instead,
  because that fixture is self-consistent **as well as** working, and the
  extraction confirmed both (`d*G == (x, y)`, the point is on P-256, and the
  signature verifies).
- **An `aud` array is permitted by the prose and excluded by both summaries of
  it.** §3.1.3 allows *"each of the audience array element values"* to be a
  StringOrURI *"when the audience claim value is an array"*. §4's Table 1 says
  `aud | 3 | text string` and nothing else; §9.1.2's registry entry says
  `Claim Value Type(s): text string`; all three printed examples use the scalar.
  **No erratum covers this** (checked 2026-10-20). A validator generated from
  Table 1 or from the IANA registry — which is what a code generator reads —
  rejects a conformant CWT. If we build CDDL for the CWT claim space, this is
  the one cell we must not take from the registry.
- **Both of its normative encoding references are obsolete.** It cites RFC 7049
  for CBOR (superseded by RFC 8949, which `rfc-8949` records as
  `supersedes: rfc-7049`) and RFC 8152 for COSE (superseded by RFC 9052 and
  RFC 9053, recorded on `rfc-9052`). Locators moved with them: §2's "Section
  2.4.1 of [RFC7049]" is §3.4.2 in RFC 8949. §7's procedures — the only
  procedures in the document — therefore cite a document this library marks
  `marginal`. Normal ageing rather than a defect, but it means nobody can follow
  §7 without a substitution table the document does not supply.
- **It settles nothing about which claims a CWT must have.** §3 puts that
  outside scope and §3.1 declines to make any claim mandatory. Deliberate, and
  also the single largest gap for us: `R-I-03`'s envelope needs a claim set, and
  this document supplies a vocabulary and no profile. `rfc-9943` §6 is the only
  ratified profile in the library that closes it (`iss` and `sub` both MUST) —
  and it closes it in the *header*, via `rfc-9597`, not in the payload.
- **Nothing here is reviewed.** This is a summary written from the source and
  from two adjacent `profile: full` records; no human has checked it, and the
  CBOR decodings and the byte-cost table are ours, computed here, not quoted
  from the document.

---
schema: "library-summary/v1"
id: rfc-9679
record: rfc-9679
type: summary
updated: "2026-10-19"
---

# COSE Key Thumbprint

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | standard — Proposed Standard |
| **Authors** | K. Isobe, H. Tschofenig, O. Steele |
| **Published** | December 2024 |
| **Identifier** | RFC 9679 · DOI 10.17487/RFC9679 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9679.txt |
| **Digest** | `f6b460e38ba1…` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

RFC 9679 defines a canonical digest of a COSE key: strip the key down to the
parameters that are *required* for its key type, encode that reduced map in
RFC 8949 §4.2.1 deterministic order, and hash it. The result is a stable
identifier for a key, independent of whatever optional parameters — `kid`,
`alg`, `key_ops`, `Base IV` — happen to travel with it. It also registers two
carriers: the `ckt` CWT confirmation member (§5.6, §8) and a
`urn:ietf:params:oauth:ckt:<hash>:<value>` URI (§5.7).

The required set is fixed per key type and nothing else is ever hashed: OKP
`kty`/`crv`/`x`; EC2 `kty`/`crv`/`x`/`y`; RSA `kty`/`n`/`e`; Symmetric
`kty`/`k`; HSS-LMS `kty`/`pub`. For P-256 the hashed input is 75 octets, and
the document's one fully worked example reproduces from it exactly.

SHA-256 MUST be supported and other hashes MAY be; the hash function is chosen
by the application and is **not carried in the digest**.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Naming | **core** | ADR-0001 promoted key-relative naming to ARCH-0002 P1, which makes the key identifier the root of the whole naming scheme. This is the candidate definition of that identifier. |
| Security | **core** | R-O-01: "Every signed object SHALL have an issuer key that can be specified as `KeyId`." |
| Encoding | supporting | The construction presupposes a canonical encoding but specifies none of its own; it inherits RFC 8949 §4.2.1. |

**Verdict from `distilled/design-notes.md`: ADAPT — and not yet for the
post-quantum path.** Adopt the construction (§3, §5.1); adapt the inputs. Three
blockers, and two of them are ours rather than the RFC's:

1. The thumbprint input *is* a `COSE_Key`, and §4 requires the `kty` integer
   from the IANA COSE Key Types registry — a class ADR-0001 and ARCH-0002 P1
   call interchange. Fixable with one ADR paragraph.
2. §4.3, §4.4 and §4.5 cite **no defining specification at all**, where §4.1
   and §4.2 both cite RFC 9053 §7.1. See Limits — this is a missing citation,
   not a missing rule.
3. For AKP — the only post-quantum key type — `alg` is inside the digest. Not
   ours to fix.

**What actually moves a `KeyId`, and it is not the algorithm.** The COSE Key
parameter `alg` is named **nowhere** in this document, and neither is `AKP`;
§4.1–§4.5 enumerate five key types and none lists label 3. So in RFC 9679
itself a key used under ES256 and under anything else has one thumbprint. Two
things do move it:

- **The hash function.** H is the application's choice and is not in the value,
  so changing it silently changes every `KeyId`, and two parties on different H
  never match on any key and cannot tell why. Only the §5.7 URI form names H.
  **Adopting this as `KeyId` means pinning H ourselves and choosing between the
  bare digest and the self-describing URI** — materially different failure
  modes.
- **§4.6's delegation.** "As other key type values are defined, their defining
  specifications should be similarly consulted to determine which parameters …
  are required." RFC 9964 §6 then answers that for AKP: `kty` (1, int, 7),
  `alg` (3, int), `pub` (−1, bstr). So one `pub` under ML-DSA-44 and ML-DSA-65
  gives different thumbprints — and since AKP has no `crv` and `pub`'s format
  is "specified by the alg value", **§7's own uniqueness test is what forces
  `alg` in.** There is no sanctioned subset: both escape hatches (§5.1, §7)
  contemplate thumbprints over *more* parameters, never fewer.

For ARCH-0002 P1 that is a renaming, not a re-signing: statements stay valid
but become statements by a principal nobody can name. **Nothing in ARCH-0001,
ARCH-0002 or ADR-0001 says whether `KeyId` means "this key, now" or "this
principal, across changes"**, and R-O-01 reads like the second. That is the
record's first open question.

Two further properties worth stating plainly: a private key and its public key
produce the **same** thumbprint (`d` is not required), and a Symmetric
thumbprint is a digest of a known four-byte prefix over the secret — which is
why §7 carries one MUST and two MUST NOTs about that single field.

## Implementations

The RFC names none and has no implementation-status section. Its one worked
example (§6) is a single EC2 P-256 key, and every other printed value in the
document descends from it. *Searched on 2026-10-19 for a named COSE Key
Thumbprint implementation; none found in the document.* The extraction
recomputed the whole §6 chain independently — reduced encoding, SHA-256
digest, `kid`, `ckt`, base64url and URN — with a hand-written RFC 8949 §4.2.1
encoder and no CBOR or COSE library, and all of it reproduces.

## Limits

- **RSA is unusable as cited, and the fix is one citation.** §4.3 requires `n`
  and `e` as bare `bstr` and says nothing about leading zero octets, which
  alone would leave §7's precondition unmet. **RFC 8230 §4 does close it** —
  "The octet sequence MUST utilize the minimum number of octets needed to
  represent the value" — but **RFC 9679 never cites RFC 8230, 0 occurrences**,
  and §4.3/§4.4/§4.5 cite nothing. The rule exists and is unreachable from this
  document. A `see_also` edge to `rfc-8230` now records it.
- **§4.5 is the same missing citation a second time, and it costs less.**
  Recorded 2026-10-20. §4.5 requires `pub` for an HSS-LMS thumbprint and cites
  **neither RFC 8778 nor RFC 8554 — 0 occurrences of each**. RFC 8778 §6.3 is
  the registry entry that defines label −1 for key type 5, and RFC 8778
  §2.1/§2.2 the
  only specification of the octets: "u32str(lms_algorithm_type) ||
  u32str(otstype) || I || T[1]", 56 octets, every field fixed-width. Unlike
  RSA, **no normalisation rule is owed** — there is no variable-length integer
  and no optional field for one to settle — so the cost is a reader's search
  rather than a thumbprint divergence. The `see_also` edge is authored on
  `rfc-8778`'s side, which is where its warrant is written out;
  `docs/references.md` derives the inverse rather than having both sides author
  it. **Honest limit: no HSS-LMS thumbprint is computable from any document
  this library holds** — RFC 8778 prints no `COSE_Key` and no `pub` value at
  all, `kty` occurring exactly once in it — so `examples/` carries no vector
  for this key type and none was synthesised.
- **The `ckt` registration pins SHA-256 while §3 does not.** §8 registers "COSE
  Key SHA-256 Thumbprint" and the value is a bare binary string with nowhere to
  name H, so a SHA-384 `ckt` is indistinguishable on the wire from a SHA-256
  one. A bare 32-octet `KeyId` is algorithm-ambiguous.
- **The §6 full example is not in §4.2.1 order.** It prints `kid` last where
  §4.2.1 sorts label 2 second — harmless for the thumbprint, since step 1 has
  already dropped `kid`, but a determinism-dependent specification labels a
  non-deterministic encoding "the following CBOR encoding" and switches regime
  between two adjacent hex blocks. Not in the errata. It is also the clearest
  proof that step 1 **re-encodes** rather than filtering in place.
- **No thumbprint this document defines can discriminate §4.2.1 from §4.2.3
  ordering.** Across all five key types every required label lies in −24..23
  and encodes in one octet, so bytewise and length-first sorts coincide. An
  implementation can get §4.2.1's map sorting wrong and pass every value the
  document prints.
- **§5.4 and §5.5 misattribute three cross-references between them.** Two are in
  §5.5 — the `ckt` to RFC 9052
  §7 (which is "Key Objects" and never mentions `ckt`, a member *this* document
  defines) and the `jkt` to RFC 7517 §4 (which lists JWK parameters; `jkt` does
  not occur anywhere in RFC 7517, and lives in RFC 9449 §6.1).
  **[correction] 2026-10-20: this bullet recorded two, and there is a third, in
  §5.4.** It glosses `x5t` as "(X.509 certificate SHA-1 thumbprint) [RFC9360]",
  and **"SHA-1" occurs zero times in RFC 9360** under every spelling checked.
  There `x5t` is `COSE_CertHash = [ hashAlg: (int / tstr), hashValue: bstr ]`,
  hash-agile, with SHA-256 the only algorithm it mentions and that one only
  "MUST support ... but can use other hash algorithms"; the parenthetical is
  the JOSE registry name for `x5t`, attached to a COSE citation. The source
  sentence is also **the only place RFC 9679's body names RFC 9360 at all**.
  All three sit in the two subsections that relate this thumbprint to a
  neighbouring construct, and each names a family document in place of the
  defining one — so it is one property of §5.4–§5.5 rather than three slips.
  The §5.4 leg is the worst of the three: the other two send a reader to the
  wrong place, this one states something false about the right one, and it
  states it in the direction of *weaker* security than RFC 9360 defines.
  `records/ietf/rfc-9360` authors `contradicts: rfc-9679` for it with the
  reason in its own `summary.md`; `contradicts` is symmetric and
  `docs/references.md` §2 derives the inverse, so no edge is authored here.
  Full working in `distilled/README.md` item 4.
- The extraction is **complete to FX-1 `profile: full`** — extract, verify and
  cross-check have all run at effort max. No human has signed anything off:
  every `reviewed_by` is empty, so these artifacts are machine-checked, not
  reviewed.

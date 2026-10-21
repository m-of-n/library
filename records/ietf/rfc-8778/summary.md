---
schema: "library-summary/v1"
id: rfc-8778
record: rfc-8778
type: summary
updated: "2026-10-20"
---

# Use of the HSS/LMS Hash-Based Signature Algorithm with CBOR Object Signing and Encryption (COSE)

|  |  |
|---|---|
| **Type** | rfc (IETF, Standards Track) |
| **Maturity** | `standard` — "This is an Internet Standards Track document", IESG-approved. **Not an STD**, and it normatively references RFC 8152, since obsoleted by STD 96 |
| **Authors** | R. Housley (Vigil Security) |
| **Published** | 2020-04 |
| **Identifier** | RFC 8778 · DOI 10.17487/RFC8778 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8778.txt |
| **Digest** | `sha256:2d43646b…` — full value in `record.yaml`, recomputed from `.cache/rfc-8778.txt` and re-verified 2026-10-20 |

## Overview

A short binding document with a long shadow. §3 is the whole COSE integration —
five checks on a COSE key: `kty` MUST be `HSS-LMS`; `alg` MUST be `HSS-LMS`
*if present*; `key_ops` must include `sign`/`verify` if present; and a `kid`
that MAY be the tree's 16-byte `I` — plus §6's three registry entries, `alg`
−46 marked "Recommended: Yes", `kty` 5, and `pub` at label −1. §2 restates
enough of RFC 8554 to make the wire format parseable, including the public-key
layout "u32str(lms_algorithm_type) || u32str(otstype) || I || T[1]" (§2.2) and
§2.1's statement that the HSS public key *is* the topmost LMS tree's public key.

The argument is §1.1's: HSS/LMS rests on hash collision resistance rather than
factoring or discrete logarithms, so it is post-quantum secure with no new
mathematics and can be deployed today to protect the software that will carry
tomorrow's cryptosystems. The price is §4's and §5's, and that is the reason to
read it. The scheme is stateful — "An implementation MUST ensure that an LM-OTS
private key is used to generate a signature only one time" — the signature
budget per key is finite and not exactly knowable, exhaustion forces "the
establishment of a new trust anchor", and **no COSE encoding for the private key
and its state exists**: §5 says it was "deliberately not defined… to avoid
creating the ability to save the private key and state, generate one or more
signatures, and then restore the private key and state."

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | **`core`** | §4 and §5 are an operational-security specification wearing a binding's clothes: one-time keys, state integrity, snapshot and clone hazards, trust-anchor replacement on exhaustion |
| Cryptography | `adjacent` | A binding, not a primitive — the primitive is RFC 8554, and this document adds no mathematics |
| This project | **`adjacent`** | NG3 defers the suite, so nothing here is adopted. The key model and the principal lifetime are decision-bearing now, whatever suite is eventually chosen |

`bears_on` reads as follows; the full warrant for each, with the quoted text,
is the comment block above `bears_on` in `record.yaml`.

- **DEC-002** — a second, independent instance of `rfc-9964`'s Cut B, by a
  different mechanism, and it **refutes that cut's escape clause.** rfc-9964
  concluded that "a raw `pub` is `alg`-independent, so DEC-003 option 1 is
  immune to this hazard". For HSS/LMS the raw `pub` is *not*
  parameter-independent: §2.2's public key begins with two u32 IANA code points,
  `lms_algorithm_type` and `otstype`. The allocation is in the key material,
  where no choice of digest input removes it — option 1 carries it, RFC 9679
  §4.5's `{kty: 5, pub}` thumbprint digests it, and rfc-9964's "digest
  `(kty, pub)` alone" escape digests it too. And the bound: §3 makes `alg`
  conditional and RFC 9679 §4.5 excludes it, so the COSE Algorithms value −46
  is **not** in the preimage. rfc-9964's general proposition reproduces; its
  stated mechanism is AKP-specific.
- **DEC-003** — §3's `kid` bullet is a sixth answer to "what is a KeyId", and
  the only one in the library where the identifier is a *field of* the key
  rather than a function of it. §2.1 + §2.2 are also the canonical-key-bytes
  specification DEC-003's mandatory clause demands — the one RFC 9679 §4.5
  requires and does not cite.
- **R-M-02** — "A principal MAY be identified solely by key or key digest."
  rfc-9964 made this a size trade; **for HSS/LMS it collapses.** §2.2's layout
  with m=32 and §3's 16-byte `I` give a 56-octet public key, 24 octets more
  than its own SHA-256 thumbprint, while Appendix A.2 measures 2512 octets of
  *signature* for a 20-octet payload. "Carry the Key, not the KeyId" is nearly
  free here and the expense moves to the signature.
- **ARCH-0002 P1** — the finding no other record in this lane supplies. P1
  roots every name in a key; §5 gives that root a counted lifetime and refuses
  it a backup format. A namespace root that cannot be replicated or migrated
  and retires by exhaustion rather than by policy. rfc-9964's open question —
  whether `KeyId` means "this key, now" or "this principal, across changes" —
  is deferrable for ML-DSA and is *forced* here.
- **R-O-01** — "Every signed object SHALL have an issuer key that can be
  specified as KeyId." Under this algorithm that SHALL has a per-object price
  no other candidate carries: every signed object consumes one leaf,
  irreversibly, and §4 names "failed writes, virtual machine snapshotting or
  cloning" as how the tracking data is lost.
- **DEC-005** — a stateful one-time-signature scheme is a *recommended* COSE
  algorithm (§6.1, "Recommended: Yes"), and Appendix A exercises both COSE_Sign
  (tag 98) and COSE_Sign1 (tag 18). The cost of admitting it is operational
  rather than cryptographic, and it is §5's.

**Not claimed, deliberately: the tag observation.** Both examples are tagged
and the untagged form is never printed — a third instance of `rfc-9964`'s Cut A,
not a new finding.

## Implementations

**Searched 2026-10-20.** One, named by the document itself; nothing else found
for the COSE binding.

| Name | Kind | License | URL |
|---|---|---|---|
| `cose-wg/Examples` | open source (test vectors) | not stated | https://github.com/cose-wg/Examples |

Appendix A says "The programs that were used to generate the examples can be
found at <https://github.com/cose-wg/Examples>", so that repository is the only
implementation this document vouches for, and it is an example generator rather
than a library. Searches for an HSS/LMS **COSE** implementation returned the
RFC and its mirrors only. Implementations of RFC 8554 itself exist independently
of COSE and were not enumerated — if NG3 is ever lifted, that is the search to
run, and the stateful-signer requirements in §4/§5 are the criteria to run it
against.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, the locator-by-locator warrant for each `bears_on` id, and the `distillation` block |
| `summary.md` | this document |
| `distilled/README.md` | the artifact index, the one result, the verification, and what pass 2 should attack |
| `distilled/normative.md` | every normative sentence with its locator, plus 25 byte-exact fenced runs of source lines and nine source observations |
| `distilled/requirements.yaml` | 135 entries, all 9 BCP 14 keywords, counts reconciled exactly; 135/135 locators resolve inside their section |
| `distilled/schema/` | 1 verbatim renderings file + 6 derived (3 CDDL, 1 ABNF, 1 JSON Schema, 1 parameter-set table), with the full 56-octet width derivation |
| `distilled/messages.yaml` | 11 structures, 35 fields, with offsets and encoded sizes; `constrained_by` wired on 30 of them |
| `distilled/state-machine.yaml` | **applicable** — two machines, 2 error states with no way out, 2 forbidden transitions, 5 unspecified behaviours |
| `distilled/protocol.{yaml,md}` | **not applicable**, with the word counts written out; `protocol.md` carries a state diagram as a reading aid |
| `distilled/examples/` | 11 vectors, 4 byte fixtures, both stated sizes reproduced to the octet |
| `distilled/design-notes.md` | the `rfc-9964` result, six `MD-3` cuts naming their `DEC-002` option, the conditions (0) and (1)–(6), seven open questions |

**FX-1 pass 1 of 3, and no `profile` is claimed.** `distillation.standard:
FX-1`, `pass: extract` on 2026-10-20 at effort `max`; **verify and cross-check
have not run** and every `reviewed_by` is empty, so the artifacts are readable
and citable but not buildable-on. `status` stays `summarized` for that reason.

**This replaces a settled decision, and the reason it was overturned is worth
recording.** On 2026-10-20 this record was to carry **no distilled artifacts at
all**: FX-1 here looked "unusually dependent on a second document — the record is a
9-keyword binding whose substance is RFC 8554's, and [`rfc-8554`] is a stub."
The extraction found that **wrong in the one direction that mattered**. Three of
the deferrals to `[HASHSIG]` turned out to be closable from RFC 8778 alone, by
measurement against its own Appendix A: the `u32str` width, the parameter set of
the printed signatures (`h = 10`, `p = 67`), and the length of an LM-OTS
signature. The dependency that *does* remain is narrower than it looked —
**the parameter-set code points**, which RFC 8778 names nine of and numbers none
of, so the document cannot resolve its own examples. Extracting RFC 8554 is still
the highest-value follow-on; it was not a precondition.

## Limits

- **No key is ever printed, which is why the DEC-002 finding is marked
  non-byte-verifiable.** `kty` occurs exactly once in the whole document (§3's
  checklist) and no COSE_Key or `pub` value appears anywhere; Appendix A gives
  signatures only. So the thumbprint RFC 9679 §4.5 defines for this key type
  **cannot be computed from any document this library holds**, and §2.1/§2.2's
  public-key layout is prose rather than bytes.

  **[correction] 2026-10-20, FX-1 pass 1.** This bullet used to end: "The u32str
  type-code convention is at least confirmed in the printed signatures, whose
  octets 8..11 are `00000003` — LMOTS_SHA256_N32_W8 — in both examples." The
  octets are right and **the name is wrong**, and the reason it is wrong is the
  sharper finding. `00000003` is at octets 8–11 of both signatures, as stated.
  But the structural arithmetic fixes `p = 67` for those signatures
  (`distilled/examples/vectors.yaml` `V-0003`), and 67 is the `w = 4` parameter
  count; `w = 8` has `p = 34` and would make the signature `1136 + 32h` octets,
  never 2512. So `00000003` cannot be the W8 code point. **And RFC 8778 supports
  neither reading: it names nine parameter sets and prints no code point for any
  of them**, so the document cannot resolve its own examples at all. What the
  printed signatures *do* pin, and nothing else in this library does, is the
  **width** — `u32str` is 4 octets, uniquely, because `2512 − 4u − 32` is
  divisible by 32 for no other `u`.
- **Its own examples ignore its own suggestion.** §3 says a `kid` MAY be the
  16-byte `I`; both Appendix A examples use `kid: 'ItsBig'`, six ASCII octets.
  The suggestion has no worked instance here, so anyone adopting it is the
  first.
- **Exhaustion is named and not handled.** §5 requires "the establishment of a
  new trust anchor" and stops. No rekey procedure, no cross-signature from the
  old root to the new, nothing about how a verifier learns a principal was
  replaced — the same hole `rfc-9964` found in `ARCH-0001` §4.2, reached from
  the algorithm side instead.
- **Statefulness and replication are incompatible, and this matters more to us
  than to most readers.** §4 names "virtual machine snapshotting or cloning" as
  a way one-time keys get reused, and §5 withholds a private-key serialisation
  precisely to prevent save-and-restore. A threshold or multi-party signer that
  holds one HSS/LMS key in more than one place is the attack. Recorded as our
  inference, not the document's claim: RFC 8778 says nothing about threshold
  signing, and no `R-*` id is asserted for it here.
- **RFC 8152, not RFC 9052.** The document predates STD 96 and references the
  obsoleted COSE throughout. §3's key checks and §2's structures are
  unaffected, but a conformance statement of ours would have to say which COSE
  it means.
- **Thin and conditional normative surface.** 9 BCP 14 keywords
  (`bin/bcp14-count`). Of §3's five key checks, `alg`, `key_ops` and `kid` are
  all conditioned on presence, so the only unconditional MUST about a key is
  `kty`. An implementation that omits `alg` is conforming, which is exactly
  what keeps −46 out of the thumbprint preimage.

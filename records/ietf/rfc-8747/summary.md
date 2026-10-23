---
schema: "library-summary/v1"
id: rfc-8747
record: rfc-8747
type: summary
updated: "2026-10-22"
---

# Proof-of-Possession Key Semantics for CBOR Web Tokens (CWTs)

|  |  |
|---|---|
| **Type** | rfc (IETF, Standards Track) |
| **Maturity** | `standard` — "This is an Internet Standards Track document", IESG-approved. **Not an STD**, and it normatively references RFC 7049 and RFC 8152, both since obsoleted |
| **Authors** | M. Jones (Microsoft), L. Seitz (Combitech), G. Selander (Ericsson AB), S. Erdtman (Spotify), H. Tschofenig (Arm Ltd.) |
| **Published** | 2020-03 |
| **Identifier** | RFC 8747 · DOI 10.17487/RFC8747 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8747.txt |
| **Digest** | `sha256:9b695379…` — full value in `record.yaml`, recomputed from `.cache/rfc-8747.txt` and re-verified 2026-10-20 |

## Overview

The claim is narrow and made precisely: a CWT can say *the presenter of this
token holds this key*, and it can say so in exactly three ways — by carrying
the public key (`COSE_Key`, member 1), by carrying the key encrypted to the
recipient (`Encrypted_COSE_Key`, member 2), or by naming it (`kid`, member 3) —
all inside one `cnf` claim at claim key 8 (§3.1, Table 1). It is the CBOR
restatement of RFC 7800 and says so in terms (§3.2, §3.3).

What makes it worth holding is not the claim. It is §3.4 and §6, which are the
standards-track account of what a bare `kid` is **not**: its content is
"application specific", with the hash-of-public-key construction offered as one
thing "some applications may choose" and no preimage specified; "implementers
should expect collisions" wherever the value is not cryptographically derived
from the key; and the value "is not necessarily the same for different
parties", so one key can have a different Key ID on each side of a single
conversation. §6 then
puts non-reuse on the *issuer* as operational discipline rather than on the
identifier as a property, with impersonation as the stated failure. The
document also establishes the IANA "CWT Confirmation Methods" registry (§7.2)
in which RFC 9679's `ckt` thumbprint was later allocated.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Proof of possession is a security mechanism, but §3.5 intentionally specifies no exchange: the nonce, its transport and the signed response are all out of scope |
| Cryptography | `none` | Invents nothing. Key representations are RFC 8152's, encryption is RFC 8392's, and no algorithm is registered |
| This project | **`adjacent`** | We may never need `cnf`. We do need §3.4's account of what a `kid` is, which is DEC-003's subject and R-O-01's literal one |

`bears_on` reads as follows; the full warrant for each, with the quoted text,
is the comment block above `bears_on` in `record.yaml`.

- **ARCH-0002 P1** — the sharpest thing here, and it is a definition by
  contrast. §3.4's Key ID is a *(party, local label)* pair resolved by table
  lookup. P1's extension point is a *(defining key, local label)* pair resolved
  by derivation. Same shape, different first element, and that difference is
  the whole of P1: a party-relative alias has an owner but no cryptographic
  root, which is ADR-0001's "escape from a registry, not a namespace" reached
  from the other side.
- **DEC-003** — §3.1's Table 1 *is* DEC-003's option list, drawn on the
  standards track in 2020: raw COSE key against text KeyId. And §3.4 is the
  precedent for declining DEC-003's mandatory clause, "Must specify: canonical
  key bytes before hashing" — it names the digest construction and specifies no
  key encoding, no parameter subset and no hash function.
- **R-O-01** — "Every signed object SHALL have an issuer key that can be
  specified as KeyId." §3.4 and §6 price the underived alternative: foreseen
  collisions, and uniqueness maintained by issuer bookkeeping on pain of
  impersonation. Prior art we do not follow, with the reason in the text.
- **DEC-002** — narrow, and it *bounds* a live finding rather than adding one.
  §7.2.2 makes the COSE_Encrypt/COSE_Encrypt0 tag **optional** for member 2 and
  §3.3's worked example carries the structure untagged. `rfc-9964`'s Cut A found
  every COSE example in RFC 9964 tagged 18 with the untagged form never
  printed. Both hold: customary at the top level, explicitly optional when
  nested — which is where an export mapping would put one.

## Implementations

**Searched 2026-10-20.** The `cnf` claim is implemented, partially, in the
Veraison and `python-cwt` lines; nothing found implements all three members.

| Name | Kind | License | URL |
|---|---|---|---|
| `veraison/eat` | open source | Apache-2.0 | https://github.com/veraison/eat |
| `dajiaji/python-cwt` | open source | MIT | https://github.com/dajiaji/python-cwt |
| `veraison/go-cose` | open source | MIT | https://github.com/veraison/go-cose |
| `ldclabs/cose` (Go) | open source | MIT | https://github.com/ldclabs/cose |

Two observations worth more than the list:

- **`veraison/eat` implements members 1 and 3 and not 2**, and says so: its
  `cnf` support covers "only OKP and EC2 COSE_Key, no EncryptedKey support". So
  the one member §3.1 constrains by name — at most one of `COSE_Key` and
  `Encrypted_COSE_Key` — is the one left out, and §3.1's constraint goes
  unexercised in the implementation most likely to be read as a reference.
- **`veraison/go-cose` defines the claim key and not the claim**: `cwt.go`
  carries the constant 8 with the remaining CWT claims marked TODO upstream. A
  constant is not an implementation, and the gap is recorded here so the next
  search does not count it twice.

Licences are as stated by each repository and were not re-verified against the
LICENSE files.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, and the locator-by-locator warrant for each `bears_on` id |
| `summary.md` | this document |
| `distilled/` | the full FX-1 artifact set — `distilled/README.md` is the index |

**This record is fully extracted.** Settled 2026-10-20 (library#39 Tier 2), this
section said *"No `distilled/`, deliberately"*, and that was true until
library#39 promoted the record out of Tier 2 — which is exactly the trigger the
old wording named. FX-1 ran 2026-10-21 to 2026-10-22: `normative.md`,
`requirements.yaml` (118 entries), `distilled/schema/`, `messages.yaml`,
`protocol.yaml`/`protocol.md`, `examples/` and `design-notes.md`, with
`state-machine.yaml` declared not applicable with its reason written out. The
extraction confirmed what the old wording predicted — the normative surface is
**8** BCP 14 keywords and none of them is in §3.4 or §6, the two sections this
record is held for, and `requirements.yaml`'s `reconciliation` says so at
length. It also found more than a summary could: a source defect in the
document's own worked example (`rfc-8747#D-0001`, §3.3's printed `COSE_Key` is
not the plaintext of its printed ciphertext — the entries are in a different
order), and six named cuts against `MD-3`, one of which ranks the `DEC-002`
options the opposite way round from the narrowing. See `distilled/README.md`.

## Limits

- **§3.1's co-presence rule does not cover the identifier members, and this is
  the one real gap.** "The "cnf" claim value MUST represent only a single
  proof-of- possession key. At most one of the "COSE_Key" and
  "Encrypted_COSE_Key" confirmation values defined in Table 1 may be present."
  (The space inside `proof-of- possession` is the line break at source lines
  180–181. Joining at the hyphen would make the quoted token occur nowhere in
  the document, which is the convention `requirements.yaml`, `normative.md` and
  `distilled/README.md` all state; this file used to be the one place that
  broke it.)
  Member 3 (`kid`) is in that same table and is *not* in that enumeration, and
  the second sentence's "may" is lowercase. RFC 9679 §8 later adds `ckt` at
  Confirmation Key 5. So `cnf: {3: …, 5: …}` — two identifiers for one key,
  with no stated precedence and no requirement that they agree — is not
  excluded by the letter of §3.1, while §3.1's own MUST ("all confirmation
  members that are not understood by implementations MUST be ignored")
  guarantees that an implementation knowing only one of them will silently use
  it. R-O-01 has to close this on our side; it cannot be inherited.
- **No binding rule between a `kid` and its key.** §3.4's hash-of-public-key
  suggestion fixes no key encoding, no parameter subset and no digest
  algorithm, so two conforming implementations can compute different Key IDs
  for one key. RFC 9679 §3 fixes exactly that, five years later, and only for
  the thumbprint route.
- **The weight of the document is not normative.** 8 BCP 14 keywords in total.
  §3.4's "implementers should expect collisions", §5's "it is recommended that
  different proof-of-possession keys be used" and §6's "needs to make sure" are
  all lowercase, and under `docs/requirements.md` §2 none of them is a
  requirement. That is precisely why this is prior art rather than something to
  conform to — and why a reader who takes §3.4 for a prohibition has misread it.
- **It settles no proof-of-possession exchange.** §3.5 is titled "Specifics
  Intentionally Not Specified": the nonce, how it is communicated and how the
  signed nonce comes back are all left to the protocol. Possession is declared
  here and demonstrated elsewhere.
- **The registry it establishes has moved on and we do not hold the snapshot.**
  §7.2.2's initial contents are members 1, 2 and 3; RFC 9679 §8 adds 5. What
  took Confirmation Key 4 is in neither this document nor this library.
- **Obsoleted normative base.** RFC 7049 and RFC 8152, not RFC 8949 and STD 96.
  Nothing in §3's structures depends on the difference, but a conformance
  statement of ours would have to say which CBOR and which COSE it means.

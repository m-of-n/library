---
schema: "library-summary/v1"
id: rfc-9338
record: rfc-9338
type: summary
updated: "2026-10-20"
---

# CBOR Object Signing and Encryption (COSE): Countersignatures

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | standard — Standards Track, and part of **STD 96** jointly with RFC 9052; header reads `STD: 96` / `Updates: 9052` |
| **Authors** | J. Schaad (Russ Housley served as document editor after Schaad's death in 2020; Acknowledgments) |
| **Published** | December 2022 |
| **Identifier** | RFC 9338 · STD 96 · DOI 10.17487/RFC9338 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9338.txt |
| **Digest** | `3fd3a4b1cb4060070ffcf6104de0c12c6c5bed6cf2329d9019a16f7717365dde` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

A repair. §1 records that during COSE's advancement to Internet Standard "it
was noticed that the description of the security properties of
countersignatures was incorrect for the COSE_Sign1 structure mentioned in
Section 4.5 of [RFC8152]" — the cryptographically computed value "was not
always included" in what the countersignature covered — so the WG removed all
countersignature text from RFC 9052 and this document replaces it.

What it defines: two **unprotected** header parameters, `Countersignature
version 2` (label 11) and `Countersignature0 version 2` (label 12, §2);
`COSE_Countersignature = COSE_Signature` for the full form and
`COSE_Countersignature0 = bstr` for the abbreviated one (§3.1, §3.2); CBOR
**tag 19** for a standalone full countersignature (§5.1); and a
`Countersign_structure` that adds exactly one field, `other_fields`, to the
RFC 8152 to-be-signed array (§3.3). IANA's Descriptions for the old labels 7
and 9 now carry "(Deprecated by RFC 9338)" (§5.2).

Its normative surface is two sentences: §4's "The narrowed deterministic
encoding rules MUST be used to ensure that all implementations generate the
same byte string for the 'to be signed' value", and §6's "To provide 128-bit
security against collision attacks, the tag length MUST be at least 256 bits."
Everything about migrating off the broken mechanism is in **lowercase** prose.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | **core** | It exists because the predecessor's coverage was wrong, and what a signature covers is the only question it answers. |
| Cryptography | adjacent | It specifies no algorithm; §3.1 constrains the *class* (signature schemes "with appendix" only), which is a `DEC-005` input. |
| This project | **core** | `DEC-005`, `R-M-12`, `R-O-05`, and the nearest COSE primitive to a transparency witness — `rfc-9052`'s design notes already weighed it and this record narrows that verdict. |

**The finding to act on: the fix reaches three of the eight COSE structures,
and the five it misses keep RFC 8152's context string and omit the
cryptographic value — which is the defect this document exists to remove.**
§3.3's rule is arithmetic on the target: `other_fields` is "Omitted if there
are only two bstr fields in the target structure" and otherwise is "an array of
all bstr fields after the second"; the `context` string is `"CounterSignatureV2"`
only "when other_fields is present", and `"CounterSignature"` otherwise.
Counting `bstr`-typed slots against RFC 9052's own CDDL — held verbatim in this
library at `records/ietf/rfc-9052/distilled/schema/cose.cddl` — gives:

| target | `bstr` slots | `other_fields` | `context` |
|---|---|---|---|
| `COSE_Sign1` | protected, payload, signature | `[signature]` | `CounterSignatureV2` |
| `COSE_Mac` | protected, payload, tag | `[tag]` | `CounterSignatureV2` |
| `COSE_Mac0` | protected, payload, tag | `[tag]` | `CounterSignatureV2` |
| `COSE_Signature` | protected, signature | **omitted** | `CounterSignature` |
| `COSE_Sign` | protected, payload | **omitted** | `CounterSignature` |
| `COSE_Encrypt` | protected, ciphertext | **omitted** | `CounterSignature` |
| `COSE_Encrypt0` | protected, ciphertext | **omitted** | `CounterSignature` |
| `COSE_recipient` | protected, ciphertext | **omitted** | `CounterSignature` |

The `COSE_Sign1` row is checkable against the document: §3.3 says
`other_fields` "would be an array of one element for the COSE_Sign1 structure
containing the signature value", which is only true if `payload` counts as the
second `bstr` field. Apply the same count everywhere and **a countersignature
on a `COSE_Signature` does not cover the signature it is countersigning.** §1
concedes it in a subordinate clause — "The exception to this is the
COSE_Signature structure where there is no cryptographically computed value" —
and §3 asserts the opposite two pages later: "When done on a COSE_Signature or
COSE_Sign1, the normal countersignature semantics are preserved. That is, the
countersignature makes a statement about the existence of a signature". Both
cannot hold. **The "V2" names the header label and the registry row, not the
signed bytes.**

For the five omitted rows the signed byte string is the RFC 8152 one, by
design: §1 says the new algorithm "is designed to produce the same
countersignature value in those cases where the computed cryptographic value
was already included. This means that for those structures the only thing that
would need to be done is to change the value of the header parameter." So the
`context` string — the only domain separator in `Countersign_structure` — does
not separate the old mechanism from the new one for five of eight targets.
Combined with §1's instruction that new implementations keep *verifying* label
7, a verifier that accepts both accepts the same bytes under two names.

**And `sign_protected` is ambiguous exactly where it matters.** §3.3 defines
`body_protected` as "the serialized protected attributes from **the target
structure**" and `sign_protected` as those "from **the signer structure**",
with the signing process taking "the countersignature target structure … [and]
the signer information (COSE_Signature)" as separate inputs. When the target is
itself a `COSE_Signature` inside a `COSE_Sign`, those two readings diverge:
read by the field names, `body_protected` is the countersigned
`COSE_Signature`'s bucket and the enclosing `COSE_Sign`'s protected header is
covered **nowhere**; read by analogy with RFC 9052 §4.4's `Sig_structure`
(where `body_protected` is the body's and `sign_protected` is the signer's),
the countersigned signer's own protected bucket is covered nowhere. The
document resolves neither, and `other_fields` is omitted either way. The
practical form: in all six of the document's own examples `kid` sits in the
*unprotected* bucket, so two signers over one payload with identical protected
buckets produce a byte-identical `Countersign_structure` — **a countersignature
over Alice's `COSE_Signature` verifies unchanged as one over Bob's.**

**Does it supersede RFC 8152's countersignatures? It deprecates them by
registry action and replaces the algorithm — and it is not a document-line
supersession.** The facts: §1, the WG "decided to remove all of the
countersignature text from [RFC9052], which obsoletes [RFC8152]"; §5.2, IANA
"has modified the existing 'Description' field for 'counter signature' (7) and
'CounterSignature0' (9) to include the words '(Deprecated by RFC 9338)'"; §1,
migration 7 → 11 and 9 → 12 is "encouraged". But every migration obligation is
**lowercase** in a document that invokes BCP 14 in §1.1: verification of
`CounterSignature` "must be supported by new implementations", of
`CounterSignature0` "may be supported". Neither is a BCP 14 keyword, so the
backward-compatibility contract of a repair document carries no normative force
at all.

**Typed relations, and what was deliberately *not* set.** `updates: rfc-9052`
stands — the RFC's own header says `Updates: 9052`. **`supersedes: rfc-8152`
is deliberately not set**, and the reasoning belongs in the record rather than
in a reviewer's head: `docs/references.md` §3 scopes `supersedes` to document
*lines*, `rfc-9052` already carries `supersedes: rfc-8152`, and `rfc-9053` —
which replaces another severed part of RFC 8152 — does not. Adding a second
edge would render `rfc-8152` as `superseded_by: [rfc-9052, rfc-9338]`, reading
as two alternative whole replacements of one document, which is precisely the
silent citation retargeting this library's id rules exist to prevent. The
mechanism-level supersession is real and is recorded instead as
`see_also: rfc-8152` plus the §5.2 locator above. Overrule it if the library
decides mechanism-scoped supersession deserves its own relation; it currently
has none.

**Usable as a transparency or witness co-signature? For exactly three targets,
and the live open question is one of the five it misses.**
`records/ietf/rfc-9052/distilled/design-notes.md` §6 already concludes that
countersignatures are wrong for `Endorse` and right for "a witness or receipt
over one exported statement … because `other_fields` binds the target's
signature bytes". **That verdict holds — and only for `COSE_Sign1`, `COSE_Mac`
and `COSE_Mac0`.** The same file's open question 7 asks whether the threshold
export extends the target from `COSE_Sign1` to `COSE_Sign`; the table above is
the price. A countersignature over a `COSE_Sign` binds **no signature at
all** — not one of the *n* `COSE_Signature` entries — so a witness receipt over
a *k*-of-*n* export would witness the payload and nothing about who signed it.
**That is the one thing a reviewer should carry back to `rfc-9052`.** Two
further ceilings the primitive cannot escape: §3 states no COSE timestamp
exists ("such a timestamp has not yet been defined for COSE"), so the "when" is
not carried; and label 11 is unprotected, so anything beside it is unsigned by
the primary signer.

**`R-M-12` and `R-O-05`.** The full countersignature "has the same structure as
COSE_Signature" and so "can have protected and unprotected attributes,
including chained countersignatures" (§3) — a second, *nested, unbounded*
instance of the same global COSE header label space, with no scoping by key or
by countersigner. Where `rfc-9360` §3 at least scopes its labels by algorithm,
this document scopes nothing, so `R-M-12`'s *(key, local label)* pair has no
native expression here. For `R-O-05`: the `context` text string is an
authenticated type indicator inside the signed bytes, which is the right shape,
and the table above is a worked example of that indicator **failing to
distinguish two versions of the protocol it is meant to version** — a hazard
rather than a confirmation.

## Implementations

The RFC names none and has no implementation-status section. §1 and §3 name two
*consumers* of the primitive rather than implementations of it:
`[GROUP-OSCORE]` (`draft-ietf-core-oscore-groupcomm-16`), which §3 cites for
the rule that "The countersignature needs to be treated as a separate operation
from the initial operation even if it is applied by the same user", and
`[RFC4998]` Evidence Record Syntax, cited in §3.1 for chained countersignatures
in long-term archiving. The only tool it names is `[CBORDIAG]`
(`github.com/cabo/cbor-diag`, commit 1952a04), needed to turn Appendix A's
diagnostic notation into bytes. *Searched on 2026-10-20 for a named RFC 9338
implementation: none in the document.*

| Name | Kind | License | URL |
|---|---|---|---|
| cbor-diag | tool (diagnostic↔binary, needed to use Appendix A) | MIT | https://github.com/cabo/cbor-diag |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

**No `distilled/` yet, and this one has the strongest claim on an extraction of
the three in this lane.** This PR claims the **summary bar**: the record is
`summarized`, declares no `distillation` block, and touches no `distilled/`, so
FX-1 does not fire (`docs/extraction.md`). But the case for extracting it later
is concrete rather than hypothetical, and naming it is the point of this
paragraph. **What would trigger an extraction** is `rfc-9052`'s open question 7
being answered "extend the target to `COSE_Sign`", or any transparency/receipt
increment: `examples/` would hold all six Appendix A messages as fixtures
(180, 275, 326, 136, 159 and 159 bytes, each convertible with `diag2cbor.rb`),
`schema/` would hold the four CDDL fragments plus a `*.derived.cddl` with
erratum 7338 applied, `messages.yaml` would carry the coverage table above as
eight rows with their `other_fields` and `context` values, and
`requirements.yaml` would have to record that only **two** BCP 14 statements
exist and that the migration contract is lowercase. That is an issue worth
filing against the receipt increment; none owns it today.

**No verbatim normative text here.** Under FX-1 that belongs in
`distilled/normative.md` with its locator; in a summary the rule is to cite the
§ and let the reader open the source, so the fragments quoted above are short
and locator-bearing by design.

**No `state-machine` would be owed even then.** A countersignature has no
lifecycle: §3.3's only ordering constraint is that "The target structure of the
countersignature needs to have all of its cryptographic functions finalized
before computing the signature", which is a precondition on one operation, not
a state.

## Limits

1. **The two lists of permitted targets disagree, in both directions, and the
   document's only signed-message example follows neither cleanly.** §2 says
   label 11 "can occur as an unprotected attribute in any of the following
   structures that are defined in [RFC9052]: COSE_Sign1, COSE_Signature,
   COSE_Encrypt, COSE_recipient, COSE_Encrypt0, COSE_Mac, and COSE_Mac0" —
   seven, with **`COSE_Sign` absent**. §3.3 says the process "takes in the
   countersignature target structure (COSE_Signature, COSE_Sign1, COSE_Sign,
   COSE_Mac, COSE_Mac0, COSE_Encrypt, or COSE_Encrypt0)" — also seven, but it
   **adds `COSE_Sign` and drops `COSE_recipient`**. Appendix A.1.1 is a
   `98(…)`, a tagged `COSE_Sign`, carrying label 11 in the **body's**
   unprotected map — permitted by §3.3, not permitted by §2 — and §3 never
   assigns a countersignature semantics to `COSE_Sign` at all (it covers
   Signature/Sign1, Mac/Mac0 and Encrypt/Encrypt0 and stops). Not in the
   errata.
2. **§1 and §3 contradict each other on `COSE_Signature` coverage** (above),
   and §3.3's arithmetic settles it against §3. This is the document's own
   subject matter.
3. **Erratum 7338 (status *Reported*, checked 2026-10-20): §3.3's CDDL
   `context` choice ends `"CounterSignature0V2" /,` — a trailing `/` before the
   comma, so the fragment does not parse.** In a document that tells the reader
   (§1.2) the CDDL "can be extracted from the XML version of this document via
   the XPath expression below" and that `Internal_Types` exists "for dealing
   with the automated validation tools used during the writing of this
   document". The tools did not reach the one fragment that defines the domain
   separator.
4. **Detached payloads are unhandled, and the ambiguity lands on the exact
   defect this document fixes.** RFC 9052 has `payload : bstr / nil`. With a
   detached payload a `COSE_Sign1` carries `nil` on the wire, so §3.3's "only
   two bstr fields in the target structure" is true by wire item and false by
   type slot. On the first reading `other_fields` is omitted and the signature
   binding — the whole repair — silently disappears for every detached-payload
   message. Nothing in the document chooses, and detached payloads are ordinary
   COSE practice.
5. **No timestamp, acknowledged.** §3 offers the notary analogy and then
   withdraws its essential element: "A notary typically includes a timestamp to
   indicate when notarization occurs; however, such a timestamp has not yet
   been defined for COSE." A countersignature therefore attests existence
   without time, which is most of what a witness is wanted for.
6. **Countersigning a MAC or an encryption is capped by the tag it covers.**
   §6: a countersignature of a `COSE_Mac` with AES-MAC gives "at most 64 bits
   of integrity protection", and of a `COSE_Encrypt` with AES-CCM-16-64-128
   "at most 32 bits" — so the countersignature's own algorithm strength is
   irrelevant above that ceiling. §6 also notes that with more than two parties
   sharing a MAC key "data origin authentication is not provided" at all.
7. **The abbreviated form is unusable by a third party, by construction.**
   `COSE_Countersignature0 = bstr` and §3 says it "only contains the signature
   value and nothing else"; §3.2 states that the verification parameters "are
   provided by the same context used to describe the encryption, signature, or
   MAC processing". A witness is by definition not in that context, so label 12
   cannot carry one. §3 also warns the two forms are not interconvertible,
   because the `context` string differs.
8. **Appendix A is diagnostic notation, not bytes** — the same limitation
   `rfc-9052`'s extraction records for its Appendix C. Byte *sizes* are given
   but no octets, and the ECDSA examples (A.1.1, A.2.1, A.3.1) are randomised,
   so they can be verified and not reproduced. The EdDSA ones (A.4.1, A.5.1,
   A.6.1) are the reproducible fixtures.
9. **Signature schemes with message recovery are excluded** (§3.1: only
   algorithms "with appendix", "because the body should be able to be processed
   without having to evaluate the countersignature"). A real constraint on
   `DEC-005`'s algorithm list, stated once, in a sentence that reads like an
   aside.

## Where it cuts against MD-3

**It cuts, on the literal clause, and the cut is shallow but names a real
cost.** MD-3 narrowed `DEC-002` to **option 5: reduced CBOR, no IANA tags, COSE
export only**, and §5.1 registers **CBOR tag 19** for `COSE_Countersignature` —
the only new CBOR tag anywhere in this lane, against the one exclusion option 5
spells out.

The document itself supplies the escape, and it matters that it does: §3.1 says
"The full countersignature structure can be encoded as either tagged or
untagged, depending on the context", and the *header-parameter* form at label 11
or 12 is untagged. Tag 19's registered semantics are "COSE standalone V2
countersignature" (§5.1) — it exists only for a countersignature **detached**
from what it countersigns. So option 5 can carry countersignatures at full
fidelity and never emit a tag.

**What option 5 cannot carry is a detached one**, and that is the cost to name:
a transparency receipt or a witness statement that must be stored, cited or
served *separately* from the statement it covers has exactly one sanctioned way
to identify itself out of context, and option 5 forbids it. The alternative is
our own framing, which `R-O-03` then obliges us to cite, and there is nothing
to cite. **Name it against option 5 explicitly: the receipt either lives inside
the message it witnesses, or it is an invention.** `rfc-9052`'s design notes
reached the same tag-19 fact from the other direction and left the consequence
open; this is the consequence.

Two smaller observations for the same section. First, §4's determinism
obligation is **inherited and partial**, not chosen: it requires RFC 9052 §9's
narrowing of RFC 8949 §4.2, which `rfc-9052`'s extraction found applies only to
the to-be-signed structures and not to the transmitted message — so an option 5
profile gets byte-stable `ToBeSigned` and byte-unstable messages, from this
document as from its parent. Second, the countersignature is **unprotected** by
§2, which `rfc-9052`'s design notes record as the single exception to our
"everything we emit is protected" adaptation; so adopting it is also a
deliberate exception to a rule we have already written down, and should be
recorded as one rather than discovered later.

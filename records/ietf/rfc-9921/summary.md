---
schema: "library-summary/v1"
id: rfc-9921
record: rfc-9921
type: summary
updated: "2026-10-20"
---

# CBOR Object Signing and Encryption (COSE) Header Parameter for Timestamp Tokens as Defined in RFC 3161

|  |  |
|---|---|
| **Type** | rfc (IETF, Standards Track) |
| **Maturity** | `standard` — "This is an Internet Standards Track document", IESG-approved. **Not an STD**; it builds on STD 96 (RFC 9052) |
| **Authors** | H. Birkholz (Fraunhofer SIT), T. Fossati (Linaro), M. Riechert (Microsoft) |
| **Published** | 2026-02 |
| **Identifier** | RFC 9921 · DOI 10.17487/RFC9921 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9921.txt |
| **Digest** | `sha256:ba1c4dbb…` — full value in `record.yaml`, recomputed from `.cache/rfc-9921.txt` and re-verified 2026-10-20 |

## Overview

Two COSE header parameters, each carrying an RFC 3161 TimeStampToken, and the
document's real content is the distinction between them. §2.1's "COSE, Then
Timestamp" digests the finished COSE signature and puts the TSA's token back
into the **unprotected** header (`3161-ctt`, label 270): evidence that the
*signature* existed at a time. §2.2's "Timestamp, Then COSE" digests the datum
first and puts the token into the **protected** header (`3161-ttc`, label 269),
so the signature covers it: evidence that the *payload* existed at a time, and
nothing about the signature. §5.1 is emphatic that confusing the two is a
vulnerability — "incorrectly accepting signatures created after key revocation
based on older payload-only timestamps" — and that "each mode has its own
separate verification algorithm".

In both modes the token is "a DER-encoded TST [RFC3161] wrapped in a CBOR byte
string (Major type 2)" (§3.1, §3.2), §6 registers both labels with Value Type
`bstr` and **no value registry**, and §4 makes the COSE receiver's own
obligation to look inside: "the receiver MUST make sure that the MessageImprint
in the embedded timestamp token matches a hash of either the payload,
signature, or signature fields", with CMS [RFC5652] named as where that
verification is defined. Appendix A.1 measures what that means: **5453 octets**
of ASN.1 DER, carrying a two-certificate X.509 chain, inside one
protected-header parameter, against a 20-octet payload.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | **`core`** | §5 and §5.1 are the substance: an unprotected-header timestamp an attacker can strip, and two modes whose confusion §5.1 names as a revocation bypass |
| Cryptography | `none` | Invents nothing. Every primitive and every verification rule is RFC 3161's, RFC 5652's or RFC 9052's |
| This project | **`adjacent`** | We may never want third-party time. The measurement is decision-bearing now: this is what one COSE header parameter costs a reduced-CBOR profile |

`bears_on` reads as follows; the full warrant for each, with the quoted text,
is the comment block above `bears_on` in `record.yaml`.

- **DEC-002** — the hardest finding, and it is a cost MD-3's premise does not
  price. **A reduced-CBOR profile reduces the CBOR; it does not reduce what is
  inside a byte string.** The canonical encoding stops at the bstr boundary,
  §6 declines a value registry so nothing CBOR-side constrains the contents,
  and §4 obliges a CBOR verifier to acquire an ASN.1/CMS/X.509 stack and a
  clock. Option 5 separately forbids "native use of COSE header parameters", so
  the capability is unreachable natively and reachable only on export. Recorded
  with equal weight, the half that cuts the other way: §3.1.1 computes the CTT
  MessageImprint over "the bstr-wrapped signature… (including the heading bytes
  0x5840)", so the CBOR *head* of the `signature` field sits in a third party's
  digest preimage while the COSE signature does not cover it — an argument for
  requiring RFC 8949 §4.2.1 determinism on the **export** path, not only
  natively.
- **R-M-12** — the cleanest available demonstration that making the *label*
  key-relative buys nothing when the *value* is a foreign format. The whole
  capability is two centrally allocated labels (§6), and the 5453 octets they
  carry are registry-rooted end to end: OIDs, X.509 names, CMS content types.
  Relabel it `(our key, "rfc3161-timestamp")` and every identifier inside the
  value is still allocated by someone else.
- **R-O-05** — one adopt and one hazard. *Adopt:* §3.2's TTC imprint is "the
  hash of the payload… This does not include the bstr wrapping -- only the
  payload bytes", while §3.1's CTT imprint deliberately does include the
  wrapper; two digests in one document, two answers to "does the wrapper
  count", each written down — and §4 has the verifier hash the bytes as
  received rather than re-serialise. *Hazard:* the only discriminator between
  the two verification algorithms is which header label carries the token, and
  one of those labels is in the unprotected bucket. An unauthenticated type
  indicator selecting a verification algorithm is the shape R-O-05 exists to
  forbid.

**Not claimed, deliberately: DEC-005.** RFC 9921 is COSE-only by construction
(§3.1/§3.2 define the imprint over the CBOR-encoded `signature`/`signatures`
field or the payload of a *COSE* Signed Message), so time attestation is
available to one DEC-005 option and not the other — the same asymmetry as
`rfc-9964`'s Cut D. Establishing it needs the DSSE record as well as this one,
so it is left to the extraction rather than asserted from this document alone.

## Implementations

**Searched 2026-10-20: none found.** No library, SDK or reference
implementation of either header parameter surfaced, which is unsurprising eight
months after publication but is recorded as a result rather than an omission.

| Name | Kind | License | URL |
|---|---|---|---|

Two notes stand in for the empty table:

- **The document ships no reference code.** Unlike RFC 8778, whose Appendix A
  names its generator, Appendix A here gives bytes with no pointer to the
  tooling that produced them.
- **The example token is from a public demo TSA.** Decoding the ASCII inside
  the Appendix A DER gives `Free TSA` and `www.freetsa.org`, with a
  `freetsa.org` CPS URL and a CRL distribution point. Worth knowing before
  anyone treats the Appendix A bytes as a conformance fixture: it is one
  volunteer TSA's certificate chain, and it expires.

## Artifacts in this record

**FX-1 pass 1 (extract) landed 2026-10-20; passes 2 (verify) and 3
(cross-check) landed 2026-10-21.** `record.yaml` declares `standard: FX-1`, the
artifact set is complete, and no `reviewed_by` is signed — that is pass 4, a
person, which `docs/extraction.md` lists separately from the profile.
Pass 2 fixed nine defects — two dropped statements, four leaked generator
templates, three relaxed quotations, a quotation attributed to the wrong
section, a wrong line range and four stale or mis-split counts.
**Pass 3 closed the four cross-check closures** — every field a requirement
names exists (68 requirements name a wire artefact, 0 undefined), every one of
20 protocol steps and 23 state-machine triggers resolves, and every example
validates against the production covering it. It also fixed defects in six
classes, each listed with its file and line in `record.yaml`: a **leaked
brace-escaped template** in `messages.yaml`'s two CBOR diagnostic renderings —
the same class pass 2 found in `design-notes.md`, and again invisible to a
quotation audit because the text inside it was right; **two octet
decompositions that did not sum**, in `messages.yaml` and
`timestamp-token.derived.outline.txt`; **`98.09 %` written against the wrong
numerator** (it is 5453/5559, not the 5456-octet header field, which is
98.15 %); **three cross-references pointing at the wrong section**, two of them
transposed with each other; an **undelimited near-quotation of `CLAUDE.md`**
that had swapped the referent of the sentence it leaned on; and **four stale
counts**, including a citation total that was already stale in the commit that
recorded it. All measurements are in `record.yaml`'s `distillation.passes`.
Per-artifact coverage lines are in `record.yaml`; `distilled/README.md` indexes
them.

| File | What it is |
|---|---|
| `record.yaml` | metadata, the locator-by-locator warrant for each `bears_on` id, and the `distillation` block |
| `summary.md` | this document |
| `distilled/normative.md` | 29 verbatim regions, each with its source line range and its own sha256; 27 carry a printed block and 2 are declared with a digest only (the two final Appendix A objects, 166 and 173 lines). Measured coverage: 0 statement-bearing lines of §1–Appendix A.2 uncovered |
| `distilled/requirements.yaml` | **111** entries, 11 stated and 100 inferred (R-0110 and R-0111 added by pass 2 as dropped statements, placed in source order); `source_keyword_count` and `extracted_keyword_count` both **8** and agreeing; 111/111 texts verbatim with **0 relaxations**, and 111/111 `source_lines` re-measured exact |
| `distilled/schema/` | 1 verbatim capture of the document's twelve printed renderings (1 IANA table, 6 ASN.1 value dumps, 3 CBOR diagnostic objects, 2 byte listings), plus 4 derived files — RFC 9921 ships **no** CDDL, ABNF, ASN.1 or JSON Schema |
| `distilled/messages.yaml` | 13 structures, 48 fields, every layout produced by **decoding** the appendix bytes and re-decoded by pass 3 with an independent parser; 24 fields carry an empty `constrained_by`, enumerated exhaustively as 7 RFC 9052, 5 RFC 5652 and 12 RFC 3161 |
| `distilled/protocol.{yaml,md}` | **applicable**: 4 roles, 4 flows, 20 steps, a Mermaid diagram per flow |
| `distilled/state-machine.yaml` | **applicable**: 5 machines, 28 states, 23 transitions, 10 `error_states` entries of which 8 are named error states and 2 are `(none defined)` markers |
| `distilled/examples/` | 15 vectors and the two 5453-octet tokens as `.hex` fixtures |
| `distilled/design-notes.md` | DEC-002 both ways, R-M-12 from the value side, R-O-05's adopt and hazard, the six `canonical-encoding` conditions, MD-3 mapped and then five cuts against it, 11 source defects, 8 open questions |

### What the extraction changed about this summary's own claims

**Nothing above was falsified; two things were overtaken and three were
sharpened.**

- **Overtaken: "No `distilled/`, deliberately."** That paragraph stood here
  until 2026-10-20 and is now wrong — the extraction ran. Its *warning* was
  right about the reason, though: `normative.md` did have to decide how much of
  RFC 3161 and RFC 5652 counts as in scope, and the answer is recorded as a
  **boundary** in `protocol.yaml` and `state-machine.yaml` (every TSA-side step
  and every CMS validation step is marked as crossing into a document this
  library does not hold) rather than as content.
- **Overtaken: Appendix A as a fixture.** This summary said the example token
  was from a public demo TSA "and it expires". It **has expired**: the signing
  certificate's `notAfter` is **2026-03-11 01:57:39Z**, one month after this
  RFC published. `examples/README.md` says which tests the bytes are still good
  for (parsing and digest agreement) and which they are not (path validation,
  acceptance).
- **Sharpened: the 5453 octets.** Re-measured from the bytes: **75.26 %** of
  the token is a two-certificate X.509 chain and **6.73 %** is the timestamp
  assertion; the token is **98.09 %** of the whole 5559-octet tagged
  `COSE_Sign1`, a ratio of **272.65 : 1** against the payload.
- **Sharpened: §3.1.1's imprint over the head bytes.** Now **proved**, not
  read: `sha256(0x58 0x40 ‖ signature)` reproduces the printed MessageImprint
  byte for byte. And §3.1.2 is worse than this summary said — the `COSE_Sign`
  preimage is the whole `signatures` array, 77 octets for a 64-octet signature,
  **5 of them the per-signature *unprotected* header map**.
- **Sharpened: "each mode has its own separate verification algorithm."**
  Confirmed verbatim, and **neither algorithm is written down anywhere in the
  document**: §4 is one sentence covering both modes.

**New, and not in this summary before:** **Appendix A.2's MessageImprint does
not reproduce.** The document's rule, its own §3.1.1 worked example and A.2
disagree three ways and the disagreement resolves against A.2 — 207 candidate
preimages assembled from the document's printed bytes produce none of the
printed value. RFC Errata **9177** (status *Reported*, filed 2026-09-13) says
the same — **that errata record is not verifiable from this repository** and is
flagged as second-hand in `examples/vectors.yaml`; the mismatch itself needs no
network. See `distilled/design-notes.md` D-1 and `examples/` `V-0011`.

## Limits

- **Protection and evidence are inverted. The document requires the inversion
  and never remarks on it.** The mode that proves something about the
  *signature* (`3161-ctt`, 270) lives in the bucket nothing signs; the mode in
  the protected bucket (`3161-ttc`, 269) proves only that the payload existed.
  **Four MUSTs close the matrix**: §3.1 makes the signature-covering parameter
  the *unprotected* one and binds its imprint to the `signature`/`signatures`
  field, and §3.2 makes the *protected* parameter's imprint the payload hash —
  so no RFC 9921 parameter can carry signature-time evidence inside the signed
  bytes, and a second signature pass does not open one. §5 concedes the
  consequence — "an attacker could manipulate the unprotected header by
  removing or replacing the timestamp" — and answers with "the COSE Signed
  Message should be integrity protected during transit and at rest": lowercase,
  and at a layer this document does not define. The stronger evidence is the
  more fragile carrier, and that is normative rather than accidental:
  `distilled/design-notes.md` §9 separates the document's own normative leg
  from this library's mechanical one.
- **No value registry and no CDDL.** §6 gives both parameters Value Type `bstr`
  and Value Registry "-", and the document contains no CDDL at all. There is
  nothing a CBOR validator can check about those 5453 octets, by design.
- **Nothing about deterministic encoding.** §3.1.1's imprint includes the
  `0x5840` head bytes and the document never requires RFC 8949 §4.2.1, so a
  CTT timestamp is bound to one serialisation that COSE itself does not pin.
  Re-encode the object and the COSE signature still verifies while the
  timestamp no longer matches.
- **TSA trust distribution is out of scope.** §4 defers verification to RFC
  5652 and RFC 3161; §5 simply assumes "the TSA is a trusted third party" and
  says nothing about how a verifier comes to trust one, or what happens when a
  TSA certificate expires — which, for "long-term signatures" (§1.1), is the
  whole problem recursing one level up.
- **Privacy in TTC mode is deferred to a mechanism that does not exist here.**
  §5: the TSA receives "an opaque identifier (a cryptographic hash value) for
  the payload", and preventing comparison against known payloads "would need"
  armoring with a shared nonce — "Such a mechanism is out of scope for this
  document."
- **§1.1's second use case is SCITT's, in SCITT's words, with no citation.**
  "Transparency service", "statements", "append-only log", "transparent
  statement" — and zero occurrences of "SCITT" or "9943". The edge to
  [`rfc-9943`] is made from this library because the document does not make it;
  see `relations` in `record.yaml`.

---
record: rfc-9921
kind: design-notes
title: "rfc-9921 — bearing on our design"
extracted: "2026-10-20"
reviewed_by: ""
---

# RFC 9921 — bearing on our design

Voice markers, as `rfc-8949` and `rfc-9964` use them: **unmarked** is the
source or our own decisions as cited; **[analysis]** is this extraction's
reasoning; **[correction]** is a project assumption the source does not
support.

## 0. Provenance — what is checkable from this repository and what is not

**Every quotation of RFC 9921 in this file was cut from `.cache/rfc-9921.txt`
by script**, located by anchor in the whitespace-normalised source and verified
as a contiguous substring of it before this file was written. The audit retries
any non-resolving fragment under terminal-punctuation swap, hyphenation heal,
line-break heal and case fold, so that class of defect is reported rather than
silently healed. **Result: 0 relaxations needed.**

**[correction] The `mofn` documents this file reasons about are not in this
repository.** This library is **standalone by design** — independently
cloneable, forkable and citable by projects that are not `mofn` (`CLAUDE.md`).
A `find` over the worktree returns none of `ARCH-0001`,
`ARCH-0001-PROPOSAL-v0.2.0`, `ARCH-0002`, `ADR-0001`, `DECISIONS-0001`, `MD-3`,
or the `DEC-00n` / `R-M-*` / `R-O-*` / `R-I-*` rules. **Every quotation of
those documents below is reproduced from the extracting agent's context and
cannot be verified here.** Treat each as a citation to re-check against `mofn`
before relying on it, including the three identifiers `record.yaml` names in
`bears_on` (`DEC-002`, `R-M-12`, `R-O-05`). Nothing in this record's
*findings* rests on them: every finding is measured against the source, and the
`mofn` ids say only which of our decisions a measured finding bears on. The
convention is `records/ietf/rfc-9741`'s, adopted 2026-10-20 and carried by
`rfc-9964`.

**What IS checkable here, and was checked.** `topics/canonical-encoding.yaml`
is in this worktree and is the source for the six conditions scored in §6 and
for the identification of `DEC-002` options 1 and 3.
`records/ietf/rfc-9052/distilled/schema/cose.cddl` is here and is where
`header_map`, `empty_or_serialized_map`, `label` and `values` are defined.
`records/ietf/rfc-9360` is here at `profile: full` and is where the first
instance of this record's central cut was established (§2).
`records/ietf/rfc-9943` is here and is what §1.1's second use case is written
about without citing (§9). **`RFC 3161` and `RFC 5652` are NOT here**, and that
is the first thing this extraction has to report: they are two of the
document's six normative references and they are where everything the
timestamp token *means* is defined.

**What this extraction added beyond the summary, mechanically.** Four digests
tested and three reproduced byte for byte; one that does not, with a
207-candidate preimage sweep behind the claim; two CMS internal consistency
checks per token, both passing; the octet budget of both appendix objects; a
map-order census; and the expiry date of the fixture's own TSA certificate. A
CBOR codec and a DER parser were written for this pass over `hashlib` alone —
no CBOR, COSE, ASN.1, CMS, X.509 or cryptography library was used. Details in
`examples/vectors.yaml`.

---

## 1. What this record decides, in one paragraph

**A COSE header parameter is not a bounded cost, and this is the document that
measures how unbounded it can get.** Appendix A.1 puts **5453 octets** of
ASN.1 DER — including a **two-certificate X.509 chain** — into **one**
protected header parameter, against a **20-octet** payload: 272.65 to 1, and
**98.09 per cent** of the whole tagged `COSE_Sign1`. §6 registers both labels
with Value Type `bstr` and **Value Registry `-`**, the document contains **no
CDDL at all**, and §4 makes the COSE receiver's own obligation to look inside.
**[analysis]** For `DEC-002` the honest reading is that this cost is *evaded*
rather than *violated* by every option equally (§2), so the decision it forces
belongs to scope rather than to encoding. What it *does* decide for us is
narrower and sharper: **if we ever carry third-party time, the two legs of
this document point in opposite directions on the one question our envelope
has to answer** — whether a digest covers the wrapper — and one of them puts a
CBOR head inside a stranger's signature (§3).

---
## 2. `DEC-002` — the DER-in-a-header cut, measured, and why it is a scope argument

**The mechanism, verbatim.** §3.1 and §3.2 say the same thing with one word
changed:

> The 3161-ctt unprotected header parameter contains a DER-encoded TST [RFC3161] wrapped in a CBOR byte string (Major type 2).

> The 3161-ttc protected header parameter contains a DER-encoded TST [RFC3161] wrapped in a CBOR byte string (Major type 2).

**And nothing CBOR-side constrains what is inside.** §6's Table 1 gives both
parameters Value Type `bstr` and **Value Registry `-`** (reassembled from the
column-wrapped rows; the verbatim table is in
`schema/source-renderings.txt`). Measured over all 1056 lines of the source:
`CDDL` **0**, `ABNF` **0**, `ASN.1` **0**, `JSON Schema` **0**, `schema`
**0**, `grammar` **0**.

**The measurement.** From decoding Appendix A.1's hex — not from the prose,
whose own ASN.1 dump the document truncates with `[...]` at source line 592:

| | octets |
|---|---|
| the DER TimeStampToken | **5453** |
| of which X.509 certificates (two) | **4104** (75.26 %) |
| of which the TSTInfo assertion | **367** (6.73 %) |
| the `bstr` head that carries it | 3 (`59 154d`) |
| the whole protected header field | 5465 |
| the payload field | 21 (20 content octets) |
| the whole tagged `COSE_Sign1` | **5559** |
| the token's share of the object | **98.09 %** |
| token : payload | **272.65 : 1** |

**Who parses it: the COSE receiver, normatively.** §4:

> As part of the signature verification, the receiver MUST make sure that the MessageImprint in the embedded timestamp token matches a hash of either the payload, signature, or signature fields, depending on the mode of use and type of COSE structure.

and the verification it is part of is somebody else's:

> Timestamp tokens [RFC3161] use Cryptographic Message Syntax (CMS) as the signature envelope format. [RFC5652] provides details about signature verification, and [RFC3161] provides details specific to timestamp token validation.

**[analysis]** So a CBOR verifier that supports this parameter acquires an
ASN.1/DER parser, a CMS implementation, an X.509 path validator, a revocation
story and **a clock** — none of which it needed for COSE. And the cut
*compounds*: `records/ietf/rfc-9360` established the same cut for one
certificate in `x5chain`; RFC 9921 carries **a CMS message that itself carries
a certificate chain**, so adopting it acquires everything `x5chain` acquires
*plus* CMS *plus* time.

**[correction] Do not score this as `DEC-002` option 5 losing to another
option.** `records/ietf/rfc-9360/distilled/design-notes.md` §7.2 settled this
and the reasoning transfers unchanged: *"Every `DEC-002` option pays this cost
identically — option 1 (canonical S-expressions) would carry the same DER
inside the same opaque octet string, and so would option 3 inside a base64
JSON string."* The same is true here, and this record adds the mechanical
confirmation on the CBOR side: **not even CDDL's `.cbor` control operator
could reach this payload, because the payload is not CBOR.** A reduced-CBOR
profile reduces the CBOR; **it does not reach inside a byte string**. The
decision this forces is *"do we carry third-party time at all"*, which is a
**scope** question and belongs with `DEC-003`'s family of
what-do-we-carry decisions rather than with `DEC-002`'s choice of encoding.

**What IS option-5-specific, and it is a clean finding.** Option 5 as drafted
says — CBOR as the canonical encoding, using the CBOR data model and deterministic encoding rules, but with no reliance on the IANA CBOR Tags registry and no native use of COSE header parameters — so **this mechanism is
unreachable natively by construction.** It is a COSE header parameter and
nothing else: there is no payload form, no claim, no tag. Under option 5 RFC
9921 is **export-only or nothing**, and the export is where option 5 says the
mapping is a lossy interchange step.
**[analysis]** That is not a cost option 5 pays over the others — it is a
*capability* option 5 declines natively and can only rent on export. The
question to put to the `DEC-002` ADR is therefore not *"can we afford 5453
octets"* but *"is a capability that exists only on the export path a
capability we have at all"*, and §3 below is the reason the answer is not
obviously yes.

---
## 3. `DEC-002`, cutting the other way — a CBOR head inside a third party's digest

**This is the leg that discriminates between options, and it is an argument
for determinism on the EXPORT path.** §3.1.1 says what the CTT MessageImprint
is computed over. The sentence is interrupted **twice** — by the CBOR
diagnostic object and then by the byte listing — so it has three fragments, and
the two that carry the rule are quoted here with the elision visible,
**adjacent in the source and not welded** (its opening fragment, *Given the
COSE_Sign1 message*, is `R-0110`):

> the bstr-wrapped signature … (including the heading bytes 0x5840) is used as input for computing the MessageImprint.

**Verified in this pass.** `sha256(0x58 0x40 || the 64-octet signature)` =
`44c2419d131d53d55584b5dd33b788c24e551c6d44b1afc8b2b85e6954763b4e`, which is
§3.1.1's printed MessageImprint **byte for byte**. `sha256` of the bare 64
octets is `14da2538…`, which appears nowhere in the document. So the claim is
not an inference: **the CBOR head is in the preimage and the document's own
worked example proves it.**

**And §3.1.2 is worse, which the document does not say.** For `COSE_Sign` the
preimage is the whole `signatures` array — 77 octets for a 64-octet signature,
of which **13 are not the signature** and **5 are the per-signature
`unprotected` map** carrying `kid`. `sha256` of those 77 octets reproduces
§3.1.2's printed imprint exactly. A COSE signature is computed over a
`Sig_structure` built from the protected bucket, `external_aad` and the payload
(RFC 9052 §4.4, `records/ietf/rfc-9052`), so **neither the `signature` field's
own head nor the per-signature unprotected bucket is covered by it**.

**[analysis] The consequence, stated as a test a harness can run.** Re-encode
the object writing the 64-octet byte string head as `59 0040` instead of
`58 40` — legal CBOR, forbidden only by RFC 8949 §4.2.1, which RFC 9921 never
invokes (`canonical` and `deterministic` each occur **zero** times). **The COSE
signature still verifies and the TSA's timestamp no longer matches.** Change
`kid` from `'11'` to `'12'` in a `COSE_Sign` and the same thing happens. The
timestamp has been bound to **one serialisation that the envelope itself leaves
free**.

**Measured, and it is not hypothetical.** The document prints exactly two maps
with more than one key. A.1's protected map is `01` then `19010d` — in RFC 8949
§4.2.1 order. **A.2's unprotected map is printed `270` then `4`, which is not**:
§4.2.1 sorts on the encoded key bytes and `04` precedes `19010e`. So **one of
the document's two multi-key maps is already non-deterministic**, in the mode
whose digest is head-sensitive.

**[analysis] Where this lands for us.** Our export path is exactly where a
re-encode happens: a native statement is mapped to a `COSE_Sign1`, and option 5
calls that mapping lossy. If a CTT timestamp is acquired on the exported bytes,
then **any later re-export must reproduce those bytes exactly or the third
party's attestation is destroyed** — not invalidated loudly, but silently, with
the COSE signature still verifying. **That is an argument for requiring RFC 8949
§4.2.1 determinism on the export path and not only natively**, and it is a
requirement option 5 as drafted does not state: its determinism clause is about
the native canonical encoding. **Options 1, 3 and 4 are not better off here** —
a canonical S-expression export or a JCS export would each have the same
property that a third-party digest over the *encoded* signature field is
encoding-sensitive — so this is not an argument between options either. It is a
**missing clause** in whichever option wins.

**The TTC leg is the clean one.** §3.2:

> The MessageImprint sent to the TSA (Section 2.4 of [RFC3161]) MUST be the hash of the payload of the COSE Signed Message. This does not include the bstr wrapping -- only the payload bytes.

Verified: `sha256('This is the content.')` =
`09e638d4aa95fd7271866203595303bce232f462a94d38e393773cd3aae3f6b0`, which is
both A.1's printed request imprint **and** the imprint embedded in the TSTInfo
of the token A.1 prints. **Payload content octets do not move when an envelope
is re-encoded, so the TTC preimage is encoding-stable and the CTT preimage is
not.** If we ever adopt one mode, adopt that one — and §5 below is why that
recommendation is uncomfortable.

---
## 4. `R-M-12` — the cleanest demonstration that a key-relative *label* buys nothing

**What we require** (R-M-12 and ADR-0001: native extension points "SHALL be identified relative to a defining principal" and the native model "SHALL NOT depend on a centrally allocated registry for their meaning"),
and `ARCH-0002 P1` sharper still: private-use ranges give escape from a registry, not a namespace, because nothing in the encoding can disambiguate them because no principal is attached.

**The ledger here is two allocations and zero tags.** §6 allocates `3161-ttc`
= **269** and `3161-ctt` = **270** in the *COSE Header Parameters* registry,
and that is the document's entire IANA footprint: measured, `tag` occurs
**zero** times in the source. So option 5's literal *no IANA tags* clause
survives untouched — and the profile acquires an ASN.1 identifier tree.

**[analysis] The point this record makes that no other record in this library
makes as well: relabelling the parameter changes nothing, because the VALUE is
registry-rooted end to end.** Measured from the Appendix A.1 token, which
carries **25 distinct OIDs**:

- `1.2.840.113549.1.7.2` (`id-signedData`), `1.2.840.113549.1.9.16.1.4`
  (`id-ct-TSTInfo`) — RSA Laboratories' arc under ISO/ITU-T;
- `2.16.840.1.101.3.4.2.1` and `…2.3` (SHA-256, SHA-512) — NIST's arc;
- `2.5.4.3`, `2.5.4.6`, `2.5.4.7`, `2.5.4.8`, `2.5.4.10`, `2.5.4.11`,
  `2.5.4.13` (X.520 attribute types), `2.5.29.14`/`15`/`19`/`31`/`32`/`35`/`37`
  (X.509 extensions) — ITU-T's;
- `1.3.6.1.5.5.7.1.1` (`id-ad-ocsp`'s parent, authorityInfoAccess) — IANA's
  enterprise arc;
- and `1.2.3.4.1`, the TSAPolicyId, **which is a placeholder in the ITU-T
  example arc** rather than a real policy.

Rename the label to `(our key, "rfc3161-timestamp")` as `R-M-12` would have
us do and **every one of those 25 identifiers is still allocated by someone
else**, inside a byte string our schema cannot see into. The label is the
cheapest 3 octets in the structure; the governance is all in the other 5453.

**[analysis] So `R-M-12` needs a second clause, and this is the evidence for
it.** As written, `R-M-12` constrains *identification of extension points*. It
says nothing about **what an extension point may carry**, and this record is
the proof that the two are separable: a perfectly key-relative label can carry
a value whose every component name is centrally allocated. `ARCH-0001`'s
*escape from a registry, not a namespace* was arrived at from the **label**
side; this is the same conclusion from the **value** side, and it suggests the
rule we actually want is about the *closure* of identifiers reachable from a
statement, not about the top-level label.

---
## 5. `R-O-05` — one adopt and one hazard, and the hazard is the sharper

**What we require, verbatim** (The signed payload SHALL be the canonical encoding verbatim, carried with an authenticated type indicator. A verifier SHALL verify the signature before decoding and SHALL NOT canonicalize input as part of verification. Any human-facing form SHALL be regenerated from verified canonical bytes.), as `records/ietf/rfc-8785` quotes it.

### 5.1 ADOPT — two digests, two written answers, and the verifier hashes what it received

§3.1 includes the wrapper in the CTT preimage and §3.2 excludes it from the
TTC one, **three paragraphs apart, each in writing**, and §4 then has the
receiver compare against the bytes in hand rather than re-serialising
anything: *matches a hash of either the payload, signature, or signature fields*.
**[analysis]** That is `R-O-05`'s second sentence satisfied, and it is worth
citing for two reasons. First, the *ordering*: nothing in the document asks a
verifier to canonicalise before checking. Second, and more useful to us, **the
wrapper question is settled per digest rather than once for the document.** We
have been treating *"does the wrapper count"* as a single global decision; RFC
9921 is a worked example of a format where the answer differs by **which
digest** you are computing, and where getting it wrong is undetectable until a
third party disagrees with you.

### 5.2 HAZARD — an unauthenticated type indicator selecting a verification algorithm

§5.1 asserts, and this is the hinge of the whole record:

> In particular, symmetric to the signature and assembly mechanics, each mode has its own separate verification algorithm.

**And the only discriminator between the two algorithms is which header label
carries the token.** There is no type field inside the value — §3's own
reasoning is *To clearly separate their semantics, two different COSE header parameters are defined as described in the following subsections.* —
and §5 concedes what that means for the CTT label:

> In CTT mode, an attacker could manipulate the unprotected header by removing or replacing the timestamp. To avoid that, the COSE Signed Message should be integrity protected during transit and at rest.

**Lower case, and at a layer the document does not define.** Under §1.2's
*when, and only when, they appear in all capitals* that sentence binds nobody,
and it pushes the integrity of a *signed message* outside the signed message.

**[analysis]** So RFC 9921 is a ratified, Standards Track instance of exactly
the shape `R-O-05` exists to forbid: **a type indicator that selects a
verification algorithm and is not inside the signed bytes.** The document names
the consequence itself —
*such as incorrectly accepting signatures created after key revocation based on older payload-only timestamps* —
and the state machine makes the undetectability explicit: strip label 270 and
the object verifies as an untimestamped `COSE_Sign1`, because **no state
anywhere records that a timestamp was expected** (`state-machine.yaml`, M3
`timestamp-stripped`).

**A third leg `R-O-05` cares about and the summary did not name.** §4 puts the
imprint check *As part of the signature verification*. In CTT mode the
token is in the unprotected bucket, so a receiver that follows the document
**runs an ASN.1/CMS/X.509 parser over 5453 unauthenticated octets before it has
a signature verification result.** `R-O-05`'s *verify the signature before
decoding* is not merely unmet — the ordering the document specifies is the
reverse, and the attack surface it exposes is the largest parser in the stack.

---
## 6. The `canonical-encoding` conditions, scored

`topics/canonical-encoding.yaml` is in this repository, so these six are quoted
from a file a reader can open.

| | condition | RFC 9921's answer |
|---|---|---|
| **(1)** | *"The encoding is INJECTIVE over the values it encodes, not merely deterministic"* | **Broken at the bstr boundary, and the document builds on the break.** The CTT preimage is the *encoded* `signature` field, so a value with two legal encodings has two timestamps; `58 40` is the only §4.2.1-legal head but §4.2.1 is never invoked. The TTC preimage is injective because it is content octets. |
| **(2)** | *"The decoder REJECTS non-canonical input rather than normalising it"* | **Absent, and unreachable.** `reject` occurs **0** times. The value is opaque, so a CBOR decoder has nothing to reject; DER is itself a canonicalisation with its own rules, and §4 delegates all of it to RFC 5652. |
| **(3)** | *"Canonicalisation runs once, at authoring, on trusted input, and never as part of verification"* | **Satisfied in letter, violated in spirit.** §4 hashes the bytes as received — no re-serialisation. But it runs a *DER* parse, on untrusted input, *as part of* verification, and DER parsing is canonical-form checking. |
| **(4)** | *"The encoding profile is named by an authenticated type indicator carried inside the signed bytes"* | **THE DIRECT ENGAGEMENT, and it is split down the middle.** The TTC indicator (label 269) **is** inside the signed bytes — §3.2 spends a MUST on it. The CTT indicator (label 270) is **not**, by the same kind of MUST. One document, one mechanism, both answers. |
| **(5)** | *"Set-valued fields carried in arrays have a defined canonical order"* | **Not engaged, with one wrinkle.** No set-valued field is defined. But `COSE_Sign`'s `signatures` array is in the CTT preimage, so **signer order becomes digest-relevant** in a structure RFC 9052 does not order. |
| **(6)** | *"Text that is load-bearing for identity has a declared Unicode normalisation rule"* | **Not engaged by RFC 9921 and smuggled in by its value.** No text field. Inside the token, X.509 `DirectoryName` RDNs are text with their own comparison rules (PrintableString, IA5String, UTF8String), and the TSA name is one: `www.freetsa.org`. |

**[analysis] The finding (4) yields is new and it is not what `MD-3` assumed.**
`topics/canonical-encoding.yaml` records that for CBOR the indicator *"has to
be CONSTRUCTED BY SUBTRACTION — a positive rule excluding major type 6,
rejection on decode, and a named untagged export profile"*. RFC 9921 shows a
**fourth** construction nobody costed: a **protected header label**. It is
authenticated, it is inside the signed bytes, and it is **centrally allocated**
— so it satisfies condition (4) and fails `R-M-12` in the same breath.
**Condition (4) and `R-M-12` are in tension and this document is the proof**:
the only indicator COSE offers that is *authenticated* is one the registry
owns, and the only indicator that is *key-relative* is one we have to put in
the payload, where it is no longer a header at all.

---
## 7. `MD-3` — the header-by-header mapping

`MD-3` (2026-09-28) narrowed `DEC-002` to **option 5**, which
`docs/extraction.md` — in this repository — states as reduced CBOR, no IANA tags, COSE as export only.
**A narrowing, not an acceptance**: `docs/extraction.md` says so in terms, and
no `DEC-002` ADR exists. Nothing below may be read as an accepted encoding
decision.

**What RFC 9921 would ride in, if we carried it at all.**

| our field (`ARCH-0001` §4.1) | RFC 9921 carrier | label | registry | option-5 verdict |
|---|---|---|---|---|
| "this statement was timestamped, and the timestamp covers the payload" | `3161-ttc`, protected | **269** | COSE Header Parameters | **export only** — option 5 forbids native COSE header parameters; nothing else in RFC 9921 can carry it |
| "this statement was timestamped, and the timestamp covers the signature" | `3161-ctt`, unprotected | **270** | COSE Header Parameters | **reject** — the carrier is a bucket nothing signs, and the indicator selects a verification algorithm (§5) |
| the timestamp value itself | `bstr` holding DER CMS | — | **none (`-`)** | **carry opaquely or not at all.** No reduced-CBOR rule reaches inside it; our CDDL cannot constrain it and `.cbor` cannot either |
| the imprint hash algorithm | inside the TSA's `MessageImprint` | — | ITU-T/NIST OID arcs | **inherit** — §4: *"The hash algorithm is contained in the MessageImprint structure, together with the hash itself."* It is **not** our `alg` and we do not choose it |
| the time value | `TSTInfo.genTime`, `GeneralizedTime` | — | RFC 3161's | **inherit as text.** A `GeneralizedTime` string, not a CBOR integer or a tag-1 epoch value |
| the TSA identity | `TSTInfo.tsa`, X.509 `DirectoryName` | — | X.520 attribute OIDs | **reject as a principal.** It is a directory name, not a key; our `KeyId` model cannot consume it |
| accuracy / precision of the time | `TSTInfo.accuracy` | — | RFC 3161's | **absent in both of the document's own tokens**, while §5 says it *"must be taken into account when implementing solutions based on the COSE header parameters defined in this document"* |
| replay protection for the request | `TimeStampReq.nonce` | — | RFC 3161's | **absent in both examples**, although both figures draw one |
| "these bytes are a COSE_Sign1" | COSE tag 18 | — | CBOR Tags | **drop**, as elsewhere in this lane; the appendix objects carry it and nothing depends on it |

**The export mapping, in one line.** A `COSE_Sign1` whose protected bucket
carries `alg`, our type indicator and — *if* third-party time is in scope at
all — label **269** only, with the payload a §4.2.1-deterministic encoding of
our statement, **no label 270 anywhere**, and the export path pinned to
reproduce the exported bytes exactly, because §3.1.1 has shown what a
re-encode costs when a third party has signed over a head.

**What we deliberately do not carry:** label 270 in any form; the TSA
`DirectoryName` as an identity; `GeneralizedTime` as our time type; and the
token's certificate chain as a trust input — `records/ietf/rfc-9360`'s record
already holds that argument and this document nests it.

---
## 8. Where the source cuts against `MD-3` — five cuts, each naming the option

**`docs/extraction.md`: an extraction that can only confirm is not evidence.**
Here is where this one disagrees.

### 8.1 Cut 1 — the capability is export-only under option 5, and that is a real loss. **Costs option 5; options 2 and 4 do not pay it.**

Option 5 forbids native use of COSE header parameters,
and RFC 9921 is **nothing but** a COSE header parameter: no claim, no tag, no
payload form, no media type. **[analysis]** So under option 5 third-party time
is available only to exported bytes — and the thing an exported byte string
most lacks is a **stable identity across re-exports**, which §3 has just shown
a CTT timestamp depends on. **Option 2** (CBOR with deterministic encoding and
native COSE) would carry label 269 natively; **option 4** (dual canonical CBOR
and JSON with a documented mapping) would too. This is the first cut in this
lane where option 5's *no native COSE headers* clause costs a capability rather
than a tag number, and it should be priced as one.

### 8.2 Cut 2 — option 5's determinism clause does not reach the export path. **Costs option 5 as drafted; the gap is a missing clause, not another option's win.**

**[analysis]** Option 5 names deterministic encoding for the native model and
calls the COSE export a lossy interchange step.
§3.1.1 shows that a third party can sign over the **encoding** of an exported
field, so *lossy* is the wrong frame: an export that is re-generated
differently does not lose information, it **destroys an external
attestation**, silently, while the signature still verifies. Measured: the
document's own A.2 object is already out of §4.2.1 map order. The clause option
5 needs is *the export encoding is deterministic and reproducible*, and no
`DEC-002` option currently states it.

### 8.3 Cut 3 — the one authenticated type indicator COSE offers is registry-owned. **Costs every option; it is `R-M-12` against condition (4).**

See §6. **[analysis]** `MD-3` assumes we can have both a key-relative identity
model and an authenticated encoding-profile indicator. RFC 9921 is a worked
example where you choose: label 269 is authenticated **because** it is a
registered protected header parameter. A key-relative indicator has to live in
the payload, and then it is not a header and cannot be read before decoding —
which is `R-O-05`'s own ordering problem arriving from the other side.

### 8.4 Cut 4 — the DER payload evades every option equally, so `DEC-002` is the wrong decision for it. **Costs no option; it is a scope question for `DEC-003`.**

See §2, and `records/ietf/rfc-9360/distilled/design-notes.md` §7.2 for the
first instance. **[analysis]** What this record adds is the *compounding*: the
payload here is a CMS message that itself carries a certificate chain, so the
scope question is not *"do we carry certificates"* but *"do we carry a second
envelope format that carries certificates"*. Stated in option 5's favour for
once: because option 5 is the option that most explicitly draws a boundary
around its own data model, it is also the option where this evasion is easiest
to **see** — a profile that says *no tags, no native headers* makes an opaque
foreign blob visibly exceptional, where options 2 and 4 absorb it without
comment.

### 8.5 Cut 5 — the mode that proves the useful thing is the one option 5 must reject. **Costs option 5 nothing extra, and costs the FEATURE.**

**[analysis]** §5.1 is explicit that only a CTT timestamp may be used for
signature validity timing:
*should rely exclusively on TSA timestamps [RFC3161] explicitly covering signature data for determining signature validity timing*.
But CTT is the unprotected mode, which §7's mapping rejects, and TTC proves
only that the payload existed. **So the mapping above can carry exactly the
half of RFC 9921 that does not answer the long-term-signature question §1.1
opens with.** That is not an argument between `DEC-002` options — it is the
document's own inversion (§10) reaching our design, and it means that if we
ever need signature-time evidence we need a mechanism this document does not
offer: a countersignature over the signature *inside* the signed bytes, which
is `records/ietf/rfc-9338`'s territory and which §2.1 gestures at —
*In this context, timestamp tokens are similar to a countersignature made by the TSA.*

---
## 9. The inversion itself, verified leg by leg

The summary states this as the record's sharpest finding. **Every leg checks
out, and one is sharper than stated.**

| leg | verdict |
|---|---|
| `3161-ctt` (270) is unprotected, and MUST be | **CONFIRMED.** §3.1: *The 3161-ctt COSE _unprotected_ header parameter MUST be used for the mode described in Section 2.1.* |
| `3161-ttc` (269) is protected, and MUST be | **CONFIRMED.** §3.2: *The 3161-ttc COSE _protected_ header parameter MUST be used for the mode described in Section 2.2.* |
| CTT covers the signature | **CONFIRMED**, §3.1 and §3.1.1, and reproduced |
| TTC covers the payload only | **CONFIRMED**, §3.2, and reproduced |
| *"This does not include the bstr wrapping -- only the payload bytes"* | **CONFIRMED verbatim**, §3.2 |
| §5 concedes the stripping attack | **CONFIRMED verbatim**, and the mitigation is lower case |
| the integrity requirement is pushed to an undefined layer | **CONFIRMED.** *the COSE Signed Message should be integrity protected during transit and at rest* — no mechanism, no layer, no reference |
| the stronger evidence is the more fragile carrier | **CONFIRMED — but this leg is OUR characterisation, not a span of the source** (pass 2 marked it): the seven legs above each resolve to the document's own words, this one is the conclusion drawn from them. It is structural rather than an oversight, for the reasons in leg A below |

**Why it is forced, in two legs — and pass 2 found the first one, which is the
document's own and not ours.**

**Leg A — normative, and it is stated, as the conjunction of four MUSTs.** The
matrix is closed by the document itself, in words, not by inference:

| | protected bucket | unprotected bucket |
|---|---|---|
| imprint over the **signature** | **unreachable** | `3161-ctt`, §3.1 |
| imprint over the **payload** | `3161-ttc`, §3.2 | — |

- §3.1, source line 256: *The 3161-ctt COSE _unprotected_ header parameter MUST be used for the mode described in Section 2.1.* — the signature-covering mode's carrier is the **unprotected** parameter, by MUST.
- §3.1, source lines 262-268: *The MessageImprint sent in the request to the TSA MUST be* the hash of the `signature` or `signatures` field — so `3161-ctt` is the signature-covering parameter, by MUST.
- §3.2, source line 383: *The 3161-ttc COSE _protected_ header parameter MUST be used for the mode described in Section 2.2.*
- §3.2, source lines 389-390: *The MessageImprint sent to the TSA (Section 2.4 of [RFC3161]) MUST be the hash of the payload of the COSE Signed Message.* — so the **protected** parameter may only ever carry a payload imprint, by MUST.

**[analysis]** Read together, those four leave no RFC 9921 parameter that can
carry a signature-covering imprint inside the protected bucket. **A second
signature pass does not open one**, because the only protected carrier the
document defines is bound by MUST to a payload hash. So the inversion is
*normatively* forced, within this document's two parameters, and that part of
the claim is the document's rather than this extraction's.

**Leg B — mechanical, and this leg is OURS.** **[analysis]** The CTT imprint is
over the signature, so the signature must exist before the token does; the
token therefore cannot be inside the signed bytes without a second signature
pass. **The inversion is forced by the dependency order as well as by the four
MUSTs, not chosen.** Measured, so that the inference is checkable: nothing in
the source states the dependency or the forcing in those terms and nothing
permits the other order — `cannot` occurs twice (source lines 124 and 435) and
neither occurrence is about placement; `re-sign`, `resign`, `second signature`
and `already signed` occur **zero** times; the nearest the document comes is
Appendix A.2's *The contents of the TST are bstr-wrapped and added to the
unprotected headers bucket in the original COSE_Sign1 object*, where *in the
original* carries the whole point without arguing it, and §5.1's *symmetric to
the signature and assembly mechanics*. **The document never names the
consequence, and the fix it does not mention** is the one §2.1's own
countersignature analogy points at: a countersignature structure that is itself
signed. `countersignature` occurs **once** in 1056 lines (source line 199).
`records/ietf/rfc-9338` (COSE Countersignatures) is in this library and is
**not cited by RFC 9921**; `9338` occurs zero times in the source.

**One leg is sharper than the summary states.** For `COSE_Sign`, the CTT
preimage includes the **per-signature unprotected bucket** (§3.1.2, 5 of 77
octets). So in the multi-signer case the TSA's digest covers bytes that *no*
COSE signature covers — not merely a head, a whole header map.

---

## 10. §1.1 is SCITT's second use case, uncited

Measured over all 1056 lines: `transparency` **4**, `statement` **9**,
`statements` **1**, `append-only` **1**, `transparent statement` **2**, and
**`SCITT` 0** and **`9943` 0**. The paragraph is written in that
architecture's vocabulary word for word, and the sentence that makes the
dependency load-bearing is:

> In order to avoid losing the TST during the registration process, the TST must be included in the signed statement.

**Lower case**, and it is the entire reason the TTC mode exists.

**What this library did about it.** `records/ietf/rfc-9943` is held here. This
record's `record.yaml` carries `see_also: [rfc-9943]` with the warrant in a
comment, which `docs/references.md` permits as the weakest relation and the one
left when no stronger fits: the document does not *cite* RFC 9943, so this is
**our** assertion about how the two relate, not a `cites` fact. `rfc-9943` was
read and **not edited** — inverses in this library are derived by `bin/reindex`,
never authored, so nothing was written on the other side.

**[analysis]** The reason to care is not bibliographic. §1.1's registration
argument is the only place in the document where the TTC mode's *protected*
placement is justified by something other than taste, and it is justified by a
property of a system the document will not name: an append-only log that keeps
only the signed parts. If we are the transparency service, that paragraph is a
requirement on **us**, and it arrives with no citation to check it against.

---
## 11. The other identifiers

**`ARCH-0001` §4.1 (`KeyId`) and §7 (`DEC-002`).** **[analysis]** RFC 9921
contributes nothing to `KeyId` and one thing against it: the only principal
identifier anywhere in the mechanism is the TSA's X.509 `DirectoryName`
(measured: 8 RDNs, `Free TSA` / `TSA` / `www.freetsa.org` / `Wuerzburg` /
`Bayern` / `DE` / an email address). It is **a name, not a key**, and
`ARCH-0001` §4.1's `KeyId` is Digest of … a key.
A verifier that trusts a timestamp trusts a certificate chain and a name — the
exact model `DEC-003`'s thumbprint work exists to avoid. **If we ever consume
third-party time we acquire a second, name-based principal model beside our
key-based one**, and nothing in this document reconciles them.

**`ARCH-0002 P1` (a local label is identity).** **[analysis]** Labels 269 and
270 are flat global integers with no principal attached — the `rfc-9165` record
makes the same observation about CDDL control-operator names. There is not even
a private-use range to criticise: the COSE Header Parameters registry's
private-use space exists, but RFC 9921 does not use it, and if it did, §5's
stripping attack would be unchanged. **P1 is untouched by this document and
unhelped by it.**

**`DEC-003`.** Two contributions, both negative and both useful. First, the
scope question §2 hands it: *do we carry a second envelope format at all*.
Second, a type observation: `TSTInfo.genTime` is a `GeneralizedTime` **string**
and the imprint algorithm is an **OID**, so a statement that carries a
timestamp carries two identifier systems that our canonical form has no
rendering for. There is no `KeyId`-shaped field anywhere in the mechanism.

**`DEC-005`.** **Not claimed, and the reason is now measured rather than
asserted.** RFC 9921 is COSE-only by construction: `COSE_Sign` and `COSE_Sign1`
are named in the Abstract and in §1 and no other envelope appears; §3.1's two
imprint alternatives are defined over *"the CBOR-encoded signature field of the COSE_Sign1"*
and the `signatures` field of `COSE_Sign`; §3.2's over
*"the payload of the COSE Signed Message"*. So the mechanism is available
to one `DEC-005` option and not the other — the same asymmetry
`records/ietf/rfc-9964` records as its Cut D. **[analysis]** Settling it needs
the DSSE record as well as this one, and this extraction does not settle it.
What it adds is the measurement that the obstacle is **not** incidental: the
CTT imprint is defined over a *field of the COSE array*, so a DSSE port would
have to choose a different preimage and would then be a different mechanism
with the same label.

**`R-O-01` (every signed object has an issuer key that can be specified).**
**[analysis]** Unaffected for the COSE object and **unmet for the token**: the
TSA's key is identified by `issuerAndSerialNumber` plus an `ESSCertID` SHA-1
certificate hash (measured: `916da3d8…`, and it does equal `sha1` of the
embedded signing certificate). A SHA-1 certificate hash as the key identifier
of a trusted third party is a 2001 design arriving in a 2026 document, and
nothing in RFC 9921 remarks on it.

**`R-O-03` (cited, not invented silently).** Satisfied by the document — every
mechanism is RFC 3161's, RFC 5652's or RFC 9052's and all three are normatively
referenced — and satisfied by this extraction: everything formal in
`schema/` that this library wrote carries `.derived.` in its filename, and
`source-renderings.txt`, which is the source's own bytes, does not.

---
## 12. The summary's claims, tested one by one

| claim in `summary.md` / `record.yaml` | verdict |
|---|---|
| *"5453 octets of ASN.1 DER, carrying a two-certificate X.509 chain, inside ONE protected-header parameter, against a 20-octet payload"* | **CONFIRMED to the octet**, and extended: 98.09 % of the object, 272.65 : 1, and 75.26 % of the token is the certificates |
| *"§6 allocates label 269 … and 270 … with Value Type `bstr` and Value Registry `-`"* | **CONFIRMED**, and the inversion of label order against mode order is new |
| *"no CDDL anywhere in the document"* | **CONFIRMED**, and six grammar words each measure zero |
| *"the receiver MUST make sure…"* with CMS named | **CONFIRMED verbatim** |
| *"§3.1.1 computes the CTT MessageImprint over the bstr-wrapped signature … including the heading bytes 0x5840"* | **CONFIRMED and PROVED**: the printed imprint reproduces from `0x5840 ‖ signature` |
| *"each mode has its own separate verification algorithm"* | **CONFIRMED verbatim**, and sharpened: neither algorithm is written down anywhere |
| *"an attacker could manipulate the unprotected header…"* and the lower-case answer | **CONFIRMED verbatim** |
| *"two digests in one document, two answers to does the wrapper count"* | **CONFIRMED**, both reproduced |
| *"§1.1's second use case is SCITT's, in SCITT's words, with no citation"* | **CONFIRMED** with counts |
| *"the example token is from a public demo TSA … and it expires"* | **CONFIRMED and DATED: it expired on 2026-03-11**, one month after publication |
| *"8 BCP 14 keywords"* | **CONFIRMED**: 6 MUST, 2 SHOULD, and the extraction's own count is 8 |
| *"Appendix A gives bytes with no pointer to the tooling that produced them"* | **CONFIRMED**, and the tooling turns out to matter: see D-1 |
| *"No `distilled/`, deliberately … If FX-1 is ever owed here the work is larger than the document's 8 BCP 14 keywords suggest"* | **OVERTAKEN** by this extraction, and the warning was right about *why*: `normative.md` had to decide how much of RFC 3161 and RFC 5652 counts as in scope, and the answer is recorded as a boundary in `protocol.yaml` and `state-machine.yaml` rather than as content |
| *"the mode that proves something about the signature sits in the bucket nothing signs"* | **CONFIRMED, and shown to be forced** by the dependency order rather than chosen (§9) |

**Nothing in the summary was falsified.** Two things it does not say and this
extraction found: **Appendix A.2's fixture does not reproduce** (D-1), and the
`COSE_Sign` CTT preimage **includes a per-signature unprotected header map**
(§3, §9).

---
## 13. Source defects — recorded, never repaired

**D-1. Appendix A.2's MessageImprint does not match the signature it is
printed beside, and §3.1.1's does.** The document's rule, its own worked
example and this appendix are in three-way disagreement that resolves against
the appendix. A.2 says
*the CBOR-encoded signature field is hashed using SHA-256 to create the following TimeStampReq object*
and prints `DD 94 71 EF …`. The signature it prints is **byte-identical** to
§3.1.1's (checked: three printings, three different hex wraps, one value), and
§3.1.1's rule over that value gives `44 C2 41 9D …`, which §3.1.1 itself
prints. **207 candidate preimages** assembled from the document's own printed
bytes were tried — bare and head-prefixed signatures, all three printed
signature values, the payload with and without its head, both header buckets in
both key orders, the whole object tagged and untagged, `Sig_structure` in three
context strings, every pairwise concatenation of the small values, and the head
written non-canonically as `59 0040`, `5a 00000040`, `5b …` and
indefinite-length — and **none** produces `DD 94 71 EF …`. The token A.2 prints
**commits to the same wrong digest** in its own TSTInfo and is otherwise
internally perfect, so this is not a transcription slip in the hex: the request
that produced the token carried the wrong imprint. **Severity: the CTT
appendix cannot be used as a fixture.** *Errata status, stated as a result
rather than an absence, and **UNVERIFIABLE FROM THIS REPOSITORY** (pass 2):
the lookup below was made from the network on 2026-10-20 and nothing in this
worktree can re-check it — the id, status, reporter, date, proposed value,
cause and the RFC 3161 control counts are all second-hand here, so treat them
as a citation to re-check, exactly as §0 treats quotations of `mofn`
documents. The mismatch itself needs no network and is verified in
`examples/vectors.yaml`.* As recorded: `errata.rfc-editor.org/rfc9921` returns
**one** erratum, **ID 9177, REPORTED (not Verified), Technical, §A.2**, filed
2026-09-13 by Florent Morselli, proposing `44 C2 41 9D …` and asking for a
newly issued token rather than an edit; its notes attribute the printed value
to a generator script hashing an error message. **Positive control:** the same
endpoint returns **5** errata for RFC 3161 (1879, 2931, 2932 Verified; 844 Held
for Document Update; 4042 Rejected), so an empty result would have been a
result and not a silent failure. The erratum's *cause* is reported, not
verified here; what is verified here is the mismatch and the correct value.

**D-2. §4 names the wrong field for the multi-signature case.** The MUST reads
*matches a hash of either the payload, signature, or signature fields*.
The `COSE_Sign` field is `signatures`, plural, as §3.1 and §3.1.2 both write
it. As spelled, the third alternative repeats the second and the multi-signer
case has no name in the document's only verification sentence.

**D-3. Both figures name the result object with a prefix the registry does not
use.** Source lines 194 and 241 draw `rfc3161-ctt COSE` and `rfc3161-ttc COSE`;
the registered names (§3.1, §3.2, §6) are `3161-ctt` and `3161-ttc`. **Four
occurrences of the prefixed spelling, all inside the two figures.** A reader
searching the IANA registry for `rfc3161-ttc` finds nothing.

**D-4. Both figures draw a `nonce` and neither example has one.** `nonce`
occurs three times: twice inside the figures, as a box crossing to the TSA, and
once in §5 as payload armoring. No normative sentence mentions a nonce; both
appendix `TimeStampReq`s are
`SEQUENCE ( INTEGER 1, MessageImprint, BOOLEAN TRUE )` with no nonce field, so
neither `TSTInfo` can echo one. An implementer taking replay protection from
the figures finds nothing behind them.

**D-5. §3 cites the two modes in reverse document order**: *The two modes described in Sections 2.2 and 2.1*.
Trivial, recorded for completeness.

**D-6. §1.1 describes a mechanism the document does not define.** *the document signer acquires a fresh TST for the document's signature from a trusted Time Stamping Authority (TSA) [RFC3161] and concatenates it with the document*.
Nothing is concatenated: §3.1 puts the token in a COSE header.

**D-7. §4's only machine-facing MUST has no failure action.** `reject`,
`rejected`, `invalid`, `discard`, `abort` and `accept` each occur **zero**
times in the source. The receiver must check the imprint and the document never
says what to do when the check fails. Compare `rfc-8392` §7.2, which spends its
last keyword on exactly that.

**D-8. §5's answer to the one attack it concedes is lower case and names no
layer.** *To avoid that, the COSE Signed Message should be integrity protected during transit and at rest.*
Under §1.2 it binds nobody, and the integrity of a signed message is delegated
outside the signed message with no mechanism named.

**D-9. The document's own test vectors are a public demonstration TSA's, with
an expiring chain and a placeholder policy OID.** Measured: `Free TSA`,
`www.freetsa.org`, TSAPolicyId `1.2.3.4.1` (an example arc), signing
certificate valid `2016-03-13` to **`2026-03-11 01:57:39Z`**, root to 2041.
The RFC published in **February 2026**, so **the only fixture it ships had an
expired signing certificate within a month of publication.** Nothing in the
document flags this, and §5 says nothing about a TSA certificate's own
lifetime — which, for §1.1's long-term signatures, is the whole problem
recursing one level up.

**D-10. Both appendix ASN.1 dumps are truncated by the document with
`[...]`** (source lines 592 and 835), so the printed structure of the token
stops before the certificates, the signer info and the signature. Everything
after that point exists only inside the hex. Recorded because it means the
document's human-readable rendering **cannot** be used to check the bytes; this
extraction had to decode them.

**D-11. §4's verification ordering runs the biggest parser first.** The imprint
check is *As part of the signature verification*, so in CTT mode — where
the token is unprotected — a conformant receiver parses 5453 unauthenticated
octets of DER before it has any signature result. Recorded as a defect rather
than a design choice because §5's threat model considers a manipulated
unprotected header and does not consider the parser reached through it.

---

## 14. Open questions

**Q-1. What does a receiver do when both labels are present?** Undefined. The
state machine has no transition for it and §5.1's *each mode has its own
separate verification algorithm* gives two answers with no precedence.

**Q-2. What does a receiver do when `3161-ttc` appears unprotected, or
`3161-ctt` protected?** Both MUSTs are addressed to the producer. Nothing tells
a consumer to check, and the CDDL that would express it does not exist.

**Q-3. Is a CTT timestamp worth anything without a transport integrity
guarantee?** §5 says it needs one and names none. For us the question is
concrete: if our export path is a file in object storage, what provides
*integrity at rest* for a header the signature does not cover?

**Q-4. Do we need signature-time evidence at all, or only payload-time?** §5.1
makes this the first question, because only CTT answers the first and only TTC
is carryable (§8.5). If the answer is signature-time, RFC 9921 is not the
mechanism and `records/ietf/rfc-9338` is where to look.

**Q-5. Who holds the TSA trust anchor, and what happens when it expires?**
`trust anchor` occurs zero times; §5 assumes trust. D-9 shows the document's own
anchor expiring inside a month.

**Q-6. If we require deterministic encoding on the export path (§8.2), what
re-exports it?** A timestamp acquired over exported bytes is only as durable as
our ability to regenerate those exact bytes years later, which is a
requirement on the *implementation*, not on the format.

**Q-7. Does `R-M-12` need a value-closure clause (§4)?** This record is the
evidence that a key-relative label can carry a registry-rooted value. Whether
the rule should reach that far is not ours to decide here.

---

## 15. Adopt / adapt / reject

| | what | why |
|---|---|---|
| **adopt** | the **per-digest** answer to *does the wrapper count*, written down beside each digest | §3.1 vs §3.2. Two digests, two answers, both deliberate, both reproducible. A global rule would have been wrong for one of them |
| **adopt** | *hash the bytes as received; never re-serialise to verify* | §4, and `R-O-05`'s second sentence |
| **adopt** | **state the failure action beside every check**, because this document does not | D-7. Our verifier spec should not be able to have this defect |
| **adapt** | third-party time, **TTC only, export only, label 269 only** | §7's mapping. Option 5 forbids native header parameters, and §8.5 says what that costs |
| **adapt** | *"determinism on the export path"* as an explicit requirement | §3, §8.2. Not stated by any `DEC-002` option today |
| **adapt** | the **mode-selection** idea, with the discriminator moved **inside the signed bytes** | §5.2, §6 condition (4). A label in the unprotected bucket cannot select a verification algorithm |
| **reject** | `3161-ctt` (label 270) in any form | an unauthenticated type indicator selecting a verification algorithm, with the conceded stripping attack and a lower-case mitigation at an undefined layer |
| **reject** | the TSA `DirectoryName` as a principal identifier | §11. A name, not a key; `R-O-01` and `DEC-003` both want the key |
| **reject** | `GeneralizedTime` and OIDs as our time and algorithm types | §7. Two identifier systems our canonical form has no rendering for |
| **reject** | the Appendix A bytes as a conformance fixture | D-9. A demonstration TSA with an expired certificate and a placeholder policy OID. Use them for parse and digest tests only — `examples/README.md` says which |

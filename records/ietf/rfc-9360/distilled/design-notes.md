---
record: rfc-9360
kind: design-notes
title: "rfc-9360 — bearing on our design"
extracted: "2026-10-20"
reviewed_by: ""
---

**Scope and provenance conventions.** Section numbers with no document name
(`§2`, `§5`) are RFC 9360's. Our own documents are cited by id (`ARCH-0001`,
`ARCH-0002 P1`, `DEC-002`, `MD-3`, `R-O-01`). Three markers distinguish
voices, following `records/ietf/rfc-9741/distilled/design-notes.md` and
`rfc-8392`'s:

- unmarked prose reports **RFC 9360** or **our decisions**, as cited;
- **[analysis]** marks reasoning of this extraction that neither the source nor
  our documents state;
- **[correction]** marks a working assumption, or a claim in one of our own
  artifacts, that the source does not support.

**Which quotations below are checkable here, and which are not.** This library
is **standalone by design** — independently cloneable and citable by projects
that are not `mofn` (`CLAUDE.md`). The `mofn` documents this file cites are
**not present in this repository**: `ARCH-0001` (including §4.1 and §7),
`ARCH-0001-PROPOSAL-v0.2.0`, `ARCH-0002` (P1–P5), `ADR-0001`, `MD-3`,
`DECISIONS-0001`, and the `R-O-*` / `R-M-*` / `R-I-*` rules. **Every quotation
of those documents here is reproduced from the extracting agent's context and
cannot be verified from this repository.** Treat each as a citation to be
re-checked against `mofn` before it is relied on. `rfc-9741`'s cross-check pass
set that convention and `rfc-9964` followed it; this file follows it rather
than inventing a third.

What *is* checkable here, and was: `docs/extraction.md`'s statement of MD-3
(*"option 5: reduced CBOR, no IANA tags, COSE as export only"*),
`topics/canonical-encoding.yaml`'s six conditions and its identification of
`DEC-002` options 1 and 3, and the artifacts of `records/ietf/rfc-9054`,
`rfc-9679`, `rfc-8610`, `rfc-8742` and `rfc-9053`. Each is in this worktree.

**How quotations of the source are produced.** Every one was cut from
`.cache/rfc-9360.txt` by line range **by script**, narrowed to a contiguous
character span where a sentence is quoted out of a flowed paragraph, and
verified mechanically as a substring of the whitespace-normalised source before
this file was written. **Nothing is spliced and no line-break hyphenation is
healed.** Where the source wraps a word across lines the break is declared in
place. A lane-wide audit over this file, `rfc-9054`'s design notes and both
READMEs was run as one pass, not per record, because the defect it hunts — an
inserted or dropped word that propagates into every file of a lane — is
invisible to a per-record check.

**Decision status, stated plainly.** `DEC-002` in `ARCH-0001` §7 lists **four**
options. "Option 5" exists only as *proposed* text in
`ARCH-0001-PROPOSAL-v0.2.0` §3.3, and that proposal is unmerged. `MD-3`
(2026-09-28) *narrows* `DEC-002` to option 5. **No `DEC-002` ADR has been
written.** Nothing below may be read as an accepted encoding decision. Within
this library, option 1 is canonical S-expressions
(`records/ietf/rfc-9804`, `rfc-2693`) and option 3 is JCS over JSON
(`records/ietf/rfc-8785`); both identifications come from
`topics/canonical-encoding.yaml`, which is here.

**What this extraction added beyond the summary, mechanically.** Eight computed
vectors, a CDDL parser run against RFC 8610's own grammar, and one correction
to the record's own summary that changes the shape of its headline finding
(§3 below). The source prints **no example of any kind**, so every fixture in
`examples/` is this extraction's and says so.

---
## 1. What this record decides, in one paragraph

**`DEC-003` must say no to `x5t`, and the reason is a measurement rather than a
preference.** `ARCH-0001` §4.1's `KeyId` is a digest over canonical **key**
bytes; §2 of this document puts `x5t`'s digest over the **certificate**:> The second element is a binary string containing the hash value computed over the DER- encoded certificate.
The source wraps `DER-encoded` across lines 222–223 as `DER-` + `encoded`,
and the quotation above carries that break rather than healing it. So an `x5t`
value identifies a certificate, not a key: two certificates over one key have
two `x5t` values, one certificate reissued has a third, and none of them is a
function of the key alone. `rfc-9679` §5.4 draws the same line from the other
side, preferring a SubjectPublicKeyInfo digest to a digest of a complete
certificate value. **That is the one decision a reviewer should take from this
record.** Everything below is either its evidence or a separate finding about
what the document *does* supply — of which the valuable one is §6's
authenticated in-band algorithm indicator.

---
## 2. The contradiction, and the correction that sharpens it

The record's `contradicts: rfc-9054` edge rests on §5's last paragraph:> The security of the algorithm used for 'x5t' does not affect the security of the system, as this header parameter selects which certificate that is already present on the system should be used, but it does not provide any trust.
Against §2, which defines the opposite use four times over. The `x5t`
definition itself:> The 'x5t' header parameter can be used alone or together with the 'x5bag', 'x5chain', or 'x5u' header parameters to provide integrity protection of the end-entity certificate.
And §2's worked suggestion for satisfying the integrity obligation, for
`x5chain`:> This can, for example, be done by sending the header parameter in the protected header, sending an 'x5chain' in the unprotected header combined with an 'x5t' in the protected header, or including the end-entity certificate in the external_aad.
Two lines earlier, about that same unprotected bucket:> Sending the header parameter in the unprotected header bucket allows an intermediary to remove or add certificates.
**In that configuration the certificate is not already present on the
system.** It arrives in a bucket the document says an intermediary may rewrite,
and the protected `x5t` is the only thing binding it. `examples/vectors.yaml`
V-0006 executes exactly this: same protected bucket, two different unprotected
buckets, and **the protected bucket's bytes are byte-identical before and
after the swap**, so whatever signature covers them still verifies and the
only detection is the digest comparison. The property that configuration needs
is second-preimage resistance at minimum — a property `rfc-9054` §5 names and
RFC 9360 never does. Measured: `collision` occurs **zero** times in RFC 9360's
614 lines and **15** times in RFC 9054's 498.

### 2.1 [correction] The summary says "§5's own next paragraph". It is not the next paragraph, and the real neighbour is worse

This record's `summary.md` and its `record.yaml` comment both locate the
identity-misbinding attack in *"the identity-misbinding attack §5's own next
paragraph describes"*. **That is wrong about the ordering, and the correct
ordering strengthens the finding rather than weakening it.** §5 has **nine
paragraphs**, at source lines 440–446, 448–459, 461–469, 471–477, 479–485,
487–489, 491–495, 497–500 and 502–505 — the boundaries are blank lines and
`normative.md` quotes all nine, one region each, in order.

- The `x5t` claim is **paragraph 9 of 9**, the last in the section. §6
  (References) begins at line 507. **There is no next paragraph.**
- The identity-misbinding attack is **paragraph 3 of 9**, forty-one lines
  *earlier*.
- The paragraph immediately **before** the `x5t` claim is paragraph 8, and it
  says this:
> Protecting the integrity of the 'x5bag', 'x5chain', and 'x5t' contents by placing them in the protected header bucket can help mitigate some risks of a misbehaving CA (cf. Section 5.1 of [RFC2634]).
**Read those two paragraphs in the order the document prints them.**
Paragraph 8 says that protecting the integrity of `x5bag`, `x5chain` **and
`x5t`** by placing them in the protected bucket mitigates a risk — i.e. that
the protected `x5t` is doing security work. Paragraph 9 then says the security
of the algorithm used for `x5t` does not affect the security of the system.
They are adjacent, they are about the same parameter in the same bucket, and
they cannot both stand. The misbinding paragraph is *also* evidence, and §5's
own account of it is quotable:> Without proof of possession, an attacker can trick the CA into issuing an identity-misbinding certificate with someone else's "borrowed" public key but with a different subject. An on-path attacker can then perform an identity-misbinding attack by replacing the real end-entity certificate in COSE with such an identity- misbinding certificate.
but it is forty-one lines away and about proof of possession rather than
about `x5t`. **The adjacent pair is the better citation**, and the summary's
version should be corrected to it rather than defended. Recorded here rather
than edited into `summary.md` by this pass; §13 lists it as a summary
correction owed.

---
## 3. `R-O-01` — `kid` occurs zero times, and the gap is in the message

`R-O-01`: *"Every signed object SHALL have an issuer key that can be specified
as `KeyId`."* **[Unverifiable from this repository — `mofn` rule.]**

**Measured over all 614 lines: `kid` occurs zero times.** So does `verify`, and
so does `verifier`. This document adds **four** ways to identify a key —
`x5bag` (32), `x5chain` (33), `x5t` (34), `x5u` (35) — and relates none of them
to COSE's own key identifier (RFC 9052 §3.1, label 4). The consequence is
precise and it is a property of the **message**, not of an implementation: a
conforming `COSE_Sign1` may carry `x5chain` and no `kid` at all, and then no
`KeyId` is recoverable from the object without a rule we write. Two rules are
available and they are not equivalent:

1. **Derive the `KeyId` from the certificate's SubjectPublicKeyInfo.** Correct
   under `DEC-003` — it is a digest over key bytes — but it requires parsing
   DER to get at the key, which is the cost §7's Cut 1 prices.
2. **Require `kid` alongside, protected.** Cheap, and the format does not
   require it, so it is our rule and must be stated as one.

[analysis] **Option 1's advantage here is structural rather than incidental,
and it is the kind of finding `docs/extraction.md` asks for.** Under `DEC-002`
option 1 (canonical S-expressions) a key is named by its own canonical
encoding, so there is no separate identifier field that can be absent. The
hole `R-O-01` falls into here exists *because* the export format separates
"the key" from "the name of the key" and then makes the name optional. That is
a cost option 5 pays by construction and option 1 does not pay at all. Scored
in §7 as Cut 5.

---
## 4. `DEC-003` — the document answers the mandatory clause, and answers it wrongly

`DEC-003`'s mandatory clause: *"must specify canonical key bytes before
hashing."* **[Unverifiable from this repository — `mofn` decision.]**

RFC 9360 does specify what gets hashed, which is more than `rfc-9054` does, and
what it specifies is the wrong object (§1 above). Three further facts bear on
`DEC-003`, each measured:

- **The digest has no declared length.** `hashValue` is `bstr` and nothing in
  the CDDL or the prose ties its length to `hashAlg`. `examples/vectors.yaml`
  V-0008 shows that `[-16, h'']` — an **empty** digest declaring itself
  SHA-256 — conforms to the document's own grammar. An implementation that
  compares without checking the length has no binding at all.
- **The algorithm is unrestricted.** §2's only algorithm statement is a floor
  on support:
> For interoperability, applications that use this header parameter MUST support the hash algorithm 'SHA-256' but can use other hash algorithms.
  A floor on *support*, not a ceiling on *use*: it excludes no registry
  value. `schema/x5t-hashalg-policy.derived.yaml` is the restriction we would
  have to add, with a per-value verdict for all eight of `rfc-9054`'s hash
  identifiers.
- **And the registry is named without being cited.** §2 points `hashAlg` at
  *"the "COSE Algorithms" registry"* and gives the IANA URL; `9054` occurs
  **zero** times in RFC 9360. §5 of this file is that finding in full.

**What `DEC-003` should take from this document, then, is a negative and a
shape.** The negative: an `x5t` value is not a `KeyId` and must not be used as
one. The shape: §6.

---
## 5. `R-O-03` — what can be cited from here, and what cannot

`R-O-03`: *"Canonicalization algorithm for each concrete encoding SHALL be
cited, not invented silently."* (`ARCH-0001` §5.3, as five other records in
this library quote it.) **[Unverifiable from this repository — `mofn` rule.]**

**RFC 9360 cites no canonicalization and defines none.** Measured: `canonical`,
`canonicalization` and `deterministic` each occur **zero** times. What it does
instead is inherit one, silently, in a byte string — see §7's Cut 1.

The citable thing it supplies is a *floor*, not an algorithm: `MUST support the
hash algorithm 'SHA-256'`. The algorithm identifier itself has to be cited from
`rfc-9054` (`-16`), which is the other record in this lane, and **this document
does not make that citation itself.** That is the cross-record finding and it
runs in the direction nobody would guess:

| | |
|---|---|
| RFC 9054 (August 2022) → RFC 9360 | cites it **twice**, as `draft-ietf-cose-x509-08`, 14 December 2020 — in §1 for the certificate-fingerprint use case and in §3.2 as the **justification for registering SHA-256/64** |
| RFC 9360 (February 2023) → RFC 9054 | **zero citations.** `9054` does not occur in the source. Its normative references are RFC 2119, RFC 5280, RFC 8152, RFC 8174, RFC 8949 and RFC 9052; twelve more are informative; RFC 9054 is in neither list |

So the registry rows `x5t` selects from were created **for this document**, six
months before it published, and this document never names the document that
created them. An implementer reading RFC 9360 alone learns that `hashAlg` comes
from a registry and is given a URL to a live IANA page — no stable reference,
no list, and no warning that two of the values that page holds are marked
`Filter Only`. **That is the load-bearing form of the citation gap, and neither
record could have found it alone:** RFC 9360's record would have recorded "it
names a registry and cites nobody", and RFC 9054's would have recorded "it
cites a draft that became an RFC". The finding is the *asymmetry*.

---
## 6. `R-O-05` — the one thing to copy, and it is in the protected bucket

`R-O-05`'s type-indicator clause wants *"an authenticated type indicator
carried inside the signed bytes"* (the wording here is
`topics/canonical-encoding.yaml`'s condition (4), which **is** in this
repository: *"The encoding profile is named by an authenticated type indicator
carried inside the signed bytes."*). **ADOPT.**

`x5t` carries its algorithm **in-band**, as the first element of the structure
rather than as a side agreement:> The first element is an algorithm identifier that is an integer or a string containing the hash algorithm identifier corresponding to the Value column (integer or text string) of the algorithm registered in the "COSE Algorithms" registry (see <https://www.iana.org/assignments/cose/>).
and in the configuration §2 recommends, that structure is **inside the
protected bucket** — so the algorithm indicator is covered by the signature.
`examples/vectors.yaml` V-0006 shows the protected bytes that carry it.

**Compare `rfc-9679`, same working group, same question, opposite answer.**
That record is at `profile: full` in this library and its finding is that the
COSE Key Thumbprint is a **bare digest with nowhere to name `H`** — so two
parties on different hash functions never match and cannot tell why. RFC 9360
got this right and RFC 9679 did not. `R-O-05` should copy RFC 9360's shape:
*(algorithm identifier, digest)*, both inside the signed bytes.

[analysis] **One caveat, and it is the reason §7's Cut 4 exists.** An in-band
algorithm indicator is only as good as the set of values it may take. RFC 9360
authenticates the indicator and restricts it to nothing, so the shape is right
and the range is wrong. Our version needs both halves.

---
## 7. MD-3, header by header — and where this document cuts against it

`MD-3` narrowed `DEC-002` to **option 5**: `docs/extraction.md`, which is in
this repository, states it as *"reduced CBOR, no IANA tags, COSE as export
only"*. **A narrowing, not an acceptance.** The mapping first, then five cuts.

### 7.1 The header-by-header mapping

**What our statement fields would ride in if we accepted X.509 carriage, and
under which allocation.** Field names are `ARCH-0001` §4.1's, in the vocabulary
`rfc-8392`'s design notes established for this effort.

| our field (`ARCH-0001` §4.1) | RFC 9360 carrier | label | registry | option-5 verdict |
|---|---|---|---|---|
| `KeyId` of the signing key | `x5t` | 34 | COSE Header Parameters (§4.1) | **reject as a `KeyId`** — digest is over the certificate, not the key (§1, §4) |
| issuer principal | the certificate `Subject`, **inside the DER** | — | the CA's namespace, not IANA's | **reject** — a global name, against `ARCH-0002` P1 (§8) |
| the signing key itself | `x5bag` / `x5chain` | 32, 33 | COSE Header Parameters | **export only**, never native — Cut 1 |
| key-discovery pointer | `x5u` | 35 | COSE Header Parameters | **reject** — network dependence inside a signature check (§9 limit 8) |
| digest algorithm indicator | `x5t[0]` (`hashAlg`), in-band and protected | — | COSE Algorithms (`rfc-9054`) | **adopt the shape, restrict the range** (§6, Cut 4) |
| sender's static-static ECDH key | `x5t-sender`, `x5u-sender`, `x5chain-sender` | −27, −28, −29 | COSE Header **Algorithm** Parameters (§4.2) | **reject the parameters, keep the precedent** (§10) |
| statement type | — | — | — | **nothing here**; `rfc-9596`'s `typ` (16) is the carrier |
| "these bytes carry certificates" | `application/cose-x509` | — | Media Types (§4.3) | **drop** — a transport signal, and it has no magic number |
| certificate canonical form | **ASN.1 DER**, inside the `bstr` | — | ITU-T X.690 | **inherited, not chosen** — Cut 1, and it is the finding |
| statement canonical form | — | — | — | **ours**; the document names none |

**The export mapping, in one line.** If we ever export a certificate-bearing
COSE object: `x5chain` (33) and `x5t` (34) **both in the protected bucket**,
`hashAlg` restricted to `Recommended: Yes` values, `hashValue` length pinned
per algorithm, `kid` (4) present and protected alongside, and no `x5bag`, no
`x5u`, no `−27`/`−28`/`−29` and no `application/cose-x509`.

**What we deliberately do not carry:** `x5bag` (unbounded work — §9 limit 5),
`x5u` (network dependence), all three `*-sender` labels (they are
ECDH-SS-scoped and we do key agreement nowhere), the media type, and the
certificate `Subject` as a name of anything.

### 7.2 Cut 1 — the DER cut, and it cuts by **evasion**. Costs **every** option identically, which is the finding

**Count the ledger on option 5's own terms first.** RFC 9360's IANA footprint
is **eight allocations and zero CBOR tags**: four header labels (§4.1), three
algorithm-scoped header labels (§4.2), one media type (§4.3). Measured: `tag`,
`tags` and `tagged` occur **zero** times in the source. So option 5's literal
"no IANA tags" clause **survives completely untouched** — and the profile
acquires ASN.1.

The mechanism is one sentence, and it is the whole of what the CDDL says about
the content:> The contents of "bstr" are the bytes of a DER-encoded certificate.
A reduced-CBOR profile reduces the CBOR. **It does not reach inside a byte
string.** Carrying one certificate buys a second encoding (DER), a second
parser, a second *canonical form* — DER is itself a canonicalization, with its
own rules and its own history of parser differentials — and a second trust
system (RFC 5280 §6 path validation, revocation, anchors). None of that is
governed by "reduced CBOR", none of it is expressible in our CDDL, and none of
it is excluded by "no IANA tags". Mechanically confirmed for this pass:
`schema/cddl-parse.derived.txt` records that neither of the document's two CDDL
rules can constrain the content, and that even CDDL's `.cbor` control operator
would be wrong here because the payload is not CBOR.

**[correction] Do not score this as option 5 losing to another option.** Every
`DEC-002` option pays this cost identically — option 1 (canonical
S-expressions) would carry the same DER inside the same opaque octet string,
and so would option 3 inside a base64 JSON string. So the DER-in-a-header
problem is an argument about **scope**, not about encoding: it says the
decision that matters is *"do we carry certificates at all"*, and that decision
belongs to `DEC-003`, not `DEC-002`. **What option 5 should say and does not is
that its exclusions do not and cannot reach a payload.** That is a defect in
how the narrowing is *worded*, not in the option.

**What option 5 *can* exclude here is the whole parameter set**, and that is
cheap to write and worth writing: a lint rule rejecting labels 32, 33, 34, 35
and −27, −28, −29 in a native statement. Note it must reject `x5t` (34) **too**,
even though `x5t` is the only one of the four that carries no ASN.1 — because
§2's digest is over the DER certificate, so accepting an `x5t` accepts the DER
canonical form **by reference** without carrying the bytes.

### 7.3 Cut 2 — option 5 inherits a second governed namespace. Costs **option 5**; options 1 and 3 do not pay it

"COSE as export only" means the COSE Header Parameters registry is ours by
construction, and this document is what that dependence costs: **seven labels,
every one of them two octets.** `examples/vectors.yaml` V-0001 measures it —
32–35 encode as `0x1820`–`0x1823` and −27/−28/−29 as `0x381a`–`0x381c`, because
32 is above the 23 that fits in an initial byte and −27 is below the −24 that
does. There is no one-octet label left in the general range for a parameter of
ours.

This is the same shape two other records in this lane found one layer up and
one layer down, and the convergence is the evidence rather than any single
record:

- `rfc-9165`'s extraction: option 5 is **registry-reduced, not registry-free**
  — §6.1's dotted-name policy prices the namespaced form above the global one.
- `rfc-8392`'s extraction: option 5 trades **one tag number** for the CWT
  Claims registry, *"a governed namespace with four allocation tiers, a mailing
  list, a three-week review and a 21-day escalation path"*.
- this record: the COSE Header Parameters registry, at two octets a label, with
  no cheap range remaining.

Options 1 and 3 are registry-free at this layer: `topics/canonical-encoding.yaml`
records that JSON *"has no tag space and no header space"*, and canonical
S-expressions name their fields in the expression.

### 7.4 Cut 3 — the export format carries **three** framings of one list, and two of them are the same bytes. Costs **option 5**

§2 gives a certificate list two encodings, and §4.3 gives it a third:> When the application/cose-x509 media type is used, the data is a CBOR sequence of single-entry COSE_X509 structures (encoding "bstr").
So the same information travels as a bare `bstr` (one certificate), as a
`[ 2*certs: bstr ]` array (two or more), or as a **CBOR sequence** with no
enclosing data item. `examples/vectors.yaml` V-0003 encodes all three and finds
the result that matters: **for one certificate the array framing and the
sequence framing are byte-identical**, because a one-item CBOR sequence is just
the item. The only thing that could disambiguate is the media type's `usage`
parameter, which is optional and whose absence means only *"no further
information about the intended meaning of the order"*.

That is `topics/canonical-encoding.yaml` condition (1) failing — *"The encoding
is INJECTIVE over the values it encodes, not merely deterministic"* — **inside a
format option 5 exports to**, and it is not a cost of CBOR. Option 3 pays
nothing here: JSON has no sequence construct, so there is no second framing to
collide with the first. Option 1 pays nothing either.

Worth saying in the same breath, because it is the opposite result and the
document earned it: `COSE_X509 = bstr / [ 2*certs: bstr ]` makes the
**one-element array invalid**, so one certificate has exactly one encoding
inside the CDDL. Checked for this pass against RFC 8610's grammar:
`X = bstr / [ 1*certs: bstr ]` parses perfectly well, so the `2*` is a
deliberate choice rather than a grammatical necessity
(`schema/cddl-parse.derived.txt`). **The document removes an ambiguity by
construction at the CDDL layer and reintroduces it at the media-type layer.**

### 7.5 Cut 4 — the export format admits an algorithm our profile must forbid, and cannot say which. Costs **option 5** by construction

This is §2's contradiction expressed as a `DEC-002` cost. `COSE_CertHash` has
**exactly two fields**; `rfc-9054` marks SHA-1 (−14) and SHA-256/64 (−15)
`Recommended: Filter Only`, defined there as *"not to be used for purposes that
require collision resistance"*; and `Recommended` is a **registry column, not a
wire field**. `examples/vectors.yaml` V-0004 is the result as an identity rather
than an inference: **a filtering `x5t` and a binding `x5t` with the same
algorithm are the same bytes** — 23 octets with SHA-1, and the identity holds
for every value of `hashAlg`.

Option 5 says "COSE as export only", so we export into a format whose own
grammar permits a value our profile must reject and whose wire form cannot
express the distinction the registry draws. **The forbidding therefore has to
live in our profile rather than in the format**, which is exactly the shape
`R-O-03` exists to prevent — except that here the invention is a *restriction*
rather than an algorithm, so `R-O-03` does not catch it. Options 1 and 3 pay
this cost only if they choose to cite the same registry; option 5 pays it by
construction.

### 7.6 Cut 5 — the export format makes the key identifier optional. Costs **option 5**; option 1 cannot pay it at all

§3 above, as a `DEC-002` entry. `kid` occurs **zero** times in RFC 9360, and a
conforming certificate-bearing `COSE_Sign1` need carry none. So option 5's
export mapping has to **add** a rule the format does not have — "`kid` present
and protected, always" — and a receiver that applies RFC 9360 faithfully and
our rule not at all gets an object with no recoverable `KeyId`.

[analysis] **Option 1 cannot pay this cost, because it has no separate
identifier field.** Under canonical S-expressions a key is named by its own
canonical encoding, so "the name of the key" is not a field that can be absent.
That is the second ground on which option 1 comes out ahead in this lane, and
`docs/extraction.md`'s worked example is the precedent for reporting it: RFC
9804's extraction put option 1 *"on the right side of all four grounds that
withdraw option 3"*, and that finding existed only because the extraction was
not required to agree with the narrowing. **An extraction that can only confirm
is not evidence.**

---
## 8. `ARCH-0002` P1 — the RFC's own worst case is an argument for key-relative naming

`ARCH-0002` P1 is key-relative naming, accepted by `ADR-0001`. **[Unverifiable
from this repository — `mofn` decisions.]** A certificate carries a CA-issued
**global** name.

**The document never argues against key-relative naming; it is silent on it**,
and the overclaim to avoid is pretending otherwise. §2's actual case for
certificates is operational:> The use of X.509 certificates allows for an existing trust infrastructure to be used with COSE. This includes the full suite of enrollment protocols, trust anchors, trust chaining, and revocation checking that have been defined over time by the IETF and other organizations.
What it does supply, and it is better evidence than anything we would have
asserted, is §5's identity-misbinding paragraph (quoted in §2.1 above). **That
attack exists only because the name and the key are separable.** Under P1 the
name *is* the key, so there is nothing to misbind: no CA can be tricked into
binding someone else's borrowed public key to a different subject, because
there is no subject field to differ. The RFC's own worst case is P1's argument.

The second P1-relevant fact is about linkability, and it covers the hash too:> COSE does not provide identity protection by itself, and the 'x5t' and 'x5u' header parameters are just alternative permanent identifiers and can also be used to track the subject.
So `x5t` is not an escape from the certificate's identity exposure — the
document classes it as another permanent identifier. [analysis] That is worth
holding against any later suggestion that a thumbprint is a privacy-preserving
alternative to a certificate; by this document's own account it is not.

---
## 9. `DEC-005` — it mandates no algorithm, and the one floor it sets is in this lane

`DEC-005`. **[Unverifiable from this repository — `mofn` decision.]**

RFC 9360 specifies **no** cryptographic algorithm. It names exactly one, as a
mandatory-to-**implement** floor for interoperability (§4 above), and it defers
everything else: signatures and key agreement to RFC 9052 and RFC 9053, hash
identifiers to the COSE Algorithms registry, certificate validation to
RFC 5280.

Two observations for `DEC-005`:

- **`MUST support SHA-256` is the only mandatory-to-implement algorithm floor
  anywhere in this lane**, and it is in the carriage document rather than in
  the algorithm document. `rfc-9054`, whose entire subject is hash algorithms,
  sets no floor at all — it is Informational and has two BCP 14 keywords, both
  `SHOULD`-strength and both about collision attacks. If we want a floor we
  take it from here and cite the identifier from there.
- **The floor is on support and not on use**, so it coexists with an
  unrestricted range (Cut 4). A `DEC-005` statement modelled on this one would
  inherit that defect; ours needs both a floor and a ceiling.

---
## 10. `R-M-12` — IANA's own answer to label scoping, and it is not ours

`R-M-12` requires an extension point to be a *(key, local label)* pair.
**[Unverifiable from this repository — `mofn` rule.]**

§3's three parameters live in a **different registry** from §2's four:> IANA has registered the new COSE Header Algorithm parameters in Table 2 in the "COSE Header Algorithm Parameters" registry.
and Table 2 pins each of them to five algorithms — `ECDH-SS+HKDF-256`,
`ECDH-SS+HKDF-512`, `ECDH-SS+A128KW`, `ECDH-SS+A192KW`, `ECDH-SS+A256KW`. So
`−27` means `x5t-sender` **only** under those five, and the same integer is free
elsewhere in the registry.

**That is a ratified precedent for scoping a label by a value in the protected
header rather than globally** — the *(algorithm, label)* pair. It is **not**
`R-M-12`'s *(key, local label)* pair, and this record should not claim it is.
What it is worth is narrower and still useful:

1. It shows the pattern is **implementable inside COSE without a fresh registry
   per extension point** — one registry, scoped lookups — which is more than
   `rfc-9052`'s extraction could say.
2. It shows the scoping key is a value the signature covers (`alg` is in the
   protected header), so the scoping is authenticated. `R-M-12`'s key would
   need the same property.
3. [analysis] And it shows the cost: CDDL cannot express it.
   `schema/x5-headers.derived.cddl` carries the five algorithms as a **comment**
   and `messages.yaml` as a `valid_only_under_algorithms` list, because there is
   no grammar for *"this label means this only when that field holds one of
   these"*. Any `R-M-12` implementation inherits that — the scoping lives in
   prose or in code, never in the schema.

---
## 11. `canonical-encoding` conditions (1)–(6), scored

The six conditions are `topics/canonical-encoding.yaml`'s, which **is** in this
repository, so these quotations are checkable.

| condition | verdict for RFC 9360 |
|---|---|
| **(1)** *"The encoding is INJECTIVE over the values it encodes, not merely deterministic."* | **split, and the split is the finding.** PASS at the CDDL layer: the `2*` makes one certificate have exactly one encoding, deliberately (Cut 3). FAIL at the media-type layer: for one certificate the array and CBOR-sequence framings are the same bytes, and §4.3's `usage` parameter is optional. Also FAIL on `hashValue`, whose length is unconstrained, so `[-16, h'']` and `[-16, <32 octets>]` both claim SHA-256 (V-0008) |
| **(2)** *"The decoder REJECTS non-canonical input rather than normalising it."* | **not addressed.** The document states no decoder behaviour at all. Its one rejection rule is about trust (`MUST NOT be trusted`), not about encoding |
| **(3)** canonicalisation runs once, at authoring, on trusted input, never as part of verification | **VIOLATED by construction, one layer down.** §2's `x5t` digest is over the DER certificate, so a verifier that re-encodes the certificate to check the digest is canonicalising **untrusted input during verification** — which is exactly what (3) forbids. The only safe reading is that the verifier digests the received bytes verbatim and never re-encodes, and the document does not say so |
| **(4)** *"The encoding profile is named by an authenticated type indicator carried inside the signed bytes."* | **PASS, and it is the one thing to copy.** `hashAlg` is in-band and, in §2's recommended configuration, inside the protected bucket (§6). The indicator names the digest algorithm rather than the encoding profile, but the shape is right |
| **(5)** *"Set-valued fields carried in arrays have a defined canonical order."* | **FAILED, and named as failed by the document itself.** `x5bag` is explicitly unordered, may contain duplicates, and may contain extraneous certificates. `x5chain` is ordered, and that is the difference between them — so the document knows the problem and ships both answers |
| **(6)** text load-bearing for identity has a declared Unicode normalisation rule, or an explicit refusal plus rejection | **not addressed, and there is text in the identity path.** `x5u` is a CBOR text string holding a URI, and the certificate `Subject` is a DER structure full of text with its own X.500 string-equality rules. `Unicode` occurs **zero** times in the source. RFC 5280 §7 has rules; RFC 9360 does not cite them |

**Three fails, two of them structural.** (3) is the sharp one: the document's
own digest definition makes the safe implementation the one nobody is told to
write.

---
## 12. What we adopt, adapt and reject

### 12.1 Adopt

1. **`(algorithm identifier, digest)` as the shape of any digest we carry, with
   the identifier in-band and inside the signed bytes** (§6). This is the
   record's positive contribution and the opposite of `rfc-9679`'s choice.
2. **`COSE_X509`'s refusal of the one-element array**, as a pattern: remove an
   ambiguity by construction where the grammar can, rather than by a
   canonicalization rule (Cut 3). The price — two shapes for one field — is
   worth naming when we copy it.
3. **"The end-entity certificate MUST be integrity protected by COSE" as a
   single rule with one named mechanism**, not four restatements with
   "for example" (§13 defect D-1).

### 12.2 Adapt

1. **The `hashAlg` range.** Adopt the in-band indicator; restrict the values to
   `Recommended: Yes` and pin the digest length per algorithm
   (`schema/x5t-hashalg-policy.derived.yaml`, `schema/x5-headers.derived.cddl`).
2. **The bucket rule.** RFC 9360 permits either bucket for all four parameters;
   our version requires the protected bucket wherever the parameter carries a
   binding, which is what §2's own recommendation does in prose and the format
   does not require.
3. **The *(algorithm, label)* scoping precedent**, as evidence that `R-M-12`'s
   shape is implementable inside COSE — not as `R-M-12` itself (§10).
4. **`rfc-9054` §2's filtering argument as the test for when a weak digest is
   admissible.** Its precondition is that surviving candidates are each checked
   against the signature. Where that downstream check exists, a Filter Only
   value is defensible; where it does not, it is not. Stated this way the rule
   is checkable, which neither document makes it.

### 12.3 Reject

1. **`x5t` as a `KeyId`** (§1, §4). The digest is over the wrong object.
2. **`x5bag`** (§13 limit 5): unordered, duplicate-bearing, extraneous-bearing,
   possibly incomplete, with path building left to the verifier. A constrained
   relying party cannot bound the cost of a conforming message.
3. **`x5u`**: it reintroduces a network dependence inside a signature check,
   and §5 admits the ordering problem that creates without resolving it.
4. **The certificate `Subject` as a name of anything** (§8).
5. **`application/cose-x509`**: a third framing (Cut 3), with no magic number
   and no file extension, so a file of this type is not self-identifying.
6. **All three `*-sender` labels**: they are scoped to five ECDH-SS algorithms
   and we do static-static key agreement nowhere. Keep the precedent, drop the
   parameters.
7. **Silence on failure reporting.** The document specifies no error code and
   no message; `protocol.yaml`'s `absent` list records it. We make reporting a
   rule.

---
## 13. The summary's findings, tested against the source

Each of the record's `summary.md` findings, with a verdict. One is corrected,
four are confirmed, three are scoped.

1. **"§5's claim that the `x5t` hash does not matter is false in the
   configuration §2 itself recommends."** **CONFIRMED**, and the configuration
   is now executed as a fixture (V-0006): the protected bucket's bytes are
   identical across an intermediary rewrite, so the digest comparison is the
   whole binding.
2. **"the identity-misbinding attack §5's own next paragraph describes."**
   **[correction] REFUTED as stated** (§2.1). The misbinding paragraph is §5's
   **third of nine**, forty-one lines earlier; the `x5t` claim is the **ninth
   and last** and nothing follows it. The adjacent paragraph is §5's eighth,
   which says protecting `x5t`'s integrity mitigates a misbehaving CA — a
   **sharper** contradiction than the one claimed. The finding survives and
   improves; the citation must change.
3. **"`COSE_CertHash` excludes no registry value, and Filter Only is a registry
   column, not a wire field, so a verifier handed `[-14, h'…']` cannot tell
   whether the sender was filtering or binding."** **CONFIRMED and executed**
   (V-0004): byte-identical — 23 octets with SHA-1 — and the structure has exactly two
   fields so there is nowhere a purpose could have gone. What it costs us is in
   Cut 4: the restriction has to live in our profile because the format cannot
   express it.
4. **"`kid` occurs zero times."** **CONFIRMED** by sweep. Also confirmed:
   `verify` and `verifier` zero, `SHA-1` zero, `tag`/`tags`/`tagged` zero,
   `canonical`/`deterministic` zero, `9054` zero, `8742` zero.
5. **"§2's `x5t` hash is over the whole DER certificate, not the key, which is
   the wrong answer to `DEC-003`."** **CONFIRMED** (§1), quoted with the
   source's own line-break hyphenation intact.
6. **"The DER-in-a-header cut cuts by evasion, not violation … do not score it
   as option 5 losing."** **CONFIRMED and sharpened** (Cut 1): eight IANA
   allocations, zero CBOR tags, and the mechanical confirmation that no CDDL
   constraint — including `.cbor` — can reach the payload. The scope argument
   stands and the decision belongs to `DEC-003`.
7. **"§3's `x5*-sender` labels sit in the COSE Header Algorithm Parameters
   registry … the nearest ratified relative of `R-M-12`."** **SCOPED** (§10).
   Confirmed as to the registry and the five-algorithm scoping, and narrowed on
   two points the summary does not make: the scoping key is authenticated
   (which `R-M-12` would need), and **CDDL cannot express it**, so any
   `R-M-12` implementation keeps its scoping outside the schema.
8. **"an errata search returns nothing for RFC 9360."** **CONFIRMED, with a
   positive control.** Searched `https://errata.rfc-editor.org/search/?rfc_number=9360`
   on 2026-10-20: *"No matching errata found."* The same endpoint with
   `rfc_number=9054` returns `Reported (1)` and errata ID 7335, so the search
   works and the negative is a real negative rather than a broken query.
9. **"it prints no example at all."** **CONFIRMED** (V-0007): `Figure`,
   `Appendix`, `vector` and "test vector" all zero, no hex, no base64. Scoped
   by one addition — the summary's comparison to `rfc-9338` ("carries six") was
   not re-checked by this pass and is left as the summary's claim.

---
## 14. Source defects and ambiguities — reported, never repaired

**D-1. The document's central obligation is stated four times and mandated
never.** "The end-entity certificate MUST be integrity protected by COSE"
appears at lines 163, 198 and 261, each followed by> This can, for example, be done by
and a list of three mechanisms, **none mandated**; and at line 463 in a
conditional form whose condition is a CA practice statement the message does
not carry. The property is about the whole COSE object, so a validator holding
one header cannot decide it. Four requirement entries, four locators, one
obligation, zero checkable rules.

**D-2. §2 contradicts itself about whether the `x5u` URI needs protection.**
Lines 264–267: *"As the end-entity certificate is integrity protected by COSE,
the URI does not need to provide any protection."* Lines 269–274 then make
trusting a non-chaining retrieved certificate conditional on the URI providing
*"integrity protection and server authentication"*. Reconcilable only by
reading the first as about the end-entity certificate and the second as about
trust anchors, which the text does not say.

**D-3. §5's last two paragraphs contradict each other** (§2.1). No erratum
covers it; the errata search returned none for this RFC.

**D-4. `hashValue` has no length rule** (V-0008). `[-16, h'']` conforms, and an
empty expected digest matches every certificate.

**D-5. The `hashAlg` `tstr` branch is unreachable.** §2 admits *"an integer or
a string"*; the COSE Algorithms registry holds no text identifier for any hash
algorithm, so half the declared type is dead on arrival and stays in the
grammar.

**D-6. §4.3 defines its content as a CBOR sequence and cites RFC 8742 zero
times**, although RFC 8742 defines CBOR sequences and registers
`application/cbor-seq`. `see_also: rfc-8742` on the record records it.

**D-7. The registry `x5t` depends on is named without a reference** (§5). The
document gives a live IANA URL and no stable citation, and `rfc-9054` — which
populates it — appears in neither reference list.

**D-8. Two locations, and three COSE structures unaccounted for.** §2 names
`COSE_Signature`, `COSE_Sign1` and `COSE_recipient`. Whether these parameters
may appear in `COSE_Encrypt`, `COSE_Mac` or `COSE_Mac0` is undefined, and the
IANA registry carries no location column.

**D-9. Table 2's three rows pin each label to five algorithms, and §4.2's
registration text does not repeat the constraint.** A reader of the registry
sees the Algorithm column; a reader of §4.2 alone sees only "the new COSE
Header Algorithm parameters in Table 2".

**Nine defects, none repaired here.** `requirements.yaml` carries each in the
`note` of the entry it belongs to.

---
## 15. Open questions

1. **Does `DEC-003` want certificates at all?** Cut 1 says the DER cost is
   identical under every `DEC-002` option, so the question is not an encoding
   question. Until it is answered, `x5t`'s only role in our design is as the
   worked example of what a `KeyId` must not be.
2. **If we ever export a certificate-bearing COSE object, is `kid` mandatory in
   our profile?** §3 says it has to be, or the `KeyId` is unrecoverable. The
   rule is ours and it is not written anywhere yet.
3. **Which 64 bits does SHA-256/64 keep?** Not a question about this document,
   but it is in this lane and it bears on anything that accepts `−15`:
   `records/ietf/rfc-9054/distilled/examples/vectors.yaml` V-0003 computes both
   readings and they differ.
4. **Does anything of ours ever verify a digest it did not compute?**
   Condition (3) is violated the moment a verifier re-encodes an untrusted
   certificate to check an `x5t`. If the answer is "digest the received bytes
   verbatim, never re-encode", that is a rule we must state, because this
   document does not.
5. **Should the `(algorithm, label)` scoping precedent be lifted into
   `R-M-12`'s formulation?** §10 says it is the nearest ratified relative and
   not the same thing. Someone has to decide whether the difference matters.
6. **What is our deprecation path for a digest algorithm we have cited?**
   `rfc-9054`'s state-machine verdict is `NOT APPLICABLE` precisely because
   there is nothing to inherit: no deprecation state, no mechanism, no actor
   but "protocol maintainers and users". The policy is ours to write.

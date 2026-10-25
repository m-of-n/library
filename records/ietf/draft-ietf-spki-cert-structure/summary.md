---
schema: "library-summary/v1"
id: draft-ietf-spki-cert-structure
record: draft-ietf-spki-cert-structure
type: summary
updated: "2026-10-23"
---

# Simple Public Key Certificate

|  |  |
|---|---|
| **Type** | draft |
| **Maturity** | _unset._ An Internet-Draft that expired without reaching the RFC stream holds no RFC 2026 level. -06's Status section says it *"is intended to become a Proposed Standard RFC"*; intended, not reached. `maturity: draft` is left off on purpose, because the revision this record tracks is not in the IETF archive (next row). |
| **Authors** | C. Ellison (Intel), B. Frantz (Electric Communities), B. Lampson (Microsoft), R. Rivest (MIT LCS), B. Thomas (Southwestern Bell), T. Ylonen (SSH). Same six as -05 and as RFC 2693. Ellison's affiliation changed from CyberCash (-05) to Intel (-06). |
| **Published** | 26 July 1999 (-06). Expired 31 January 2000. Never published as an RFC. |
| **Identifier** | `draft-ietf-spki-cert-structure-06` · https://datatracker.ietf.org/doc/draft-ietf-spki-cert-structure/ |
| **Source** | https://theworld.com/~cme/spki.txt. This is the lead author's own copy: the file header and §"Expiration and File Name" both identify it as `-06`, and the server reports `Last-Modified: 30 Jan 2000`. |
| **Digest** | `6d3332d77a3b0231748dea94a22fa5876c191b51f5f789589024bb64b7397d15` (sha-256 of the plain text, retrieved 2026-10-23) |

## Which revision, and why

Under `docs/scope.md` §5 there is one record for the document line, tracking
its current version. **This record tracks -06 (26 July 1999)**, the last
revision of the line. The provenance is awkward and is recorded here so it is
not lost:

- **The IETF stops at -05.** Datatracker lists only `-05` (dated
  1998-03-16), and `https://www.ietf.org/archive/id/` serves -00 through -05.
  It returns 404 for -06. The IETF holds no copy of -06.
- **-06 still exists, and its authors cite it.** Rivest's own bibliography
  entry (`people.csail.mit.edu/rivest/pubs/EFLRx99a.bib.txt`) gives
  *"Internet-draft draft-ietf-spki-cert-structure-06.txt, July 26, 1999"*.
  -06's Status section says it *"supersedes the draft filed under the name
  draft-ietf-spki-cert-structure-05.txt"*. It is also the revision that was
  current when RFC 2692 and RFC 2693 were published in September 1999.
  Neither RFC cites the structure draft by file name.
- **-06 differs from -05 in ways the R-0006 questions turn on.** -05 §3.5
  only *recommends* transmitting canonical form: *"it is recommended that the
  canonical form be the form transmitted and stored in normal use"*. -06 §3.1
  makes it a requirement (below). -06 also adds the RFC 2119 boilerplate,
  §3.2.1 `<integer>`, RSA, DSA and ECDSA key-format sections (§3.8.1.1–§3.8.1.3), a
  restructured `<sig-val>` `(<pub-sig-alg-id> <sig-params>)` (-05's was a bare
  byte string for RSA and DSA) and sample signatures (§3.8.3.1–§3.8.3.2), a wrapped
  `(valid ...)` (§4.9) and `(online new-cert ...)` (§4.9.2). It also adds a
  display-type rule to range intersection (§8.3 rule 5).

**The -05 alternative.** -05 is the IETF-archived text, and mofn R-001 §5.5
cites `draft-ietf-spki-cert-structure-05`. Its plain text is at
`https://www.ietf.org/archive/id/draft-ietf-spki-cert-structure-05.txt`
(sha-256 `fc59ad04cc3e7846ae8e874132c62078f222c684ed0fa2ac7ced3f57d25029f1`,
retrieved 2026-10-23, not kept). R-001's claim that the wire format expired
and was never published is true of both revisions. Where this summary relies
on a -06 change, it says so.

## Overview

This is the SPKI working group's wire-format document, the "SDSI 2.0"
structures. The theory is in RFC 2693 and the requirements are in RFC 2692.
Every object is an S-expression whose first element names its type (§3, §3.8).
An **authorization certificate** `(cert ...)` carries version, display hint,
issuer, issuer-info, subject, subject-info, `(propagate)`, `(tag ...)`,
`(valid ...)` and comment (§4). A **name certificate** reuses the same
`cert` type with an `(issuer (name <principal> <byte-string>))` issuer and no
tag (§5.1). The prover hands the verifier a `(sequence ...)` of certs, keys,
signatures, online-test replies and `(do hash ...)` opcodes (§6.2). The
verifier combines those with its own unsigned `(acl ...)` (§6.1) and runs
5-tuple reduction (§8). Every hash and every signature is computed over the
**canonical S-expression** (§3.1, §3.5). That is a length-prefixed binary
encoding, defined in this document and later published alone as RFC 9804.

## The ∅ cells mofn R-0006 asked about

R-0006 `unverified.md` §5 lists two SPKI cells this record was opened to
fill. They feed report §2.2, the mechanism frame.

### 1. The to-be-signed construction

- **The signed object is the canonical S-expression of the whole
  `(cert ...)` object.** §3.1 says the canonical form *"is used as the input
  to all hash and signature functions"*. §3.5: *"The canonical S-expression
  is the form which is hashed for both generating and verifying
  signatures."* No field is cut out, and no to-be-signed wrapper is built
  around the object. Contrast COSE's `Sig_structure` and DSSE's PAE.
- **The signature is detached and refers to the object by hash.** §3.8.3
  defines `(signature <hash> <principal> <sig-val>)`, where `<hash>` is
  `(hash <hash-alg-name> <hash-value> <uris>?)` (§3.8.2). A signature
  *"typically follows that <cert> object in a <sequence>"* (§3.8.3). §6.2
  ties the two together only by position: *"we assume that <signature> does
  double duty, calling for the hash of the preceding item"*. An explicit
  `(do hash <alg>)` op may come first.
- **What `<sig-val>` is computed over is not stated.** §3.8.3.1 defines the
  shape, `(<pub-sig-alg-id> <sig-params>)`: one integer for RSA, `(r ..)
  (s ..)` for DSA. Neither revision says whether the signature primitive takes
  the hash value, the canonical bytes of the `(hash ...)` object, or the
  certificate bytes. The §3.8.3.2 sample signatures do not settle it either,
  because the object they sign is never shown. The hash algorithm is named in
  two places that can disagree: in `<hash>` (`md5` | `sha1` | URI, §9.2) and
  inside `<pub-sig-alg-id>` (`rsa-pkcs1-md5`, `rsa-pkcs1-sha1`, `dsa-sha1`,
  §9.2). -05's Status section says the WG was still weighing *"the proper
  place to bind hash algorithm choice"*. -06 does not resolve that.
- **Canonical, advanced and transport.** The canonical form is
  `<decimal>:<bytes>` byte strings plus `()[]`, with no leading zeros on
  lengths (§3.1, §3.2). The **advanced** form (bare tokens, quoted strings,
  `#hex#`, `|base64|`, free white space) is for reading. Its features *"are
  not part of the canonical form"*, and its white space is *"ignored on
  conversion to canonical form"* (§3.6). For 7-bit channels the canonical
  bytes go inside `{base64}` braces (§3.1, §3.4). That is a wrapper that
  decodes back to the same bytes, not a re-encoding.
- **Must a verifier re-canonicalise? Not if the producer obeyed §3.1.** -06
  §3.1: *"All SPKI structures communicated from one machine to another must be
  in canonical form."* The verifier can then hash the bytes it received. But
  nothing tells the verifier to hash the received bytes *rather than*
  re-serialise its parse. §3.5 leaves it optional: *"The implementer may wish
  to keep the canonical form around, alongside any parsed version"*. Nothing
  obliges a consumer to reject input that is not canonical.
- **Canonical is syntactic, not semantic.** §3.1 says canonical form is
  *"a unique representation of an S-expression"*. But `<cert>` *"is sub-type
  based so the parameter fields may be in any order, but the BNF suggests a
  fixed order"* (§3.8). So one certificate content has several valid
  canonical encodings and several hashes. A cert is identified, and revoked,
  by the hash of the bytes its issuer produced (`(canceled <hash>*)` in §7.1;
  `(object-hash ..)` in §4.5.1), not by its content. §3.2.1 leaves a second
  gap in integers: a sign byte may be needed, *"but redundant bytes of sign
  need not be"*. Redundant sign bytes are therefore not forbidden.

Against R-0006 §3.2's six conditions, as we read it:

1. **Injective:** yes over S-expressions; no over certificate content,
   because of free field order and integer sign padding.
2. **Decoder rejects non-canonical input:** absent.
3. **Canonicalise once, at authoring:** required of the transmitter by
   -06 §3.1. Not forbidden to the verifier.
4. **Authenticated type indicator:** partly. The leading `cert`, and an
   optional `(version ..)` (§4.1), are inside the hash. The encoding profile
   and the hash algorithm are not; the hash algorithm is named in the detached
   `<signature>`.
5. **Canonical order for sets:** none for `(* set ...)`, for `k-of-n`
   subjects or for cert fields.
6. **Unicode normalisation:** none. Byte strings *"can use any character
   set encoding desired"*. A display type signals the encoding, and equality
   is bytewise including that display type (§3.2).

### 2. Which fields of a signed SPKI object are authenticated

**Inside the hash:** everything in the `(cert ...)` list. That covers
`(version)`, `(display)`, `(issuer)`, `(issuer-info)`, `(subject)`,
`(subject-info)`, `(propagate)`, `(tag)`, `(valid)` including every
`(online ...)` test spec, and `(comment)`. It also covers each byte string's
`[display-type]` (§3.2: the display type *"is considered part of the string
for any equality comparisons or hashing"*).

**Authenticated but not reduced.** Only issuer, subject, propagate, tag and
validity feed the 5-tuple (§8.1). `(display)` is authenticated, yet *"For
verifiers of certificates, this field is treated as a comment"* (§4.2).
`(comment)` is *"meant to be ignored by any processing code"* (§4.10). The
`issuer-info` and `subject-info` URIs are location hints (§4.4, §4.6). A
byte-string display type is *not* inert. It changes equality (§3.2), and -06
§8.3 rule 5 makes a range comparison across unequal display types empty.

**Outside the hash:**
- the `(signature ...)` object itself: its `<hash>` (algorithm name and URIs),
  the signer `<principal>` and `<sig-val>`;
- the `(sequence ...)` wrapper, the order of its elements, and its
  `(do ...)` ops (§6.2);
- online-test replies, `(crl)`, `(delta-crl)` and `(reval)`. These are
  separate objects that must be signed by the principal named in the
  `(online ...)` spec (§7.1, §7.2).

**Signer and issuer are not tied by a stated rule.** The Glossary defines
ISSUER as *"the signer of a certificate and the source of empowerment"* (§2).
No step says a verifier must check that the `<signature>`'s `<principal>`
matches the `(cert ...)`'s `(issuer ...)`, nor that the `<signature>`'s hash
equals the hash of the preceding object. For a name certificate, *"the
certificate issuer <principal> is taken from the (name..) structure"* (§5.1).

### Sequences, reduction and tags (pointers only)

- **Sequence (§6.2):** an ordered sequence of objects the verifier is to
  consider when deciding to grant access; the prover assembles it (§7). The only opcode defined is `hash`.
- **5-tuple reduction (§8):** the §8.2 rule is `<i1,s1,d1,a1,v1> +
  <i2,s2,d2,a2,v2>` ⇒ `<i1,s2,d2,a,v>` when `s1 = i2` and `d1 = "t"`. It is
  RFC 2693 §6.3 restated. See also `rfc-2693` §6.1 (5-tuple), §6.3.1
  (AIntersect), §6.3.2 (VIntersect) and §6.3.3 (threshold). §8 defers the reduction code
  (*"A separate document will give the 5-tuple reduction code"*), and §8.4
  defers the full K-of-N algorithm the same way. `rfc-2693/distilled/` holds the extracted reduction
  model.
- **Tags (§4.8, §8.3, §9.2):** `(tag (*))` means all permissions. Tags are
  positional, and adding a trailing field restricts them. `*`-forms are
  `set`, `prefix` and `range`, with orderings `alpha | numeric | time |
  binary | date` (§9.2 `<range-ordering>`). This is the concrete grammar
  behind RFC 2693's tag algebra. Tag semantics belong to `rfc-2693` and
  DEC-004, which this record does not re-argue.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | It defines what an SPKI signature covers: the whole canonical `cert` object, with a detached signature joined by hash and position. It also defines what it leaves out (the signature object, the sequence, the signer/issuer check). |
| Cryptography | adjacent | Names algorithms (`rsa-pkcs1-md5`, `rsa-pkcs1-sha1`, `dsa-sha1`, `md5`, `sha1`; §9.2) and key formats. It does not specify what the signature primitive is applied to, and its ECDSA format is an editor's placeholder (§3.8.1.3). |
| This project | adjacent | Prior art for the closest peer named in `ARCH-0001` §6. Not a candidate encoding in its own right: DEC-002 option 1 is carried by `rfc-9804`. |

Bears on:
- **DEC-002.** This is the certificate profile that option 1's S-expressions
  were built for, and it shows what that profile actually fixed and what it
  left open (conditions above).
- **R-O-05**, proposed in `ARCH-0001-PROPOSAL-v0.2.0`, not accepted. -06 §3.1
  is a precedent, from an unratified draft, for its first half: the
  transmitted form *is* the canonical form. That is RFC 2692's *"A
  certificate should be signed exactly as it is transmitted"* honoured by the
  WG's own wire draft. R-0006 §2.3 reads RFC 9804 as SPKI reversing that
  requirement. Read against this record, the reversal is RFC 9804's, not the
  working group's. -06 still lacks R-O-05's verify-before-decode and
  no-canonicalise-during-verification clauses.
- **R-O-03:** it cites [SEXP] for its S-expression technology (§3) and then
  defines the canonical form itself (§3.1).
- **R-O-01:** the issuer is a `<principal>`, meaning `<pub-key>` or
  `<hash-of-key>` (§4.3).
- **R-M-04:** a counter-example on the wire. Name and authorization
  certificates are both `(cert ...)` and are told apart only by the shape of
  `issuer` and the missing `tag` (§5.1).
- **R-M-06:** `(k-of-n <k-val> <n-val> <subj-obj>*)` as a subject (§4.5.3).
  There is no CA hierarchy, and the reduction is deferred (§8.4).

## Implementations

Searched 2026-10-23. Nothing current implements this draft as a certificate
system. What survives is the S-expression layer: GnuPG/libgcrypt and Nettle
use S-expressions for key storage (see `rfc-9804`), not for SPKI
certificates.

| Name | Kind | License | URL |
|---|---|---|---|
| JSDSI | Java, SPKI/SDSI provider; last release 2005 | not checked | https://jsdsi.sourceforge.net/ |
| Inferno OS `spki.m` | Limbo module in the Inferno source tree; a 9front copy adds sequence verification | not checked | https://src.rcs.uwaterloo.ca/xref/inferno-os/module/spki.m |
| libspki (N. Möller) | C; announced 2003, no current release | not checked | https://lists.gnupg.org/pipermail/gcrypt-devel/2003-March/000254.html |
| MIT SDSI/SPKI 2.0 distribution | reference code; archival | not checked | https://toc.csail.mit.edu/node/213 |

We did not check which revision (-05 or -06) each of these tracks. The
differences listed under "Which revision" (`sig-val` shape, the `(valid ..)`
wrapper) would make one revision's certificates fail to parse under a strict
reader of the other.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, revision choice, digest, relations, `bears_on`, implementations |
| `summary.md` | this document |

**No `distilled/`, and none is owed by this pass.** This pass (library#87)
claims the **summary bar**: `status: summarized`, no `distillation` block,
nothing added under `distilled/`, so FX-1 does not fire. The record's type is
`draft`, so a full FX-1 extraction is still owed eventually. It is owned by
library#89. That extraction has to handle two
things a summary cannot: the §9.2 BNF against the prose sections (the
defects below), and a stated choice of revision for `normative.md`. -06 has
no IETF-archived copy and -05 has no RFC 2119 boilerplate at all.

**No `versions/`.** The -05 alternative is described above with its URL and
digest. Its bytes and metadata were not kept as a version directory, because
nothing yet cites -05's text in a way that differs from -06 on a point the
library uses.

**No verbatim normative text beyond short, locator-bearing quotes.** Under
FX-1 that text belongs in `distilled/normative.md`.

## Limits

1. **It does not say what is signed at the primitive level** (§3.8.3.1).
   This is the gap that matters most for the R-0006 frame. "The canonical
   form is hashed" is stated. "The signature is over X" is not.
2. **No verifier procedure.** Hash matching, signer/issuer equality and
   decode-versus-verify ordering are all left implicit (§3.8.3, §6.2). The
   reduction code and the threshold algorithm are deferred to a separate
   document (§8, §8.4); this library holds no such document.
3. **It is a working draft, with visible scaffolding.** -06 carries editors'
   placeholders at §3.8.1.3 (ECDSA) and at the head of §7 (*"should I have an
   ID for a CRL or reval thread or let the public key signing the instrument
   be the ID for it?"*). The section numbering jumps from §8.4 to §8.7.
4. **The RFC 2119 boilerplate is declared and then not used.** -06's Status
   section imports RFC 2119. The text never uses an upper-case keyword, and
   its obligations are lower-case: §3.1 *"must be in canonical form"*, §4.1
   *"must be ignored"*, §7.1 and §7.2 *"must be signed"*. How much weight
   these carry is a reading, not a given.
5. **The BNF and the prose disagree in several places** (our reading,
   recorded rather than repaired):
   - §4.1 makes `<version>` an `<integer>` while the prose says *"Version
     numbers are alphanumeric strings"* and gives `(version "0")`.
   - §4.9 wraps `(valid ...)`, but the §5.3 examples use a bare
     `(not-after ...)`.
   - §4.9.2's `<online-test>` (with `<online-id>` and `new-cert`) is not
     the one in §9.2.
   - §7.2 defines `<reval>` with `(valid <hash>+)`, while §7.3 redefines it
     with `<subj-hash>`.
   - §9.2's `<dsa-sig-val>` uses `dsa-sha1-sig`, but the §3.8.3.2 sample
     uses `dsa-sha1`.
   - §8.1 uses `<threshold-subj>` and `<tag-body>`, and §9.2's `<subject5>`
     uses `<fq-name5>`; none of the three is defined.
6. **K-of-N, as written, excludes N-of-N.** §4.5.3 states the constraint
   *"where K < N"*, but its own example 4, an off-line and an online issuer
   where delegation *"could require both"*, is a 2-of-2. R-M-06 should not inherit
   the strict inequality by accident.
7. **Provenance of -06.** The tracked bytes come from an author's personal
   host, not an IETF repository. The digest pins what was read on 2026-10-23.
   If that host disappears, the -05 archive copy is the fallback, and the
   differences listed under "Which revision" then apply.
8. **Read scope:** the whole of -06 (2,622 lines) was read, and -05 was read
   in full for the revision comparison. The key-format detail (the
   §3.8.1.1–§3.8.1.2 base64 blobs) was not checked for correctness.

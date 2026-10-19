---
record: rfc-9679
kind: index
title: "rfc-9679 — distilled artifacts"
extracted: "2026-10-18"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

**State: passes 1 and 2 of 3 complete.** The extract pass ran at effort max,
agents in parallel, each reading only `.cache/rfc-9679.txt`; the verify pass
then re-derived every count, quotation, locator and fixture from the source
independently. **The cross-check pass has NOT run**, so this record carries no
`profile`. Readable; nothing may be built on it. library#39 owns finishing it.

Source: RFC 9679, *COSE Key Thumbprint*.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 93 verbatim prose runs and 19 fenced blocks (byte-exact source lines, three-space RFC margin retained), §2–§8 in source order. §1, §9, Acknowledgements, Authors' Addresses and front matter dropped and stated as dropped |
| requirements | `requirements.yaml` | 68 entries, `R-0001`–`R-0068`, source order, no gaps: 66 `stated`, 2 `inferred`. Only 13 carry a BCP 14 verb; 55 are `verb: none` because the binding content — the three procedure steps, all five required-parameter lists, the exclusion rule, the ordering statements, the registration values — is stated in lowercase. 5 entries are `testable: no` (`R-0021`, `R-0035`, `R-0039`, `R-0059`, `R-0064`), each with a reason |
| schema | `schema/` | 3 derived, 0 verbatim: a CDDL of the thumbprint input (6 rules), the §3 procedure and §4 label table as JSON data, and a JSON Schema 2020-12 with five `oneOf` branches for §4.1–§4.5. **The source ships no formal grammar at all**, so every formal artifact here is ours and is named `.derived.` |
| messages | `messages.yaml` | 9 structures, 29 fields, every field carrying a non-empty `constrained_by`; 47 of the 68 requirements are wired. The 21 unwired are enumerated with a reason each, so an adversarial reader can falsify the claim cheaply |
| examples | `examples/` | 13 vectors. **Every printed value in the document reproduces** — recomputed with a hand-written RFC 8949 §4.2.1 encoder plus `hashlib`, no CBOR or COSE library. 5 of 13 are the source's (`V-0008`–`V-0012`); 8 are `source: constructed`, each with a `constructed_why`, because RFC 9679 prints exactly one complete computation and every other printed value descends from it |
| design-notes | `design-notes.md` | the per-key-type hashed set; an ADAPT verdict on RFC 9679 as `KeyId` with three blockers, two of them ours; the `alg` hazard adjudicated; and nine named cuts against MD-3 |

## Not applicable

- **protocol** — RFC 9679 defines a computation, a value, one CWT claim member
  and one URI. §5.6 *names* three roles ("the issuer of a CWT declares that the
  presenter possesses a particular key and that the recipient can
  cryptographically confirm …"), but defines no message, no ordering and no
  error path: that flow belongs to RFC 8747, and the key-resolution step is
  expressly assumed away — "This approach assumes that the recipient is able to
  obtain the identified COSE Key using the thumbprint contained in the "ckt"
  member." Modelling it here would be extracting a different document. The only
  other multi-party sentence is a precondition, not an exchange: "it is crucial
  that they know and use the same hash function to ensure consistent results."
- **state-machine** — no lifecycle. A thumbprint is a pure function of a key:
  "Including only the required parameters ensures that the COSE Key Thumbprint
  remains consistent for a given key, regardless of any additional attributes."
  No registration, issuance, rotation, revocation or expiry appears anywhere.
  The nearest thing is a one-shot validity predicate on the URI form, which is
  an accept/reject test rather than a lifecycle.

## What actually enters the digest

The complete hashed set per key type — §4 admits these and nothing else:

| `kty` | value | labels, in encoded order |
|---|---|---|
| OKP | 1 | `1` kty, `-1` crv, `-2` x |
| EC2 | 2 | `1` kty, `-1` crv, `-2` x, `-3` y |
| RSA | 3 | `1` kty, `-1` n, `-2` e |
| Symmetric | 4 | `1` kty, `-1` k |
| HSS-LMS | 5 | `1` kty, `-1` pub |

For P-256 the wire form is `a4 01 02 20 <crv> 21 58 20 <32B x> 22 58 20 <32B y>`
— 75 octets, and the §6 worked example reproduces from it exactly.

**`alg` is not in it. The COSE Key parameter `alg` is never named anywhere in
the document**: `alg` occurs as a bare word zero times and as `"alg"` zero
times, and its only six occurrences in the 627 lines are inside the words
"algorithm" and "algorithms" (§3 once each, §5.7 four times), none of which
names a key parameter. `AKP` is absent outright — zero occurrences, case
-insensitively. *(Corrected by the verify pass: pass 1 wrote "the string `alg`
occurs zero times", which `grep -c alg` falsifies in one command. The claim that
survives is the one about the parameter, and it is the load-bearing one.)* What
makes a `KeyId` move is therefore *not* the algorithm, in this document. Two
things do:

- **The hash function.** H is chosen by the application and is **not carried in
  the value**. Change H and every `KeyId` changes silently; two parties on
  different H never match on any key and cannot tell why. Only the §5.7 URI
  form names H. Adopting this as `KeyId` means pinning H ourselves and choosing
  between the bare digest and the self-describing URI — materially different
  failure modes.
- **§4.6's delegation.** The required set is per-key-type and open-ended. For
  AKP — defined in RFC 9964, a document RFC 9679 never cites — `alg` *is*
  required and therefore *is* inside the digest, so one `pub` under ML-DSA-44
  and -65 gives different thumbprints. That is where the post-quantum hazard
  enters, and it enters by delegation rather than from anything RFC 9679 says.

Also worth stating plainly: a private key and its public key produce the **same**
`KeyId` (`d` is not required for OKP, EC2 or RSA), and a Symmetric thumbprint is
a digest of a known four-byte prefix over the secret — which is why §7 carries
one MUST and two MUST NOTs about that one field.

## Source defects found

Reported, never repaired:

1. **RSA `n` and `e` have no normalisation that RFC 9679 either states or
   cites.** §4.3 gives both as bare `bstr` and says nothing about leading zero
   octets or width; unlike §4.1 and §4.2, which both end "Further details are
   described in Section 7.1 of [RFC9053]", §4.3 cites no defining specification
   at all — and neither do §4.4 or §4.5. So, reading only the documents RFC 9679
   names, 65537 as `h'010001'` and `h'00010001'` are two thumbprints for one key,
   which collides head-on with §7's own precondition: "A COSE Key Thumbprint will
   only uniquely identify a particular key if a single unambiguous COSE Key
   representation for that key is defined and used".

   **[corrected by the verify pass]** Pass 1 wrote that "RFC 8230 §4 does not
   close it either". That is **false**, and it was asserted against a document
   this record had not fetched. RFC 8230 §4 closes it exactly: "All numeric key
   parameters are encoded in an unsigned big-endian representation as an octet
   sequence using the CBOR byte string type (major type 2). The octet sequence
   MUST utilize the minimum number of octets needed to represent the value."
   Under that rule `h'00010001'` is non-conforming and only `h'010001'` is
   admissible, so the ambiguity is **resolvable**. The defect that survives is
   narrower and still real: **RFC 9679 never cites RFC 8230 — zero occurrences
   in the whole document** — and §4.6's "consult the defining specification"
   clause is written for key types *other* than the five §4.1–§4.5 enumerates.
   An implementer who follows RFC 9679 and its own reference list has no
   leading-octet rule for RSA; one who independently knows RFC 8230 does. The
   consequence for us is unchanged — anything we build on this must pin a
   normalisation and cite it — but the citation now exists and is RFC 8230 §4.
   `V-0003` therefore remains `expect: ambiguous` *against RFC 9679*, not
   against COSE as a whole.
2. **The §6 full example key is not in deterministic-encoding order** — printed
   with `kid` last, where RFC 8949 §4.2.1 puts label 2 second. Not
   non-conformance, since the input key is unconstrained, but a
   determinism-dependent specification labels a non-deterministic encoding "the
   following CBOR encoding" and switches regime silently between two adjacent
   hex blocks. Not in the errata. It is also the clearest proof that step 1
   **re-encodes** rather than filtering a received encoding in place.
3. **The `ckt` registration pins SHA-256 while §3 does not.** §8 registers "COSE
   Key SHA-256 Thumbprint", but §3 requires only that SHA-256 be *supported* and
   permits others, and the member is a bare binary string with nowhere to name
   H. A SHA-384 `ckt` is indistinguishable on the wire from a SHA-256 one.
4. **§5.5 misattributes both of its cross-references** — the `ckt` to "Section 7
   of [RFC9052]" (which defines `COSE_Key` and never mentions `ckt`, a member
   *this* document defines) and the `jkt` to "Section 4 of [RFC7517]" (which
   lists JWK parameters; `jkt` is RFC 7638, and the confirmation member is
   RFC 9449 §6.1). Both legs checked against the documents themselves by the
   verify pass: RFC 9052 §7 is "Key Objects" and `ckt` appears nowhere in this
   library's own full extraction of it, while RFC 9679 §8 registers `ckt` with
   "Specification Document(s): RFC 9679"; RFC 7517 §4 is "JSON Web Key (JWK)
   Format" with §4.1–§4.9 enumerating `kty`, `use`, `key_ops`, `alg`, `kid`,
   `x5u`, `x5c`, `x5t` and `x5t#S256`, and the string `jkt` occurs **zero**
   times in the whole of RFC 7517; `jkt` is defined as a confirmation member in
   RFC 9449 §6.1, "JWK Thumbprint Confirmation Method". RFC 9679's own
   reference list titles [RFC7638] "JSON Web Key (JWK) Thumbprint" and its
   Acknowledgements thank that document's authors "for their work on the JWK
   Thumbprint specification", so the document contradicts its own §5.5.
5. §4.1 labels its own columns differently from §4.2–§4.5 — `value: int` where
   every other subsection writes `data type:`.
6. **No defined thumbprint discriminates §4.2.1 from §4.2.3 map ordering.**
   Across all five key types every required label lies in −24..23 and encodes in
   one octet, so bytewise and length-first order coincide. An implementation can
   get §4.2.1's sorting wrong and pass every value the document prints.
7. Minor: §6 reads "with **link** breaks added for display purposes only."

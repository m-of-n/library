---
schema: "library-summary/v1"
id: rfc-8742
record: rfc-8742
type: summary
updated: "2026-10-20"
---

# Concise Binary Object Representation (CBOR) Sequences

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | standard — Standards Track |
| **Authors** | C. Bormann |
| **Published** | February 2020 |
| **Identifier** | RFC 8742 · DOI 10.17487/RFC8742 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8742.txt |
| **Digest** | `4462966836b60f42ebae9b5f1d2a479c328e16f0380a3434311a083bccbce30e` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

RFC 8742 is the claim that a container is unnecessary. Concatenate encoded CBOR
data items and the bytes *are* a CBOR Sequence: §2's recursive definition has
exactly two cases, "an empty (zero-length) sequence of bytes" and one encoded
data item followed by a sequence. No separator, no length prefix, no
terminator — and §2 gives the reason the marker JSON Text Sequences need is
unnecessary here, that CBOR items "are self delimiting and the end can always
be calculated."

What it registers (§6) is **three out-of-band labels and no CBOR tag**: the
media type `application/cbor-seq`, CoAP Content-Format ID 63, and the
`+cbor-seq` structured syntax suffix. The whole document carries **four** BCP 14
keywords (`bin/bcp14-count`), and §2 — the entire format — contains none of
them.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Encoding | **core** | DEC-002 asks what our native encoding is; this is the only ratified answer to "and how do two of them share one file". MD-3's option 5 names no container, so this is option 5's container by default. |
| Security | supporting | §5 is three sentences, and one of them is the only statement in our reference set about what per-element COSE does *not* bind. |
| Naming | supporting | §6 registers a media type, a content-format number and a suffix — three labels, all out of band. The *absence* of a tag is the datum, and it belongs to `R-M-12`. |

**The finding to act on: a CBOR Sequence cannot tell you it is complete, and §2
says so three times.** First, "There is no end-of-sequence indicator." Second,
the format "can reliably detect truncation of the bytes making up the last CBOR
data item in the sequence, but it cannot detect entirely missing CBOR data items
at the end." Third, the empty byte sequence is itself a valid CBOR Sequence,
decoding to zero values. Together: **truncating an append-only log at an item
boundary is in-spec and undetectable**, and a log truncated to nothing is a
valid empty log.

§5 closes the escape route rather than opening one. COSE "protections can be
applied to an entire CBOR Sequence or to each of the elements of the sequence
independently; in the latter case, additional effort may be required if there is
a need to protect the relationship of the elements in the sequence." Option 5's
export story is per-statement `COSE_Sign1`, which is the latter case. So an
exported bundle of *n* signed statements is *n* facts and no fact about the
bundle: nothing binds the count, nothing binds the order, and under `R-O-01` the
sequence has no issuer key at all, because the sequence is not a signed object.
The fix is one sentence in the export profile — a count, a chain, or a root,
inside the signed bytes — and **nothing in RFC 8742 supplies it or asks for
it**. Its one MUST (§5) is "decoders MUST fail gracefully in the face of
malicious inputs", which is about not crashing.

One corrupt entry also costs the tail, not just the entry: §2, "if any data item
in the sequence is not well formed, it is not possible to reliably decode the
rest of the sequence."

**§4.3 is the mitigation, and it is already in our vocabulary.** Wrap each
element in a byte string — `my-element = bytes .cbor my-element-structure` — and
the sequence becomes skippable without decoding, fannable out to parallel
decoders, and partially recoverable: "within limits, this may also enable
recovering from elements that internally are not well formed; the limitation is
that the sequence of byte strings does need to be well formed as such." That is
tag 24's pattern with the tag removed, which is the move `rfc-8949`'s design
notes already record option 5 making for its signed payload. It costs one
byte-string head per entry, and it has to be *chosen*: nothing in option 5
chooses it.

**The distinction that is easy to blur, and the registry blurs it anyway.**
All three of §6's registrations are *out of band* — a media type in a header or
a file's metadata, a CoAP Content-Format number in a CoAP option, a suffix in a
media-type name. None of them appears in the encoded bytes, and §6.1's own
template says so in two fields: **"Magic number(s): N/A"** and "File
extension(s): N/A". A CBOR tag would be in the bytes; RFC 8742 asks for none.
Meanwhile the IANA **CBOR Tags** registry does carry tag **63** with semantics
"Encoded CBOR Sequence RFC 8742" — and its Reference column reads
`draft-bormann-cbor-notable-tags-02, Section 2.1` (`iana-cbor-tags`,
`distilled/tables.yaml`). The matching numeral is a coincidence across two
registries: CoAP Content-Format 63 (§6.2, Table 1) and CBOR tag 63 are different
namespaces. So the tag registry attributes a code point to this RFC, in a prose
semantics field, for an allocation this RFC never requested and an individual
draft made. For the registry-reduction argument that is the **governance** half
of `R-M-12` and not the encoding half: option 5 pays nothing for RFC 8742's own
registrations, and the ecosystem minted a tag for the concept anyway, from
outside the RFC process.

## Where it cuts against MD-3

MD-3 (2026-09-28) narrowed DEC-002 to option 5 — "reduced CBOR, no IANA tags,
COSE export only" — and a narrowing is not an acceptance; no DEC-002 ADR exists.
Three cuts, each naming an option.

**Cut 1 — option 5 inherits this container by inertia, and option 3 recovers
from a corrupt entry where option 5 does not.** On the letter of option 5's
exclusion list (reliance on the IANA CBOR Tags registry, and native use of COSE
header parameters) a CBOR Sequence is *admissible*: zero tags, zero header
parameters. That admissibility is exactly why it will become the container
nobody chose. Its cost is the completeness hole above, and DEC-002 option 3's
JSON lineage does not pay it the same way — §2 declines the framing RFC 7464
uses, "CBOR Sequences, unlike JSON Text Sequences [RFC7464], do not use a marker
between items", and that marker is what makes **resynchronisation after a
malformed item** possible. Neither format detects a dropped tail; only the CBOR
one loses the whole tail to one bad entry. On a ground DEC-002's drivers never
list — library availability, SCITT alignment, SPKI fidelity, human debug — that
is a durability argument for option 3, and §4.3's byte-string wrapper is option
5's answer to it.

**Cut 2 — CDDL cannot express the container, so our schema cannot either.**
§4.1: "Currently, CDDL does not provide for unadorned CBOR Sequences as a
top-level subject of a specification." The suggestion is to write an array rule
and "add English text that explains that the specification is really about a
CBOR Sequence with the elements of the array". `.cborseq` (RFC 8610 §3.8.4)
reaches only *inside* a byte string, so it cannot describe the file. §4.2 says
diagnostic notation has the same hole, with the same workaround — "it is also
possible to leave off the outer brackets for this array" — so the fixtures
cannot be written honestly either. A multi-statement file's top-level rule is
therefore an array that is not an array, corrected by a comment. Under
`R-O-03`'s discipline — cited, not invented silently — an English-prose
container is the weakest citation available, and there is nothing here for a
lint rule to target. **This cost is shared by option 2 and option 5 and paid by
neither option 1 nor option 3:** a canonical S-expression file and a JSON text
sequence each have a grammar for the whole file.

**Cut 3 — and running the other way, §2 names the fix, and the fix is tag-free.**
"(If one is desired, CBOR encoding an array of the CBOR data model values being
encoded, employing either a definite or an indefinite length encoding, as a
single CBOR data item may actually be the more appropriate representation.)" A
definite-length array head states *n*, is self-delimiting, and uses no tag — so
it is as option-5-compliant as the sequence is. **That settles a question, and
it is not a DEC-002 question: a finished signed export should be an array, and
the sequence buys exactly one thing — incremental append — which is the same
thing that makes the count unstateable.** A signed export and an append-only log
are two artifacts, and option 5 currently names neither. One sentence of ADR
work, and the document wrote it for us. The indefinite-length variant §2 also
offers would hand the problem back (no count in the head) and is excluded
anyway by every deterministic profile this library holds.

## Implementations

RFC 8742 names none and has no implementation-status section. Two of the
libraries already recorded on `rfc-8949` carry sequence support, which is the
only deployment evidence we hold:

| Name | Kind | License | URL |
|---|---|---|---|
| fxamacker/cbor | Go library | MIT | https://github.com/fxamacker/cbor |
| libcbor | C99 library | MIT | https://github.com/PJK/libcbor |

`fxamacker/cbor` is recorded as "RFC 8949 + RFC 8742"; `libcbor` as "C99, RFC
8949 compliant, CBOR Sequences. Runs the CBOR WG test vectors in CI." *Searched
the document on 2026-10-20 for a named implementation: none, and none for the
`+cbor-seq` suffix either.* The §6.2 CoAP Content-Format allocation is the
document's only evidence of deployment interest, and an allocation is not a
deployment.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata — `bears_on: DEC-002`, five typed `see_also` edges, each commented |
| `summary.md` | this document |
| `summary.html` | GENERATED and untracked — `bin/render-html` builds it beside the source (`docs/generated-views.md`) |

The absences, and what would trigger each:

- **No `distilled/`, and no `distillation` block.** This record was summarised,
  not extracted: FX-1 fires on what a record says it was measured against, and
  this one claims no standard. The extraction would be cheap — four BCP 14
  keywords makes `requirements.yaml` a four-row file — but cheapness is not the
  reason to spend it. The reason would be Cut 2: the artifact worth having is a
  `schema/*.derived.cddl` top-level sequence rule that §4.1 says CDDL cannot
  write, and that file is derived by construction. **Trigger: a DEC-002 ADR that
  names a container.**
- **No test vectors, and that is the document's gap rather than ours.** It
  prints `[1, 2, 3]` and `1, 2, 3` in diagnostic notation (§4.2) and three CDDL
  fragments (§4.1, §4.3), and **not one hex octet**. For a specification whose
  whole content is a byte-layout claim there is nothing here to make a fixture
  from, so any conformance test for RFC 8742 is ours and has to be marked so.
- **No `contradicts` edge.** The tension with `rfc-9277` over concatenation is
  real and is stated on that record; it is a well-formedness-versus-interpretation
  difference rather than a disagreement, so asserting `contradicts` would
  overclaim.

## Limits

- **Normatively anchored on a superseded CBOR specification, and never
  updated.** §2 defines the sequence in terms of "an encoded CBOR data item
  [RFC7049]", and §5's security considerations and COSE reference are [RFC7049]
  and [RFC8152] — obsoleted by RFC 8949 ten months after this RFC, and by
  RFC 9052. The header carries no `Updates:` or `Obsoleted by:` line.
  Well-formedness did not change across the restatement, so the *format*
  survives intact; the *citation* does not, and under `R-O-03` citing RFC 8742
  drags two superseded documents in behind it. The library already models both
  edges (`rfc-8949 supersedes rfc-7049`, `rfc-9052 supersedes rfc-8152`), and
  the `see_also` edges here are what make the current specifications reachable
  from a document that names neither.
- **Four BCP 14 keywords, and not one of them constrains the format.**
  `bin/bcp14-count` returns 4, at §3 (SHOULD — when a media type should take the
  `+cbor-seq` suffix), §5 (MUST — fail gracefully) and §6.3 twice (SHOULD —
  fragment identifiers). §2 is entirely declarative. So nothing says a producer
  MUST NOT put anything between items, nothing says a consumer MUST read to end
  of input, and nothing about the container is testable. "We use RFC 8742" cites
  a definition, not a conformance target — which matters precisely because §4.1
  has already pushed our container's specification into prose.
- **§3's own test for the suffix is not decidable.** The suffix SHOULD be used
  where parsing as a sequence "is meaningful and is at least sometimes not just
  a single CBOR data item", with the parenthetical "(Without the qualification
  at the end, this sentence is trivially true for any +cbor media type, which of
  course should continue to use the "+cbor" structured syntax suffix.)" Whether
  a format qualifies turns on an unquantified "sometimes". It is the only conduct
  rule in the document aimed at a specification author and it has no decision
  procedure.
- **The zero-length case is acknowledged and left awkward.** §4.2: "Note that it
  is somewhat difficult to discuss zero-length CBOR Sequences in the latter
  form." It is valid, it has no notation, and it is indistinguishable from an
  empty file, a fully truncated file, and a file that was never written.
- **§6.1 asserts a section that does not exist**: "Interoperability
  considerations: Described herein." The nearest content is §2's truncation
  paragraph and §4.3's skipping advice, neither headed as interoperability.
- **Both of its stated gaps were marked temporary and neither has closed.**
  "Currently" (§4.1), "at this time" (§4.2), and "(Future versions of CDDL may
  provide a notation for top-level CBOR Sequences, e.g., by using a group as the
  top-level rule in a CDDL specification.)" Six years on, no record in this
  library closes it — and CDDL's live extension point is the control-operator
  registry, which is not where a top-level subject could be added.

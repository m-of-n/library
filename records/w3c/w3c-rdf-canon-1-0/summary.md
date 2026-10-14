---
schema: "library-summary/v1"
id: w3c-rdf-canon-1-0
record: w3c-rdf-canon-1-0
type: summary
updated: "2026-10-13"
---

# RDF Dataset Canonicalization (RDFC-1.0)

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` — W3C Recommendation, the W3C's terminal maturity level. The RFC 2026 ladder does not apply to W3C documents; this is a mapping, not a quotation. |
| **Authors** | Dave Longley (author). Editors: Dave Longley (Digital Bazaar), Gregg Kellogg, Dan Yamamoto. Former editor: Manu Sporny (Digital Bazaar) |
| **Published** | 2024-05-21 (W3C Recommendation; this version `REC-rdf-canon-20240521`) |
| **Identifier** | https://www.w3.org/TR/rdf-canon/ |
| **Source** | https://www.w3.org/TR/rdf-canon/ |
| **Digest** | `330eb4f00c5f12300e23cb7a7b979bdfc910890a41bfb87a93327d7b43161fd0` (re-verified 2026-10-13 against the live URL — unchanged) |

## Overview

RDFC-1.0 canonicalizes an RDF **dataset** — an unordered set of quads — in two
separable moves. First it manufactures stable identifiers for *blank nodes*,
which have no identity of their own, by hashing the information incident to
each one and, where that is not unique, the whole transitively connected
subgraph (§4.6, §4.7, §4.8). Second it serializes every quad in a fully
specified N-Quads layout (Appendix A), sorts those serializations into Unicode
code point order, and concatenates them (§5). The claim is that two datasets
yield the same output if and only if they are isomorphic (§4.4.1). It stops
deliberately short of use: "This specification does not define such a graph
signature" (§1.1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | adjacent | Defines no signature and no verification step. It does carry a named availability failure — §4.4.3 opens with a MUST to defend against denial of service, and §7.1 describes dataset poisoning. |
| Cryptography | adjacent | Hashing (SHA-256 by default, §4.1) is *internal* to blank-node labelling, not an output commitment. §7.2 notes no internal hash value is ever revealed. |
| This project | adjacent | Not a DEC-002 candidate and cannot become one: its input is an unordered set of triples, ours are tree-shaped statements. Held as **prior art** for the condition (5) ordering rule. |

Bears on **DEC-002** (as prior art, not as a candidate encoding), **DEC-004**
(a tag's value set is set-valued and needs the same rule) and **R-O-03**
(canonicalization algorithms SHALL be cited, not invented silently — this
record is one of the two citations available for the rule we must write).

**The finding, stated against the question library#56 asked.** Yes, RDFC-1.0 is
real prior art for condition (5) — a ratified, widely implemented algorithm for
canonically ordering a set, blank nodes and all. But the part that transfers to
us is one sentence, and the part that makes RDFC hard is a problem we do not
have.

What transfers is §5: *serialize each member into a canonical form that admits
exactly one representation, sort the serializations in code point order,
concatenate.* Appendix A supplies the element-level injectivity that makes the
sort meaningful — "each code point can be represented by only one of UCHAR,
ECHAR, or unencoded character" — and §5 supplies the order. That is precisely
the shape the condition (5) rule needs for `Threshold` members (ARCH-0001
§4.1), DEC-004 tag value sets and ARCH-0002 P4's schema set, and it is the same
construction as RFC 8949 §4.2.1's map-key rule — sort on the **encoded** form —
lifted from keys to set members.

What does not transfer is §4.6 through §4.8 — first-degree hashes, related
hashes, N-degree hashes, gossip paths, permutations. That machinery exists for
one reason: an RDF blank node has no identifier at all, so identity must be
*manufactured* from surrounding graph structure before anything can be sorted
(§1.1, §4.4.1). None of our set members are like that. A `Threshold` member is
a `Principal`, which bottoms out in a `Key` or a `KeyId`, and under R-M-02 a
key digest *is* the principal's name — self-contained and stable. A DEC-004 tag
value and a P4 schema are likewise self-identifying. We have no blank nodes,
therefore no graph-isomorphism problem, therefore no need for the expensive
half.

**The consequence worth having.** The topic answer's claim that no DEC-002
candidate supplies condition (5) is unchanged — RDFC is not a candidate and
this record does not make it one. What changes is the **R-O-03 cost of writing
the rule ourselves**. Before this reading, a bytewise ordering rule for
set-valued fields looked like a partly invented algorithm. It is not: its shape
is ratified twice over, by RFC 8949 §4.2.1 for map keys and by RDFC-1.0 §5 for
set members, the second with eleven interoperating implementations. We are
citing a construction, not inventing one, and that is the difference R-O-03
turns on. It also sharpens the case already recorded against DEC-002 option 3:
RFC 8785 §3.2.3 *prohibits* reordering array elements, and the thing it
prohibits is the thing another ratified W3C specification *mandates* for the
same purpose.

## Implementations

Eleven independent implementations, from the W3C implementation report
(https://w3c.github.io/rdf-canon/reports/, edition of 24 February 2026,
retrieved 2026-10-13), across nine languages and unaffiliated developers. Ten
of the eleven pass 86/86 of the RDFC-1.0 test suite; `RDF-URDNA` passes 84/86
and records why. This is a markedly healthier implementation picture than
rfc-8785's, where our own extraction found four of five verified
implementations living in one author's repository.

| Name | Kind | License | URL |
|---|---|---|---|
| Corese (Wimmics Team, INRIA) | Java | not checked | https://project.inria.fr/corese/ |
| YoucTagh RDF Canonicalization | Python | not checked | https://github.com/YoucTagh/rdf-canon |
| rdf-canonicalization-cpp (Digital Contract Design) | C++ | not checked | https://github.com/dcdpr/rdf-canonicalization-cpp |
| rdf-canonize (Digital Bazaar) | JavaScript | not checked | https://github.com/digitalbazaar/rdf-canonize |
| Titanium RDFC (Filip Kolarik) | Java | not checked | https://github.com/filip26/titanium-rdf-canon |
| Sophia (Pierre-Antoine Champin) | Rust | not checked | https://github.com/pchampin/sophia_rs |
| RDF-URDNA (Simon Greatrix) | Java | not checked | https://github.com/setl/rdf-urdna |
| zkp-ld/rdf-canon (Dan Yamamoto) | Rust | not checked | https://github.com/zkp-ld/rdf-canon |
| RDF.ex (Marcel Otto) | Elixir | not checked | https://rdf-elixir.dev/ |
| rdfjs-c14n (Ivan Herman) | TypeScript | not checked | https://iherman.github.io/rdfjs-c14n/ |
| Ruby RDF::Normalize (Gregg Kellogg) | Ruby | not checked | https://github.com/ruby-rdf/rdf-normalize |

**Licences are deliberately unfilled rather than guessed.** The W3C report
carries name, release, language, home page and conformance, and no licence
field; filling the column would mean opening eleven repositories, which this
record does not need, since we are borrowing a construction and not a
dependency. Searched 2026-10-13.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

**No `distilled/`, and none is owed.** This PR claims the **summary bar**
(`CONTRIBUTING` §4): the record is `summarized`, it declares no `distillation`
block and the PR touches no `distilled/`, so FX-1 does not fire. The judgement
behind that is not merely economy — RDFC-1.0 is not a DEC-002 candidate and
cannot become one, so there is no implementation of ours that would otherwise
have to re-read the source. **What would trigger an extraction** is a decision
to make RDFC's construction the *normative basis* of the condition (5) ordering
rule rather than one of two citations for its shape. The ordering steps would
then become text someone implements and tests, and would owe
`requirements.yaml` and `examples/` — the 86-case W3C test suite
(https://w3c.github.io/rdf-canon/tests/) is the ready-made fixture set. No
issue owns that today, because on the reading above it should not happen.

**No verbatim normative text here.** Under FX-1 that belongs in
`distilled/normative.md` with its locator; in a summary the rule is to cite the
§ and let the reader open the source, so the few quoted fragments above are
short and locator-bearing by design.

## Limits

1. **It defines no signature.** §1.1 says so outright. Everything about *how* a
   canonical form gets committed to is left to a caller — which is consistent
   with R-O-05's separation but means this document settles nothing about
   verification order.
2. **The canonical form is canonical only relative to a hash algorithm.** §7.2
   permits parameterizing the hash, and warns that doing so "will generally lead
   to different results"; the §1.1 note adds that any use case needing
   reproduction must "unequivocally express or communicate" the algorithm used.
   So the output is not self-describing. That is condition (4) — an
   authenticated profile indicator — reappearing *inside* a canonicalization
   algorithm, and it is independent support for R-O-05's type-indicator clause.
3. **Canonicalization is partial in practice.** §4.4.3 step 5.4 iterates over
   *every permutation* of a blank-node list sharing a hash; §4.4.3 opens with a
   MUST that implementations defend against denial of service "by raising
   suitable exceptions and terminating early"; §7.1 names dataset poisoning.
   A conforming implementation may therefore refuse to canonicalize a valid
   input. An ordering rule for our set-valued fields inherits none of this, and
   that is a direct consequence of having no blank nodes.
4. **Nothing rejects non-canonical input.** §5 and Appendix A are producer-side
   constructions; no clause obliges a consumer to refuse an N-Quads document
   whose quads are out of order. Condition (2) is as absent here as it is from
   RFC 8949 §4.2 — which is now the third ratified canonicalization
   specification in this library to define an encoder and leave the decoder's
   obligation unstated.
5. **On condition (6) it supplies the refusal, not the rejection.** The note at
   §4.4.3 step 2 states that "literal components of quads are not subject to any
   normalization", resting on RDF 1.1 Concepts §3.3 lexical-form equality, so
   `"01"^^xsd:integer` and `"1"^^xsd:integer` stay distinct. That is a ratified
   precedent for the *explicit refusal to normalise* branch of condition (6),
   which our topic answer identifies as the only citation-compatible route left.
   It is not the whole of it: RDFC has nothing to reject, because in RDF two
   lexical forms are simply two different terms, whereas for us they would be
   two names for one thing. Appendix A is worth separating out here — it
   canonicalizes *escaping* (each code point represented exactly one way) while
   refusing to touch *characters*. Canonicalize the escaping, refuse to
   normalize the text: that separation is the borrowable idea, and it is cleaner
   than RFC 8785 §3.1's unenforceable MUST on parties we do not control.
6. **It is silent on nesting, which we need.** RDFC sorts a flat set of quads.
   `Threshold.members` is a list of `Principal`, and a `Principal` may itself be
   a `Threshold` with its own member set (ARCH-0001 §4.1), so our rule must
   apply bottom-up — inner sets canonicalized and ordered before the outer set
   serializes. RDFC gives no guidance on recursion because its data model never
   poses it.
7. **It is not `contradicts` with rfc-8785, and the tension is still real.**
   RFC 8785 §3.2.3 forbids reordering array elements; RDFC-1.0 §5 requires
   sorting set members. Asserting `contradicts` would overclaim — the two
   address different data models, arrays versus sets, and neither is wrong on
   its own ground. Recorded as `see_also` with the tension stated here instead,
   because the disagreement a reader needs is about *our* use, not about the two
   documents.

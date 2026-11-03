---
schema: "library-summary/v1"
id: ipld-dag-cbor
record: ipld-dag-cbor
type: summary
updated: "2026-11-03"
---

# Specification: DAG-CBOR

|  |  |
|---|---|
| **Type** | spec (IPLD codec specification, `specs/codecs/dag-cbor/spec.md` in `ipld/ipld`) |
| **Maturity** | `draft`: the document labels itself "Status: Descriptive - Draft". *Descriptive* means it records what deployed codecs do, not a ratified rule set |
| **Authors** | No byline. IPLD team; recent changes by Volker Mische (#310, #356, #380) |
| **Published** | 2026-07-23 (last change to the file, commit `0f0ea9c`, "dag-cbor: exclude -0.0"). Unversioned |
| **Identifier** | https://ipld.io/specs/codecs/dag-cbor/spec/ · source pinned at `ipld/ipld@0f0ea9c9a9b95e2e37168ac9fc887470f7f8ba58` · CBOR tag 42 ("IPLD content identifier") |
| **Source** | https://raw.githubusercontent.com/ipld/ipld/0f0ea9c9a9b95e2e37168ac9fc887470f7f8ba58/specs/codecs/dag-cbor/spec.md |
| **Digest** | `sha256:82f6b526…` (Markdown source; full value in `record.yaml`), fetched 2026-11-03. It replaces the earlier HTML-page digest `4a35ffac…`, which changes with CSS cache-busting and so cannot be re-verified |

## Overview

DAG-CBOR is the CBOR codec for the IPLD Data Model, used for content-addressed blocks in IPFS and Filecoin. Its argument is in §Strictness: content addressing needs "a single, canonical way of encoding any given set of data", so DAG-CBOR is a strict subset of CBOR. Its rules:

- **Tags.** One tag only, 42 for CID links, carried as a byte string with a mandatory `0x00` multibase prefix (§Links). Every other tag is forbidden, including the RFC 8949 §3.4 ones.
- **Maps.** Keys must be strings (§Map Keys), sorted length-first then bytewise (§Strictness).
- **Lengths and integers.** Shortest-form integers, lengths and tag head. No indefinite lengths.
- **Major type 7.** Only `false`, `true`, `null` and floats. Floats are **always 64-bit**. NaN, ±Infinity and −0.0 are excluded.
- **One item per block.** Exactly one top-level item, with no trailing bytes.

It then takes back the decoder half in §Decode strictness. Because of historical data, decoders "may relax strictness requirements by default". A strict mode is merely something that "may be offered". §Implementations records that most named codecs do not enforce the rules.

**What it contributes to the topic question** ("Do the emerging deterministic CBOR profiles converge, and which one should a key-centric profile cite rather than invent?"): DAG-CBOR is **a fourth profile that converges on integers and lengths and diverges on floats, tags and simple values.** It is not a good citation target for us.

- **Agrees with RFC 8949 §4.2.1** on shortest-form integers, lengths and tag heads, and on no indefinite lengths. On map order it agrees *in effect*. RFC 8949 §4.2.1 sorts by "bytewise lexicographic order of their deterministic encodings". DAG-CBOR sorts length-first (the RFC 7049 §3.9 "canonical" order). The two coincide here only because DAG-CBOR allows text-string keys alone: a text key's head grows with its length, so bytewise order of encodings is length-first. This is our derivation, not a statement in the spec.
- **Contradicts §4.2.1 on floats.** §Strictness says to "Use the 'Deterministically Encoded CBOR' rule suggestions defined in section 4.2 of RFC 8949", then requires 64-bit floats "regardless of whether they can be represented as half (16) or single (32) precision". RFC 8949 §4.2.1 says "Floating-point values also MUST use the shortest form that preserves the value". The same value therefore encodes differently under the two profiles. RFC 8949 §4.2.2 does let an application add float rules (negative zero, precision), but forcing a *longer* form is not an addition to §4.2.1. It replaces it.
- **Narrower than every general profile.** It forbids all tags but 42 and all simple values but three. A key-centric format that needs any other tag cannot be DAG-CBOR.
- **Strictness belongs to the encoder alone.** Relaxed decoding by default means a DAG-CBOR verifier cannot rely on the spec to reject non-canonical bytes. Its recommended Go codec accepts NaN and Infinity, which §Strictness says "must not be accepted".

So, on this record alone: cite RFC 8949 §4.2.1 or CDE (`draft-ietf-cbor-cde`) for a key-centric profile, not DAG-CBOR. Treat DAG-CBOR as an interchange target that needs a documented mapping. The comparison with CDE and dCBOR is the topic's job, not this record's.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Encoding determinism is what makes a content address unique. Relaxed decoders weaken that property (§Decode strictness) |
| Cryptography | `none` | No primitive. CIDs carry a multihash defined elsewhere |
| This project | `adjacent` | One of the profiles DEC-002's CBOR option would choose between or map to |

- **DEC-002** (concrete native encoding). If CBOR wins, this is one of the four incompatible profiles in the topic answer. The float rule alone makes it byte-incompatible with an RFC 8949 §4.2.1 encoder.
- **R-O-03** (cite the canonicalisation algorithm, do not invent it). DAG-CBOR is citable: it is stable, pinned, and in production. But it is self-labelled descriptive and draft, it claims §4.2 conformance it does not have, and its decode side is optional. Citing it would cite a moving description, not a rule.
- **R-M-12** (proposed in ARCH-0001 v0.2.0, since relocated to ARCH-0002 P1 and accepted by ADR-0001: native extension points not dependent on a central registry). DAG-CBOR's one permitted tag gets its meaning from the IANA CBOR tag registry (42) and from the multiformats tables behind the CID (multibase prefix `0x00`, §Links). Adopting DAG-CBOR natively would build both registry dependencies into the core. That is the thing R-M-12 says to confine to interchange boundaries.

**Relations.** `see_also` is kept to the two profiles this record is compared against: `draft-ietf-cbor-cde` (the citation target recommended above) and `draft-mcnally-deterministic-cbor` (dCBOR). RFC 8949, RFC 7049 and the IANA tag registry are under `cites`, which is what the spec links to.

## Implementations

**Searched 2026-11-03.** The list comes from the spec's own §Implementations, plus a GitHub API check of licences and activity.

| Name | Kind | License | URL |
|---|---|---|---|
| @ipld/dag-cbor | open source, JS | Apache-2.0 | https://github.com/ipld/js-dag-cbor |
| go-ipld-prime (dagcbor) | open source, Go | MIT | https://github.com/ipld/go-ipld-prime |
| cbor-gen | open source, Go | MIT | https://github.com/whyrusleeping/cbor-gen |
| serde_ipld_dagcbor | open source, Rust | not asserted (API NOASSERTION) | https://github.com/ipld/serde_ipld_dagcbor |
| Java IPLD (Peergos) | open source, Java | AGPL-3.0 | https://github.com/Peergos/Peergos |

By the spec's own account (§Implementations), **no named implementation enforces the full rule set on decode**:

- **@ipld/dag-cbor** skips map order and float width.
- **go-ipld-prime and go-ipld-cbor** enforce no decode strictness and accept NaN and ±Infinity.
- **cbor-gen** sorts keys with `sort.Strings()`, which is plain lexical order, not length-first. That is an *encoder* violation, yet the spec still says cbor-gen "adheres to this specification".

We did not test any codec.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, pinned source and digest history, relations, `bears_on`, implementations |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed.** This is a `spec` record moved from `fetched` to the summary bar. The `deterministic-cbor-profiles` topic cannot close until its records are distilled, so this record will need an FX-1 extraction. That would cover the strictness rules as requirements, the §Decode strictness relaxations as a declared second profile, the forbidden-token list as negative fixtures, and a crosswalk to `rfc-8949`'s fourteen application decisions. **It needs its own issue.** None owns it yet. The `.cache/` copies (HTML of 2026-10-05 and 2026-11-03, Markdown source) are local and gitignored.

## Limits

- **Normative force is unclear throughout.** §Strictness says the codec "must" follow the §4.2 rules, then says an encoder "should produce" and a decoder "should reject". §Decode strictness then lets decoders relax five rules by default. What that list leaves untouched for a decoder is: other tags and trailing bytes ("must"), indefinite lengths (a "should reject" under item 2), other simple values ("not supported"), NaN and ±Infinity ("must not be accepted", then "should not … be accepted" in the same item), and −0.0 ("should not"). Even the NaN and Infinity rule is not enforced by the named Go codec. No BCP 14 boilerplate is invoked, so "must" and "should" are plain English.
- **The float rule contradicts the section it cites** (see Overview). Not set as `contradicts` on `rfc-8949`, because RFC 8949 §4.2.2 leaves applications room to define float rules, and §4.2.1 describes *core* deterministic encoding, not a requirement on every profile. The defect is DAG-CBOR's claim that it follows §4.2.
- **−0.0 is stated imprecisely.** §Strictness item 6 says −0.0 "should always be encoded as `0x0000000000000000`". That is the 8-byte payload. The full DAG-CBOR token for 0.0 is `0xfb0000000000000000`. "should not appear or be accepted" is also weaker than the "must not" used for NaN and Infinity in the item before it.
- **A broken link.** In §Implementations > JavaScript, the legacy-codec bullet writes `[#decode-strictness](Decode strictness)`, with the label and target swapped. It renders literally on the site.
- **What it does not settle:** the multihash and CID rules (other specs), any float canonicalisation beyond width (for example integral floats versus integers), the JavaScript number problem it describes under §Limitations without a rule, and how a strict decoder should be identified to a peer.
- **Read scope.** The whole file was read, both as Markdown and as rendered HTML. The CID-in-CBOR and Data Model documents it cites were not fetched.

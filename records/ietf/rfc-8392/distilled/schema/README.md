---
record: rfc-8392
kind: schema
title: "rfc-8392 — schemas"
extracted: "2026-10-20"
reviewed_by: ""
---

# Schemas

**RFC 8392 ships no grammar of any kind.** Measured over all 1403 lines of
`.cache/rfc-8392.txt`, whole-word and case-insensitive: `CDDL` **0**, `ABNF`
**0**, `ASN.1` **0**, `JSON Schema` **0**, `schema` **0**, `grammar` **0**. The
word `syntax` occurs **once**, at line 485, inside §7.2 step 4 — *"whose syntax
and semantics are both understood and supported"* — which is a validation rule,
not a grammar. So one file here is verbatim and every other file is the
library's own and says so in its name.

| file | kind | what it is |
|---|---|---|
| `source-renderings.txt` | **verbatim** | the four places RFC 8392 renders a structure itself: §4's Table 1, §6's Figure 1, §9.1.1's registration template and the five registry-contents blocks. Nine regions, each with its line range and its own `sha256`. Lifted by line range by script, never retyped |
| `cwt-claims-set.derived.cddl` | derived | the claims set as CDDL: the seven claims with their keys and value types, the reserved key 0, the open extension socket §3 requires, and the `aud` disagreement left visible |
| `cwt-envelope.derived.cddl` | derived | the tag layers: §6's pairing rule, §7.2 step 3's untagged form, and the nesting of §7.1 step 5 / §7.2 step 6. The COSE structures are **named, not redefined** |
| `cwt-claims-set.derived.schema.json` | derived | a JSON-projection schema for fixture validation. `$id: urn:library:rfc-8392:cwt-claims-set.derived`. **The projection is ours** — RFC 8392 defines no JSON form, and §1 exists to avoid one |
| `claim-key-policy.derived.yaml` | derived | §9.1.1's four allocation tiers as data, each priced in octets from RFC 8949 §3 heads. The prices are ours, computed, and marked as such |

## What the derived schemas deliberately do not constrain

Each of these is the source's own position, not a gap in the rendering.

- **Which claims a CWT must have.** §3 puts it out of scope; §3.1 declines to
  make any claim mandatory. `cwt-claims-set` therefore has **no required
  member and the empty map `{}` validates.** A profile supplies this; RFC 9943
  §6 is the only ratified one the library holds.
- **Unknown claims.** `* other-claim-key => any` is wide open because §3
  requires that unknown claims *"MUST be ignored"*. A schema that rejected them
  would contradict the document.
- **Map key order and encoding determinism.** Nothing in RFC 8392 mentions
  either; `canonical` and `deterministic` occur **zero** times. Measured
  consequence, from decoding Appendix A: **all five printed CWTs are in
  RFC 8949 §4.2.1 deterministic map order and all three printed `COSE_Key`s are
  not** — their keys run `-1, 1, 2, 3`, where §4.2.1 sorts `1, 2, 3, -1`. See
  `../design-notes.md` and `../examples/vectors.yaml`.
- **The `aud` type.** Both forms are in the CDDL with the disagreement named.
  §3.1.3 permits an array of `StringOrURI`; §4's Table 1 and §9.1.2's registry
  entry both say `text string` and nothing else. **This is the one cell a code
  generator must not take from the registry.**
- **The claim-key space.** `int / tstr`, unbounded, because §9.1.1 bounds it
  only by registration *policy*. Policy is not a type, so it lives in
  `claim-key-policy.derived.yaml` instead.

## Derived-vs-verbatim

`.derived.` is mandatory on anything this library wrote and an unmarked name
asserts the source's own bytes (`docs/extraction.md`). `source-renderings.txt`
is the only unmarked file here, and it is unmarked because every byte in it is
RFC 8392's. `bin/validate` checks the name against the header marker in the
first 12 lines of each file, and the `$id` of every `*.derived.schema.json`.

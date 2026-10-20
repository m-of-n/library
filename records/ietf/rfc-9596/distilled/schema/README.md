---
record: rfc-9596
kind: schema
title: "rfc-9596 — schemas"
extracted: "2026-10-20"
reviewed_by: ""
---

# Schemas

**RFC 9596 ships no grammar of any kind.** Measured over all 232 lines of
`.cache/rfc-9596.txt`, whole-word and case-insensitive: `CDDL` **0**, `ABNF`
**0**, `ASN.1` **0**, `JSON Schema` **0**. The word `syntax` occurs **three**
times (lines 20, 83, 114) and every one is the English word in prose about the
value space. So the document's whole formal account of itself is **Table 1 plus
two prose sentences**, and everything derived here is the library's own.

| file | kind | what it is |
|---|---|---|
| `source-renderings.txt` | **verbatim** | five regions: §1's statement of the value space, §2's statement of it again with the content-type cross-reference, the one `MUST NOT`, the two sentences about what `typ` does *not* describe, and §4.1's Table 1. Each with its line range and its own `sha256` |
| `typ-header.derived.cddl` | derived | the label, the two-branch value space, the placement rule as a CDDL shape, and a named list of the three things CDDL cannot express |
| `typ-header.derived.schema.json` | derived | a JSON-projection schema for fixture validation. `$id: urn:library:rfc-9596:typ-header.derived` |

## The line breaks are preserved, not healed

The plain-text wrap cuts the registry name **"CoAP Content-Formats"** in two
at lines 86/87 and again at 116/117, hyphen and all. The verbatim regions carry
those breaks **exactly as printed**, and `requirements.yaml` R-0004 and R-0010
carry the flowed span — so the hyphen appears as `CoAP Content- Formats` after
whitespace normalisation rather than being silently repaired.

**That is deliberate and it is declared in three places.** Two silently healed
line breaks are among the five transcription defects this lane's own quote audit
found in its own prose, so this directory does not repeat them.

## The three things the derived schemas cannot constrain

Each is the document's own silence, not a gap in the rendering.

1. **Equality.** The same type has **two wire spellings** — `typ: 61` (CoAP
   Content-Format, `rfc-8392` §9.3.1) and `typ: "application/cwt"` (media type,
   `rfc-8392` §9.2.1) — and they compare unequal under any byte comparison.
   Media type names are case-insensitive (RFC 2045 §5.1, a document this library
   does not hold) while a CBOR `tstr` is not, and §2 permits media type
   *parameters* unconstrained. §3's only guidance is to reject a value
   *"different than values that they expect"*, and "different" is undefined.
   **A confusion-resistance mechanism with an unspecified equality relation can
   be defeated by respelling the type.**

2. **Consistency with content type.** Labels 16 and 3 have the same syntax and
   overlapping value spaces, and §2 distinguishes them only by scope. Nothing
   requires them to agree, and a verifier reading one and not the other is
   conformant.

3. **Any check at all.** §2 tells COSE libraries to ignore the parameter and
   §3's two reject rules are **lowercase**. A schema cannot supply an obligation
   the specification declines to state.

## Derived-vs-verbatim

`.derived.` is mandatory on anything this library wrote and an unmarked name
asserts the source's own bytes (`docs/extraction.md`).
`source-renderings.txt` is the only unmarked file here. `bin/validate` checks
the name against the header marker in each file's first 12 lines, and the `$id`
of every `*.derived.schema.json`.

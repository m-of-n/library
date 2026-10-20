---
record: rfc-9165
kind: normative
title: "rfc-9165 — normative statements"
extracted: "2026-10-19"
reviewed_by: ""
---

<!-- Every normative statement, VERBATIM, with its locator. Keep the source's
section structure as headings. Drop motivation, history, acknowledgements. -->

Source: RFC 9165, "Additional Control Operators for the Concise Data Definition Language (CDDL)", C. Bormann, Standards Track, December 2021. sha256 `94f86116c04fde0f11d54576465181090ec33983d78db82527c0703a41976774` (555 lines, 23143 bytes, plain text). Quotations are verbatim from the plain-text RFC. Blocks that reproduce tables, figures, grammar fragments or numbered lists preserve the source's own line breaks and indentation inside fenced blocks.

**Why this file is mostly definitions.** `bin/bcp14-count` reports **5** BCP 14
keyword occurrences in 23 KB, all five of them the bare keyword `MUST`, and all
five are **type admissibility rules on an operator's operands** — two numeric,
two string, one UTF-8 — not obligations laid on an actor. This is a **grammar
extension**: it adds six entries to CDDL's one declared extension point, and its
normativity is carried by *operator definitions and matching rules*, exactly as
RFC 8610's is. The precedent is this library's `rfc-8610` extraction (2 keywords
in 125 KB, 137 of 139 requirements `inferred`) and
`draft-ietf-cbor-edn-literals` (10 in 100 KB, 216 of 226 `inferred`). This file
therefore records the **definitional-normative** material — what each operator
means, what its target and controller may be, what the resulting type is, and
what the document says CDDL still cannot do — at the same grain another record
would use for MUST statements.

**Conventions in this file.**

- A bullet `- (§X) "…"` is one contiguous verbatim span of the source. No span
  is spliced from two non-adjacent parts of the document. Contiguity is
  asserted after collapsing runs of whitespace and nothing else: **RFC 9165
  carries no form feeds, no `[Page n]` markers and no running header or footer**
  (all three counted at zero), so unlike RFC 8610 and RFC 8949 there is no page
  decoration to remove and **no span in this record crosses a page frame.**
- **One token in this document is severed by hyphenation at a line break** —
  `left-` / `hand` at source lines 370/371. Per `docs/extraction.md` it is not
  quoted whole anywhere in this record. The §4 bullet that would contain it
  stops before the break and says so; `requirements.yaml` records the same fact
  in that entry's `field`. Nothing was silently healed.
- The source's own cursive convention is preserved: `_dedented_` and `_not_` in
  a quote are the RFC's rendering, not emphasis added here.
- The source's `--` for an em dash and its doubled sentence spacing are its own
  bytes and are reproduced.

---

## §1. Introduction

- (§1) "The Concise Data Definition Language (CDDL), standardized in [RFC8610], provides "control operators" as its main language extension point (Section 3.8 of [RFC8610])."
- (§1) "The present document defines a number of control operators that were not yet ready at the time [RFC8610] was completed:"

Table 1, verbatim (§1, source lines 82–98):

```
      +==========+==================================================+
      | Name     | Purpose                                          |
      +==========+==================================================+
      | .plus    | Numeric addition                                 |
      +----------+--------------------------------------------------+
      | .cat     | String concatenation                             |
      +----------+--------------------------------------------------+
      | .det     | String concatenation, pre-dedenting              |
      +----------+--------------------------------------------------+
      | .abnf    | ABNF in CDDL (text strings)                      |
      +----------+--------------------------------------------------+
      | .abnfb   | ABNF in CDDL (byte strings)                      |
      +----------+--------------------------------------------------+
      | .feature | Indicates name of feature used (extension point) |
      +----------+--------------------------------------------------+

              Table 1: New Control Operators in this Document
```

### §1.1. Terminology

- (§1.1) "This specification uses terminology from [RFC8610]."
- (§1.1) "In particular, with respect to control operators, "target" refers to the left-hand side operand and "controller" to the right-hand side operand."
- (§1.1) ""Tool" refers to tools along the lines of that described in Appendix F of [RFC8610]."
- (§1.1) "Note also that the data model underlying CDDL provides for text strings as well as byte strings as two separate types, which are then collectively referred to as "strings"."
- (§1.1) "The term "ABNF" in this specification stands for the combination of [RFC5234] and [RFC7405]; i.e., the ABNF control operators defined by this document allow use of the case-sensitive extensions defined in [RFC7405]."

The §1.1 BCP 14 boilerplate is deliberately **not** quoted anywhere in this
record. `bin/validate` recomputes the extracted keyword count over requirement
texts with boilerplate stripping **off**, so quoting it would add 11 phantom
keywords. Its presence is recorded here as a fact, not as a quotation.

## §2. Computed Literals

- (§2) "CDDL as defined in [RFC8610] does not have any mechanisms to compute literals."
- (§2) "To cover a large part of the use cases, this specification adds three control operators: .plus for numeric addition, .cat for string concatenation, and .det for string concatenation with dedenting of both sides (target and controller)."
- (§2) "For these operators, as with all control operators, targets and controllers are types."
- (§2) "The resulting type is therefore formally a function of the elements of the cross-product of the two types."
- (§2) "Not all tools may be able to work with non-unique targets or controllers."

### §2.1. Numeric Addition

- (§2.1) "In many cases, numbers are needed relative to a base number in a specification."
- (§2.1) "The .plus control identifies a number that is constructed by adding the numeric values of the target and the controller."
- (§2.1) "The target and controller both MUST be numeric."
- (§2.1) "If the target is a floating point number and the controller an integer number, or vice versa, the sum is converted into the type of the target; converting from a floating point number to an integer selects its floor (the largest integer less than or equal to the floating point number, i.e., rounding towards negative infinity)."

Figure 1, verbatim (§2.1, source lines 148–161):

```
   interval<BASE> = (
     BASE => int             ; lower bound
     (BASE .plus 1) => int   ; upper bound
     ? (BASE .plus 2) => int ; tolerance
   )

   X = 0
   Y = 3
   rect = {
     interval<X>
     interval<Y>
   }

              Figure 1: An Example of Addition to a Base Value
```

- (§2.1) "The example in Figure 1 contains the generic definition of a CDDL group interval that gives a lower and upper bound and, optionally, a tolerance."
- (§2.1) "The parameter BASE allows the non-conflicting use of a multiple of these interval groups in one map by assigning different labels to the entries of the interval."
- (§2.1) "The rule rect combines two of these interval groups into a map, one group for the X dimension (using 0, 1, and 2 as labels) and one for the Y dimension (using 3, 4, and 5 as labels)."

### §2.2. String Concatenation

- (§2.2) "It is often useful to be able to compose string literals out of component literals defined in different places in the specification."
- (§2.2) "The .cat control identifies a string that is built from a concatenation of the target and the controller."
- (§2.2) "The target and controller both MUST be strings."
- (§2.2) "The result of the operation has the same type as the target."
- (§2.2) "The concatenation is performed on the bytes in both strings."
- (§2.2) "If the target is a text string, the result of that concatenation MUST be valid UTF-8."

Figure 2, verbatim (§2.2, source lines 184–191):

```
   c = "foo" .cat '
     bar
     baz
   '
   ; on a system where the newline is \n, is the same string as:
   b = "foo\n  bar\n  baz\n"

       Figure 2: An Example of Concatenation of Text and Byte Strings
```

- (§2.2) "The example in Figure 2 builds a text string named c from concatenating the target text string "foo" and the controller byte string entered in a text form byte string literal."
- (§2.2) "(This particular idiom is useful when the text string contains newlines, which, as shown in the example for b, may be harder to read when entered in the format that the pure CDDL text string notation inherits from JSON.)"

### §2.3. String Concatenation with Dedenting

- (§2.3) "Multi-line string literals for various applications, including embedded ABNF (Section 3), need to be set flush left, at least partially."
- (§2.3) "Often, having some indentation in the source code for the literal can promote readability, as in Figure 3."

Figure 3, verbatim (§2.3, source lines 207–217):

```
   oid = bytes .abnfb ("oid" .det cbor-tags-oid)
   roid = bytes .abnfb ("roid" .det cbor-tags-oid)

   cbor-tags-oid = '
     oid = 1*arc
     roid = *arc
     arc = [nlsb] %x00-7f
     nlsb = %x81-ff *%x80-ff
   '

              Figure 3: An Example of Dedenting Concatenation
```

- (§2.3) "The control operator .det works like .cat, except that both arguments (target and controller) are independently _dedented_ before the concatenation takes place."
- (§2.3) "For the first rule in Figure 3, the result is equivalent to Figure 4."

Figure 4, verbatim (§2.3, source lines 225–232):

```
   oid = bytes .abnfb 'oid
   oid = 1*arc
   roid = *arc
   arc = [nlsb] %x00-7f
   nlsb = %x81-ff *%x80-ff
   '

             Figure 4: Dedenting Example: Result of First .det
```

The definition of dedenting, verbatim (§2.3, source lines 234–243):

```
   For the purposes of this specification, we define "dedenting" as:

   1.  determining the smallest amount of leftmost blank space (number
       of leading space characters) present in all the non-blank lines,
       and

   2.  removing exactly that number of leading space characters from
       each line.  For blank (blank space only or empty) lines, there
       may be fewer (or no) leading space characters than this amount,
       in which case all leading space is removed.
```

- (§2.3) "Occasionally, dedenting of only a single item is needed."
- (§2.3) "This can be achieved by using this operator with an empty string, e.g., "" .det rhs or lhs .det "", which can in turn be combined with a .cat: in the construct lhs .cat ("" .det rhs), only rhs is dedented."

## §3. Embedded ABNF

- (§3) "Many IETF protocols define allowable values for their text strings in ABNF [RFC5234] [RFC7405]."
- (§3) "It is often desirable to define a text string type in CDDL by employing existing ABNF embedded into the CDDL specification."
- (§3) "Without specific ABNF support in CDDL, that ABNF would usually need to be translated into a regular expression (if that is even possible)."
- (§3) "ABNF is added to CDDL in the same way that regular expressions were added: by defining a .abnf control operator."
- (§3) "The target is usually text or some restriction on it, and the controller is the text of an ABNF specification."
- (§3) "There are several small issues; the solutions are given here:"

The four issues and their solutions, each a bullet in the source.

- (§3) "ABNF can be used to define byte sequences as well as UTF-8 text strings interpreted as Unicode scalar sequences."
- (§3) "This means this specification defines two control operators: .abnfb for ABNF denoting byte sequences and .abnf for denoting sequences of Unicode scalar values (code points) represented as UTF-8 text strings."
- (§3) "Both control operators can be applied to targets of either string type; the ABNF is applied to the sequence of bytes in the string and interprets it as a sequence of bytes (.abnfb) or as a sequence of code points represented as an UTF-8 text string (.abnf)."
- (§3) "The controller string MUST be a string."
- (§3) "When a byte string, it MUST be valid UTF-8 and is interpreted as the text string that has the same sequence of bytes."
- (§3) "ABNF defines a list of rules, not a single expression (called "elements" in [RFC5234])."
- (§3) "This is resolved by requiring the controller string to be one valid "element", followed by zero or more valid "rules" separated from the element by a newline; thus, the controller string can be built by preceding a piece of valid ABNF by an "element" that selects from that ABNF and a newline."
- (§3) "For the same reason, ABNF requires newlines; specifying newlines in CDDL text strings is tedious (and leads to essentially unreadable ABNF)."
- (§3) "The workaround employs the .cat operator introduced in Section 2.2 and the syntax for text in byte strings."

The relaxation of ABNF's own newline, verbatim (§3, source lines 294–298):

```
      As is customary for ABNF, the syntax of ABNF itself (_not_ the
      syntax expressed in ABNF!) is relaxed to allow a single line feed
      as a newline:

      CRLF = %x0A / %x0D.0A
```

- (§3) "One set of rules provided in an ABNF specification is often used in multiple positions, particularly staples such as DIGIT and ALPHA."
- (§3) "(Note that all rules referenced need to be defined in each ABNF operator controller string -- there is no implicit import of core ABNF rules from [RFC5234] or other rules.)"
- (§3) "The composition this calls for can be provided by the .cat operator and/or by .det if there is indentation to be disposed of."
- (§3) "These points are combined into an example in Figure 5, which uses ABNF from [RFC3339] to specify one of each of the Concise Binary Object Representation (CBOR) tags defined in [RFC8943] and [RFC8949]."

Figure 5, verbatim (§3, source lines 312–349):

```
   ; for RFC 8943
   Tag1004 = #6.1004(text .abnf full-date)
   ; for RFC 8949
   Tag0 = #6.0(text .abnf date-time)

   full-date = "full-date" .cat rfc3339
   date-time = "date-time" .cat rfc3339

   ; Note the trick of idiomatically starting with a newline, separating
   ;   off the element in the concatenations above from the rule-list
   rfc3339 = '
      date-fullyear   = 4DIGIT
      date-month      = 2DIGIT  ; 01-12
      date-mday       = 2DIGIT  ; 01-28, 01-29, 01-30, 01-31 based on
                                ; month/year
      time-hour       = 2DIGIT  ; 00-23
      time-minute     = 2DIGIT  ; 00-59
      time-second     = 2DIGIT  ; 00-58, 00-59, 00-60 based on leap sec
                                ; rules
      time-secfrac    = "." 1*DIGIT
      time-numoffset  = ("+" / "-") time-hour ":" time-minute
      time-offset     = "Z" / time-numoffset

      partial-time    = time-hour ":" time-minute ":" time-second
                        [time-secfrac]
      full-date       = date-fullyear "-" date-month "-" date-mday
      full-time       = partial-time time-offset

      date-time       = full-date "T" full-time
   ' .det rfc5234-core

   rfc5234-core = '
      DIGIT          =  %x30-39 ; 0-9
      ; abbreviated here
   '

     Figure 5: An Example of Employing ABNF from RFC 3339 for Defining
                                 CBOR Tags
```

## §4. Features

- (§4) "Commonly, the kind of validation enabled by languages such as CDDL provides a Boolean result: valid or invalid."
- (§4) "In rapidly evolving environments, this is too simplistic."
- (§4) "The data models described by a CDDL specification may continually be enhanced by additional features, and it would be useful even for a specification that does not yet describe a specific future feature to identify the extension point the feature can use and accept such extensions while marking them as extensions."
- (§4) "The .feature control annotates the target as making use of the feature named by the controller."
- (§4) "The latter will usually be a string."
- (§4) "A tool that validates an instance against that specification may mark the instance as using a feature that is annotated by the specification."
- (§4) "More specifically, the tool's diagnostic output might contain the controller (right-hand side) as a feature name" — **the span stops here.** The token `left-hand` is **severed by the line break between source lines 370 and 371**, which the source sets as `…and the target (left-` then `hand side) as a feature detail.` Because whitespace normalisation turns that into `(left- hand side)`, the healed spelling `(left-hand side)` is **not this document's bytes**, and it is therefore written nowhere in this record. Under `docs/extraction.md` a token cut by a line break cannot be quoted whole, so this record quotes the obligation-bearing half and states the severance here and in `requirements.yaml`. The dropped half, **in our words, not the document's**: the target supplies the feature *detail* as the controller supplies the feature *name*.
- (§4) "However, in some cases, the target has too much detail, and the specification might want to hint to the tool that more limited detail is appropriate."
- (§4) "In this case, the controller should be an array, with the first element being the feature name (that would otherwise be the entire controller) and the second element being the detail (usually another string), as illustrated in Figure 6."

Figure 6, verbatim (§4, source lines 379–385):

```
   foo = {
     kind: bar / baz .feature (["foo-extensions", "bazify"])
   }
   bar = ...
   baz = ... ; complex stuff that doesn't all need to be in the detail

             Figure 6: Providing Explicit Detail with .feature
```

- (§4) "Figure 7 shows what could be the definition of a person, with potential extensions beyond name and organization being marked further-person-extension."
- (§4) "Extensions that are known at the time this definition is written can be collected into $$person-extensions."
- (§4) "However, future extensions would be deemed invalid unless the wildcard at the end of the map is added."
- (§4) "These extensions could then be specifically examined by a user or a tool that makes use of the validation result; the label (map key) actually used makes a fine feature detail for the tool's diagnostic output."
- (§4) "Leaving out the entire extension point would mean that instances that make use of an extension would be marked as wholesale invalid, making the entire validation approach much less useful."
- (§4) "Leaving the extension point in but not marking its use as special would render mistakes (such as using the label "organisation" instead of "organization") invisible."

Figure 7, verbatim (§4, source lines 404–413):

```
   person = {
     ? name: text
     ? organization: text
     $$person-extensions
     * (text .feature "further-person-extension") => any
   }

   $$person-extensions //= (? bloodgroup: text)

                 Figure 7: Map Extensibility with .feature
```

- (§4) "Figure 8 shows another example where .feature provides for type extensibility."

Figure 8, verbatim (§4, source lines 418–422):

```
   allowed-types = number / text / bool / null
                 / [* number] / [* text] / [* bool]
                 / (any .feature "allowed-type-extension")

                 Figure 8: Type Extensibility with .feature
```

- (§4) "A CDDL tool may simply report the set of features being used; the control then only provides information to the process requesting the validation."
- (§4) "One could also imagine a tool that takes arguments, allowing the tool to accept certain features and reject others (enable/disable)."
- (§4) "The latter approach could, for instance, be used for a JSON/CBOR switch, as illustrated in Figure 9, using Sensor Measurement Lists (SenML) [RFC8428] as the example data model used with both JSON and CBOR."

Figure 9, verbatim (§4, source lines 433–441):

```
   SenML-Record = {
   ; ...
     ? v => number
   ; ...
   }
   v = JC<"v", 2>
   JC<J,C> = J .feature "json" / C .feature "cbor"

                Figure 9: Describing Variants with .feature
```

- (§4) "It remains to be seen if the enable/disable approach can lead to new idioms of using CDDL."
- (§4) "The language currently has no way to enforce mutually exclusive use of features, as would be needed in this example."

## §5. IANA Considerations

- (§5) "IANA has registered the contents of Table 2 into the "CDDL Control Operators" registry of [IANA.cddl]:"

Table 2, verbatim (§5, source lines 453–470):

```
                          +==========+===========+
                          | Name     | Reference |
                          +==========+===========+
                          | .plus    | RFC 9165  |
                          +----------+-----------+
                          | .cat     | RFC 9165  |
                          +----------+-----------+
                          | .det     | RFC 9165  |
                          +----------+-----------+
                          | .abnf    | RFC 9165  |
                          +----------+-----------+
                          | .abnfb   | RFC 9165  |
                          +----------+-----------+
                          | .feature | RFC 9165  |
                          +----------+-----------+

                            Table 2: New Control
                                 Operators
```

Note that the registry entry is **a name and a reference, and nothing else** —
no target type, no controller type, no semantics. That is the whole of what a
registered CDDL control operator carries, and it is why
`schema/control-operators.derived.yaml` in this record (and in `rfc-8610`) has
to exist.

## §6. Security Considerations

- (§6) "The security considerations of [RFC8610] apply."
- (§6) "While both [RFC5234] and [RFC7405] state that security is truly believed to be irrelevant to the respective document, the use of formal description techniques cannot only simplify but sometimes also complicate a specification."
- (§6) "This can lead to security problems in implementations and in the specification itself."
- (§6) "As with CDDL itself, ABNF should be judiciously applied, and overly complex (or "cute") constructions should be avoided."

## §7.1. Normative References

Recorded because the normative reference set is what a conforming tool must
implement, and this document's set is unusual: it makes **two ABNF RFCs
normative for a CDDL extension**, and it makes an **IANA registry page** a
normative reference.

- `[IANA.cddl]` — IANA, "Concise Data Definition Language (CDDL)", <https://www.iana.org/assignments/cddl>.
- `[RFC2119]`, `[RFC8174]` — BCP 14.
- `[RFC5234]` — "Augmented BNF for Syntax Specifications: ABNF", STD 68.
- `[RFC7405]` — "Case-Sensitive String Support in ABNF".
- `[RFC8610]` — "Concise Data Definition Language (CDDL)".

Informative: `[RFC3339]`, `[RFC8428]` (SenML), `[RFC8943]` (CBOR tags for date),
`[RFC8949]` (CBOR, STD 94).

---
record: rfc-9741
kind: design-notes
title: "rfc-9741 — bearing on our design"
extracted: "2026-10-19"
reviewed_by: ""
---

**Scope and provenance conventions.** Section numbers with no document name
(`§2.3`) are RFC 9741. Our own documents are cited by id (`ARCH-0002 P1`,
`MD-3`, `R-O-03`). Three markers distinguish voices, following
`records/ietf/rfc-8949/distilled/design-notes.md`:

- unmarked prose reports **RFC 9741** or **our decisions**, as cited;
- **[analysis]** marks reasoning of this extraction that neither the source nor
  our documents state;
- **[correction]** marks a working assumption of the project, or a claim in one
  of our own artifacts, that the source does not support.

**Decision status, stated plainly.** DEC-002 in `ARCH-0001` §7 lists **four**
options. "Option 5" exists only as *proposed* text in
`ARCH-0001-PROPOSAL-v0.2.0` §3.3; that proposal is unmerged. `ADR-0001`
(accepted) constrains DEC-002 and says option 2 "as originally written does
not" remain on the table. `MD-3` (2026-09-28) *narrows* DEC-002 to option 5.
**No ADR for DEC-002 has been written**, and `DECISIONS-0001` item 2 says so in
terms: "a narrowing is not an acceptance". Nothing below may be read as an
accepted encoding decision.

**One sentence of context for why this record exists.** `rfc-8610` reached
`profile: full` with a gate in both its `distilled/README.md` and its
`summary.md`: *nothing there may be treated as the current state of CDDL until
`rfc-9165`, `rfc-9682`, `rfc-9741` and `draft-ietf-cbor-cddl-modules` are
read.* This is one of the four. §7 below says what it closes.

---

## 1. The question this record was extracted to answer

Three of our documents have an open question about text identity:

- `rfc-8610`'s extraction found that **CDDL does no Unicode normalisation** —
  §3.1 "Processing of CDDL does not involve Unicode normalization processes",
  §3.8.6 compares text "bytewise identical" — and recorded that as a second
  independent source for the `canonical-encoding` topic's **condition (6)**.
- `draft-mcnally-deterministic-cbor` found that dCBOR §2.7 *does* require NFC,
  and called it "the only answer to condition (6) any document we hold
  supplies" — at the price of Unicode tables on the untrusted-input path.
- `draft-ietf-cbor-edn-literals` found CDN's text repertoire wider than
  RFC 9682's.

RFC 9741 is the IETF's 2025 document *for the conversion and processing of
text* in CDDL. If any document were going to give CDDL a way to say "this text
must be NFC", it is this one.

### 1.1 It does not. The answer is no, and the document says so itself

**A CDDL schema cannot state a Unicode normalisation constraint, or any
text-identity constraint over general text, after RFC 9741.** Four pieces of
evidence, in increasing order of force:

1. **Mechanical.** The strings `normaliz`, `normalis`, `NFC`, `NFD`, `NFKC` and
   `NFKD` do not occur anywhere in the cached source. `Unicode` occurs **once**,
   in §2.3: *"The "c" conversion specifier (paragraph 8) represents a single
   Unicode scalar value as a UTF-8 character."* `UTF-8` occurs three times, all
   in §2.3 and §3.1. And — the one that surprised this extraction —
   **`canonical` occurs zero times**, as do `identity`, `hash` and `digest`. A
   document that defines eight injective text forms never calls one of them
   canonical, which is why `text_identity_summary` in
   `schema/control-operators.derived.yaml` is **ours** and must be cited as
   ours.
2. **By enumeration.** All fourteen operators are in Table 1 with their target
   and controller types. Ten convert text ↔ bytes, one text ↔ int, one text ↔
   a printf argument list, one text ↔ a JSON value, one concatenates strings.
   **Not one takes a text target and imposes a predicate about the text's own
   form as text.** The nearest thing is `.hexlc`/`.hexuc`, which constrain
   *case* over a 16-character ASCII alphabet.
3. **The only text-identity property any operator here imposes is UTF-8
   validity**, in §3.1: *"If the result of the concatenation is a text string,
   the resulting sequence of bytes only matches the target data item if that
   result is a valid text string (i.e., valid UTF-8)."*
4. **The document states the absence of the operator class in its own words**,
   in §2.4: *"This control operator provides no way to constrain the use of
   blank space or other serialization variants in the JSON representation of
   the data items; restrictions on the serialization to specific variants
   (e.g., not providing for the addition of any insignificant blank space and
   prescribing an order in which map entries are serialized) could be defined
   in future control operators."* That is a canonical-text-form constraint, it
   is named, and it is deferred.

> **[analysis] Could it be smuggled in with RFC 8610's `.regexp`?** Not
> citably. NFC-ness of a code point sequence is in principle a finite-state
> property — the quick-check property plus canonical combining-class ordering —
> so some monstrous regular expression exists. But XSD regular expressions
> (RFC 8610 §3.8.3) offer no Unicode-normalisation character class, so the
> expression would have to enumerate composition exclusions and combining
> classes by hand. Under `R-O-03` that is **a partly invented algorithm**, which
> is precisely what `R-O-03` exists to forbid. And `.printf` cannot do it
> either: `text .printf (["%s", tstr])` is **vacuous**, because `%s`
> interpolates whatever text it is given. `.printf` can pin an exact code point
> sequence — `["%c%c", 97, 0x0301]` is the NFD form of "á" and `["%c", 0x00E1]`
> the NFC form — but a CDDL text literal already does that, and neither is a
> predicate over an open set of strings.

### 1.2 What it *can* pin, and this part is genuinely useful

Eight of the fourteen give an **injective text form**: exactly one text string
per value. `schema/control-operators.derived.yaml` →
`text_identity_summary` is the table; the short version:

| injective | not injective, by design | conditional |
|---|---|---|
| `.b64u` `.b64c` `.b45` `.b32` `.h32` `.hexlc` `.hexuc` `.base10` | `.hex` (either case) · `.b64u-sloppy` `.b64c-sloppy` (trailing bits unchecked) · `.json` (blank space, map order) | `.printf` (format-dependent and locale-undetermined) · `.join` (inherits from its elements) |

So for **text that is a transcoding of a byte string or of an integer**, RFC
9741 supplies a *citable* canonical form where before we would have had to
invent one. That is a real `R-O-03` win and it lands on two of our fields
directly (§5).

**The three traps are all in the default-looking names.** `.hex` is the name a
person reaches for and it is the wrong one — Table 2 says "either case", so an
*n*-digit value has 2ⁿ matching texts. `.b64u-sloppy` and `.b64c-sloppy` are
non-injective by definition (§2.1: *"not validated for any additional bits
being zero"*). Where text is hashed or signed, use `.hexlc`, `.hexuc`, `.b64u`,
`.b64c`.

### 1.3 `.join` makes text identity non-compositional — the new finding

This is the thing in this document that changes something for us, and it is not
in the abstract.

§3.1, three sentences in a row: *"The concatenation is performed on the
sequences of bytes in the strings."* / *"If the result of the concatenation is
a text string, the resulting sequence of bytes only matches the target data
item if that result is a valid text string (i.e., valid UTF-8)."* / *"Note that
in contrast to the algorithm used in Section 3.2.3 of RFC 8949 [STD94], there
is no need for all individual byte sequences going into the concatenation to
constitute valid text strings."*

> **[analysis]** `.join` therefore permits an element that **ends in the middle
> of a multi-byte UTF-8 sequence**, and a fortiori one that ends in the middle
> of a **combining-character sequence**. Unicode normalisation is **not closed
> under concatenation**: `NFC(a) · NFC(b)` need not equal `NFC(a·b)`. The
> standard witness is an element ending in a base character and the next
> beginning with a combining mark — each part is already NFC, the join is not.
> **So even if a future `.nfc` operator existed, it could not be checked
> element-by-element across a `.join`.** A normalisation property on the parts
> says nothing about the whole.
>
> **This lands on `ARCH-0002` P1 and `ARCH-0001` §4.1 exactly.** `Name` is
> `{ issuer: Principal, labels: [string, ...] }` — SDSI compound names are an
> *array of text labels*, and `.join` is the operator one would reach for to
> model their rendered form. The rule we now owe the ADR is one line:
> **a name chain must be normalised after joining, never per label.** Nothing
> of ours says this, and nothing in the sources says it either; it follows from
> §3.1 plus the definition of NFC.

### 1.4 What this settles for condition (6)

`library/topics/canonical-encoding.yaml` states condition (6) as: *"Text that
is load-bearing for identity has a declared Unicode normalisation rule, or an
explicit refusal to normalise together with rejection of unnormalised input."*
Both branches are predicates over text. **Neither is stateable in CDDL, and
after this document that is a published fact rather than an inference from
silence.**

The difference between this record and `rfc-8610`'s matters. `rfc-8610` records
CDDL's silence as of **2019**, from a document that was not about text. RFC 9741
is from **2025**, is titled *for the Conversion and Processing of Text*, had the
occasion in front of it, and declined — naming the missing operator class and
deferring it to "future control operators". **Condition (6) is therefore not a
schema-layer question at all.** It can be answered in exactly three places:

1. the **encoding** layer, as dCBOR §2.7 does (normalise branch, Unicode tables
   on the decode path);
2. **by absence**, as RFC 9804 does (refuse-to-normalise branch, nothing to
   implement);
3. an **application** rule outside the schema, which is where `R-O-05` already
   puts canonicalisation — `PLAN-0001`'s phrase for it is that
   "canonicalization happens once, at authoring time, on trusted input".

**This does not favour one DEC-002 option over another; it removes an argument
one of them could have made.** Option 2 — "CBOR + CDDL as canonical" — is the
option whose whole claim is that the schema carries the constraints. On
condition (6) the schema carries nothing, and option 2 pays CDDL's costs (§6)
without buying the answer. `ADR-0001` has already withdrawn option 2 as
originally written; this is an independent reason, and it is the first time a
CDDL document rather than our own inference supplies it.

---

## 2. What we adopt

### 2.1 §2.1's first example is our export path, almost verbatim

The document's first example, printed with no instance (our `V-0001`):

```
   signature-for-json = text .b64u signature
   signature = bytes .cbor COSE_Sign1
```

A **COSE_Sign1, CBOR-encoded, base64url-encoded, carried in a text field.**
That is `R-I-03` ("Export to in-toto Statement + DSSE OR COSE_Sign1 + CWT
claims") and `MD-3`'s "COSE as export only", written as CDDL by the CBOR
working group. We adopt the idiom for the export schema:

- the strict `.b64u`, never `.b64u-sloppy` (see §4);
- `.cbor` (RFC 8610 §3.8.4) under it, so the schema states that the bytes are
  CBOR and what they decode to;
- composition **through a rule name**, which is the only way CDDL composes
  controls at all — RFC 8610's grammar admits at most one control per `type1`.
  `rfc-8610`'s gap **G-44** said Table 1 implies a chaining the grammar
  forbids; this document shows the idiom that replaces it, in both its worked
  examples.

`COSE_Sign1` is named and never defined in RFC 9741. The vector is carried
unresolved.

### 2.2 `.hexlc` / `.hexuc` for `ArtifactId.digest.hex`

`ARCH-0001` §4.1: `ArtifactId` is `{ uri?: string, digest: { alg, hex } }`. The
field is literally named `hex` and is text. Before this document, *lower-case
hex with no separators* had no citation and under `R-O-03` would have been
ours. Now:

```
digest-hex = text .hexlc bytes          ; or .hexuc; NOT .hex
```

**Pick one and write it down.** [analysis] `.hexuc` is RFC 4648 §8's own case
and `.hexlc` is the common deviation; the document states no default and offers
no plain `.hex16`. Our existing fixtures and `rcbor` spike use lower case, so
`.hexlc` is the lower-friction choice — but it is a choice, it must be in the
ADR, and `.hex` must be excluded by name because it admits both.

### 2.3 `.base10` for integer-valued text, within its limits

`text .base10 (0..255)` is a citable canonical decimal form: no leading zeros,
no `+`, and no `-0` (the I-Regexp `0|-?[1-9][0-9]*`, held verbatim as
`schema/base10-numeral.iregexp`). Where `MD-3` puts YAML as the human form and
a number has to survive a text round trip, this is the rule to cite. §1.1 fixes
the dialect as **I-Regexp (RFC 9485)**, not the XSD dialect of RFC 8610
§3.8.3 — a detail that matters if we ever generate the regexp into tooling.

### 2.4 The registry fact

§1: *"RFCs have added to this extension point in both an application-specific
[RFC9090] and a more general [RFC9165] way."* §4 then registers fourteen more
names. We adopt this as the correction to our own artifact — §9.

---

## 3. What we adapt, and how

### 3.1 `.join` for rendered forms only, never for identity

`.join` is the right tool for the **human** form and the wrong tool for the
**canonical** one. Figure 1 is the pattern — three literal `"."` markers
isolating four `.base10`-controlled elements — and the document is explicit
about the discipline (§3.1): limit it to *"simple arrangements where the array
elements are laid out explicitly and there are no adjacent variable elements
without intervening constant values, and where these constant values do not
occur within the text described by the variable elements."*

We adapt it as: **`.join` may appear in a schema for a rendered or
diagnostic field; it may not appear on any path whose bytes are hashed or
signed.** Three reasons, all the document's own: validation in the general case
*"would require full parser functionality"*; a conforming validator may return
**false negatives** (§3.1's `RECOMMENDED` asks only for the marker-based
subset); and §1.3's non-compositionality.

### 3.2 `.json`, but only where the JSON is opaque to us

`.json` is the right shape for a field that carries somebody else's JSON — a
foreign predicate, an imported in-toto statement. It is the wrong shape for
anything of ours, because it cannot constrain the serialization (§1.1
evidence 4). [analysis] Read `.json` as *"this text parses as JSON and its
value matches T"*, never as *"this text is the canonical JSON of a T"*. The
first is useful at an `R-I-01` boundary. The second does not exist.

### 3.3 Two fields `.printf` would be reached for, and should not be

[analysis] `Validity` is `{ not_before?, not_after?, online_check? }`, and the
obvious text form is RFC 3339. **`.base10` cannot model it**, because RFC 3339
requires fixed-width two-digit components (`01`) and `.base10`'s canonical form
*forbids leading zeros*. The one numeral operator's canonical form is exactly
wrong for the commonest fixed-width text format we would want. The route the
document offers is `.printf (["%02d", 1..12])` — which drags in §4's objections.
So: carry timestamps as integers, or as text validated outside CDDL, and say
which in the ADR. This is a concrete D4 input, due 2026-10-21.

---

## 4. What we reject, and why

**`.printf`, everywhere.** Three independent reasons, any one sufficient:

1. **It imports a paywalled normative reference into the matching relation.**
   §6.1 lists `[C]` as ISO/IEC 9899:2024 at `https://www.iso.org/standard/82075.html`.
   A validator's answer to "does this text match" is defined by a document this
   library does not hold and cannot ship. Under `R-O-03` — "cited, not invented
   silently" — a citation we cannot read is not much better than an invention.
2. **The matching relation is locale-dependent and the document never fixes a
   locale** (§8 defect 1). For `%f`, `%e`, `%g` and `%a` two conforming
   validators can disagree about the same instance.
3. **It cannot render our integers.** The only `MUST NOT`s in the document
   forbid length modifiers, so each conversion carries C's default argument
   type. A 64-bit SID — §2.2's own example reaches `9223372036854775807` — let
   alone a 256-bit digest, has no conversion. See
   `schema/printf-profile.derived.txt`, U-2.

**`.hex`.** Case-ambiguous, therefore not injective. Use `.hexlc` or `.hexuc`.

**`.b64u-sloppy` and `.b64c-sloppy`.** Non-injective by definition. [analysis]
The trap is specific and worth stating: in §2.1's own export example, a
`-sloppy` wrapper would admit **several distinct text strings for one signed
payload**. `R-O-05` says "The signed payload SHALL be the canonical encoding
verbatim". If an export envelope is carried as base64url text, then the strict
operator is **mandatory**, and any digest must be taken over the **decoded
bytes**, never over the text.

**`.json` for anything of ours.** §3.2.

---

## 5. Mapping to our decisions

`MD-3` narrowed DEC-002 to option 5: CBOR data model, no IANA tags, COSE
export only, YAML as the human form. FX-1 asks for the header-by-header
mapping; this document has no headers, so the mapping is operator-to-field.

| our field (`ARCH-0001` §4.1) | option-5 native | text form, if any | operator | verdict |
|---|---|---|---|---|
| `Key` material | byte string | — | — | no text form; nothing here applies |
| `KeyId` (digest of canonical key bytes) | byte string | hex or base64url in the human form | `.hexlc` / `.b64u` | **adopt**, strict variants only |
| `ArtifactId.digest.hex` | `{alg, hex}`; `hex` is text | lower- or upper-case hex | `.hexlc` / `.hexuc` | **adopt**; `.hex` rejected by name |
| `ArtifactId.uri` | text | — | — | nothing applies |
| `Name.labels` (P1 local labels) | array of text | the rendered name chain | `.join` | **rendered form only** (§1.3, §3.1) |
| `Threshold.k`, `.n` | int | `.base10` if ever text | `.base10` | adopt for the text form; **the `1 ≤ k ≤ n` constraint is still inexpressible** |
| `Threshold.members` | array | — | — | nothing applies; the set/sequence problem is untouched |
| `Validity.not_before`/`not_after` | int or RFC 3339 text | RFC 3339 | **none usable** | §3.3 |
| `Tag` | opaque byte string | — | — | nothing applies |
| `PredicateType` (URI) | text | — | — | a *global* identifier, which P1 rejects natively |
| export envelope (`R-I-03`) | COSE_Sign1 bytes | base64url text | `.b64u` + `.cbor` | **adopt** (§2.1) |
| `Predicate` carrying foreign JSON | text | somebody else's JSON | `.json` | adapt (§3.2) |

**What we deliberately do not carry.** Nine of the fourteen operators have no
use in our model: `.b32`, `.h32`, `.b45`, `.b64c`, `.b64c-sloppy`,
`.b64u-sloppy`, `.hex`, `.printf`, `.json`-for-our-own-types. `.b45` deserves a
sentence because it is the one with a live constituency we might meet —
§2.1 says it is *"included because of its close relationship to QR codes and
its wide use in health informatics"* — and if a QR-coded `NameCert` is ever a
demo, `.b45` is the citation.

**Three things option 5 still owes that this document does not supply:** a
canonical order for set-valued fields (condition (5)); a normalisation rule for
identity-bearing text (condition (6), §1.4); and a decoder-side rejection rule
(condition (2)). None is a schema-layer question, and that is now evidenced
rather than assumed.

---

## 6. Where this document cuts against MD-3

`MD-3` is a dated **narrowing** of DEC-002, not an acceptance. `docs/extraction.md`
is explicit that an extraction which only confirms is not evidence. Six cuts,
each naming the option it favours.

**Cut 1 — an option-5 CDDL schema is not registry-free; it moves the registry
one layer up. Favours option 1.** Option 5's defining exclusion is "no reliance
on the IANA CBOR Tags registry and no native use of COSE header parameters".
It says nothing about the **CDDL Control Operators** registry — and §4 of this
document registers fourteen names into it, under RFC 8610 §6.1's Specification
Required / IETF Review policy, with §1 noting that RFC 9090 and RFC 9165 got
there first. [analysis] `ARCH-0002` P1 says an extension point is a pair
`(defining key, local label)`. **A control operator is an extension point** —
§1 of *this* document says CDDL "provides "control operators" as its main
language extension point (Section 3.8 of [RFC8610])" — and CDDL offers no way
to write a key-relative one. So a schema
written in CDDL depends on central allocation **for the meaning of its own
schema language**, which is the dependence P1 rejects one layer down. Options 2
and 5 both pay this; option 1 does not, because RFC 9804's canonical form is
two ABNF productions with no schema registry behind it.

**Cut 2 — the schema language now has a paywalled normative dependency.
Favours option 1.** §4 reason 1. A CDDL *tool* that claims full coverage of the
registry must implement `.printf` against ISO/IEC 9899:2024. We would not use
the operator, but we would depend on tools that claim to. (Option 3 does not
pay this either, but `DECISIONS-0001`'s standing note withdraws option 3 on
other grounds, so it is not a live comparison.)

**Cut 3 — text identity is non-compositional, and our name chains are
compositional. Option-neutral, and it is a new constraint on `R-O-05`.** §1.3.
This favours no option; it is a rule the ADR must carry whichever wins, and
nothing of ours states it.

**Cut 4 — the canonical form of the one numeral operator is incompatible with
fixed-width text, so `MD-3`'s "YAML as the human form" cannot be
schema-checked for timestamps. Favours option 1 weakly.** §3.3. Under option 1
the question does not arise in the same way, because RFC 9804 has no schema
layer to disappoint.

**Cut 5 — P4's hash-identified schema set cannot be made canonical by a CDDL
schema, and this document says so about the analogous case. Favours option 1.**
`ARCH-0002` P4 requires a domain of discourse to be "serialized in a form that
can be reliably and repeatably hashed", over P3 schemas that include "short
descriptions, possibly multilingual". §2.4's absence is that problem one layer
up: a CDDL schema cannot constrain blank space or map-entry order in a nested
text document. [analysis] P4's hash therefore needs a canonicalisation rule
**outside** the schema language, and the two conditions `canonical-encoding`
already calls unreachable — (5) set order and (6) text normalisation — are
exactly the two P4's hash depends on. Under option 1 a domain of discourse
would be an S-expression whose canonical form is a **grammar**, which is the
smallest such rule available.

**Cut 6 — and one point in option 5's favour, stated so the balance is
honest.** §2.1's first example *is* option 5's export path (§2.1 above). The
CBOR working group wrote `text .b64u signature` / `signature = bytes .cbor
COSE_Sign1` as the natural idiom in 2025. Option 5's interchange story is the
one thing in this document that lands cleanly, and `.b64u`'s strictness makes
it safe where `-sloppy` would not.

---

## 7. The gate on `rfc-8610`: what this closes and what it does not

`rfc-8610`'s gate names four documents. This is one; `rfc-9165`, `rfc-9682` and
`draft-ietf-cbor-cddl-modules` remain. What this one settles:

- **Syntax: nothing changed.** RFC 9741 adds no grammar. `rfc-8610`'s
  `schema/cddl.abnf` is still the whole of CDDL's syntax, and a tool that
  parses CDDL needs no parser change for these fourteen operators — it needs
  fourteen semantic cases.
- **Registry: the count is wrong.** §9.
- **The 44 side conditions: none is closed.** Full verdicts in
  `schema/control-operators.derived.yaml` → `gap_effects`. Summary:
  **G-11 extended** (fourteen more
  target/controller admissibility conditions, three of a shape G-11 did not
  anticipate); **G-12 confirmed by a newer normative source** (RFC 9741 states
  in its own words that the `b64` *literal prefix* "simply accepts characters
  from either alphabet", and that this differs from the operators — so the
  operators do not fix G-12, they sit beside it); **G-35 partially relieved**
  (hex case is now pinnable by name instead of by regexp, though
  case-insensitive matching remains impossible); **G-44 refined** (controls
  still do not chain; they nest through rule names, and this document makes
  that the idiom); **G-36 and G-38 reinforced** one layer up; **G-39 worsened**
  (this is the first CDDL document to state a *partial* validator coverage
  target and concede false negatives). **Ten new side conditions** are added,
  `N-01`–`N-10` in the same file.
- **"What CDDL cannot express that we need" — all six items stand.** Item 4
  (Unicode normalisation of labels) is now *strengthened*: not merely absent,
  but declined by the document that would have added it. Item 1 (cross-field
  constraints, `1 ≤ k ≤ n`) is untouched; [analysis] `.printf` with a generic
  parameter ties two members to one *parameter at the use site*
  (`hexlabel<K>`), which is not the same as relating two members of a given
  instance, so the hole is where it was.

---

## 8. Source defects

Reported, never repaired. Numbered; `requirements.yaml` cites defect 1.

1. **`.printf`'s matching relation is locale-dependent and no locale is
   fixed.** §2.3 says the construct matches *"the textual output of an
   equivalent C-language printf function call"*. [analysis] C's floating-point
   conversions emit the decimal-point character of the current locale, so
   `1.5` and `1,5` are both conforming outputs of the same format string. The
   document fixes no locale, not even the C locale. This is the sharpest defect
   because it is silent: the format string *looks* deterministic.
2. **The ban on length modifiers caps `.printf`'s integer range, and the
   document gives no rule for overflow.** §4 reason 3;
   `schema/printf-profile.derived.txt` U-2.
3. **`%c` is redefined away from C and the deviation is not labelled.** §2.3
   says `%c` *"represents a single Unicode scalar value as a UTF-8
   character"*. [analysis] In C, `%c` writes one byte; the wide form `%lc`
   needs a length modifier, which the same paragraph forbids. The
   redefinition is *forced*, and a reader who knows C and skims the paragraph
   will take the opposite meaning. `%s` is redefined the same way, and nothing
   is said about a precision (`%.3s`) that falls inside a multi-byte sequence.
4. **The `[C]` URL is broken across a line and contains a space as printed.**
   §6.1: *"Technically equivalent specification text is available at
   <https://www.open-std.org/jtc1/sc22/wg14/www/docs/ n3220.pdf>."* A
   rendering defect in the exact bytes `content.sha256` pins, not a
   specification defect — recorded because our verbatim quote necessarily
   reproduces it, and because it is the *only free route* to a normative
   reference.
5. **One hyphenation break makes a normative sentence unquotable whole.**
   Source lines 133/134 sever `left-hand-side`. Carried as two requirement
   entries, `rfc-9741#R-0007` and `R-0008`, and not healed.
6. **"Table 1" is ambiguous across two documents in the sentence that needs it
   most.** §2.1 defines "sloppy" as a variance from *"the paragraph that
   follows Table 1 in Section 4 of [RFC4648]"*. That is RFC 4648's Table 1;
   this document has its own Table 1 two pages earlier, which is the summary of
   all fourteen operators.
7. **The same fourteen names appear in three different orders** — Table 1
   (grouped by purpose), Table 2 (hex last), Table 7 (the registry's). Not an
   error, but a diff of any two of them is noise.
8. **`COSE_Sign1` is used and never defined** (§2.1), and §2.3's `%b`/`%B` note
   leaves it unstated whether they are in the profile.
9. **The `RECOMMENDED` is inside an aside.** §3.1's implementation note is set
   as an RFC v3 aside — visually an editorial remark — and it carries the only
   BCP 14 keyword in the document that binds an implementation.

---

## 9. Corrections owed to records already at `profile: full`

**[correction] `rfc-8610` — one factual claim is now false.**
`records/ietf/rfc-8610/distilled/schema/control-operators.derived.yaml` says,
under `extension_point.policy_note`: *"All names other than the fourteen below
are Unassigned."* That wording is **ours**, not RFC 8610's. RFC 9741 §4
registers fourteen further names, and RFC 9741 §1 states that RFC 9090 and
RFC 9165 had already added others. The registry holds **at least 28** and
strictly more. The same file's `counts.operators: 14` is correct as "the
fourteen RFC 8610 defines" and false as a statement of registry state, and its
`grammar-gaps.derived.txt` item **G-11**, headed "§3.8 (all fourteen
operators)", must be read as RFC 8610's fourteen. **The gaps themselves are
unaffected and none of the 44 is closed** (§7). This is a fix to one of our
derived files, not to any quotation of RFC 8610.

**`draft-mcnally-deterministic-cbor` — nothing is invalidated, and one claim is
strengthened.** Its design notes call dCBOR §2.7 *"the only answer to condition
(6) any document we hold supplies"*. That survives, and is now stronger than
when it was written: the IETF's 2025 document on *text conversion and
processing in CDDL* adds no normalisation operator and says the
canonical-text-form class is future work. dCBOR remains the only answer we
hold, and `R-O-05`'s normalise-at-authoring route remains the only
citation-compatible alternative.

**`rfc-8949` — unaffected.** §2.4 and §3.1 both cite it (the §6.2 JSON-to-CBOR
rules and the §3.2.3 string-concatenation algorithm) and neither citation
disturbs anything in that record.

---

## 10. Open questions

1. **`.hexlc` or `.hexuc` for `ArtifactId.digest.hex`?** A one-line ADR
   decision that must be taken rather than defaulted, because `.hex` admits
   both and is the name a reader will assume. Owner: D4 (2026-10-21).
2. **Does the name-chain normalisation rule go in `R-O-05` or in `ARCH-0002`
   P1?** §1.3 produces a rule neither document has. It is about *identity*, so
   P1 is the better home; `R-O-05` is where canonicalisation timing lives.
   `mofn#72` already owns an `ARCH-0002` P5 amendment for condition (2); this
   may belong with it.
3. **Does the project accept a CDDL schema at all, given cut 1?** If an
   extension point must be key-relative under P1, and a control operator is an
   extension point, then a CDDL schema is already a registry dependency. The
   honest answers are (a) accept CDDL as a *tooling* artifact and not as the
   normative model, or (b) treat the dependency as acceptable because it is on
   a *language* rather than on a *vocabulary*. [analysis] (b) is defensible and
   nobody has written it down; the ADR should.
4. **Do we need `.b45` for a QR demo?** §5. Cheap to answer, and the only
   reason to care about an operator we would otherwise ignore.
5. **Is a `profile: partial` schema acceptable for D4 given §3.3?** `Validity`
   has no usable text form in CDDL after this document. D4 is "encoding-neutral
   schema"; a schema that cannot state its timestamps has to say so.

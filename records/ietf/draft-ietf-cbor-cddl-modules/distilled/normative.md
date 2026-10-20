---
record: draft-ietf-cbor-cddl-modules
kind: normative
title: "draft-ietf-cbor-cddl-modules — normative statements"
extracted: "2026-10-19"
reviewed_by: ""
---

<!-- Every normative statement, VERBATIM, with its locator. Keep the source's
section structure as headings. Drop motivation, history, acknowledgements. -->

Source: draft-ietf-cbor-cddl-modules-07, "CDDL Module Structure", Bormann &
Moran, 2 September 2026, Intended status: Standards Track, **Expires 6 March
2027**. sha256 `7cf825aaad43d3d4995bcd540d3865ee3f69dd3dd453be5761a02c009458a644`
(784 lines, 26 KB, plain text). Quotations are verbatim from the plain-text
Internet-Draft. Blocks that reproduce the grammar, a directive, a command line
or a composed model preserve the source's own line breaks and indentation
inside fenced blocks.

**Why this file has no MUST in it.** `bin/bcp14-count` reports **0** BCP 14
keyword occurrences in 26 KB. That is not a measurement error and not a
deficiency in the draft: this is a **language-structure** document, and its
normativity is carried by a **grammar** (Appendix A, ten productions) and by
**composition rules** stated as definitions — what a module *is*, what
`include` and `import` *draw in*, what the `as` clause *does to a name*. A
rule about the shape of a file has almost no occasion to say that somebody
MUST do something. The document says as much structurally: the only actor
sentences it contains are in §2.7 and §3, and all five use a lower-case force
word (`may provide`, `need to ascertain`, `needs to undergo`, `needs to be
considered`, `should strive`). The precedents in this library are
`rfc-8610` (2 keywords in 125 KB, 137 of 139 requirements `inferred`) and
`draft-ietf-cbor-edn-literals` (10 keywords in 168 KB, 205 of 226 `inferred`).

**§1.1's BCP 14 boilerplate is deliberately never quoted here or in
`requirements.yaml`.** The paragraph at source lines 146–150 recites all eleven
keywords and constrains nothing; `bin/validate` counts our requirement texts
with boilerplate stripping **off**, so quoting it would add eleven phantom
keywords to a document that uses none. The fact that the draft *declares*
BCP 14 applicable and then never exercises it is recorded in
`requirements.yaml`'s `reconciliation` and in `design-notes.md`, which is where
it belongs.

**Normative scope, as the document itself states it.** The draft marks exactly
one of its two appendices: **Appendix B opens "This appendix is for information
only."** (source line 692). **Appendix A carries no such disclaimer** and is
introduced as the grammar the directives employ, so it is read here as
normative. §4 is one sentence. There is no other statement of scope.

**Conventions in this file.**

- A bullet `- (§X) "…"` is one contiguous verbatim span of the source. No span
  is spliced from two non-adjacent parts of the document. Contiguity is
  asserted after removing the running page decoration (`Bormann & Moran
  Expires 6 March 2027 [Page n]`, `Internet-Draft CDDL Module Structure
  September 2026`, form feeds) and collapsing runs of whitespace to one space,
  exactly as the mechanical check in this record's PR applies it. No interior
  word, clause or punctuation mark was altered, dropped or reordered. The
  source's RFC-style double space after a sentence period and the stray double
  spaces at `_Compatibility_:  bidirectional` and `(partial?)  URIs` are
  therefore rendered here as one space.
- The source's own cursive convention is preserved: `_module_`, `_basic CDDL_`,
  `_directives_`, `_identical_` and `_Compatibility_` in a quote are the
  draft's rendering of a term being introduced, not emphasis added here.
- **Hyphenation at a line break severs a token in three of the spans quoted
  below**, and each one carries the hyphen and the following space exactly as
  the normalised source renders them, with the break named in place: `follow-
  up` (§1, source lines 137/138), `Internet- Drafts` (§2.4, lines 267/268) and
  `module- structured` (Appendix B, lines 694/695). Not every hyphen before a
  space is a break: **`backward- and forward-compatible`** in §1 is a suspended
  hyphen the source writes on one line (line 130), and the trailing `-` on
  every `$ cddlc -2tcddl -` command line is the tool's stdin argument.
- **No normative sentence in this document is cut by a page frame.** All
  thirteen page breaks fall in blank space, in the table of contents, in the
  reference list or between a sentence and a display block. Appendix A's
  grammar sits in **one** unbroken region (lines 677–688). This is unusual for
  this family of documents — `rfc-8610` and `draft-ietf-cbor-edn-literals` each
  had a load-bearing sentence severed by the page furniture — and it is stated
  here because it was checked, not assumed.
- Bullet markers (`*  `) in §2.5 are layout and are not part of the quoted
  text.

---

## Document status and stability

The draft's own front matter and boilerplate, because this record cites an
unstable document and `design-notes.md` costs that out.

- (front matter) "Expires: 6 March 2027"
- (front matter) "Intended status: Standards Track"
- (front matter) "2 September 2026"
- (title block) "draft-ietf-cbor-cddl-modules-07"
- (Status of This Memo) "Internet-Drafts are draft documents valid for a maximum of six months and may be updated, replaced, or obsoleted by other documents at any time."
- (Status of This Memo) "It is inappropriate to use Internet-Drafts as reference material or to cite them other than as "work in progress.""
- (Status of This Memo) "This Internet-Draft will expire on 6 March 2027."
- (About This Document) "This note is to be removed before publishing as an RFC."
- (About This Document) "Source for this draft and an issue tracker can be found at https://github.com/cbor-wg/cddl-modules."

---

## §1. Introduction

The Abstract (source lines 17–27) is **word-for-word identical** to the first
three paragraphs of §1 (lines 121–131); it is quoted once, here, and not
double-counted.

- (§1) "At the time of writing, the Concise Data Definition Language (CDDL) is defined by RFC 8610 and RFC 9682 as well as RFC 9165 and RFC 9741."
- (§1) "The latter two have used the extension point provided in RFC 8610, the _control operator_."
- (§1) "As CDDL is being used in larger projects, the need for features has become known that cannot be easily mapped into this single extension point."
- (§1) "The present document defines a backward- and forward-compatible way to add a module structure to CDDL."
- (§1) "The functionality of the present document is considered a core part of what has colloquially been called CDDL 2.0, and is intended to be used with (and orthogonal to) other recent specifications such as a small set of CDDL grammar updates [RFC9682] and an additional exercise of the control operator extension point [RFC9741] (a follow- up to [RFC9165])." — *`follow-` / `up` is severed by the line break at source lines 137/138.*

## §1.1. Conventions and Definitions

- (§1.1) "The Terminology from [RFC8610] applies."
- (§1.1) "Some examples use CDDL definitions from [RFC9052]."

The third paragraph of §1.1 is the BCP 14 boilerplate and is deliberately not
quoted; see *Conventions in this file* above.

---

## §2. Module superstructure

§2 opens with a labelled property rather than a sentence:

- (§2) "_Compatibility_: bidirectional (both backward and forward)"

The problem statement, in the document's own words:

- (§2) "Originally, CDDL was used for small data models that could be expressed in a few lines."
- (§2) "As the size of data models that need to be expressed in CDDL has increased, the need to modularize and re-use components is increasing."

What basic CDDL already had, and what it costs — **this is the paragraph that
fixes the baseline the rest of the document is measured against**:

- (§2) "CDDL as documented in [RFC8610] (_basic CDDL_) has been designed with a crude form of composition: Concatenating a number of CDDL snippets creates a valid CDDL data model unless there is a name collision (_identical_ redefinition is allowed to facilitate this approach)."
- (§2) "With larger models, managing the overall name space to avoid collisions becomes more pressing."
- (§2) "In CDDL's original composition model, the knowledge which CDDL snippets need to be concatenated in order to obtain the desired data model lives entirely outside the CDDL snippets."
- (§2) "With the module structure defined in the present document, rule sets are packaged as modules and referenced from other modules, providing methods for control of namespace pollution."

What is **not** in this document, stated by the document:

- (§2) "Further work may be expended on unambiguous referencing into evolving specifications ("versioning") and selection of alternatives (as was emulated with snippets in Section 11 of [RFC8428]."
- (§2) "Note that one approach for expressing variants is demonstrated in [useful] based on Section 4 of [RFC9165])."
- (§2) "Potential further work is outlined in Sections 4 and A.2 of [I-D.bormann-cbor-cddl-2-draft]."

*The opening parenthesis of the first of those three sentences is closed only
at the end of the second — the parenthetical runs across a sentence boundary
and encloses a full stop. Recorded as printed; see `README.md`, defect 7.*

## §2.1. Compatibility

- (§2.1) "To achieve the module structure in a way that is friendly to existing environments that operate with CDDL and basic CDDL implementations, we add a super-syntax (similar to the way pragmas are often added to a language), by carrying them in _directives_."
- (§2.1) "Directives are parsed as comments in basic CDDL, so that each module source file can at the same time be basic CDDL on its own."
- (§2.1) "This enables forward compatibility: a single file can be designed to serve both as valid basic CDDL and as a module with directives that specify how additional rule definitions are to be imported from other source files."
- (§2.1) "This bidirectional compatibility is useful to allow CDDL model designers to start using directives before the bulk of the tools that process CDDL has been updated to implement the present specification."

## §2.2. Namespacing

- (§2.2) "When importing rules from other modules, there is the potential for name collisions."
- (§2.2) "This is exacerbated when the modules evolve, which may lead to the introduction of a name into an imported module that is also used (likely in a different way) in the importing module."
- (§2.2) "To be able to manage names in such a way that collisions can be avoided, we introduce means to prepend a prefix to the names of rules being imported: the "as" clause."

## §2.3. "Directives", the "module"

- (§2.3) "This specification introduces _directives_ into CDDL."
- (§2.3) "A single CDDL file becomes a _module_ by processing the (zero or more) directives in it."
- (§2.3) "The semantics of the module are independent of the module(s) using it, however, importing a module may involve transforming its rule names into a new namespace (Section 2.2)."
- (§2.3) "Directives are parsed as comments in basic CDDL, so they do not interfere with forward compatibility."
- (§2.3) "In the CDDL module structure, lines that start with the prefix ;# are parsed as directives."

## §2.4. Naming and Finding Modules

- (§2.4) "We assume that module names are filenames taken from one of several source directories available to the CDDL module structure processor via the environment."
- (§2.4) "This avoids the need to nail down brittle pathnames or (partial?) URIs into the CDDL files."
- (§2.4) "The exact way how these source directories and possibly a precedence between them are established is intentionally not fully defined in this specification; it is expected that this will be specified in the context of the models just as the way they are intended to be used will be."
- (§2.4) "(A more formal structure may follow later.)"

The one worked resolution mechanism the document describes is the tool's, not
the specification's:

- (§2.4) "In the module structure implementation that is part of the CDDL Tool described in Appendix B, the set of sources is determined from an environment variable, CDDL_INCLUDE_PATH, which is modeled after usual command-line search paths."
- (§2.4) "It is a colon-separated list of pathnames to directories, with one special feature: an empty element points to the tool's own collection."
- (§2.4) "This collection contains fragments of extracted CDDL from published RFCs, using names such as rfc9052."
- (§2.4) "(Future versions might augment this with Web extractors and/or ways to extract CDDL modules from sites such as github and from Internet- Drafts; see Appendix A.2 of [I-D.bormann-cbor-cddl-2-draft] for some design considerations.)" — *`Internet-` / `Drafts` is severed by the line break at source lines 267/268.*
- (§2.4) "The default CDDL_INCLUDE_PATH is:"

The default, as the source prints it (one line, source line 273):

```
   .:
```

- (§2.4) "That is: files are found in the current directory (.) and, if not found there, cddlc’s collection." — *the apostrophe in `cddlc’s` is U+2019 in the source bytes, not an ASCII apostrophe.*
- (§2.4) "In the examples that follow, a cddlc command line will be shown (starting with an isolated $ sign as in a shell command) with the module-structured CDDL input; the resulting basic CDDL will be shown separately."

## §2.5. Basic Set of Directives

- (§2.5) "Two groups of directives are defined at this point:"
- (§2.5) "include, which includes all the rules from a module (which includes the ones imported/included there, transitively), or specific explicitly selected rules (clause ending in "from");"
- (§2.5) "import, which is similar to include but includes only those rules from the module that are referenced from the importing module, implicitly or explicitly (clause ending in "from"), including the rules that are referenced from these rules, transitively."
- (§2.5) "The include function is more useful for composing a single model from parts controlled by one author, while the import function is more about treating a module as a library:"
- (§2.5) "The way an import works is shown by this simple example:"

The example, verbatim (source lines 309–311) — the command line, then the
module-structured input:

```
   $ cddlc -2tcddl -
   start = COSE_Key
   ;# import rfc9052
```

- (§2.5) "This results in the following CDDL 1.0 specification:"

The composed output, verbatim (source lines 315–325):

```
   start = COSE_Key
   COSE_Key = {
     1 => tstr / int,
     ? 2 => bstr,
     ? 3 => tstr / int,
     ? 4 => [+ tstr / int],
     ? 5 => bstr,
     * label => values,
   }
   label = int / tstr
   values = any
```

- (§2.5) "This is appropriate for using libraries that are well known to the importing specification."
- (§2.5) "However, if it is not acceptable that the library can pollute the namespace of the importing module, the import directive can specify a namespace prefix ("as" clause):"

The prefixed example, verbatim (source lines 341–343):

```
   $ cddlc -2tcddl -
   start = cose.COSE_Key
   ;# import rfc9052 as cose
```

- (§2.5) "This results in the following CDDL 1.0 specification:"

Its composed output, verbatim (source lines 347–357):

```
   start = cose.COSE_Key
   cose.COSE_Key = {
     1 => tstr / int,
     ? 2 => bstr,
     ? 3 => tstr / int,
     ? 4 => [+ tstr / int],
     ? 5 => bstr,
     * cose.label => cose.values,
   }
   cose.label = int / tstr
   cose.values = any
```

- (§2.5) "Note how the imported names are prefixed with cose. as specified in the import directive, but CDDL prelude (Appendix D of [RFC8610]) names such as tstr and any are not."

## §2.6. Explicit selection of names

- (§2.6) "Both import and include directives can be augmented by an explicit mentioning of rule names (clause ending in "from") or a wild-card "*" for all rules."

### §2.6, "include"

- (§2.6 include) "Starting with include:"

Verbatim (source lines 373–375):

```
   $ cddlc -2tcddl -
   mydata = {* label => values}
   ;# include label, values from rfc9052
```

- (§2.6 include) "With include, only exactly the rules mentioned are included:"

Verbatim (source lines 379–381):

```
   mydata = {* label => values}
   label = int / tstr
   values = any
```

- (§2.6 include) "The module from which rules are explicitly imported can be namespaced:"

Verbatim (source lines 386–388):

```
   $ cddlc -2tcddl -
   mydata = {* label => values}
   ;# include cose.label, cose.values from rfc9052 as cose
```

- (§2.6 include) "Again, only exactly the rules mentioned are included:"

Verbatim (source lines 399–401):

```
   mydata = {* label => values}
   cose.label = int / tstr
   cose.values = any
```

### §2.6, "import"

- (§2.6 import) "Both examples would work exactly the same with import, as the included rules do not reference anything else from the included module."
- (§2.6 import) "An import however also draws in the transitive closure of the rules referenced:"

Verbatim (source lines 412–414):

```
   $ cddlc -2tcddl -
   mydata = {Fritz: cose.empty_or_serialized_map}
   ;# import cose.empty_or_serialized_map from rfc9052 as cose
```

- (§2.6 import) "The transitive closure of the rules mentioned is included:"
- (§2.6 import) "=============== NOTE: '\' line wrapping per RFC 8792 ================"

Verbatim (source lines 420–435), **including the RFC 8792 `\` wrap the source
prints** — the only two blocks in the document that carry one are this and the
next. `schema/cose-closure-unfolded.derived.cddl` holds the unwrapped form:

```
   mydata = {Fritz: cose.empty_or_serialized_map}
   cose.empty_or_serialized_map = bstr .cbor cose.header_map / bstr .\
                                                                  size 0
   cose.header_map = {
     cose.Generic_Headers,
     * cose.label => cose.values,
   }
   cose.Generic_Headers = (
     ? 1 => int / tstr,
     ? 2 => [+ cose.label],
     ? 3 => tstr / int,
     ? 4 => bstr,
     ? (5 => bstr // 6 => bstr),
     )
   cose.label = int / tstr
   cose.values = any
```

- (§2.6 import) "The import statement can also request an alias for an imported name:"

Verbatim (source lines 439–441) — note that the selected name is written
**without** the prefix here, where line 414 wrote it **with** the prefix:

```
   $ cddlc -2tcddl -
   mydata = {Fritz: cose.empty_or_serialized_map}
   ;# import empty_or_serialized_map from rfc9052 as cose
```

- (§2.6 import) "Note how an additional rule provides an alias for empty_or_serialized_map that does not have the namespace prefix:"
- (§2.6 import) "=============== NOTE: '\' line wrapping per RFC 8792 ================"

Verbatim (source lines 455–471):

```
   mydata = {Fritz: cose.empty_or_serialized_map}
   empty_or_serialized_map = cose.empty_or_serialized_map
   cose.empty_or_serialized_map = bstr .cbor cose.header_map / bstr .\
                                                                  size 0
   cose.header_map = {
     cose.Generic_Headers,
     * cose.label => cose.values,
   }
   cose.Generic_Headers = (
     ? 1 => int / tstr,
     ? 2 => [+ cose.label],
     ? 3 => tstr / int,
     ? 4 => bstr,
     ? (5 => bstr // 6 => bstr),
     )
   cose.label = int / tstr
   cose.values = any
```

## §2.7. Tool Support for Command-Line Control

- (§2.7) "Tools may provide a convenient way to initiate the processing of directives from the command line."
- (§2.7) "A tool may provide a way to specify a root for the module tree from the command line:"

Verbatim (source line 481):

```
   $ cddlc -2tcddl -icose=rfc9052 -scose.COSE_Key
```

- (§2.7) "The command line argument -icose=rfc9052 is a shortcut for"

Verbatim (source line 485):

```
   ;# import rfc9052 as cose
```

- (§2.7) "Together with the start (root) rule name, cose.COSE_Key, supplied by -scose.COSE_Key, this results in the following CDDL 1.0 specification:"

Verbatim (source lines 509–519). The synthesized root rule is spelled
`$.start.$`, which appears exactly once in the document and is nowhere
defined:

```
   $.start.$ = cose.COSE_Key
   cose.COSE_Key = {
     1 => tstr / int,
     ? 2 => bstr,
     ? 3 => tstr / int,
     ? 4 => [+ tstr / int],
     ? 5 => bstr,
     * cose.label => cose.values,
   }
   cose.label = int / tstr
   cose.values = any
```

- (§2.7) "In other words, the module synthesized from the command line had an empty CDDL file, which therefore was not provided (no – was given on the command line)." — *the dash in `(no – was given` is U+2013 EN DASH in the source bytes where the sense requires the ASCII `-` of the stdin argument; see `README.md`, defect 5.*

---

## §3. Security Considerations

- (§3) "The module structure specified in this document is not believed to create additional security considerations beyond the general security considerations in Section 5 of [RFC8610]."
- (§3) "Implementations that employ the module structure defined in this document need to ascertain the provenance of the modules they combine into the CDDL models they employ operationally."
- (§3) "This specification does not define how the source directories accessed via the CDDL_INCLUDE_PATH are populated; this process needs to undergo the same care and scrutiny as any other introduction of source code into a build environment; the possibility of supply-chain attacks on the modules imported needs to be considered."
- (§3) "Specifically, implementations that rely on model-based input validation for enforcing certain properties of the data structure ingested (which, if not validated, could lead to malfunctions such as crashes and remote code execution) need to be particularly careful about the data models they apply, including their provenance and potential changes of these properties that upgrades to the referenced modules may (inadvertently or as part of an attack) cause."
- (§3) "More generally speaking, implementations should strive to be robust against limitations of the model-based input validation mechanisms and their implementations that they employ."
- (§3) "In applications that dynamically acquire models and dereference module references in these, the security considerations of dereferenceable identifiers apply (see [I-D.bormann-t2trg-deref-id] for a more extensive discussion of dereferenceable identifiers)."

## §4. IANA Considerations

- (§4) "This document has no IANA actions."

That is the whole section. It is quoted here because it is the document's own
answer to the question `design-notes.md` §*Does module naming need an
authority?* asks: the specification allocates nothing and registers nothing.

---

## Appendix A. ABNF Specification

Appendix A carries **no** "for information only" line, in contrast with
Appendix B, so it is read here as normative.

- (Appendix A) "This section specifies the grammar employed by the module structure directives using the ABNF language defined in [STD68] and [RFC7405]."

The grammar is **not** re-typed here. It is this record's
`distilled/schema/module-directives.abnf`, captured byte-for-byte from source
lines 677–688 with the Internet-Draft's three-column margin intact (region
sha256 `43c17148af31265a171f2e722b24d2e0063d0ab253d8b681cc1c223d5df696ab`),
with a margin-removed companion at
`module-directives-dedented.derived.abnf`. Each of its ten productions is
carried as an individual requirement in `requirements.yaml`
(`R-0078`–`R-0087`), because here the productions *are* the obligations.
*[corrected in pass 2: this pointer previously read `R-0073`–`R-0082`, which
lands on §3's security sentences and the first five productions. The ten
productions are `R-0078`–`R-0087`, as `requirements.yaml`'s own `note` and
`reconciliation` both say.]*

Three properties of that grammar that no sentence of the document states, and
which `schema/grammar-gaps.derived.txt` records in full:

1. `id` admits neither `-` nor `.`, so it is **strictly narrower** than
   RFC 8610's `id`, and it cannot match the dotted selectors
   `cose.label`, `cose.values` and `cose.empty_or_serialized_map` that §2.6's
   own examples write in a `from` clause.
2. `CRLF` is redefined as `%x0A / %x0D.0A`, admitting a bare LF where STD 68's
   core rule is CR LF — and the appendix says nothing about having done so.
   The **substance** of that relaxation is deliberate, customary practice:
   RFC 9165 §3 makes the byte-identical redefinition and *declares* it ("As is
   customary for ABNF, the syntax of ABNF itself (_not_ the syntax expressed in
   ABNF!) is relaxed to allow a single line feed as a newline",
   `rfc-9165#R-0053`). What this appendix lacks is that sentence. The gap is
   therefore a **documentation** gap, not a grammar error (`README.md`
   defect 4, `schema/grammar-gaps.derived.txt` G-02).
3. `directive` requires `RS` (one or more spaces) after `";#"`, where §2.3's
   prose requires only that the line "start with the prefix ;#".

## Appendix B. A CDDL Tool that Implements CDDL Module Structure

- (Appendix B) "This appendix is for information only."
- (Appendix B) "A CDDL conversion tool is available [cddlc] that can process module- structured CDDL models into basic CDDL models; the latter can then be processed by other CDDL tools such as the one described in Appendix F of [RFC8610]." — *`module-` / `structured` is severed by the line break at source lines 694/695.*
- (Appendix B) "A typical command line involving both tools mentioned might be:"

Verbatim (source line 701) — note `-2 -tcddl` as two arguments, where every
example in §2.5–§2.7 writes `-2tcddl` as one:

```
   cddlc -2 -tcddl mytestfile.cddl | cddl - gp 10
```

- (Appendix B) "The CDDL conversion tool can be installed on a system with a modern Ruby (Ruby version ≥ 3.0) via:" — *`≥` is U+2265 in the source bytes.*

Verbatim (source line 706):

```
   gem install cddlc
```

- (Appendix B) "The present document assumes the use of cddlc of at least version 0.2.5."

## Acknowledgments

The section is a single unresolved placeholder line in revision -07. Its
content is **not quoted** anywhere in this record: it is the all-capitals
four-letter placeholder token followed by the word `acknowledge`, and
`bin/validate` rejects that token as a literal string inside any file under
`distilled/` (`docs/extraction.md`, *Definition of done*). The placeholder is
recorded as `README.md` defect 8 instead.

---

## What the document does **not** say

Each of these was searched for mechanically across the full 784 lines, and the
absence is part of the extraction. The grep counts are in `README.md`.

- **No `export` directive, and no statement of what a module exports.**
  `export`, `private` and `visib`(le/ility) occur **zero** times; `public`
  occurs **once**, inside "date of publication" in the copyright boilerplate
  (line 80). Selection is stated only from the **consumer** side (§2.5, §2.6).
- **No mention of sockets or plugs.** `socket`, `plug` and `$$` occur **zero**
  times. RFC 8610 §3.9's extension mechanism is neither amended nor exempted,
  and the document never says whether a socket name is prefixed by an `as`
  clause.
- **No mention of `/=` or `//=`.** Those two spellings occur **zero** times, so
  the document says nothing about how RFC 8610's accretive choice, which
  §3.9 of that RFC says "is populated in the order the rules are given",
  behaves under composition.
- **No statement of the order in which composed rules are emitted.** The word
  `order` occurs **once** in the whole document (line 181, "in order to obtain
  the desired data model") and is not about output order; `precedence` occurs
  **once** (line 252) and is explicitly left undefined; `determined` occurs
  **once** (line 259) and is about the tool's set of source directories.
- **No conflict rule for two `as` clauses that choose the same prefix**, and no
  rule for an `as` prefix that collides with a rule the importing module
  defines itself.
- **No example of the wild-card `*`** that §2.6's first sentence and Appendix
  A's `id-or-all` both admit, and no statement of how `include * from m`
  differs from `include m`.
- **No versioning and no variant selection** — §2 says so itself and points at
  `[I-D.bormann-cbor-cddl-2-draft]`, a second Internet-Draft, for the design
  considerations.
- **No definition of `$.start.$`**, the synthesized root rule name §2.7's
  output uses once.

---
record: draft-ietf-cbor-cddl-modules
kind: design-notes
title: "draft-ietf-cbor-cddl-modules — bearing on our design"
extracted: "2026-10-19"
reviewed_by: ""
---

**Scope and provenance conventions.** Section numbers with no document name
(`§2.4`) are `draft-ietf-cbor-cddl-modules-07`. Requirement ids with no record
prefix (`R-0046`) are this record's `distilled/requirements.yaml`; ids with one
(`rfc-8610#R-0079`) are that record's. Our own documents are cited by id
(`ARCH-0002 P1`, `MD-3`, `R-M-12`, `R-O-03`). Four markers distinguish voices:

- unmarked prose reports **the draft** or **our decisions**, as cited;
- **[analysis]** marks reasoning of this extraction that neither the source nor
  our documents state;
- **[correction]** marks a working assumption of the project that the sources
  do not support;
- **[beyond source]** marks a point where this extraction had to reason past
  both the draft and our own documents.

**Decision status, stated plainly.** DEC-002 in `ARCH-0001` §7 (v0.1.1) lists
**four** options. "Option 5" exists only as *proposed* text in
`ARCH-0001-PROPOSAL-v0.2.0` §3.3; that proposal is unmerged and `ARCH-0001`
still carries DEC-002 under "Open decisions". `ADR-0001` (accepted) constrains
DEC-002 and says option 2 "as originally written does not" remain on the table.
`MD-3` (2026-09-28) narrows DEC-002 to option 5. **No ADR for DEC-002 has been
written**, and `DECISIONS-0001` tier 1 item 2 says so in terms: "a narrowing is
not an acceptance". Nothing below may be read as an accepted encoding decision.

**Provenance of the source read.** `draft-ietf-cbor-cddl-modules-07`, dated
**2 September 2026** on its own front page, authors Bormann (Universität Bremen
TZI) and Moran (Arm Limited), "Intended status: Standards Track",
"Expires: 6 March 2027". The cached bytes match `record.yaml`'s
`content.sha256` (`7cf825aa…a644`, retrieved 2026-09-22). **Not expired as of
this extraction** (2026-10-19): 138 days of nominal validity remain. §*The cost
of an unstable reference* below treats that as a finding rather than a
footnote, because this draft is unusual in depending on **two further**
Internet-Drafts for its own substance.

**Why this record exists.** `rfc-8610` reached `profile: full` on 2026-10-19
carrying a gate in both its `distilled/README.md` and its `summary.md`: *nothing
in that record may be treated as the current state of CDDL until `rfc-9165`,
`rfc-9682`, `rfc-9741` and this draft are read.* This is one of the four that
closes it. Two findings of that extraction made this record's own
`usefulness.reason` — "Relevant the moment our schema stops being one file" —
concrete, and they are the two questions answered first below.

---

## The two questions, answered first

### 1. Does a module system give CDDL a real boundary between a native schema and an export schema?

**No. `rfc-8610`'s finding stands unchanged, and this document is the strongest
possible evidence for it** — because a module system is exactly where such a
boundary would live, and this one declines to put it there.

`rfc-8610`'s extraction concluded (`design-notes.md` §3c, open question 4) that
"nothing in the language distinguishes a native schema from an export schema,
and a tool cannot tell them apart", that §3.9's sockets "do not separate files"
because a tool honours an undefined socket by *not raising an error*
(`rfc-8610#R-0079`), and that the remedy therefore has to be filename and header
convention plus our own CI, exactly as this library's `.derived.` rule already
is. Four facts from this draft, each with its id:

1. **There is no export construct, and no statement of what a module exports.**
   `export`, `private` and `visib`(le/ility) occur **zero** times in 784 lines;
   `public` occurs once, inside "date of publication" in the copyright
   boilerplate. Every one of the five selection forms is written by the
   **consumer**: `R-0046`, `R-0047`, `R-0054`, `R-0056`, `R-0060`. The producer
   declares nothing.
2. **`include` reaches *through* a module into its own dependencies.** `R-0046`:
   include draws in "all the rules from a module (which includes the ones
   imported/included there, transitively)". **[analysis]** So a module cannot
   make a rule private, *and adding an import to a module changes what its
   consumers' `include` draws in* — a non-local effect with no declaration
   anywhere to constrain it.
3. **Module-hood is never declared.** `R-0030`: "A single CDDL file becomes a
   _module_ by processing the (zero or more) directives in it." Zero is allowed,
   so **every basic CDDL file is already a module**. There is no file-level
   marker, no manifest, no header. The only thing a module says about itself is
   what it *imports*, and it says it in comments (`R-0023`) that every
   pre-existing tool is required to ignore.
4. **The one boundary the document does give is semantic, not nominal, and it
   says so in one sentence.** `R-0031`: "The semantics of the module are
   independent of the module(s) using it, however, importing a module may
   involve transforming its rule names into a new namespace." **[analysis]**
   That is real and worth having — a module means the same thing wherever it is
   used — but it is encapsulation of *meaning* with explicit non-encapsulation
   of *names*, and it is the opposite of what a native/export split needs, which
   is a boundary on *visibility*.

**And the compatibility claim is weaker than it reads.** §2.1 says "each module
source file can at the same time be basic CDDL on its own" (`R-0023`). Checked
mechanically against all six module files the document prints: **every one of
them, read as basic CDDL alone, has at least one rule name that resolves to
nothing** — `COSE_Key`, `cose.COSE_Key`, `label` and `values`,
`cose.empty_or_serialized_map` (`examples/README.md` has the table). That is by
design, since the dangling name is what the directive resolves. But it fixes
the sense of the claim: **"basic CDDL on its own" is lexical, not semantic.**
RFC 8610's only dispensation for an undefined name is §3.9's socket convention
— "Tools honor that convention by not raising an error if such a type or group
is not defined at all" (`rfc-8610#R-0079`) — and it applies **only** to names
beginning `$` or `$$`, which none of these are. **[analysis]** So an un-updated
tool reading a module file gets a model with unresolvable references, and
nothing in either document says what it does with one. This is the same
"honours it by not raising an error" failure mode `rfc-8610` identified, one
level up: silence as success, now about whole files.

**What *is* new, and it is genuinely useful to us.** `R-0034`: "module names are
filenames". The language's own module identity *is* a filename. **[analysis]**
So this library's `.derived.` discipline, and the filename-and-CI remedy
`rfc-8610` proposed for the native/export split, stop being a workaround around
the language and become **the mechanism the language itself uses**. If D4 names
`statement.cddl` and `statement-cose-export.cddl` and enforces the split in CI,
it is not substituting for a missing CDDL feature — it is supplying the half of
CDDL's own module mechanism that the specification deliberately left to "the
context of the models" (`R-0036`).

### 2. Does module naming fix the socket-collision failure `ARCH-0002` P1 exists to fix, or reproduce it?

**It relocates it. For sockets specifically, it does not address it at all —
and its own namespacing mechanism cannot be applied to a socket without
breaking it.**

`rfc-8610`'s extraction found that a socket name is "a *flat global name* within
whatever set of files is concatenated", that two parties plugging
`$$statement-extensions` collide "because no principal is attached", and that
this is "word for word `ADR-0001`'s rejection of private-use ranges: *private
use gives escape from a registry, not a namespace*". Four findings here.

**(a) Module names carry no principal, no version and no digest, and URIs are
explicitly refused.** `R-0081`: `filename` admits `-`, `.`, digits, `A-Z`, `_`
and `a-z` and **no `/`** — so a module namespace is **flat**, with no hierarchy
and no path. `R-0034`: the name is resolved against "source directories
available to the CDDL module structure processor via the environment".
`R-0036`: how those directories and "possibly a precedence between them are
established is **intentionally not fully defined** in this specification".
`R-0035`: this "avoids the need to nail down brittle pathnames or (partial?)
URIs into the CDDL files". **[analysis]** The refusal in `R-0035` is the load-
bearing one: a URI is the one spelling that would have made a module reference
describe its own origin, and it is declined on ergonomic grounds. The document
then names the consequence itself, in §3: implementations "need to ascertain the
provenance of the modules they combine" (`R-0071`), and "the possibility of
supply-chain attacks on the modules imported needs to be considered"
(`R-0072`). **And the default search path puts the current directory first**
(`R-0043`): a local file named `rfc9052` shadows the curated RFC 9052 extract,
silently, with no diagnostic specified anywhere. That is dependency confusion
as the default, in the default.

**(b) The `as` prefix renames into the same flat space; it does not create a
scope.** `R-0028`: the mechanism is to "prepend a prefix to the names of rules
being imported". The emitted names are ordinary basic-CDDL rule names —
`cose.COSE_Key`, `cose.label`, `cose.Generic_Headers` — because `.` is a legal
interior character of an RFC 8610 `id`. **[analysis]** After composition there
is exactly one flat global name space, the same one RFC 8610 has; prefixing
makes names longer, not scoped. The prefix is chosen by the **importer**
(`R-0052`) and bound to nothing, so the same module imported by two parties
carries two different prefixes, and two different modules can carry the same
one with no diagnostic specified (`schema/grammar-gaps.derived.txt` G-11). That
is `ADR-0001`'s rejected shape: escape from a collision, not a namespace.

**Said in the other direction, because an extraction that can only confirm is
not evidence.** The `as` prefix *is* **composer-relative naming**, and that is
the right *direction* for P1. P1 is `(defining key, local label)`; this is
`(composing file, local label)`. The local-label half transfers exactly — a
rule name means something relative to the thing that pulled it in, not
globally. What is missing is the principal, and nothing in CDDL has ever had
one. **[analysis]** So the honest verdict is: CDDL modules get one of P1's two
components and have no vocabulary for the other, and the component they get is
the one that was never the hard part.

**(c) Sockets are not mentioned, and either answer about them breaks
something.** `socket`, `plug` and `$$` occur **zero** times in the document.
RFC 8610 §3.9's one registry-free extension point is neither amended nor
exempted nor named. Appendix A's `id` admits `$` in every position (`R-0082`),
so a socket *is* selectable in a `from` clause; §2.2 states the prefixing rule
without exception (`R-0028`) and §2.5's only stated exception is the CDDL
prelude (`R-0053`). **[analysis]** Two readings:

- **sockets are prefixed.** Then `$$statement-extensions` becomes
  `cose.$$statement-extensions` and a plug written elsewhere as
  `$$statement-extensions /= …` no longer plugs it. Importing a module
  **silently disconnects its extension point.**
- **sockets are not prefixed.** Then the one construct CDDL offers as a
  registry-free extension point keeps a flat global name across every module in
  the build, and the collision the module structure exists to prevent persists
  for **precisely** the construct `rfc-8610`'s extraction identified as
  inheriting `ADR-0001`'s critique.

The document chooses neither. **So the answer to the question as asked is: a
module system does not fix the socket collision. It is silent about it, and its
namespacing mechanism is unusable on sockets without breaking the plug
relation.** Anyone proposing sockets as D4's key-relative extension mechanism
should be told this second, after `rfc-8610`'s finding.

**(d) On registries, this document is — unusually — *in option 5's favour*.**
§4 is one sentence: "This document has no IANA actions" (`R-0076`). It defines
no registry and depends on none. `rfc-8610`'s extraction concluded that option 5
is "registry-reduced, not registry-free", having dropped two registries and
adopted the CDDL control-operator registry; the caller's question was whether
module names would be a **fourth**. **They are not.** But the authority is not
absent — it is *unstated*: the only resolution mechanism the document actually
describes keys its bundled modules on **RFC numbers** (`R-0040`, "using names
such as rfc9052"), and that mechanism is scoped to one tool rather than to the
specification — §2.4 introduces it as what happens "in the module structure
implementation that is part of the CDDL Tool described in Appendix B"
(`R-0038`), and Appendix B, the only place that tool is specified, declares
itself "for information only" (`R-0088`). *[precision corrected in pass 2: the
`CDDL_INCLUDE_PATH` text is in §2.4, not inside the appendix. What is in the
appendix is the tool. `requirements.yaml`'s `field` for `R-0038` already had
this right.]* **[analysis]** So whoever populates
the search path is the name authority, and §3 says as much without using the
word. For `MD-3`: adopting CDDL modules adds **no registry dependency** and
does add a **build-reproducibility** dependency. Those are different costs and
only the first was ever scored.

### 3. Does `/=` and `//=` ordering survive module composition?

**The document is silent, and the silence is a regression in auditability
rather than a neutral omission.**

`/=` and `//=` occur **zero** times. There is **no statement of the order in
which composed rules are emitted**: `order` occurs once in the whole document
(line 181, "in order to obtain the desired data model") and is not about output
order; `precedence` occurs once (line 252) and is explicitly left undefined
(`R-0036`). All seven composed outputs the document prints are *consistent with*
"the importing module's own rules first, then the selected rules, then their
closure" — but that is induction from seven examples, not a rule
(`schema/grammar-gaps.derived.txt` G-12).

It matters because `rfc-8610`'s extraction established that an accretive choice
"is populated in the order the rules are given" (`rfc-8610#R-0102`) and that
"the first choice that matches wins" (`rfc-8610#R-0106`), and drew the
consequence that if D4 assembles schemas from plug files "the *concatenation
order of the files* is semantic" (open question 6). **[analysis]** This document
does not fix that and does not formalise it. It **moves** it: the old
non-determinism was the order of filenames in a build script — ugly, but
visible in a file we write and reviewable in a diff. The new one is the order in
which an unspecified resolver walks an import graph, over a search path whose
precedence the specification declines to define. **That is strictly worse for
us.** If D4's native schema uses `/=` or `//=` anywhere, a module build must be
pinned by a lockfile-equivalent, and no part of this mechanism provides one —
`R-0019` defers versioning to future work and `R-0035` refuses the digest-
bearing spelling.

---

## What we adopt

**The `as`-prefix spelling as a naming discipline, today, with no tool
support.** `R-0023` and `R-0032` are the whole of the compatibility mechanism:
a directive is a comment, so a basic CDDL tool ignores it. The *converse* is
what we can use now — the **prefixed rule names are just rule names**. Writing
`mofn.Statement`, `mofn.Threshold`, `cose.COSE_Key` in a single hand-assembled
file is valid RFC 8610 CDDL today, needs no `cddlc`, and is forward-compatible
with the module structure if it is ever standardised. `R-0053`'s prelude
exemption tells us where to stop: `tstr`, `int`, `bstr`, `any` and the other 36
prelude names stay bare.

**`R-0031`'s semantic independence as the property to aim for.** "The semantics
of the module are independent of the module(s) using it" is the right invariant
for a native schema that will also be exported, and it is one we can state in
prose and test with fixtures even where CDDL cannot enforce it.

**§3's provenance requirement as a build obligation we must discharge
ourselves.** `R-0071` and `R-0072` are the only sentences in the document that
put a force word on an actor about anything consequential, and they say the
mechanism does not carry provenance. So our build must: a digest per schema
file, recorded where a reviewer sees it. This library already does exactly that
for third-party documents (`content.sha256`, bytes never committed), so the
pattern is in hand.

**The two-file split the mechanism makes natural.** `rfc-8610` open question 4
asked "how are native and COSE-export schemas kept apart without CDDL
modules?" **[analysis]** This draft is the first CDDL document to supply *any*
vocabulary for the question — a native module and an export module, each a
file, composed by name — even though it supplies no enforcement. That is a
better starting point for the DEC-002/DEC-005 ADR than "filename convention,
because the language has nothing".

## What we adapt, and how

**Module name → module name plus digest.** `R-0034` makes the name a bare
filename; `R-0035` refuses URIs; `R-0019` defers versioning. **[analysis]** All
three gaps land on us, and the same remedy covers them: our schema filenames
carry the distinction (as `.derived.` already does) and CI carries the digest.
Under `R-O-03` this is not optional — "Canonicalization algorithm for each
concrete encoding SHALL be cited, not invented silently" — and a schema
composed from a module whose bytes nobody pinned is a silently invented schema.

**`import`, never unqualified `include`.** `R-0047`'s selection criterion is
reachability from the consumer; `R-0046`'s is everything, transitively, through
the module into its own dependencies. **[analysis]** The second is the one that
breaks review: a reviewer reading a file cannot see what an `include` three
modules down brought in, and under option 5 what it brought in might be a
`#6.nnn` production that the native model forbids. House rule for D4: explicit
`import … from … as …` only, and a CI lint on any other form.

**The composed output is a build artifact, not a source.** `R-0050` calls it
"CDDL 1.0". Checked against the document alone: **not one of the seven composed
outputs contains a single `;` character** (`schema/grammar-gaps.derived.txt`
G-17). Since directives *are* comments, the transformation is **one-way** — a
composed model cannot be read back as the module structure that produced it —
and every comment in every input module is discarded with them. **[analysis]
That is a direct cost to us, and a specific one.** `rfc-8610`'s extraction
found that four of `ARCH-0002` P3's five rows have no CDDL expression and that
§3.1's comments are not part of the language, so whatever a schema says about
*meaning* lives in comments. A module build deletes it. If D4 is composed rather
than hand-written, the semantics have to live in a document beside the CDDL,
which is `rfc-8610` open question 2 ("is D4 a CDDL file or a container that
carries one?") answered in the affirmative by a mechanical property of the
toolchain.

The cross-document half of this is attributed rather than asserted from this
source: the RFC 9052 fragments those outputs are drawn from *do* carry per-field
comments (`; kty`, `; kid`, `; alg`, `; criticality`, `; content type`,
`; key identifier`, `; IV`, `; Partial IV`), per this library's verbatim capture
at `records/ietf/rfc-9052/distilled/schema/cose.cddl` — its `COSE_Key` and
`Generic_Headers` fragments, under that file's own markers
`; §7 Key Objects -- COSE_Key` and
`; §3.1 Common COSE Header Parameters -- Generic_Headers`. *[correction
2026-10-20, cross-check pass: this cited "lines 60–67 and 168–175" of that
file — a cross-record citation by line number, the drift pass 2 repaired in
G-01. The ranges still hold; the citation form did not.]*
The rendering also drops the redundant inner parentheses of
`? 4 => [+ (tstr / int) ]`, reindents from four columns to two and adds a
trailing comma. **None of those changes the language** — an occurrence
indicator binds the whole following `type`, so `[+ tstr / int]` and
`[+ (tstr / int)]` denote the same thing, and `optcom` admits a trailing comma.
What is lost is the documentation.

## What we reject, and why

**`CDDL_INCLUDE_PATH` as part of our build.** `R-0043`: the default is the
current directory first, the curated collection second. **[analysis]** A
build whose dependency resolution can be changed by creating a file in the
working directory is not a build we can put a signature behind. If we use the
mechanism at all, the path is explicit, absolute and pinned, and `.` is not on
it.

**The alias form.** `R-0063` and `R-0064`: writing a selector without its prefix
emits an extra rule `name = prefix.name`, so the name then exists both prefixed
and unprefixed. **[analysis]** That reintroduces, for exactly the names it
aliases, the namespace pollution the `as` clause was introduced to prevent
(`R-0052`). It is a convenience with a cost and no marker. Reject it; write the
prefixed spelling everywhere.

**Any dependence on Appendix A's `id` as written.** It admits neither `-` nor
`.` (`R-0082`) and so cannot match the dotted selectors the document's **own**
§2.6 examples write (`schema/grammar-gaps.derived.txt` G-01), nor any rule name
containing a hyphen — and our model has `key-id`-shaped names in prospect.
Until that is fixed, the `from` clause is not a mechanism we can rely on.

---

## Where this cuts against MD-3, by DEC-002 option

`MD-3` narrowed DEC-002 to **option 5** on 2026-09-28 — CBOR data model, no
IANA tags, COSE export only, YAML as the human form. `docs/extraction.md`
requires this section to say where a source supports a different option or
exposes a cost option 5 pays and another does not. Five, and the second one goes
the other way.

### 1. A module graph is a build input that must be pinned — and options 1 and 3 have no module graph at all

**Affects options 2 and 5; costs options 1, 3 and 4's JSON half nothing.**

Everything in §*question 3* above — unspecified emission order, undefined
search-path precedence, no versioning, no digest — is a property of **composing
a schema from files**. Canonical S-expressions (option 1) have no schema
language and no module system to pin; JCS JSON (option 3) likewise. Option 4's
CBOR half inherits whatever option 2 does, and its JSON half does not.
**[analysis]** `MD-3`'s scoring axes were fidelity, tooling and ergonomics, and
`ARCH-0001-PROPOSAL-v0.2.0` §3.3 records that namespace governance was never
scored. **Build reproducibility was not scored either**, and it is a real
criterion the moment a schema stops being one file — which this record's own
`usefulness.reason` says WP1 will reach quickly. On that axis option 1 wins
because it has nothing to reproduce.

### 2. On registries this document *favours* option 5, and that is worth recording

**[analysis]** Four CDDL-family extractions in this library have now cut against
option 5 on namespace governance. This one does not. §4 is "This document has
no IANA actions" (`R-0076`): the module mechanism defines no registry and
depends on none, so the fourth registry the caller's question anticipated does
not exist. Option 5 remains "registry-reduced, not registry-free" on
`rfc-8610`'s finding (the control-operator registry), and modules do not make
it worse. **The qualification is real but narrower than a registry**: the
authority moved into the deployment environment rather than disappearing
(`R-0036`, `R-0040`, `R-0043`), and an unstated authority is harder to audit
than a named one even when it is not centrally allocated. Both halves belong in
the ADR.

### 3. Modules make option 5's unstateable exclusion easier to breach, not harder

**Affects option 5 uniquely, for the same reason §3c of `rfc-8610`'s notes
gave: it is the only option with both a declared export envelope and a native
prohibition on the same construct.**

`rfc-8610`'s extraction found that option 5's defining exclusion — no major type
6 — **cannot be stated in CDDL at all**, only enforced by a prohibition on
nineteen prelude names and on bare `any`, plus a decoder rule in the verifier.
Modules do not change that. **[analysis]** They make it reachable by a new
route: a single `include` of someone else's module readmits that module's whole
transitive closure (`R-0046`), including any `#6.nnn` production in it, with no
export declaration to inspect and — `R-0073` says this in the document's own
voice — with "potential changes of these properties that upgrades to the
referenced modules may (inadvertently or as part of an attack) cause". Under
option 5 that is a **native prohibition breached by a build action**. CI is the
only place it can be caught, and our CI does not currently look at CDDL at all.

### 4. The option CDDL supports natively is still option 4, and this document does not move that

`rfc-8610`'s extraction concluded that "option 4 is the only DEC-002 option
whose schema story RFC 8610 actually tells", because Appendix E *is* a
documented two-serialization account of one schema. **[analysis]** Modules are
orthogonal to that: they are per-file, Appendix E is per-schema, and nothing
here helps. And nothing here touches `MD-3`'s YAML human form — this is a CDDL
document, CDDL has no YAML, and the YAML↔CBOR mapping remains unowned
(`rfc-8610` open question 10).

### 5. `ARCH-0002` P1 gets its clearest negative result yet, and it is a standards-track one

**[analysis]** This is the document that *could* have given CDDL key-relative
naming. A module system is exactly where you would put it: you are already
introducing a notion of "whose name is this?", and the IETF process was open.
What it does instead is name modules by **filename** (`R-0034`), resolve them
through an **environment variable** (`R-0038`), prefix rules by a
**consumer-chosen string** (`R-0052`), **refuse URIs explicitly** (`R-0035`),
and allocate **nothing** (`R-0076`).

So the answer to "is there a standards-track path to P1 at the schema layer?"
is **not through CDDL modules**, and now there is a cited document saying so
rather than an absence. The consequence for `ARCH-0002`: P1 lives in the
**instance** — the `(defining key, local label)` pair carried as ordinary map
entries, which is what `R-M-12` and the proposal §3.3 already say — and the
schema layer will only ever describe its *shape*. `rfc-8610`'s extraction found
that CDDL expresses that shape "with no friction at all", which is precisely
what `R-M-12` wants from an encoding layer. **That is the whole of what the
schema layer can contribute to P1, and this document closes the question.**

---

## The cost of an unstable reference

Three distinct costs, and the third is specific to this draft.

1. **The citation itself.** `R-0003`: "It is inappropriate to use
   Internet-Drafts as reference material or to cite them other than as 'work in
   progress.'" Under `R-O-03` that is not a technicality. If D4 adopts a module
   convention from this draft, it adopts one from a work in progress **whose own
   `id` production does not admit the names its own examples use** (G-01) and
   **whose only demonstration of `include` with an `as` clause produces a model
   that does not resolve** (`examples/README.md`). Both are the kind of defect a
   -07 fixes; neither is fixed in the bytes we hold.
2. **Expiry.** `R-0001`: expires **6 March 2027**. Not expired — **137 days
   remain as of 2026-10-20**, the date of this record's verify pass — which
   puts it in better standing than `draft-ietf-cbor-cde`, which
   this library holds **expired 2026-04-17 and parked**. But the -07 revision
   still has an **unfinished Acknowledgments section** (defect 8 in
   `README.md`), which is a drafting-in-progress signal on a document seven
   revisions in.
3. **It depends on two further Internet-Drafts for its own substance, and we
   hold neither.** `R-0021` and `R-0041` point at
   `[I-D.bormann-cbor-cddl-2-draft]-09` (1 September 2026) for the design
   considerations — i.e. the rationale for the naming scheme is in a *different*
   unstable document. `R-0075` points at `[I-D.bormann-t2trg-deref-id]-07`
   (24 February 2026) for "the security considerations of dereferenceable
   identifiers". **[analysis]** That second one is the sharp cost: the analysis
   this record most needs — what it means to resolve a name that carries no
   principal — is *one hop away and unheld by this library*. The sibling records
   for dCBOR, CDE and serialization each had to make the instability point;
   this one has to make it twice over, because the chain is two drafts deep.

---

## What this does **not** invalidate in `rfc-8610`'s artifacts

`rfc-8610` is at `profile: full`. Everything below was checked and **stands**:

- **§3c and open question 4** — nothing in the language distinguishes a native
  from an export schema. **Confirmed and strengthened**, see question 1.
- **§3f's socket finding** — the socket mechanism inherits `ADR-0001`'s
  critique. **Confirmed and unaffected**: this document does not mention
  sockets at all, and cannot namespace one without breaking the plug relation.
- **Open question 6** — plug-file concatenation order is semantic and must be
  pinned. **Confirmed, and the problem is relocated rather than solved.**
- **Defect 7** — `CRLF = %x0A / %x0D.0A` admits a bare LF against RFC 5234.
  **Reproduced verbatim** in this draft's Appendix A (`R-0087`), and
  **undeclared here as there**, where it stands alone rather than camouflaged
  among four identical core-rule redefinitions. **Stands, in that record's own
  narrowed form**: the `rfc-9165` extraction established on 2026-10-19 that
  RFC 9165 §3 makes the identical redefinition and *declares* it, calling it
  "customary for ABNF" (`rfc-9165#R-0053`), so the substance is deliberate
  practice and the defect is the *silence*, not the rule. This draft is
  silent, so it is another undeclared instance — along with RFC 9682's
  Figure 11, which carries it over unremarked. One declared instance, three
  undeclared. *[framing narrowed in pass 2; this bullet previously said "the
  defect is now in two current CDDL documents".]*
- **The claim that RFC 8610 gives no module system.** Correct, and this document
  is the separate, later one that `rfc-8610`'s notes said `#39` listed.
- **Open question 11** — do the four siblings change the above? For this one:
  **yes in one respect, no in the rest.** The one respect is below.

**The one refinement, and it is a sharpening rather than a contradiction.**
`rfc-8610`'s notes say sockets "do not separate files". That is right. What this
record adds is that **a module file is not separated from a composed model
either**, in a way RFC 8610 alone could not show: §2.1's "basic CDDL on its own"
(`R-0023`) is lexical, every printed module file has dangling non-socket rule
names, and RFC 8610's one dispensation for an undefined name covers only
`$`/`$$` names (`rfc-8610#R-0079`). **[beyond source]** So the correct statement
of the combined finding is not "sockets do not separate files" but **"CDDL has
no construct that makes a file a unit of meaning — neither sockets nor modules
— and both mechanisms degrade by being silently ignored rather than by
failing."** `rfc-8610`'s `design-notes.md` should carry that sentence when its
open question 11 is closed; this record does not edit it.

---

## Open questions

Items this document cannot settle, with who must. **[beyond source]** marks
ones where this extraction had to reason past both the draft and our own
documents.

1. **Does D4 compose, or is it one hand-written file?** The answer decides
   whether any of §*What we adapt* applies. If it composes, the comment loss
   (G-17) alone forces `rfc-8610` open question 2 — D4 is a container that
   carries CDDL, not a CDDL file. *D4 (Oct 21), then the DEC-002 ADR.*
2. **If D4 composes, what pins the module graph?** No version (`R-0019`), no
   digest, no URI (`R-0035`), undefined search-path precedence (`R-0036`), and
   unspecified emission order (G-12) — while `/=`/`//=` ordering is semantic
   (`rfc-8610#R-0102`). **[beyond source]** A lockfile-equivalent is needed and
   nothing in CDDL provides one. *D4/D5, and it is an `R-O-03` obligation.*
3. **Does D4 use sockets at all?** If yes, G-13 has to be resolved by us
   because the document does not resolve it, and either resolution has a cost.
   If no, `rfc-8610` §3f's registry-free extension point is off the table and
   P4's domains of discourse need another mechanism. *DEC-002/DEC-005 ADR.*
4. **Do we adopt the `prefix.name` spelling now, before any tool supports it?**
   It costs nothing (`R-0023`: it is just rule names) and buys forward
   compatibility, but it commits our fixtures to a convention from an expiring
   draft with a known grammar defect. **[beyond source]** *D4, David's lane
   (#13).*
5. **Who owns the CI check that a native schema contains no `#6.nnn`?** Cut 3
   makes a build action able to breach a native prohibition. Our CI does not
   look at CDDL today. *DEC-002 ADR / library CI.*
6. **Should this library hold `[I-D.bormann-t2trg-deref-id]`?** It carries the
   analysis of exactly the problem question 2 identifies, this draft
   incorporates it by reference (`R-0075`), and we do not have it.
   **[beyond source]** *Ingest decision — it bears on `ARCH-0002` P1 directly.*
7. **Should `[I-D.bormann-cbor-cddl-2-draft]` be held too?** It is where the
   module naming rationale and the "further work" of `R-0019`, `R-0021` and
   `R-0041` actually live, and a reviewer asking *why* filenames was decided on
   cannot be answered from this document. *Ingest decision.*
8. ~~**Does the `rfc-9682` grammar update change Appendix A's `id`?**~~
   **ANSWERED in pass 2 (2026-10-20): no, and G-01 is therefore at full
   strength.** `R-0005` says CDDL is defined by RFC 8610 **and RFC 9682** as
   well as RFC 9165 and RFC 9741, and if RFC 9682 had widened or narrowed `id`,
   G-01's severity would move with it. The `rfc-9682` record landed in this
   library between this record's pass 1 and pass 2, and its
   production-by-production change table lists `id` — with `ALPHA`, `EALPHA`
   and `DIGIT` beside it — among the **forty-one productions carried into
   Figure 11 unaltered**
   (`records/ietf/rfc-9682/distilled/schema/production-changes.derived.txt`).
   So the CDDL `id` in force today is still
   `EALPHA *(*("-" / ".") (EALPHA / DIGIT))`, and Appendix A's `id` is narrower
   than the **current** grammar, not merely than the 2019 one. The same table
   records `CRLF` as unchanged too, which is what lets this record's defect 4
   count three undeclared instances of that redefinition against RFC 9165's one
   declared one. *Closed; nothing is owed to the `rfc-9682` lane on this point.*
9. **Who tells the CBOR WG about G-01 and the `V-0009` defect?** Both are
   mechanically demonstrable, both are in the bytes we cite, and the draft names
   its issue tracker (`https://github.com/cbor-wg/cddl-modules`). Reporting is
   outside this library's remit; recording that nobody has is not.
   *Paul / David.*

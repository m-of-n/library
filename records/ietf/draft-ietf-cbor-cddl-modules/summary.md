---
schema: "library-summary/v1"
id: draft-ietf-cbor-cddl-modules
record: draft-ietf-cbor-cddl-modules
type: summary
updated: "2026-10-19"
---

# CDDL Module Structure

|  |  |
|---|---|
| **Type** | draft |
| **Maturity** | draft — IETF CBOR WG, intended status **Standards Track** |
| **Authors** | C. Bormann (Universität Bremen TZI), B. Moran (Arm) |
| **Published** | 2 September 2026 (revision -07); expires 6 March 2027 — **not yet expired** |
| **Identifier** | draft-ietf-cbor-cddl-modules-07 |
| **Source** | https://www.ietf.org/archive/id/draft-ietf-cbor-cddl-modules-07.txt |
| **Digest** | `7cf825aaad43d3d4995bcd540d3865ee3f69dd3dd453be5761a02c009458a644` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

CDDL has no module system; this draft proposes one. A CDDL file becomes a
module by carrying directives written as `;#`-prefixed **comments**, so every
pre-existing tool ignores them and the file "can at the same time be basic CDDL
on its own". Five selection forms — `include`, `import`, and variants with an
`as` prefix — draw rules from one module into another, and a module's name is
**a filename**, resolved against directories through the environment.

Its compatibility story is that silence is success: an un-updated tool sees
comments. That is also its central weakness, below.

**It has no IANA actions at all** (§4, one sentence), which makes it the first
document in this library's CDDL family not to grow a registry.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Naming | **core** | This is the document that could have given CDDL key-relative naming at the schema layer. It does not — see the negative result below. |
| Encoding | supporting | Relevant the moment D4's schema stops being one file, which WP1 reaches quickly. |

**The negative result, and it closes a question.** ARCH-0002 P1 is
key-relative naming, accepted by ADR-0001. A module system is exactly where a
schema language would express it, and this one offers: filenames for module
identity, an environment variable for resolution, prefixes chosen by the
*importer*, URIs **explicitly refused** ("avoids the need to nail down brittle
pathnames or (partial?) URIs into the CDDL files"), and nothing allocated.
**There is no standards-track path to P1 at the schema layer through CDDL
modules.** P1 lives in the instance; the schema layer only ever describes its
shape — which `rfc-8610`'s extraction found CDDL does with no friction at all.

**The `as` prefix relocates the collision rather than fixing it.** Emitted
names like `cose.label` are *ordinary* basic-CDDL rule names, because `.` is
legal inside an RFC 8610 `id`. So after composition there is still one flat
global namespace, exactly as in RFC 8610; prefixes make names longer, not
scoped. The prefix is chosen by the importer and bound to nothing, so two
modules may take the same prefix with no diagnostic. That is ADR-0001's
rejected shape: an escape from a collision, not a namespace. Stated the other
way for balance — the prefix *is* **composer-relative** naming, which is the
right direction; P1 is `(defining key, local label)` and this is
`(composing file, local label)`. The local-label half transfers. The principal
does not exist, and this document does not add it. **Modules get the half that
was never the hard part.**

**No export boundary exists.** `export`, `private` and `visib` occur **zero**
times in 784 lines. All five selection forms are written by the *consumer*; the
producer-side column is empty. Worse, `include` draws in "all the rules from a
module (which includes the ones imported/included there, transitively)" — so a
module cannot make a rule private, and **adding an import to a module changes
what its consumers' `include` draws in**, a non-local effect with nothing to
constrain it. This is the strongest possible evidence for `rfc-8610`'s finding
that nothing in CDDL distinguishes a native schema from an export schema,
precisely because a module system is where that boundary would live.

**Sockets are not mentioned once.** `socket`, `plug` and `$$` occur zero times.
RFC 8610 §3.9 is neither amended, exempted nor named, and whether an `as`
clause prefixes a socket is unstated — and **both answers break something**:
prefix them and `$$ext` becomes `cose.$$ext`, so a plug written elsewhere
silently stops plugging; don't, and the one registry-free extension point keeps
a flat global name across the whole build, which is the exact collision the
module system exists to prevent.

**One thing it gives us that is genuinely useful.** Module names *are*
filenames. So this library's `.derived.` discipline, and `rfc-8610`'s
filename-plus-CI remedy for the missing native/export boundary, stop being
workarounds *around* CDDL and become the half of CDDL's own module mechanism
that the draft deliberately leaves to "the context of the models".

## Implementations

The draft references `cddlc` by command line (`-2tcddl`) but registers and
names no implementation, and its Acknowledgments section is **still an
unfinished placeholder at revision -07**. *Searched on 2026-10-19; no named
implementation in the document.*

## Limits

- **The grammar cannot derive the document's own examples.** Appendix A's
  `id = ("$" / %x40-5a / "_" / %x61-7a) *("$" / %x30-39 / %x40-5a / "_" /
  %x61-7a)` admits neither `.` nor `-`, where RFC 8610's
  `id = EALPHA *(*("-" / ".") (EALPHA / DIGIT))` admits both. So
  `;# include cose.label, cose.values from rfc9052 as cose` (line 388) and
  `;# import cose.empty_or_serialized_map from rfc9052 as cose` (line 414) —
  **2 of the 7 directive instances printed** — are not derivable from the
  draft's own grammar. It also bars any rule name containing a hyphen. Verified
  mechanically against both productions.
- **The only demonstration of `include` with an `as` clause emits a model that
  does not resolve.** The output at lines 399–401 defines `mydata`,
  `cose.label` and `cose.values`, while `mydata` references bare `label` and
  `values` — defined nowhere in the block and not among RFC 8610's 40 prelude
  names. The other six composed outputs are all closed. The document introduces
  this one with "Again, only exactly the rules mentioned are included".
- **`/=` and `//=` ordering under composition is unspecified, and that is
  strictly worse than before.** Neither operator appears in the document, and
  `precedence` appears once — explicitly undefined. `rfc-8610` found plug-file
  concatenation order is *semantic*; this moves that from the order of
  filenames in a build script, which is ugly but visible in a diff we write,
  into the order an unspecified resolver walks an import graph over a search
  path whose precedence the draft declines to define. If D4's schema uses
  `/=` anywhere, a lockfile equivalent is required and nothing here supplies
  one.
- **Dependency confusion is the default.** The search path tries `.` first, so a
  local `rfc9052` silently shadows a curated extract. The draft names the
  consequence in its own voice — "the possibility of supply-chain attacks on
  the modules imported needs to be considered" — and declines the one spelling
  (a URI or digest) that would make a reference self-describing.
- **The compatibility claim is lexical, not semantic.** "Each module source
  file can at the same time be basic CDDL on its own" is true of the syntax,
  but **all six module files the draft prints have at least one rule name that
  resolves to nothing**. RFC 8610's only dispensation for an undefined name is
  the §3.9 socket convention, which covers only `$`/`$$` names — none of these.
  So an un-updated tool gets an unresolvable model and nothing says what it
  does: the same "silence is success" failure mode, now about whole files.
- **It is a work in progress, two drafts deep.** Its own boilerplate says it is
  "inappropriate to use Internet-Drafts as reference material". The design
  rationale for the naming scheme is in another draft, and the security
  analysis of dereferenceable identifiers in a third — **this library holds
  neither**, so the analysis of the namespacing question is one hop away and
  unread.
- `CRLF = %x0A / %x0D.0A` is redefined against STD 68 to admit a bare LF. That
  is the same defect `rfc-8610` records, and here it stands **alone** rather
  than camouflaged among four identical core-rule redefinitions — so the defect
  now sits in two current CDDL documents.
- The extraction is at **pass 1 of 3**; verify and cross-check have not run and
  nothing carries a human sign-off, so these artifacts are readable but not
  buildable-on.

## Where it cuts against MD-3

Five cuts are recorded in `distilled/design-notes.md`, each naming a DEC-002
option. Two are worth stating here:

- **On registries it favours option 5** — the first of this library's five
  CDDL-family extractions to cut that way. §4 defines no registry and depends
  on none, so module names are *not* a fourth registry. The qualification
  matters though: the authority moved into the deployment environment rather
  than disappearing, and the only resolver the draft describes keys modules on
  **RFC numbers**, inside an appendix marked "for information only". An
  unstated authority is harder to audit than a named one.
- **Modules make option 5's unstateable exclusion easier to breach.** One
  `include` readmits a module's whole transitive closure, including any tag,
  with no export declaration to inspect. That is a native prohibition breached
  by a *build action*; CI is the only catch, and our CI does not look at CDDL.

---
schema: "library-doc/v1"
id: rfc-8747-distilled-index
record: rfc-8747
type: index
updated: "2026-10-21"
---

# Distilled artifacts — RFC 8747 (Proof-of-Possession Key Semantics for CWTs)

**FX-1 pass 1 (extract) only.** `distillation.passes` in `record.yaml` is the
only authority for which passes have run — this file deliberately does not
restate a pass count, because such a restatement goes stale the moment the next
pass lands and nothing reports it. It was found stale in four files at once in
`rfc-9338`, four in `rfc-8778` and one in `rfc-9921`, each time inside a file
that recorded the pass it denied.

No `profile` is declared: an unfinished extraction has neither `full` nor
`partial`. `reviewed_by` is empty on every artifact — that is pass 4, human
review. Artifacts may be read; nothing may be built on them yet
(`docs/requirements.md`).

## The source

| | |
|---|---|
| Lines | **683** newline-delimited, **0** form feeds — so no page decoration and no running header to exclude |
| Digest | `9b695379f119f9675828d054f1b0e76014c06c9a59dccef8bb417e0420272dda`, matching `content.sha256` and a fresh `shasum -a 256` of the cache |
| Standing | `Category: Standards Track`, read off the front page, matching `maturity: standard` |
| BCP 14 keywords | **8** — 4 MUST, 2 MAY, 1 SHOULD, 1 MUST NOT |

## The artifacts

| file | what it is | coverage |
|---|---|---|
| `normative.md` | every normative statement verbatim with its locator, plus Table 1 and the §7 registration templates | regions carry a line range and a digest |
| `requirements.yaml` | **118** entries, `R-0001`–`R-0118`, source order, no gaps | 8 = 8 keywords reconciled; all 118 texts verified contiguous |
| `schema/` | 1 verbatim rendering + 3 derived | `cnf-claim.derived.cddl`, `.schema.json`, `confirmation-methods.derived.yaml`, `source-renderings.txt` |
| `messages.yaml` | 4 structures, 8 field entries | 17 distinct ids wired; the 101 not wired are enumerated **by locator** |
| `protocol.yaml` + `protocol.md` | **3 roles, 0 flows, 2 declared absences** | produced, not N/A — see below |
| `state-machine.yaml` | `not_applicable`, with the sweep behind it | 13 lifecycle words at zero, 4 near misses each checked |
| `examples/` | the §3.2/§3.3/§3.4 CWT Claims Sets as fixtures | CBOR diagnostic notation; the document prints no hex |
| `design-notes.md` | the finding, MD-3 header by header, and where it cuts | 3 adopt, 2 adapt, 2 reject, 3 cuts + 1 convergence |

## Why `protocol` is produced and `state-machine` is not

These two verdicts go opposite ways in the same record, and both are measured.

**Protocol: produced.** This is the only record in library#39's CBOR/COSE set
whose source names parties and still has no flow. Measured whole-word,
case-insensitively, over all 683 lines: `presenter` **18**, `recipient`
**14**, `issuer` **8**, `party` **8**, `parties` **7** — three roles with
distinct obligations. What it lacks is the exchange, and that absence is the
document's own: §3.5 is titled *"Specifics Intentionally Not Specified"* and
withholds both the nonce and the signed nonce. Recording three roles and two
declared absences says more than an N/A verdict would, because the gap is the
finding — an application adopting `cnf` supplies the entire proof mechanism
itself.

**State machine: not applicable.** Thirteen lifecycle words occur **zero**
times; the four near misses are an issuer-side uniqueness constraint, the IANA
registry procedure, two uses of "in order to", and §3.5's refusal to specify
freshness. Five sibling CBOR/COSE records at `profile: full` declare this
artifact N/A on three different grounds; **this record's ground is a fourth** —
it has a lifecycle-shaped subject, a key bound to a token and held by parties
over time, and the document declines to give it states. Kept distinct rather
than folded in, because a reader looking for prior art on key rotation will
come here and should find the absence rather than an oversight.

## What the record is for

Almost nothing is adopted from it. Its value is a **definition by contrast**,
and it is in §3.4:

> Note that the value of a Key ID for a specific key is not necessarily the
> same for different parties.

A `kid` is a *(party, local label)* pair resolved by table lookup.
`ARCH-0002 P1` makes an extension point a *(defining key, local label)* pair
resolved by derivation. Same shape, different first element — and that
difference is the whole of P1. Set out in `design-notes.md` §5, with the other
three limbs of what a Key ID is **not**: not derived, not unique, and with the
collision foreseen in the text and nothing mandated against it.

## Two defects found in this pass's own prose

Recorded rather than quietly fixed, because the point of writing them down is
that the next pass knows which classes actually fire here.

1. **A healed hyphenation break.** `design-notes.md` §2 first quoted §3.1's
   MUST as *"a single proof-of-possession key"*. Source lines 180–181 break it
   **at the hyphen**, so the normalised source reads `proof-of- possession` and
   the quoted token would have occurred nowhere in RFC 8747. Corrected and
   declared in place. It is the only hyphenation break among the document's
   eight keyword-bearing sentences.
2. **A verbatim sentence unmarked in a whole-scalar value.** `messages.yaml`'s
   `cnf` `purpose:` field carried *"Some of them use proof-of-possession keys,
   while others do not."* with no quotation marks — invisible to a delimited
   quote audit, which is the blind spot `hazards.md` §2 names. Now marked.

And one count this pass got wrong about itself: `messages.yaml`'s `coverage`
first said 21 ids and 11 fields where the parsed file has **17** and **8**.
Corrected. Any pass that edits an artifact falsifies every count of it that it
does not also update.

## What passes 2 and 3 should attack

`design-notes.md` §10 carries the list. In short: the unusually high
**111 `stated` / 7 `inferred`** split, since *contiguous* and *literally stated*
are different claims; **R-0038 and R-0052, which each occur twice in the
source** — a duplicate-text group, the one place a wrong id still matches the
quoted words, and neither cited from any artifact yet; **R-0040**, which begins
with a conjunction after a mid-sentence split off R-0039; this pass's own
recounted numbers; and the inference behind producing `protocol` rather than
declaring it N/A.

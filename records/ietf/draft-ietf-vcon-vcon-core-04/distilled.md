---
schema: "library-distilled/v1"
id: draft-ietf-vcon-vcon-core-04
record: draft-ietf-vcon-vcon-core-04
type: distilled
source_version: "-04"
source_digest: "sha256:cc2a2cb5051b860e2f29478a9ff946e3…"
extracted: "2026-09-22"
extracted_by: agent
reviewed_by: ""
coverage: "top-level vCon object (§4.1) complete; Party, Dialog, Attachment, Analysis pending"
updated: "2026-09-22"
---

# vCon core — distilled

**Purpose:** a compacted form from which the container can be implemented
without re-reading the draft. **Normative language is verbatim.** Locators are
section numbers, never pages.

> **`reviewed_by` is empty. Nothing may be built on this yet.** Readable;
> not usable. library#9 step 6.

**Source normative verbs:** MUST 67 · MUST NOT 17 · SHOULD 98 · SHOULD NOT 7 ·
MAY 32 · SHALL 1 · SHALL NOT 1 · REQUIRED 1 · RECOMMENDED 2 · OPTIONAL 1.
Across **137** paragraphs. A distillation that loses any of these has failed.

---

## 1. Conventions — §2

RFC 2119 as updated by RFC 8174. Only capitalised keywords are normative.

Base types (§2.2), each with its own constraint:

- **Date** — *"A string that MUST have the form of an [RFC3339] date string as
  defined for the Date type"*
- **Mediatype** — *"A 'String' value that MUST be of the following form as
  defined in section 5.1 of [MIME]"*

## 2. The vCon object — §4.1

### 2.1 `vcon` — §4.1.1
Schema version. **Marked deprecated in the draft itself**, value `"0.4.0"`.
Flagged: a deprecated version field in a draft means versioning is unsettled.

### 2.2 `uuid` — §4.1.2
> *"The UUID value MUST be globally unique. All vCon documents MUST have the
> uuid parameter and value set."*

> *"The value of the string SHOULD be generated using the version 8 UUID defined
> in [UUID] which is generated identically to a version 7 UUID with the
> exception that…"*

Type `String`. **Two MUSTs and a SHOULD.** Globally unique, always present,
v8 preferred.

### 2.3 `extensions` — §4.1.3
> *"The extensions parameter SHOULD contain the list of names of all vCon
> extensions for any parameters used that are not defined in this core vCon
> schema document."*

Type `String[]`. **SHOULD**, not MUST — declaring your extensions is
recommended, not required.

### 2.4 `critical` — §4.1.4 · **the must-understand mechanism**
> *"Implementations that include extensions which are incompatible with the core
> vCon schema MUST list the names of those extensions in the critical
> parameter."*

> *"An implementation that does not recognize or support the extensions listed in
> the critical parameter MUST NOT attempt to process or operate on the vCon,
> except to reject it or report unsupported content."*

Type `String[]`. **MUST + MUST NOT.** Reject-if-not-understood, stated as
strongly as it can be.

**Note for ARCH-0002 P5.** This is must-understand implemented — but it is
**opt-in by the producer**. A producer that omits `critical` gets silent
skipping, and the consumer cannot tell the difference between "no critical
extensions" and "producer forgot". Our P5 inverts this: unknown is critical
unless declared otherwise, so **forgetting is safe**. vCon's default makes
forgetting unsafe. *This is the clearest available argument for P5's inversion,
and it came from reading a spec that chose the other way.*

### 2.5 `created_at` / `updated_at` — §4.1.5–6
Type `Date` (RFC 3339, per §2.2).

### 2.6 `subject` — §4.1.7
Type `String`, optional. Conversation topic.

### 2.7 `redacted` — §4.1.8, object §4.1.8.1
Reference to a **less-redacted** prior vCon.

### 2.8 `amended` — §4.1.9, object §4.1.9.1
Reference to a **prior version** to which data has been added.

**Note on supersession.** Both point *backwards* at a distinct, separately
addressable vCon rather than replacing it. Contrast `docs/scope.md` §5, where we
fold prior versions into one record. vCon treats each version as a first-class
object with its own `uuid`. **Neither is obviously right** — ours optimises for
"we want the latest", theirs for "every version must remain citable". Ours would
lose the redaction chain, which for them is the point.

### 2.9 Arrays — §4.1.10–13
`parties`, `dialog`, `analysis`, `attachments` — arrays of the objects in §4.2–4.5.

---

## 3. Sub-objects — §4.2–4.5 · **NOT YET EXTRACTED**

| object | §  | status |
|---|---|---|
| Party | 4.2 | pending |
| Dialog — recording, text, transfer, incomplete, recording-set | 4.3 | pending |
| Attachment | 4.4 | pending |
| Analysis | 4.5 | pending |
| Party_History | 4.3.13.1 | pending |

Deliberately marked pending rather than skimmed. **A partial extraction that
says so is usable; one that pretends to be complete is not.**

---

## 4. Security — §5, and what is delegated

Integrity and confidentiality are **JWS** and **JWE**. No new cryptography is
defined. Algorithms reference the **IANA COSE Algorithms registry**.

**Note for R-M-12 / ARCH-0002 P1.** A current draft reaching for a
registry-allocated algorithm space is the normal, frictionless choice. That is
evidence about the *cost* of our alternative: key-relative identifiers must be
as easy as citing a registry, or specifications will keep citing registries.

---

## 5. Correctness review — what it caught

An automated pass checked every verbatim quote against the source, confirmed
every §4.1.x subsection was cited, and cross-checked sections containing MUST
against the verb extracted. **It found five defects in the first draft of this
extraction:**

| § | defect | fixed |
|---|---|---|
| 4.1.1 `vcon` | source has *"the string MUST have the value"*; extracted as `verb: none` | → MUST |
| 4.1.6 `updated_at` | missed *"Future updates MUST first set the updated_at to the new signing time"* — the field is **bound to the signature**, not merely descriptive | → MUST |
| 4.1.8 `redacted` | missed a conditional MUST restricting access to the unredacted URL | → MUST |
| 4.1.9 `amended` | missed *"a new vCon instance version MUST be created"* | → MUST |
| 4.1.4 `critical` | two **non-adjacent** sentences spliced into one quote — a third sentence separates them | split into `text` and `text_2` |

**Four of five were dropped MUSTs.** That is the failure `docs/requirements.md`
warns about, arriving on the first real extraction: the normative statements
sitting in prose rather than in the field bullet are the ones that get missed.
`updated_at` is the consequential one — read without it, an implementer would
treat the field as informational and break the signature relationship.

The splice is the subtler defect. Both sentences are verbatim and both are in
§4.1.4; joined, they assert an adjacency the source does not have. **Verbatim is
not enough — contiguity has to be preserved too.**

Re-verified: **8/8 quotes match the source, 13/13 sections cited, 0 weakened
verbs.**

## 6. What this distillation does not cover

- §4.2–4.5 sub-objects (above)
- §5 security considerations in full — only the delegation is captured
- §6 IANA considerations
- §7 examples
- The informative references (10)

**Completeness is per-object, and stated per-object.** Nothing here should be
read as "the spec says nothing else".

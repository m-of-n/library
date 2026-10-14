# Pass 3 handoff — vcon-core-04 FX-1 cross-check (#9)

**Delete this file before the PR.** It is a working note, not a record artifact.

Branch `vcon-fx1-extraction`, on top of `vcon-profile-partial` (PR #78).
Passes 1 and 2 are committed at `e5302aa`. `bin/validate` is clean: 0 errors.

Source, cached and digest-verified (`.cache/` is gitignored — refetch if missing):

    .cache/draft-ietf-vcon-vcon-core-04.txt  cc2a2cb5051b860e2f29478a9ff946e3d882818bfad55dff48e0f5ae033cd722
    .cache/rfc-7515.txt                      ecbf84674118e62526511c1237e1deaa86aada86d25b247623a2a7e04ae62e40
    .cache/rfc-7516.txt                      722cfcddc15f58e746891ba4b846853d3711153a774e4dd55ad6db100474a21f

    curl -sSfL -o .cache/draft-ietf-vcon-vcon-core-04.txt https://www.ietf.org/archive/id/draft-ietf-vcon-vcon-core-04.txt

## What pass 3 is

`docs/extraction.md`, pass 3 of 4: requirements <-> schema <-> messages <->
state machine. Every field a requirement names exists in the schema; every
message in a protocol flow is defined; every state-machine trigger is a defined
message or named event; every example validates against the schema.
Then pass 4 is a HUMAN signing `reviewed_by` — not us.

Run at **maximum effort** and record it in `distillation.passes`, or
`bin/validate` fails the record.

## The queue

1. **Wire `messages.yaml`'s `constrained_by`.** All 187 fields carry
   `constrained_by: []` with the real section in `constrained_by_locator`.
   Pass 1 did this deliberately: `requirements.yaml` was being rewritten
   concurrently so no id was stable. Ids are stable now (R-0001..R-0249).
   The file's own `cross_links` header block says this is pass 3's job.

2. **Resolve `protocol.yaml`'s message names.** It ran while `messages.yaml`
   was still a scaffold, so no `message:` name resolves. It lists exactly what
   to find under `messages.expected_in_messages_yaml`. Only five requirement
   ids are wired (R-0004, R-0007, R-0008, R-0017, R-0026); the rest cite the
   source directly and are listed under `requirements_not_yet_wired`.
   Same in `state-machine.yaml`.

3. **Regenerate `types.derived.cddl`** with `bin/derive`. It is STALE — built
   from the pre-correction field table. NEVER hand-edit it; fix `fields.yaml`
   and regenerate. Expected delta, simulated by pass 2: 71 -> ~152 lines,
   5 -> 15 groups, all nine `required` rows corrected, §5 objects added,
   Dialog Content and the six transfer parameters added, the leaked heading
   `"party_history Objects Array"` -> `"party_history"` fixed.
   Two faults will arrive with it, both in `bin/derive` not in `fields.yaml`:
   object names with spaces/parens flatten to `vcon__signed_form_`,
   `header__jws_`, `header__jwe_`; and it still emits no
   `extension_parameters_type`. Decide whether to fix `bin/derive` or record
   them; do not paper over them in the output.

4. **Strike four now-answered criticisms in `schema/README.md`** when 3 lands —
   missing §5, missing Dialog Content/transfer params, the §4.3.9->4.3.11
   numbering jump, the leaked heading. The README records the delta so the two
   land together.

5. **Validate every fixture against the schema.** 12 fixtures in
   `distilled/examples/`, `vcon.derived.schema.json` is the parseable one
   (Appendix B as printed is NOT valid JSON — 89 line breaks inside string
   literals; this is a recorded source defect, not our error). `jsonschema` was
   not installed when pass 2 ran, so this check has never been run.

6. **Rewrite `distilled/README.md`.** It is still the pre-extraction version
   and is wrong twice: it says `examples/` is "empty — §7 examples not yet
   lifted", and its "Still to distil" table repeats the same mis-citation.
   §7 is "Non-Upward Compatible Changes to the vCon Container", a version
   migration log. The examples are Appendix A.

7. **Rebuild `record.yaml`.** Set `standard: FX-1`, `profile: full`, drop
   `profile_reason`, list every artifact with honest per-artifact coverage
   (see `records/ietf/rfc-9804/record.yaml` for the bar — coverage strings
   there state what is NOT covered, not just what is), and record all three
   passes with `effort: max`. `reviewed_by` stays `""` on every artifact —
   that is pass 4 and it is a person.

   NOTE the ratchet: `profile: partial -> full` is forward, so allowed. The
   record currently says `standard: distillation/0.1.0`, `profile: partial`,
   set by PR #78.

8. **Correct `topics/artifact-statements.yaml`.** It is `status: answered` and
   says "vCon never distinguishes ASSEMBLED from ASSERTED". §4.4.3 refutes
   that: the Attachment `party` index is a MUST, the draft calls it
   "provenance", and says "This party is not necessarily the document's
   author, but rather the party that distributed the document" and "an
   organization that processes or constructs the vCon ... SHOULD be
   represented as a Party Object". Strike that clause; KEEP the `analysis[]`
   clause, which is exactly right — `analysis[]` has no `party` at all, only
   `vendor`/`product`/`schema`, which name software.
   Do NOT write that the draft uses the words "assembled" or "asserted":
   `assembl*` appears zero times in 8904 lines. `design-notes.md` marks the
   mapping `[we conclude]`; match that.

## Rulings already made — do not relitigate

- **D1 count.** 216 source / 169 body / 47 in Appendix B+C, excluded on the
  source's own instruction. A rival count of 174 included the RFC 8174
  boilerplate sentence (one of each of eleven keywords).
- **D2 Table 1.** 120 cells: X 57, O 30, S 19, M 9, SN 4, `-` 1. BOTH
  appendices express M and X; NEITHER expresses S, SN or `-`. Appendix B's
  prohibitions are enforceable (`if type=const then not{anyOf[{required:[p]}]}`,
  no `additionalProperties` needed); Appendix C's are advisory (its
  `* tstr => any` wildcard absorbs them, as its own preamble concedes), and C
  CONFLATES SN with X.
- **D3 A.7 `protected`.** The EXAMPLE is right; §5.3's five-member list is
  incomplete. RFC 7516 §7.2.1 makes `protected` a conditional MUST. `aad` is
  omitted too.
- **D4.** Appendix C DOES define `file_content_type`, `inline_content_type`,
  `external_content_type`, `dialog_transfer_type`, and covers §2, §4 AND §5.
  The gap belongs to OUR `types.derived.cddl`. This mis-relay survived two
  hops and one correction — re-derive from the source, never from an
  artifact's description of it.
- **D5 hyphen line-breaks.** A span carrying `Verbatim:` declares a verbatim
  contract and SPLITS (`"recording- set"`); a quotation woven into commentary
  JOINS. Six requirements entries carry a split hyphen and all six must say so
  in `testable_note` — that is a stated MUST now, so check the seventh.
- **D6 JWS header placement.** `x5c`/`x5u`: §5.2 says unprotected, not
  ambiguous. `alg`: GENUINELY AMBIGUOUS and recorded as such, not resolved.
  A.6 takes a third option RFC 7515 §7.2.1 forbids — `alg` and `x5c` in BOTH
  headers, where §7.2.1 says "The Header Parameter names in the two locations
  MUST be disjoint".
- **Ids never overlap.** §2.5's *Parameter Definitions* is carried at sentence
  granularity rather than as a whole-bullet entry containing R-0052/R-0053,
  because an entry whose text contains another's lets one obligation be cited
  twice. The asymmetry is deliberate and documented in R-0220's note.
- **Exemptions belong in the register** (R-0248, R-0249): a checker fed
  obligations without exemptions fails on conforming input.
- **Inference is marked.** T-F-06 is `inferred` — no verb in the document
  takes the payload as an object. T-F-05 is `stated`, because an obligation
  that fires on an event asserts the event occurs.

## Known source defects — already recorded, do not re-report as ours

Line 6725 and line 4633 carry the literal editorial marker `bin/validate`
forbids under `distilled/`. DESCRIBE it, never reproduce it. No fixture does.

The draft's own worked redaction (A.8) fails in both directions: `"Okay."` ->
`"{{US_STATE}}"` twice while "Bob" and "Alice" survive in the transcript. One
uuid names four documents. A.8's uuid timestamp is 692 days BEFORE its parent.
A.6 and A.7 both violate JOSE header disjointness. A.7 fails the draft's own
CDDL. `extensions` and `critical` — the must-understand mechanism this record
is held for — are exercised by NO example.

## Before the PR

    bin/validate                        # must be 0 errors
    bin/check-pr-extraction origin/main # will fire: distilled/ is being changed
    bin/export && bin/reindex           # 0 dangling; do NOT commit index/ or exports/
    rm PASS3-HANDOFF.md

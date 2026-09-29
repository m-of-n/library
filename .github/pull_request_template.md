## What this adds

<!-- Records, topic, and what question the topic answers. -->

## FX-1 checklist — for every rfc / draft / spec / ietf record past stub

See `docs/extraction.md`. CI enforces this (`bin/check-pr-extraction`); the
checklist is so you are not surprised by it.

- [ ] `summary.md` complete; `tags`, `bears_on`, `topic` set
- [ ] `normative.md` — every normative statement, verbatim, with locator
- [ ] `requirements.yaml` — **all** BCP 14 statements; `source_keyword_count` from `bin/bcp14-count`; counts reconciled
- [ ] `schema/` — the source's own CDDL / ASN.1 / JSON Schema, verbatim
- [ ] `messages.yaml` — every message and structure, field by field
- [ ] `protocol.yaml` + `protocol.md` — roles, flows, error paths, sequence diagram
- [ ] `state-machine.yaml` — every lifecycle
- [ ] `examples/` — every example as a fixture with expected result
- [ ] `design-notes.md` — adopt / adapt / reject, mapped to our decisions (COSE/CBOR: D-3)
- [ ] anything not applicable is in `not_applicable` **with a reason**
- [ ] passes recorded: extract, verify, cross-check — all at effort `max`

Stubs (`status: stub` or `queued`) are exempt: ingesting a reference is fine;
calling it finished is not.

## Signed-off-by
Every commit carries `Signed-off-by` (`git commit -s`).

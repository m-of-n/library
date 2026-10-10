# D1 — Library construction best practice (v0.1, iterating)

> **Status: v0.1 skeleton.** This is the first research output of the project and
> it is deliberately meta: *before we collect references, we decide how.*
> Revised at the end of every increment with what we got wrong. An honestly
> revised methodology report is a more credible artifact than a clean one
> written at the end.

## Exit criterion

A second person adds a correct record from this document alone, without asking.

## Decisions taken in v0.1 (each needs defending or reversing)

| # | Decision | Rationale | Still to verify |
|---|---|---|---|
| 1 | CSL-JSON is the interchange format, not the source of truth | Round-trips through Zotero, Citation.js, pandoc. `record.yaml` is authored; `exports/` generated | Does CSL-JSON lose our typed relations? (It does — is that acceptable?) |
| 2 | Typed cross-references, not tags | Makes the library queryable against DEC-*/R-* | Is the relation vocabulary complete? Compare SKOS, PROV |
| 3 | Never commit third-party bytes | Size, licensing, publishability; digest preserves integrity | Link rot — is digest + URL enough in 5 years? |
| 4 | Content hash is identity | Two libraries that never sync still agree what document they mean | Which digest for a *versioned* spec — the PDF, or the version string? |
| 5 | Stable, never-reused ids | Citations must not silently retarget | Naming convention for multi-version specs |
| 6 | Attribution by locator, not by transcription | A summary cites §n and the reader opens the source; verbatim normative text lives only in `distilled/normative.md`, where the verbatim check can reach it. The `quotes.md` companion held this convention from v0.1 and was used by **0 of 304 records** — the discipline was real, the file was not. Retired 2026-10-09 | Does a non-FX-1 record (`paper`, `web`, `dataset`) ever need a verbatim excerpt with nowhere to put it? If one does, that is the trigger to reinstate a quote file — not a reason to keep an unused one |

## Method to follow

- **Kitchenham & Charters** three-stage SLR: protocol → conduct → report. Write
  the protocol before searching; the protocol is a committed artifact.
- **Wohlin snowballing**: a start set, then backward (reference lists) and
  forward (citations) iteration to closure. Record each iteration's yield.
- **PRISMA 2020** for transparent reporting of what was found, screened, and
  excluded — and why.

## Open questions for v0.2

- How do we record a *specification family* (IETF WG, C2PA releases) without one
  record per revision becoming unusable? Current answer is `part_of` + a
  `hierarchy` record; untested at scale.
- Do agent-ingested records need different `confidence` handling than
  human-ingested ones?
- Does `bears_on` belong on the record, or is it properly a topic-level edge?

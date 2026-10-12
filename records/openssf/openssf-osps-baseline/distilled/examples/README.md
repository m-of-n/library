---
schema: "library-doc/v1"
id: openssf-osps-baseline-examples
record: openssf-osps-baseline
type: examples
updated: "2026-10-02"
reviewed_by: ""
---

# Examples — OSPS Baseline v2026.08.28

The OSPS Baseline contains no worked examples or test vectors of its own: it is a control
catalog. The fixtures here are therefore **verbatim excerpts of the catalog's own data files**
at tag `v2026.08.28` (Apache-2.0), chosen so that each structure in `messages.yaml` and each
constraint in `schema/` is exercised once. Every file starts with a two-line comment header naming
the source file and line range; everything below that header is byte-identical to the source.

| fixture | source | exercises | expected result |
|---|---|---|---|
| `01-control-osps-ac-01.yaml` | `baseline/OSPS-AC.yaml` 1–30 | `groups[]` (#Group), one `#Control` with one `#AssessmentRequirement` applicable at all three maturity groups | valid against `#OSPSBaseline` (`schema/osps.cue`) when merged with `metadata.yaml`; `state` defaults to `Active` (`#Lifecycle` default in `gemara-v1.2.0/collections.cue`) |
| `02-control-osps-br-01-with-retired-ar.yaml` | `baseline/OSPS-BR.yaml` 1–69 | a control holding a **Retired** assessment requirement (`OSPS-BR-01.02`, `state: Retired`, no `recommendation`) and an AR applicable at `maturity-3` only (`OSPS-BR-01.04`) | valid: Gemara forbids `recommendation` on a Retired AR (`if state == "Retired" { recommendation?: _\|_ }`), and the fixture has none; the retired id stays in the file, per `docs/maintenance.md` "Identifiers for retired controls MUST NOT be reused" |
| `03-catalog-metadata-applicability-groups.yaml` | `baseline/metadata.yaml` 1–22 | `#Metadata` with the three `applicability-groups` | every group id matches `=~"^maturity-"` (`#OSPSBaseline`); `draft: true` is still set on the released catalog. As an excerpt it is **incomplete** on its own (`cue vet -d '#OSPSBaseline'` reports the missing `mapping-references` fields as incomplete values); it vets only as part of the whole `metadata.yaml` (verified 2026-10-02) |
| `04-mapping-document-osps-to-slsa.yaml` | `baseline/mappings/osps-to-slsa.yaml` (whole file, 88 lines) | `#MappingDocument` (`#OSPSMapping`): source pinned to `osps-baseline`, `entry-type: Control` → `Guideline`; 9 `relates-to` mappings | valid against `#OSPSMapping`; note the SLSA target entries are **requirement prose names**, not identifiers (e.g. `Build platform - Isolation strength - Isolated`), and the referenced SLSA version is `"1.0"` |
| `05-lexicon-sensitive-data-resource.yaml` | `baseline/lexicon.yaml` 223–245 | lexicon `term`/`definition` list entries (Sensitive Data, Sensitive Resource, start of Software Provenance) | **not** a Gemara `#Lexicon` document: the OSPS lexicon is a bare YAML list with keys `term`, `definition`, `synonyms`, `references`, whereas `gemara-v1.2.0/lexicon.cue` expects `terms[]` with `id`, `title`, `definition`. No schema validates this file; recorded as a source observation |

The fifth fixture is truncated mid-entry by design (lines 223–245 end inside the `Software
Provenance` definition); it parses as YAML but the last term is incomplete — it is there to show
the two definitions that `OSPS-AC-01.01` and `OSPS-BR-07.01` depend on.

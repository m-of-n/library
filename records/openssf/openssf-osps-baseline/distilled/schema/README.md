---
schema: "library-doc/v1"
id: openssf-osps-baseline-schema
record: openssf-osps-baseline
type: schema
updated: "2026-10-02"
reviewed_by: ""
---

# Schema — OSPS Baseline v2026.08.28

The baseline ships its own schema, in CUE, layered on the OpenSSF **Gemara** model. Everything
here is copied **verbatim** (Apache-2.0); nothing is derived.

| file | origin | what it constrains |
|---|---|---|
| `osps.cue` | `ossf/security-baseline` tag `v2026.08.28`, `schema/osps.cue` | `#OSPSBaseline` = `gemara.#ControlCatalog` + applicability-group ids must match `^maturity-` + mapping-reference ids must match `^[A-Za-z0-9][A-Za-z0-9._-]*$`; `#OSPSMapping` = `gemara.#MappingDocument` with `source-reference.reference-id` pinned to `"osps-baseline"` |
| `osps.cue.mod.module.cue` | same tag, `schema/cue.mod/module.cue` | pins the dependency `github.com/gemaraproj/gemara@v1` at **v1.2.0**, CUE language v0.16.0 |
| `gemara-v1.2.0/controlcatalog.cue` | `gemaraproj/gemara` tag `v1.2.0` (tarball sha256 `ab46861377246ef9be6821fd8e942b20f4a5a61c66fdb40c10f7e0a09b3eb5da`) | `#ControlCatalog`, `#Control`, `#AssessmentRequirement`; group and applicability referential integrity; Retired AR must not carry a recommendation |
| `gemara-v1.2.0/mappingdocument.cue` | same | `#MappingDocument`, `#TypedMapping`, `#Mapping`, `#MappingTarget` (strength 1–10, confidence-level), `#RelationshipType` (8 values), `#EntryType` (9 values); status `experimental` |
| `gemara-v1.2.0/metadata.cue` | same | `#Metadata`, `#Group`, `#Datetime`, `#ArtifactType` |
| `gemara-v1.2.0/collections.cue` | same | `#Catalog`, `#Log`, **`#Lifecycle`** (`*"Active" \| "Draft" \| "Deprecated" \| "Retired"`), `#ConfidenceLevel` |
| `gemara-v1.2.0/mapping_inline.cue` | same | `#MappingReference`, `#ArtifactMapping`, `#MultiEntryMapping`, `#EntryMapping` (used by `replaced-by`, `guidelines`, `threats`) |
| `gemara-v1.2.0/entities.cue` | same | `#Entity`, `#Actor` (catalog `author`), `#Resource`, `#Contact`, `#RACI` |
| `gemara-v1.2.0/lexicon.cue` | same | `#Lexicon` / `#LexiconTerm` — **not** what `baseline/lexicon.yaml` uses (see examples/README.md fixture 05) |

## How the source validates itself

The repository's CI action `.github/actions/compile-and-vet` builds `baseline-compiler`, assembles
the eight family files plus `metadata.yaml` into one `baseline.gemara.yaml`, then runs
`cue vet -d '#OSPSBaseline' . ../baseline.gemara.yaml` and one `cue vet -d '#OSPSMapping'` per
mapping document. The per-family YAML files are therefore **fragments**: only the compiled catalog
is a complete `#ControlCatalog`.

## Not done here

- `cue vet` was not run in the extract pass (no `cue` binary on the extraction host). **The verify
  / cross-check pass (2026-10-02) ran it** with cue v0.16.0 (the version `cue.mod/module.cue` pins),
  fetching `github.com/gemaraproj/gemara@v1.2.0` from the CUE registry: all 14 mapping documents vet
  clean against `#OSPSMapping`; the catalog assembled from `metadata.yaml` + the eight family files
  vets clean against `#OSPSBaseline` once the unquoted `mapping-references[].version` scalars
  (`2024`, `2.0`, `1.1`, `1.0`) are carried as strings (raw YAML types them int/float, which
  `#MappingReference.version: string` rejects — the repo's Go compiler marshals them as strings);
  fixtures 01 and 02 (each merged with the catalog `title` + `metadata`) and fixture 04 vet clean.
  See `../verification.md`.
- Gemara files not imported by the OSPS schema (`threatcatalog.cue`, `evaluationlog.cue`,
  `policy.cue`, …) are not copied. `#Control.threats` and `#Control.guidelines` exist in the schema
  but are **unused** by OSPS v2026.08.28 — its mappings live in separate MappingDocuments instead.

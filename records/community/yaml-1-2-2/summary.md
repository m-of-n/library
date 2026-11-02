---
schema: "library-summary/v1"
id: yaml-1-2-2
record: yaml-1-2-2
type: summary
updated: "2026-11-01"
---

# YAML Ain't Markup Language (YAML) version 1.2.2

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `unofficial`: a community specification, not ratified by a standards body |
| **Authors** | Copyright 2001-2009 Oren Ben-Kiki, Clark Evans, Ingy döt Net; present copyright YAML Language Development Team |
| **Published** | Revision 1.2.2, 2021-10-01 |
| **Identifier** | YAML 1.2, revision 1.2.2 |
| **Source** | https://yaml.org/spec/1.2.2/ |
| **Digest** | `2fe1bf40792df22ef8b8a5972a34c48e639969222e0bbae605aa9bb2ca85e9ab`, re-fetched 2026-11-01 unchanged |

## Overview

YAML 1.2.2 defines a data serialization language in two parts: a class of data objects (representations) and a character syntax for them (§3). It separates a representation graph, a serialization tree and a presentation stream, and comments, key order, styles and indentation belong to the last two, so application data may not depend on them (§3.1 to §3.2). This revision makes no normative change from 1.2 and exists to correct errors and add clarity (*Status of this Document*). Plain scalars get their types from a schema, not the grammar: tag resolution is left to the application (§3.3.2), and chapter 10 recommends the Failsafe, JSON and Core schemas, with Core as the default. So the same text can load as different values under different schemas, which is the fact the rest of this record turns on.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Parsing and type confusion hazards, with no security analysis of its own |
| Cryptography | `none` | Scalar canonical forms exist only for equality testing (§3.2.1.3) |
| This project | `core` | The library's records and mofn's human-review form are written in it |

- **DEC-002.** Decided by `ADR-0004` for KSA-CBOR, and YAML was never a candidate encoding. It bears on the human side of that decision: `SPEC-0002` §11 makes YAML the human-review form of a statement, converted one-to-one with the signed bytes. **This supersedes the topic's earlier note that the link was only an analogy**, which predates §11. YAML is not signed, but a wrong type on load changes the bytes a tool would encode.
- **`SPEC-0002` §11.3 tightens this spec.** It rejects forms §10.3.2 accepts, such as hexadecimal and octal integers, `null` and floats, and forbids timestamp resolution. It names no YAML version, which `design-log/0016-wallet-engine-v0/review.md` item 5 already asks about. The version matters: see the implementations note below.
- **The library's own reader differs too.** `bin/_yaml.py` keeps every plain scalar as a string, which is closer to Failsafe than to Core and is not a recommended schema. Tested 2026-11-01: `NO`, `9.3`, `Null`, `012` and `true` all stay strings. It also takes the last of a duplicate key silently, where §3.2.1.1 requires keys to be unique and §3.3 lists that as a load failure.

## Implementations

**Searched 2026-11-01.** Confirmed on GitHub or PyPI. PyYAML and ruamel.yaml were tested with the snippet below.

| Name | Kind | License | URL |
|---|---|---|---|
| yaml-test-suite | test suite | MIT | https://github.com/yaml/yaml-test-suite |
| libyaml | open source, C | MIT | https://github.com/yaml/libyaml |
| PyYAML 6.0.3 | open source, Python | MIT | https://github.com/yaml/pyyaml |
| ruamel.yaml 0.19.1 | open source, Python | not checked | https://pypi.org/project/ruamel.yaml/ |
| yaml | open source, TypeScript | ISC | https://github.com/eemeli/yaml |

**Implementations do not agree on the version.** On `NO`, `on`, `010` and a duplicate key, PyYAML 6.0.3 gave `False`, `True`, `8` and last-wins, while ruamel.yaml 0.19.1 (safe loader) gave `"NO"`, `"on"`, `10` and an error. Only the second matches §10.3.2 and §3.3. A library is not "YAML 1.2" because it says YAML.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled. No copy of the spec is committed.

## Limits

- **No determinism.** The spec leaves key order and anchor names to the processor (§3.1.1), so it gives no canonical text form. §3.2.1.3 canonical forms are per-scalar, for equality. `SPEC-0002` §11 has to supply its own rules, and does.
- **Recommended, not required.** Chapter 10 schemas are recommendations and §3.3.2 leaves resolution to the application, so the Core default does not bind an implementation in the way the test above assumes.
- **A known defect is left open.** The note in §10.2.2 says the float regular expression does not exactly match JSON's, and that this could not be addressed in 1.2.2.
- **Mostly a superset of 1.1, not wholly.** §6.8.1 says so and tells a 1.2 processor to treat 1.1 documents as 1.2 with warnings. A `%YAML 1.1` directive therefore does not ask for 1.1 typing.
- **`contradicts: strictyaml-why`.** See that record. On the Norway problem and duplicate keys, the critique describes implementations, and this spec says otherwise.
- **Read scope.** The front matter, chapter 1, chapter 3, chapter 10 and §6.8.1 were read whole, as text extracted from the HTML page. Chapter 2 was seen only by its headings. Chapters 4 to 9, the grammar, were not read beyond §6.8.1, so nothing here speaks to individual productions. The figures were not seen. Companion documents the spec points to were not read.

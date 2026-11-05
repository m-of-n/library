---
schema: "library-summary/v1"
id: strictyaml-why
record: strictyaml-why
type: summary
updated: "2026-11-05"
---

# StrictYAML: Design Justifications

|  |  |
|---|---|
| **Type** | web (the design justifications of a Python library) |
| **Maturity** | `unofficial`: one maintainer's project documentation |
| **Authors** | Colm O'Connor |
| **Published** | Undated. The footer says Copyright © 2018 - 2023, so `date` uses the later year |
| **Identifier** | https://hitchdev.com/strictyaml/why/, headed "Design Justifications" |
| **Source** | https://hitchdev.com/strictyaml/why/ and its ten sub-pages |
| **Digest** | `55822c1a90f4b280c6953e106c3bdc7b491691464ed65ef53832261a852b05dd`, index only, re-fetched 2026-11-01 and 2026-11-05 unchanged. Sub-page digests are in `content.note` |

## Overview

StrictYAML argues that YAML should be narrowed, not extended, for human-edited configuration. The core page, on the Norway problem, says implicit typing is a type-system bug in a markup language: an unquoted `NO` becomes `False`, `9.3` becomes a float beside the string `3.5.3`, and the surname `Null` becomes `None`. Its answer is that everything is a string unless a schema says otherwise, and the schema lives in code outside the data. On the same reasoning it refuses duplicate keys, explicit tags, flow style, anchors and aliases, and direct representations of Python objects, the last on security grounds. It accepts the costs: more repetition, a Python-only schema, and speed as a low priority.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | One sub-page ties object construction from YAML to arbitrary code execution |
| Cryptography | `none` | Nothing on signing or canonical forms |
| This project | `adjacent` | The hazards apply to anything reading YAML here, and the library is prior art, not a dependency |

- **DEC-002.** Decided by `ADR-0004`, and YAML was not a candidate encoding. The bearing is on `SPEC-0002` §11, the YAML human-review form. §11.3's lexical rules go the same way as this page: quoted byte strings and times, and no `null`, floats or YAML-only types. Since mofn#125 (2026-11-03) §11.3 also names its YAML, "YAML 1.2, core schema, restricted to what a YAML 1.1 parser reads the same way", and requires (MUST) quoting text such as `yes`, `no`, `on` and `off`. That answers the Norway problem by quoting and rejection, not by this page's schema. Its schema-outside-the-data stance also matches `ARCH-0001-PROPOSAL-v0.2.0` Appendix A, whose withdrawn profile would make a field declared textual read `no` as the string. §11 does not adopt the everything-is-a-string default, as integers stay integers.
- **`bin/_yaml.py` already behaves like this on typing.** Tested 2026-11-01, plain scalars stay strings. It differs on duplicate keys, taking the last one silently where StrictYAML refuses, and that gap is real for `record.yaml` files, because a duplicated field would validate.

## Implementations

**Searched 2026-11-01.** PyPI and GitHub. Not run.

| Name | Kind | License | URL |
|---|---|---|---|
| strictyaml 1.7.3 | open source, Python | MIT | https://github.com/crdoconnor/strictyaml |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, sub-page digests, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** A `web` record is outside FX-1's type scope. No page is committed.

## Limits

**`contradicts: yaml-1-2-2`.** The page is right about the hazard and wrong about where it comes from:

- **Norway is not YAML 1.2 behaviour.** The page says this bug "is intended behavior according to the YAML 1.2 specification". §10.3.2 of `yaml-1-2-2` resolves only `true`, `True`, `TRUE`, `false`, `False` and `FALSE` to booleans, so `NO` is a string under the default schema, and §1.2 says 1.2 removed many of the problematic implicit typing recommendations. An application may add resolution rules (§3.3.2, §10.4), but no recommended schema has this one. The behaviour is PyYAML's. Tested 2026-11-01 and again 2026-11-05, PyYAML 6.0.3 gave `False` and ruamel.yaml 0.19.1 gave `"NO"`. The syntax-typing page's `"yes"` and `"on"` examples have the same problem.
- **Duplicate keys are not "allowed in regular YAML".** `yaml-1-2-2` §3.2.1.1 requires unique keys and §3.3 lists non-unique keys as a load failure. PyYAML 6.0.3 does take the last one, as the page says, but ruamel.yaml 0.19.1 raised, so the page's list of parsers is out of date too.
- **Python objects are not part of the spec.** The page says "Regular YAML allows the direct representation of Python objects", but they come from a processor's local tags, which §10.4 says do not suffice for interoperable exchange.

**What survives.** `9.3` and `Null` do resolve to a float and a null under §10.3.2, as the page says, so the case for schema-driven typing stands without Norway.

Beyond that:

- **It is advocacy.** It comes from the maintainer of the library it justifies, with anecdotes for evidence. Counterarguments are linked to GitHub issues, and those were not read.
- **It says nothing on determinism.** A subset that fixes typing does not give a canonical text form.
- **Python-only schemas** are the page's own stated trade-off, which rules out a portable schema for us.
- **Relations.** Only `contradicts`, authored here, with the reason above. The earlier `see_also: yaml-1-2-2` repeated that edge and was dropped.
- **Read scope.** The index page and all ten sub-pages were read whole as text extracted from HTML. Linked issues, the rest of the StrictYAML documentation and the library code were not read. The usefulness note used to attribute the Norway argument to this URL, and it is on a sub-page.

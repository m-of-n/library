---
schema: "library-summary/v1"
id: schneier-attack-trees-1999
record: schneier-attack-trees-1999
type: summary
updated: "2026-09-29"
---

# Attack Trees

|  |  |
|---|---|
| **Type** | article (magazine) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Bruce Schneier |
| **Published** | *Dr. Dobb's Journal*, December 1999 |
| **Identifier** | https://www.schneier.com/academic/archives/1999/12/attack_trees.html |
| **Source** | https://www.schneier.com/academic/archives/1999/12/attack_trees.html (author's archive copy) |
| **Digest** | `not fetched` |

## Overview

The article that introduced attack trees as a way to model threats. An attack is
drawn as a tree whose root is the attacker's goal and whose children are ways to
reach it; **OR** nodes are alternatives and **AND** nodes are steps that must all
be done. Values are attached to the leaves — Boolean (possible/impossible,
legal/illegal, needs special equipment) or continuous (cost, probability) — and
propagate up the tree: an OR node takes its cheapest child, an AND node the sum
of its children. Comparing those values against an **attacker profile** (a bored
student vs organised crime) shows which attacks are realistic, and changing a
node's value supports "what if" analysis of countermeasures. The running example
is opening a safe; the article also sketches a tree for reading PGP-encrypted
email, and argues trees capture security knowledge in a **reusable** form — a
library of trees that can be plugged into larger ones.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The primary source for the attack-tree method. |
| Cryptography | adjacent | Uses PGP as a worked example; not about cryptography itself. |
| This project | core | Attack trees are the classic representation of multi-step attacks — input to tmodel's `AttackStep` / `AttackPath` (ARCH-0001 §3) and to RPT-0002 §4. |

Bears on **DEC-001** (object model — how attack paths are represented) and
**DEC-005** (MVP scope).

## Implementations

The article describes a method, not software. Dedicated attack-tree tools found
(details in RPT-0002 §4); searched 2026-09-29.

| Name | Kind | License | URL |
|---|---|---|---|
| SecurITree (Amenaza) | commercial tool | commercial | https://www.amenaza.com/securitree-main.php |
| ADTool | academic tool (attack–defence trees) | none stated in repo; unmaintained since 2017 | https://satoss.uni.lu/members/piotr/adtool/ |
| SeaMonster (SINTEF) | academic tool | open source; unmaintained since 2016 | https://sourceforge.net/projects/seamonster/ |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **No step ordering.** AND means "all of these", not "in this order"; the tree
  cannot express sequence, which ARCH-0001's *ordered* `AttackPath` needs.
  Later work (sequential-AND trees) adds it.
- **Countermeasures are not nodes.** Defences enter only as "what if" changes to
  values; attack–defence trees later made them explicit.
- **Informal.** A magazine article with no formal semantics; later academic work
  formalised attack trees.
- **Assumes expert builders.** Completeness depends on the analyst knowing the
  attacks; the article gives no method for finding missing branches.
- **Date discrepancy.** The author's archive dates it December 1999; the SEI
  survey (`sei-threat-modeling-methods-2018`, ref [17]) cites a reprint dated
  22 July 2001.

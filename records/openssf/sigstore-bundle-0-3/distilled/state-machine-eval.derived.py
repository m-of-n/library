#!/usr/bin/env python3
# DERIVED - not verbatim. Written by this library (FX-1 verify pass, library#151), not by Sigstore.
#
# Re-runs the guard evaluation of state-machine.yaml FROM THE COMMITTED FILE and compares it with the
# file's own `guard_evaluation` section. Pass 1 computed that section with scripts that stayed in a
# scratch directory; this script is the reproducible replacement.
#
#   python3 -I distilled/state-machine-eval.derived.py        (from the repository root, or anywhere)
#
# Inputs: distilled/state-machine.yaml only, read with BOTH of the library's YAML readers (bin/_yaml.py
# and bin/_record_yaml.py), which must agree. No .cache input: guards are over the model's own inputs.
# Dependencies: the Python standard library (ast, itertools). Exit 1 on any difference.
#
# What is evaluated (state-machine.yaml `conventions.guard_expr`): every guard_expr is a restricted
# Python boolean expression over the machine's inputs (names, single-quoted strings, integers, True,
# False, and, or, not, ==, !=, in, not in, tuples), compiled with ast and refused if it uses anything
# else. For each machine, every combination of the input domains that meets input_constraints is
# examined. A state whose outgoing transitions are all triggered by `evaluate` is a decision state:
# per combination, the targets of the firing transitions are counted, stated transitions alone and
# then all of them (one, several or none; plus "two transitions, same target"), and the combinations
# that do not reach exactly one target are grouped by which transitions fired. Any other state is
# event-driven: per combination, the most transitions one event enables, the combinations with no
# enabled transition, and the fewest and most events enabled.
import ast
import collections
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "bin"))
import _yaml  # noqa: E402
import _record_yaml  # noqa: E402
from pathlib import Path  # noqa: E402

SM = os.path.join(HERE, "state-machine.yaml")
OK_NODES = (ast.Expression, ast.BoolOp, ast.And, ast.Or, ast.UnaryOp, ast.Not, ast.Compare, ast.Eq,
            ast.NotEq, ast.In, ast.NotIn, ast.Name, ast.Load, ast.Constant, ast.Tuple)
FAILS = []


def compile_guard(expr, names):
    tree = ast.parse(expr, mode="eval")
    for node in ast.walk(tree):
        if not isinstance(node, OK_NODES):
            raise SystemExit(f"guard {expr!r}: {type(node).__name__} is outside the guard grammar")
        if isinstance(node, ast.Name) and node.id not in names:
            raise SystemExit(f"guard {expr!r}: unknown input {node.id!r}")
    return tree


def ev(node, env):
    if isinstance(node, ast.Expression):
        return ev(node.body, env)
    if isinstance(node, ast.BoolOp):
        vals = [ev(v, env) for v in node.values]
        return all(vals) if isinstance(node.op, ast.And) else any(vals)
    if isinstance(node, ast.UnaryOp):
        return not ev(node.operand, env)
    if isinstance(node, ast.Compare):
        left = ev(node.left, env)
        for op, comp in zip(node.ops, node.comparators):
            right = ev(comp, env)
            ok = {ast.Eq: lambda a, b: a == b, ast.NotEq: lambda a, b: a != b,
                  ast.In: lambda a, b: a in b, ast.NotIn: lambda a, b: a not in b}[type(op)](left, right)
            if not ok:
                return False
            left = right
        return True
    if isinstance(node, ast.Name):
        return env[node.id]
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Tuple):
        return tuple(ev(e, env) for e in node.elts)
    raise SystemExit(f"unexpected node {type(node).__name__}")


def value(s):
    s = str(s)
    return True if s == "true" else False if s == "false" else int(s) if s.lstrip("-").isdigit() else s


def show(v):
    return "true" if v is True else "false" if v is False else str(v)


def combos(m):
    names = [i["name"] for i in m["inputs"]]
    doms = [[value(v) for v in i["domain"]] for i in m["inputs"]]
    cons = [compile_guard(c, names) for c in m.get("input_constraints", []) or []]
    for vals in itertools.product(*doms):
        env = dict(zip(names, vals))
        if all(ev(c, env) for c in cons):
            yield env


def values_seen(m, envs):
    out = []
    for i in m["inputs"]:
        dom = [value(v) for v in i["domain"]]
        seen = [v for v in dom if any(e[i["name"]] == v for e in envs)]
        if len(seen) < len(dom):
            out.append(i["name"] + "=" + "|".join(show(v) for v in seen))
    return "; ".join(out) if out else "any"


def groups(m, lst):
    g = collections.OrderedDict()
    for env, fst, fall, tall in lst:
        g.setdefault((tuple(fst), tuple(fall), tuple(tall)), []).append(env)
    return [{"stated_fired": ", ".join(a) or "none", "all_fired": ", ".join(b) or "none",
             "targets_all": ", ".join(c) or "none", "inputs": str(len(e)), "values_seen": values_seen(m, e)}
            for (a, b, c), e in g.items()]


def evaluate(m):
    names = [i["name"] for i in m["inputs"]]
    trs = m["transitions"]
    comp = {t["id"]: compile_guard(t["guard_expr"], names) for t in trs if t.get("guard_expr")}
    envs = list(combos(m))
    dec, evs = [], []
    for s in m["states"]:
        out = [t for t in trs if t["from"] == s["name"]]
        if not out:
            continue
        if all(t["trigger"] == "evaluate" for t in out):
            c = collections.Counter()
            st_not, all_not = [], []
            for env in envs:
                fall = [t for t in out if t["id"] not in comp or ev(comp[t["id"]], env)]
                fst = [t for t in fall if t["kind"] == "stated"]
                tst = sorted({t["to"] for t in fst})
                tall = sorted({t["to"] for t in fall})
                c["stated_" + ("none" if not tst else "one" if len(tst) == 1 else "several")] += 1
                c["all_" + ("none" if not tall else "one" if len(tall) == 1 else "several")] += 1
                if len(fall) > 1 and len(tall) == 1:
                    c["all_two_transitions_same_target"] += 1
                ids_st, ids_all = [t["id"] for t in fst], [t["id"] for t in fall]
                if len(tst) != 1:
                    st_not.append((env, ids_st, ids_all, tall))
                if len(tall) != 1:
                    all_not.append((env, ids_all, ids_all, tall))
            d = {"state": s["name"], "inputs_examined": str(len(envs))}
            for k in ("stated_one", "stated_several", "stated_none", "all_one", "all_several", "all_none",
                      "all_two_transitions_same_target"):
                d[k] = str(c.get(k, 0))
            if st_not:
                d["stated_not_one"] = groups(m, st_not)
            if all_not:
                d["all_not_one"] = groups(m, all_not)
            dec.append(d)
        else:
            per = []
            for env in envs:
                by = collections.defaultdict(list)
                for t in out:
                    if t["id"] not in comp or ev(comp[t["id"]], env):
                        by[t["trigger"]].append(t)
                per.append(by)
            n_en = [sum(1 for v in by.values() if v) for by in per]
            evs.append({"state": s["name"],
                        "max_transitions_per_event": str(max((len(v) for by in per for v in by.values()), default=0)),
                        "combinations_without_exit": str(sum(1 for n in n_en if n == 0)),
                        "enabled_events": f"{min(n_en)} to {max(n_en)}"})
    return len(envs), dec, evs


def compare(where, mine, theirs):
    if mine != theirs:
        FAILS.append(where)
        print(f"DIFFERS {where}:\n  recomputed: {mine}\n  committed:  {theirs}")


def main():
    text = open(SM, encoding="utf-8").read()
    a = _yaml.parse(text)
    b = _record_yaml.load_yaml(Path(SM))
    if a != b:
        raise SystemExit("bin/_yaml.py and bin/_record_yaml.py read state-machine.yaml differently")
    committed = {g["machine"]: g for g in a["guard_evaluation"]}
    examined = 0
    for m in a["machines"]:
        n, dec, evs = evaluate(m)
        g = committed.get(m["id"])
        if g is None:
            FAILS.append(f"{m['id']}: no guard_evaluation entry"); continue
        compare(f"{m['id']} combinations", str(n), str(g["combinations"]))
        mine_dec = {d["state"]: d for d in dec}
        for d in g.get("decision_states", []) or []:
            compare(f"{m['id']} {d['state']}", mine_dec.pop(d["state"], None), d)
        for s in mine_dec:
            compare(f"{m['id']} {s} (decision state missing from the file)", mine_dec[s], None)
        mine_ev = {d["state"]: d for d in evs}
        for d in g.get("event_states", []) or []:
            compare(f"{m['id']} {d['state']}", mine_ev.pop(d["state"], None), d)
        for s in mine_ev:
            compare(f"{m['id']} {s} (event state missing from the file)", mine_ev[s], None)
        examined += n
        print(f"{m['id']}: {n} input combinations, {len(m['transitions'])} transitions, "
              f"{len(dec)} decision state(s), {len(evs)} event-driven state(s)")
    print(f"EXAMINED {examined} input combinations over {len(a['machines'])} machines; "
          f"{len(FAILS)} difference(s) from guard_evaluation")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())

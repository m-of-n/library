#!/usr/bin/env python3
"""DERIVED - not verbatim. Checks messages.yaml against the verbatim BNF.

    python3 -I check_messages.derived.py

For every message that carries a minimal_instance: its advanced text and its
canonical_hex must parse to the same S-expression, re-encode to exactly the
canonical bytes, and be accepted by the message's own production in section
9.2 (spki_bnf.derived.py), with no semantic issue. For every message with
fields: each field's `required` and `type` must agree with the 9.2 production
(a literal or <rule> item of the single alternative; nested lists are checked
by name). Prints how many messages, instances and fields it EXAMINED.
"""
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "bin"))
import _yaml  # noqa: E402


def load(name, fname):
    sp = importlib.util.spec_from_file_location(name, HERE / fname)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


bnf = load("bnf_cm", "spki_bnf.derived.py")
sx = bnf.sx
G = bnf.grammar_from_file()
QUANT = {"": ("once", True), "?": ("zero or one", False), "*": ("zero or more", False), "+": ("one or more", True)}


def top_items(alt):
    """Items between the outer ( keyword ... ), inline groups kept as ('list', first literal)."""
    items, depth, out = alt, 0, []
    for it in items:
        if it.kind == "lit" and it.val == "(":
            if depth == 1:
                out.append(None)  # start of an inline group; name taken from next literal
            depth += 1
        elif it.kind == "lit" and it.val == ")":
            depth -= 1
        elif depth == 1:
            out.append(it)
        elif depth == 2 and out and out[-1] is None:
            out[-1] = ("group", it.val if it.kind == "lit" else f"<{it.val}>")
    return out


def main():
    msgs = _yaml.parse((HERE.parent / "messages.yaml").read_text())["messages"]
    n_inst = n_field = bad = 0
    for m in msgs:
        name = m["name"]
        mi = m.get("minimal_instance")
        if isinstance(mi, dict) and "advanced" in mi:
            n_inst += 1
            a = sx.parse_advanced(mi["advanced"])
            c = sx.parse_canonical(bytes.fromhex(mi["canonical_hex"]))
            ok = a == c and sx.encode(a) == bytes.fromhex(mi["canonical_hex"]) \
                and len(sx.encode(a)) == int(mi["canonical_octets"]) \
                and bnf.accepts(G, name, a) and not bnf.semantic_issues(a)
            if not ok:
                bad += 1
                print(f"FAIL instance of <{name}>")
        if m.get("kind") == "object" and name in G.rules and m.get("fields") is not None:
            items = top_items(G.rules[name][0])
            body = items[1:]  # drop the object-name literal / ref
            want = []
            for it in body:
                if isinstance(it, tuple):
                    want.append((f"({it[1]} ...)", "once", True))
                else:
                    r, req = QUANT[it.q]
                    want.append((it.val, r, req))
            got = [(f["name"], f["repeat"], bool(f["required"]) if not isinstance(f["required"], str) else f["required"] == "true")
                   for f in m["fields"]]
            n_field += len(got)
            if want != got:
                bad += 1
                print(f"FAIL fields of <{name}>: BNF {want} vs file {got}")
    print(f"check_messages: examined {len(msgs)} messages, {n_inst} minimal instances, {n_field} top-level fields, {bad} failures")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()

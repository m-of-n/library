#!/usr/bin/env python3
"""DERIVED - not verbatim. Which requirement each case of test_spki.derived.py rests on.

test_spki.derived.py labels every case with the section of the draft that makes it
a MUST case. This file joins each case to the ids in ../requirements.yaml that state
the rule, so a failing case can be traced to a requirement and a requirement to the
cases that exercise it. It changes no case and no verdict.

    python3 -I schema/test_basis.derived.py          # summary; exit 1 on a case with no id or a dangling id
    python3 -I schema/test_basis.derived.py --list   # every case beside the ids and the first words of each

How a case is joined, in order:
  1. A case takes the production requirement of the rule it tests (BNF_*, AMBIG, RULE_CASES)
     and of every <name> its label mentions (text beginning `<name>::`).
  2. Every case takes the prose or inferred requirements that REGEX_RULES lists for its
     group and the words of its label. REGEX_RULES is written by hand and is meant to be read:
     each line is a claim that those requirements state the rule the label cites.
  3. A case whose label says [assumption] still takes the requirement it tests; the
     marker says the verdict rests on a reader choice (spki_sexp.derived.py A1 to A6),
     not that no rule is involved.
It reports how many cases it EXAMINED beside how many it joined: a case with no id is an error.
"""
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
REQ = HERE.parent / "requirements.yaml"


def load_tests():
    spec = importlib.util.spec_from_file_location("test_spki_b", HERE / "test_spki.derived.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def read_requirements():
    """{int id: text}, and {production name: [ids]}, by line scan (stdlib only)."""
    ids, prod = {}, {}
    cur = None
    for ln in REQ.read_text().split("\n"):
        m = re.match(r"^  - id: '[^']*#R-(\d+)'", ln)
        if m:
            cur = int(m.group(1)); continue
        m = re.match(r"^    text: (['\"])(.*)\1\s*$", ln)
        if m and cur is not None and cur not in ids:
            t = m.group(2).replace("''", "'")
            ids[cur] = t
            p = re.match(r"\s*<([^>]+)>::", t)
            if p:
                prod.setdefault(p.group(1), []).append(cur)
    return ids, prod


# (group, regex on the label, ids). All matching lines contribute. Group "*" = any group.
REGEX_RULES = [
    # canonical form, section 3.1 to 3.3
    ("canon", r"draft's own example", [36, 37]),
    ("canon", r"list of one byte string|nested lists|top level must be", [17, 27, 59]),
    ("canon", r"may be \"0\"|multi-digit|bytes are binary|':' is a legal", [37, 42, 43]),
    ("canon", r"display[ -]type", [41, 44, 52]),
    ("canon", r"no empty lists|empty list", [18, 28]),
    ("canon", r"first element", [19, 29, 30]),
    ("canon", r"leading 0|leading zeros|length|':'|colon|missing|non-negative", [37, 386]),
    ("canon", r"white space", [71, 387]),
    ("canon", r"unterminated|trailing|no list|empty input|inner list|stray", [59]),
    # advanced form, section 3.6
    ("adv", r"advanced form of its canonical example", [61, 65]),
    ("adv", r"tokens|token|digit after", [33, 62]),
    ("adv", r"white space", [69]),
    ("adv", r"quoted|escape|C string|\\x", [67]),
    ("adv", r"^(?!.*\\x).*hex", [68, 70]),
    ("adv", r"base64", [68, 70]),
    ("adv", r"nesting|list of one byte string|not a list|two S-expressions|trailing|unterminated", [17, 59]),
    ("adv", r"no empty lists", [18, 28]),
    ("adv", r"first element", [19, 29, 30]),
    ("adv", r"\(\*\) form", [157, 458]),
    ("adv", r"display[ -]type", [41, 44]),
    ("adv", r"length|\d:[a-z]", [65]),
    # transport form, section 3.4
    ("transport", r".", [63, 391]),
    ("transport", r"empty list", [18, 28]),
    ("transport", r"not canonical|trailing byte", [34, 391]),
    # BNF prose that the production alone does not carry
    ("bnf", r"fixes the field order|BNF order", [85, 86, 88, 89]),
    ("bnf", r"at most one|one subject|one not-before", [88]),
    ("bnf", r"name-cert has no tag|no <tag> in a name", [216, 217]),
    ("bnf", r"no <deleg>", [218]),
    ("bnf", r"issuer-name is one", [213, 214]),
    ("bnf", r"k-of-n|4\.5\.3", [143, 144, 145]),
    ("bnf", r"DSA sig-params", [108]),
    ("bnf", r"RSA: a single integer", [107]),
    ("bnf", r"<uri>|may be a <uri>", [73, 74]),
    ("bnf", r"new-cert", [189]),
    ("bnf", r"<online-id>|\(id \.\.\.\)", [177, 411]),
    ("bnf", r"one-time reply|reval-body", [288, 292]),
    ("bnf", r"subj-hash", [288]),
    ("bnf", r"valid-basic may be empty|empty cancel list", [421]),
    ("bnf", r"relative name", [229]),
    ("bnf", r"fully qualified name", [7]),
    ("bnf", r"display-typed", [45, 46]),
    ("bnf", r"<tag-prefix>|\(\* prefix|prefix", [331]),
    ("bnf", r"malformed \*-form|ambiguous|both match", [458]),
    ("bnf", r"BNF does not constrain <date>", [172, 408]),
    ("bnf", r"keyholder", [136, 141]),
    ("bnf", r"hash-op|\(do hash", [253, 257]),
    ("bnf", r"general-op", [455]),
    ("bnf", r"range|<gte>|<lte>|range-ordering", [329, 432]),
    ("bnf", r"case-sensitive", [78, 393]),
    # semantic checks
    ("semantic", r"K<N|K < N|N subjects listed", [143, 144, 145, 403]),
    ("semantic", r"empty string is not an integer", [58]),
    ("semantic", r"version integer", [115, 116, 400]),
    ("semantic", r"date", [172, 408]),
    ("semantic", r"md5 16 octets|md5 digests", [100]),
]

# cases of test_spki.derived.py that sit inside run_sexp as inline checks, with the ids they rest on
INLINE = [
    ("3.2 same bytes, different display types are unequal", [45, 46, 388]),
    ("3.2 same bytes, same display type are equal", [45, 388]),
    ("3.2 display type survives encode", [45]),
    ("a bare byte string is not an S-expression (3.3)", [59]),
    ("3.2.1: a list is not an integer", [53]),
    ("3.2.1 empty string is not the integer 0", [58]),
    ("4.9.1: a non-ASCII date is rejected", [172, 408]),
    ("4.9.1 a date with a display type is rejected [assumption]", [172, 408]),
]


def cases(T):
    """-> [(group, key, label, rule or None)] for every case table of test_spki.derived.py."""
    out = []
    for name, grp in (("CANON_ACCEPT", "canon"), ("CANON_REJECT", "canon"), ("ADV_ACCEPT", "adv"), ("ADV_REJECT", "adv"),
                      ("TRANSPORT_ACCEPT", "transport"), ("TRANSPORT_REJECT", "transport")):
        for c in getattr(T, name):
            out.append((grp, name, str(c[-1]), None))
    for name in ("BNF_ACCEPT", "BNF_REJECT", "BNF_ACCEPT_ODD"):
        for c in getattr(T, name):
            out.append(("bnf", name, str(c[2]), c[0]))
    for c in T.AMBIG:
        out.append(("bnf", "AMBIG", str(c[3]), c[0]))
    for c in T.SEMANTIC_CASES:
        out.append(("semantic", "SEMANTIC_CASES", str(c[2]), None))
    for c in T.RULE_CASES:
        out.append(("bnf", "RULE_CASES", str(c[3]), c[0]))
    for _ in T.INT_CASES:
        out.append(("fixed", "INT_CASES", "3.2.1 integer decoding", None))
    for _ in T.INT_ENCODE:
        out.append(("fixed", "INT_ENCODE", "3.2.1 integer encoding", None))
    for _ in T.DATE_ACCEPT + T.DATE_REJECT:
        out.append(("fixed", "DATE", "4.9.1 date", None))
    for _ in T.DATE_CASES:
        out.append(("fixed", "DATE_CASES", "4.9.1 date", None))
    for label, _ids in INLINE:
        out.append(("inline", "INLINE", label, None))
    return out


FIXED = {"INT_CASES": [53, 55, 56, 57, 389], "INT_ENCODE": [53, 56, 57, 58, 389], "DATE": [172, 174, 408],
         "DATE_CASES": [172, 174, 408]}
# assumption-only cases get the requirement they test; this is the one rule for all of them
ALIAS = {"crl-hash-list": "cancel-list", "hash-of-crl": "hash-of-pred", "reval-hash-list": "reval-list"}


def join(case, prod):
    grp, key, label, rule = case
    ids = set()
    if grp == "fixed":
        ids |= set(FIXED[key])
    if grp == "inline":
        ids |= set(dict(INLINE)[label])
    names = set(re.findall(r"<([a-z0-9-]+)>", label)) | ({rule} if rule else set())
    if names:
        for n in list(names):
            if n in ALIAS: names.add(ALIAS[n])
        for n in names:
            ids |= set(prod.get(n, []))
        if rule == "tag" and key == "AMBIG" and "both" in label:
            for n in ("tag-star", "tag-expr", "simple-tag", "tag-set"):
                ids |= set(prod.get(n, []))
    for g, rx, rids in REGEX_RULES:
        if g == grp and re.search(rx, label):
            ids |= set(rids)
    return sorted(ids)


def main():
    T = load_tests()
    texts, prod = read_requirements()
    cs = cases(T)
    rows = [(c, join(c, prod)) for c in cs]
    bad = [(c, i) for c, i in rows for x in i if x not in texts]
    empty = [c for c, i in rows if not i]
    distinct = {x for _, i in rows for x in i}
    print(f"examined: {len(cs)} cases in {len({c[1] for c in cs})} tables, {len(texts)} requirements")
    print(f"joined: {len(cs) - len(empty)} cases carry at least one id; {len(distinct)} distinct ids; {sum(len(i) for _, i in rows)} pairs")
    print(f"dangling ids: {len(bad)}; cases with no id: {len(empty)}")
    for c in empty:
        print("   NO ID:", c[1], c[2])
    if "--list" in sys.argv:
        for c, i in rows:
            print(f"{c[1]:16} {c[2][:70]!r:74} " + " ".join("R-%04d" % x for x in i))
    sys.exit(1 if bad or empty else 0)


if __name__ == "__main__":
    main()

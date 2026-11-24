#!/usr/bin/env python3
"""DERIVED - not verbatim. Compares the BNF fragments the draft prints in
sections 3-8 against its section 9.2 alphabetical list, by script, and writes
bnf-comparison.derived.txt (this script's whole output).

    python3 -I bnf_compare.derived.py [--write]

Method: every production of bnf-fragments-s3-s8.verbatim.bnf is looked up by
name in bnf-s9-2-alphabetical.verbatim.bnf. Same name and same right-hand side
(white space and hyphen wraps normalised) is IDENTICAL. Same name, different
right-hand side is DIFFERENT. A name absent from 9.2 is looked up in ALIAS, a
table of this library's judgement (each entry says why); the right-hand sides
are then compared with the alias applied to both. <valid-basic> and <tag-star> are
inlined before comparing, because 4.9 and 4.8 spell out what 9.2 names. What remains different
is a source defect or inconsistency of the draft, not of this script.
Finally the fragment grammar is laid over 9.2 and every MUST case of
test_spki.derived.py is re-run, to show which verdicts the disagreements change.
"""
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent


def load(name, fname):
    sp = importlib.util.spec_from_file_location(name, HERE / fname)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


bnf = load("bnf_c", "spki_bnf.derived.py")
tst = load("tst_c", "test_spki.derived.py")

# fragment name -> 9.2 name. These are judgement, not source facts.
ALIAS = {
    "cancel-list": ("crl-hash-list", "7.1 <cancel-list> and 9.2 <crl-hash-list> both: ( canceled <hash>* )"),
    "hash-of-pred": ("hash-of-crl", "7.1 'hash of the predecessor CRL or delta-CRL' and 9.2 <hash-of-crl>: both <hash>"),
    "reval-list": ("reval-hash-list", "7.2 and 9.2: ( valid <hash>+ )"),
    "threshold-subj": ("subj-thresh", "8.1 <subject5> lists <threshold-subj>; 9.2 <subject5> lists <subj-thresh>; 4.5.3 defines <subj-thresh>"),
    "tag-body": ("tag-expr", "8.1 <tag-body5> says <tag-body>, which no section defines; 9.2 says <tag-expr>"),
}
INLINE = {"valid-basic", "tag-star"}


def norm(rhs, alias=True):
    r = re.sub(r"\s+", " ", rhs).strip()
    if alias:
        for a, (b, _) in ALIAS.items():
            r = r.replace(f"<{a}>", f"<{b}>")
    return r


def inline(rhs, defs):
    for n in INLINE:
        if n in defs and "|" not in defs[n]:
            rr = re.sub(rf"<{n}>(?![?*+])", defs[n], rhs)
            rhs = rr
    return rhs


def main():
    out = []
    P = out.append
    t92 = (HERE / "bnf-s9-2-alphabetical.verbatim.bnf").read_text(encoding="utf-8")
    tfr = (HERE / "bnf-fragments-s3-s8.verbatim.bnf").read_text(encoding="utf-8")
    p92 = bnf.parse_productions(t92)
    pfr = bnf.parse_productions(tfr)
    d92 = {}
    for n, r, loc in p92:
        if n in d92:
            P(f"DUPLICATE in 9.2: <{n}> defined twice")
        d92[n] = norm(r, alias=False)
    P("# bnf-comparison.derived.txt -- DERIVED, written by bnf_compare.derived.py; do not edit")
    P(f"section 9.2 productions: {len(p92)}  (distinct names {len(d92)})")
    P(f"fragment productions (sections 3-8): {len(pfr)}  (distinct names {len({n for n, _, _ in pfr})})")
    P("")
    g92 = bnf.Grammar(t92)
    gfr = bnf.Grammar(tfr)
    both = set(g92.rules) | set(gfr.rules)
    P("== references no section defines (9.2 together with the fragments) ==")
    for g, label in ((g92, "9.2"), (gfr, "fragments")):
        und = sorted({r for n in g.rules for r in g.refs(n)} - both - bnf.LEXICAL)
        for u in und:
            users = sorted(n for n in g.rules if u in g.refs(n))
            P(f"  <{u}> is used by {label} rule(s) {', '.join('<'+x+'>' for x in users)} and defined nowhere")
    P("")
    P("== rules 9.2 defines that no other rule uses (and no section lists as a top-level object) ==")
    top = {"5-tuple", "acl", "crl", "delta-crl", "reval", "sequence", "cert", "name-cert", "pub-key", "signature",
           "hash", "op", "tag", "valid", "name", "integer", "s-expr"}
    used = {r for n in g92.rules for r in g92.refs(n)}
    unused = sorted(n for n in g92.rules if n not in used and n not in top)
    P("  " + ", ".join(f"<{n}>" for n in unused))
    P("  (9.1 lists as top-level: <5-tuple> <acl> <crl> <delta-crl> <reval> <sequence>; 3.8 adds <cert> <pub-key> <signature> <op>)")
    P("")
    P("== fragment vs 9.2, production by production ==")
    cnt = {"IDENTICAL": 0, "IDENTICAL-AFTER-ALIAS": 0, "DIFFERENT": 0, "ONLY-IN-FRAGMENT": 0}
    seen = {}
    rows = []
    for n, r, loc in pfr:
        seen.setdefault(n, []).append((r, loc))
        target = n
        aliased = False
        if n not in d92 and n in ALIAS:
            target, why = ALIAS[n]
            aliased = True
        if target not in d92:
            cnt["ONLY-IN-FRAGMENT"] += 1
            rows.append(f"  ONLY-IN-FRAGMENT <{n}> ({loc}): not defined in 9.2 and no alias")
            continue
        a = inline(norm(r), {**{k: norm(v) for k, v in d92.items()}})
        b = inline(norm(d92[target]), {**{k: norm(v) for k, v in d92.items()}})
        if norm(r, alias=False) == d92.get(n) and not aliased:
            cnt["IDENTICAL"] += 1
            rows.append(f"  IDENTICAL <{n}> ({loc})")
        elif a == b:
            cnt["IDENTICAL-AFTER-ALIAS"] += 1
            if aliased:
                how = "alias <%s> = <%s> (%s)" % (n, target, ALIAS[n][1])
            else:
                # name what made the two sides equal: each ALIAS the fragment uses, and each
                # INLINE name that only one side writes (pass 2: this used to print the inline
                # reason for every such row, including <crl>, <delta-crl> and <tag-body5>,
                # which are equal only through ALIAS)
                used = [f"<{x}> = <{ALIAS[x][0]}>" for x in ALIAS if f"<{x}>" in r]
                inl = [f"<{x}> inlined" for x in sorted(INLINE)
                       if (f"<{x}>" in d92[target]) != (f"<{x}>" in norm(r, alias=False))]
                how = "after " + "; ".join(used + inl)
            rows.append(f"  IDENTICAL-AFTER-ALIAS <{n}> ({loc}): {how}")
        else:
            cnt["DIFFERENT"] += 1
            rows.append(f"  DIFFERENT <{n}> ({loc})" + (f" [as <{target}>]" if aliased else ""))
            rows.append(f"      fragment: {r}")
            rows.append(f"      9.2     : {d92[target]}")
    out += rows
    P("")
    P("== names a fragment defines more than once, with different right-hand sides ==")
    for n, defs in seen.items():
        if len({norm(d[0], alias=False) for d in defs}) > 1:
            P(f"  <{n}>:")
            for r, loc in defs:
                P(f"      {loc}: {r}")
    P("")
    P("== 9.2 productions with no fragment (informational: defined only in section 9) ==")
    fr_names = {n for n, _, _ in pfr} | {ALIAS[n][0] for n in ALIAS}
    P("  " + ", ".join(f"<{n}>" for n in sorted(d92) if n not in fr_names))
    P("")
    P("== summary ==")
    P("  " + ", ".join(f"{k}={v}" for k, v in cnt.items()))
    # overlay grammar: fragments over 9.2, first definition per name
    overlay = {}
    for n, r, loc in pfr:
        tgt = ALIAS[n][0] if (n not in d92 and n in ALIAS) else n
        if tgt in overlay:
            continue
        rr = r
        for a, (b, _) in ALIAS.items():
            rr = rr.replace(f"<{a}>", f"<{b}>")
        overlay[tgt] = rr
    base = [(n, r, loc) for n, r, loc in p92 if n not in overlay]
    ptxt = "\n".join(f"<{n}>:: {r} ;" for n, r, _ in base + [(n, r, "") for n, r in overlay.items()])
    sx_ = bnf.sx
    nb, fails_base = tst.run_bnf(bnf)
    no, fails_over = tst.run_bnf(bnf, ptxt)
    P("")
    P("== verdicts that change when the fragment definitions replace 9.2's (cases of test_spki.derived.py) ==")
    P(f"  cases run under each grammar: {nb} / {no}; failing under 9.2: {len(fails_base)}; failing under fragments-over-9.2: {len(fails_over)}")
    for f in fails_over:
        if f not in fails_base:
            P("  CHANGED: " + f)
    text = "\n".join(out) + "\n"
    if "--write" in sys.argv:
        (HERE / "bnf-comparison.derived.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

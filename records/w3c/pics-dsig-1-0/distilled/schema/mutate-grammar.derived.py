#!/usr/bin/env python3
"""DERIVED mutation test for check-grammar.derived.py. Each mutation removes one
rule from a scratch copy of the recogniser; the self-test cases must then FAIL
(a case that cannot fail binds nothing). A mutation no case notices is a gap
and is reported as SURVIVED.

    python3 -I mutate-grammar.derived.py
"""
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
SRC = (HERE / "check-grammar.derived.py").read_text()

MUTATIONS = {
    "drop the duplicate-hash rule (7.2)": ("        if d[0][1] in seen:", "        if False:"),
    "drop the base64 length rule (alone: equivalent, b64decode also rejects it)": ("if not s or len(s) % 4 or not", "if not s or not"),
    "drop the base64 length rule and the b64decode check": [("if not s or len(s) % 4 or not", "if not s or not"), ("base64.b64decode(s, validate=True)", "pass")],
    "accept minute 60 in DSig dates": ("int(m[5]) <= 59 and (m[6]", "int(m[5]) <= 60 and (m[6]"),
    "drop the include+exclude rule (7.3.4.7)": ("if incl + excl > 1:", "if False:"),
    "drop the sigblock-only-as-label-option rule (7.3.1)": ('raise Reject("a sigblock extension is only valid', "pass  #"),
    "allow a Signature with no SigData": ('len(n) >= 3 and n[0] == ("str", "Signature")', 'len(n) >= 2 and n[0] == ("str", "Signature")'),
    "let a SigData carry many SigInfo": ("len(n) == 2 and quoted_name(n[0])", "len(n) >= 2 and quoted_name(n[0])"),
    "let PICS 1.1 quotedname admit '/'": ('PICS_URLCHAR = rf"(?:[{ALPHANUMPM}.$,;:&=?!*~@#_()]', 'PICS_URLCHAR = rf"(?:[{ALPHANUMPM}.$,;:&=?!*~@#_()/]'),
    "drop the resinfo-in-generic-label rule (6.2)": ('raise Reject("resinfo in a generic label', "pass  #"),
    "ignore a generic option inherited from the service section (added by pass 2)": ("for src in (opts, svc):", "for src in (opts,):"),
    "ignore a resinfo inherited from the service section (added by pass 2)": ("list(found) + list(svc_opts)", "list(found)"),
    "drop the generic-needs-for rule (6.2 L153; added by pass 2)": ('raise Reject("a generic label must include the for option', "pass  #"),
    "drop the duplicate-extension rule (PICS 1.1)": ("        if w == \"extension\" and prev[1][1] == url:", "        if False:"),
    "accept a mandatory DSig extension": ('if v[0][1].lower() != "optional":', "if False:"),
    "drop the field-list order rule": ("if k < pos:", "if False:"),
}


def main():
    survived = 0
    equivalent = 0
    for name, pairs in MUTATIONS.items():
        pairs = pairs if isinstance(pairs, list) else [pairs]
        text = SRC
        for a, b in pairs:
            if SRC.count(a) != 1:
                print(f"BROKEN   {name}: pattern occurs {SRC.count(a)} times")
                survived += 1
                break
            text = text.replace(a, b)
        else:
            pairs = None
        if pairs is not None:
            continue
        with tempfile.TemporaryDirectory() as d:
            p = pathlib.Path(d) / "mutant.py"
            p.write_text(text)
            r = subprocess.run([sys.executable, "-I", str(p)], capture_output=True, text=True)
        failed = [ln.split()[1] for ln in r.stdout.split("\n") if ln.startswith("BAD")]
        if failed:
            print(f"KILLED   {name}: fails {', '.join(failed)}")
        elif "equivalent" in name:
            print(f"EQUIVALENT {name}")
            equivalent += 1
        else:
            print(f"SURVIVED {name}")
            survived += 1
    killed = len(MUTATIONS) - survived - equivalent
    print(f"MUTATIONS {len(MUTATIONS)}: {killed} killed, {equivalent} equivalent, {survived} survived")
    return 1 if survived else 0


if __name__ == "__main__":
    sys.exit(main())

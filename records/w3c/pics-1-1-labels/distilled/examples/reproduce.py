#!/usr/bin/env python3
# DERIVED, not verbatim. Written by this library (FX-1 pass 1, examples lane) for pics-1-1-labels.
#
#   python3 -I reproduce.py [path/to/pics-1-1-labels.bin]
#
# Re-extracts every <pre> of the source HTML by a method independent of the one that wrote the
# fixtures (regular expressions and html.unescape; the writer used html.parser) and checks:
#   (a) every fixture in this directory, and the body of every *.verbatim.txt in ../schema, is
#       byte-identical to its <pre> block;
#   (b) every label list, request header, response header and query line against the derived
#       grammar (../schema/check-grammar.derived.py), comparing the result with the EXPECTED
#       result written in EXPECT below and in README.md. An example the grammar rejects is a finding
#       about the source, never repaired in a fixture; the minimal repair under which it parses
#       is applied to a COPY and reported;
#   (c) what can be computed about the examples: Content-Length against the bytes shown, the
#       positional rules of section 12.3 against Appendix B, the URLs decoded from each query
#       against the URLs the Appendix B prose lists, the HTML escape table of section 10, and the
#       length of a base64 MD5 (the source prints no base64 string, so there is nothing printed to
#       check against: this is said, not faked).
# Exit 1 if (a) differs, or if any outcome differs from EXPECT. Prints how many it EXAMINED.

import hashlib
import html
import importlib.util
import pathlib
import re
import sys
import urllib.parse

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SCHEMA = HERE.parent / "schema"
RECORD = HERE.parent.parent / "record.yaml"

spec = importlib.util.spec_from_file_location("check_grammar", SCHEMA / "check-grammar.derived.py")
cg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cg)

# fixture file -> index of its <pre> (counting from 0 in document order)
FIXTURE_PRE = {
    "ex01-general-form-template.txt": 0, "ex02-label-list-long.txt": 1, "ex03-label-list-compact-full.txt": 2,
    "ex04-label-list-minimal.txt": 3, "ex05-multi-value.txt": 5, "ex06-pics-label-header-template.txt": 6,
    "ex07-html-meta-template.txt": 7, "ex08-html-escape-table.txt": 8, "ex09-http-request.txt": 9,
    "ex10-http-response.txt": 10, "ex11-bureau-sample-query.txt": 13,
    "ex12-appb1-generic-request.txt": 16, "ex13-appb1-generic-response.txt": 17,
    "ex14-appb2-normal-request.txt": 18, "ex15-appb2-normal-response.txt": 19,
    "ex16-appb3-tree-request.txt": 20, "ex17-appb3-tree-response.txt": 21,
    "ex18-appb4-generic-tree-request.txt": 22, "ex19-appb4-generic-tree-response.txt": 23,
}
SCHEMA_PRE = {
    "labels-s07-detailed-syntax.verbatim.txt": 4, "http-request-s11-3.verbatim.txt": 11,
    "http-response-s11-4.verbatim.txt": 12, "bureau-query-s12-2.verbatim.txt": 14,
}
MARKER = "---- verbatim <pre> begins on the next line ----\n"
NOT_FIXTURE_PRE = {15: "the Acknowledgments list (section 16), not an example"}

# expected outcome of each check: (kind, expected) ; "accept"/"reject"/"n/a"
EXPECT = {
    "ex01": "n/a", "ex02": "accept", "ex03": "accept", "ex04": "accept", "ex05": "accept", "ex06": "n/a",
    "ex07": "n/a", "ex09.header": "accept", "ex10.protocol": "accept", "ex10.label": "accept",
    "ex11": "accept",
    "ex12.raw": "reject", "ex12.repaired": "accept", "ex14.raw": "reject", "ex14.repaired": "accept",
    "ex16.raw": "reject", "ex16.repaired": "accept", "ex18.raw": "reject", "ex18.repaired": "accept",
    "ex13.raw": "reject", "ex13.nocomments": "accept", "ex15.raw": "reject", "ex15.nocomments": "accept",
    "ex17.raw": "reject", "ex17.nocomments": "accept", "ex19.raw": "accept", "ex19.nocomments": "accept",
}

fails = []
examined = 0


def check(label, cond, detail=""):
    global examined
    examined += 1
    if not cond:
        fails.append(label + (": " + detail if detail else ""))
    return cond


def outcome(key, result, note=""):
    got = "accept" if result else "reject"
    exp = EXPECT[key]
    check("%s expected %s, got %s" % (key, exp, got), got == exp)
    print("  %-16s %-6s (expected %s)%s %s" % (key, got, exp, "" if got == exp else "  <-- DIFFERS", note if result else result.reason))
    return result


# ------------------------------------------------------------------ (a) re-extraction

def pres(raw):
    out = []
    for m in re.finditer(r"<pre[^>]*>(.*?)</pre>", raw, re.S | re.I):
        inner = re.split(r"<P>", m.group(1), maxsplit=1, flags=re.I)[0]  # the last <PRE> is never closed before the footer
        txt = html.unescape(re.sub(r"<[^>]*>", "", inner))
        out.append(txt[1:] if txt.startswith("\n") else txt)
    return out


def main():
    binp = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / ".cache" / "pics-1-1-labels.bin"
    data = binp.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    rec = RECORD.read_text(encoding="utf-8")
    m = re.search(r"sha256:\s*['\"]?([0-9a-f]{64})", rec)
    print("source %s sha256 %s" % (binp.name, sha))
    check("source digest equals content.sha256 in record.yaml", bool(m) and m.group(1) == sha,
          "record.yaml says %s" % (m.group(1) if m else "nothing"))
    raw = data.decode("latin-1")
    blocks = pres(raw)
    npre = len(re.findall(r"<pre\b", raw, re.I))
    check("count of <pre> equals count of </pre>-terminated blocks", npre == len(blocks) == 24, "%d vs %d" % (npre, len(blocks)))
    cut = [i for i, mm in enumerate(re.finditer(r"<pre[^>]*>(.*?)</pre>", raw, re.S | re.I)) if re.search(r"<P>", mm.group(1), re.I)]
    check("exactly one <pre> (the last) swallows the page footer", cut == [23], str(cut))
    print("(a) re-extraction: %d <pre> blocks; block 23 is closed only after the footer (source defect D1), fixture cut at its <P>" % len(blocks))
    n_fix = 0
    for name, idx in FIXTURE_PRE.items():
        got = (HERE / name).read_bytes()
        want = blocks[idx].encode("utf-8")
        n_fix += 1
        check("fixture %s is byte-identical to <pre> %d" % (name, idx), got == want,
              "%d bytes on disk, %d in the HTML" % (len(got), len(want)))
    n_sch = 0
    for name, idx in SCHEMA_PRE.items():
        txt = (SCHEMA / name).read_bytes().decode("utf-8")
        check("schema/%s has its marker line" % name, MARKER in txt)
        body = txt.split(MARKER, 1)[1] if MARKER in txt else ""
        n_sch += 1
        check("schema/%s body is byte-identical to <pre> %d" % (name, idx), body.encode("utf-8") == blocks[idx].encode("utf-8"))
    used = set(FIXTURE_PRE.values()) | set(SCHEMA_PRE.values()) | set(NOT_FIXTURE_PRE)
    check("every one of the 24 <pre> blocks is a fixture, a schema file, or named as not one", used == set(range(24)), str(sorted(set(range(24)) - used)))
    on_disk = sorted(p.name for p in HERE.iterdir() if p.name.startswith("ex") and p.suffix == ".txt")
    check("no fixture file on disk that is not in the table", on_disk == sorted(FIXTURE_PRE), str(set(on_disk) ^ set(FIXTURE_PRE)))
    print("    %d fixtures and %d verbatim grammar files byte-identical to their <pre> (pre 15 is the Acknowledgments list)" % (n_fix, n_sch))

    fx = {n[:4]: (HERE / n).read_text(encoding="utf-8") for n in FIXTURE_PRE}

    # ------------------------------------------------------------------ (b) grammar
    print("(b) grammar, EXPECTED vs got (derived grammar: ../schema/*.derived.abnf)")
    print("  ex01, ex06, ex07: n/a, each is a template with a placeholder (<service url>, [option...], <labellist>)")
    for k in ("ex02", "ex03", "ex04", "ex05"):
        outcome(k, cg.parse_labellist(fx[k]))
    hdrs = unfold_headers(fx["ex09"])
    pr = [h for h in hdrs if h.lower().startswith("protocol-request:")]
    check("ex09 has one Protocol-Request header", len(pr) == 1)
    outcome("ex09.header", cg.parse_request_header(pr[0]))
    head, body = split_response(fx["ex10"])
    hh = unfold_headers(head)
    outcome("ex10.protocol", cg.parse_protocol_header([h for h in hh if h.lower().startswith("protocol:")][0]))
    outcome("ex10.label", cg.parse_label_header([h for h in hh if h.lower().startswith("pics-label:")][0]))
    check("ex10: the PICS-Label header is folded onto a continuation line", "PICS-Label:\n (" in fx["ex10"])
    check("ex10: body after the blank line is a placeholder, not a document", body.strip().startswith("...contents of foo.html"))
    q11 = cg.unfold_request(fx["ex11"])
    outcome("ex11", cg.parse_request_line(q11))
    # queries of Appendix B: raw, then repaired
    qs = {"ex12": fx["ex12"], "ex14": fx["ex14"], "ex16": fx["ex16"], "ex18": fx["ex18"]}
    decoded = {}
    for k, t in qs.items():
        line = cg.unfold_request(t)
        r = cg.parse_request_line(line)
        outcome(k + ".raw", r)
        rep, notes = repair_query(line)
        outcome(k + ".repaired", cg.parse_request_line(rep), "repairs: " + ", ".join(notes))
        decoded[k] = decode_query(rep)
    # Appendix B responses
    resp = {"ex13": ("generic", "ex12"), "ex15": ("normal", "ex14"), "ex17": ("tree", "ex16"), "ex19": ("generic+tree", "ex18")}
    structs = {}
    for k, (mode, q) in resp.items():
        head, body = split_response(fx[k])
        outcome(k + ".raw", cg.parse_labellist(body))
        stripped, ncom, in_quote = strip_comments(body)
        check("%s: no ';' inside a quoted string (so stripping comments cannot damage data)" % k, in_quote == 0)
        outcome(k + ".nocomments", cg.parse_labellist(stripped), "(%d comment runs removed)" % ncom)
        structs[k] = (mode, walk(stripped))
        # missing blank line between headers and body
        has_blank = "\n\n(" in fx[k]
        print("    %s: blank line between headers and body: %s" % (k, has_blank))
        # Content-Length
        m = re.search(r"Content-Length:\s*(\d+)", head)
        printed = int(m.group(1))
        b = body.rstrip("\n")
        lf, crlf = len(b.encode("ascii")), len(b.encode("ascii")) + b.count("\n")
        mini = " ".join(t for t, _ in cg.tokenize(stripped))
        mini2 = re.sub(r"\( ", "(", re.sub(r" \)", ")", mini))
        print("    %s: Content-Length printed %d; body bytes LF %d, CRLF %d, comments stripped and whitespace collapsed %d (%d with no space inside parentheses)"
              % (k, printed, lf, crlf, len(mini), len(mini2)))
        check("%s Content-Length is a number" % k, True)
    # mutation sweep over every label list that parses (the schema runner sweeps only ex02-ex05)
    sweep = {k: fx[k] for k in ("ex02", "ex03", "ex04", "ex05")}
    for k in ("ex13", "ex15", "ex17", "ex19"):
        sweep[k] = strip_comments(split_response(fx[k])[1])[0]
    sweep["ex10"] = " ".join(
        h.split(":", 1)[1] for h in unfold_headers(split_response(fx["ex10"])[0]) if h.lower().startswith("pics-label:"))
    lists, mutants, survivors = cg.mutation_sweep(sweep)
    check("mutation sweep examined every list (%d of %d)" % (lists, len(sweep)), lists == len(sweep))
    check("mutation sweep: %d single-edit mutants all rejected" % mutants, mutants > 0 and not survivors, "; ".join(survivors[:5]))
    print("    mutation sweep: %d lists, %d single-edit mutants (delete a paren, a quote, a keyword letter, the version, the last character), %d still accepted" % (lists, mutants, len(survivors)))
    # ------------------------------------------------------------------ (c) computed checks
    print("(c) computed checks")
    holdings = {
        "http://www.ages.org/our-service/v1.0/": {("http://www.w3.org/pub", True), ("http://www.w3.org/pub/WWW/", True),
                                                   ("http://www.w3.org/pub/WWW/Daemon", True), ("http://www.w3.org/pub/WWW/PICS", True),
                                                   ("http://www.w3.org/pub/WWW/Overview.html", False)},
        "http://www.rsac.org/v1.0": {("http://www.w3.org/pub/WWW", True), ("http://www.w3.org/pub/WWW/Daemon", True),
                                     ("http://www.w3.org/pub/WWW/PICS", True), ("http://www.w3.org/pub/WWW/Daemon/Overview.html", False),
                                     ("http://www.w3.org/pub/WWW/TheProject.html", False)},
        "http://unknown.com": set(),
    }
    req_urls = ["http://www.w3.org/pub/WWW/", "http://www.w3.org/pub/WWW/TheProject.html", "http://www.w3.org/unknown"]
    req_svcs = list(holdings)
    for k, (mode, st) in structs.items():
        qk = resp[k][1]
        d = decoded[qk]
        check("%s: query %s decodes to the three URLs of the Appendix B prose (after repair)" % (k, qk),
              [u.rstrip("+") for u in d["u"]] == req_urls and d["s"] == req_svcs, str(d))
        sv = st
        check("%s: three service-infos, the third error(no-ratings): one per requested service, same order (12.3)" % k,
              len(sv) == 3 and sv[2][0] == "no-ratings")
        for i, s in enumerate(sv[:2]):
            check("%s: service %d is %s, the %d-th requested" % (k, i + 1, s[1], i + 1), s[1].strip('"') == req_svcs[i])
            check("%s: service %d has one entry per requested URL (3): %d" % (k, i + 1, len(s[2])), len(s[2]) == 3)
            for j, e in enumerate(s[2]):
                labs = e[1] if e[0] == "set" else ([e] if e[0] == "label" else [])
                if mode in ("tree", "generic+tree"):
                    check("%s svc %d entry %d: %s entries are a parenthesised set or an error" % (k, i + 1, j + 1, mode), e[0] in ("set", "error"))
                else:
                    check("%s svc %d entry %d: a single label or an error" % (k, i + 1, j + 1), e[0] in ("label", "error"))
                for L in labs:
                    o = L[1]
                    gen = o.get("generic", o.get("gen", "f")).lower() in ("t", "true")
                    fo = o.get("for")
                    check("%s svc %d entry %d: a generic label carries for" % (k, i + 1, j + 1), (not gen) or fo is not None)
                    if mode in ("tree", "generic+tree"):
                        check("%s svc %d entry %d: every label of a tree response carries for (12.3)" % (k, i + 1, j + 1), fo is not None)
                    if mode in ("generic", "generic+tree"):
                        check("%s svc %d entry %d: a %s response returns only generic labels" % (k, i + 1, j + 1, mode), gen)
                    if fo is not None:
                        check("%s svc %d entry %d: (for, generic) %s is a label the server holds" % (k, i + 1, j + 1, (fo.strip('"'), gen)),
                              (fo.strip('"'), gen) in holdings[req_svcs[i]])
                if mode in ("generic", "normal") and e[0] == "label":
                    fo = e[1].get("for", "").strip('"')
                    gen = e[1].get("generic", e[1].get("gen", "f")).lower() in ("t", "true")
                    u = req_urls[j]
                    # the label must apply: generic label -> prefix of the requested URL; specific -> equal
                    check("%s svc %d entry %d: the label's URL applies to the requested URL" % (k, i + 1, j + 1),
                          (gen and u.startswith(fo)) or (not gen and u == fo))
    # the explicit 'no-label' of 12.3 vs the grammar's not-labeled
    html_txt = re.sub(r"<[^>]*>", "", raw)
    check("12.3 prose says the server should include the \"no-label\" message", '"no-label"' in html.unescape(html_txt))
    check("the grammar of section 7 has not-labeled and no 'no-label'", "no-label" not in fx["ex02"] and "not-labeled" in blocks[4] and "no-label" not in blocks[4])
    print("    12.3 prose names a \"no-label\" message; the section 7 grammar defines only not-labeled (finding D6)")
    # section 12.1 decode
    d = decode_query(q11)
    print("    ex11 decodes to u=%s s=%s" % (d["u"], d["s"]))
    check("ex11: u and s decode to the URLs the 12.1 prose names", d["u"] == ["http://www.questionable.org/images"] and d["s"] == ["http://www.gcf.org/v2.5"])
    # first URL of every Appendix B query: trailing '+'
    for qk in ("ex12", "ex14", "ex16", "ex18"):
        raw_u = decode_query(cg.unfold_request(qs[qk]).replace('&"', '"&'))["u"][0]
        check("%s: the first u= decodes to the prose URL plus a trailing '+' (D3)" % qk, raw_u == req_urls[0] + "+", raw_u)
    print("    all four Appendix B queries end the first u= value with '+': decoded as form data that is a trailing space (finding D3)")
    # section 10 escape table
    tbl = re.findall(r"^\s*(\S)\s+(&\S+?;)\s+/\*", fx["ex08"], re.M)
    check("ex08: three rows", len(tbl) == 3, str(tbl))
    for ch, ent in tbl:
        check("ex08: %s decodes to %r" % (ent, ch), html.unescape(ent) == ch)
    lab = " ".join(fx["ex04"].split())
    esc = lab.replace("&", "&amp;").replace("'", "&#39;").replace(">", "&gt;")
    meta = "<META http-equiv=\"PICS-Label\" content='" + esc + "'>"
    check("section 10: an embedded label with the three escapes survives unescaping", html.unescape(re.search(r"content='(.*)'>", meta).group(1)) == lab)
    lab2 = "(PICS-1.1 \"http://a/?x=1&y=2\" l for \"http://a/it's\" r (a 1))"
    esc2 = lab2.replace("&", "&amp;").replace("'", "&#39;").replace(">", "&gt;")
    check("section 10: a label with & and ' needs the escapes inside content='...'", "'" not in esc2 and html.unescape(esc2) == lab2)
    check("section 10 (derived): escaped label still has no raw apostrophe and parses after unescape", bool(cg.parse_labellist(html.unescape(esc2))))
    # base64 / MD5 lengths
    import base64
    d16 = hashlib.md5(b"").digest()
    b64 = base64.b64encode(d16).decode()
    check("MD5 digest is 16 bytes and its base64 is 24 characters with '==' padding", len(d16) == 16 and len(b64) == 24 and b64.endswith("=="))
    check("the derived grammar accepts a real MD5 in base64 (md5 \"%s\")" % b64, bool(cg.parse_labellist('(PICS-1.1 "http://a/" l md5 "%s" r (a 1))' % b64)))
    check("the derived grammar accepts it with MIC-md5 as well", bool(cg.parse_labellist('(PICS-1.1 "http://a/" l MIC-md5 "%s" r (a 1))' % b64)))
    sig = base64.b64encode(bytes(range(64))).decode()
    wrapped = "\n".join(sig[i:i + 60] for i in range(0, len(sig), 60))
    check("a signature split into 60-character lines is accepted (section 13)", bool(cg.parse_labellist('(PICS-1.1 "http://a/" l signature-RSA-MD5 "%s" r (a 1))' % wrapped)))
    n_b64 = len(re.findall(r"(?i)\b(?:md5|mic-md5|signature-rsa-md5)\s+\"", "".join(fx.values())))
    print("    base64 strings printed in the examples: %d (the source prints no MD5 or signature value; the lengths above are computed, not checked against the source)" % n_b64)
    check("the source prints no base64 value in any example", n_b64 == 0)

    print("EXAMINED %d checks, %d FAILED" % (examined, len(fails)))
    for f in fails:
        print("  FAIL", f)
    return 1 if fails else 0


# ------------------------------------------------------------------ helpers

def unfold_headers(text):
    hs = []
    for ln in text.split("\n"):
        if ln == "":
            break
        if ln[0] in " \t" and hs:
            hs[-1] += " " + ln.strip()
        else:
            hs.append(ln.rstrip())
    return hs


def split_response(text):
    """(header block, body). The body is what follows the first blank line, or, where there is none
    (Appendix B 18.2 to 18.4), the first line that begins with '('."""
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        if ln == "" and i > 0:
            return "\n".join(lines[:i]), "\n".join(lines[i + 1:])
        if ln.startswith("(") and i > 0:
            return "\n".join(lines[:i]), "\n".join(lines[i:])
    return text, ""


def strip_comments(body):
    n = 0
    inq = 0
    out = []
    for ln in body.split("\n"):
        q = False
        for i, ch in enumerate(ln):
            if ch == '"':
                q = not q
            if ch == ";":
                if q:
                    inq += 1
                else:
                    n += 1
                    ln = ln[:i]
                    break
        out.append(ln)
    return "\n".join(out), n, inq


def repair_query(line):
    notes = []
    r = line
    if '&"' in r:
        notes.append("R1 move %d '&' from inside the closing quote to after it" % r.count('&"'))
        r = r.replace('&"', '"&')
    if "%2B" in r:
        notes.append("R2 opt=generic%2Btree -> opt=generic+tree (the grammar's literal)")
        r = r.replace("%2B", "+")
    return r, notes or ["none"]


def decode_query(line):
    q = line.split("?", 1)[1].rsplit(" HTTP", 1)[0]
    d = {"u": [], "s": [], "other": []}
    for part in q.split("&"):
        k, _, v = part.partition("=")
        v = v.strip('"')
        v = urllib.parse.unquote(v)
        (d[k] if k in ("u", "s") else d["other"]).append(v if k in ("u", "s") else part)
    return d


def walk(text):
    """A structural walk of a label list the grammar has already accepted:
    [(kind, service-url, [entries])]. An entry is ("label", options), ("set", [labels]) or ("error", kind)."""
    toks = [t for t, _ in cg.tokenize(text)]
    i = 2
    services = []

    def group_end(j):  # toks[j] == "(" -> index after the matching ")"
        depth = 0
        while True:
            if toks[j] == "(":
                depth += 1
            elif toks[j] == ")":
                depth -= 1
                if depth == 0:
                    return j + 1
            j += 1

    def single(j):
        opts = {}
        while toks[j].lower() not in ("ratings", "r"):
            kw = toks[j].lower()
            if toks[j + 1] == "(":
                j = group_end(j + 1)
                opts.setdefault(kw, "(…)")
            else:
                opts[kw] = toks[j + 1]
                j += 2
        return ("label", opts), group_end(j + 1)

    while toks[i] != ")":
        if toks[i].lower() == "error":
            services.append(("no-ratings", None, []))
            i = group_end(i + 1)
            continue
        url = toks[i]
        i += 1
        ents = []
        if toks[i].lower() == "error":
            services.append(("error", url, []))
            i = group_end(i + 1) if toks[i + 1] == "(" else i + 2
            continue
        while toks[i].lower() not in ("labels", "l"):  # service-level options
            i = group_end(i + 1) if toks[i + 1] == "(" else i + 2
        i += 1
        while toks[i] != ")" and not toks[i].startswith('"') and not (toks[i].lower() == "error" and toks[i + 2].lower() == "no-ratings"):
            if toks[i] == "(":
                j = i + 1
                labs = []
                while toks[j] != ")":
                    e, j = single(j)
                    labs.append(e)
                ents.append(("set", labs))
                i = j + 1
            elif toks[i].lower() == "error":
                ents.append(("error", toks[i + 2].lower()))
                i = group_end(i + 1)
            else:
                e, i = single(i)
                ents.append(e)
        services.append(("service", url, ents))
    return services


if __name__ == "__main__":
    sys.exit(main())

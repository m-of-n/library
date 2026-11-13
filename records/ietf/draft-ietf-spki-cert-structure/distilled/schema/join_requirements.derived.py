"""DERIVED - not verbatim. Wires `constrained_by` in ../messages.yaml from ../requirements.yaml.

Three layers, each printed so a reader can accept or drop a pair:

  1. PROPOSE (default). Candidate pairs by source_lines overlap and by name, as
     the first version of this script did. A candidate is not a join.
  2. PRODUCTION RULE (mechanical). A requirement whose text begins `<name>::` is
     the production for message `name`, so it constrains that message. It also
     constrains each field whose type token appears on the right-hand side of
     that production. A section-text name and its section-9.2 name are one
     structure (ALIAS), so each gets the other's production.
  3. CURATED (read by a person). CURATED below lists, for each message and
     field, the prose or inferred requirements that actually constrain it,
     chosen by reading every requirement in ../requirements.yaml against every
     message and field. Where a requirement has split_of children, the child that
     is the exact rule is cited, not the parent, except where the parent carries
     several rules that all bear on the object.

    python3 -I schema/join_requirements.derived.py            # propose + report
    python3 -I schema/join_requirements.derived.py --wire     # print the final pairs
    python3 -I schema/join_requirements.derived.py --apply    # (re)write every constrained_by in messages.yaml; safe to rerun

Every mode prints how many requirements, messages and fields it EXAMINED beside
what it found, and lists anything left unwired. --apply rewrites only the
`constrained_by:` lines and their id lists (and the counts in `coverage`), by line, so no other
text of messages.yaml can change.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "bin"))
import _yaml

D = HERE.parent
PFX = "draft-ietf-spki-cert-structure#R-"
MSGFILE = D / "messages.yaml"

ALIAS = {"crl-hash-list": "cancel-list", "cancel-list": "crl-hash-list",
         "hash-of-crl": "hash-of-pred", "hash-of-pred": "hash-of-crl",
         "reval-hash-list": "reval-list", "reval-list": "reval-hash-list"}

# ---------------------------------------------------------------------------
# CURATED. {message: {"msg": [R numbers], "fields": {field path: [R numbers]},
#                     "all_fields": [R numbers added to every field]}}
# Productions are NOT listed: layer 2 adds them.
# ---------------------------------------------------------------------------
C = {}
def m(name, msg=(), fields=None, all_fields=()):
    C[name] = {"msg": list(msg), "fields": {k: list(v) for k, v in (fields or {}).items()}, "all_fields": list(all_fields)}

m("5-tuple", [22, 26, 294, 295, 297, 298, 307, 308, 345, 424, 425, 429, 447, 453],
  {"issuer5": [295, 306, 307, 309], "subject5": [295, 309, 456], "deleg5": [310], "tag-body5": [311], "valid5": [312, 313]})
m("acl-entry", [3, 112, 244, 245, 247, 394, 414, 425],
  {"subj-obj": [247, 414, 444], "deleg": [247, 425], "tag": [247, 425], "valid": [247, 425], "comment": []},
  all_fields=[245])
m("acl", [76, 113, 241, 244, 246, 247, 346, 438],
  {"version": [117, 401], "acl-entry": [244, 247]})
m("byte-string", [41, 42, 43, 45, 46, 78, 388, 393])
m("bytes", [36, 37, 42, 386])
m("cert-display", [120, 121, 122, 123, 402, 461], {"byte-string": [122, 123]})
m("cert", [4, 5, 83, 85, 86, 88, 89, 111, 392, 394, 424, 439],
  {"version": [116, 117, 118], "cert-display": [120, 121, 402], "issuer": [4, 12],
   "issuer-loc": [128], "subject": [4, 444], "subject-loc": [153], "deleg": [155],
   "tag": [5, 157, 158, 159, 160, 161], "valid": [166], "comment": [203, 402]})
m("comment", [203, 402], {"byte-string": [203]})
m("crl", [181, 182, 262, 267, 269, 270, 278, 347, 401, 409, 421],
  {"version": [117, 401], "crl-hash-list": [181, 182, 422], "valid-basic": [267, 269, 270, 421]})
m("crl-hash-list", [181, 182, 422], {"hash": [422]})
m("date", [172, 173, 174, 408])
m("ddigit")
m("decimal", [37, 386])
m("deleg5", [310, 424, 425])
m("deleg", [155, 247, 424, 425])
m("delta-crl", [271, 276, 277, 278, 280, 262, 267, 269, 270, 347, 401, 421, 423],
  {"version": [117, 401], "hash-of-crl": [276, 277, 423], "crl-hash-list": [422, 423],
   "valid-basic": [267, 269, 270, 421]})
m("display-type", [44, 45, 46, 388])
m("dsa-sig-val", [108], {"(r ...)": [108, 352], "(r ...)/r": [108, 352], "(r ...)/byte-string": [108, 352],
                         "(s ...)": [108, 352], "(s ...)/s": [108, 352], "(s ...)/byte-string": [108, 352]})
m("fq-name", [7, 8, 234, 415, 441],
  {"principal": [7, 8], "names": [7, 415]})
m("general-op", [253, 256, 455], {"byte-string": [253, 455], "s-part": [455]})
m("gte", [432])
m("hash-alg-name", [73, 74, 459])
m("hash-list", [])
m("hash-of-crl", [276, 277, 423])
m("hash-of-key", [126, 396, 418, 454, 459])
m("hash-op", [253, 257, 258, 260, 261, 418, 419],
  {"hash": [253, 257], "hash-alg-name": [257]})
m("hash-value", [100, 396])
m("hash", [9, 10, 11, 100, 396, 459],
  {"hash-alg-name": [73, 74, 459], "hash-value": [100, 396], "uris": [457]})
m("integer", [53, 55, 56, 57, 58, 389, 390])
m("issuer-loc", [128, 129, 457], {"uris": [128, 457]})
m("issuer-name", [205, 206, 210, 213, 214, 215, 415],
  {"(name ...)": [210, 212, 213, 214, 215], "(name ...)/name": [214], "(name ...)/principal": [213, 215],
   "(name ...)/byte-string": [208, 214]})
m("issuer5", [306, 307, 424, 425])
m("issuer", [4, 12, 126, 397, 418], {"principal": [12, 126, 418]})
m("k-val", [143, 144, 146, 403])
m("key5", [296, 297, 424])
m("keyholder-obj", [136, 141])
m("keyholder", [136, 141, 440, 456], {"keyholder-obj": [136, 141]})
m("low-lim", [329, 432], {"gte": [432], "byte-string": [329]})
m("lte", [432])
m("n-val", [143, 145, 403])
m("name-cert", [204, 205, 206, 207, 210, 216, 217, 218, 219, 221, 222, 223, 394, 412, 413, 415, 416, 439, 452],
  {"version": [116, 117, 118], "cert-display": [120, 121, 402], "issuer-name": [210, 213, 214, 215],
   "subject": [220, 224, 234], "valid": [166, 416], "comment": [203, 402]})
m("name", [13, 204, 208, 209, 224, 229, 233, 234, 235, 236, 238, 239, 240, 414, 415, 417, 441])
m("names", [235, 415], {"byte-string": [208]})
m("not-after", [170, 407], {"date": [172, 174, 408]})
m("not-before", [170, 407], {"date": [172, 174, 408]})
m("nzddigit")
m("obj-hash", [138, 456], {"hash": [138]})
m("one-valid", [184, 185, 187, 188, 200, 201, 265, 287, 290, 291, 292, 409], {"byte-string": [200, 201, 265, 290]})
m("online-test", [14, 15, 178, 179, 180, 189, 190, 191, 195, 409, 410, 411, 426, 457],
  {"online-type": [14], "uris": [190, 457], "principal": [179, 278, 286, 291, 409], "s-part": [191]})
m("online-type", [14])
m("op", [253, 256, 455])
m("principal", [8, 126, 418, 442, 454, 459])
m("pub-key", [91, 92, 93, 94, 396, 457],
  {"(<pub-sig-alg-id> ...)": [90, 91, 93, 94], "(<pub-sig-alg-id> ...)/pub-sig-alg-id": [73, 74, 93],
   "(<pub-sig-alg-id> ...)/s-expr": [91, 94, 98], "uris": [92, 457]})
m("pub-sig-alg-id", [73, 74, 93, 399])
m("range-ordering", [329, 432])
m("relative-name", [229, 230, 231, 232, 233, 414], {"names": [229, 232]})
m("reval-body", [185, 187, 281, 288, 292])
m("reval-hash-list", [283, 285, 422], {"hash": [283, 285, 422]})
m("reval", [183, 262, 267, 269, 270, 283, 284, 285, 286, 287, 291, 292, 347, 401, 409, 421],
  {"version": [117, 401], "reval-hash-list": [283, 285, 422], "reval-body": [288, 292, 421]})
m("s-expr", [17, 18, 19, 27, 28, 29, 30, 75, 445, 449], {"s-part": [450]})
m("s-part", [450])
m("seq-ent", [254, 256, 460])
m("sequence", [16, 102, 129, 253, 254, 255, 256, 264, 348, 418, 419, 420, 448, 455, 460], {"seq-ent": [254, 255, 264]})
m("sig-params", [106, 107, 108, 109, 398])
m("sig-val", [106, 398, 399], {"sig-params": [106, 109]})
m("signature", [102, 103, 259, 260, 397, 398, 420, 443],
  {"hash": [259, 397], "principal": [397, 443], "sig-val": [398, 399]})
m("simple-tag", [72, 75, 162, 163, 164, 165, 405, 430], {"tag-expr": [162, 163, 164, 405, 430]})
m("subj-hash", [287, 288])
m("subj-obj", [132, 134, 135, 136, 138, 141, 224, 414, 444, 456])
m("subj-thresh", [20, 21, 143, 144, 145, 146, 147, 148, 149, 150, 151, 332, 333, 334, 335, 403, 404, 435, 446, 451],
  {"k-val": [143, 144, 146, 403], "n-val": [143, 145, 403], "subj-obj": [143, 145, 403, 404]})
m("subject-loc", [153, 457], {"uris": [153, 457]})
m("subject5", [424, 425, 456])
m("subject", [4, 135, 444], {"subj-obj": [135, 444]})
m("tag-body5", [311, 317, 318, 319, 320, 321, 424, 425])
m("tag-expr", [158, 159, 322, 430])
m("tag-prefix", [331, 433, 458], {"prefix": [331, 458], "byte-string": [331, 433]})
m("tag-range", [329, 330, 432, 458],
  {"range": [329, 458], "range-ordering": [329, 432], "low-lim": [329, 432], "up-lim": [329, 432]})
m("tag-set", [323, 328, 431, 458], {"set": [328, 458], "tag-expr": [328, 431]})
m("tag-star", [156, 157, 326, 327, 458], {"(*)": [157, 458]})
m("tag-string", [325, 329, 331, 393])
m("tag", [1, 5, 72, 79, 157, 158, 159, 160, 161, 162, 163, 164, 165, 322, 324, 325, 326, 327, 405, 430, 434, 458])
m("up-lim", [329, 432], {"lte": [432], "byte-string": [329]})
m("uri", [73, 74, 457])
m("uris", [92, 190, 457], {"uri": [190, 457]})
m("valid-basic", [167, 170, 313, 406, 407, 408, 421], {"not-before": [170, 406, 407], "not-after": [170, 406, 407]})
m("valid5", [312, 313, 314, 315, 316, 424, 425, 427, 428])
m("valid", [14, 15, 23, 166, 178, 406, 426],
  {"valid-basic": [24, 167, 170, 406], "online-test": [25, 178, 426]})
m("version", [116, 117, 118, 400, 401], {"integer": [116, 400]})
m("canonical-form", [6, 34, 36, 37, 386, 38, 39, 40, 64, 71, 344, 387, 392, 449],
  {"length": [37, 386], "bytes": [41, 42, 43], "display-type": [44, 45], "white space": [71, 387]})
m("advanced-form", [32, 33, 61, 62, 65, 69, 70, 71, 387],
  {"token": [33, 62, 66], "quoted string": [67], "hex": [68, 70], "base64": [68, 70], "white space": [69]})
m("transport-form", [35, 63, 391], {"content": [63, 391], "line wrapping": [391]})
m("rsa-key-params", [91, 93, 390, 396], {"alg id": [93], "e": [390], "n": [390]})
m("rsa-private-key", [95, 96, 390, 395],
  {"e": [95, 390], "n": [95, 390], "d": [95], "p": [95], "q": [95], "a": [96, 395], "b": [96, 395], "c": [96, 395]})
m("dsa-key-params", [93, 97, 390],
  {"alg id": [93], "p": [390], "g": [390], "q": [390], "y": [390], "x": [97]})
m("ecdsa-key", [94, 98])
m("rsa-sig-params", [106, 107], {"sig-value": [107]})
m("dsa-sig-params", [106, 108, 352], {"r": [108], "s": [108]})
m("online-id", [411])
m("cancel-list", [181, 182, 422])
m("hash-of-pred", [276, 277, 423])
m("reval-list", [283, 285, 422])
m("tag-body", [72, 305])
m("threshold-subj", [301, 446])
m("fq-name5", [372])
m("result-certificate", [337, 338, 339, 340, 341, 342, 343, 436, 437])

# Requirements no message, field or encoding rule cites, and why. The script
# fails if this list and the computed one differ, so a change is noticed.
UNCITED = {
    "split_of parent whose children are cited": [84, 87, 268],
    "notation of the BNF itself, not a message": [31],
    "leaves a top-level object's parts to its designer": [80],
    "reduction or trust-engine process (protocol.yaml, state-machine.yaml)": [2, 114, 237, 293, 336],
    "online-test fetch process (protocol.yaml, state-machine.yaml)": [186, 192, 193, 194, 196, 197, 198, 199, 263, 266, 279],
}

ENC = {"ENC-01": [36, 37, 386], "ENC-02": [42, 43], "ENC-03": [45, 46, 388], "ENC-04": [56, 57, 389],
       "ENC-11": [58], "ENC-05": [18, 19, 28, 29, 30], "ENC-06": [81, 82, 83],
       "ENC-07": [38, 39, 40, 64], "ENC-08": [77, 78, 393], "ENC-09": [172, 174, 408], "ENC-10": [344]}

# ---------------------------------------------------------------------------
def lines(s):
    s = str(s).strip("'\"").lstrip("L"); a, _, b = s.partition("-"); return int(a), int((b or a).lstrip("L"))

def load():
    req = _yaml.parse((D / "requirements.yaml").read_text())
    R = [r for r in (req.get("requirements") or []) if isinstance(r, dict) and r.get("id")]
    byid = {int(r["id"].split("#R-")[1]): r for r in R}
    msgs = _yaml.parse(MSGFILE.read_text())
    return R, byid, msgs

def walk_fields(fs, prefix=""):
    for f in fs or []:
        p = prefix + f["name"]
        yield p, f
        yield from walk_fields(f.get("fields"), p + "/")

def productions(R):
    out = {}
    for r in R:
        mt = re.match(r"\s*<([^>]+)>::\s*(.*)", str(r["text"]), re.S)
        if mt:
            out.setdefault(mt.group(1), []).append((int(r["id"].split("#R-")[1]), mt.group(2)))
    return out

def has_token(tok, rhs):
    return bool(re.search(re.escape(tok) + r"(?![\w-])", rhs))

def build(R, byid, msgs):
    """-> {path: sorted list of ints}; path = 'msg' or 'msg/field/path' or 'ENC-nn'."""
    prod = productions(R)
    out = {}
    missing = []
    for x in msgs["messages"]:
        n = x["name"]
        pr = list(prod.get(n, []))
        if ALIAS.get(n):
            pr += prod.get(ALIAS[n], [])
        if n == "tag-star":
            pr += [p for p in prod.get("tag", []) if p[0] == 156]  # R-0156 inlines (tag (*))
        if n == "valid-basic":
            pr += [p for p in prod.get("valid", []) if p[0] == 167]  # R-0167 inlines <valid-basic>
        cur = C.get(n)
        if cur is None:
            missing.append(n); cur = {"msg": [], "fields": {}, "all_fields": []}
        out[n] = sorted(set([p[0] for p in pr]) | set(cur["msg"]))
        for path, f in walk_fields(x.get("fields")):
            ids = set(cur["fields"].get(path, [])) | set(cur["all_fields"])
            typ = str(f.get("type", ""))
            toks = {typ}
            if typ.startswith("<") and typ.endswith(">") and ALIAS.get(typ[1:-1]):
                toks.add("<" + ALIAS[typ[1:-1]] + ">")
            if typ.startswith("<"):
                for pid, rhs in pr:
                    if any(has_token(t, rhs) for t in toks):
                        ids.add(pid)
            if f.get("literal"):          # a literal byte string: the production that quotes it
                for pid, rhs in pr:
                    if '"%s"' % f["literal"] in rhs:
                        ids.add(pid)
            out[n + "/" + path] = sorted(ids)
    for e in msgs["encoding_rules"]:
        out[e["id"]] = sorted(ENC.get(e["id"], []))
    return out, missing

def propose(R, msgs):
    """layer 1: candidates by source_lines overlap and name, for a reader."""
    def mlines(x):
        o = []
        for k in ("bnf", "bnf_restated"):
            if isinstance(x.get(k), dict) and x[k].get("source_lines"): o.append(lines(x[k]["source_lines"]))
        for p in x.get("prose") or []: o.append(lines(p["source_lines"]))
        return o
    cand = {}
    for r in R:
        ls = []
        for k in ("source_lines", "repeated_in"):
            if r.get(k):
                for part in str(r[k]).split(","):
                    try: ls.append(lines(part.strip()))
                    except Exception: pass
        if r.get("basis"):
            for part in str(r["basis"]).split(","):
                try: ls.append(lines(part.strip()))
                except Exception: pass
        blob = " ".join(str(r.get(k, "")) for k in ("text", "object", "field")).lower()
        rid = int(r["id"].split("#R-")[1])
        for x in msgs["messages"]:
            names = {x["name"].lower(), str(x.get("object_name", "")).lower().strip("<>")} - {""}
            near = any(not (rb < a - 3 or ra > b + 3) for (a, b) in mlines(x) for (ra, rb) in ls)
            if near and any(re.search(r"(?<![\w-])" + re.escape(nm) + r"(?![\w-])", blob) for nm in names):
                cand.setdefault(x["name"], set()).add(rid)
    return cand

def report(R, byid, msgs, final, missing):
    nm = len(msgs["messages"]); nf = sum(1 for x in msgs["messages"] for _ in walk_fields(x.get("fields")))
    ne = len(msgs["encoding_rules"])
    print(f"examined: {len(R)} requirements, {nm} messages, {nf} fields, {ne} encoding rules")
    if missing: print("messages with no CURATED entry:", missing)
    bad = [(k, i) for k, v in final.items() for i in v if i not in byid]
    print("dangling curated ids:", bad)
    mw = sum(1 for x in msgs["messages"] if final[x["name"]])
    fw = sum(1 for x in msgs["messages"] for p, _ in walk_fields(x.get("fields")) if final[x["name"] + "/" + p])
    ew = sum(1 for e in msgs["encoding_rules"] if final[e["id"]])
    ids = {i for v in final.values() for i in v}
    pairs = sum(len(v) for v in final.values())
    print(f"wired: messages {mw}/{nm}, fields {fw}/{nf}, encoding rules {ew}/{ne}; {pairs} pairs; {len(ids)} distinct ids")
    unc = sorted(set(byid) - ids)
    assert unc == sorted(i for v in UNCITED.values() for i in v), ("UNCITED out of date", unc)
    print("cited by nothing:", len(unc), {k: v for k, v in UNCITED.items()})
    unw = [k for k, v in final.items() if not v]
    print("unwired:", unw)
    return dict(mw=mw, nm=nm, fw=fw, nf=nf, ew=ew, ne=ne, pairs=pairs, ids=len(ids), unwired=unw, uncited=len(unc))

def apply(final, msgs, stats):
    src = MSGFILE.read_text().split("\n")
    out, stack, section = [], {}, None
    n_done = 0
    skip = 0
    for ln in src:
        if re.match(r"^\s+- \"draft-ietf-spki-cert-structure#R-\d+\"\s*$", ln) and skip:
            continue                       # an old id list, replaced below
        skip = 0
        if re.match(r"^[a-z_]+:", ln):
            section = ln.split(":")[0]
        mt = re.match(r"^(\s*)- (?:name|id): \"(.*)\"\s*$", ln)
        if mt and section in ("messages", "encoding_rules"):
            ind = len(mt.group(1))
            for k in [k for k in stack if k >= ind]: del stack[k]
            stack[ind] = mt.group(2)
        mc = re.match(r"^(\s*)constrained_by:(?: \[\])?\s*$", ln)
        if mc and section in ("messages", "encoding_rules"):
            k = len(mc.group(1)) - 2
            chain = [stack[i] for i in sorted(stack) if i <= k]
            if section == "encoding_rules":
                key = chain[-1]
            else:
                key = chain[0] if len(chain) == 1 else chain[0] + "/" + "/".join(chain[1:])
            ids = final[key]
            n_done += 1
            skip = 1
            if ids:
                out.append(mc.group(1) + "constrained_by:")
                out += [mc.group(1) + '  - "' + PFX + "%04d" % i + '"' for i in ids]
            else:
                out.append(ln)
            continue
        out.append(ln)
    text = "\n".join(out)
    # coverage status
    new_status = ('constrained_by_status: "WIRED. %d of %d messages, %d of %d fields and %d of %d encoding rules carry at least one id: '
                  '%d pairs over %d distinct ids of the 461 in requirements.yaml. Unwired messages, fields or encoding rules: %s. '
                  '%d requirements are cited by no message, field or encoding rule, each for a reason recorded in UNCITED in schema/join_requirements.derived.py: '
                  'three split_of parents whose children are cited (R-0084, R-0087, R-0268), the BNF notation (R-0031), a clause leaving a top-level object to its designer (R-0080), '
                  'five reduction or trust-engine process rules and eleven online-test fetch rules, which belong to protocol.yaml and state-machine.yaml. '
                  'Pairs were proposed by schema/join_requirements.derived.py (production text rule, then a curated table) and each was read against its requirement.' % (
                      stats["mw"], stats["nm"], stats["fw"], stats["nf"], stats["ew"], stats["ne"], stats["pairs"], stats["ids"],
                      ("none" if not stats["unwired"] else ", ".join(stats["unwired"])), stats["uncited"]) + '"')
    text, c = re.subn(r"^  constrained_by_status: .*$", "  " + new_status, text, flags=re.M)
    assert c == 1, c
    MSGFILE.write_text(text)
    return n_done

def main():
    R, byid, msgs = load()
    final, missing = build(R, byid, msgs)
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "":
        cand = propose(R, msgs)
        print("PROPOSE: messages with candidate ids from lines+name overlap:", len(cand))
        wired = 0
        for k, v in sorted(cand.items()):
            extra = sorted(v - set(final[k]))
            wired += len(v) - len(extra)
            if extra:
                print(k, "candidates not wired:")
                for i in extra: print("    R-%04d" % i, " ".join(str(byid[i]["text"]).split())[:110])
        print("candidates wired:", wired)
    st = report(R, byid, msgs, final, missing)
    if mode == "--wire":
        for k, v in final.items():
            print(k, ["R-%04d" % i for i in v])
    if mode == "--apply":
        print("lines rewritten:", apply(final, msgs, st))

if __name__ == "__main__":
    main()

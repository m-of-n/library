#!/usr/bin/env python3
"""join_protocol.derived.py -- DERIVED, library-written (FX-1, draft-ietf-spki-cert-structure).

Not source text. Re-runs, against the files as they stand, the three things the protocol and
state-machine lane of pass 1 computed by script:

  1. `constrained_by` of every step and error path in protocol.yaml and of every transition in
     state-machine.yaml, joined from requirements.yaml as below;
  2. each file's `requirements_join` mapping: the method, what was examined, the result, and the
     account of the ids messages.yaml left to these two files;
  3. each file's `coverage` paragraph, and the same two paragraphs under `## Coverage` in
     protocol.md.

Usage:  python3 -I join_protocol.derived.py           # recompute and compare, change nothing; exit 1 on any difference
        python3 -I join_protocol.derived.py --pairs   # also print every resolved pair, for reading
        python3 -I join_protocol.derived.py --write   # rewrite 1-3 in place, then re-read and check nothing else moved

Every count printed is EXAMINED beside FOUND. The source text is not read: the quotations come from
the two files (bin/check-quotes verifies them against the source) and the requirement texts from
requirements.yaml. Run it after any edit to protocol.yaml, state-machine.yaml, requirements.yaml or
messages.yaml.

The join. A requirement R is cited by an item when:

  (a) QUOTE JOIN. For one of the item's quotations Q, R.source_lines and Q.source_lines overlap and
      the whitespace-collapsed text of one contains the other. Nine requirement texts cross a page
      and carry the draft's running header (requirements.yaml extraction_notes); the header is
      removed from R's text for this comparison only, because no quotation here crosses a page.
  (b) SPLIT PARENTS ARE REPLACED BY THEIR CHILDREN. A split_of parent that joins is replaced by
      those of its children that join to the same item (each child is a sub-span of the parent, so
      it joins exactly when the item quotes that part). A parent none of whose children joins is
      kept, and reported. Where the item relies on words of the parent that no joined child
      carries, the parent is added back by a selector (c) that says so.
  (c) SELECTORS. OVERRIDES, at the end of this file, adds a requirement no quotation of the item
      reaches (every inferred requirement, which has no source_lines; a stated rule the item
      applies but does not quote) or drops one the item quotes only for contrast, each with its
      reason. A selector is (section, text fragment) and must match exactly one requirement whose
      locator is that section, or the run fails; where a split child's whole text is the fragment,
      the requirement whose text IS the fragment is the match (a child's words always occur in its
      parent too).

No id written to a file is typed here: every one comes out of requirements.yaml. The comment on
each selector names the id its author expects. The run resolves every selector and fails if one
resolves elsewhere or two resolve to the same id, so an edited requirements.yaml cannot silently
retarget a selector; an id typed anywhere else in this file also fails the run.

Both repository YAML readers (bin/_yaml.py, bin/_record_yaml.py) read every input and must agree
once scalar typing is undone (_record_yaml types integers and true/false; bin/_yaml.py does not).
--write edits only the three things above, line by line in the layout pass 1 wrote; it then re-reads
every file with both readers and fails unless the computed values are on file and every other value
is unchanged. A date changes only where the text it dates changes.
"""
import collections
import datetime
import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / "bin" / "_yaml.py").is_file())
sys.path.insert(0, str(REPO / "bin"))
from _yaml import parse as read_strings  # noqa: E402
import _record_yaml  # noqa: E402

RID = "draft-ietf-spki-cert-structure"
SELF = pathlib.Path(__file__).name
PROTOCOL = HERE / "protocol.yaml"
MACHINES = HERE / "state-machine.yaml"
REQUIREMENTS = HERE / "requirements.yaml"
MESSAGES = HERE / "messages.yaml"
PROSE = HERE / "protocol.md"
MESSAGES_JOIN = HERE / "schema" / "join_requirements.derived.py"
FILES = {"protocol": PROTOCOL, "sm": MACHINES}
# The keys of the UNCITED table in MESSAGES_JOIN whose ids messages.yaml left to these two files.
MESSAGES_LEFT_KEYS = ("reduction or trust-engine process", "online-test fetch process")
# The draft's running header: page furniture inside nine requirement texts, not their words.
RUNNING_HEADER = "INTERNET-DRAFT Simple Public Key Certificate 26 July 1999"
WS = re.compile(r"\s+")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
TOP = re.compile(r"^[a-z_]+:")
SIMPLE_OK = re.compile(r'^[^"\\\n]*$')
WIDTH = 100
METHOD = (
    "(a) quote join: a requirement whose source_lines overlap one of the item's quotations and "
    "whose text contains it or is contained in it; (b) a split_of parent that joins is replaced by "
    "its children that join to the same item, and kept where none does; (c) selectors (section plus "
    "a text fragment that must match exactly one requirement) add inferred requirements and stated "
    "ones no quotation reaches, and drop a requirement an item quotes only for contrast. Every "
    "resolved pair was read against the item's own wording; every selector carries its reason in "
    "the script, which re-runs this join against the files as they stand.")


class Failure(Exception):
    pass


def fail(msg):
    raise Failure(msg)


# ------------------------------------------------------------------ reading
def flat(n, path="", out=None):
    """Every scalar by path, with _record_yaml's typing undone (true/false, integers, null)."""
    out = {} if out is None else out
    if isinstance(n, dict):
        for k, v in n.items():
            flat(v, f"{path}/{k}", out)
    elif isinstance(n, list):
        for i, v in enumerate(n):
            flat(v, f"{path}[{i}]", out)
    elif isinstance(n, bool):
        out[path] = "true" if n else "false"
    else:
        out[path] = "null" if n is None else str(n)
    return out


def read_both(path):
    """The file as bin/_yaml.py reads it (every scalar a string), once both readers agree."""
    a = read_strings(path.read_text(encoding="utf-8"))
    b = _record_yaml.load_yaml(path)
    fa, fb = flat(a), flat(b)
    if fa != fb:
        diff = sorted(k for k in set(fa) | set(fb) if fa.get(k) != fb.get(k))
        fail(f"{path.name} reads differently under bin/_yaml.py and bin/_record_yaml.py at "
             f"{len(diff)} paths, first {diff[:3]}")
    return a, fa


def norm(s):
    return WS.sub(" ", str(s)).strip()


def span(v):
    a, _, b = str(v).strip().strip("'\"").lstrip("L").partition("-")
    return int(a), int(b.lstrip("L") or a)


def num(rid):
    return int(rid.split("R-")[1])


def as_list(v):
    if v in (None, "", "[]"):
        return []
    if not isinstance(v, list):
        fail(f"expected a list, found {str(v)[:80]!r}")
    return v


class Requirements:
    def __init__(self):
        doc, leaves = read_both(REQUIREMENTS)
        self.leaves = len(leaves)
        self.rows = []
        for r in doc["requirements"]:
            rid = str(r["id"])
            if not rid.startswith(RID + "#R-"):
                fail(f"requirements.yaml: foreign id {rid}")
            sl = r.get("source_lines")
            a, b = span(sl) if sl else (None, None)
            text = norm(r.get("text", ""))
            self.rows.append({"id": rid, "short": rid.split("#")[1], "text": text,
                              "cmp": norm(text.replace(RUNNING_HEADER, " ")), "a": a, "b": b,
                              "locator": str(r.get("locator", "")), "kind": str(r.get("kind", "")),
                              "split_of": str(r.get("split_of") or "") or None})
        ids = [r["id"] for r in self.rows]
        if len(set(ids)) != len(ids):
            fail("requirements.yaml: duplicate id")
        self.by_id = {r["id"]: r for r in self.rows}
        self.children = collections.defaultdict(list)
        for r in self.rows:
            if r["split_of"]:
                if r["split_of"] not in self.by_id:
                    fail(f"requirements.yaml: {r['short']} is split_of an id it does not hold")
                self.children[r["split_of"]].append(r["id"])
        self.digest = hashlib.sha256(REQUIREMENTS.read_bytes()).hexdigest()
        self.n_inferred = sum(1 for r in self.rows if r["kind"] == "inferred")
        self.n_split = sum(1 for r in self.rows if r["split_of"])


def in_section(r, sec):
    loc = r["locator"]
    return loc == sec or loc.startswith(sec + " ") or loc.startswith(sec + ",")


def select(sel, reqs):
    sec, frag = sel
    frag = norm(frag)
    m = [r for r in reqs.rows if frag in r["cmp"] and in_section(r, sec)]
    if len(m) > 1:
        exact = [r for r in m if r["cmp"] == frag]
        if len(exact) == 1:
            m = exact
    if len(m) != 1:
        fail(f"selector {sel!r} matched {len(m)} requirements: {[r['short'] for r in m]}")
    return m[0]


SEL_LINE = re.compile(r"^    ([A-Z0-9_]+) = \(.*\)\s+# (R-\d{4})\s*$")
TYPED_ID = re.compile(r"\bR-\d{4}\b")


def check_selectors(reqs):
    """Every selector resolves to the id its comment expects, no two to the same id, and no id is
    typed anywhere else in this file. Returns how many selectors were examined."""
    expected, elsewhere = {}, []
    for i, ln in enumerate(pathlib.Path(__file__).read_text(encoding="utf-8").split("\n"), 1):
        m = SEL_LINE.match(ln)
        if m:
            expected[m.group(1)] = m.group(2)
        elif TYPED_ID.search(ln):
            elsewhere.append(i)
    if elsewhere:
        fail(f"{SELF}: a requirement id is typed outside a selector comment, line(s) {elsewhere}")
    names = [k for k in vars(S) if not k.startswith("_")]
    if set(names) != set(expected):
        fail(f"{SELF}: selectors and expected-id comments disagree: {sorted(set(names) ^ set(expected))}")
    seen = {}
    for name in names:
        got = select(getattr(S, name), reqs)["short"]
        if got != expected[name]:
            fail(f"selector S.{name} resolves to {got}; its comment expects {expected[name]}")
        if got in seen:
            fail(f"selectors S.{seen[got]} and S.{name} both resolve to {got}")
        seen[got] = name
    return len(names)


# --------------------------------------------------------------------- join
def items_of(doc, label):
    items, n = collections.OrderedDict(), 0
    if label == "protocol":
        for f in as_list(doc.get("flows")):
            for s in as_list(f.get("steps")):
                items[f"{f['id']} {s['n']}"] = s
                n += 1
        for e in as_list(doc.get("error_paths")):
            items[e["id"]] = e
            n += 1
    else:
        for m in as_list(doc.get("machines")):
            for t in as_list(m.get("transitions")):
                items[t["id"]] = t
                n += 1
    if len(items) != n:
        fail(f"{FILES[label].name}: two items share a key")
    return items


class Join:
    """One file's join: the computed constrained_by of every item, and what was examined."""

    def __init__(self, label, doc, reqs):
        self.label = label
        self.items = items_of(doc, label)
        self.examined = collections.Counter()
        self.kept_parents = []
        self.pairs = []
        self.computed = collections.OrderedDict(
            (key, self.wire(key, item, reqs)) for key, item in self.items.items())

    def wire(self, key, item, reqs):
        ex = self.examined
        joined = collections.OrderedDict()
        for q in as_list(item.get("quotes")):
            ex["quotes"] += 1
            qa, qb = span(q["source_lines"])
            qt = norm(q["quote"])
            for r in reqs.rows:
                if r["a"] is None or r["b"] < qa or r["a"] > qb:
                    continue
                if r["cmp"] in qt:
                    how = "full"
                elif qt in r["cmp"]:
                    how = "part"
                else:
                    continue
                ex["quote_hits"] += 1
                joined.setdefault(r["id"], (how, q))
        out = collections.OrderedDict()
        for rid, (how, q) in joined.items():
            if rid in reqs.children:
                if any(c in joined for c in reqs.children[rid]):
                    ex["parents_replaced"] += 1
                    continue
                out[rid] = (how, q, "parent kept: no child joins")
                self.kept_parents.append((key, reqs.by_id[rid]["short"], f"L{q['source_lines']}"))
                continue
            out[rid] = (how, q, "")
        ex["quote_join_links"] += len(out)
        for op, sel, reason in OVERRIDES.get(key, []):
            ex["selectors"] += 1
            r = select(sel, reqs)
            if op == "add":
                if r["id"] in out:
                    fail(f"{key}: a selector adds {r['short']}, which the quotation join already gives")
                out[r["id"]] = ("selector", None, reason)
                ex["selector_adds"] += 1
            elif op == "drop":
                if r["id"] not in out:
                    fail(f"{key}: a selector drops {r['short']}, which did not join")
                del out[r["id"]]
                ex["selector_drops"] += 1
                self.pairs.append((key, r["short"], "DROPPED", reason, r["text"]))
            else:
                fail(f"{key}: unknown override {op!r}")
        for rid, (how, q, why) in out.items():
            src = f"quote L{q['source_lines']}" if q else "selector"
            self.pairs.append((key, reqs.by_id[rid]["short"], f"{how} {src}", why, reqs.by_id[rid]["text"]))
        return sorted(out, key=num)

    def cited(self):
        return sorted({r for v in self.computed.values() for r in v}, key=num)

    def links(self):
        return sum(len(v) for v in self.computed.values())

    def unwired(self):
        return [k for k, v in self.computed.items() if not v]


def plural(n, one, many):
    return f"{n} {one if n == 1 else many}"


def join_mapping(j, reqs, ran):
    ex = j.examined
    what = "steps and error paths" if j.label == "protocol" else "transitions"
    cited = j.cited()
    kinds = collections.Counter(reqs.by_id[c]["kind"] for c in cited)
    n = len(reqs.rows)
    return collections.OrderedDict([
        ("ran", ran),
        ("script", "distilled/" + SELF),
        ("requirements_file", "distilled/requirements.yaml"),
        ("requirements_sha256", reqs.digest),
        ("requirements_seen", f"{n} ids: {n - reqs.n_inferred} stated ({reqs.n_split} of them "
                              f"split_of children) and {reqs.n_inferred} inferred"),
        ("method", METHOD),
        ("items", f"{len(j.items)} {what}"),
        ("examined", f"{ex['quotes']} quotations, {ex['quote_hits']} quotation hits, "
                     f"{ex['quote_join_links']} links from the quotation join after "
                     f"{plural(ex['parents_replaced'], 'parent replacement', 'parent replacements')}, "
                     f"{plural(len(j.kept_parents), 'parent', 'parents')} kept with no child joined, "
                     f"{plural(ex['selector_adds'], 'selector addition', 'selector additions')}, "
                     f"{plural(ex['selector_drops'], 'selector drop', 'selector drops')}"),
        ("result", f"{j.links()} constrained_by links to {len(cited)} distinct requirement ids "
                   f"({kinds.get('stated', 0)} stated, {kinds.get('inferred', 0)} inferred); "
                   f"{len(j.unwired())} {what} carry none"),
        ("parents_kept", [f"{k}: {r} ({ln})" for k, r, ln in j.kept_parents] or "none"),
        ("unwired", j.unwired() or "none"),
    ])


def messages_left():
    """The UNCITED table of schema/join_requirements.derived.py, and the ids it leaves to these
    two files (read from that file, not typed here)."""
    src = MESSAGES_JOIN.read_text(encoding="utf-8")
    body = src[src.index("UNCITED = {"):]
    body = body[:body.index("\n}") + 2]
    table = collections.OrderedDict()
    for k, v in re.findall(r'"([^"]+)":\s*\[([0-9,\s]+)\]', body):
        table[k] = [int(x) for x in v.replace(" ", "").split(",") if x.strip()]
    left = sorted(n for k, v in table.items() if k.startswith(MESSAGES_LEFT_KEYS) for n in v)
    return table, left


def messages_cited():
    """Every requirement id messages.yaml cites under a constrained_by key."""
    doc, leaves = read_both(MESSAGES)
    out = set()

    def walk(n, under):
        if isinstance(n, dict):
            for k, v in n.items():
                walk(v, under or k == "constrained_by")
        elif isinstance(n, list):
            for v in n:
                walk(v, under)
        elif under and isinstance(n, str) and n.startswith(RID + "#R-"):
            out.add(n)
    walk(doc, False)
    return out, len(leaves)


def cross(jp, js, reqs):
    """protocol.yaml's account of the ids messages.yaml left to this lane, and of those no one of
    messages.yaml, protocol.yaml or state-machine.yaml cites; and the ids left, for the other file."""
    table, left = messages_left()
    by_num = {num(r["id"]): r["id"] for r in reqs.rows}
    absent = [n for n in left if n not in by_num]
    if absent:
        fail(f"UNCITED in {MESSAGES_JOIN.name} names numbers requirements.yaml does not hold: {absent}")
    left_ids = [by_num[n] for n in left]
    cp, cs = set(jp.cited()), set(js.cited())
    cm, leaves = messages_cited()
    rows = []
    for rid in left_ids:
        where = [name for name, c in (("protocol.yaml", cp), ("state-machine.yaml", cs)) if rid in c]
        rows.append(f"{reqs.by_id[rid]['short']}: {', '.join(where) if where else 'NOT CITED'}")
    nobody = sorted((r["id"] for r in reqs.rows if r["id"] not in cm | cp | cs), key=num)
    reason = {by_num[n]: k for k, v in table.items() for n in v if n in by_num}
    return collections.OrderedDict([
        ("messages_left", f"{len(left_ids)} ids, read from UNCITED in "
                          "distilled/schema/join_requirements.derived.py under the keys "
                          + " and ".join(f"'{k}'" for k in MESSAGES_LEFT_KEYS)
                          + f"; {sum(1 for r in left_ids if r in cp | cs)} of them cited here or in "
                          "state-machine.yaml"),
        ("messages_left_cited_by", rows),
        ("messages_yaml_cites", f"{len(cm)} distinct ids under constrained_by keys, read from "
                                f"messages.yaml by script ({leaves} values, the same under both YAML "
                                "readers once scalar typing is undone)"),
        ("cited_by_none_of_the_three",
         [f"{reqs.by_id[r]['short']}: {reason.get(r, 'no reason recorded in UNCITED')}" for r in nobody]
         or "none"),
    ]), left_ids, leaves


# ----------------------------------------------------------------- coverage
def count_quotes(n):
    if isinstance(n, dict):
        return int("quote" in n and "source_lines" in n) + sum(count_quotes(v) for v in n.values())
    if isinstance(n, list):
        return sum(count_quotes(v) for v in n)
    return 0


def counted(name, date):
    return f"Counted by {SELF} from {name} as written, {date}; any later edit owes a re-run."


COUNTED = re.compile(r"Counted by \S+ from \S+ as written, (\d{4}-\d{2}-\d{2}); any later edit "
                     r"owes a re-run\.$")


def coverage_protocol(doc, j, n_reqs, date):
    flows = as_list(doc["flows"])
    steps = [s for f in flows for s in as_list(f["steps"])]
    errors = as_list(doc["error_paths"])
    kinds = collections.Counter(f["kind"] for f in flows)
    inferred = sum(1 for s in steps if s["kind"] == "inferred")
    basis = collections.Counter(s["on_error_basis"] for s in steps)
    none = sum(1 for s in steps if s["message"] == "none")
    defects = as_list(doc["source_defects_and_tensions"])
    dk = collections.Counter(d["kind"] for d in defects)
    return " ".join([
        f"{len(as_list(doc['roles']))} roles. {len(flows)} flows ("
        + ", ".join(f"{v} {k}" for k, v in sorted(kinds.items())) + f") with {len(steps)} steps, "
        f"{inferred} of them inferred and {none} with message none; on_error_basis "
        + ", ".join(f"{k} {v}" for k, v in sorted(basis.items())) + ".",
        f"{len(as_list(doc['message_names_used']))} draft object names used. {len(errors)} error "
        f"paths. {len(defects)} source defects and gaps ("
        + ", ".join(f"{v} {k}" for k, v in sorted(dk.items())) + f"). "
        f"{len(as_list(doc['not_defined']))} not_defined items. {count_quotes(doc)} quote items, all "
        "cut by script.",
        f"constrained_by: {j.links()} links from {len(steps)} steps and {len(errors)} error paths to "
        f"{len(j.cited())} distinct requirement ids, of {n_reqs} in requirements.yaml when the join "
        f"ran; {len(j.unwired())} items carry none.",
        counted(PROTOCOL.name, date),
    ])


def coverage_sm(doc, j, n_reqs, date):
    machines = as_list(doc["machines"])
    tot_s = tot_t = tot_i = 0
    per = []
    for m in machines:
        ts = as_list(m["transitions"])
        n_i = sum(1 for t in ts if t["kind"] == "inferred")
        n_s = len(as_list(m["states"]))
        tot_s, tot_t, tot_i = tot_s + n_s, tot_t + len(ts), tot_i + n_i
        per.append(f"{m['id']} {n_s} states, {len(ts)} transitions, {n_i} inferred")
    triggers = as_list(doc["triggers_used"])
    ev = sum(1 for t in triggers if t["kind"] == "event")
    return " ".join([
        f"{len(machines)} machines, {tot_s} states, {tot_t} transitions, {tot_i} inferred. "
        + "; ".join(per) + ".",
        f"{len(triggers)} triggers ({len(triggers) - ev} draft objects, {ev} events). "
        f"{count_quotes(doc)} quote items, all cut by script.",
        f"constrained_by: {j.links()} links from {tot_t} transitions to {len(j.cited())} distinct "
        f"requirement ids, of {n_reqs} in requirements.yaml when the join ran; {len(j.unwired())} "
        "transitions carry none.",
        counted(MACHINES.name, date),
    ])


# ------------------------------------------------------------------ compute
def file_date(value, pattern=None):
    """The date a file already carries, or None."""
    s = norm(value or "")
    if pattern is not None:
        m = pattern.search(s)
        return m.group(1) if m else None
    return s if DATE.fullmatch(s) else None


def compute(today, settle):
    """Everything the three outputs should be. With settle, a text whose content (dates aside)
    differs from the file is dated today; otherwise every date is the file's own."""
    reqs = Requirements()
    n_sel = check_selectors(reqs)
    docs = {label: read_both(path) for label, path in FILES.items()}
    joins = {label: Join(label, docs[label][0], reqs) for label in FILES}
    unknown = [k for k in OVERRIDES if not any(k in j.items for j in joins.values())]
    if unknown:
        fail(f"overrides name items neither file holds: {unknown}")
    extra, left_ids, m_leaves = cross(joins["protocol"], joins["sm"], reqs)
    js = joins["sm"]
    sm_left = (f"{sum(1 for r in js.cited() if r in left_ids)} of the {len(left_ids)} ids "
               "messages.yaml left to this lane are cited here; protocol.yaml requirements_join "
               "gives the account across both files")

    def mapping(label, ran):
        m = join_mapping(joins[label], reqs, ran)
        if label == "protocol":
            m.update(extra)
        else:
            m["messages_left"] = sm_left
        return m

    def cover(label, date):
        f = coverage_protocol if label == "protocol" else coverage_sm
        return f(docs[label][0], joins[label], len(reqs.rows), date)

    want = {}
    for label in FILES:
        doc = docs[label][0]
        on_map = doc.get("requirements_join")
        ran = file_date(on_map.get("ran") if isinstance(on_map, dict) else None) or today
        m = mapping(label, ran)
        if settle and plain(m, "ran") != plain(on_map, "ran"):
            m = mapping(label, today)
        date = file_date(doc.get("coverage"), COUNTED) or today
        c = cover(label, date)
        if settle and c != norm(doc.get("coverage", "")):
            c = cover(label, today)
        if "<" in c:
            fail(f"{FILES[label].name}: coverage carries <...>, which protocol.md would backtick")
        want[label] = {"map": m, "coverage": c}
    return {"reqs": reqs, "n_sel": n_sel, "docs": docs, "joins": joins, "want": want,
            "messages_leaves": m_leaves}


def plain(m, drop):
    """A requirements_join mapping as comparable data, one key left out."""
    if not isinstance(m, dict):
        return m
    return [(k, norm(v) if isinstance(v, str) else v) for k, v in m.items() if k != drop]


# -------------------------------------------------------------------- check
def short(rids):
    return ", ".join(r.split("#")[1] for r in rids) or "nothing"


def clip(v, n=160):
    s = str(v)
    return s if len(s) <= n else s[:n] + " ..."


def where(a, b, before=40, after=120):
    """Both texts from just before the first character where they differ."""
    a, b = str(a), str(b)
    i = next((k for k, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
    lo = max(0, i - before)
    cut = lambda s: ("..." if lo else "") + s[lo:i + after] + ("..." if len(s) > i + after else "")
    return f"at character {i}: on file {cut(a)!r}; computed {cut(b)!r}"


def prose_paragraphs(text):
    lines = text.split("\n")
    at = [i for i, ln in enumerate(lines) if ln == "## Coverage"]
    if len(at) != 1:
        fail(f"{PROSE.name}: expected one '## Coverage' heading, found {len(at)}")
    tail = lines[at[0] + 1:]
    if any(ln.startswith("## ") for ln in tail):
        fail(f"{PROSE.name}: '## Coverage' is not the last section")
    return lines, at[0], [ln for ln in tail if ln.strip()]


def check(state, show_pairs, quiet=False):
    reqs, docs, joins, want = state["reqs"], state["docs"], state["joins"], state["want"]
    diffs = []
    say = (lambda *a: None) if quiet else print
    say(f"{SELF}: {RID}")
    say(f"readers: requirements.yaml {reqs.leaves} values, protocol.yaml {len(docs['protocol'][1])}, "
          f"state-machine.yaml {len(docs['sm'][1])}, messages.yaml {state['messages_leaves']}; each the same "
          "under bin/_yaml.py and "
          "bin/_record_yaml.py")
    say(f"requirements: {len(reqs.rows)} ids examined ({len(reqs.rows) - reqs.n_inferred} stated, "
          f"{reqs.n_split} of them split_of children; {reqs.n_inferred} inferred), sha256 {reqs.digest}")
    n_ov = sum(len(v) for v in OVERRIDES.values())
    n_add = sum(1 for v in OVERRIDES.values() for o in v if o[0] == "add")
    say(f"selectors: {state['n_sel']} examined, all resolve to the id their comment expects, none "
          f"shared; overrides: {n_ov} examined on {len(OVERRIDES)} items ({n_add} add, "
          f"{n_ov - n_add} drop), none for an item neither file holds")
    for label, path in FILES.items():
        j, doc = joins[label], docs[label][0]
        differ = []
        on_links = 0
        for key, item in j.items.items():
            on = [str(x) for x in as_list(item.get("constrained_by"))]
            on_links += len(on)
            if on != j.computed[key]:
                differ.append(key)
                diffs.append(f"{path.name} {key}: constrained_by on file only {short(sorted(set(on) - set(j.computed[key]), key=num))}; "
                             f"computed only {short(sorted(set(j.computed[key]) - set(on), key=num))}"
                             + ("; same ids, other order" if set(on) == set(j.computed[key]) else ""))
        ex = j.examined
        kind = ("steps and error paths" if label == "protocol" else "transitions")
        say(f"{path.name}: {len(j.items)} {kind} examined, {ex['quotes']} quotations, "
              f"{ex['quote_hits']} quotation hits, {ex['selectors']} selector overrides; computed "
              f"{j.links()} links to {len(j.cited())} ids, found on file {on_links} links; "
              f"{len(differ)} items differ")
        on_map = doc.get("requirements_join")
        m = want[label]["map"]
        n_keys = 0
        if not isinstance(on_map, dict):
            diffs.append(f"{path.name} requirements_join: not a mapping on file")
        else:
            for k in list(m) + [k for k in on_map if k not in m]:
                n_keys += 1
                a, b = on_map.get(k, "(absent)"), m.get(k, "(absent)")
                if isinstance(b, str) and isinstance(a, str):
                    a = norm(a)
                if a != b:
                    diffs.append(f"{path.name} requirements_join.{k}: " + (where(a, b) if isinstance(a, str) and isinstance(b, str)
                                                                    else f"on file {clip(a)!r}; computed {clip(b)!r}"))
            if [k for k in on_map] != [k for k in m] and set(on_map) == set(m):
                diffs.append(f"{path.name} requirements_join: keys in another order")
        on_cov = norm(doc.get("coverage", ""))
        if on_cov != want[label]["coverage"]:
            diffs.append(f"{path.name} coverage " + where(on_cov, want[label]["coverage"]))
        say(f"{path.name}: requirements_join {n_keys} keys examined, coverage 1 paragraph examined")
    _, _, paras = prose_paragraphs(PROSE.read_text(encoding="utf-8"))
    expect = [want["protocol"]["coverage"], want["sm"]["coverage"]]
    if paras != expect:
        for i, (a, b) in enumerate(zip(paras + [""] * 2, expect)):
            if a != b:
                diffs.append(f"{PROSE.name} Coverage paragraph {i + 1} " + where(a, b))
        if len(paras) != 2:
            diffs.append(f"{PROSE.name} Coverage: {len(paras)} paragraphs on file, 2 expected")
    say(f"{PROSE.name}: Coverage {len(paras)} paragraphs examined")
    if show_pairs:
        for label in FILES:
            say(f"--- pairs, {FILES[label].name} (item | id | how | reason | requirement text)")
            for p in joins[label].pairs:
                say(" | ".join(p))
    say(f"differences: {len(diffs)}")
    for d in diffs:
        say("  " + d)
    return diffs


# -------------------------------------------------------------------- write
def emit_list(key, values, indent):
    if not values:
        return [f"{indent}{key}: []"]
    for v in values:
        if not SIMPLE_OK.match(v):
            fail(f"list value needs a mapping: {v[:60]!r}")
    return [f"{indent}{key}:"] + [f'{indent}  - "{v}"' for v in values]


def wrap(text, indent):
    out = []
    paras = text.split("\n")
    for k, p in enumerate(paras):
        line = ""
        for w in p.split():
            if line and len(indent) + len(line) + 1 + len(w) > WIDTH:
                out.append(indent + line)
                line = w
            else:
                line = (line + " " + w) if line else w
        if line:
            out.append(indent + line)
        if k != len(paras) - 1:
            out.append("")
    return out


def emit_scalar(key, v, indent):
    v = str(v).strip()
    if v == "":
        return [f'{indent}{key}: ""']
    if len(v) <= 88 and SIMPLE_OK.match(v):
        return [f'{indent}{key}: "{v}"']
    return [f"{indent}{key}: >-"] + wrap(v, indent + "  ")


def emit_mapping(key, m):
    out = [f"{key}:"]
    for k, v in m.items():
        out += emit_list(k, v, "  ") if isinstance(v, list) else emit_scalar(k, v, "  ")
    return out


ITEM_INDENT = {"flows": 8, "error_paths": 4, "machines": 8}


def rewrite_constrained_by(lines, label, computed):
    """Replace each item's constrained_by list, finding items by the layout pass 1 wrote."""
    out, i, section, flow, key, done = [], 0, None, None, None, set()
    while i < len(lines):
        ln = lines[i]
        if TOP.match(ln):
            section, key = ln.split(":")[0], None
        elif label == "protocol" and section == "flows":
            m_f = re.match(r'^  - id: "(F-\d+)"$', ln)
            m_s = re.match(r'^      - n: "([^"]+)"$', ln)
            if m_f:
                flow, key = m_f.group(1), None
            elif m_s:
                key = f"{flow} {m_s.group(1)}"
            elif re.match(r"^ {0,6}- ", ln):
                key = None
        elif label == "protocol" and section == "error_paths":
            m_e = re.match(r'^  - id: "(E-\d+)"$', ln)
            if m_e:
                key = m_e.group(1)
            elif re.match(r"^ {0,2}- ", ln):
                key = None
        elif label == "sm" and section == "machines":
            m_t = re.match(r'^      - id: "(SM-\d+-T\d+)"$', ln)
            if m_t:
                key = m_t.group(1)
            elif re.match(r"^ {0,6}- ", ln):
                key = None
        ind = " " * ITEM_INDENT.get(section, -1) if section in ITEM_INDENT else None
        if key is not None and ind is not None and ln in (ind + "constrained_by:", ind + "constrained_by: []"):
            if key in done or key not in computed:
                fail(f"{FILES[label].name} line {i + 1}: constrained_by of {key} found twice or for no item")
            entry = re.compile("^" + ind + r'  - "[^"]*"$')
            j = i + 1
            while j < len(lines) and entry.match(lines[j]):
                j += 1
            out += emit_list("constrained_by", computed[key], ind)
            done.add(key)
            i = j
            continue
        out.append(ln)
        i += 1
    missing = [k for k in computed if k not in done]
    if missing:
        fail(f"{FILES[label].name}: no constrained_by line found for {missing[:5]}")
    return out


def replace_top(lines, key, block):
    at = [i for i, ln in enumerate(lines) if ln == f"{key}:" or ln.startswith(f"{key}: ")]
    if len(at) != 1:
        fail(f"expected one top-level {key}, found {len(at)}")
    s = at[0]
    e = next((i for i in range(s + 1, len(lines)) if TOP.match(lines[i])), len(lines))
    return lines[:s] + block + lines[e:]


def write(state):
    changed = []
    for label, path in FILES.items():
        text = path.read_text(encoding="utf-8")
        lines = text.split("\n")
        if lines[-1] != "":
            fail(f"{path.name}: no final newline")
        body = rewrite_constrained_by(lines[:-1], label, state["joins"][label].computed)
        body = replace_top(body, "requirements_join", emit_mapping("requirements_join", state["want"][label]["map"]))
        body = replace_top(body, "coverage", emit_scalar("coverage", state["want"][label]["coverage"], ""))
        new = "\n".join(body) + "\n"
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed.append(path.name)
    text = PROSE.read_text(encoding="utf-8")
    lines, at, _ = prose_paragraphs(text)
    new = "\n".join(lines[:at + 1] + ["", state["want"]["protocol"]["coverage"], "",
                                      state["want"]["sm"]["coverage"], ""])
    if new != text:
        PROSE.write_text(new, encoding="utf-8")
        changed.append(PROSE.name)
    return changed


TARGET = re.compile(r"^(/requirements_join(/|\[|$)|/coverage$|/(flows|error_paths|machines)\[\d+\]"
                    r"(/(steps|transitions)\[\d+\])?/constrained_by\[\d+\]$)")


def unmoved(before, after):
    """Paths outside the three outputs whose value differs between two readings."""
    return sorted(k for k in set(before) | set(after)
                  if not TARGET.match(k) and before.get(k) != after.get(k))


# --------------------------------------------------------------------- main
def main(argv):
    flags = set(argv)
    if flags - {"--write", "--pairs"}:
        print(next(p for p in __doc__.split("\n\n") if p.startswith("Usage:")))
        return 2
    today = datetime.date.today().isoformat()
    try:
        if "--write" in flags:
            before = compute(today, settle=True)
            pending = check(before, False, quiet=True)
            print(f"before --write: {len(pending)} differences")
            for d in pending:
                print("  " + d)
            prose_before = prose_paragraphs(PROSE.read_text(encoding="utf-8"))
            changed = write(before)
            print(f"write: {', '.join(changed) or 'nothing'} changed")
            after = compute(today, settle=False)
            for label in FILES:
                moved = unmoved(before["docs"][label][1], after["docs"][label][1])
                if moved:
                    fail(f"{FILES[label].name}: --write moved {len(moved)} values it does not own, "
                         f"first {moved[:3]}")
            prose_after = prose_paragraphs(PROSE.read_text(encoding="utf-8"))
            if prose_after[0][:prose_after[1]] != prose_before[0][:prose_before[1]]:
                fail(f"{PROSE.name}: --write changed text above the Coverage section")
            diffs = check(after, "--pairs" in flags)
        else:
            diffs = check(compute(today, settle=False), "--pairs" in flags)
    except Failure as e:
        print(f"FAIL: {e}")
        return 1
    return 1 if diffs else 0


# ====================================================================== tables
# The selectors and the overrides were written after reading every resolved pair of the quotation
# join and the list of parent words no joined child carries (pass 1, 2026-11-11). Run with --pairs
# to read them again.

class S:
    """(section, text fragment). The comment is the id the author expects: a check, never the
    source; the id written to a file is the one the selector resolves to."""
    # ---- inferred requirements (no source_lines; reached only by selector)
    CANON_NO_PREFIX = ("§3.1", "A canonical-form parser rejects a length prefix")  # R-0386
    CANON_NO_WS = ("§3.1", "Canonical form carries no white space")  # R-0387
    BYTES_EQUAL = ("§3.2", "Two byte strings are equal only when")  # R-0388
    TRANSPORT_B64 = ("§3.4", "The {...} transport form is base64 of one complete canonical encoding")  # R-0391
    HASH_AS_RECEIVED = ("§3.5", "Hash and verify the canonical bytes as received")  # R-0392
    BYTEWISE = ("§3.8", "Every comparison is bytewise and case-sensitive")  # R-0393
    FIELDS_BY_NAME = ("§3.8", "Because <cert> fields may come in any order, a parser identifies each")  # R-0394
    KEY_HASH = ("§3.8.2", "The hash of a key is the hash of the canonical encoding")  # R-0396
    SIG_FIRST = ("§3.8.3", "A verifier admits a <cert> into reduction only after checking its <signature>")  # R-0397
    SIGNED_BYTES_UNSPEC = ("§3.8.3", "The bytes <sig-val> is computed over are never specified")  # R-0398
    SIG_ALG_MISMATCH = ("§3.8.3.1", "A verifier rejects a <signature> whose <sig-val> algorithm id differs")  # R-0399
    VERSION0_FORMS = ("§4.1", "Version 0 can be written in ways the draft does not reconcile")  # R-0400
    VERSION_CERTS_ONLY = ("§4.1", "The rule that an unrecognised version is ignored names certificates only")  # R-0401
    DISPLAY_NO_EFFECT = ("§4.2", "<cert-display> and <comment> do not affect reduction")  # R-0402
    K_PATHS_SUBJECTS = ("§4.5.3", "K distinct paths is read as K different listed subjects")  # R-0404
    TAG_APPEND_NARROWS = ("§4.8", "By §4.8, appending fields to a tag list narrows it")  # R-0405
    VALID_ORDER = ("§4.9", "Inside (valid ...), which is not one of the two order-free exceptions")  # R-0406
    VALID_AT_T = ("§4.9", "A validity range holds at time t when not-before")  # R-0407
    DATE_ORDER = ("§4.9.1", "Byte-string comparison orders dates correctly only when")  # R-0408
    ONLINE_REPLY_SIG = ("§4.9.2", "For each online test the verifier checks the reply's signature")  # R-0409
    NEWCERT_NO_PRINCIPAL = ("§4.9.2", "A new-cert test names no <principal>")  # R-0410
    ONLINE_ID_UNSPEC = ("§4.9.2", "The draft never says what the <online-id> byte string identifies")  # R-0411
    NAMECERT_FEEDS = ("§5.1", "A name certificate feeds name reduction")  # R-0412
    NAME_SEVERAL = ("§5.1", "Where several valid name certificates define one name")  # R-0413
    RELNAME_ISSUER = ("§5.2", "A relative name can only be completed with a certificate issuer's principal")  # R-0414
    NAME_REDUCE_STEP = ("§5.3", "Name reduction step: a fully qualified name")  # R-0415
    NAMECERT_VALID_AT_USE = ("§5.3", "A name certificate used in a reduction is valid at the time of use")  # R-0416
    NAME_TERMINATES = ("§5.3", "A name reducer terminates on the §5.3 trouble-making certificate")  # R-0417
    HASH_OF_KEY_RESOLVE = ("§6.2", "A <hash-of-key> principal is resolved by finding a key")  # R-0418
    DO_HASH_RECENT = ("§6.2", "A (do hash ...) op hashes the most recent object")  # R-0419
    SIG_HASH_BEFORE = ("§6.2", "Because a <signature> calls for the hash of the item before it")  # R-0420
    VALID_BASIC_EMPTY = ("§7", "<valid-basic> may be empty")  # R-0421
    CRL_HASHES_IDENTIFY = ("§7.1", "The hashes in (canceled ...) and (valid ...) identify certificates")  # R-0422
    DELTA_COMBINE_UNSPEC = ("§7.1", "How a delta-CRL combines with its predecessor is not stated")  # R-0423
    CERT_TO_5TUPLE = ("§8.1", "Translating a verified <cert> into a 5-tuple")  # R-0424
    ACL_TO_5TUPLE = ("§8.1", "Translating an <acl-entry>")  # R-0425
    ALL_ONLINE_SUCCEED = ("§8.2", "Every online test in a <valid> has to succeed")  # R-0426
    NOW_INTERSECT = ("§8.2", "now intersected with a date range is now when")  # R-0427
    NULL_VALIDITY = ("§8.2", "A reduction whose validity intersection is null yields nothing usable")  # R-0428
    ORDER_FREE = ("§8.2", "Reduction gives the same result whichever order")  # R-0429
    TAG_FIELD_RULES56 = ("§8.3", "Rules 5 and 6 speak of a <tag> field")  # R-0430
    SET_INTERSECT = ("§8.3", "A (* set ...) intersected with another tag yields")  # R-0431
    RANGE_ORDERINGS = ("§8.3", "The orderings of (* range ...)")  # R-0432
    PREFIX_TEST = ("§8.3", "A (* prefix ...) test, like a (* range ...) test")  # R-0433
    NO_STAR_INTERSECT = ("§8.3", "An implementation that does not intersect two *-forms")  # R-0434
    K_CONVERGE = ("§8.4", "When K reductions converge on one subject")  # R-0435
    CRC_VALIDITY = ("§8.7", "A certificate result certificate's validity is the reduced V")  # R-0436
    CRC_ISSUER = ("§8.7", "A certificate result certificate is issued under the verifier's own key")  # R-0437
    REQUEST_UNCHECKED = ("§8", "The draft never says how the prover's request is checked")  # R-0453
    PRINCIPAL_EQUAL = ("§8.2", "In s1 = i2 two principals are equal")  # R-0454
    GENERAL_OP_UNDEF = ("§6.2", "<general-op> is a production with no defined operation")  # R-0455
    CHAIN_END = ("§8.2", "A 5-tuple whose subject is an <obj-hash> or a <keyholder> ends a chain")  # R-0456
    URIS_ANY = ("§4.4", "Every <uris> (in a public key, issuer-info, subject-info or an online test)")  # R-0457
    STAR_LIST = ("§4.8", "In canonical form every *-form is a list")  # R-0458
    HASH_ALG_UNIMPL = ("§3.8.2", "A verifier that does not implement the algorithm a <hash> names")  # R-0459
    # ---- stated requirements no quotation of the item reaches
    ABS_TAG_UNDEFINED = ("Abstract", "The authorization field carried by SPKI certificates and ACLs is left to be defined")  # R-0001
    HASH_ANYWHERE = ("§2", "In general, the hash of an object can be used wherever the object can appear.")  # R-0010
    HASH_NAMES = ("§2", "The hash serves as a name for the object from which it was computed.")  # R-0011
    GLOSS_NAME = ("§2", "NAME: a SDSI name always relative to the definer of some name space.")  # R-0013
    GLOSS_ONLINE = ("§2", "ONLINE TEST: one of three forms of validity test")  # R-0014
    GLOSS_VALIDITY = ("§2", "a date range that must include the current date and time")  # R-0024
    BNF_BYTESTRING = ("§3.2", '<byte-string>:: <bytes> | <display-type> <bytes> ;')  # R-0047
    BNF_BYTES = ("§3.2", '<bytes>:: <decimal> ":"')  # R-0048
    BNF_DECIMAL = ("§3.2", "<decimal>:: <nzddigit> <ddigit>*")  # R-0049
    BNF_DISPLAY_TYPE = ("§3.2", '<display-type>:: "[" <bytes> "]" ;')  # R-0052
    BNF_SEXPR = ("§3.3", '<s-expr>:: "(" <byte-string> <s-part>* ")" ;')  # R-0059
    ADV_TOKENS = ("§3.4", "the advanced form follows familiar token recognition rules, not permitting tokens to start with digits, terminating them with white space or punctuation marks.")  # R-0062
    ADV_NO_LENGTH = ("§3.6", "individual byte strings may be expressed without length fields (if they are what most languages consider text tokens)")  # R-0066
    ADV_QUOTED = ("§3.6", "may be written as quoted strings (under normal C string rules)")  # R-0067
    ADV_HEX_B64 = ("§3.6", "may be individually hex or base64 encoded.")  # R-0068
    EXAMPLES_KEYWORDS = ("§3.6", "In these examples, we will use keywords without preceding length fields")  # R-0070
    TAG_USER_DEFINED = ("§3.7", "<tag> objects are user-defined")  # R-0072
    ORDER_EXCEPTIONS = ("§3.8", "Exceptions to this are found in the top level <cert> and <acl> constructs.")  # R-0083
    ONLY_ALGS = ("§3.8.1", "The only pub-sig-alg-id's we have defined at this point are for")  # R-0093
    OTHER_KEY_TYPES = ("§3.8.1", "Other key types are open to being defined by application developers.")  # R-0094
    CAPTURE_CHOICES = ("§3.8.1.3", "All of these choices need to be captured and expressed in the public key definition.")  # R-0098
    BNF_SIGNATURE = ("§3.8.3", '<signature>:: "(" "signature" <hash> <principal> <sig-val> ")" ;')  # R-0101
    BNF_SIGVAL = ("§3.8.3.1", '<sig-val>:: "(" <pub-sig-alg-id> <sig-params> ")" ;')  # R-0104
    BNF_SIGPARAMS = ("§3.8.3.1", "<sig-params>:: <byte-string> | <s-expr>+ ;")  # R-0105
    BNF_CERT = ("§4", '<cert>:: "(" "cert" <version>?')  # R-0110
    BNF_VERSION = ("§4.1", '<version>:: "(" "version" <integer> ")" ;')  # R-0115
    BNF_DISPLAY = ("§4.2", '<cert-display>:: "(" "display" <byte-string> ")" ;')  # R-0119
    DISPLAY_DEV = ("§4.2", "This field is up to developers to define as they see fit.")  # R-0122
    BNF_ISSUER = ("§4.3", '<issuer>:: "(" "issuer" <principal> ")" ;')  # R-0124
    BNF_ISSUER_LOC = ("§4.4", '<issuer-loc>:: "(" "issuer-info" <uris> ")" ;')  # R-0127
    BNF_SUBJECT = ("§4.5", '<subject>:: "(" "subject" <subj-obj> ")" ;')  # R-0130
    BNF_SUBJOBJ = ("§4.5", "<subj-obj>:: <principal> | <name> | <obj-hash> | <keyholder> | <subj-thresh> ;")  # R-0131
    BNF_SUBJOBJ_BASIC = ("§4.5", "<subj-obj>:: <principal> ;")  # R-0133
    KEYHOLDER_SPECIAL = ("§4.5", "The <keyholder> case is special and of little interest to verifier code")  # R-0136
    BNF_OBJHASH = ("§4.5.1", '<obj-hash>:: "(" "object-hash" <hash> ")" ;')  # R-0137
    BNF_KEYHOLDER = ("§4.5.2", '<keyholder>:: "(" "keyholder" <keyholder-obj> ")" ;')  # R-0139
    KEYHOLDER_FLESH = ("§4.5.2", "This form of subject refers to the flesh and blood")  # R-0141
    THRESH_INTRO = ("§4.5.3", "A threshold subject, introduced by Tatu Ylonen")  # R-0146
    THRESH_INTENT = ("§4.5.3", "The actual intent is to insure that there are K distinct paths")  # R-0147
    BNF_SUBJECT_LOC = ("§4.6", '<subject-loc>:: "(" "subject-info" <uris> ")" ;')  # R-0152
    SUBJECT_LOC_OPT = ("§4.6", "This optional field provides the location of information about the subject.")  # R-0153
    BNF_DELEG = ("§4.7", '<deleg>:: "(" "propagate" ")" ;')  # R-0154
    BNF_TAG = ("§4.8", '<tag>:: "(" "tag" "(*)" ")"')  # R-0156
    TAG_STAR_SET = ("§4.8", "A tag with *-forms represents a set of specific permissions.")  # R-0159
    TAG_ADD_RESTRICTS = ("§4.8", "if one adds a field to the end of a tag definition, one is restricting the permission granted.")  # R-0164
    BNF_VALID = ("§4.9", '<valid>:: "(" "valid" <not-before>? <not-after>? <online-test>* ")" ;')  # R-0167
    BNF_NOT_AFTER = ("§4.9", '<not-after>:: "(" "not-after" <date> ")" ;')  # R-0168
    BNF_NOT_BEFORE = ("§4.9", '<not-before>:: "(" "not-before" <date> ")" ;')  # R-0169
    BNF_DATE = ("§4.9.1", "<date>:: <byte-string> ;")  # R-0171
    DATE_INTERNAL = ("§4.9.1", "For internal use, it is treated as a normal byte string.")  # R-0173
    BNF_ONLINE_TEST = ("§4.9.2", '<online-test>:: "(" "online" <online-type>')  # R-0175
    BNF_ONLINE_TYPE = ("§4.9.2", '<online-type>:: "crl" | "reval" | "one-time" ;')  # R-0176
    BNF_ONLINE_ID = ("§4.9.2", '<online-id>:: "(" "id" <byte-string> ")" ;')  # R-0177
    ONLINE_REPLY_VALIDATED = ("§4.9.2", "The reply from an online test is a digitally signed object")  # R-0179
    ONETIME_NO_DATES = ("§4.9.2", "The one-time form is a re-validate form without validity dates.")  # R-0185
    ONETIME_VERIFIER_FETCH = ("§4.9.2", "It must be fetched by the verifier, rather than the prover, since it is valid only for the current verification step.")  # R-0186
    NEWCERT_FORM = ("§4.9.2", "The new-cert form requests a new copy of the certificate in question.")  # R-0189
    PROTO_NOT_SPEC = ("§4.9.3", "The protocol used for these online tests is not fully specified here.")  # R-0192
    PASSIVE_PAGES = ("§4.9.3", "One can use passive web pages")  # R-0193
    WORKS_BUT_ONETIME = ("§4.9.3", "This works for everything but one-time revalidations.")  # R-0194
    OTHER_SERVERS = ("§4.9.3", "If there are other servers and protocols defined")  # R-0196
    ONETIME_FETCH_CONTRAST = ("§4.9.3", "The fetch of a one-time test result must be done by the verifying code, while all other tests fetches")  # R-0197
    TRANSACTION_DATA = ("§4.9.3", "but it will probably also include transaction data")  # R-0200
    BNF_COMMENT = ("§4.10", '<comment>:: "(" "comment" <byte-string> ")" ;')  # R-0202
    NAME_ARBITRARY = ("§5", "A name can be an arbitrary byte string assigned by the issuer")  # R-0208
    NAME_NOT_CONFORM = ("§5", "A name is not required or expected necessarily to conform")  # R-0209
    NAMECERT_FORM = ("§5.1", "A name certificate has the form:")  # R-0210
    BNF_NAMECERT = ("§5.1", '<name-cert>:: "(" "cert" <version>?')  # R-0211
    NAMECERT_GROUPS = ("§5.1", "More specifically, all name certificates define groups")  # R-0222
    BNF_RELNAME = ("§5.2", '<relative-name>:: "(" "name" <names> ")" ;')  # R-0226
    BNF_FQNAME = ("§5.2", '<fq-name>:: "(" "name" <principal> <names> ")" ;')  # R-0227
    NAME_DEF_GIVEN = ("§5.3", "Given the name definition")  # R-0235
    TROUBLE_CERT = ("§5.3", "It is possible for someone to generate a trouble-making name certificate")  # R-0238
    ACL_PRIVATE = ("§6", "ACLs are private to one developer or application.")  # R-0241
    ACL_FIELDS = ("§6.1", "Since the fields of the ACL are fields of a <cert>")  # R-0245
    BNF_GENERAL_OP = ("§6.2", '<general-op>:: "(" "do" <byte-string> <s-part>* ")" ;')  # R-0252
    SIG_DOUBLE_DUTY = ("§6.2", "At this time, we assume that <signature> does double duty")  # R-0259
    S7_NO_PROTOCOLS = ("§7", "This section does not give details of protocols")  # R-0263
    S7_DIRECT_OR_PROVER = ("§7", "Whether the verifier contacts the revalidation center directly or via the prover")  # R-0266
    CRL_GROWS = ("§7.1", "If one wants to provide CRLs, and that CRL grows")  # R-0271
    REVAL_SIGNED = ("§7.2", "The <reval> must be signed by the principal indicated")  # R-0286
    ONETIME_VERIFIER_MUST = ("§7.3", "For one-time revalidation, the verifier itself must fetch")  # R-0287
    BNF_ONE_VALID = ("§7.3", '<one-valid>:: "(" "one-time" <byte-string> ")" ;')  # R-0289
    TUPLE_REP_DEV = ("§8.1", "How a 5-tuple is represented and stored is up to the developer.")  # R-0298
    RANGE_RULE5 = ("§8.3", "(* range ...): if some <tag> field compares a (* range")  # R-0329
    TUPLE_DOC_ONLY = ("§9.1", "<5-tuple>: an object defined for documentation purposes only.")  # R-0345
    CANON_HASHED = ("§3.5", "The canonical S-expression is the form which is hashed for both generating and verifying signatures.")  # R-0064
    BNF_SEQ_ENT = ("§9.2", "<seq-ent>:: <cert> | <name-cert>")  # R-0369
    BNF_SUBJ_HASH = ("§9.2", '<subj-hash>:: "(" "cert" <hash> ")" ;')  # R-0371
    GLOSS_KEYHOLDER = ("§2", "KEYHOLDER: the person or other entity that owns and controls a given private key.")  # R-0440
    LOCAL_NAME = ("§2", "This is sometimes also referred to as a local name.")  # R-0441


OVERRIDES = collections.OrderedDict()   # item key -> [(op, selector, reason)]


def add(keys, *sels, why):
    """The items in keys (comma-separated) obey each selected requirement."""
    for k in keys.split(","):
        for s in sels:
            OVERRIDES.setdefault(k.strip(), []).append(("add", s, why))


def drop(key, s, why):
    """The item quotes the selected requirement for contrast, not as a rule it obeys."""
    OVERRIDES.setdefault(key, []).append(("drop", s, why))


# ------------------------------------------------------------------ drops
drop("F-10 4", S.ONLINE_REPLY_VALIDATED,
     "the step quotes the rule that a reply is validated by the test's <principal> to show it "
     "cannot apply: a new-cert test names no principal (the inferred new-cert rule is carried instead)")

# ------------------------------------------------- split parents added back
add("F-06 2, F-08 2", S.PASSIVE_PAGES,
    why="the step's choice of a passive web page or CGI fetch is the parent sentence's opening "
        "words, which no split child carries")
add("F-09 2, SM-05-T02", S.TRANSACTION_DATA,
    why="the request carries transaction data, words of the parent no split child carries")
add("F-14 3", S.GLOSS_ONLINE,
    why="the step relies on the glossary's three forms of online test, which only the parent holds")
add("F-17 6, SM-07-T09, E-26", S.TROUBLE_CERT,
    why="the trouble-making certificate itself is the parent's subject; the children carry only "
        "its consequences")
add("F-19 5", S.RANGE_RULE5,
    why="rule 5's opening condition (a range compared with a byte string) is the parent's words")
add("SM-07-T03", S.NAME_DEF_GIVEN,
    why="the rewrite applies the parent's given definition, which no child carries")
add("E-16", S.ONETIME_FETCH_CONTRAST,
    why="the error rests on the whole sentence's contrast: one-time fetches by the verifier, "
        "all other fetches by either party")

# ------------------------------------------------------------- F-01..F-05
add("F-01 5", S.REQUEST_UNCHECKED,
    why="the decision checks the request, which the draft never says how to check")
add("F-02 1", S.CANON_NO_WS, S.BNF_BYTESTRING, S.BNF_BYTES, S.BNF_DECIMAL, S.BNF_DISPLAY_TYPE, S.BNF_SEXPR,
    why="canonical serialisation: length-prefixed byte strings, bracketed display types, "
        "parenthesised lists, no white space")
add("F-02 2", S.TRANSPORT_B64,
    why="the brace transport form is base64 of one canonical encoding")
add("F-02 3", S.TRANSPORT_B64, S.CANON_NO_PREFIX, S.CANON_NO_WS,
    why="decoding braces recovers canonical bytes, which a canonical parser checks as canonical")
add("F-02 4", S.HASH_AS_RECEIVED,
    why="the received bytes are kept because hashing and verifying use them as received")
add("F-02 5", S.CANON_NO_WS, S.ADV_TOKENS, S.ADV_NO_LENGTH, S.ADV_QUOTED, S.ADV_HEX_B64, S.EXAMPLES_KEYWORDS,
    why="the advanced form's token, quoted, hex and base64 rules, converted to canonical form")
add("F-03 1", S.BNF_ISSUER, why="the issuer field's production")
add("F-03 2", S.BNF_SUBJECT, S.BNF_SUBJOBJ, S.BNF_SUBJOBJ_BASIC,
    why="the subject field's productions, full and principal-only")
add("F-03 3", S.BNF_DELEG, S.BNF_TAG, S.TAG_STAR_SET, S.ABS_TAG_UNDEFINED, S.TAG_USER_DEFINED,
    why="writing <tag> and (propagate): their productions, the *-form set reading, and the tag "
        "left to its designer")
add("F-03 4", S.BNF_VALID, S.BNF_NOT_AFTER, S.BNF_NOT_BEFORE, S.BNF_ONLINE_TEST, S.BNF_ONLINE_TYPE,
    S.BNF_ONLINE_ID, why="the validity field's productions, dates and online tests")
add("F-03 5", S.BNF_VERSION, S.BNF_DISPLAY, S.DISPLAY_DEV, S.BNF_ISSUER_LOC, S.BNF_SUBJECT_LOC, S.BNF_COMMENT,
    why="the optional fields' productions")
add("F-03 6", S.BNF_CERT, S.ORDER_EXCEPTIONS,
    why="the <cert> production and its order-free fields")
add("F-03 7", S.BNF_SIGVAL, S.BNF_SIGPARAMS, S.SIGNED_BYTES_UNSPEC,
    why="the signature value's productions; the bytes signed are not specified")
add("F-03 9", S.BNF_KEYHOLDER, S.KEYHOLDER_FLESH,
    why="the keyholder subject's production and what it refers to")
add("F-04 1", S.NAME_ARBITRARY, S.NAME_NOT_CONFORM, S.GLOSS_NAME,
    why="choosing a local name: any byte string, no conformance, relative to the definer")
add("F-04 2", S.BNF_NAMECERT, S.NAMECERT_FORM, why="the name certificate's form and production")
add("F-04 4", S.NAMECERT_GROUPS, why="several certificates for one name define a group")
add("F-04 5", S.CANON_HASHED, S.BNF_SIGNATURE,
    why="signing hashes the canonical form and yields a <signature>")
add("F-04 6", S.SUBJECT_LOC_OPT, why="publication where subject-info points")
add("F-05 4", S.URIS_ANY, why="the fetch follows whatever <uris> names")
add("F-05 5", S.SIG_HASH_BEFORE, S.SIG_DOUBLE_DUTY,
    why="each signature follows the body it signs and hashes the item before it")
add("F-05 6", S.ORDER_FREE, why="reduction is order-free, so no chain order is required")

# ------------------------------------------------------------- F-06..F-11
add("F-06 1, F-08 1", S.BNF_ONLINE_ID, S.ONLINE_ID_UNSPEC,
    why="reading the test's <online-id>, whose meaning the draft never gives")
add("F-09 1", S.BNF_ONLINE_TEST, S.BNF_ONLINE_ID, S.ONLINE_ID_UNSPEC,
    why="reading the one-time test; its <online-id> is unexplained")
add("F-06 2, F-08 2", S.PROTO_NOT_SPEC, S.S7_NO_PROTOCOLS,
    why="the fetch protocol is not specified (§4.9.3, §7)")
add("F-06 5, F-07 5, F-08 5", S.ONLINE_REPLY_SIG,
    why="the reply's signature is checked against the test's principal")
add("F-06 6, F-08 6", S.ONLINE_REPLY_SIG, S.VALID_BASIC_EMPTY,
    why="currency is checked on a signed reply whose <valid-basic> may be empty")
add("F-06 7", S.ONLINE_REPLY_SIG, S.CRL_HASHES_IDENTIFY, S.HASH_ALG_UNIMPL,
    why="membership in (canceled ...) compares certificate hashes, under an algorithm the "
        "verifier must implement")
add("F-07 3", S.S7_NO_PROTOCOLS, why="fetching predecessors uses no specified protocol")
add("F-07 6", S.DELTA_COMBINE_UNSPEC, why="how a delta combines with its predecessor is not stated")
add("F-07 7", S.DELTA_COMBINE_UNSPEC, S.ONLINE_REPLY_SIG,
    why="checking the combined list rests on the unstated combination and on the signed reply")
add("F-08 7", S.ONLINE_REPLY_SIG, S.CRL_HASHES_IDENTIFY,
    why="membership in (valid ...) compares certificate hashes from a signed reply")
add("F-09 2", S.PROTO_NOT_SPEC, S.S7_NO_PROTOCOLS, S.WORKS_BUT_ONETIME, S.ONETIME_VERIFIER_FETCH,
    S.ONETIME_VERIFIER_MUST,
    why="the verifier's own fetch of a one-time result, by an unspecified protocol for which "
        "passive pages do not work")
add("F-09 3", S.BNF_SUBJ_HASH, why="the one-time reply names the certificate by (cert <hash>)")
add("F-09 4", S.ONLINE_REPLY_SIG, S.CRL_HASHES_IDENTIFY,
    why="checking the signer and the certificate hash of the one-time reply")
add("F-09 5, F-09 6", S.NOW_INTERSECT, why="the one-time result is `now`, intersected by rule")
add("F-10 2", S.PROTO_NOT_SPEC, why="the new-cert fetch protocol is not specified")
add("F-10 3", S.NEWCERT_FORM, S.NEWCERT_NO_PRINCIPAL,
    why="the responder returns a new copy; the test names no principal to sign a reply")
add("F-10 4", S.NEWCERT_NO_PRINCIPAL, S.SIG_FIRST,
    why="the copy is checked as any certificate, by its own issuer's signature, since the test "
        "names no principal")
add("F-11 4", S.CRL_GROWS, why="the choice of deltas when a CRL grows")
add("F-11 5", S.ONETIME_NO_DATES, S.BNF_ONE_VALID,
    why="a one-time reply carries no dates and echoes the nonce in <one-valid>")

# ------------------------------------------------------------- F-12..F-16
add("F-12 2, F-12 3", S.DO_HASH_RECENT, why="the held item is what a hash opcode hashes")
add("F-12 4", S.SIG_HASH_BEFORE, why="a signature hashes the item before it")
add("F-12 5", S.GENERAL_OP_UNDEF, why="no operation other than hash is defined")
add("F-12 6", S.HASH_OF_KEY_RESOLVE, S.KEY_HASH, S.HASH_ANYWHERE, S.HASH_NAMES,
    why="references by hash resolve from the index; a hash stands for its object")
add("F-13 1", S.HASH_AS_RECEIVED, S.DISPLAY_NO_EFFECT,
    why="the bytes as received are hashed, display and comment included")
add("F-13 2", S.SIG_FIRST, S.SIG_HASH_BEFORE, S.HASH_ALG_UNIMPL,
    why="the hash over the item before the signature is checked first, under a named algorithm")
add("F-13 3", S.HASH_OF_KEY_RESOLVE, S.KEY_HASH, why="resolving the signer's key from its hash")
add("F-13 4", S.SIG_ALG_MISMATCH, S.SIGNED_BYTES_UNSPEC, S.ONLY_ALGS,
    why="verifying the value under the key's algorithm, RSA and DSA being the only ones defined")
add("F-13 5", S.SIG_FIRST, why="a certificate is admitted only on its issuer's signature")
add("F-14 1", S.VALID_ORDER, S.BNF_NOT_AFTER, S.BNF_NOT_BEFORE,
    why="reading the bounds of (valid ...), in their fixed order")
add("F-14 2", S.DATE_INTERNAL, S.BNF_DATE, S.VALID_AT_T, S.DATE_ORDER,
    why="comparing the present with the bounds as byte strings")
add("F-14 3", S.ALL_ONLINE_SUCCEED, S.ONLINE_REPLY_SIG,
    why="every online test must succeed on a checked reply")
add("F-14 4, F-14 5", S.ALL_ONLINE_SUCCEED, why="validity holds only when every test succeeds")
add("F-14 6", S.CERT_TO_5TUPLE, why="the result becomes valid5")
add("F-15 1", S.VERSION0_FORMS, S.VERSION_CERTS_ONLY,
    why="version recognition: version 0's two spellings, and certificates only")
add("F-15 2", S.DISPLAY_NO_EFFECT, why="display and comment do not affect reduction")
add("F-15 3", S.CERT_TO_5TUPLE, S.TUPLE_REP_DEV, S.TUPLE_DOC_ONLY,
    why="forming a 5-tuple, whose representation is the developer's")
add("F-15 4", S.ACL_TO_5TUPLE, why="an ACL entry's 5-tuple")
add("F-15 5", S.NAMECERT_FEEDS, why="a name certificate feeds name reduction as a 4-tuple")
add("F-15 8", S.CHAIN_END, why="a keyholder subject ends a chain")
add("F-16 1", S.RELNAME_ISSUER, S.ACL_FIELDS,
    why="ACL entry fields are <cert> fields; a relative name has no issuer to complete it (E-34)")
add("F-16 2, F-16 4", S.ACL_TO_5TUPLE, why="an ACL entry becomes a 5-tuple issued by `self`")
add("F-16 3", S.ACL_PRIVATE, why="the ACL is private to its application")

# ------------------------------------------------------------- F-17..F-22
add("F-17 1", S.BNF_RELNAME, S.BNF_FQNAME, S.LOCAL_NAME,
    why="relative and fully qualified names' productions")
add("F-17 2, F-17 3, F-17 4", S.NAME_REDUCE_STEP, why="one name-reduction step")
add("F-17 5", S.NAME_SEVERAL, S.NAMECERT_GROUPS, why="several definitions make a group")
add("F-17 6", S.NAME_TERMINATES, why="a reducer must terminate on the trouble-making certificate")
add("F-17 7", S.NAMECERT_VALID_AT_USE, why="a name certificate must be valid when used")
add("F-18 1", S.PRINCIPAL_EQUAL, S.ORDER_FREE, S.CHAIN_END,
    why="linking s1 = i2 by principal equality, in any order, until a chain ends")
add("F-18 4", S.ALL_ONLINE_SUCCEED, S.NOW_INTERSECT, S.NULL_VALIDITY,
    why="intersecting validities: tests united, `now` against a range, null yields nothing")
add("F-18 7", S.ORDER_FREE, why="an equivalent algorithm gives the same result")
add("F-19 1", S.STAR_LIST, why="the (*) form is a list in canonical form")
add("F-19 2", S.BYTES_EQUAL, S.BYTEWISE, why="tag equality is bytewise, display types included")
add("F-19 3", S.TAG_APPEND_NARROWS, S.TAG_ADD_RESTRICTS,
    why="a field added to a tag narrows it, here to nothing")
add("F-19 4", S.SET_INTERSECT, why="the result of intersecting a set")
add("F-19 5", S.RANGE_ORDERINGS, why="the range orderings")
add("F-19 6", S.PREFIX_TEST, why="the prefix test's result")
add("F-19 7", S.TAG_FIELD_RULES56, why="fields matched by position")
add("F-19 8", S.NO_STAR_INTERSECT, why="two *-forms are not intersected")
add("F-20 1", S.THRESH_INTRO, why="the threshold subject")
add("F-20 3", S.K_PATHS_SUBJECTS, S.THRESH_INTENT, why="K distinct paths, converging")
add("F-20 5", S.K_CONVERGE, why="the merged tuple's fields")
add("F-21 2", S.CRC_VALIDITY, why="the result certificate's validity")
add("F-21 5", S.CRC_ISSUER, why="the result certificate is under the verifier's own key")
add("F-22 1", S.BNF_OBJHASH, why="the object-hash subject's production")
add("F-22 3", S.CHAIN_END, why="an object-hash subject ends the chain")
add("F-22 4", S.KEYHOLDER_SPECIAL, S.KEYHOLDER_FLESH, S.CHAIN_END, S.GLOSS_KEYHOLDER,
    why="keyholder statements are for people and end a chain")

# ------------------------------------------------------------ error paths
add("E-01", S.VERSION_CERTS_ONLY, why="the ignore rule names certificates only")
add("E-02", S.VERSION0_FORMS, why="version 0's unreconciled spellings")
add("E-03", S.SIG_HASH_BEFORE, S.SIG_FIRST, why="the hash must be over the item before the signature")
add("E-04, E-05", S.SIG_FIRST, why="a certificate is admitted only after its signature checks")
add("E-06", S.HASH_ALG_UNIMPL, S.SIG_FIRST, S.OTHER_KEY_TYPES, S.CAPTURE_CHOICES,
    why="an algorithm the verifier lacks or the draft leaves to developers")
add("E-07", S.HASH_OF_KEY_RESOLVE, why="a hash of a key must resolve to a key")
add("E-09", S.ALL_ONLINE_SUCCEED, why="every online test must succeed")
add("E-12, E-15", S.ONLINE_REPLY_SIG, why="the reply's signer and content are checked")
add("E-14", S.DELTA_COMBINE_UNSPEC, why="the delta's combination with its predecessor")
add("E-19", S.PRINCIPAL_EQUAL, why="s1 = i2 is principal equality")
add("E-21", S.NO_STAR_INTERSECT, why="uncovered *-form cases")
add("E-22", S.NULL_VALIDITY, why="a null validity yields nothing usable")
add("E-23", S.REQUEST_UNCHECKED, why="the decision on the request")
add("E-26", S.NAME_TERMINATES, why="a reducer must terminate")
add("E-25", S.NAME_REDUCE_STEP,
    why="the reduction step needs a name certificate defining (P n1); without one it does not apply")
add("E-27", S.GENERAL_OP_UNDEF, why="no operation other than hash is defined")
add("E-29", S.FIELDS_BY_NAME, why="fields are identified by name, so a repeat is detectable")
add("E-30", S.RANGE_ORDERINGS, why="the range orderings and display types")
add("E-33", S.CANON_NO_PREFIX, S.CANON_NO_WS, why="a canonical parser refuses non-canonical input")
add("E-34", S.RELNAME_ISSUER, why="a relative name needs an issuer's principal")

# --------------------------------------------------------- state machines
add("SM-01-T02", S.BNF_SEQ_ENT, S.DO_HASH_RECENT, why="a sequence entry becomes the held item")
add("SM-01-T03, SM-01-T04, SM-01-T06", S.DO_HASH_RECENT, why="the held item is what is hashed")
add("SM-01-T05", S.SIG_HASH_BEFORE, why="a signature hashes the held item")
add("SM-01-T08", S.GENERAL_OP_UNDEF, why="no operation other than hash is defined")
add("SM-01-T09", S.GENERAL_OP_UNDEF, S.BNF_GENERAL_OP, why="the <general-op> production has no operation")
add("SM-02-T01", S.HASH_AS_RECEIVED, S.DISPLAY_NO_EFFECT, why="hashing the bytes as received")
add("SM-02-T02, SM-02-T03", S.SIG_FIRST, S.SIG_HASH_BEFORE, why="the hash comparison")
add("SM-02-T04", S.HASH_OF_KEY_RESOLVE, S.KEY_HASH, why="resolving the key")
add("SM-02-T05", S.HASH_OF_KEY_RESOLVE, why="a hash that resolves to no key")
add("SM-02-T06", S.SIG_FIRST, S.HASH_ALG_UNIMPL, S.ONLY_ALGS,
    why="an algorithm the verifier lacks or the draft does not define")
add("SM-02-T07", S.SIG_FIRST, S.SIG_ALG_MISMATCH, S.SIGNED_BYTES_UNSPEC, why="verifying the value")
add("SM-02-T08, SM-02-T09, SM-02-T10", S.SIG_FIRST, why="admission only on the issuer's signature")
add("SM-03-T01", S.VERSION_CERTS_ONLY, S.VERSION0_FORMS, why="version recognition")
add("SM-03-T02", S.VERSION0_FORMS, why="an absent version is version 0")
add("SM-03-T03, SM-03-T04", S.SIG_FIRST, why="admission only after the signature checks")
add("SM-03-T05, SM-03-T06", S.VALID_AT_T, S.DATE_ORDER, why="the date comparison")
add("SM-03-T08", S.NEWCERT_NO_PRINCIPAL, why="the new copy is checked as a certificate")
add("SM-03-T11, SM-03-T12, SM-03-T13", S.ALL_ONLINE_SUCCEED, why="every test must succeed")
add("SM-03-T14", S.CERT_TO_5TUPLE, S.DISPLAY_NO_EFFECT, why="forming the tuple without display")
add("SM-04-T02", S.ALL_ONLINE_SUCCEED, why="a missing reply fails the test")
add("SM-04-T03", S.ONLINE_REPLY_SIG, why="the reply's signer")
add("SM-04-T04", S.ONLINE_REPLY_SIG, S.REVAL_SIGNED, why="a reply signed by another principal")
add("SM-04-T05, SM-04-T06", S.ONLINE_REPLY_SIG, S.VALID_BASIC_EMPTY, why="the reply's interval")
add("SM-04-T07, SM-04-T08, SM-04-T11", S.DELTA_COMBINE_UNSPEC, why="combining a delta")
add("SM-04-T09, SM-04-T13", S.ONLINE_REPLY_SIG, S.CRL_HASHES_IDENTIFY, why="list membership by hash")
add("SM-04-T10", S.ONLINE_REPLY_SIG, S.CRL_HASHES_IDENTIFY, S.HASH_ALG_UNIMPL,
    why="absence from the list, by hash")
add("SM-04-T12", S.DELTA_COMBINE_UNSPEC, S.HASH_ALG_UNIMPL, why="absence from the combined list")
add("SM-04-T14", S.ONLINE_REPLY_SIG, why="a reval that does not list it")
add("SM-05-T02", S.OTHER_SERVERS, S.S7_DIRECT_OR_PROVER, S.PROTO_NOT_SPEC,
    why="the request goes by whatever server and protocol is defined, directly or via the prover")
add("SM-05-T03", S.BNF_ONE_VALID, S.BNF_SUBJ_HASH, why="the one-time reply's form")
add("SM-05-T04", S.ALL_ONLINE_SUCCEED, why="a missing reply fails the test")
add("SM-05-T05, SM-05-T06, SM-05-T08", S.ONLINE_REPLY_SIG, why="checking the reply")
add("SM-05-T07", S.ONLINE_REPLY_SIG, S.CRL_HASHES_IDENTIFY, why="the certificate hash")
add("SM-05-T09", S.NOW_INTERSECT, why="`now` lasts one verification step")
add("SM-07-T03", S.NAME_REDUCE_STEP, why="one name-reduction step")
add("SM-07-T04, SM-07-T05", S.NAME_SEVERAL, why="several definitions make a group")
add("SM-07-T07, SM-07-T08", S.NAME_REDUCE_STEP, why="the step repeats until a principal")
add("SM-07-T06", S.NAME_REDUCE_STEP,
    why="the reduction step needs a name certificate defining (P n1); without one it does not apply")
add("SM-07-T09", S.NAME_TERMINATES, why="a reducer must terminate")
add("SM-08-T01, SM-08-T02", S.PRINCIPAL_EQUAL, why="s1 = i2 is principal equality")
add("SM-08-T08, SM-08-T09", S.NULL_VALIDITY, why="a null validity yields nothing usable")
add("SM-09-T02", S.ORDER_FREE, why="order-free reduction")
add("SM-09-T04, SM-09-T05", S.REQUEST_UNCHECKED, why="the decision on the request")
add("SM-10-T01, SM-10-T02", S.STAR_LIST, why="the (*) form")
add("SM-10-T03", S.BYTES_EQUAL, S.BYTEWISE, why="bytewise equality")
add("SM-10-T04", S.TAG_APPEND_NARROWS, S.TAG_ADD_RESTRICTS, why="differing tags")
add("SM-10-T05, SM-10-T06, SM-10-T07", S.SET_INTERSECT, why="set intersection")
add("SM-10-T08, SM-10-T09, SM-10-T10", S.RANGE_ORDERINGS, why="the range orderings")
add("SM-10-T11, SM-10-T12", S.PREFIX_TEST, why="the prefix test")
add("SM-10-T13", S.TAG_FIELD_RULES56, why="fields by position")
add("SM-10-T14", S.NO_STAR_INTERSECT, why="two *-forms meet")
add("SM-11-T01", S.VALID_AT_T, why="date-range intersection")
add("SM-11-T02, SM-11-T07", S.NULL_VALIDITY, why="a null validity")
add("SM-11-T03", S.ALL_ONLINE_SUCCEED, why="online tests united")
add("SM-11-T04, SM-11-T05", S.NOW_INTERSECT, why="`now` against a range")
add("SM-12-T03", S.K_PATHS_SUBJECTS, S.THRESH_INTENT, why="K distinct paths")
add("SM-12-T04", S.K_CONVERGE, why="the merged tuple")
add("SM-13-T01", S.ACL_TO_5TUPLE, why="an ACL entry's validity default")
add("SM-14-T01, SM-14-T07", S.CRC_VALIDITY, why="the result certificate's validity")
add("SM-14-T04", S.CRC_ISSUER, why="the verifier's own key")
add("SM-15-T04", S.GLOSS_VALIDITY, why="the validity date range")
add("SM-15-T05", S.NEWCERT_NO_PRINCIPAL, why="the new copy carries its own signature")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

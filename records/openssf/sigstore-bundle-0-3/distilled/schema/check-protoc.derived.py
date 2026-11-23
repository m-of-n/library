#!/usr/bin/env python3
# DERIVED - not verbatim. Written by this library, not part of the Sigstore protobuf-specs.
#
# Compiles the four *.verbatim.proto files with protoc and dumps what protoc says about them
# (messages, fields, numbers, json_name, labels, oneofs, google.api.field_behavior, enums,
# reserved ranges, and the source line of each declaration) to protoc-descriptor.derived.json,
# which build-schema.derived.py and build-messages.derived.py read. Nothing in those two reads
# the .proto text by regex: protoc is the parser of record here.
#
#   <python with grpcio-tools> -I check-protoc.derived.py --googleapis DIR [--write]
#
# DIR holds google/api/field_behavior.proto, fetched from googleapis/googleapis at the commit
# recorded in the descriptor's "googleapis" member (the library does not vendor it: it is not
# part of the source). Without --write the dump is compared with the committed file. Without
# grpc_tools importable the script says SKIPPED and exits 2 (never a silent pass).
#
# Why the originals are staged under their ORIGINAL names: the protos import each other by the
# bare names "envelope.proto", "sigstore_common.proto", "sigstore_rekor.proto", and the
# committed copies are named *.verbatim.proto. The staged bytes are asserted equal to the
# committed copies and to the sha256 table of ../render-source.py.
import hashlib, json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "protoc-descriptor.derived.json")
PROTOS = {  # original name -> committed verbatim copy
    "sigstore_bundle.proto": "sigstore_bundle.verbatim.proto",
    "envelope.proto": "envelope.verbatim.proto",
    "sigstore_common.proto": "sigstore_common.verbatim.proto",
    "sigstore_rekor.proto": "sigstore_rekor.verbatim.proto",
}
GOOGLEAPIS_COMMIT = "a6f4580d494b12461aa1b9190cac8eefe8a3fd22"
GOOGLEAPIS_FILE_SHA256 = "e2a1ac88c49909d4579bacbb18519085e82da32c2c7bb15c31037f3be19f667f"
# the number of the google.api.field_behavior extension on FieldOptions (field_behavior.proto)
FIELD_BEHAVIOR_EXT = 1052

TYPE = {1: "double", 2: "float", 3: "int64", 4: "uint64", 5: "int32", 6: "fixed64", 7: "fixed32",
        8: "bool", 9: "string", 10: "group", 11: "message", 12: "bytes", 13: "uint32", 14: "enum",
        15: "sfixed32", 16: "sfixed64", 17: "sint32", 18: "sint64"}
LABEL = {1: "optional", 2: "required", 3: "repeated"}


def varints(b):
    out, i = [], 0
    while i < len(b):
        v = s = 0
        while True:
            c = b[i]; i += 1
            v |= (c & 0x7F) << s; s += 7
            if not c & 0x80:
                break
        out.append(v)
    return out


def behaviours(raw, names):
    """google.api.field_behavior values (extension 1052, repeated enum) in raw FieldOptions bytes."""
    got, i = [], 0
    while i < len(raw):
        v = s = 0
        while True:
            c = raw[i]; i += 1
            v |= (c & 0x7F) << s; s += 7
            if not c & 0x80:
                break
        field, wt = v >> 3, v & 7
        if wt == 0:
            v = s = 0
            while True:
                c = raw[i]; i += 1
                v |= (c & 0x7F) << s; s += 7
                if not c & 0x80:
                    break
            val = [v]
        elif wt == 2:
            n = s = 0
            while True:
                c = raw[i]; i += 1
                n |= (c & 0x7F) << s; s += 7
                if not c & 0x80:
                    break
            val = varints(raw[i:i + n]) if field == FIELD_BEHAVIOR_EXT else None
            i += n
        else:
            raise SystemExit(f"unexpected wire type {wt} in FieldOptions")
        if field == FIELD_BEHAVIOR_EXT:
            got += [names[x] for x in val]
    return got


def rendering_map():
    """(original proto name, proto line) -> line of the rendering .cache/sigstore-bundle-0-3.txt, by
    running the record's own ../render-source.py renderer on the pinned inputs."""
    import importlib.util
    root = os.path.normpath(os.path.join(HERE, "..", "..", "..", "..", ".."))
    spec = importlib.util.spec_from_file_location("render_source", os.path.join(HERE, "..", "render-source.py"))
    rs = importlib.util.module_from_spec(spec); spec.loader.exec_module(rs)
    out, _ = rs.render(os.path.join(root, ".cache", "sigstore-bundle-0-3.bin"),
                       os.path.join(root, ".cache", "sigstore-bundle-0-3.include"))
    return {(name, s): i for i, (l, name, s) in enumerate(out, 1) if s is not None}


def span_line(f, path):
    for loc in f.source_code_info.location:
        if list(loc.path) == path:
            return loc.span[0] + 1  # protoc spans are 0-based
    return None


def dump(descset, rmap):
    from google.protobuf import descriptor_pb2 as d  # noqa: F401
    fb = None
    for f in descset.file:
        if f.name == "google/api/field_behavior.proto":
            fb = {v.number: v.name for v in f.enum_type[0].value}
    assert fb, "google/api/field_behavior.proto missing from the descriptor set"
    files = []
    for f in descset.file:
        if f.name not in PROTOS:
            continue
        ent = {"name": f.name, "package": f.package, "syntax": f.syntax or "proto2",
               "dependency": list(f.dependency), "messages": [], "enums": []}
        for mi, m in enumerate(f.message_type):
            oneofs = [o.name for o in m.oneof_decl]
            fields = []
            for fi, fl in enumerate(m.field):
                fields.append({
                    "name": fl.name, "number": fl.number, "json_name": fl.json_name,
                    "type": TYPE[fl.type], "type_name": fl.type_name.lstrip("."),
                    "label": LABEL[fl.label],
                    "oneof": oneofs[fl.oneof_index] if fl.HasField("oneof_index") and not fl.proto3_optional else None,
                    "proto3_optional": bool(fl.proto3_optional),
                    "behavior": behaviours(fl.options.SerializeToString(), fb),
                    "deprecated": bool(fl.options.deprecated),
                    "line": span_line(f, [4, mi, 2, fi]),
                    "rendering_line": rmap[(f.name, span_line(f, [4, mi, 2, fi]))],
                })
            ent["messages"].append({
                "name": m.name, "full_name": f"{f.package}.{m.name}", "line": span_line(f, [4, mi]),
                "rendering_line": rmap[(f.name, span_line(f, [4, mi]))],
                "fields": fields,
                "oneofs": [o.name for i, o in enumerate(m.oneof_decl)
                           if not any(fl.proto3_optional and fl.oneof_index == i for fl in m.field)],
                "reserved": [[r.start, r.end - 1] for r in m.reserved_range],
            })
        for ei, e in enumerate(f.enum_type):
            ent["enums"].append({
                "name": e.name, "full_name": f"{f.package}.{e.name}", "line": span_line(f, [5, ei]),
                "rendering_line": rmap[(f.name, span_line(f, [5, ei]))],
                "values": [{"name": v.name, "number": v.number, "deprecated": bool(v.options.deprecated),
                            "line": span_line(f, [5, ei, 2, vi]),
                            "rendering_line": rmap[(f.name, span_line(f, [5, ei, 2, vi]))]} for vi, v in enumerate(e.value)],
                "reserved": [[r.start, r.end] for r in e.reserved_range],
            })
        files.append(ent)
    return files


def main(argv):
    write = "--write" in argv
    gapis = argv[argv.index("--googleapis") + 1] if "--googleapis" in argv else None
    try:
        import grpc_tools  # noqa: F401
        from google.protobuf import descriptor_pb2
    except ImportError as e:
        print(f"SKIPPED: {e} (needs grpcio-tools and protobuf; use a scratch venv)")
        return 2
    if not gapis:
        print("usage: check-protoc.derived.py --googleapis DIR [--write]")
        return 2
    fbp = os.path.join(gapis, "google", "api", "field_behavior.proto")
    got = hashlib.sha256(open(fbp, "rb").read()).hexdigest()
    if got != GOOGLEAPIS_FILE_SHA256:
        print(f"FAIL: {fbp} sha256 {got} != pinned {GOOGLEAPIS_FILE_SHA256}")
        return 1
    # the sha256 table lives in render-source.py: read it, do not copy it
    src = open(os.path.join(HERE, "..", "render-source.py")).read()
    table = dict(re.findall(r'"(\w+\.proto)":\s*"([0-9a-f]{64})"', src))
    fails = []
    with tempfile.TemporaryDirectory() as td:
        for orig, ver in PROTOS.items():
            b = open(os.path.join(HERE, ver), "rb").read()
            if hashlib.sha256(b).hexdigest() != table[orig]:
                fails.append(f"{ver}: sha256 differs from render-source.py's table for {orig}")
            open(os.path.join(td, orig), "wb").write(b)
        desc = os.path.join(td, "bundle.desc")
        cmd = [sys.executable, "-m", "grpc_tools.protoc", "-I", td, "-I", gapis,
               f"--descriptor_set_out={desc}", "--include_imports", "--include_source_info",
               "sigstore_bundle.proto"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode:
            print("protoc FAILED:\n" + r.stderr)
            return 1
        ver = subprocess.run([sys.executable, "-m", "grpc_tools.protoc", "--version"],
                             capture_output=True, text=True).stdout.strip()
        ds = descriptor_pb2.FileDescriptorSet()
        ds.ParseFromString(open(desc, "rb").read())
    try:
        import importlib.metadata as md
        gt = md.version("grpcio-tools"); pb = md.version("protobuf")
    except Exception:
        gt = pb = "unknown"
    doc = {
        "kind": "derived-protoc-descriptor",
        "note": "DERIVED - written by this library, not the source. What protoc reports for the four "
                "*.verbatim.proto files in this directory. line = the line of the declaration in the "
                "ORIGINAL proto file; rendering_line = the line of that declaration in "
                ".cache/sigstore-bundle-0-3.txt (the one text every source_lines refers to), by "
                "../render-source.py's own line table.",
        "protoc": {"version": ver, "grpcio_tools": gt, "protobuf": pb, "include_imports": True},
        "googleapis": {"repo": "googleapis/googleapis", "commit": GOOGLEAPIS_COMMIT,
                       "path": "google/api/field_behavior.proto", "sha256": GOOGLEAPIS_FILE_SHA256,
                       "note": "the commit is the newest one touching that path when it was fetched (2026-11-20); "
                               "only the enum numbering (REQUIRED = 2) and extension number 1052 are used"},
        "inputs": {k: table[k] for k in PROTOS},
        "files": dump(ds, rendering_map()),
    }
    text = json.dumps(doc, indent=1, ensure_ascii=False) + "\n"
    n_msg = sum(len(f["messages"]) for f in doc["files"])
    n_fld = sum(len(m["fields"]) for f in doc["files"] for m in f["messages"])
    n_enum = sum(len(f["enums"]) for f in doc["files"])
    n_req = sum(1 for f in doc["files"] for m in f["messages"] for x in m["fields"] if "REQUIRED" in x["behavior"])
    print(f"protoc ({ver}): {len(doc['files'])} files, {n_msg} messages, {n_fld} fields "
          f"({n_req} REQUIRED), {n_enum} enums")
    if write:
        open(OUT, "w").write(text)
        print("wrote", OUT)
    else:
        have = open(OUT).read() if os.path.exists(OUT) else None
        # tool versions may differ between machines: compare everything but the protoc member
        a = json.loads(text); a.pop("protoc")
        b = json.loads(have) if have else {}; b.pop("protoc", None)
        if a != b:
            fails.append("descriptor differs from the committed protoc-descriptor.derived.json")
    for f in fails:
        print("FAIL:", f)
    if not fails:
        print("OK: compiled; descriptor matches" if not write else "OK")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

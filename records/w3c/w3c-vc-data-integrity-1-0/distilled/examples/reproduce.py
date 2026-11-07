#!/usr/bin/env python3
"""reproduce.py -- re-extract every example fixture of w3c-vc-data-integrity-1-0
from the source HTML and diff it against the files in this directory.

    python3 -I reproduce.py /path/to/w3c-vc-data-integrity-1-0.bin

Method (independent of the one that wrote the fixtures, which used html5lib):
regular expressions over the raw bytes. Each of the 14 <div class="example">
holds one <pre>; its content is taken between the tags, every other tag
(<wbr>, <span>, <code>, <strong>) removed, character references decoded with
html.unescape, and the LF directly after <pre> dropped if there is one. The
.bin must hash to content.sha256 in ../../record.yaml. The 12 derived fixtures
(*.derived.json, computed by this extraction, not the source's characters) are
re-computed by derive() below and diffed too. Prints EXAMINED beside FOUND.
Exit 1 on any difference.
"""
import hashlib, html, pathlib, re, sys, json

HERE = pathlib.Path(__file__).resolve().parent
EXPECT_SHA = 'ba5c4baf13fe3bab3ebd95ab6650d6fe83720e254b383bb444b4fbbae7bcf4fe'
TABLE = [
 [
  1,
  "ex01-simple-json-document.json",
  "71b62e2ef5f3213a68fdc9913065237e69a8a6b7645f17c3edf223336c11cfa2",
  "ex01-simple-json-document.derived.json",
  "21f26ddd11026d7aa1f1807b451891f7881fb372b280d48310b0b305b675865a"
 ],
 [
  2,
  "ex02-simple-signed-json-document.json",
  "61a2843265794222d66231fff257d87e0a550068997a6fa20b7f3d744567b9b7",
  None,
  None
 ],
 [
  3,
  "ex03-simple-json-ld-document.json",
  "f54357ca4cf0a9bf89f006fac997f04869a9761aeade0a1a2c77b6ff0e34adc0",
  "ex03-simple-json-ld-document.derived.json",
  "0e8101ae660e8139f367e65925a4db8e0a8d54fe230dac0c97143fafba531e16"
 ],
 [
  4,
  "ex04-simple-signed-json-ld-document.json",
  "4dbb4124bd2ae1d0252c3b89c209c938f3e9ea7b5c7224d866a20e8cdca6075f",
  None,
  None
 ],
 [
  5,
  "ex05-proof-with-expires.json",
  "a1e2c65a3e1072ba19c128c9318f81e2a0cbc7f94726bbed11d5925fa701e542",
  "ex05-proof-with-expires.derived.json",
  "4bf317c05779a819dc2b6cb28c1104cc1c3bde60a1d358bd6d6175feaa9588fa"
 ],
 [
  6,
  "ex06-proof-set.json",
  "443cb3aa9648a7eb95b11542a82b9dd06958bbbb0ae06e462acbb79481af50d0",
  "ex06-proof-set.derived.json",
  "30ef45610da62baa42311d53852ce83b0cf8e7a1d23489c8ec2effd3256012f5"
 ],
 [
  7,
  "ex07-proof-chain.json",
  "fcbb89b7c8006d0ca9bf9d7b41933c839de10cca30430b197aa415d13051f9d4",
  "ex07-proof-chain.derived.json",
  "f72c62baddeb553971455769bcef355e2badd834342f4c7c01f284883ae6ce73"
 ],
 [
  8,
  "ex08-integrity-protected-image.json",
  "26cd287485a98fa30db196a31cece73e585d8f59a1dbf35dac06d534bf653ca5",
  "ex08-integrity-protected-image.derived.json",
  "471d5b0702733052004c20c27e02bb74e964c051f803b9f79c481d73eecadf24"
 ],
 [
  9,
  "ex09-symbolic-proof.json",
  "1cbc697af8d4c427ec542f402aaa1d6b6138ec1a9988191097500e3daee9fa4a",
  "ex09-symbolic-proof.derived.json",
  "aa50c08a79ed454ab683cd4e4dcd7c2c2b2294353f81ff2de6cba1fc324fdd27"
 ],
 [
  10,
  "ex10-symbolic-proof-set.json",
  "7fec6cbda4e6aba42e38addbfabec7acedc439e66ae2165441174b9b56c9c4d3",
  "ex10-symbolic-proof-set.derived.json",
  "1c484878fe6af177d45623a4b3b0f13c2bac14bc5184ff5f86e7774b4f88a56d"
 ],
 [
  11,
  "ex11-symbolic-proof-set-removal.json",
  "6d4dc200a3726d60dc6ec304938821de1b5ceb38f509f78069524180dada31cb",
  "ex11-symbolic-proof-set-removal.derived.json",
  "5bf5d19706d044d160222715cbc7e74a3280c324637eeceea515db92b7a47179"
 ],
 [
  12,
  "ex12-symbolic-chain-first-proof.json",
  "ddf4d9676c59cac9142111ba54266fba55543bc54db946b70cf6368dd62aaf03",
  "ex12-symbolic-chain-first-proof.derived.json",
  "b6fb9fae8d540fc24ca3d8924354eb5367a936308106d015c8e40fc0b6abf775"
 ],
 [
  13,
  "ex13-symbolic-chain-two-proofs.json",
  "9fe8b503c3901d9bec1a20a1daae9327dba09a1e4bb119343b798f2d01a479ca",
  "ex13-symbolic-chain-two-proofs.derived.json",
  "47d7c70b4b30c8a5034345b117b29103f08f27ee4fa4533445812d7c3c0d51f9"
 ],
 [
  14,
  "ex14-symbolic-chain-three-proofs.json",
  "ae1fd4c0b6a1dd7d54fe3969d0de6e2e1296145d8e3d8f5d55d116242797504c",
  "ex14-symbolic-chain-three-proofs.derived.json",
  "376679ce0973b2b522c0d0ee522865273e4db53a3ba0f00276cbdb1713eeb470"
 ]
]


def derive(n, t):
    if n in (1, 3):
        assert t.endswith("};")
        return t[:-1]
    if n in (5, 6, 7):
        return "\n".join(l for l in t.split("\n") if not l.strip().startswith("//"))
    if n == 8:
        ls = t.split("\n")
        assert ls[1].strip() == "..." and ls[2].strip() == '"image": {' and ls[5].strip() == "},"
        return "{\n" + "\n".join(l[2:] for l in ls[3:5]) + "\n}"
    if n in (9, 10, 11, 12, 13, 14):
        out = []
        for l in t.split("\n"):
            if l.strip().startswith("//"):
                continue
            l = re.sub(r'(:\s*)(public[A-Z]+)(,?)$', r'\1"\2"\3', l)
            l = re.sub(r'(:\s*)(signature\([^()]*\))(,?)$', r'\1"\2"\3', l)
            out.append(l)
        return "\n".join(out)
    return None


def main():
    raw = pathlib.Path(sys.argv[1]).read_bytes()
    got = hashlib.sha256(raw).hexdigest()
    rec = (HERE.parent.parent / "record.yaml").read_text()
    m = re.search(r'sha256:\s*"([0-9a-f]{64})"', rec)
    assert m and m.group(1) == got == EXPECT_SHA, ("source digest mismatch", got)
    text = raw.decode("utf-8")
    blocks = re.findall(r'<div class="example" id="[^"]*">\s*<div class="marker">.*?Example<bdi> (\d+)</bdi>.*?</div>\s*<pre[^>]*>(.*?)</pre>', text, re.S)
    examined = found = 0
    assert len(blocks) == 14, len(blocks)
    for (num, body), (n, fname, digest, dname, ddigest) in zip(blocks, TABLE):
        assert int(num) == n
        body = re.sub(r"<[^>]+>", "", body)
        body = html.unescape(body)
        if body.startswith("\n"):
            body = body[1:]
        for fn, want, val in ((fname, digest, body), (dname, ddigest, derive(n, body) if dname else None)):
            if fn is None:
                continue
            examined += 1
            disk = (HERE / fn).read_bytes()
            ok = disk == val.encode("utf-8") and hashlib.sha256(disk).hexdigest() == want
            if not ok:
                found += 1
                print("DIFF", fn)
    print(f"EXAMINED {examined} fixtures (14 verbatim + {sum(1 for t in TABLE if t[3])} derived); DIFFERENT {found}")
    sys.exit(1 if found else 0)


main()

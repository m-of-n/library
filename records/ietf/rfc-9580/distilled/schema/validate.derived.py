#!/usr/bin/env python3
"""DERIVED -- not part of RFC 9580.

Decoder and checker for the derived artifacts in this directory:

  * decodes binary or ASCII-armored OpenPGP data (RFC 9580 §4, §5, §6, §7)
    into the JSON model described by openpgp-packets.derived.schema.json;
  * validates that JSON against the schema (needs the `jsonschema` package;
    skipped with a note if it is absent);
  * applies the checks JSON Schema cannot express (MPI bit counts, length
    fields that must agree, fingerprints, OPS/Signature correspondence);
  * matches the packet sequence against the §10 grammars as rendered in
    packet-sequences.derived.abnf.

It does no cryptography: no signature is verified and nothing is decrypted.

Usage:
  python3 -I validate.derived.py FILE...            # binary or armored
  python3 -I validate.derived.py --json FILE...     # also print decoded JSON
  python3 -I validate.derived.py --rfc .cache/rfc-9580.txt
        # self-test on every armored block of Appendix A
  --padding-anywhere   drop Padding packets before grammar matching (R-0239)

Every check names its source section and, where one exists, its requirement
id (rfc-9580#R-NNNN, see ../requirements.yaml).
"""
import base64, binascii, bz2, hashlib, json, os, re, sys, zlib

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA = os.path.join(HERE, 'openpgp-packets.derived.schema.json')

# Values RFC 9580 tabulates (Table 23, 25) or names (Table 21, inferred).
SALT = {8: 16, 9: 24, 10: 32, 11: 16, 12: 16, 14: 32}                 # Table 23
DIGEST = {1: 16, 2: 20, 3: 20, 8: 32, 9: 48, 10: 64, 11: 28, 12: 32, 14: 64}
NONCE = {1: 16, 2: 15, 3: 12}                                         # Table 25
TAG = {1: 16, 2: 16, 3: 16}
HASH_TEXT_NAMES = {'MD5', 'SHA1', 'RIPEMD160', 'SHA256', 'SHA384',     # Table 23
                   'SHA512', 'SHA224', 'SHA3-256', 'SHA3-512'}         # Text Name
BLOCK = {1: 8, 2: 8, 3: 8, 4: 8, 7: 16, 8: 16, 9: 16, 10: 16, 11: 16, 12: 16, 13: 16}  # INFERRED
CURVE25519_LEGACY = '2b060104019755010501'


class Malformed(Exception):
    pass


class Reader:
    def __init__(self, data, pos=0, end=None):
        self.d, self.p, self.e = data, pos, len(data) if end is None else end

    def left(self):
        return self.e - self.p

    def take(self, n, what='field'):
        if n < 0 or self.p + n > self.e:          # §4.1 R-0021
            raise Malformed(f'{what}: needs {n} octets, {self.left()} left (§4.1, R-0021)')
        b = self.d[self.p:self.p + n]
        self.p += n
        return b

    def u8(self, w='octet'):
        return self.take(1, w)[0]

    def u16(self, w='2-octet scalar'):
        return int.from_bytes(self.take(2, w), 'big')

    def u32(self, w='4-octet scalar'):
        return int.from_bytes(self.take(4, w), 'big')

    def hexn(self, n, w='octets'):
        return self.take(n, w).hex()

    def rest(self):
        return self.take(self.left()).hex()

    def mpi(self, w='MPI'):
        bits = self.u16(w + ' bit count')
        return {'bits': bits, 'value': self.take((bits + 7) // 8, w).hex()}


# ------------------------------------------------------------------ armor §6
ARMOR = re.compile(r'^-----BEGIN PGP ([A-Z ,0-9/]+)-----\s*$')


def crc24(data):                                   # §6.1.1, verbatim E-46
    crc = 0xB704CE
    for o in data:
        crc ^= o << 16
        for _ in range(8):
            crc <<= 1
            if crc & 0x1000000:
                crc &= 0xFFFFFF
                crc ^= 0x864CFB
    return crc & 0xFFFFFF


def dearmor(text, notes):
    """Yield (label, bytes) for every armored block; cleartext frameworks yield
    their signature block.  §6.2, §7.1."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        m = ARMOR.match(lines[i])
        if not m:
            i += 1
            continue
        label = m.group(1)
        i += 1
        headers = []
        while i < len(lines) and lines[i].strip():          # §6.2.2 R-0254
            headers.append(lines[i])
            i += 1
        i += 1                                              # blank line
        if label == 'SIGNED MESSAGE':                       # §7.1: skip cleartext
            for h in headers:
                if not h.startswith('Hash: '):
                    notes.append(f'cleartext header other than Hash: {h!r} -> MUST decline (§7.1, R-0267)')
                elif not all(n.strip() in HASH_TEXT_NAMES for n in h[6:].split(',')):
                    notes.append(f'non-conformant Hash header: {h!r} -> MUST decline (§6.2.2.3, R-0259)')
            while i < len(lines) and not lines[i].startswith('-----BEGIN PGP SIGNATURE-----'):
                if lines[i].startswith('-') and not lines[i].startswith('- '):
                    notes.append(f'unescaped dash line in cleartext: {lines[i]!r} (§7.2, R-0271)')
                i += 1
            continue
        for h in headers:
            if ': ' not in h:
                notes.append(f'improper Armor Header {h!r} (§6.2.2, R-0255)')
        b64, crc = [], None
        while i < len(lines) and not lines[i].startswith('-----END PGP '):
            s = lines[i].strip()
            if s.startswith('=') and len(s) == 5:
                crc = s[1:]
            elif s:
                b64.append(s)
            i += 1
        tail = lines[i].strip() if i < len(lines) else ''
        if tail != f'-----END PGP {label}-----':            # §6.2.3
            notes.append(f'Armor Tail Line {tail!r} does not match header {label!r} (§6.2.3)')
        data = base64.b64decode(''.join(b64))               # §6 R-0241: whitespace ignored
        if crc is not None:
            ok = base64.b64decode(crc) == crc24(data).to_bytes(3, 'big')
            notes.append(f'CRC24 footer present ({"matches" if ok else "MISMATCH, not a rejection (R-0244)"}); '
                         'SHOULD NOT be generated (§6.1, R-0245)')
        yield label, data
        i += 1


# ------------------------------------------------------------------ headers §4.2
def read_packets(data, notes, depth=0):
    r = Reader(data)
    out = []
    while r.left():
        b0 = r.u8('packet header')
        if not b0 & 0x80:
            raise Malformed(f'packet header octet 0x{b0:02x}: bit 7 not set (§4.2)')
        if b0 & 0x40:
            tag = b0 & 0x3F
            hdr = {'format': 'openpgp', 'type_id': tag}
            o = r.u8('length')
            if o < 192:
                ln, length = o, {'encoding': '1-octet', 'body_length': o}
            elif o < 224:
                ln = ((o - 192) << 8) + r.u8('length') + 192
                length = {'encoding': '2-octet', 'body_length': ln}
            elif o == 255:
                ln = r.u32('length')
                length = {'encoding': '5-octet', 'body_length': ln}
            else:                                           # §4.2.1.4 partial
                parts, body = [], b''
                while 224 <= o < 255:
                    n = 1 << (o & 0x1F)
                    parts.append(n)
                    body += r.take(n, 'partial body')
                    o = r.u8('length')
                if o < 192:
                    fl, final = o, {'encoding': '1-octet', 'body_length': o}
                elif o < 224:
                    fl = ((o - 192) << 8) + r.u8() + 192
                    final = {'encoding': '2-octet', 'body_length': fl}
                else:
                    fl = r.u32()
                    final = {'encoding': '5-octet', 'body_length': fl}
                body += r.take(fl, 'final partial body')
                length = {'encoding': 'partial', 'parts': parts, 'final': final, 'body_length': len(body)}
                hdr['length'] = length
                out.append({'header': hdr, 'body': decode_body(tag, body, notes, depth)})
                continue
        else:
            tag = (b0 >> 2) & 0x0F
            lt = b0 & 3
            hdr = {'format': 'legacy', 'type_id': tag}
            if lt == 3:
                ln = r.left()
                length = {'encoding': 'legacy-indeterminate', 'length_type': 3}
            else:
                ln = int.from_bytes(r.take((1, 2, 4)[lt], 'length'), 'big')
                length = {'encoding': ('legacy-1-octet', 'legacy-2-octet', 'legacy-4-octet')[lt],
                          'length_type': lt, 'body_length': ln}
        hdr['length'] = length
        body = r.take(ln, 'packet body')                    # §4.1 R-0020
        out.append({'header': hdr, 'body': decode_body(tag, body, notes, depth)})
    return out


# ------------------------------------------------------------------ bodies §5
def s2k(r):                                                  # §3.7.1
    t = r.u8('S2K type')
    if t == 0:
        return {'type': 0, 'hash_algo': r.u8()}
    if t == 1:
        return {'type': 1, 'hash_algo': r.u8(), 'salt': r.hexn(8)}
    if t == 3:
        return {'type': 3, 'hash_algo': r.u8(), 'salt': r.hexn(8), 'count': r.u8()}
    if t == 4:
        return {'type': 4, 'salt': r.hexn(16), 't': r.u8(), 'p': r.u8(), 'encoded_m': r.u8()}
    return {'type': t, 'body': r.rest()}


def curve(r):
    n = r.u8('curve OID length')
    return {'length': n, 'oid': r.hexn(n, 'curve OID')}


def public_material(a, r):                                   # §5.5.5
    if a in (1, 2, 3):
        return {'n': r.mpi(), 'e': r.mpi()}
    if a == 16:
        return {'p': r.mpi(), 'g': r.mpi(), 'y': r.mpi()}
    if a == 17:
        return {'p': r.mpi(), 'q': r.mpi(), 'g': r.mpi(), 'y': r.mpi()}
    if a in (19, 22):
        return {'curve': curve(r), 'point': r.mpi()}
    if a == 18:
        c, pt = curve(r), r.mpi()
        n = r.u8('KDF parameter size')
        kr = Reader(r.take(n, 'KDF parameters'))
        kdf = {'length': n, 'reserved': kr.u8(), 'hash_algo': kr.u8(), 'sym_algo': kr.u8()}
        if kr.left():
            raise Malformed('ECDH KDF parameters longer than 3 octets (§5.5.5.6)')
        return {'curve': c, 'point': pt, 'kdf': kdf}
    if a in (25, 26, 27, 28):
        return {'public': r.hexn({25: 32, 26: 56, 27: 32, 28: 57}[a])}
    return {'unknown': r.rest()}


def secret_material(a, r):
    if a in (1, 2, 3):
        return {'d': r.mpi(), 'p': r.mpi(), 'q': r.mpi(), 'u': r.mpi()}
    if a in (16, 17, 19, 18):
        return {'x': r.mpi()}
    if a == 22:
        return {'seed': r.mpi()}
    if a in (25, 26, 27, 28):
        return {'secret': r.hexn({25: 32, 26: 56, 27: 32, 28: 57}[a])}
    return {'unknown': r.rest()}


def key(body, secret):                                       # §5.5.2, §5.5.3
    r = Reader(body)
    v = r.u8('key version')
    k = {'version': v, 'creation_time': r.u32()}
    if v in (2, 3):
        k['validity_days'] = r.u16()
    k['pk_algo'] = a = r.u8()
    if v == 6:
        k['material_length'] = ml = r.u32()
        mr = Reader(r.take(ml, 'public key material'))
        k['public'] = public_material(a, mr)
        if mr.left():
            raise Malformed('v6 key material count exceeds the material (§5.5.2.3)')
    elif v in (2, 3, 4):
        k['public'] = public_material(a, r)
    else:
        raise Malformed(f'unknown key version {v} (§5.5.2)')
    pub_len = r.p
    if not secret:
        if r.left():
            raise Malformed('trailing octets after public key material')
        return k, body[:pub_len]
    u = r.u8('S2K usage')
    s = {'s2k_usage': u}
    if v == 6 and u:
        s['params_length'] = r.u8()
    if u in (253, 254, 255):
        s['sym_algo'] = r.u8()
    if u == 253:
        s['aead_algo'] = r.u8()
    if v == 6 and u in (253, 254):
        s['s2k_length'] = r.u8()
    if u in (253, 254, 255):
        if 's2k_length' in s:
            s['s2k'] = s2k(Reader(r.take(s['s2k_length'], 'S2K specifier')))
        else:
            s['s2k'] = s2k(r)
    if u == 253:
        s['iv'] = r.hexn(NONCE.get(s['aead_algo'], 0), 'AEAD nonce')
    elif u:
        cipher = s.get('sym_algo', u)
        if cipher not in BLOCK:
            raise Malformed(f'unknown cipher {cipher}: IV length unknown (§5.5.3)')
        s['iv'] = r.hexn(BLOCK[cipher], 'CFB IV')
    if u == 0:
        s['cleartext'] = secret_material(a, r)
        if v in (2, 3, 4):
            s['checksum'] = r.hexn(2, 'secret checksum')
    elif u == 253:
        rest = r.take(r.left())
        s['encrypted'], s['aead_tag'] = rest[:-16].hex(), rest[-16:].hex()
    else:
        s['encrypted'] = r.rest()
    if r.left():
        raise Malformed('trailing octets after secret key material')
    k['secret'] = s
    # the public part of a secret key packet, for fingerprints (§5.5.4)
    return k, body[:pub_len]


def subpackets(r, n, notes):                                 # §5.2.3.7
    sr = Reader(r.take(n, 'subpacket area'))
    out = []
    while sr.left():
        o = sr.u8('subpacket length')
        if o < 192:
            ln, lo = o, 1
        elif o < 255:
            ln, lo = ((o - 192) << 8) + sr.u8() + 192, 2
        else:
            ln, lo = sr.u32(), 5
        if ln == 0:
            raise Malformed('subpacket length 0 leaves no type octet (§5.2.3.7)')
        data = sr.take(ln, 'subpacket')
        t = data[0]
        sp = {'critical': bool(t & 0x80), 'type_id': t & 0x7F, 'length_octets': lo}
        try:
            sp['value'] = subpacket_value(t & 0x7F, data[1:], notes)
        except (Malformed, UnicodeDecodeError, IndexError, ValueError) as e:
            sp['body'] = data[1:].hex()
            notes.append(f'subpacket {t & 0x7F} body not decodable: {e}')
        if sp.get('value') is None:
            sp.pop('value', None)
            sp['body'] = data[1:].hex()
        out.append(sp)
    return out


def subpacket_value(t, d, notes):                            # §5.2.3.11-§5.2.3.36
    r = Reader(d)
    def done(v):
        if r.left():
            raise Malformed(f'subpacket {t}: {r.left()} unexpected octets (§5.2.5)')
        return v
    if t == 2:
        return done({'time': r.u32()})
    if t in (3, 9):
        return done({'seconds': r.u32()})
    if t == 4:
        return done({'exportable': r.u8()})
    if t == 5:
        return done({'level': r.u8(), 'amount': r.u8()})
    if t == 6:
        term = d.endswith(b'\0')                  # R-0126, R-0127
        return {'regex': (d[:-1] if term else d).decode('utf-8'), 'nul_terminated': term}
    if t == 7:
        return done({'revocable': r.u8()})
    if t in (11, 21, 22):
        return {'algorithms': list(d)}
    if t == 12:
        return done({'class': r.u8(), 'pk_algo': r.u8(), 'fingerprint': r.hexn(20)})
    if t == 16:
        return done({'key_id': r.hexn(8)})
    if t == 20:
        f, m, n = r.hexn(4), r.u16(), r.u16()
        return done({'flags': f, 'name_length': m, 'value_length': n,
                     'name': r.take(m).decode('utf-8'), 'value': r.hexn(n)})
    if t in (23, 27, 30):
        return {'flags': d.hex()}
    if t in (24, 26):
        return {'uri': d.decode('utf-8')}
    if t == 25:
        return done({'primary': r.u8()})
    if t == 28:
        return {'user_id': d.decode('utf-8')}
    if t == 29:
        return {'code': r.u8(), 'reason': r.take(r.left()).decode('utf-8')}
    if t == 31:
        return {'pk_algo': r.u8(), 'hash_algo': r.u8(), 'hash': r.rest()}
    if t == 32:
        return {'signature': signature(d, notes)}
    if t in (33, 35):
        return {'key_version': r.u8(), 'fingerprint': r.rest()}
    if t == 39:
        if len(d) % 2:
            raise Malformed('Preferred AEAD Ciphersuites: odd length (§5.2.3.15)')
        return {'pairs': [[d[i], d[i + 1]] for i in range(0, len(d), 2)]}
    return None


def sig_material(a, r):
    if a in (1, 3):
        return {'m_d_mod_n': r.mpi()}
    if a in (17, 19, 22):
        return {'r': r.mpi(), 's': r.mpi()}
    if a == 27:
        return {'native': r.hexn(64)}
    if a == 28:
        return {'native': r.hexn(114)}
    return {'unknown': r.rest()}


def signature(body, notes):                                  # §5.2.2, §5.2.3
    r = Reader(body)
    v = r.u8('signature version')
    if v == 3:
        s = {'version': 3, 'hashed_length': r.u8(), 'sig_type': r.u8(), 'creation_time': r.u32(),
             'key_id': r.hexn(8), 'pk_algo': r.u8(), 'hash_algo': r.u8(), 'hash_left16': r.hexn(2)}
    elif v in (4, 6):
        s = {'version': v, 'sig_type': r.u8(), 'pk_algo': r.u8(), 'hash_algo': r.u8()}
        lf = r.u16 if v == 4 else r.u32
        s['hashed_length'] = n = lf()
        s['hashed'] = subpackets(r, n, notes)
        s['unhashed_length'] = n = lf()
        s['unhashed'] = subpackets(r, n, notes)
        s['hash_left16'] = r.hexn(2)
        if v == 6:
            s['salt_size'] = n = r.u8()
            s['salt'] = r.hexn(n, 'salt')
    else:
        raise Malformed(f'unknown signature version {v} (§5.2.5: ignore the signature)')
    s['signature'] = sig_material(s['pk_algo'], r)
    if r.left():
        raise Malformed('trailing octets after signature material')
    return s


def pkesk(body):                                              # §5.1
    r = Reader(body)
    v = r.u8()
    if v == 3:
        p = {'version': 3, 'key_id': r.hexn(8)}
    elif v == 6:
        p = {'version': 6, 'key_info_length': r.u8()}
        if p['key_info_length']:
            p['key_version'] = r.u8()
            p['fingerprint'] = r.hexn(p['key_info_length'] - 1)
    else:
        raise Malformed(f'unknown PKESK version {v}')
    p['pk_algo'] = a = r.u8()
    if a in (1, 2):
        e = {'m_e_mod_n': r.mpi()}
    elif a == 16:
        e = {'g_k_mod_p': r.mpi(), 'm_y_k_mod_p': r.mpi()}
    elif a == 18:
        e = {'ephemeral': r.mpi()}
        e['wrapped_length'] = n = r.u8()
        e['wrapped_key'] = r.hexn(n)
    elif a in (25, 26):
        e = {'ephemeral': r.hexn(32 if a == 25 else 56), 'length': r.u8()}
        if v == 3:
            e['sym_algo'] = r.u8()
        e['wrapped_key'] = r.hexn(e['length'] - (1 if v == 3 else 0))
    else:
        e = {'unknown': r.rest()}
    if r.left():
        raise Malformed('trailing octets after PKESK fields')
    p['esk'] = e
    return p


def skesk(body):                                              # §5.3
    r = Reader(body)
    v = r.u8()
    if v == 4:
        k = {'version': 4, 'sym_algo': r.u8(), 's2k': s2k(r)}
        if r.left():
            k['encrypted_session_key'] = r.rest()
        return k
    if v == 6:
        k = {'version': 6, 'params_length': r.u8(), 'sym_algo': r.u8(), 'aead_algo': r.u8(),
             's2k_length': r.u8()}
        k['s2k'] = s2k(Reader(r.take(k['s2k_length'], 'S2K specifier')))
        k['iv'] = r.hexn(NONCE.get(k['aead_algo'], 0))
        rest = r.take(r.left())
        k['encrypted_session_key'], k['tag'] = rest[:-16].hex(), rest[-16:].hex()
        return k
    raise Malformed(f'unknown SKESK version {v}')


def ops(body):                                                # §5.4
    r = Reader(body)
    v = r.u8()
    o = {'version': v, 'sig_type': r.u8(), 'hash_algo': r.u8(), 'pk_algo': r.u8()}
    if v == 3:
        o['key_id'] = r.hexn(8)
    elif v == 6:
        o['salt_size'] = n = r.u8()
        o['salt'] = r.hexn(n)
        o['fingerprint'] = r.hexn(32)
    else:
        raise Malformed(f'unknown OPS version {v}')
    o['nested'] = r.u8()
    if r.left():
        raise Malformed('trailing octets after OPS fields')
    return o


def decode_body(tag, body, notes, depth):
    r = Reader(body)
    try:
        if tag == 1:
            return pkesk(body)
        if tag == 2:
            return signature(body, notes)
        if tag == 3:
            return skesk(body)
        if tag == 4:
            return ops(body)
        if tag in (5, 6, 7, 14):
            k, pub = key(body, tag in (5, 7))
            k['_public_body'] = pub.hex()        # private to this tool; removed before schema check
            return k
        if tag == 8:
            c = {'algorithm': r.u8(), 'data': r.rest()}
            raw = bytes.fromhex(c['data'])
            try:
                inner = {0: lambda b: b, 1: lambda b: zlib.decompress(b, -15), 2: zlib.decompress,
                         3: bz2.decompress}[c['algorithm']](raw)
                if depth > 8:                    # §13.14 R-0419
                    notes.append('more than 8 nested compression layers: stop (§13.14, R-0419)')
                else:
                    c['packets'] = read_packets(inner, notes, depth + 1)
            except (KeyError, zlib.error, OSError, ValueError) as e:
                notes.append(f'compressed data not decompressed: {e}')
            return c
        if tag == 9:
            return {'data': r.rest()}
        if tag == 10:
            return {'octets': r.rest()}
        if tag == 11:
            f = chr(r.u8())
            n = r.u8()
            return {'format': f, 'filename': r.hexn(n), 'date': r.u32(), 'data': r.rest()}
        if tag == 12:
            return {'data': r.rest()}
        if tag == 13:
            return {'user_id': body.decode('utf-8')}
        if tag == 17:
            subs = []
            while r.left():
                o = r.u8()
                if o < 192:
                    ln, lo = o, 1
                elif o < 255:
                    ln, lo = ((o - 192) << 8) + r.u8() + 192, 2
                else:
                    ln, lo = r.u32(), 5
                d = r.take(ln, 'attribute subpacket')
                sp = {'type_id': d[0], 'length_octets': lo}
                if d[0] == 1:
                    ir = Reader(d[1:])
                    hl = int.from_bytes(ir.take(2), 'little')       # §5.12.1: little-endian
                    sp['value'] = {'header_length': hl, 'header_version': ir.u8(), 'encoding': ir.u8(),
                                   'reserved': ir.hexn(12), 'image': ir.rest()}
                else:
                    sp['body'] = d[1:].hex()
                subs.append(sp)
            return {'subpackets': subs}
        if tag == 18:
            v = r.u8()
            if v == 1:
                return {'version': 1, 'data': r.rest()}
            if v == 2:
                s = {'version': 2, 'sym_algo': r.u8(), 'aead_algo': r.u8(), 'chunk_size': r.u8(),
                     'salt': r.hexn(32)}
                rest = r.take(r.left())
                s['data'], s['final_tag'] = rest[:-16].hex(), rest[-16:].hex()
                return s
            raise Malformed(f'unknown SEIPD version {v}')
        if tag == 21:
            return {'data': r.rest()}
        return {'data': r.rest()}
    except Malformed as e:
        notes.append(f'packet type {tag}: MALFORMED: {e}')
        return {'_malformed': str(e), 'data': body.hex()}


# ------------------------------------------------------------------ extra checks
def fingerprint(version, pub):                                 # §5.5.4
    if version == 4:
        return hashlib.sha1(b'\x99' + len(pub).to_bytes(2, 'big') + pub).hexdigest()
    if version == 6:
        return hashlib.sha256(b'\x9b' + len(pub).to_bytes(4, 'big') + pub).hexdigest()
    return None


def key_id(version, fp, k):
    if version == 4:
        return fp[-16:]
    if version == 6:
        return fp[:16]
    return k['public']['n']['value'][-16:]


def walk_mpis(o, path=''):
    if isinstance(o, dict):
        if set(o) == {'bits', 'value'}:
            yield path, o
        else:
            for k, v in o.items():
                yield from walk_mpis(v, f'{path}.{k}')
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from walk_mpis(v, f'{path}[{i}]')


def check_mpis(pkt, errs, warns=None):                                     # §3.2 R-0003, R-0004
    b = pkt['body']
    strict = b.get('version') == 6 and pkt['header']['type_id'] in (1, 2, 5, 6, 7, 14)
    for path, m in walk_mpis({k: v for k, v in b.items() if k != 'secret' or
                              'cleartext' in v}):
        val = bytes.fromhex(m['value'])
        if len(val) != (m['bits'] + 7) // 8:
            errs.append(f'MPI {path}: {len(val)} octets for {m["bits"]} bits (§3.2)')
            continue
        actual = int.from_bytes(val, 'big').bit_length()
        if actual > m['bits']:
            errs.append(f'MPI {path}: unused bits not zero (§3.2, R-0004)')
        elif actual != m['bits'] and strict:
            errs.append(f'MPI {path}: bit count {m["bits"]} != {actual} in a v6 packet (§3.2, R-0003)')
        elif actual != m['bits'] and warns is not None:
            warns.append(f'MPI {path}: bit count {m["bits"]} != {actual}: "not formed correctly" (§3.2); '
                         'rejection is required only in v6 packets (R-0003)')


def check_packet(pkt, errs, warns):
    t, b = pkt['header']['type_id'], pkt['body']
    if '_malformed' in b:
        errs.append(b['_malformed'])
        return
    check_mpis(pkt, errs, warns)
    if t in (5, 6, 7, 14) and b.get('version') == 6:
        pub = bytes.fromhex(b['_public_body'])
        if b['material_length'] != len(pub) - 10:
            errs.append('v6 key material_length disagrees with the material (§5.5.2.3)')
    if t in (5, 7) and b.get('secret', {}).get('s2k_usage') and b['version'] == 6:
        s = b['secret']
        n = sum(1 for k in ('sym_algo', 'aead_algo', 's2k_length') if k in s) + len(bytes.fromhex(s['iv']))
        n += len(encode_s2k(s['s2k'])) if 's2k' in s else 0
        if s['params_length'] != n:
            errs.append(f'v6 secret key params_length {s["params_length"]} != {n} (§5.5.3)')
    if t in (5, 7):
        s = b.get('secret', {})
        if s.get('s2k_usage') == 0 and b['pk_algo'] == 18 and b['public'].get('curve', {}).get('oid') == CURVE25519_LEGACY:
            x = s['cleartext']['x']
            iv = int(x['value'], 16)
            if not (x['bits'] == 255 and iv % 8 == 0 and 2**254 <= iv < 2**255):
                errs.append('Curve25519Legacy secret MPI form (§5.5.5.6.1.1, R-0199..R-0202)')
    if t == 1:
        e = b['esk']
        if b['pk_algo'] in (25, 26) and e['length'] != len(bytes.fromhex(e['wrapped_key'])) + (b['version'] == 3):
            errs.append('X25519/X448 PKESK size octet disagrees (§5.1.6, §5.1.7)')
    if t == 3 and b.get('version') == 6:
        if b['s2k_length'] != len(encode_s2k(b['s2k'])):
            errs.append('v6 SKESK s2k_length disagrees with the S2K specifier (§5.3.2)')
        if b['params_length'] != 3 + b['s2k_length'] + len(bytes.fromhex(b['iv'])):
            errs.append('v6 SKESK count of the 5 following fields disagrees (§5.3.2)')
    if t == 2:
        check_signature(b, errs, warns)
    if t == 11:
        if b['format'] in 'tl1':
            warns.append(f'Literal Data format {b["format"]!r} is deprecated (§5.9, R-0210)')
    for k in ('packets',):
        for inner in b.get(k, []):
            check_packet(inner, errs, warns)


def check_signature(s, errs, warns, embedded=False):
    if s['version'] in (4, 6):
        for area in ('hashed', 'unhashed'):
            for sp in s[area]:
                v = sp.get('value', {})
                known = sp['type_id'] in {2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 16, 20, 21, 22, 23, 24, 25,
                                          26, 27, 28, 29, 30, 31, 32, 33, 35, 39}
                if sp['critical'] and not known and area == 'hashed':
                    warns.append(f'unknown critical subpacket {sp["type_id"]}: signature in error '
                                 '(§5.2.3.7, R-0080, §5.2.5)')
                if sp['type_id'] == 20 and v:
                    if v['name_length'] != len(v['name'].encode()) or v['value_length'] * 2 != len(v['value']):
                        errs.append('Notation Data lengths disagree (§5.2.3.24)')
                if sp['type_id'] == 32 and v:
                    check_signature(v['signature'], errs, warns, True)
        fps = [sp['value']['fingerprint'] for sp in s['hashed'] + s['unhashed']
               if sp['type_id'] == 33 and 'value' in sp]
        kids = [sp['value']['key_id'] for sp in s['hashed'] + s['unhashed']
                if sp['type_id'] == 16 and 'value' in sp]
        if s['version'] == 4:
            for k in kids:
                for f in fps:
                    if f[-16:] != k:
                        errs.append('Issuer Key ID != low 64 bits of Issuer Fingerprint (§5.2.3.35, R-0158)')
        if s['version'] == 6 and kids:
            warns.append('Issuer Key ID in a v6 signature: MUST NOT be included (§5.2.3.12, R-0103)')


def encode_s2k(s):
    t = s['type']
    if t == 0:
        return bytes([0, s['hash_algo']])
    if t == 1:
        return bytes([1, s['hash_algo']]) + bytes.fromhex(s['salt'])
    if t == 3:
        return bytes([3, s['hash_algo']]) + bytes.fromhex(s['salt']) + bytes([s['count']])
    if t == 4:
        return bytes([4]) + bytes.fromhex(s['salt']) + bytes([s['t'], s['p'], s['encoded_m']])
    return bytes([t]) + bytes.fromhex(s.get('body', ''))


# ------------------------------------------------------------------ grammars §10
def token(p):
    t = p['header']['type_id']
    return chr(0x200 + p['body']['sig_type']) if t == 2 and 'sig_type' in p['body'] else chr(t)

PK, SK, PSUB, SSUB, UID, UAT, PAD = '\x06', '\x05', '\x0e', '\x07', '\x0d', '\x11', '\x15'
KEYREV, DKS, CERT, CERTREV = 'Ƞ', 'ȟ', '[Ȑ-ȓ]', 'Ȱ'
SUBBIND, SUBREV, ANYSIG = 'Ș', 'Ȩ', '[Ȁ-˿]'


def key_grammars(secret):
    P = f'[{PK}{SK}]' if secret else PK
    K = f'[{PSUB}{SSUB}]' if secret else PSUB
    return {   # packet-sequences.derived.abnf, rules v6-certificate .. v3-key
        'v6-certificate': f'{P}{KEYREV}*{DKS}+(?:[{UID}{UAT}]{CERTREV}*{CERT}*)*(?:{K}{SUBREV}*{SUBBIND}+)*{PAD}?',
        'v6-revocation-certificate': f'{P}{KEYREV}',
        'v4-certificate': f'{P}{KEYREV}?{DKS}*(?:[{UID}{UAT}]{ANYSIG}*)*(?:{K}{SUBREV}*{SUBBIND}+)*',
        'v3-key': f'{P}{KEYREV}?{UID}{ANYSIG}*(?:{UID}{ANYSIG}*)*',
    }


def match_keys(pkts, errs, warns, secret):
    """§10.1, §10.2: split at each primary key and match each certificate."""
    certs, cur = [], []
    for p in pkts:
        if p['header']['type_id'] in (5, 6) and cur:
            certs.append(cur)
            cur = []
        cur.append(p)
    certs.append(cur)
    g = key_grammars(secret)
    names = []
    for c in certs:
        prim = c[0]['body']
        v = prim.get('version')
        cand = {6: ['v6-certificate', 'v6-revocation-certificate'], 4: ['v4-certificate'],
                3: ['v3-key'], 2: ['v3-key']}.get(v, [])
        s = ''.join(token(p) for p in c)
        hit = [n for n in cand if re.fullmatch(g[n], s)]
        if not hit:
            errs.append(f'key sequence does not match the {"/".join(cand) or "?"} grammar (§10.1): '
                        + ' '.join(f'{ord(ch):x}' for ch in s))
            names.append('?')
            continue
        names.append(hit[0] + (' (secret)' if any(p['header']['type_id'] in (5, 7) for p in c) else ''))
        check_cert_versions(c, v, errs, warns)
    return names


def check_cert_versions(c, v, errs, warns):                   # §10.1.1, §10.1.3, §10.1.4
    prim = c[0]['body']
    fp = fingerprint(v, bytes.fromhex(prim['_public_body']))
    if v == 6 and not any(p['header']['type_id'] == 2 and p['body'].get('sig_type') == 0x1F for p in c) \
            and len(c) != 2:
        errs.append('v6 key without a Direct Key signature (§5.2.3.10, R-0098)')
    for p in c[1:]:
        t, b = p['header']['type_id'], p['body']
        if t in (7, 14) and b.get('version') != v and v in (4, 6):
            errs.append(f'v{v} primary with a v{b.get("version")} subkey (§10.1.1 R-0312, §10.1.3 R-0318)')
        if t in (7, 14) and v in (2, 3):
            errs.append('version 3 keys MUST NOT have subkeys (§10.1.4, R-0321)')
        if t == 2 and b.get('version') in (4, 6):
            issuers = [sp['value']['fingerprint'] for sp in b['hashed'] + b['unhashed']
                       if sp['type_id'] == 33 and 'value' in sp]
            if v == 6 and fp in issuers and b['version'] != 6:
                errs.append('self-signature by a v6 key is not v6 (§10.1.1, R-0315)')
        if t == 2 and b.get('sig_type') == 0x18 and v == 4 and b.get('version') == 3:
            warns.append('v3 Subkey Binding signature: SHOULD be v4 (§10.1.3, R-0316)')


class Parse:
    """§10.3 recursive descent over packets (LL(1); see the ABNF)."""

    def __init__(self, pkts, errs, warns):
        self.p, self.errs, self.warns = pkts, errs, warns

    def t(self, i):
        return self.p[i]['header']['type_id'] if i < len(self.p) else None

    def message(self, i):
        t = self.t(i)
        if t in (1, 3, 9, 18):                       # Encrypted Message
            j = i
            while self.t(j) in (1, 3):
                j += 1
            if self.t(j) not in (9, 18):
                raise Malformed(f'ESK sequence not followed by encrypted data at packet {j}')
            self.align(i, j)
            return j + 1
        if t == 2:                                   # Signature Packet, OpenPGP Message
            return self.message(i + 1)
        if t == 4:                                   # One-Pass Signed Message
            j = self.message(i + 1)
            if self.t(j) != 2:
                raise Malformed(f'One-Pass Signed Message without its Signature at packet {j}')
            self.correspond(self.p[i]['body'], self.p[j]['body'])
            if self.p[i]['body'].get('nested') == 0 and self.t(i + 1) != 4:
                self.errs.append('OPS nested flag 0 but the next packet is not an OPS (§5.4)')
            return j + 1
        if t in (8, 11):
            return i + 1
        raise Malformed(f'packet {i} (type {t}) cannot start an OpenPGP Message')

    def align(self, i, j):                           # §10.3.2.1, Table 26
        enc = self.p[j]['body']
        payload = 'SED' if self.t(j) == 9 else f'v{enc.get("version")}'
        ok = {'SED': {(1, 3), (3, 4), (1, 2)}, 'v1': {(1, 3), (3, 4)}, 'v2': {(1, 6), (3, 6)}}[payload]
        for k in range(i, j):
            pair = (self.t(k), self.p[k]['body'].get('version'))
            if pair not in ok:
                self.warns.append(f'ESK packet {k} (type {pair[0]} v{pair[1]}) misaligned with {payload} '
                                  'payload: MUST be discarded (§10.3.2.1, R-0343)')

    def correspond(self, o, s):                      # §5.4, §10.3.2.2, Table 27
        if '_malformed' in s or '_malformed' in o:
            return
        if (o['version'], s['version']) not in {(3, 3), (3, 4), (6, 6)}:
            self.errs.append(f'OPS v{o["version"]} with Signature v{s["version"]} (Table 27, §5.2.5)')
        for f in ('sig_type', 'hash_algo', 'pk_algo'):
            if o[f] != s[f]:
                self.errs.append(f'OPS {f} {o[f]} != Signature {f} {s[f]} (§5.4)')
        if o['version'] == 6 and o.get('salt') != s.get('salt'):
            self.errs.append('OPS salt != Signature salt (§5.4, R-0185)')
        if s['version'] in (4, 6):
            fps = [sp['value']['fingerprint'] for sp in s['hashed'] + s['unhashed']
                   if sp['type_id'] == 33 and 'value' in sp]
            if o['version'] == 6 and fps and o['fingerprint'] not in fps:
                self.errs.append('OPS fingerprint != Issuer Fingerprint (§5.4)')


def classify(pkts, errs, warns, padding_anywhere=False):
    seq = [p for p in pkts if p['header']['type_id'] != 10 and p['header']['type_id'] < 40]  # Marker, non-critical
    if padding_anywhere:
        seq = [p for p in seq if p['header']['type_id'] != 21]
    if not seq:
        return 'empty'
    t0 = seq[0]['header']['type_id']
    if t0 in (5, 6):
        return 'keys: ' + ', '.join(match_keys(seq, errs, warns, any(p['header']['type_id'] in (5, 7) for p in seq)))
    if all(p['header']['type_id'] in (2, 21) for p in seq):       # §10.4: padding anywhere
        return 'detached signature(s)'
    ps = Parse(seq, errs, warns)
    try:
        end = ps.message(0)
        if end != len(seq):
            raise Malformed(f'{len(seq) - end} packet(s) after a complete OpenPGP Message')
    except Malformed as e:
        errs.append(f'OpenPGP Message grammar (§10.3): {e}')
        return 'message?'
    for p in seq:
        if p['header']['type_id'] == 8 and 'packets' in p['body']:
            inner = [q for q in p['body']['packets'] if q['header']['type_id'] != 10]
            try:
                ip = Parse(inner, errs, warns)
                if ip.message(0) != len(inner):
                    raise Malformed('trailing packets')
            except Malformed as e:
                errs.append(f'decompressed content is not an OpenPGP Message (§10.3.1, R-0333): {e}')
    return 'message'


# ------------------------------------------------------------------ driver
def strip_private(o):
    if isinstance(o, dict):
        return {k: strip_private(v) for k, v in o.items() if not k.startswith('_')}
    if isinstance(o, list):
        return [strip_private(v) for v in o]
    return o


def schema_errors(pkts):
    try:
        import jsonschema
    except ImportError:
        return None
    v = jsonschema.Draft202012Validator(json.load(open(SCHEMA)))
    return [f'{"/".join(map(str, e.absolute_path))}: {e.message[:200]}'
            for e in sorted(v.iter_errors(strip_private(pkts)), key=lambda e: list(map(str, e.absolute_path)))]


def run(label, data, show_json, padding_anywhere, notes):
    errs, warns = [], []
    try:
        pkts = read_packets(data, notes)
    except Malformed as e:
        print(f'  {label}: MALFORMED stream: {e}')
        return False
    for p in pkts:
        check_packet(p, errs, warns)
    kind = classify(pkts, errs, warns, padding_anywhere)
    se = schema_errors(pkts)
    print(f'  {label}: {len(pkts)} packets [{" ".join(token_name(p) for p in pkts)}] -> {kind}')
    if se is None:
        print('    schema: jsonschema not installed, skipped')
    else:
        print(f'    schema: {"valid" if not se else f"{len(se)} error(s)"}')
        for e in se[:10]:
            print('      ' + e)
    for p in pkts:
        if p['header']['type_id'] in (5, 6, 7, 14) and 'version' in p['body']:
            fp = fingerprint(p['body']['version'], bytes.fromhex(p['body']['_public_body']))
            if fp:
                print(f'    fingerprint v{p["body"]["version"]} {fp.upper()}')
    for n in notes + warns:
        print('    note: ' + n)
    for e in errs:
        print('    ERROR: ' + e)
    if show_json:
        print(json.dumps(strip_private(pkts), indent=1))
    return not errs and not se


NAMES = {1: 'PKESK', 2: 'SIG', 3: 'SKESK', 4: 'OPS', 5: 'SECKEY', 6: 'PUBKEY', 7: 'SECSUBKEY', 8: 'COMP',
         9: 'SED', 10: 'MARKER', 11: 'LIT', 12: 'TRUST', 13: 'UID', 14: 'PUBSUBKEY', 17: 'UAT',
         18: 'SEIPD', 21: 'PADDING'}


def token_name(p):
    t, b = p['header']['type_id'], p['body']
    n = NAMES.get(t, f'T{t}')
    if 'version' in b:
        n += f'v{b["version"]}'
    if t == 2 and 'sig_type' in b:
        n += f'(0x{b["sig_type"]:02X})'
    return n


def rfc_blocks(path):
    """Every armored block of Appendix A, with the RFC's 3-space indent removed."""
    lines = open(path, encoding='utf-8').read().splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith('Appendix A.  Test Vectors'))
    end = next(i for i, l in enumerate(lines) if l.startswith('Appendix B.'))
    sec, out, i = None, [], start
    while i < end:
        l = lines[i]
        if re.match(r'^A\.\d+(\.\d+)?\.  ', l):
            sec = l.split('  ')[0]
        if l.startswith('   -----BEGIN PGP '):
            j = i
            label = l.strip()[15:-5]
            closer = 'SIGNATURE' if label == 'SIGNED MESSAGE' else label
            while not lines[j].startswith(f'   -----END PGP {closer}-----'):
                j += 1
            out.append((f'{sec} line {i + 1}', '\n'.join(x[3:] for x in lines[i:j + 1])))
            i = j
        i += 1
    return out


def main(argv):
    show = '--json' in argv
    pad = '--padding-anywhere' in argv
    args = [a for a in argv if not a.startswith('--')]
    ok = True
    if '--rfc' in argv:
        for label, text in rfc_blocks(args[0]):
            notes = []
            for lab, data in dearmor(text, notes):
                ok &= run(f'{label} [{lab}]', data, show, pad, notes)
                notes = []
        print('ALL OK' if ok else 'FAILURES')
        return 0 if ok else 1
    for f in args:
        raw = open(f, 'rb').read()
        notes = []
        if raw.lstrip().startswith(b'-----BEGIN PGP '):
            for lab, data in dearmor(raw.decode('utf-8'), notes):
                ok &= run(f'{f} [{lab}]', data, show, pad, notes)
                notes = []
        else:
            ok &= run(f, raw, show, pad, notes)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

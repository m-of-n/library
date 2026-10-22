---
record: rfc-8747
kind: schema
title: "rfc-8747 — schemas"
extracted: "2026-10-21"
reviewed_by: ""
---

# RFC 8747 — schemas

**RFC 8747 ships no formal grammar of any kind.** Measured over the whole
683-line source: `schema`, `grammar`, `ABNF` and `ASN.1` occur **zero** times,
`JSON Schema` **zero** times, and `CDDL` **once** — at line 630, inside the
reference entry for RFC 8610, which this document cites for its Appendix G
diagnostic notation and nothing else. So every formal artifact here except the
verbatim capture is **ours**, and says so in its filename.

| file | what it is | verbatim or derived |
|---|---|---|
| `source-renderings.txt` | Table 1 (§3.1) and all four IANA blocks (§7.1.1, §7.2.1, §7.2.2), as exact source line runs with per-region `sha256` | **verbatim** |
| `cnf-claim.derived.cddl` | the `cnf` claim and its three confirmation methods as a CDDL grammar | **derived** |
| `cnf-claim.derived.schema.json` | the same over a declared lossy JSON projection; `$id: urn:library:rfc-8747:cnf-claim.derived` | **derived** |
| `confirmation-methods.derived.yaml` | both registries as machine-readable fields, each wired to its requirement id | **derived** |

The document's **complete** structured type model is Table 1's three data rows
plus the four IANA blocks. That is what `source-renderings.txt` holds, and it is
eighteen lines of table and sixty-six of registration template.

## Does the CDDL bind, or merely parse?

No `cddl` tool is installed here, so this is **not** a parse result. A checker
was transcribed from `cnf-claim.derived.cddl` rule by rule and run over ten
instances, four of them chosen to be rejected. `hazards.md` §7 is the reason:
`rfc-9360`'s derived CDDL parsed perfectly for two passes and constrained
nothing, because a `* label => any` wildcard in the same map satisfied every
item its rule rejected.

**The instance this grammar exists to reject**, written down before it was
tested:

```
{ 1: <COSE_Key>, 2: <COSE_Encrypt0> }
```

| instance | expected | got |
|---|---|---|
| §3.2's own `cnf` — `{1: COSE_Key}` | accept | **accept** |
| §3.3's own `cnf` — `{2: [protected, unprotected, ciphertext]}` | accept | **accept** |
| §3.4's own `cnf` — `{3: h'dfd1…'}` | accept | **accept** |
| `{3: kid, 5: …}` — an unknown member (key 5 is RFC 9679's `ckt`) | accept | **accept** |
| `{}` — the empty `cnf` | accept | **accept** |
| `{1: COSE_Key, 3: kid}` | accept | **accept** |
| **`{1: COSE_Key, 2: COSE_Encrypt0}`** | **reject** | **reject** |
| `{3: "dfd1aa97"}` — `kid` as a text string | **reject** | **reject** |
| `{2: COSE_Encrypt0, 1: "nonsense"}` | **reject** | **reject** |
| `{1: COSE_Key, 2: COSE_Encrypt0, 9: 1}` | **reject** | **reject** |

**10 of 10 behave as the grammar claims.** And the vacuity probe: a naive
rendering — optional entries for 1 and 2 beside an unrestricted `* label => any`
in the same map — **accepts all four** instances the real grammar rejects. Two
devices prevent that here, and both were tested rather than assumed:

1. **The cut operator `^ =>`** on every named entry, so a wrongly typed value
   under a known label cannot fall through to the wildcard.
2. **`other-label` excludes 1, 2 and 3 by construction** — written out as `0 /
   nint / (4 .. 18446744073709551615) / tstr`, because CDDL has no negation on
   literals. This is what stops the extension socket absorbing a *second* key
   representation.

### Where the cut is inert, said plainly

On keys **1 and 2** the cut currently bites on nothing, because RFC 8747 defines
no `COSE_Key`, `COSE_Encrypt` or `COSE_Encrypt0` grammar — §3.2 and §3.3 name
them and cite RFC 8152 — so those three rules are sockets typed `any`. For those
two labels the whole of the constraint is carried by `other-label`'s exclusion,
not by the cut. The cut does real work on key **3** alone, where Table 1 gives a
value type: it is what rejects `{3: "dfd1aa97"}`. Keeping `^ =>` on 1 and 2 is
deliberate anyway — the moment a later pass or a sibling record supplies a real
`COSE_Key` rule, the entry binds without being rewritten — but a reader should
not be left thinking it binds today.

### What the grammar deliberately does not constrain

- **The empty map.** rfc-8747#R-0023 — §3.1 puts the set
  of members a CWT must contain *outside the scope of this specification*, so
  `{}` is not excluded by this document.
- **`kid` beside a key representation.** §3.1 restricts `COSE_Key` against
  `Encrypted_COSE_Key` and says nothing about `kid`; rfc-8747#R-0040
  explicitly allows a `kid` *inside* a `COSE_Key`. Forbidding `{1: …, 3: …}`
  would be this library's rule, not the document's.
- **The tag on a `COSE_Encrypt0`.** rfc-8747#R-0117
  makes it optional and §3.3's example omits it, so **both** forms are admitted
  here. That is not neutrality, it is the finding: one `cnf` has two encodings
  and this registry entry does not choose between them. See `design-notes.md`.
- **Map entry order.** The words `canonical` and `deterministic` occur **zero**
  times in the source. `examples/vectors.yaml` records what that costs: the
  document's own §3.3 ciphertext does not reproduce from its own printed
  COSE_Key, because the two differ in entry order alone.

### The JSON Schema's projection is lossy, and declared

`cnf-claim.derived.schema.json` works over a JSON projection in which an integer
confirmation key becomes its decimal string and a CBOR byte string becomes
lowercase hex. CBOR distinguishes integer key `1` from text key `"1"` and JSON
cannot, so **that schema cannot express RFC 8747's key space** and the CDDL is
normative for this extraction. The one construct in it that genuinely binds is
the `not`/`required` pair encoding rfc-8747#R-0029.

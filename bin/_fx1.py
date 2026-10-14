"""_fx1 — the extraction-standard vintage, and the one trigger that reads it.

`distillation.profile` says HOW COMPLETELY a record was extracted.
`distillation.standard` — the vintage — says AGAINST WHAT. Without the second,
"complete" has a numerator and no denominator, and a record that was complete
under an older standard is indistinguishable from one that is half-finished
under the current one. That is library#73: eleven records legitimately
`distilled` before FX-1 existed (or under another library's practice, folded in
by #62) failed CI on every PR that touched them, whatever the PR did, because
`status: distilled` alone was read as "claims FX-1".

docs/extraction.md has always said older records are grandfathered until
someone extracts them. Nothing implemented it. This module does, as a
comparison: the record names a standard, the schema names the current one, and
a record naming an older one is held to the summary bar.

The trigger lived in three incompatible places (docs/extraction.md,
library/CLAUDE.md, schema/record.schema.yaml) and in one tool. It lives here
now, and the vintages are parsed from the schema rather than restated —
the same rule as bin/validate:bodies(), for the same reason.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _yaml import parse as miniyaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "schema" / "record.schema.yaml"

# Records of these types are extractable, so FX-1 can apply to them.
IN_SCOPE = {"rfc", "draft", "spec", "ietf"}
# A stub has not claimed anything yet.
STUB_OK = {"stub", "queued"}


def _standard_key():
    d = miniyaml(SCHEMA.read_text())
    k = (((d.get("fields") or {}).get("distillation") or {}).get("keys") or {}).get("standard")
    if not isinstance(k, dict):
        sys.exit(f"ERROR {SCHEMA}:fields.distillation.keys.standard is missing")
    return k


def current():
    """The extraction standard of the day, e.g. 'FX-1'."""
    c = str(_standard_key().get("current") or "").strip()
    if not c:
        sys.exit(f"ERROR {SCHEMA}:fields.distillation.keys.standard.current is not set")
    return c


def standards():
    """Every vintage a record may legally name."""
    v = _standard_key().get("values")
    if not isinstance(v, list) or not v:
        sys.exit(f"ERROR {SCHEMA}:fields.distillation.keys.standard.values is not a "
                 f"non-empty list — it must stay a BLOCK sequence; miniyaml cannot "
                 f"read a flow list")
    return v


def vintage(d, cur=None):
    """The standard this record's completeness claim is measured against.

    Omitted means the current one: new work is measured against the standard of
    the day, so forgetting the field fails closed rather than open.
    """
    dist = d.get("distillation") if isinstance(d.get("distillation"), dict) else None
    return str((dist or {}).get("standard") or (cur or current())).strip()


def trigger(d, extracting=False, cur=None):
    """Why FX-1 applies to this record, or None if it does not.

    `extracting` is True when the PR under review adds to or changes the
    record's `distilled/`.

    Returns one of:
      'extracting'     the PR is extracting now — the vintage does not excuse it
      'distilled'      the record claims the current standard
      'declared'       a distillation block declares the current standard
      None             held to the summary bar

    Grandfathering is deliberately NOT a licence to edit `distilled/`. Touching
    the artifacts is extraction, and extraction is measured against the current
    standard whatever the record used to claim. That keeps the ratchet: an
    extracted record can never regress to a summary, and a grandfathered one
    cannot grow artifacts that quietly miss the bar.
    """
    cur = cur or current()
    if d.get("type") not in IN_SCOPE or d.get("status") in STUB_OK:
        return None
    if extracting:
        return "extracting"
    if vintage(d, cur) != cur:
        return None                       # grandfathered — docs/extraction.md
    if d.get("status") == "distilled":
        return "distilled"
    if isinstance(d.get("distillation"), dict):
        return "declared"
    return None

"""The SKILL.md contract.

A skill is run by a model, so its guarantees live in the markdown. These tests
hold the file to its own promises — the same properties tools/validate_skill.py
checks, kept here so a contributor running pytest sees them too.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"


def _split():
    text = SKILL.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, "frontmatter must be present and delimited"
    return yaml.safe_load(m.group(1)), text[m.end():]


def test_canonical_filename():
    assert SKILL.exists(), "SKILL.md must exist at the repository root"


def test_frontmatter_fields():
    fm, _ = _split()
    for f in ("name", "description"):
        assert f in fm
    for f in ("license", "version"):
        assert f in fm
    assert str(fm["license"]).lower().replace(" ", "-") == "apache-2.0"


def test_name_is_slug_safe():
    fm, _ = _split()
    assert re.fullmatch(r"[a-z0-9][a-z0-9-]*", str(fm["name"]))


def test_metadata_bounds_scope():
    fm, _ = _split()
    meta = fm.get("metadata", {})
    assert meta.get("compatibility")
    assert meta.get("not_for")


def test_body_requires_uncertainty_and_counter_argument():
    _, body = _split()
    assert re.search(r"uncertaint|confidence", body, re.I)
    assert re.search(r"counter.?argument|skeptic|self.?crit", body, re.I)
    assert re.search(r"invalidat", body, re.I)


def test_body_degrades_honestly():
    _, body = _split()
    assert re.search(r"insufficient|abstain|unknown", body, re.I)


def test_body_defers_markets_to_money_atlas():
    _, body = _split()
    # Scope boundary: this is not a markets skill and says so, by name.
    assert "money-atlas-intelligence-os" in body

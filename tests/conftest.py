"""Shared test setup for Genesis Mind.

Puts the repository root on sys.path so tests can import the reasoning engines
(first_principle_codex, decision_engine, risk_model, core/*) directly, without
installing the package.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

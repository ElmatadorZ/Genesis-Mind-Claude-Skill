"""First Principle Codex — the reasoning kernel.

It reduces a phenomenon to atomic truths, frames a problem, generates options,
scores them across frames of reference, and selects the highest-leverage one.
These tests lock that machinery: the epistemic filter, the ordering discipline
(you cannot generate options before framing the problem), the frame heuristics,
and the selection rule.
"""
from __future__ import annotations

import pytest

from first_principle_codex import (
    AtomicTruth,
    FirstPrincipleCodex,
    OptionPlan,
    ProblemTruths,
)


def test_default_atomics_loaded():
    codex = FirstPrincipleCodex()
    # The base First Principles must be present — they are what everything else
    # is reduced to.
    assert {"causation", "leverage", "compounding", "feedback"} <= set(codex.atomics)


def test_kalama_filter_drops_rumor():
    codex = FirstPrincipleCodex()
    kept = codex.kalama_filter(["ราคาปิดที่ 100", "เขาว่าจะขึ้น", "ข่าวลือว่าเจ๊ง"])
    # Rumor-tagged observations are filtered; grounded ones survive.
    assert kept == ["ราคาปิดที่ 100"]


def test_generate_options_requires_problem_first():
    codex = FirstPrincipleCodex()
    # Ordering discipline: no options before the problem is framed.
    with pytest.raises(ValueError):
        codex.generate_options("finance_entropy_behavior")


def test_define_problem_truths_shape():
    codex = FirstPrincipleCodex()
    pt = codex.define_problem_truths("surface_thinking")
    assert isinstance(pt, ProblemTruths)
    assert pt.problem == "surface_thinking"
    assert pt.paths and all("surface_thinking" in p for p in pt.paths)


def test_derive_core_truths_falls_back_when_no_match():
    codex = FirstPrincipleCodex()
    # A phenomenon that matches nothing still yields a minimal explanatory set,
    # never an empty one — the kernel must always give the model something to reason on.
    truths = codex.derive_core_truths("zzz_nomatch_zzz")
    assert 1 <= len(truths) <= len(codex.atomics)


def test_generate_options_respects_cap():
    codex = FirstPrincipleCodex()
    codex.define_problem_truths("p")
    opts = codex.generate_options("leverage_information_feedback", max_options=5)
    assert 0 < len(opts) <= 5
    assert all(isinstance(o, OptionPlan) for o in opts)


def test_self_now_frame_prefers_simplicity():
    codex = FirstPrincipleCodex()
    lean = OptionPlan(atoms=[AtomicTruth("leverage", "x")], description="")
    heavy = OptionPlan(
        atoms=[AtomicTruth("leverage", "x"), AtomicTruth("feedback", "y"),
               AtomicTruth("entropy", "z")],
        description="",
    )
    # "self_now" rewards what is executable immediately — fewer moving parts scores higher.
    assert (codex.evaluate_option_in_frame(lean, "self_now")
            > codex.evaluate_option_in_frame(heavy, "self_now"))


def test_long_horizon_frame_rewards_compounding():
    codex = FirstPrincipleCodex()
    with_comp = OptionPlan(
        atoms=[AtomicTruth("compounding", "c"), AtomicTruth("leverage", "l")],
        description="",
    )
    without = OptionPlan(
        atoms=[AtomicTruth("information", "i"), AtomicTruth("incentives", "n")],
        description="",
    )
    # Over a 10-year frame, compounding + leverage must beat an equally-sized option
    # that has neither.
    assert (codex.evaluate_option_in_frame(with_comp, "self_10y")
            > codex.evaluate_option_in_frame(without, "self_10y"))


def test_select_best_returns_an_option():
    codex = FirstPrincipleCodex()
    codex.define_problem_truths("retail_investors_lose_money")
    options = codex.generate_options("finance_entropy_investor_behavior")
    best = codex.select_best_option(options)
    assert isinstance(best, OptionPlan)
    # selection populates the per-frame scores and the system simulation.
    assert best.score_by_frame
    assert best.problem_reduction >= 0.0

"""Decision selection and risk classification.

Small, deterministic, and load-bearing: the decision engine must pick the most
confident option and be able to explain why, and the risk model must classify
downside at the right thresholds and gate action on probability.
"""
from __future__ import annotations

from decision_engine import DecisionEngine
from risk_model import RiskModel


def test_decision_picks_most_confident():
    eng = DecisionEngine()
    decisions = [
        {"identity": "Analyst", "confidence": 0.55},
        {"identity": "Strategist", "confidence": 0.81},
        {"identity": "Skeptic", "confidence": 0.60},
    ]
    assert eng.choose(decisions)["identity"] == "Strategist"


def test_synthesize_reason_joins_all_voices():
    eng = DecisionEngine()
    decisions = [{"identity": "Analyst"}, {"identity": "Skeptic"}]
    # The synthesized reason preserves every voice, not just the winner — the
    # council's dissent is part of the record.
    assert eng.synthesize_reason(decisions) == "Analyst | Skeptic"


def test_risk_classify_thresholds():
    r = RiskModel()
    assert r.classify(0.8) == "HIGH RISK"      # > 0.7
    assert r.classify(0.5) == "MEDIUM RISK"    # > 0.4
    assert r.classify(0.2) == "LOW RISK"


def test_risk_classify_boundaries_are_strict():
    r = RiskModel()
    # Exactly on a boundary falls to the lower band — 0.7 is not yet HIGH.
    assert r.classify(0.7) == "MEDIUM RISK"
    assert r.classify(0.4) == "LOW RISK"


def test_should_act_respects_threshold():
    r = RiskModel()
    assert r.should_act(0.6) is True           # meets the default 0.6
    assert r.should_act(0.59) is False
    assert r.should_act(0.9, threshold=0.95) is False

# decision_engine.py

from dataclasses import dataclass
from typing import List, Dict, Any
import math


@dataclass
class Option:
    name: str
    upside: float      # 0-1
    downside: float    # 0-1
    probability: float # 0-1
    reversibility: float # 0-1


@dataclass
class Decision:
    chosen: str
    confidence: float
    reasoning: str
    risk: str


class DecisionEngine:

    def __init__(self, risk_tolerance: float = 0.5):
        self.risk_tolerance = risk_tolerance

    def evaluate(self, options: List[Option]) -> Decision:
        scores = []

        for opt in options:
            expected_value = (opt.upside * opt.probability) - (opt.downside * (1 - opt.probability))

            # Reversibility bonus (Jeff Bezos principle)
            rev_bonus = opt.reversibility * 0.2

            # Risk penalty
            risk_penalty = opt.downside * (1 - self.risk_tolerance)

            score = expected_value + rev_bonus - risk_penalty

            scores.append((score, opt))

        scores.sort(key=lambda x: x[0], reverse=True)
        best_score, best_option = scores[0]

        confidence = min(0.95, max(0.55, best_score + 0.5))

        return Decision(
            chosen=best_option.name,
            confidence=confidence,
            reasoning=f"Selected based on highest EV with reversibility factor",
            risk=f"Downside={best_option.downside}, Probability uncertainty={1-best_option.probability}"
        )

"""
MATADOR CORE v1
---------------
Alpha Extraction System

Combines:
- First Principles
- Compound Intelligence
- Multi-Agent System
- Risk-first Finance Thinking
"""

from dataclasses import dataclass, field
from typing import List, Dict, Callable
import math
import random


# ==============================
# 1. FIRST PRINCIPLE ENGINE
# ==============================

class FirstPrincipleEngine:
    def evaluate(self, idea: str) -> float:
        score = 0

        keywords = {
            "liquidity": 1.5,
            "risk": 1.4,
            "leverage": 1.3,
            "volatility": 1.2,
            "behavior": 1.1,
            "macro": 1.3
        }

        for k, v in keywords.items():
            if k in idea.lower():
                score += v

        return score


# ==============================
# 2. COMPOUND INTELLIGENCE
# ==============================

@dataclass
class Node:
    idea: str
    depth: int = 0
    score: float = 0.0
    children: List["Node"] = field(default_factory=list)

    def expand(self, generator, max_depth=3):
        if self.depth >= max_depth:
            return

        ideas = generator(self.idea)

        for idea in ideas:
            child = Node(idea, self.depth + 1)
            self.children.append(child)
            child.expand(generator, max_depth)


class CompoundEngine:
    def __init__(self, evaluator):
        self.evaluator = evaluator

    def run(self, seed: str):
        root = Node(seed)

        def generator(idea):
            return [
                f"{idea} driven by liquidity shift",
                f"{idea} under high volatility",
                f"{idea} influenced by market behavior",
                f"{idea} with macro pressure"
            ]

        root.expand(generator)
        self._score(root)

        return self._best(root)

    def _score(self, node):
        node.score = self.evaluator.evaluate(node.idea)
        for c in node.children:
            self._score(c)

    def _best(self, node):
        best = node
        for c in node.children:
            candidate = self._best(c)
            if candidate.score > best.score:
                best = candidate
        return best


# ==============================
# 3. COSMIC PERSPECTIVE ENGINE
# ==============================

class CosmicEngine:
    def evaluate(self, idea: str):
        frames = {
            "short_term": len(idea) * 0.3,
            "long_term": math.log(len(idea)+1) * 2,
            "market": len(idea.split()) * 1.2,
            "system": len(set(idea.split())) * 1.5
        }
        return frames


# ==============================
# 4. SHADOW ENGINE (RISK)
# ==============================

class ShadowEngine:
    def analyze(self, idea: str):
        risks = []

        if "volatility" in idea:
            risks.append("High volatility risk")

        if "leverage" in idea:
            risks.append("Liquidation risk")

        if "macro" in idea:
            risks.append("Macro uncertainty")

        return risks


# ==============================
# 5. AGENTS
# ==============================

class Analyst:
    def run(self, problem):
        return f"Market context: {problem}"


class Strategist:
    def run(self, idea):
        return f"Strategy: Exploit {idea}"


class Skeptic:
    def run(self, idea):
        return f"Counter: What if {idea} fails?"


class Executor:
    def run(self, idea):
        return f"Execution Plan: Position sizing based on {idea}"


# ==============================
# 6. MATADOR CORE
# ==============================

class MatadorCore:
    def __init__(self):
        self.fp = FirstPrincipleEngine()
        self.compound = CompoundEngine(self.fp)
        self.cosmic = CosmicEngine()
        self.shadow = ShadowEngine()

        self.analyst = Analyst()
        self.strategist = Strategist()
        self.skeptic = Skeptic()
        self.executor = Executor()

    def think(self, problem: str):
        context = self.analyst.run(problem)

        best = self.compound.run(problem)

        perspective = self.cosmic.evaluate(best.idea)

        risk = self.shadow.analyze(best.idea)

        strategy = self.strategist.run(best.idea)
        counter = self.skeptic.run(best.idea)
        execution = self.executor.run(best.idea)

        confidence = self._confidence(best.score, risk)

        return {
            "context": context,
            "best_idea": best.idea,
            "score": best.score,
            "perspective": perspective,
            "risk": risk,
            "strategy": strategy,
            "counter": counter,
            "execution": execution,
            "confidence": confidence
        }

    def _confidence(self, score, risks):
        base = min(score / 5, 1.0)
        penalty = len(risks) * 0.1
        return max(base - penalty, 0)


# ==============================
# RUN
# ==============================

if __name__ == "__main__":
    core = MatadorCore()

    result = core.think("Bitcoin drops due to macro uncertainty")

    print("\n=== MATADOR OUTPUT ===\n")
    for k, v in result.items():
        print(f"{k}: {v}")

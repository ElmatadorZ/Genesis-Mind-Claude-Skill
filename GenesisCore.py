"""
GENESIS INTELLIGENCE CORE
------------------------
Unifies:
- First Principle Codex (Truth Engine)
- Compound Genius (Expansion Engine)
- Cosmic Mind (Perspective Engine)

Creator: Bunyawat Dechanon (Money Atlas)
"""

from dataclasses import dataclass, field
from typing import List, Dict, Callable
import math


# ==============================
# 1. FIRST PRINCIPLE LAYER
# ==============================

@dataclass
class AtomicTruth:
    key: str
    weight: float


class FirstPrincipleEngine:
    def __init__(self):
        self.truths = {
            "causation": AtomicTruth("causation", 1.0),
            "leverage": AtomicTruth("leverage", 1.2),
            "entropy": AtomicTruth("entropy", 0.8),
            "feedback": AtomicTruth("feedback", 1.1),
        }

    def evaluate(self, idea: str) -> float:
        score = 0
        for k, v in self.truths.items():
            if k in idea.lower():
                score += v.weight
        return score


# ==============================
# 2. COMPOUND GENIUS (UPGRADED)
# ==============================

@dataclass
class GeniusNode:
    idea: str
    depth: int = 0
    score: float = 0.0
    children: List["GeniusNode"] = field(default_factory=list)

    def expand(self, generator: Callable[[str], List[str]], max_depth=3):
        if self.depth >= max_depth:
            return

        new_ideas = generator(self.idea)

        for idea in new_ideas:
            node = GeniusNode(idea, self.depth + 1)
            self.children.append(node)
            node.expand(generator, max_depth)


class CompoundGeniusEngine:
    def __init__(self, evaluator):
        self.evaluator = evaluator

    def run(self, seed: str):
        root = GeniusNode(seed)

        def generator(idea):
            return [
                f"{idea} with leverage",
                f"{idea} with feedback loop",
                f"{idea} optimized against entropy",
            ]

        root.expand(generator)

        self._score_tree(root)
        best = self._select_best(root)

        return best

    def _score_tree(self, node):
        node.score = self.evaluator.evaluate(node.idea)
        for c in node.children:
            self._score_tree(c)

    def _select_best(self, node):
        best = node
        for c in node.children:
            candidate = self._select_best(c)
            if candidate.score > best.score:
                best = candidate
        return best


# ==============================
# 3. COSMIC MIND (REAL VERSION)
# ==============================

class CosmicMindEngine:
    def __init__(self):
        self.frames = ["self_now", "future", "market", "system"]

    def evaluate(self, idea: str) -> Dict[str, float]:
        scores = {}
        for f in self.frames:
            scores[f] = self._score_frame(idea, f)
        return scores

    def _score_frame(self, idea, frame):
        base = len(idea.split())

        if frame == "future":
            return math.log(1 + base) * 2
        if frame == "system":
            return base * 0.8
        return base * 0.5


# ==============================
# 4. GENESIS CORE
# ==============================

class GenesisCore:
    def __init__(self):
        self.fp = FirstPrincipleEngine()
        self.cg = CompoundGeniusEngine(self.fp)
        self.cm = CosmicMindEngine()

    def think(self, problem: str):
        # Step 1: Expand ideas
        best_idea = self.cg.run(problem)

        # Step 2: Evaluate perspectives
        perspective = self.cm.evaluate(best_idea.idea)

        return {
            "problem": problem,
            "best_idea": best_idea.idea,
            "score": best_idea.score,
            "perspective": perspective,
        }


# ==============================
# RUN
# ==============================

if __name__ == "__main__":
    core = GenesisCore()

    result = core.think("investor loses money due to poor decisions")

    print("=== GENESIS OUTPUT ===")
    for k, v in result.items():
        print(k, ":", v)

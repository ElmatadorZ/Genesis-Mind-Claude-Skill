# genesis_core.py

from typing import Any, Dict, List
from dataclasses import dataclass

# ===== IMPORT CORE MODULES =====
from decision_engine import DecisionEngine, Option
from decision_memory import DecisionMemory
from risk_model import RiskModel


# =========================================================
# 🧠 MEMORY SYSTEM
# =========================================================

class Memory:
    def __init__(self):
        self.store = []

    def add(self, key: str, value: Any, tags=None, strength: float = 0.5):
        self.store.append({
            "key": key,
            "value": value,
            "tags": tags or [],
            "strength": strength
        })

    def query(self, tag: str):
        return [item for item in self.store if tag in item["tags"]]


# =========================================================
# 🧬 CONTEXT
# =========================================================

class Context:
    def __init__(self):
        self.memory = Memory()
        self.decision_memory = DecisionMemory()
        self.risk_model = RiskModel()


# =========================================================
# 🧠 AGENTS
# =========================================================

class DecomposerAgent:
    name = "Decomposer"

    def run(self, ctx: Context, task: str):
        return {
            "problem": task,
            "intent": "decision_required"
        }


class AnalystAgent:
    name = "Analyst"

    def run(self, ctx: Context, data: Dict):
        problem = data["problem"]

        insight = {
            "insight": f"Core problem = {problem}",
            "uncertainty": 0.4,
            "assumptions": [
                "Market conditions unknown",
                "Outcome probabilistic"
            ]
        }

        ctx.memory.add("analysis", insight, tags=["analysis"], strength=0.6)

        return {**data, **insight}


class SynthesizerAgent:
    name = "Synthesizer"

    def run(self, ctx: Context, data: Dict):
        # Placeholder (replace with LLM later)
        options = [
            Option("Expand Now", 0.8, 0.6, 0.6, 0.5),
            Option("Wait", 0.5, 0.2, 0.5, 0.9),
        ]

        ctx.memory.add("options", options, tags=["options"], strength=0.7)

        return {**data, "options": options}


class ShadowAgent:
    name = "Shadow"

    def run(self, ctx: Context, data: Dict):
        reflections = []

        for opt in data["options"]:
            reflections.append(
                f"What if '{opt.name}' fails despite expected upside?"
            )

        ctx.memory.add("shadow", reflections, tags=["shadow"], strength=0.8)

        return {**data, "shadow_reflections": reflections}


class RiskAgent:
    name = "Risk"

    def run(self, ctx: Context, data: Dict):
        risk_profile = []

        for opt in data["options"]:
            risk = ctx.risk_model.classify(opt.downside)
            risk_profile.append((opt.name, risk))

        ctx.memory.add("risk", risk_profile, tags=["risk"], strength=0.7)

        return {**data, "risk_profile": risk_profile}


class DecisionAgent:
    name = "Decision"

    def __init__(self):
        self.engine = DecisionEngine(risk_tolerance=0.6)

    def run(self, ctx: Context, data: Dict):
        decision = self.engine.evaluate(data["options"])

        ctx.memory.add("decision", decision, tags=["decision"], strength=0.9)

        return {**data, "decision": decision}


class OutputAgent:
    name = "Output"

    def run(self, ctx: Context, data: Dict):
        decision = data["decision"]

        return {
            "problem": data["problem"],
            "decision": decision.chosen,
            "confidence": round(decision.confidence, 2),
            "reasoning": decision.reasoning,
            "risk": decision.risk,
            "shadow_insight": data.get("shadow_reflections", []),
            "risk_profile": data.get("risk_profile", [])
        }


# =========================================================
# ⚔️ GENESIS CORE ENGINE
# =========================================================

class GenesisMind:

    def __init__(self):
        self.ctx = Context()

        self.pipeline = [
            DecomposerAgent(),
            AnalystAgent(),
            SynthesizerAgent(),
            ShadowAgent(),     # 👁️ doubt layer
            RiskAgent(),       # ⚠️ risk awareness
            DecisionAgent(),   # ⚔️ action
            OutputAgent()
        ]

    def run(self, task: str) -> Dict[str, Any]:
        data: Any = task

        for agent in self.pipeline:
            data = agent.run(self.ctx, data)

        return data

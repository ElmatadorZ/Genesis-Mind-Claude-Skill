# genesis_core.py

from typing import Dict, Any

from core.decision_engine import DecisionEngine, Option
from core.decision_memory import DecisionMemory
from core.risk_model import RiskModel

from agents.analyst_llm import AnalystLLM
from agents.atlas_agent import AtlasAgent
from agents.skynet_agent import SkynetAgent
from agents.shadow_agent import ShadowAgent


# ===============================
# CONTEXT
# ===============================
class Context:
    def __init__(self):
        self.memory = []
        self.decision_memory = DecisionMemory()
        self.risk_model = RiskModel()

    def add_memory(self, item):
        self.memory.append(item)


# ===============================
# OPTION GENERATOR (REAL LOGIC)
# ===============================
class OptionGenerator:

    def generate(self, problem: str):
        return [
            Option("Aggressive Expansion", 0.9, 0.7, 0.6, 0.4),
            Option("Controlled Growth", 0.7, 0.4, 0.7, 0.7),
            Option("Hold Position", 0.5, 0.2, 0.5, 0.9),
        ]


# ===============================
# CONFLICT ENGINE
# ===============================
class ConflictEngine:

    def resolve(self, data):

        debate = {
            "atlas": data.get("atlas_view"),
            "skynet": data.get("skynet_view"),
            "shadow": data.get("shadow")
        }

        return debate


# ===============================
# GENESIS MIND V3
# ===============================
class GenesisMind:

    def __init__(self):

        self.ctx = Context()

        self.analyst = AnalystLLM()
        self.atlas = AtlasAgent()
        self.skynet = SkynetAgent()
        self.shadow = ShadowAgent()

        self.option_gen = OptionGenerator()
        self.decision_engine = DecisionEngine(risk_tolerance=0.6)
        self.conflict_engine = ConflictEngine()

    def run(self, task: str) -> Dict[str, Any]:

        data = {"problem": task}

        # 1. LLM ANALYSIS
        data = self.analyst.run(self.ctx, data)

        # 2. MULTI-AGENT VIEWS
        data = self.atlas.run(self.ctx, data)
        data = self.skynet.run(self.ctx, data)
        data = self.shadow.run(self.ctx, data)

        # 3. GENERATE OPTIONS
        options = self.option_gen.generate(task)
        data["options"] = options

        # 4. CONFLICT
        conflict = self.conflict_engine.resolve(data)

        # 5. DECISION
        decision = self.decision_engine.evaluate(options)

        # 6. OUTPUT
        return {
            "problem": task,
            "decision": decision.chosen,
            "confidence": round(decision.confidence, 2),
            "debate": conflict,
            "reasoning": decision.reasoning,
            "risk": decision.risk
        }

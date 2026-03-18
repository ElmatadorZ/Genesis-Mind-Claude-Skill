from core.first_principle import FirstPrinciple
from core.system_thinking import SystemThinking
from core.shadow_engine import ShadowEngine

class MatadorCore:
    def __init__(self):
        self.fp = FirstPrinciple()
        self.system = SystemThinking()
        self.shadow = ShadowEngine()

    def run(self, problem):
        fp = self.fp.analyze(problem)
        system = self.system.analyze(problem)
        risk = self.shadow.analyze(problem)

        return {
            "truth": fp["truth"],
            "system": system,
            "risk": risk,
            "confidence": 0.65
        }

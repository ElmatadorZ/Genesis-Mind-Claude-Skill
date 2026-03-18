class FirstPrinciple:
    def analyze(self, problem):
        return {
            "truth": "reduced core truth",
            "incentive": "who benefits",
            "risk": "uncertainty present"
        }


class SystemThinking:
    def analyze(self, problem):
        return {
            "actors": ["A", "B"],
            "flows": ["money", "data"],
            "loop": "feedback loop"
        }


class CompoundMind:
    def analyze(self, problem):
        return {
            "logical": "rational analysis",
            "strategic": "power leverage",
            "psychological": "human behavior",
            "probabilistic": "uncertainty model"
        }


class CosmicMind:
    def analyze(self, problem):
        return {
            "macro": "global pattern",
            "cycle": "repeating structure"
        }


class ShadowGenesis:
    def reflect(self, result):
        return {
            "bias_check": "possible bias detected",
            "missing": "unknown variables"
        }


class AgentBuilder:
    def create(self, problem):
        return {
            "agent_name": "CustomAgent",
            "role": "solve sub-problem",
            "method": "specialized logic"
        }


class GenesisMind:

    def __init__(self):
        self.fp = FirstPrinciple()
        self.system = SystemThinking()
        self.compound = CompoundMind()
        self.cosmic = CosmicMind()
        self.shadow = ShadowGenesis()
        self.builder = AgentBuilder()

    def run(self, problem):

        fp = self.fp.analyze(problem)
        system = self.system.analyze(problem)
        compound = self.compound.analyze(problem)
        cosmic = self.cosmic.analyze(problem)

        synthesis = {
            "truth": fp,
            "system": system,
            "perspective": compound,
            "macro": cosmic
        }

        reflection = self.shadow.reflect(synthesis)

        agent = self.builder.create(problem)

        return {
            "analysis": synthesis,
            "reflection": reflection,
            "new_agent": agent
        }


if __name__ == "__main__":
    gm = GenesisMind()
    result = gm.run("global conflict over oil")
    print(result)

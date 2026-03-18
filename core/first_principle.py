class FirstPrinciple:
    def analyze(self, problem):
        assumptions = [
            f"{problem} depends on macro",
            f"{problem} driven by behavior",
            f"{problem} affected by liquidity"
        ]

        broken = [f"Is it always true: {a}?" for a in assumptions]

        truth = f"Core truth of {problem}"

        return {
            "assumptions": assumptions,
            "challenge": broken,
            "truth": truth
        }

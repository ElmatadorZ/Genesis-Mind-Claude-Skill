class SystemThinking:
    def analyze(self, problem):
        return {
            "variables": ["price", "liquidity", "sentiment"],
            "relationships": "liquidity → price → sentiment",
            "feedback": "positive loop in bull, negative in crash"
        }

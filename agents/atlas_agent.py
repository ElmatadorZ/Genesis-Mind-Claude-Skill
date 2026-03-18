# atlas_agent.py

class AtlasAgent:

    name = "Atlas"

    def run(self, ctx, data):

        return {
            **data,
            "atlas_view": "Long-term, probability-weighted, capital preservation focused."
        }

# shadow_agent.py

class ShadowAgent:

    name = "Shadow"

    def run(self, ctx, data):

        reflections = [
            "What if all assumptions are wrong?",
            "What if inaction is the real risk?"
        ]

        ctx.memory.add("shadow", reflections, tags=["shadow"], strength=0.8)

        return {**data, "shadow": reflections}

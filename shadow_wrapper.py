# shadow_wrapper.py

class ShadowWrapper:

    def __init__(self, shadow):
        self.shadow = shadow

    def apply(self, context: str) -> str:
        return self.shadow.observe(context)

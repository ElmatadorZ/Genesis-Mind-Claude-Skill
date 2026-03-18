
# decision_engine.py

from typing import Dict, Any, List


class DecisionEngine:

    def choose(self, decisions: List[Dict[str, Any]]) -> Dict[str, Any]:
        # เลือกตัวที่ confidence สูงสุด
        best = max(decisions, key=lambda x: x["confidence"])
        return best

    def synthesize_reason(self, decisions: List[Dict[str, Any]]) -> str:
        return " | ".join([d["identity"] for d in decisions])

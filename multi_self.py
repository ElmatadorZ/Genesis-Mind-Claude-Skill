# multi_self.py

from typing import List, Dict, Any
from identity_core import IdentityCore


class MultiSelfSystem:

    def __init__(self):
        self.identities: List[IdentityCore] = self._load_identities()

    def _load_identities(self) -> List[IdentityCore]:
        return [
            IdentityCore("Skynet", {
                "risk": "aggressive",
                "values": ["speed", "dominance"]
            }),
            IdentityCore("Atlas", {
                "risk": "conservative",
                "values": ["stability", "probability"]
            }),
            IdentityCore("Eidolon", {
                "risk": "adaptive",
                "values": ["uncertainty", "exploration"]
            })
        ]

    def evaluate(self, base_decision: Dict[str, Any]) -> List[Dict[str, Any]]:
        results = []
        for identity in self.identities:
            modified = identity.influence(base_decision.copy())
            results.append(modified)
        return results

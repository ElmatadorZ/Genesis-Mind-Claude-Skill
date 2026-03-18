# decision_memory.py

from dataclasses import dataclass
from typing import List


@dataclass
class DecisionLog:
    choice: str
    outcome: float  # -1 to +1
    context: str


class DecisionMemory:

    def __init__(self):
        self.logs: List[DecisionLog] = []

    def add(self, choice: str, outcome: float, context: str):
        self.logs.append(DecisionLog(choice, outcome, context))

    def learn_bias(self):
        score = sum(log.outcome for log in self.logs)

        if score > 2:
            return "AGGRESSIVE"
        elif score < -2:
            return "DEFENSIVE"
        return "NEUTRAL"

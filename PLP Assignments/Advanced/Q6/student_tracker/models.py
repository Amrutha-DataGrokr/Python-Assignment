from dataclasses import dataclass

@dataclass
class Student:
    name: str
    scores: list[float]

    @property
    def average(self) -> float:
        return sum(self.scores) / len(self.scores)
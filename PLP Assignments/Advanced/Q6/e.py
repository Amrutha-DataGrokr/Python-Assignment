#e) Predict the output
from dataclasses import dataclass
from typing import List


@dataclass
class Student:
    name: str
    scores: List[float]

    @property
    def average(self):
        return sum(self.scores) / len(self.scores)

s = Student("Ravi", [80, 90, 70, 85])

print(s.name, round(s.average, 1), isinstance(s, Student))
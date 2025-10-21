# 20237451 - Nguyen Huu Kien

from functools import total_ordering
from IComparable import IComparable
from typing import Any

@total_ordering
class Student(IComparable):
    def __init__(self, name: str, gpa: float):
        super().__init__()

        if not isinstance(gpa, (float, int)):
            raise TypeError("GPA mus be a number")
        elif not (0.0 <= float(gpa) <= 4.0):
            raise ValueError("GPA must be in range 0.0 -> 4.0")

        self.name = name
        self.gpa = gpa

    def compare_to(self, other):
        if not isinstance(other, Student):
            raise TypeError("compare_to expects a Student instance")
        
        if self.gpa > other.gpa: 
            return 1
        elif self.gpa < other.gpa:
            return -1
        return 0
    
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.compare_to(other) == 0

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.compare_to(other) < 0

    def __str__(self) -> str:
        return f"Student(name={self.name}, gpa={self.gpa:.2f})"

    
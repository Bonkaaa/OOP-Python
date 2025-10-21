# 20237451 - Nguyen Huu Kien

from abc import ABC, abstractmethod

class IComparable(ABC):

    @abstractmethod
    def compare_to(self, other) -> int:
        pass
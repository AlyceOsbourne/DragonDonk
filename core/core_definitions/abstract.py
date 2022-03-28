from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict



class Inventory(ABC):

    @property
    @abstractmethod
    def items(self) -> Dict[Item, int]:
        ...

    @property
    @abstractmethod
    def max_size(self) -> int:
        ...

    @property
    @abstractmethod
    def max_weight(self) -> int:
        ...

    @property
    @abstractmethod
    def size(self) -> int:
        ...

    @property
    @abstractmethod
    def weight(self) -> int:
        ...

    @property
    @abstractmethod
    def gold(self) -> int:
        ...

class Effect(ABC):
    pass

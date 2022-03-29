from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod
from enum import Enum, auto
from typing import Dict, List

from core.core_definitions.abstract import Effect
from core.core_definitions.items import Equipment, Inventory


class Skill(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def description(self) -> str:
        ...

    @property
    @abstractmethod
    def effect(self) -> Effect:
        ...


class Stat(Enum):
    STRENGTH = auto()
    DEXTERITY = auto()
    CONSTITUTION = auto()
    INTELLIGENCE = auto()
    WISDOM = auto()
    CHARISMA = auto()


class Stats(ABC):
    @property
    @abstractmethod
    def stats(self) -> Dict[Stat, int]:
        ...

    @property
    @abstractmethod
    def max_hp(self) -> int:
        ...

    @property
    @abstractmethod
    def max_mp(self) -> int:
        ...

    @property
    @abstractmethod
    def hp(self) -> int:
        ...

    @property
    @abstractmethod
    def mp(self) -> int:
        ...


class Language(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def description(self) -> str:
        ...

    @property
    @abstractmethod
    def dictionary(self) -> Dict[str, str]:
        ...

    def translate(self, word: str) -> str:
        return self.dictionary[word]

    def translate_sentence(self, sentence: str) -> str:
        return " ".join([self.translate(word) for word in sentence.split(" ")])


class Actor(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def description(self) -> str:
        ...

    @property
    @abstractmethod
    def stats(self) -> Stats:
        ...

    @property
    @abstractmethod
    def equipment(self) -> Equipment:
        ...

    @property
    @abstractmethod
    def inventory(self) -> Inventory:
        ...

    @property
    @abstractmethod
    def languages(self) -> Dict[Language, bool]:
        ...


__all__ = ["Actor", "Stats", "Language", "Skill"]



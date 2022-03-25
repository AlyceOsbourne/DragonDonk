from __future__ import annotations
from main.resource_manager import __export__
from abc import ABC, abstractmethod


@__export__
class Room(ABC):

    @property
    @abstractmethod
    def x(self) -> int:
        ...

    @property
    @abstractmethod
    def y(self) -> int:
        ...

    @property
    @abstractmethod
    def width(self) -> int:
        ...

    @property
    @abstractmethod
    def height(self) -> int:
        ...

    @property
    @abstractmethod
    def description(self) -> str:
        ...

    @property
    @abstractmethod
    def north(self) -> "Room":
        ...

    @property
    @abstractmethod
    def east(self) -> "Room":
        ...

    @property
    @abstractmethod
    def south(self) -> "Room":
        ...

    @property
    @abstractmethod
    def west(self) -> "Room":
        ...

    @property
    @abstractmethod
    def loot(self) -> list:
        ...

    @property
    @abstractmethod
    def encounter(self) -> list:
        ...


@__export__
class Dungeon(ABC):

    def generate_rooms(self) -> None:
        ...

    def generate_encounters(self) -> None:
        ...

    def generate_loot(self) -> None:
        ...

    def generate_paths(self) -> None:
        ...



@__export__
class Map(ABC):
    ...


@__export__
class Quest(ABC):
    ...


@__export__
class Skill(ABC):
    ...


@__export__
class Stats(ABC):
    ...


@__export__
class Language(ABC):
    ...


@__export__
class Item(ABC):
    ...

@__export__
class Inventory(ABC):
    ...


@__export__
class Actor(ABC):
    @property
    @abstractmethod
    def name(self):
        ...

    @property
    @abstractmethod
    def description(self):
        ...

    @property
    @abstractmethod
    def stats(self) -> Stats:
        ...

    @property
    @abstractmethod
    def skills(self) -> list["Skill"]:
        ...

    @property
    @abstractmethod
    def languages(self) -> list["Language"]:
        ...

    @property
    @abstractmethod
    def inventory(self) -> Inventory:
        ...

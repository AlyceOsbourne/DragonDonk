from __future__ import annotations

from abc import ABC, abstractmethod

from core.core_definitions.items import Item
from core.core_registry import Registry


@Registry.register
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


@Registry.register
class Dungeon(ABC):

    def generate_rooms(self) -> None:
        ...

    def generate_encounters(self) -> None:
        ...

    def generate_loot(self) -> None:
        ...

    def generate_paths(self) -> None:
        ...


@Registry.register
class Town(ABC):

    def generate_buildings(self) -> None:
        ...

    def generate_encounters(self) -> None:
        ...

    def generate_loot(self) -> None:
        ...

    def generate_paths(self) -> None:
        ...


@Registry.register
class Map(ABC):
    def generate_dungeons(self) -> None:
        ...

    def generate_towns(self) -> None:
        ...

    def generate_paths(self) -> None:
        ...

    def generate_encounters(self) -> None:
        ...

    def generate_loot(self) -> None:
        ...


@Registry.register
class Quest(ABC):
    starting_location: Room or Dungeon or Town
    ending_location: Room or Dungeon or Town
    reward: [Item, ...]


__all__ = ["Room", "Dungeon", "Town", "Map", "Quest"]

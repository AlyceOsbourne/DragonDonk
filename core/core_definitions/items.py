from __future__ import annotations

from abc import ABCMeta, ABC, abstractmethod
from enum import Enum, auto

from core.core_definitions.abstract import Inventory, Effect


class Item(ABC):
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
    def value(self) -> int:
        ...

    @property
    @abstractmethod
    def weight(self) -> int:
        ...

    @property
    @abstractmethod
    def stackable(self) -> bool:
        ...


class EquipmentSlot(Enum):
    MAIN_HAND = auto()
    OFF_HAND = auto()
    HEAD = auto()
    CHEST = auto()
    LEGS = auto()
    FEET = auto()
    HANDS = auto()
    NECK = auto()
    RING = auto()
    AMMO = auto()
    BACK = auto()


class WeaponAttackType(Enum):
    SLASH = auto()
    PIERCE = auto()
    BLUNT = auto()


class Weapon(Item, metaclass=ABCMeta):
    @property
    @abstractmethod
    def attack_type(self) -> WeaponAttackType:
        ...

    @property
    @abstractmethod
    def damage(self) -> int:
        ...

    @property
    @abstractmethod
    def hands(
            self) -> EquipmentSlot.MAIN_HAND or EquipmentSlot.OFF_HAND or EquipmentSlot.MAIN_HAND and EquipmentSlot.OFF_HAND:
        ...

    @property
    @abstractmethod
    def range(self) -> int:
        ...

    @property
    @abstractmethod
    def critical_chance(self) -> int:
        ...

    @property
    @abstractmethod
    def critical_multiplier(self) -> int:
        ...

    @property
    @abstractmethod
    def speed(self) -> int:
        ...

    @property
    def stackable(self) -> bool:
        return False


class ArmorDefenseType(Enum):
    No_Armor = auto()
    Light = auto()
    Medium = auto()
    Heavy = auto()


class Armor(Item, metaclass=ABCMeta):
    @property
    @abstractmethod
    def defense_type(self) -> ArmorDefenseType:
        ...

    @property
    @abstractmethod
    def defense(self) -> int:
        ...

    @property
    @abstractmethod
    def weight(self) -> int:
        ...

    @property
    @abstractmethod
    def slot(self) -> EquipmentSlot.HEAD or \
                      EquipmentSlot.NECK or \
                      EquipmentSlot.CHEST or \
                      EquipmentSlot.HANDS or \
                      EquipmentSlot.RING or \
                      EquipmentSlot.LEGS or \
                      EquipmentSlot.FEET or \
                      EquipmentSlot.BACK:
        ...

    @property
    def stackable(self) -> bool:
        return False


class Equipment:
    @property
    @abstractmethod
    def head(self) -> Armor:
        ...

    @property
    @abstractmethod
    def neck(self) -> Armor:
        ...

    @property
    @abstractmethod
    def chest(self) -> Armor:
        ...

    @property
    @abstractmethod
    def hands(self) -> Armor:
        ...

    @property
    @abstractmethod
    def legs(self) -> Armor:
        ...

    @property
    @abstractmethod
    def feet(self) -> Armor:
        ...

    @property
    @abstractmethod
    def ring(self) -> Armor:
        ...

    @property
    @abstractmethod
    def back(self) -> Armor:
        ...

    @property
    @abstractmethod
    def main_hand(self) -> Weapon:
        ...

    @property
    @abstractmethod
    def off_hand(self) -> Weapon:
        ...


class Consumable(Item, metaclass=ABCMeta):

    @property
    @abstractmethod
    def effect(self) -> Effect:
        ...

    @property
    @abstractmethod
    def duration(self) -> int:
        ...


class WearableInventory(Inventory, Armor, metaclass=ABCMeta):
    @property
    def slot(self):
        return EquipmentSlot.BACK

    @property
    def defense_type(self) -> ArmorDefenseType:
        return ArmorDefenseType.No_Armor

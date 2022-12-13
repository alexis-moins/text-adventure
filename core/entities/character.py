from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC

from core.fight.fighter import Fighter
from core.items.equipable import Equipable

if TYPE_CHECKING:
    from core.items.item import Item
    from core.fight.statistics import Statistics
    from core.containers.inventory import Inventory


class Character(Fighter, ABC):

    def __init__(self, name: str, description: str, statistics: Statistics, inventory: Inventory) -> None:
        """
        Constructor creating a new abstract character.

        Arguments:
        name - the name of the character
        description - the description of the character
        """
        super().__init__(name, description, statistics, inventory)

        for item in self.inventory.get_entities():
            self.equip(item)

    def equip(self, item: Item) -> None:
        """
        Handle or wear the given equipment.
        """
        if not isinstance(item, Equipable):
            return

        if item.slot in self.equipments:
            self.take_off(self.equipments[item.slot])

        self.equipments[item.slot] = item
        item.is_equiped = True

    def take_off(self, item: Item) -> None:
        """
        Take the given equipment off.

        Argument:
        item - the equipment to take off
        """
        if not isinstance(item, Equipable):
            return

        del self.equipments[item.slot]
        item.is_equiped = False

    def take(self, item: Item) -> None:
        """
        Add the given item to the inventory.

        Argument:
        item - the item to take
        """
        self.inventory.add(item)

    def drop(self, item: Item) -> None:
        """
        Drop the given item. If the item is equiped, it will be taken off.

        Argument:
        item - the item to drop
        """
        if isinstance(item, Equipable) and item.is_equiped:
            self.take_off(item)

        self.inventory.remove(item)

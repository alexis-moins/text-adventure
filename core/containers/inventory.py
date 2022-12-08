from __future__ import annotations
from typing import TYPE_CHECKING

from core.items.equipable import Equipable
from core.containers.container import Container

if TYPE_CHECKING:
    from core.entities.entity import Entity
    from core.fight.equipments import Equipments


class Inventory(Container):

    def __init__(self, items: list[Entity] | None = None, *, size: int = 10) -> None:
        """
        Constructor creating a new inventory, a sized container for items
        of all kinds.
        """
        super().__init__(items or [])
        self.size = size
        self.equipments: Equipments = {}

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.b.add(f'YELLOW({len(self)}/{self.size})WHITE').build()

    def long_description(self) -> str:
        """
        Return the long description of this element.

        Returns:
        A string
        """
        for slot in self.get_slots():
            self.b.add(f'- {slot.short_description()}')

        return self.b.build()

    def equip(self, equipment: Equipable) -> None:
        """
        Handle or wear the given equipment.
        """
        if equipment.slot in self.equipments:
            self.take_off(self.equipments[equipment.slot])

        self.equipments[equipment.slot] = equipment
        equipment.equiped = True

    def take_off(self, equipment: Equipable) -> None:
        """

        """
        del self.equipments[equipment.slot]
        equipment.equiped = False

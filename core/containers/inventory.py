from __future__ import annotations

from core.items.item import Item
from core.utils.armory import Armory

from core.items.equipable import Equipable
from core.containers.sized_container import SizedContainer


class Inventory(SizedContainer[Item]):
    """
    Sized container representing a fighter's inventory.
    """
    armory = Armory()

    def __init__(self, items: list[Item] | None = None, *, size: int = 10) -> None:
        """
        Constructor creating a new inventory, a sized container for items
        of all kinds.

        Argument:
        items - list of items

        Keyword Arguments:
        size - the maximum capacity of the inventory
        """
        super().__init__(items, size=size)

    @staticmethod
    def create(items: list[str], *, size: int = 10) -> Inventory:
        """
        Create and return a new Inventory using the Armory.

        Argument:
        items - list of item names

        Keyword Arguments:
        size - the maximum capacity of the inventory

        Retuns:
        An Inventory
        """
        return Inventory([Inventory.armory.take(item)
                          for item in items], size=size)

    def long_description(self) -> str:
        """
        Return the long description of this element.

        Returns:
        A string
        """
        for slot in self.slots:
            sign = 'e' if isinstance(
                slot.first_entity, Equipable) and slot.first_entity.is_equiped else ' '

            self.b.add(f'- [RED{sign}WHITE] {slot.short_description()}')

        return self.b.build()

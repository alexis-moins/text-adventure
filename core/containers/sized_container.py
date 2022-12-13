from __future__ import annotations
from typing import TYPE_CHECKING

from core.containers.slot import Slot
from core.containers.container import Container

if TYPE_CHECKING:
    from core.entities.entity import Entity


class SizedContainer(Container):
    """
    Sized container representing a fighter's inventory.
    """

    def __init__(self, items: list[Entity] | None = None, *, size: int = 10) -> None:
        """
        Constructor creating a new sized container for entities.

        Argument:
        items - list of items

        Keyword Arguments:
        size - the maximum capacity of the inventory
        """
        super().__init__()
        self.size = size

        for item in items or []:
            self.add(item)

    def is_empty(self) -> bool:
        """
        Return true if the inventory is empty, otherwise
        return false.

        Returns:
        A boolean
        """
        return len(self.slots) == 0

    def is_full(self) -> bool:
        """
        Return true if the inventory is full, otherwise
        return false.

        Returns:
        A boolean
        """
        return len(self.slots) == self.size

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
        for slot in self.slots:
            self.b.add(f'- {slot.short_description()}')

        return self.b.build()

    def add(self, entity: Entity) -> bool:
        """
        Add an entity to the container. Return false if
        it is impossible to add items to the inventory.

        Argument:
        entity - the entity to be added

        A boolean
        Returns:
        """
        slot = self.get_slot_by_name(entity)

        if slot is None:

            if self.is_full():
                return False

            self.slots.append(Slot.of(entity))
            return True

        if slot.add(entity):
            return True

        if self.is_full():
            return False

        self.slots.append(Slot.of(entity))
        return True

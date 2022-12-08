from __future__ import annotations

from typing import TYPE_CHECKING, Iterator
from core.entities.describable import Describable

if TYPE_CHECKING:
    from core.entities.entity import Entity


class Slot(Describable):

    def __init__(self, entity: Entity, size: int) -> None:
        """
        Constructor creating a new slot of the given size.
        """
        super().__init__()
        self.size = size

        self.entities = [entity]
        self.name = entity.name

    @staticmethod
    def of(entity: Entity) -> Slot:
        """

        """
        return Slot(entity, entity.stack_size)

    def is_full(self) -> bool:
        """
        Return true if the slot is full.

        Returns:
        A boolean
        """
        return len(self.entities) == self.size

    def is_empty(self) -> bool:
        """

        """
        return len(self.entities) == 0

    def add(self, entity: Entity) -> bool:
        """

        """
        if self.is_full():
            return False

        self.entities.append(entity)
        return True

    def remove(self, entity: Entity, quantity: int) -> bool:
        """"""
        if entity not in self.entities:
            return False

        self.entities.remove(entity)
        return True

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        entity = self.entities[0]
        return self.b.add(f'BLUEx{len(self)}WHITE {entity.short_description()}').build()

    def long_description(self) -> str:
        """
        Return the long description of this element.

        Returns:
        A string
        """
        return 'Not Implemented'

    def __len__(self) -> int:
        """
        Return the number of entities in the stack.

        Returns:
        An integer
        """
        return len(self.entities)

    def __iter__(self) -> Iterator[Entity]:
        """

        """
        return iter(self.entities)

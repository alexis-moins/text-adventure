from __future__ import annotations

from typing import TYPE_CHECKING, Iterator
from core.entities.describable import Describable

if TYPE_CHECKING:
    from core.entities.entity import Entity


class Slot(Describable):

    def __init__(self, entity: Entity) -> None:
        """
        Constructor creating a new slot of the given size.
        """
        super().__init__()
        self.entities = [entity]
        self.name = entity.name

    def is_empty(self) -> bool:
        """

        """
        return len(self.entities) == 0

    def add(self, entity: Entity) -> bool:
        """

        """
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

    def __add__(self, other: Slot) -> Slot:
        """

        """
        self.entities.extend(other.entities)
        return self

from __future__ import annotations
from typing import Generic, Iterator, TypeVar

from core.entities.entity import Entity
from core.entities.describable import Describable


T = TypeVar('T', bound=Entity)


class Slot(Describable, Generic[T]):

    def __init__(self, entity: T, *, size: int = 20) -> None:
        """
        Constructor creating a new slot of the given size.
        """
        super().__init__()
        self.entities = [entity]

        self.size = size
        self.first_entity = entity

    @staticmethod
    def of(entity: T) -> Slot:
        """
        Return a new slot of entity.

        Argument:
        entity - the entity of the slot

        Returns:
        A slot
        """
        return Slot(entity, size=entity.stack_size)

    def take(self, n: int) -> list[T]:
        """
        Remove and return the n first entities of the slot.

        Argument:
        n - the number of entities to take

        Returns:
        A list of entities
        """
        if len(self.entities) < n:
            return []

        entities = self.entities[:n]

        for entity in self.entities:
            self.entities.remove(entity)

        return entities

    def is_empty(self) -> bool:
        """
        Return true if the slot is empty, return
        false otherwise.

        Returns:
        A boolean
        """
        return len(self.entities) == 0

    def is_full(self) -> bool:
        """
        Return true if the slot is full, return
        false otherwise.

        Returns:
        A boolean
        """
        return len(self.entities) == self.size

    def add(self, entity: T) -> bool:
        """

        """
        if self.is_full():
            return False

        self.entities.append(entity)
        return True

    def remove(self, entity: T) -> bool:
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
        return self.b.add(f'BLUEx{len(self)}WHITE {self.first_entity.slot_description()}').build()

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
        Return an iterator over the entities of the slot.

        Returns:
        An iterator of entities
        """
        return iter(self.entities)

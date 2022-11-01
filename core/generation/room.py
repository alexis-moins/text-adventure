from __future__ import annotations
from typing import Generic, Iterator, TypeVar

from core.entities.classes import Entity
from core.utils.strings import StringBuilder


T = TypeVar('T')


class Container(Generic[T]):

    def __init__(self, elements=None) -> None:
        self._elements = elements or []

    def add(self, element: T) -> None:
        """
        """
        self._elements.append(element)

    def find(self, name: str) -> T | None:
        """
        Return the instance of T matching the given name.

        Argument:
        name - the name of the entity you want to find

        Returns:
        An instance of T or None
        """
        entities = [entity for entity in self._entities if name in entity.name]
        return entities[0]

    def take(self, name: str) -> T | None:
        """"""
        pass

    def __iter__(self) -> Iterator[T]:
        """
        """
        return iter(self._elements)

    def __len__(self) -> int:
        """
        """
        return len(self._elements)

    def __bool__(self) -> bool:
        """
        """
        return bool(self._elements)


class Room:
    """
    Represents a room, a space containing entities (characters and / or items).
    """

    def __init__(self, name: str, description: str, entities: list = None) -> None:
        """
        """
        self.name = name
        self.description = description

        self.entities: Container[Entity] = Container(entities)

        self.is_boss_room: bool = False
        self.builder = StringBuilder()

    def __str__(self) -> str:
        """
        """
        self.builder.add(self.name).add(self.description)

        if not self.entities:
            return self.builder.build()

        verb = 'is' if len(self.entities) == 1 else 'are'
        self.builder.add(f'\nAround you {verb}:')

        for entity in self.entities:
            self.builder.add(f'{entity.determiner} {entity}')

        return self.builder.build()

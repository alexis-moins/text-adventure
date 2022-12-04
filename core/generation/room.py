from __future__ import annotations
from typing import Generic, Iterator, TypeVar


from core.entities.npc import NPC
from core.entities import Describable


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

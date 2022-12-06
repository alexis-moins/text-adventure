from __future__ import annotations
from typing import Generic, Iterator, TypeVar

T = TypeVar('T')


class Container(Generic[T]):

    def __init__(self, entities=None) -> None:
        """
        Constructor creating a new container.
        """
        self._entities = entities or []

    def add(self, entity: T) -> None:
        """
        Add an entity to the container.
        """
        self._entities.append(entity)

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
        entity = self.find(name)

        if not entity:
            return None

        self._entities.remove(entity)
        return entity

    def __iter__(self) -> Iterator[T]:
        """
        Return an iterator over the entities of the container.

        Returns:
        An iterator of entities
        """
        return iter(self._entities)

    def __len__(self) -> int:
        """
        Return the number of entities in the container.

        Returns:
        An integer
        """
        return len(self._entities)

    def __bool__(self) -> bool:
        """
        Return true if the container is not empty, returns false
        otherwise.

        Returns:
        A boolean
        """
        return bool(self._entities)

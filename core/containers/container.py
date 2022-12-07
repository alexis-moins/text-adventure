from __future__ import annotations
from typing import TYPE_CHECKING

from core.containers.slot import Slot
from core.entities.describable import Describable

if TYPE_CHECKING:
    from core.entities.entity import Entity


class Container(Describable):

    def __init__(self, entities: list[Entity]) -> None:
        """
        Constructor creating a new container.
        """
        super().__init__()
        self.slots: dict[str, Slot] = {}

        for entity in entities:
            self.add(entity)

    def add(self, entity: Entity) -> None:
        """
        Add an entity to the container.
        """
        if entity.name in self.slots:
            self.slots[entity.name].add(entity)
        else:
            self.slots[entity.name] = Slot([entity])

    def add_slot(self, slot: Slot) -> None:
        """

        """
        self.slots[slot.name] = slot

    def remove_slot(self, slot: Slot) -> None:
        """

        """
        del self.slots[slot.name]

    def remove(self, entity: Entity, *, quantity: int = 1) -> bool:
        """
        Remove an entity from the container. Return true if the
        entity was successfully removed, otherwise return false.

        Argument:
        entity - the entity to be removed from the container

        Keyword Argument:
        quantity - the number of entities to remove

        Returns:
        A boolean
        """
        if not entity in self.get_entities():
            return False

        success = self.slots[entity.name].remove(entity, quantity)

        if not success:
            return False

        if not self.slots[entity.name]:
            del self.slots[entity.name]

        return True

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.b.add('TEST').build()

    def long_description(self) -> str:
        """
        Return the long description of this element.

        Returns:
        A string
        """
        for slot in self.slots.values():
            self.b.add(f'- {slot.short_description()}')

        return self.b.build()

    def get_entities(self) -> list[Entity]:
        """
        Return the list of the entities in the container.

        Returns:
        A list of entities
        """
        entities = []
        for slot in self.slots.values():
            entities.extend(slot.entities)

        return entities

    def get_slots(self) -> list[Slot]:
        """
        Return an iterator over the slots of the container.

        Returns:
        An iterator of Slots
        """
        return list(self.slots.values())

    def __len__(self) -> int:
        """
        Return the number of entities in the container.

        Returns:
        An integer
        """
        return len(self.slots)

    def __bool__(self) -> bool:
        """
        Return true if the container is not empty, returns false
        otherwise.

        Returns:
        A boolean
        """
        return bool(self.slots)

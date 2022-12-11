from __future__ import annotations
from typing import TYPE_CHECKING, Iterator, Type, TypeVar

from core.entities.npc import NPC
from core.containers.slot import Slot
from core.containers.ncp_slot import NPCSlot
from core.entities.describable import Describable

if TYPE_CHECKING:
    from core.entities.entity import Entity


T = TypeVar('T')


class Container(Describable):

    def __init__(self) -> None:
        """
        Constructor creating a new container.
        """
        super().__init__()
        self.slots: list[Slot] = []

    @staticmethod
    def of(entities: list[Entity]) -> Container:
        """
        Return a container with the given entities inside.

        Argument:
        entities - a list of entities

        Returns:
        A container
        """
        container = Container()

        for entity in entities:
            container.add(entity)

        return container

    def add(self, entity: Entity) -> bool:
        """
        Add an entity to the container.

        Argument:
        entity - the entity to be added
        """
        slot = self.get_slot_by_name(entity)

        if slot:
            if slot.add(entity):
                return True

        _class = NPCSlot if isinstance(entity, NPC) else Slot
        self.slots.append(_class.of(entity))
        return True

    def add_slot(self, slot: Slot) -> None:
        """

        """
        for entity in slot:
            self.add(entity)

    def remove_slot(self, slot: Slot) -> None:
        """
        Remove a slot from the container.

        Argument:
        slot - the slot to be removed
        """
        self.slots.remove(slot)

    def remove(self, entity: Entity) -> None:
        """"""
        slot = self.get_slot(entity)

        if slot:
            slot.remove(entity)

            if slot.is_empty():
                self.slots.remove(slot)

    def filter(self, _type: Type[T]) -> list[T]:
        """

        """
        return list(filter(lambda x: isinstance(x, _type), self.get_entities()))  # type: ignore

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
        for slot in self.slots:
            self.b.add(f'- {slot.short_description()}')

        return self.b.build()

    def get_entities(self) -> list[Entity]:
        """
        Return the list of the entities in the container.

        Returns:
        A list of entities
        """
        entities = []
        for slot in self.slots:
            entities.extend(slot.entities)

        return entities

    def get_slot(self, entity: Entity) -> Slot | None:
        """
        Return an iterator over the slots of the container.

        Returns:
        An iterator of Slots
        """
        for slot in self.slots:
            if entity in slot:
                return slot

        return None

    def get_slot_by_name(self, entity: Entity) -> Slot | None:
        """

        """
        for slot in self.slots:
            if entity.name == slot.name:
                return slot

        return None

    def __len__(self) -> int:
        """
        Return the number of entities in the container.

        Returns:
        An integer
        """
        return len(self.slots)

    def __contains__(self, entity: Entity) -> bool:
        """
        Return true of the container contains the given entity,
        otherwise return false.

        Argument:
        entity - the considered entity

        Returns:
        A boolean
        """
        return entity in self.get_entities()

    def __iter__(self) -> Iterator[Slot]:
        """"""
        return iter(self.slots)

    def __bool__(self) -> bool:
        """
        Return true if the container is not empty, returns false
        otherwise.

        Returns:
        A boolean
        """
        return bool(self.slots)

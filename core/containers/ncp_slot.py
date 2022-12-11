from __future__ import annotations

from typing import TYPE_CHECKING, Iterator
from core.containers.slot import Slot

if TYPE_CHECKING:
    from core.entities.entity import Entity


class NPCSlot(Slot):

    def __init__(self, entity: Entity, *, size: int = 20) -> None:
        """
        Constructor creating a new slot of the given size.
        """
        super().__init__(entity)

    @staticmethod
    def of(entity: Entity) -> Slot:
        """
        Return a new slot of entity.

        Argument:
        entity - the entity of the slot

        Returns:
        A slot
        """
        return NPCSlot(entity, size=entity.stack_size)

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        health = sum([entity.health for entity in self.entities])
        max_health = sum([entity.max_health for entity in self.entities])

        entity = self.entities[0]
        percentage = int(health / max_health * 100)
        return self.b.add(f'BLUEx{len(self)}WHITE {entity.name} {"RED" if entity.is_hostile else "CYAN"}({percentage}%)WHITE').build()

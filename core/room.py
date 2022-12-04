from __future__ import annotations

from typing import TYPE_CHECKING
from core.entities import Describable

if TYPE_CHECKING:
    from core.entities.npc import NPC


class Room(Describable):
    """
    Represents a room, a space containing entities.
    """

    def __init__(self, name: str, description: str, npc: list[NPC] | None = None) -> None:
        """
        """
        super().__init__()

        self.name = name
        self.description = description

        self.npc = npc or []

        self.is_boss_room: bool = False

    @property
    def entities(self) -> list[NPC]:
        """

        """
        return self.npc  # + self.items

    def short_description(self) -> str:
        return ''

    def long_description(self) -> str:
        """
        Return the long description of the room.

        Returns:
        A string
        """
        self.b.add(self.name).add(self.description)

        if not self.entities:
            return self.b.build()

        self.b.new_line()

        verb = 'is' if len(self.entities) == 1 else 'are'
        self.b.add(f'Around you {verb}:')

        for entity in self.entities:
            self.b.add(
                f'BLUEx1WHITE {entity.short_description()}')

        return self.b.build()

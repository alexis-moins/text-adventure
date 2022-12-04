from __future__ import annotations

from typing import TYPE_CHECKING
from core.entities.character import Character

if TYPE_CHECKING:
    from core.fight.statistics import Statistics


class NPC(Character):

    def __init__(self, name: str, description: str, statistics: Statistics, *, is_hostile: bool) -> None:
        """
        Constructor creating a new NPC, whether it is hostile or not.

        Arguments:
        name - the name of the NPC
        description - the description of the NPC

        Keyword Arguments:
        is_hostile - whether the NPC is hostile to the player or not
        """
        super().__init__(name, description, statistics)
        self.is_hostile = is_hostile

    def take_turn(self) -> bool:
        """
        Make the NPC take its turn.

        Returns:
        true if the actor has executed an action, false otherwise
        """
        return True

    def short_description(self) -> str:
        """
        Return the short description of the Npc.

        Returns:
        A string
        """
        sign = 'RED(hostile)WHITE' if self.is_hostile else f'CYAN(peaceful)WHITE'
        return self.b.add(self.name + f' {sign}').build()

    def long_description(self) -> str:
        """
        Return the long description of the NPC.

        Returns:
        A string
        """
        return ''

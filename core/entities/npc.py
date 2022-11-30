from __future__ import annotations

from core.entities.character import Character
from core.fight.fighter import Fighter


class NPC(Character):

    def __init__(self, name: str, description: str, fighter: Fighter, *, is_hostile: bool, character: str) -> None:
        """
        Constructor creating a new NPC, whether it is hostile or not.

        Arguments:
        name - the name of the NPC
        description - the description of the NPC
        fighter - the fighter component to use

        Keyword Arguments:
        is_hostile - whether the NPC is hostile to the player or not
        character - the character to represent the NPC (when peaceful)
        """
        super().__init__(name, description, fighter)
        self.is_hostile = is_hostile
        self.character = character

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
        sign = 'RED[!]WHITE' if self.is_hostile else f'GREEN[{self.character}]WHITE'
        return self._builder.add(self.name + f' {sign}').build()

    def long_description(self) -> str:
        """
        Return the long description of the NPC.

        Returns:
        A string
        """
        return ''

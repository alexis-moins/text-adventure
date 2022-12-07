from __future__ import annotations
from typing import TYPE_CHECKING

from core.containers.inventory import Inventory
from core.fight.fighter import Fighter

if TYPE_CHECKING:
    from core.dungeon import Dungeon


class Player(Fighter):

    def __init__(self) -> None:
        """
        Constructor creating a new player.
        """
        super().__init__('Patate', '', {
            'health': 20, 'magic': 10, 'strength': 12, 'defence': 2}, Inventory())

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return ''

    def long_description(self) -> str:
        """
        Return the long description of this element.

        Returns:
        A string
        """
        return ''

    def take_turn(self, dungeon: Dungeon) -> bool:
        """
        Make the character take its turn.

        Argument:
        dungeon - the current dungeon

        Returns:
        true if the actor has executed an action, false otherwise
        """
        return True

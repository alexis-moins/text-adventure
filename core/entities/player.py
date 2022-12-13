from __future__ import annotations
from typing import TYPE_CHECKING
from core.entities.character import Character

from core.fight.statistics import Statistics
from core.containers.inventory import Inventory

if TYPE_CHECKING:
    from core.dungeon import Dungeon


class Player(Character):

    def __init__(self, archetype: str, statistics: Statistics, inventory: Inventory) -> None:
        """
        Constructor creating a new player.
        """
        super().__init__(archetype, 'The hero wandering through the dungeon!', statistics, inventory)

    @staticmethod
    def barbarian() -> Player:
        """
        Return a barbarian player.

        Returns:
        A Player
        """
        statistics = {'health': 20, 'magic': 10, 'strength': 5, 'defence': 2}
        inventory = Inventory.create(['leather armor', 'iron sword'])

        return Player('Barbarian', Statistics(**statistics), inventory)

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

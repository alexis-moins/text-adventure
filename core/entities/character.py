from __future__ import annotations
from typing import TYPE_CHECKING

from abc import ABC, abstractmethod
from core.fight.fighter import Fighter
from core.entities.entity import Entity

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.fight.statistics import Statistics
    from core.containers.inventory import Inventory


class Character(Entity, ABC):

    def __init__(self, name: str, description: str, statistics: Statistics, inventory: Inventory) -> None:
        """
        Constructor creating a new abstract character.

        Arguments:
        name - the name of the character
        description - the description of the character
        """
        super().__init__(name, description)
        self.fighter = Fighter(**statistics, inventory=inventory)

    @abstractmethod
    def take_turn(self, dungeon: Dungeon) -> bool:
        """
        Make the character take its turn.

        Argument:
        dungeon - the current dungeon

        Returns:
        true if the actor has executed an action, false otherwise
        """
        pass

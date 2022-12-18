from __future__ import annotations
from typing import TYPE_CHECKING

from core.entities.npc import NPC
from core.containers.inventory import Inventory

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.fight.statistics import Statistics


class Trader(NPC):

    def __init__(self, name: str, description: str, statistics: Statistics, inventory: Inventory, stock: list[str], gold: int) -> None:
        """
        Constructor creating a new NPC, whether it is hostile or not.

        Arguments:
        name - the name of the NPC
        description - the description of the NPC

        statistics - the statistics of the NPC
        inventory - the possessions of the NPC
        """
        super().__init__(name, description, statistics,
                         inventory, gold=gold, is_hostile=False)

        self.stock = Inventory.create(stock)

    def take_turn(self, dungeon: Dungeon) -> bool:
        """
        Make the NPC take its turn.

        Argument:
        dungeon - the current dungeon

        Returns:
        true if the actor has executed an action, false otherwise
        """
        return super().take_turn(dungeon)

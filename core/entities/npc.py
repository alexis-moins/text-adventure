from __future__ import annotations

from typing import TYPE_CHECKING
from core.fight.fighter import Fighter

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.fight.statistics import Statistics
    from core.containers.inventory import Inventory


class NPC(Fighter):

    def __init__(self, name: str, description: str, statistics: Statistics, inventory: Inventory, *, is_hostile: bool) -> None:
        """
        Constructor creating a new NPC, whether it is hostile or not.

        Arguments:
        name - the name of the NPC
        description - the description of the NPC

        statistics - the statistics of the NPC
        inventory - the possessions of the NPC

        Keyword Arguments:
        is_hostile - whether the NPC is hostile to the player or not
        """
        super().__init__(name, description, statistics, inventory)
        self.is_hostile = is_hostile

    def take_turn(self, dungeon: Dungeon) -> bool:
        """
        Make the NPC take its turn.

        Argument:
        dungeon - the current dungeon

        Returns:
        true if the actor has executed an action, false otherwise
        """
        if self.is_hostile:
            damage = self.get_damage()
            dungeon.player.receive_damage(damage)

            dungeon.add_log(
                f'The {self.short_description()} deals you YELLOW{damage} damageWHITE.')

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

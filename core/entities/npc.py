from __future__ import annotations

from typing import TYPE_CHECKING
from core.fight.fighter import Fighter

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.fight.statistics import Statistics
    from core.containers.inventory import Inventory


class NPC(Fighter):
    """
    Class representing any non playable character.
    """

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

            damage = dungeon.player.mitigate_damage(damage)

            if not damage:
                message = f'The {self.name_and_id} YELLOWmissesWHITE you!'
            else:
                message = f'The {self.name_and_id} deals you YELLOW{damage} damageWHITE.'

            dungeon.add_log(message)

        return True

    def die(self, dungeon: Dungeon) -> None:
        """

        """
        dungeon.add_log(f'The {self.name_and_id} is REDdead!WHITE')
        dungeon.room.npc.remove(self)

        NPC.IDs[self.name] -= 1

        for slot in self.inventory.slots:
            dungeon.room.items.add_slot(slot)

        dungeon.add_log(
            '\nIt dropped something on the ground:')

        for slot in self.inventory:
            dungeon.logger.add(f'- {slot.short_description()}')

        dungeon.logger.new_line()

    def short_description(self) -> str:
        """
        Return the short description of the Npc.

        Returns:
        A string
        """
        percentage = int(self.health / self.max_health * 100)
        health_percentage = 'RED' if self.is_hostile else 'CYAN'
        health_percentage += f'({percentage}%)WHITE'

        return self.b.add(f'{self.name_and_id} {health_percentage}').build()

    def long_description(self) -> str:
        """
        Return the long description of the NPC.

        Returns:
        A string
        """
        return ''

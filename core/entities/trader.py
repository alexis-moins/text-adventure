from __future__ import annotations

from typing import TYPE_CHECKING
from core.entities.npc import NPC

if TYPE_CHECKING:
    from core.dungeon import Dungeon


class Trader(NPC):

    def take_turn(self, dungeon: Dungeon) -> bool:
        """
        Make the NPC take its turn.

        Argument:
        dungeon - the current dungeon

        Returns:
        true if the actor has executed an action, false otherwise
        """
        super().take_turn(dungeon)

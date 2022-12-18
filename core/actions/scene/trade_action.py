from __future__ import annotations
from typing import TYPE_CHECKING

from core.entities.trader import Trader
from core.actions.base_action import BaseAction

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.controllers.controller import Controller
    from core.controllers.scene_controller import SceneController


class TradeAction(BaseAction):
    """
    Class representing the action of opening the inventory menu.
    """

    def __init__(self, dungeon: Dungeon) -> None:
        """
        Constructor creating a new action to open an inventory.

        Argument:
        dungeon - the current dungeon
        """
        super().__init__(dungeon)
        self.character = dungeon.player

    def can_be_performed(self, _: Controller) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        context - the current dungeon

        Returns:
        a boolean
        """
        return any([isinstance(npc, Trader) for npc in self.dungeon.current_room.npc.get_entities()])

    def execute(self, _: SceneController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        context - the current dungeon

        Returns:
        A boolean
        """
        npcs = self.dungeon.current_room.npc.filter(Trader)

        trader = self.dungeon.architect.selection(
            'With which merchant do you want to trade :').start(npcs, auto_select=True)

        if not trader:
            return False

        self.dungeon.architect.multi_selection(
            'Which items do you want to buy :').start(trader.stock.slots)

        return True

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.b.add(f'Trade').build()

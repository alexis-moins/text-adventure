from __future__ import annotations

from typing import TYPE_CHECKING
from core.actions.base_action import BaseAction
from core.entities.trader import Trader

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.containers.inventory import Inventory
    from core.controllers.controller import Controller
    from core.controllers.scene_controller import SceneController


class TradeAction(BaseAction):
    """
    Class representing the action of opening the inventory menu.
    """

    def __init__(self, inventory: Inventory) -> None:
        """
        Constructor creating a new action to open an inventory.

        Argument:
        inventory - the inventory to open
        """
        super().__init__()
        self.inventory = inventory

    def can_be_performed(self, context: Dungeon, controller: Controller) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        context - the current dungeon

        Returns:
        a boolean
        """
        return any([isinstance(npc, Trader) for npc in context.room.npc.get_entities()])

    def execute(self, context: SceneController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the controller of the current scene

        Returns:
        A boolean
        """
        return False

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.b.add(f'Trade').build()

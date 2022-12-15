from __future__ import annotations

from typing import TYPE_CHECKING
from core.actions.base_action import BaseAction

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.controllers.controller import Controller
    from core.controllers.scene_controller import SceneController


class InventoryAction(BaseAction):
    """
    Class representing the action of opening the inventory menu.
    """

    def __init__(self, dungeon: Dungeon) -> None:
        """
        Constructor creating a new action to open an inventory.

        Argument:
        dungeon - the current dungeon
        inventory - the inventory to open
        """
        super().__init__(dungeon)
        self.inventory = dungeon.player.inventory

    def can_be_performed(self, _: Controller) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        controller - the current controller

        Returns:
        a boolean
        """
        return True

    def execute(self, _: SceneController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the current controller

        Returns:
        A boolean
        """
        if self.inventory.is_empty():
            self.dungeon.architect.message_controller(
                'Your inventory is YELLOWempty!WHITE').start()
            return False

        self.dungeon.architect.inventory_controller().start()
        return False

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.b.add(f'Inventory {self.inventory.short_description()}').build()

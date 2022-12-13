from __future__ import annotations
from typing import TYPE_CHECKING

from core.actions.base_action import BaseAction

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.controllers.scene_controller import SceneController
    from core.controllers.selection.quantity_controller import QuantityController


class QuantitySelectAction(BaseAction):

    def __init__(self, quantity: int) -> None:
        """
        Constructor creating an abstract action with its actor.

        Argument:
        quantity - the selected quantity
        """
        super().__init__()
        self.quantity = quantity

    def can_be_performed(self, _: Dungeon, controller: SceneController) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        context - the currently opened dungeon

        Returns:
        a boolean
        """
        return True

    def execute(self, controller: QuantityController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the controller of the current scene

        Returns:
        A boolean
        """
        if self.quantity > controller.maximum:
            return False

        controller.quantity = self.quantity
        controller.is_running = False

        return False

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return 'Not Implemented'

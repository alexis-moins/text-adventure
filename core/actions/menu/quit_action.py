from __future__ import annotations

from typing import TYPE_CHECKING
from core.actions.menu_action import MenuAction

if TYPE_CHECKING:
    from core.controllers.scene_controller import SceneController


class QuitAction(MenuAction):
    """
    Class representing the action of leaving the current controller.
    """

    def execute(self, controller: SceneController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the controller of the current scene

        Returns:
        A boolean
        """
        controller.is_running = False
        return False

    def __str__(self) -> str:
        """
        Return the string used to render the action.

        Returns:
        A string
        """
        return 'quit'

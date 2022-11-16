from __future__ import annotations

from typing import TYPE_CHECKING

from core.actions import BaseAction

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.controllers import Controller


class QuitAction(BaseAction):
    """
    Class representing the action of leaving the current controller.
    """

    def can_be_performed(self, _: Dungeon) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        context - the current dungeon

        Returns:
        a boolean
        """
        return True

    def execute(self, controller: Controller) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the controller of the current scene

        Returns:
        A boolean
        """
        return True

    def __str__(self) -> str:
        """
        Return the string used to render the action.

        Returns:
        A string
        """
        return 'Quit'

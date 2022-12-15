from __future__ import annotations

from typing import TYPE_CHECKING
from core.actions.base_action import BaseAction
from core.controllers.selection.multi_selection_controller import MultiSelectionController

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.controllers.scene_controller import SceneController


class QuitAction(BaseAction):
    """
    Class representing the action of leaving the current controller.
    """

    def __init__(self, dungeon: Dungeon, text: str = 'Quit') -> None:
        """
        Constructor creating a new action of quitting the current
        controller.

        Argument:
        dungeon - the current dungeon
        text - the text displayed
        """
        super().__init__(dungeon)
        self.text = text

    def can_be_performed(self, _: SceneController) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        controller - the current controller

        Returns:
        a boolean
        """
        return True

    def execute(self, controller: SceneController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the current controller

        Returns:
        A boolean
        """
        controller.on_quit()
        controller.is_running = False
        return False

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.text

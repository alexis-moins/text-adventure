from __future__ import annotations
from typing import TYPE_CHECKING

from core.actions.base_action import BaseAction
from core.views.selection.selection_view import SelectionMenu
from core.controllers.selection.selection_controller import SelectionController

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.controllers.scene_controller import SceneController


class AttackAction(BaseAction):
    """
    Class representing the action of attacking an entity in the room.
    """

    def can_be_performed(self, context: Dungeon) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        context - the current dungeon

        Returns:
        a boolean
        """
        return len(context.room.entities) > 0

    def execute(self, controller: SceneController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the controller of the current scene

        Returns:
        A boolean
        """
        selector = SelectionController(controller.dungeon, SelectionMenu(
            controller.dungeon, 'Who will be the target of you attack ?'))

        selection = selector.select(controller.dungeon.room.npc)

        if not selection:
            return False

        input(f'attacking {selection}')

        return True

    def __str__(self) -> str:
        """
        Return the string used to render the action.

        Returns:
        A string
        """
        return 'attack'

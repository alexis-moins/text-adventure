from __future__ import annotations

from typing import TYPE_CHECKING
from core.actions.base_action import BaseAction

if TYPE_CHECKING:
    from core.controllers.selection.multi_selection_controller import MultiSelectionController


class SelectAllAction(BaseAction):

    def can_be_performed(self, controller: MultiSelectionController) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        dungeon - the current dungeon

        Returns:
        a boolean
        """
        return not all(action.is_selected for action in controller.actions)

    def execute(self, controller: MultiSelectionController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the controller of the current scene

        Returns:
        A boolean
        """
        for action in controller.actions:
            if not action.is_selected:
                action.execute(controller)

        return False

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return 'Select all'

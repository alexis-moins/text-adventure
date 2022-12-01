from __future__ import annotations

from typing import TYPE_CHECKING
from core.actions.menu_action import MenuAction

if TYPE_CHECKING:
    from core.entities.describable import Describable
    from core.controllers.selection.selection_controller import SelectionController


class SelectAction(MenuAction):

    def __init__(self, model: Describable, *, key: str = '', multi: bool = False) -> None:
        """
        Constructor creating an abstract action with its actor.

        Argument:
        model - the model that would be selected

        Keyword Arguments:
        key - the key that need to be pressed in order to trigger the action
        multi - whether the UI if that of a multi selection
        """
        super().__init__(key=key)
        self.is_selected = False

        self.model = model
        self.multi = multi

    def execute(self, controller: SelectionController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the controller of the current scene

        Returns:
        A boolean
        """
        controller.selection = self.model
        return True

    def __str__(self) -> str:
        """
        Return the string used to render the action.

        Returns:
        A string
        """
        char = f'[{"RED*WHITE" if self.is_selected else " "}] ' if self.multi else ''
        return f'{char}the {self.model.short_description().lower()}'

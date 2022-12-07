from __future__ import annotations
from typing import TYPE_CHECKING

from core.actions.base_action import BaseAction

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.entities.describable import Describable
    from core.controllers.selection.selection_controller import SelectionController


class SelectAction(BaseAction):

    def __init__(self, model: Describable, *, multi: bool = False) -> None:
        """
        Constructor creating an abstract action with its actor.

        Argument:
        model - the model that would be selected

        Keyword Arguments:
        multi - whether the UI if that of a multi selection
        """
        super().__init__()
        self.is_selected = False

        self.model = model
        self.multi = multi

    def can_be_performed(self, _: Dungeon) -> bool:
        return True

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
        self.is_selected = not self.is_selected
        return True

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        char = f'({"RED*WHITE" if self.is_selected else " "}) ' if self.multi else ''
        return f'{char}the {self.model.short_description().lower()}'

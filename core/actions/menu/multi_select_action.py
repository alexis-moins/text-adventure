from __future__ import annotations
from typing import TYPE_CHECKING

from core.actions.base_action import BaseAction
from core.containers.slot import Slot

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.entities.describable import Describable
    from core.controllers.selection.multi_selection_controller import MultiSelectionController


class MultiSelectAction(BaseAction):

    def __init__(self, dungeon: Dungeon, model: Describable) -> None:
        """
        Constructor creating an abstract action with its actor.

        Argument:
        model - the model that would be selected
        """
        super().__init__(dungeon)
        self.is_selected = False
        self.model = model

    def can_be_performed(self, _: MultiSelectionController) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        controller - the current controller

        Returns:
        a boolean
        """
        return True

    def execute(self, controller: MultiSelectionController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the current controller

        Returns:
        A boolean
        """
        if self.model in controller.selection:
            controller.selection.remove(self.model)
        else:
            controller.selection.append(self.model)

        self.is_selected = not self.is_selected
        return False

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        char = '[RED*WHITE]' if self.is_selected else '[ ]'
        determiner = '' if isinstance(self.model, Slot) else 'the '
        return f'{char} {determiner}{self.model.short_description().lower()}'

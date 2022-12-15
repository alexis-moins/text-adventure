from __future__ import annotations
from typing import TYPE_CHECKING

from core.actions.base_action import BaseAction
from core.containers.slot import Slot

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.entities.describable import Describable
    from core.controllers.scene_controller import SceneController
    from core.controllers.selection.selection_controller import SelectionController


class SelectAction(BaseAction):

    def __init__(self, dungeon: Dungeon, model: Describable) -> None:
        """
        Constructor creating an abstract action with its actor.

        Argument:
        dungeon - the current dungeon
        model - the model that would be selected
        """
        super().__init__(dungeon)
        self.is_selected = False
        self.model = model

    def can_be_performed(self, _: SceneController) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        controller - the current controller
        context - the currently opened dungeon

        Returns:
        a boolean
        """
        return True

    def execute(self, controller: SelectionController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the current controller

        Returns:
        A boolean
        """
        controller.selection = self.model
        self.is_selected = not self.is_selected

        controller.is_running = False
        return False

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        determiner = '' if isinstance(self.model, Slot) else 'the '
        return f'{determiner}{self.model.short_description().lower()}'

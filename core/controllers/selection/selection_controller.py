from __future__ import annotations
from typing import TYPE_CHECKING

from core.actions.menu.select_action import SelectAction
from core.controllers.scene_controller import SceneController

if TYPE_CHECKING:
    from core.views.view import View
    from core.dungeon import Dungeon
    from core.actions.action_group import ActionGroup
    from core.entities.describable import Describable


class SelectionController(SceneController):

    def __init__(self, dungeon: Dungeon, view: View,  pinned: list[ActionGroup]) -> None:
        """
        Constructor creating a new scene controller

        Arguments:
        dungeon - the current dungeon
        view - the view used to render the scene
        """
        super().__init__(dungeon, view, [], pinned)
        self.selection: Describable | None = None

    def select(self, models: list[Describable]) -> Describable | None:
        """
        Start the controller and ask the user to select exactly one
        item from a list of items.

        Argument:
        items - a list of items to choose from
        """
        self.actions: list[SelectAction] = [
            SelectAction(model) for model in models]

        while self.is_running:
            self.execute_turn()

        return self.selection

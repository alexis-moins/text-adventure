from __future__ import annotations
from typing import TYPE_CHECKING

from core.controllers.scene_controller import SceneController
from core.actions.menu.multi_select_action import MultiSelectAction

if TYPE_CHECKING:
    from core.views.view import View
    from core.dungeon import Dungeon
    from core.actions.base_action import BaseAction
    from core.entities.describable import Describable


class MultiSelectionController(SceneController):

    def __init__(self, dungeon: Dungeon, view: View,  pinned: dict[str, BaseAction]) -> None:
        """
        Constructor creating a new scene controller

        Arguments:
        dungeon - the current dungeon
        view - the view used to render the scene
        """
        super().__init__(dungeon, view, [], pinned)
        self.selection: list[Describable] = []

    def start(self, models: list[Describable]) -> list[Describable]:
        """
        Start the controller and ask the user to select any number
        of item from a list of items.

        Argument:
        items - a list of items to choose from
        """
        self.actions: list[MultiSelectAction] = [
            MultiSelectAction(model) for model in models]

        while self.is_running:
            self.execute_turn()

        return self.selection

    def on_quit(self) -> None:
        """
        Clear the selection before quitting the controller.
        """
        self.selection = []

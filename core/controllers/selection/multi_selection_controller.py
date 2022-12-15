from __future__ import annotations
from typing import TYPE_CHECKING, TypeVar

from core.entities.describable import Describable
from core.controllers.scene_controller import SceneController
from core.actions.menu.multi_select_action import MultiSelectAction

if TYPE_CHECKING:
    from core.views.view import View
    from core.dungeon import Dungeon
    from core.actions.action_group import ActionGroup

T = TypeVar('T', bound=Describable)


class MultiSelectionController(SceneController):

    def __init__(self, dungeon: Dungeon, view: View,  pinned: list[ActionGroup]) -> None:
        """
        Constructor creating a new scene controller

        Arguments:
        dungeon - the current dungeon
        view - the view used to render the scene
        """
        super().__init__(dungeon, view, [], pinned)
        self.selection = []

    def start(self, models: list[T], *, auto_select: bool = False) -> list[T]:
        """
        Start the controller and ask the user to select any number
        of item from a list of items.

        Argument:
        items - a list of items to choose from

        Returns:
        A list of T
        """
        if auto_select and len(models) == 1:
            return models

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

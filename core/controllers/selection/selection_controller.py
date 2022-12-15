from __future__ import annotations
from typing import TYPE_CHECKING, TypeVar

from core.entities.describable import Describable
from core.actions.menu.select_action import SelectAction
from core.controllers.scene_controller import SceneController

if TYPE_CHECKING:
    from core.views.view import View
    from core.dungeon import Dungeon
    from core.actions.action_group import ActionGroup

T = TypeVar('T', bound=Describable)


class SelectionController(SceneController):

    def __init__(self, dungeon: Dungeon, view: View,  pinned: list[ActionGroup]) -> None:
        """
        Constructor creating a new scene controller

        Arguments:
        dungeon - the current dungeon
        view - the view used to render the scene
        """
        super().__init__(dungeon, view, [], pinned)
        self.selection = None

    def start(self, models: list[T], *, auto_select: bool = False) -> T | None:
        """
        Start the controller and ask the user to select exactly one
        item from a list of items.

        Argument:
        items - a list of items to choose from

        Returns:
        A T or None
        """
        if auto_select and len(models) == 1:
            return models[0]

        self.actions: list[SelectAction] = [
            SelectAction(model) for model in models]

        while self.is_running:
            self.execute_turn()

        return self.selection

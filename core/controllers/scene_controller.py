from __future__ import annotations
from typing import TYPE_CHECKING

from core.actions.base_action import BaseAction
from core.controllers.controller import Controller

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.views.view import View


class SceneController(Controller):
    """
    Abstract class representing a scene controller.
    """

    def __init__(self, dungeon: Dungeon, view: View, actions: list[BaseAction], pinned: dict[str, BaseAction]) -> None:
        """
        Constructor creating a new scene controller

        Arguments:
        dungeon - the current dungeon
        view - the view used to render the scene
        """
        super().__init__(dungeon, view, actions, pinned)

    def start(self) -> None:
        """
        Start the controller.
        """
        while self.is_running:
            actions, pinned = self.filter_actions()

            self.view.show()
            self.view.show_actions(actions, pinned)

            action = self.get_action(actions, pinned)

            if not action:
                continue

            pass_turn = action.execute(self)

            if not pass_turn:
                continue

            input('next turn')

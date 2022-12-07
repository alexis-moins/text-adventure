from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING

from core.actions.base_action import BaseAction
from core.controllers.controller import Controller

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.views.view import View


class SceneController(ABC, Controller):
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

    def on_next_turn(self) -> None:
        """
        Method called whenever the end of turn is reached.
        Does nothing by default.
        """
        pass

    def start(self) -> None:
        """
        Start the controller.
        """
        while self.is_running and self.dungeon.player.is_alive():
            actions, pinned = self.filter_actions()

            self.view.show(actions, pinned)
            action = self.get_action(actions, pinned)

            if not action:
                continue

            pass_turn = action.execute(self)

            if not pass_turn:
                continue

            self.on_next_turn()

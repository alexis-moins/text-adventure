from __future__ import annotations
from typing import TYPE_CHECKING

from core.actions.base_action import BaseAction
from core.controllers.controller import Controller
from core.entities.npc import NPC

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.views.view import View


class SceneController(Controller):

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
        self.dungeon.next_turn()

    def on_quit(self) -> None:
        """
        Method called whenever the QuitAction is executed in
        the controller. Does nothing by default.
        """
        pass

    def execute_turn(self) -> None:
        """
        Dispay the controller view on screen, then ask for
        input to finally execute the corresponding action.
        """
        actions, pinned = self.filter_actions(self)

        self.view.show(actions, pinned)
        action = self.get_action(actions, pinned)

        if not action:
            return

        pass_turn = action.execute(self)

        if not pass_turn:
            return

        self.on_next_turn()

    def start(self) -> None:
        """
        Start the controller.
        """
        while self.is_running and self.dungeon.player.is_alive():
            self.execute_turn()

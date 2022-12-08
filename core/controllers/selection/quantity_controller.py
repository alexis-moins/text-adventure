from __future__ import annotations
from typing import TYPE_CHECKING

from core.containers.slot import Slot
from core.controllers.scene_controller import SceneController

if TYPE_CHECKING:
    from core.views.view import View
    from core.dungeon import Dungeon
    from core.actions.base_action import BaseAction


class QuantityController(SceneController):

    def __init__(self, dungeon: Dungeon, view: View,  pinned: dict[str, BaseAction]) -> None:
        """
        Constructor creating a new scene controller

        Arguments:
        dungeon - the current dungeon
        view - the view used to render the scene
        """
        super().__init__(dungeon, view, [], pinned)

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

    def select(self, slot: Slot) -> int:
        """
        Start the controller and ask the user to select exactly one
        item from a list of items.

        Argument:
        items - a list of items to choose from
        """
        while self.is_running:
            self.execute_turn()

        return 0

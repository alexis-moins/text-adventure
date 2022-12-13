from __future__ import annotations
from typing import TYPE_CHECKING

from core.controllers.scene_controller import SceneController
from core.actions.menu.quantity_select import QuantitySelectAction

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
        self.quantity = 1
        self.maximum = 0

    def get_action(self, _: list[BaseAction], pinned: dict[str, BaseAction]) -> BaseAction | None:
        """
        Format and parse the user input and return the corresponding action
        or None if the input was invalid.

        Argument:
        actions - list of actions the user can choose from
        pinned - list of the pinned actions the user can choose from

        Returns:
        A BaseAction or None
        """
        user_input = self.get_input()

        if user_input in pinned:
            return pinned[user_input]

        if not user_input.isnumeric():
            return None

        user_input = int(user_input)

        if user_input < 0:
            return None

        return QuantitySelectAction(user_input)

    def select(self, maximum: int) -> int:
        """
        Start the controller and ask the user to select exactly one
        item from a list of items.

        Argument:
        items - a list of items to choose from
        """
        self.maximum = maximum

        while self.is_running:
            self.execute_turn()

        return self.quantity

    def on_quit(self) -> None:
        """

        """
        self.quantity = 0

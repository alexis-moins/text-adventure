from __future__ import annotations

from typing import TYPE_CHECKING
from core.controllers import SceneController


if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.views.room_view import RoomView


class SelectionController(SceneController):
    """
    Controller used to interact with a room.
    """

    def __init__(self, dungeon: Dungeon, view: RoomView) -> None:
        """
        Constructor creating a new room controller.

        Arguments:
        dungeon - the currently opened dungeon
        view - the view associated with the controller
        """
        super().__init__(dungeon, view)

    def select(self, elements: list) -> None:
        """
        Start the controller.
        """
        while self.is_running:
            possible_actions = self.filter_actions()

            self.view.show(possible_actions)
            action = self.get_action(possible_actions)

            if not action:
                continue

            action.execute(self)

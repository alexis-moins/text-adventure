from __future__ import annotations

from typing import TYPE_CHECKING, Any
from core.controllers.selection.selector import Selector


if TYPE_CHECKING:
    from core.dungeon import Dungeon


class SelectionController(Selector):

    def __init__(self, dungeon: Dungeon, view) -> None:
        """
        Constructor creating a new menu to select one element
        from a given list.

        Arguments:
        dungeon - the currently opened dungeon
        view - the view associated with the controller
        """
        super().__init__(dungeon, view)

    def select(self, elements: list[Any]) -> None:
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

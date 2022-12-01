from __future__ import annotations
from typing import TYPE_CHECKING, Any

from core.actions.menu.quit_action import QuitAction
from core.actions.menu.select_action import SelectAction
from core.controllers.selection.selector import Selector


if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.views.selection.selection_view import SelectionMenu


class SelectionController(Selector):

    def __init__(self, dungeon: Dungeon, view: SelectionMenu) -> None:
        """
        Constructor creating a new menu to select one element
        from a given list.

        Arguments:
        dungeon - the currently opened dungeon
        view - the view associated with the controller
        """
        super().__init__(dungeon, view)
        self.add_pinned_actions(QuitAction(key='q'))

        self.selection = None

    def select(self, models: list[Any]) -> Any | None:
        """
        Start the controller and ask the user to select exactly one
        item from a list of items.

        Argument:
        items - a list of items to choose from
        """
        self.actions = [SelectAction(model) for model in models]

        while self.is_running:
            self.view.show()
            self.view.show_actions(
                self.actions, self.pinned, pinned_first=False)

            action = self.get_action(self.actions, self.pinned)

            if not action:
                continue

            action.execute(self)

            if self.selection:
                return self.selection

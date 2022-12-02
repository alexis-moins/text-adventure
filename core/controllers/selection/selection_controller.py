from __future__ import annotations
from typing import TYPE_CHECKING, Any

from core.controllers.controller import Controller
from core.actions.menu.select_action import SelectAction
from core.entities.npc import NPC


if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.actions.base_action import BaseAction
    from core.entities.describable import Describable
    from core.views.selection.selection_view import SelectionMenu


class SelectionController(Controller):

    def __init__(self, dungeon: Dungeon, view: SelectionMenu, actions: list[BaseAction], pinned: dict[str, BaseAction]) -> None:
        """
        Constructor creating a new menu to select one element
        from a given list.

        Arguments:
        dungeon - the currently opened dungeon
        view - the view associated with the controller
        """
        super().__init__(dungeon, view, actions, pinned)
        self.selection: Describable | None = None

    def select(self, models: list[NPC]) -> NPC | None:
        """
        Start the controller and ask the user to select exactly one
        item from a list of items.

        Argument:
        items - a list of items to choose from
        """
        self.actions: list[BaseAction] = [
            SelectAction(model) for model in models]

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

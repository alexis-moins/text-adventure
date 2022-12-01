from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.actions.base_action import BaseAction


class ActionHandler:
    """
    Class providing ways for controllers to manage actions.
    """

    def __init__(self, dungeon: Dungeon) -> None:
        """
        Constructor creating a new manager of controller actions.

        Argument:
        dungeon - the current dungeon
        """
        self.dungeon = dungeon

        self.actions: list[BaseAction] = []
        self.pinned: dict[str, BaseAction] = {}

    def add_actions(self, *actions: BaseAction) -> None:
        """
        Add the given actions to the controller. Note that the actions
        will be displayed in the order they were added in.

        Argument:
        actions - the tuple of all BaseActions passed to the function
        """
        self.actions.extend(actions)

    def add_pinned_actions(self, *actions: BaseAction) -> None:
        """"""
        self.pinned.update(
            {action.key: action for action in actions if action.key})

    def filter_actions(self) -> tuple[list[BaseAction], dict[str, BaseAction]]:
        """
        Filter the actions available in the current context from the
        list of all possible actions in the handler.

        Returns:
        A tuple comprised of
        • a list of anonymous actions
        • a dictionary of pinned actions and their keys
        """
        actions = [action for action in self.actions
                   if action.can_be_performed(self.dungeon)]

        pinned = {key: action for key, action in self.pinned.items()
                  if action.can_be_performed(self.dungeon)}

        return actions, pinned

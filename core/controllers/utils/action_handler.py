from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.actions.base_action import BaseAction
    from core.actions.action_group import ActionGroup


class ActionHandler:
    """
    Class providing ways for controllers to manage actions.
    """

    def __init__(self, dungeon: Dungeon, actions: list[BaseAction], pinned: list[ActionGroup]) -> None:
        """
        Constructor creating a new manager of controller actions.

        Argument:
        dungeon - the current dungeon
        """
        self.dungeon = dungeon
        self.actions = actions
        self.pinned = pinned

    def filter_actions(self, controller) -> tuple[list[BaseAction], list[ActionGroup]]:
        """
        Filter the actions available in the current context from the
        list of all possible actions in the handler.

        Returns:
        A tuple comprised of
        • a list of anonymous actions
        • a dictionary of pinned actions and their keys
        """
        actions = [action for action in self.actions
                   if action.can_be_performed(self.dungeon, controller)]

        pinned = [group.filter(self.dungeon, controller)
                  for group in self.pinned]

        return actions, pinned

from __future__ import annotations

from core.actions import BaseAction
from typing import TYPE_CHECKING, TypedDict


if TYPE_CHECKING:
    from core.dungeon import Dungeon


class ActionDict(TypedDict):
    """

    """
    key: dict[str, BaseAction]
    default: list[BaseAction]


class ActionManager:
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
        self.actions: ActionDict = {
            'key': {},
            'default': []
        }

    def add_actions(self, *actions: BaseAction) -> None:
        """
        Add the given actions to the controller. Note that the actions
        will be displayed in the order they were added in.

        Argument:
        actions - the tuple of all BaseActions passed to the function
        """
        for action in actions:
            if action.key:
                self.actions['key'][action.key] = action
            else:
                self.actions['default'].append(action)

    def filter_action_list(self, key: str) -> list[BaseAction]:
        """

        """
        return [action for action in self.actions[key]
                if action.can_be_performed(self.dungeon)]

    def filter_actions(self) -> ActionDict:
        """
        Filter the actions available in the current context from
        list of all the possible actions in the controller.

        Returns:
        An action dictionary
        """
        return {
            'default': self.filter_action_list('default'),
            'key': {
                key: action for key, action in self.actions['key'].items()
                if action.can_be_performed(self.dungeon)
            }
        }

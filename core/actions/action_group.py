from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.actions.base_action import BaseAction
    from core.controllers.scene_controller import SceneController


class ActionGroup:

    def __init__(self, actions: dict[str, BaseAction], color: str = 'green') -> None:
        """
        Create new action group composed of the given pinned actions.

        Arguments:
        actions - the (pinned) actions in the group
        color - the color used to dispay the group's actions
        """
        self.actions = actions
        self.color = color.upper()

    def filter(self, dungeon: Dungeon, controller: SceneController) -> ActionGroup:
        """
        Return a new ActionGroup containing the actions that can be achieved in the given
        context.

        Arguments:
        dungeon - the current dungeon
        controller - the controller of the current scene

        Returns:
        An ActionGroup
        """
        filtered_actions = {key: action for key, action in self.actions.items()
                            if action.can_be_performed(dungeon, controller)}

        return ActionGroup(filtered_actions, color=self.color)

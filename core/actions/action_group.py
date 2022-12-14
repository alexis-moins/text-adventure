from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.actions.base_action import BaseAction
    from core.controllers.scene_controller import SceneController


class ActionGroup:

    def __init__(self, actions: dict[str, BaseAction], *, color: str = 'GREEN') -> None:
        """

        """
        self.actions = actions
        self.color = color

    def filter(self, dungeon: Dungeon, controller: SceneController) -> ActionGroup:
        """
        Return a new ActionGroup

        """
        filtered_actions = {key: action for key, action in self.actions.items()
                            if action.can_be_performed(dungeon, controller)}

        return ActionGroup(filtered_actions, color=self.color)

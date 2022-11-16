from abc import ABC

from core.actions.base_action import BaseAction
from core.dungeon import Dungeon
from core.views.view import View


class Controller(ABC):
    """
    Abstract class representing a scene controller.
    """

    def __init__(self, dungeon: Dungeon, view: View) -> None:
        """
        Constructor creating a new abstract scene controller

        Arguments:
        dungeon - the current dungeon
        view - the view used to render the scene
        """
        self.dungeon = dungeon
        self.view = view

        self.is_running = True
        self.actions: list[BaseAction] = []

    def filter_actions(self) -> list[BaseAction]:
        """
        Filter the actions available in the current context from
        list of all the possible actions in the controlelr.

        Returns:
        A list of BaseAction
        """
        return [action for action in self.actions
                if action.can_be_performed(self.dungeon)]

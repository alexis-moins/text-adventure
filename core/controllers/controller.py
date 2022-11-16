from abc import ABC

import core.actions.base_action as base_action
from core.controllers.parser import Parser
from core.dungeon import Dungeon
from core.views.view import View


class Controller(ABC, Parser):
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
        self.actions: list[base_action.BaseAction] = []

    def filter_actions(self) -> list[base_action.BaseAction]:
        """
        Filter the actions available in the current context from
        list of all the possible actions in the controlelr.

        Returns:
        A list of BaseAction
        """
        return [action for action in self.actions
                if action.can_be_performed(self.dungeon)]

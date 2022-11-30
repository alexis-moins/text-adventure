from abc import ABC, abstractmethod

from core.controllers.action_manager import ActionManager
from core.controllers.parser import Parser
from core.dungeon import Dungeon
from core.views.view import View


class SceneController(ABC, ActionManager, Parser):
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
        super().__init__(dungeon)
        self.is_running = True

        self.dungeon = dungeon
        self.view = view

    @abstractmethod
    def start(self) -> None:
        """
        Start the controller.
        """
        pass

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
        actions - the list of action classes that may be performed in the context of the controller
        """
        self.dungeon = dungeon
        self.view = view

        self.is_running = True
        self.actions: list[BaseAction] = []

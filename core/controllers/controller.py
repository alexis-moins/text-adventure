from abc import ABC

from core.dungeon import Dungeon
from core.views.view import View


class Controller(ABC):
    """
    Abstract class representing a scene controller.
    """

    def __init__(self, dungeon: Dungeon, view: View) -> None:
        """
        Constructor creating a new abstract scene controller
        """
        self.dungeon = dungeon

        self.view = view
        self.is_running = True

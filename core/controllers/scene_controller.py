from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from core.controllers.controller import Controller


if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.views.view import View


class SceneController(ABC, Controller):
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
        super().__init__(dungeon, view)

    @abstractmethod
    def start(self) -> None:
        """
        Start the controller.
        """
        pass

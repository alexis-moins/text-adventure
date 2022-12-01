from __future__ import annotations
from typing import TYPE_CHECKING

from core.controllers.utils.parser import Parser
from core.controllers.utils.action_handler import ActionHandler


if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.views.view import View


class Controller(ActionHandler, Parser):

    def __init__(self, dungeon: Dungeon, view: View) -> None:
        """
        Constructor creating a new bare controller.

        Arguments:
        dungeon - the current dungeon
        view - the view used to render the scene
        """
        super().__init__(dungeon)
        self.is_running = True
        self.view = view

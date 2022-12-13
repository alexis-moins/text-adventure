from __future__ import annotations

from typing import TYPE_CHECKING
from core.views.view import View

if TYPE_CHECKING:
    from core.dungeon import Dungeon


class MessageView(View):

    def __init__(self, dungeon: Dungeon, message: str) -> None:
        """
        Constructor creating a new menu to select exactly one
        item from a selection of items.
        """
        super().__init__(dungeon)
        self.message = message

    def on_show(self) -> None:
        """
        Show the menu on screen.
        """
        self.b.new_line().add(self.message)

    def update_message(self, message: str) -> None:
        """

        """
        self.message

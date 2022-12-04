from __future__ import annotations

from typing import TYPE_CHECKING
from core.views.view import View

if TYPE_CHECKING:
    from core.dungeon import Dungeon


class Message(View):

    def __init__(self, dungeon: Dungeon, message: str) -> None:
        """
        Constructor creating a new message.

        Arguments:
        dungeon - the currently opened dungeon
        message - the message to display on screen
        """
        super().__init__(dungeon)
        self.message = message

    def show(self) -> None:
        """
        Show the message on screen, then log the message in
        the dungeon history.
        """
        self.clear_screen()

        self.b.add('\n').add(self.message)
        self.b.add('\n').add('-- GREENEnterWHITE --')

        input(self.b.build())

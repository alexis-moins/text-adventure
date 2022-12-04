from __future__ import annotations

from typing import TYPE_CHECKING
from core.views.view import View

if TYPE_CHECKING:
    from core.dungeon import Dungeon


class Menu(View):

    def __init__(self, dungeon: Dungeon, prompt: str) -> None:
        """
        Constructor creating a new bare menu interface.
        """
        super().__init__(dungeon, pinned_first=False)
        self.prompt = prompt


class SelectionMenu(Menu):

    def __init__(self, dungeon: Dungeon, prompt: str) -> None:
        """
        Constructor creating a new menu to select exactly one
        item from a selection of items.
        """
        super().__init__(dungeon, prompt)

    def on_show(self) -> None:
        """
        Show the menu on screen.
        """
        self.b.new_line().add(self.prompt)

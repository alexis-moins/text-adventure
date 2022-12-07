from __future__ import annotations

from typing import TYPE_CHECKING
from core.views.view import View

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.fight.fighter import Fighter


class InventoryView(View):

    def __init__(self, dungeon: Dungeon, fighter: Fighter) -> None:
        """
        Constructor creating a new scenery for an inventory.

        Arguments:
        dungeon - the currently opened dungeon
        """
        super().__init__(dungeon)
        self.fighter = fighter

    def on_show(self) -> None:
        """
        Show the scenery on screen.
        """
        self.show_status_bar()

        self.fighetr

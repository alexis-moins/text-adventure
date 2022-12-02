from __future__ import annotations

from typing import TYPE_CHECKING
from core.views.scenery import Scenery

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.generation.room import Room


class InventoryScenery(Scenery):

    def __init__(self, dungeon: Dungeon, room: Room) -> None:
        """
        Constructor creating a new scenery for an inventory.

        Arguments:
        dungeon - the currently opened dungeon
        room - the room used for the scenery
        """
        super().__init__(dungeon, room)

    def show(self) -> None:
        """
        Show the scenery on screen.
        """
        self.clear_screen()
        self.show_status_bar()

        print(self.model.long_description())

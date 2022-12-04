from __future__ import annotations

from typing import TYPE_CHECKING
from core.views.scenery import Scenery

if TYPE_CHECKING:
    from core.room import Room
    from core.dungeon import Dungeon


class RoomScenery(Scenery):

    def __init__(self, dungeon: Dungeon, room: Room) -> None:
        """
        Constructor creating a new scenery for a room.

        Arguments:
        dungeon - the currently opened dungeon
        room - the room used for the scenery
        """
        super().__init__(dungeon, room)

    def on_show(self) -> None:
        """
        Show the scenery on screen.
        """
        self.show_status_bar()
        self.b.add(self.model.long_description())

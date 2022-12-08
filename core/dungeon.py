from __future__ import annotations

from typing import TYPE_CHECKING
from core.controllers.utils.controller_factory import ControllerFactory
from core.entities.npc import NPC
from core.utils.strings import StringBuilder
from core.views.message import Message

if TYPE_CHECKING:
    from core.room import Room
    from core.entities.player import Player


class Dungeon:
    """
    Class representing the current dungeon. It contains the current
    room as well as the current player.
    """

    def __init__(self, player: Player, start: Room) -> None:
        """
        Constructor creating a new dungeon.

        Arguments:
        player - the player
        start - the starting room
        """
        self.player = player
        self.room = start

        self.factory = ControllerFactory(self)
        self.b = StringBuilder()

    def add_log(self, log: str) -> None:
        """

        """
        self.b.add(log)

    def show_logs(self) -> None:
        """

        """
        if not self.b.is_empty():
            message = Message(self, self.b.build())
            message.show()

    def next_turn(self) -> None:
        """"""
        npcs: list[NPC] = self.room.npc.get_entities()  # type: ignore

        for npc in npcs:

            if not npc.is_alive():
                npc.die(self)
                continue

            npc.take_turn(self)

        self.show_logs()

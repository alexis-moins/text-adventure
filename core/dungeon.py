from __future__ import annotations

from typing import TYPE_CHECKING
from core.controllers.utils.controller_factory import ControllerFactory

if TYPE_CHECKING:
    from core.generation.room import Room
    from core.entities.player import Player


class Dungeon:
    """
    Class representing the current dungeon. It contains the current
    room as well as the current player.
    """

    def __init__(self, player: Player, start: Room) -> None:
        """

        """
        self.player = player
        self.room = start

        self.factory = ControllerFactory(self)

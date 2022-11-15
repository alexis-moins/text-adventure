from core.entities.player import Player
from core.generation.room import Room


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

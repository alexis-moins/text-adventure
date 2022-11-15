from core.dungeon import Dungeon
from core.generation.room import Room
from core.views.view import View


class RoomView(View):
    """
    View used to render a room.
    """

    def __init__(self, dungeon: Dungeon, room: Room) -> None:
        """

        """
        super().__init__(dungeon, room, [])

    def show(self) -> None:
        """
        Show the scenery on screen.
        """
        print(self.model.long_description())

        self._show_actions()

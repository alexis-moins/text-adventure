from core.actions.base_action import BaseAction
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
        super().__init__(dungeon, room)

    def show(self, actions: list[BaseAction]) -> None:
        """
        Show the scenery on screen.

        Argument:
        actions - the list of available action types
        """
        self.clear()

        print(self.model.long_description())

        self.show_actions(actions)

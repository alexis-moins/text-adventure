from core.controllers.controller import Controller
from core.dungeon import Dungeon
from core.views.room_view import RoomView


class RoomController(Controller):
    """
    Controller used to interact with a room.
    """

    def __init__(self, dungeon: Dungeon, view: RoomView) -> None:
        """
        Constructor creating a new room controller.

        Arguments:
        dungeon - the currently opened dungeon
        view - the view associated with the controller
        """
        super().__init__(dungeon, view)

    def start(self) -> None:
        """
        Start the controller
        """
        while self.is_running:
            self.view.show()

            actions = self.view.actions

            input()

            # cost_a_turn = self.player.take_turn()

            # if not cost_a_turn:
            # continue

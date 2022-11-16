from core.actions.base_action import BaseAction
from core.actions.list.attack import AttackAction
from core.actions.list.quit import QuitAction
from core.controllers.controller import Controller
from core.dungeon import Dungeon
from core.engine.parser import get_input
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
        self.actions.extend((
            QuitAction(),
            AttackAction()
        ))

    def start(self) -> None:
        """
        Start the controller
        """
        while self.is_running:
            possible_actions = self.filter_actions()

            self.view.show(possible_actions)

            _input = get_input()

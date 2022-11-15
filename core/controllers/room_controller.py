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
    _actions: list[BaseAction] = [
        QuitAction(),
        AttackAction()
    ]

    def __init__(self, dungeon: Dungeon, view: RoomView) -> None:
        """
        Constructor creating a new room controller.

        Arguments:
        dungeon - the currently opened dungeon
        view - the view associated with the controller
        """
        super().__init__(dungeon, view)
        self.actions.extend(self._actions)

    def start(self) -> None:
        """
        Start the controller
        """
        while self.is_running:
            self.view.show(self.actions)

            _input = get_input()

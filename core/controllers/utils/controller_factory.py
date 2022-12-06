from __future__ import annotations
from typing import TYPE_CHECKING

from core.actions.menu.quit_action import QuitAction
from core.actions.scene.attack_action import AttackAction
from core.actions.scene.wait_action import WaitAction
from core.controllers.room_controller import RoomController

from core.controllers.scene_controller import SceneController
from core.controllers.selection.selection_controller import SelectionController

from core.views.sceneries.room_scenery import RoomScenery
from core.views.selection.selection_view import SelectionMenu

if TYPE_CHECKING:
    from core.room import Room
    from core.dungeon import Dungeon


class ControllerFactory:
    """
    Class providing static factory methods for creating controllers.
    """

    def __init__(self, dungeon: Dungeon) -> None:
        """
        Constructor creating the controller factory.
        """
        self._dungeon = dungeon

    def room_controller(self, room: Room) -> SceneController:
        """
        Return a new room controller.
        """
        return RoomController(self._dungeon, RoomScenery(self._dungeon, room),
                              [
            WaitAction(self._dungeon),
            AttackAction(self._dungeon)
        ],
            {
            'q': QuitAction(self._dungeon)
        })

    def selection_controller(self, prompt: str, *, multi: bool = False) -> SelectionController:
        """

        """
        return SelectionController(self._dungeon, SelectionMenu(self._dungeon, prompt),
                                   [],
                                   {'q': QuitAction(self._dungeon)})

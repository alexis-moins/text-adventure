from __future__ import annotations
from typing import TYPE_CHECKING

from core.actions.menu.quit_action import QuitAction
from core.actions.scene.attack_action import AttackAction
from core.actions.scene.drop_item_action import DropItemAction
from core.actions.scene.open_inventory_action import OpenInventoryAction
from core.actions.scene.take_item_action import TakeItemAction
from core.actions.scene.wait_action import WaitAction
from core.controllers.room_controller import RoomController

from core.controllers.scene_controller import SceneController
from core.controllers.selection.selection_controller import SelectionController
from core.views.sceneries.inventory_scenery import InventoryView

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
        self.dungeon = dungeon

    def room_controller(self, room: Room) -> SceneController:
        """
        Return a new room controller.

        Argument:
        room - the room to be displayed
        """
        actions = [
            WaitAction(),
            AttackAction(self.dungeon.player),
            TakeItemAction(self.dungeon.player.inventory)
        ]

        pinned = {
            'i': OpenInventoryAction(self.dungeon.player.inventory),
            'q': QuitAction()
        }

        return RoomController(self.dungeon, RoomScenery(self.dungeon, room), actions, pinned)

    def selection_controller(self, prompt: str, *, multi: bool = False) -> SelectionController:
        """

        """
        return SelectionController(self.dungeon, SelectionMenu(self.dungeon, prompt),
                                   [],
                                   {'q': QuitAction('Cancel')})

    def inventory_controller(self) -> SceneController:
        """
        Return a new controller over an inventory.
        """
        actions = [
            DropItemAction(self.dungeon.player.inventory)
        ]

        pinned = {
            'q': QuitAction('Close')
        }

        return SceneController(self.dungeon, InventoryView(self.dungeon, self.dungeon.player), actions, pinned)

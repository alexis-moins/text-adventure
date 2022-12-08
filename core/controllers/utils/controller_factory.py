from __future__ import annotations
from typing import TYPE_CHECKING
from core.actions.base_action import BaseAction

from core.actions.menu.quit_action import QuitAction
from core.actions.menu.select_all_action import SelectAllAction
from core.actions.menu.unselect_all_action import UnselectAllAction
from core.actions.menu.validate_action import ValidateAction
from core.actions.scene.attack_action import AttackAction
from core.actions.scene.drop_item_action import DropItemAction
from core.actions.scene.equip_action import EquipAction
from core.actions.scene.open_inventory_action import OpenInventoryAction
from core.actions.scene.take_item_action import TakeItemAction
from core.actions.scene.wait_action import WaitAction
from core.controllers.room_controller import RoomController

from core.controllers.scene_controller import SceneController
from core.controllers.selection.multi_selection_controller import MultiSelectionController
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

    def selection_controller(self, prompt: str) -> SelectionController:
        """

        """
        pinned: dict[str, BaseAction] = {
            'q': QuitAction('Cancel')
        }

        return SelectionController(self.dungeon, SelectionMenu(self.dungeon, prompt), pinned)

    def multi_selection_controller(self, prompt: str) -> MultiSelectionController:
        """
        Return a new controller to select multiple items from a given list.

        Returns:
        A MultiSelectionController
        """
        pinned = {
            'q': QuitAction('Cancel'),
            'a': SelectAllAction(),
            'u': UnselectAllAction(),
            'v': ValidateAction()
        }

        return MultiSelectionController(self.dungeon, SelectionMenu(self.dungeon, prompt), pinned)

    def inventory_controller(self) -> SceneController:
        """
        Return a new controller over an inventory.
        """
        actions = [
            EquipAction(self.dungeon.player.inventory),
            DropItemAction(self.dungeon.player.inventory)
        ]

        pinned = {
            'q': QuitAction('Close')
        }

        return SceneController(self.dungeon, InventoryView(self.dungeon, self.dungeon.player), actions, pinned)

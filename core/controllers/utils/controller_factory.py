from __future__ import annotations
from typing import TYPE_CHECKING
from core.actions.action_group import ActionGroup
from core.actions.base_action import BaseAction

from core.actions.menu.quit_action import QuitAction
from core.actions.menu.select_all_action import SelectAllAction
from core.actions.menu.unselect_all_action import UnselectAllAction
from core.actions.menu.validate_action import ValidateAction
from core.actions.scene.attack_action import AttackAction

from core.actions.scene.inventory.equip_action import EquipAction
from core.actions.scene.inventory.drop_action import DropItemAction
from core.actions.scene.inventory.drink_potion import DrinkPotionAction
from core.actions.scene.trade_action import TradeAction

from core.actions.scene.wait_action import WaitAction
from core.actions.scene.take_action import TakeItemAction
from core.actions.scene.inventory_action import InventoryAction

from core.controllers.scene_controller import SceneController
from core.controllers.selection.multi_selection_controller import MultiSelectionController
from core.controllers.selection.selection_controller import SelectionController
from core.views.sceneries.inventory_view import InventoryView

from core.views.sceneries.room_scenery import RoomScenery
from core.views.message_view import MessageView

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

    def room_scene(self, room: Room) -> SceneController:
        """
        Return a new room controller.

        Argument:
        room - the room to be displayed

        Returns:
        A SceneController
        """
        pinned = {
            'i': InventoryAction(self.dungeon),
            'q': QuitAction(self.dungeon)
        }
        actions = [

            WaitAction(self.dungeon),
            AttackAction(self.dungeon),
            TakeItemAction(self.dungeon),
            TradeAction(self.dungeon)
        ]

        return SceneController(self.dungeon, RoomScenery(self.dungeon, room),
                               actions, [ActionGroup(pinned)])

    def selection(self, prompt: str) -> SelectionController:
        """
        Return a new controller to select exactly one element from a given list.

        Argument:
        prompt - the prompt to display

        Returns:
        A SelectionController
        """
        pinned: dict[str, BaseAction] = {
            'q': QuitAction(self.dungeon, 'Cancel')
        }

        return SelectionController(self.dungeon, MessageView(self.dungeon, prompt),
                                   [ActionGroup(pinned)])

    def multi_selection(self, prompt: str) -> MultiSelectionController:
        """
        Return a new controller to select multiple items from a given list.

        Argument:
        prompt - the prompt to display

        Returns:
        A MultiSelectionController
        """
        pinned = {
            'q': QuitAction(self.dungeon, 'Cancel'),
            'a': SelectAllAction(self.dungeon),
            'u': UnselectAllAction(self.dungeon)
        }

        secondary_group = ActionGroup(
            {'v': ValidateAction(self.dungeon)}, color='MAGENTA')

        return MultiSelectionController(self.dungeon, MessageView(self.dungeon, prompt),
                                        [ActionGroup(pinned), secondary_group])

    def quantity_selection_controller(self, prompt: str) -> MultiSelectionController:
        """
        Return a controller to select an arbitrary quantity.

        Argument:
        prompt - the prompt to display

        Returns:
        A MultiSelectionController
        """
        controller = self.multi_selection(prompt)
        controller.pinned[1].actions['s'] = QuitAction(self.dungeon, 'test')

        return controller

    def inventory_controller(self) -> SceneController:
        """
        Return a new controller over an inventory.

        Returns:
        A SceneController
        """
        actions = [
            EquipAction(self.dungeon),
            DropItemAction(self.dungeon),
            DrinkPotionAction(self.dungeon)
        ]

        return SceneController(self.dungeon, InventoryView(self.dungeon, self.dungeon.player),
                               actions, [ActionGroup({'q': QuitAction(self.dungeon, 'Close')})])

    def message_controller(self, message: str) -> SceneController:
        """
        Return a scene controller displaying the given message and waiting
        for confirmation to give back control.

        Argument:
        message - the message to display

        Returns:
        A SceneController
        """
        return SceneController(self.dungeon, MessageView(self.dungeon, message),
                               [], [ActionGroup({'c': QuitAction(self.dungeon, 'Continue')})])

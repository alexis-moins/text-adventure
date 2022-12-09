from __future__ import annotations

from typing import TYPE_CHECKING
from core.actions.base_action import BaseAction
from core.containers.slot import Slot
from core.entities.describable import Describable

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.containers.inventory import Inventory
    from core.controllers.controller import Controller
    from core.controllers.scene_controller import SceneController


class TakeItemAction(BaseAction):

    def __init__(self, inventory: Inventory) -> None:
        """
        Constructor creating a new action of dropping one (or more)
        items in the room.

        Argument:
        inventory - the inventory to drop from
        """
        super().__init__()
        self.inventory = inventory

    def can_be_performed(self, context: Dungeon, controller: Controller) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        context - the current dungeon

        Returns:
        a boolean
        """
        return bool(context.room.items)

    def execute(self, context: SceneController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the controller of the current scene

        Returns:
        A boolean
        """
        items = context.dungeon.room.items.slots

        slots: list[Slot] = context.dungeon.factory.multi_selection_controller(
            'Which item(s) do you want to take :').select(items)  # type: ignore

        if not slots:
            return False

        for slot in slots:
            context.dungeon.player.inventory.add_slot(slot)
            context.dungeon.room.items.remove_slot(slot)

        return True

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.b.add(f'Take').build()

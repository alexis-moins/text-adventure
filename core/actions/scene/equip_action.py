from __future__ import annotations

from typing import TYPE_CHECKING
from core.actions.base_action import BaseAction
from core.items.equipable import Equipable

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.containers.inventory import Inventory
    from core.controllers.scene_controller import SceneController


class EquipAction(BaseAction):
    """
    Class representing the action of wearing / holding a piece of equipment.
    """

    def __init__(self, inventory: Inventory) -> None:
        """
        Constructor creating a new action to equip something.

        Argument:
        inventory - the inventory to open
        """
        super().__init__()
        self.inventory = inventory

    def can_be_performed(self, _: Dungeon) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        context - the current dungeon

        Returns:
        a boolean
        """
        return len(self.inventory.filter(Equipable)) > 0

    def execute(self, context: SceneController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the controller of the current scene

        Returns:
        A boolean
        """
        selector = context.dungeon.factory.selection_controller(
            'Which equipment(s) do you want to wear :')

        selector.start(self.inventory.filter(Equipable))

        equipment = selector.selection
        if not equipment:
            return False

        context.dungeon.player.inventory.equip(equipment)
        return True

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.b.add('Wear or hold').build()

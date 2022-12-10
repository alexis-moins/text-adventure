from __future__ import annotations

from typing import TYPE_CHECKING
from core.actions.base_action import BaseAction
from core.items.equipable import Equipable

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.containers.inventory import Inventory
    from core.controllers.controller import Controller
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

    def can_be_performed(self, _: Dungeon, controller: Controller) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        context - the current dungeon

        Returns:
        a boolean
        """
        return not all([e.is_equiped for e in self.inventory.filter(Equipable)])

    def execute(self, context: SceneController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the controller of the current scene

        Returns:
        A boolean
        """
        items = [equipment for equipment in self.inventory.filter(
            Equipable) if not equipment.is_equiped]

        equipments: list[Equipable] = context.dungeon.factory.multi_selection_controller(
            'Which equipment(s) do you want to wear :').select(items)  # type: ignore

        if not equipments:
            return False

        for equipment in equipments:
            context.dungeon.player.equip(equipment)

        return True

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.b.add('Wear or hold').build()

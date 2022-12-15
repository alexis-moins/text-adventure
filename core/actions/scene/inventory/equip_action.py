from __future__ import annotations

from typing import TYPE_CHECKING
from core.actions.base_action import BaseAction
from core.items.equipable import Equipable

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.controllers.controller import Controller
    from core.controllers.scene_controller import SceneController


class EquipAction(BaseAction):
    """
    Class representing the action of wearing / holding a piece of equipment.
    """

    def __init__(self, dungeon: Dungeon) -> None:
        """
        Constructor creating a new action to equip something.

        Argument:
        dungeon - the current dungeon
        """
        super().__init__(dungeon)
        self.character = dungeon.player

    def can_be_performed(self, _: Controller) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        controller - the current controller

        Returns:
        a boolean
        """
        return not all([equipment.is_equiped
                        for equipment in self.character.inventory.filter(Equipable)])

    def execute(self, _: SceneController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the current controller

        Returns:
        A boolean
        """
        items = [equipment for equipment in self.character.inventory.filter(
            Equipable) if not equipment.is_equiped]

        equipments = self.dungeon.architect.multi_selection(
            'Which equipment(s) do you want to wear :').start(items)

        if not equipments:
            return False

        for equipment in equipments:
            self.dungeon.player.equip(equipment)

        return True

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.b.add('Wear or hold').build()

from __future__ import annotations

from typing import TYPE_CHECKING

from core.items.potion import Potion
from core.actions.base_action import BaseAction

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.controllers.controller import Controller
    from core.controllers.scene_controller import SceneController


class DrinkPotionAction(BaseAction):

    def __init__(self, dungeon: Dungeon) -> None:
        """
        Constructor creating a new action of dropping one (or more)
        items in the room.

        Argument:
        dungeon - the current dungeon
        """
        super().__init__(dungeon)
        self.fighter = dungeon.player

    def can_be_performed(self, _: Controller) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        controller - the current controller

        Returns:
        a boolean
        """
        return bool(self.fighter.inventory.filter(Potion))

    def execute(self, _: SceneController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the current controller

        Returns:
        A boolean
        """
        items = self.fighter.inventory.filter(Potion)

        potion = self.dungeon.architect.selection(
            'Which potion do you want to drink :').start(items)

        if not potion:
            return False

        potion.drink(self.fighter)

        self.dungeon.add_log(f'You drink your YELLOW{potion.name}WHITE.')
        self.dungeon.add_log(potion.drink_sentence())
        return True

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.b.add(f'Drink').build()

from __future__ import annotations

from typing import TYPE_CHECKING
from core.actions.base_action import BaseAction
from core.fight.fighter import Fighter
from core.items.potion import Potion

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.controllers.controller import Controller
    from core.controllers.scene_controller import SceneController


class DrinkPotionAction(BaseAction):

    def __init__(self, fighter: Fighter) -> None:
        """
        Constructor creating a new action of dropping one (or more)
        items in the room.

        Argument:
        inventory - the inventory to drop from
        """
        super().__init__()
        self.fighter = fighter

    def can_be_performed(self, _: Dungeon, controller: Controller) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        context - the current dungeon

        Returns:
        a boolean
        """
        return bool(self.fighter.inventory.filter(Potion))

    def execute(self, context: SceneController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the controller of the current scene

        Returns:
        A boolean
        """
        items = self.fighter.inventory.filter(Potion)

        potion: Potion | None = context.dungeon.factory.selection_controller(
            'Which potion do you want to drink :').select(items)  # type: ignore

        if not potion:
            return False

        potion.drink(self.fighter)

        context.dungeon.add_log(f'You drink your YELLOW{potion.name}WHITE.')
        context.dungeon.add_log(potion.drink_sentence())
        return True

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.b.add(f'Drink').build()

from __future__ import annotations
from typing import TYPE_CHECKING

from core.actions.base_action import BaseAction

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.entities.character import Character
    from core.controllers.controller import Controller
    from core.controllers.scene_controller import SceneController


class TakeItemAction(BaseAction):

    def __init__(self, character: Character) -> None:
        """
        Constructor creating a new action of dropping one (or more)
        items in the room.

        Argument:
        inventory - the inventory to drop from
        """
        super().__init__()
        self.character = character

    def can_be_performed(self, context: Dungeon, _: Controller) -> bool:
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
        slots = context.dungeon.room.items.slots

        slots = context.dungeon.factory.multi_selection_controller(
            'Which item(s) do you want to take :').start(slots)

        if not slots:
            return False

        for slot in slots:
            items = context.dungeon.factory.quantity_selection_controller(
                f'How many YELLOW{slot.first_entity.name}WHITE to you want to take :').start(slot.entities)

            for item in items:
                self.character.take(item)
                context.dungeon.room.items.remove(item)

        return True

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.b.add(f'Take').build()
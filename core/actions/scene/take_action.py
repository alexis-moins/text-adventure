from __future__ import annotations
from typing import TYPE_CHECKING

from core.actions.base_action import BaseAction

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.controllers.controller import Controller
    from core.controllers.scene_controller import SceneController


class TakeItemAction(BaseAction):

    def __init__(self, dungeon: Dungeon) -> None:
        """
        Constructor creating a new action of dropping one (or more)
        items in the room.

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
        return bool(self.dungeon.current_room.items)

    def execute(self, _: SceneController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the controller of the current scene

        Returns:
        A boolean
        """
        slots = self.dungeon.current_room.items.slots

        slots = self.dungeon.architect.multi_selection(
            'Which item(s) do you want to take :').start(slots)

        if not slots:
            return False

        for slot in slots:
            items = self.dungeon.architect.quantity_selection_controller(
                f'How many YELLOW{slot.first_entity.name}WHITE to you want to take :').start(slot.entities)

            for item in items:
                self.character.take(item)
                self.dungeon.current_room.items.remove(item)

        return True

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.b.add(f'Take').build()

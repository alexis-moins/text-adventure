from __future__ import annotations

from typing import TYPE_CHECKING
from core.entities.npc import NPC
from core.views.message import Message
from core.actions.base_action import BaseAction

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.controllers.scene_controller import SceneController


class AttackAction(BaseAction):
    """
    Class representing the action of attacking an entity in the room.
    """

    def can_be_performed(self, context: Dungeon) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        context - the current dungeon

        Returns:
        a boolean
        """
        return len(context.room.entities) > 0

    def execute(self, controller: SceneController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the controller of the current scene

        Returns:
        A boolean
        """
        selector = controller.dungeon.factory.selection_controller(
            'Who will be the target of your attack ?')

        selector.start(controller.dungeon.room.npc)
        enemy: NPC = selector.selection

        if not enemy:
            return False

        damage = controller.dungeon.player.strength
        enemy.receive_damage(damage)

        message = Message(controller.dungeon,
                          f'You deal YELLOW{damage} damageWHITE to the {enemy.short_description()}.')

        message.show()
        return True

    def __str__(self) -> str:
        """
        Return the string used to render the action.

        Returns:
        A string
        """
        return 'attack'

from __future__ import annotations

from typing import TYPE_CHECKING
from core.views.message import Message
from core.actions.base_action import BaseAction

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.fight.fighter import Fighter
    from core.controllers.scene_controller import SceneController


class AttackAction(BaseAction):
    """
    Class representing the action of attacking an entity in the room.
    """

    def __init__(self, fighter: Fighter) -> None:
        """
        Constructor creating a new attack action.

        Argument:
        fighter - the actor making the action
        """
        super().__init__()
        self.fighter = fighter

    def can_be_performed(self, context: Dungeon, _: SceneController) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        context - the current dungeon

        Returns:
        a boolean
        """
        return len(context.room.npc) > 0

    def execute(self, controller: SceneController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the controller of the current scene

        Returns:
        A boolean
        """
        enemy = controller.dungeon.factory.selection_controller(
            'Who will be the target of your attack :').select(controller.dungeon.room.npc.get_entities())

        if not enemy:
            return False

        damage = self.fighter.get_damage()
        enemy.receive_damage(damage)

        damage = enemy.mitigate_damage(damage)

        message = f'You deal YELLOW{damage} damageWHITE to the {enemy.name}.'

        if not damage:
            message = f'You YELLOWmissWHITE the {enemy.name}'

        message = Message(controller.dungeon, message)

        message.show()
        return True

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        weapon = self.fighter.inventory.equipments.get('weapon')
        weapon_name = 'bare hands' if not weapon else weapon.name

        return self.b.add(f'Attack YELLOW(with your {weapon_name})WHITE').build()

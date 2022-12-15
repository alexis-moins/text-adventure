from __future__ import annotations

from typing import TYPE_CHECKING
from core.actions.base_action import BaseAction

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.entities.character import Character
    from core.controllers.scene_controller import SceneController


class AttackAction(BaseAction):
    """
    Class representing the action of attacking an entity in the room.
    """

    def __init__(self, character: Character) -> None:
        """
        Constructor creating a new attack action.

        Argument:
        character - the actor making the action
        """
        super().__init__()
        self.character = character

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
        npcs = controller.dungeon.room.npc.get_entities()

        target = controller.dungeon.factory.selection_controller(
            'Who will be the target of your attack :').start(npcs, auto_select=True)

        if not target:
            return False

        effective_damage = self.character.attack(target)
        message = f'You deal YELLOW{effective_damage} damageWHITE to the {target.name}.'

        if not effective_damage:
            message = f'You YELLOWmissWHITE the {target.name}'

        controller.dungeon.add_log(message + '\n')
        return True

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        weapon = self.character.equipments.get('weapon')
        weapon_name = 'bare hands' if not weapon else weapon.name

        return self.b.add(f'Attack YELLOW(with your {weapon_name})WHITE').build()

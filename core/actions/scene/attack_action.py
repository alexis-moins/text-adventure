from __future__ import annotations

from typing import TYPE_CHECKING
from core.actions.base_action import BaseAction

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.controllers.scene_controller import SceneController


class AttackAction(BaseAction):
    """
    Class representing the action of attacking an entity in the room.
    """

    def __init__(self, dungeon: Dungeon) -> None:
        """
        Constructor creating a new attack action.

        Argument:
        dungeon - the current dungeon
        """
        super().__init__(dungeon)
        self.character = dungeon.player

    def can_be_performed(self, _: SceneController) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        controller - the current controller

        Returns:
        a boolean
        """
        return len(self.dungeon.current_room.npc) > 0

    def execute(self, _: SceneController) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the current controller

        Returns:
        A boolean
        """
        npcs = self.dungeon.current_room.npc.get_entities()

        target = self.dungeon.architect.selection(
            'Who will be the target of your attack :').start(npcs)

        if not target:
            return False

        effective_damage = self.character.attack(target)
        message = f'You deal YELLOW{effective_damage} damageWHITE to the {target.name}.'

        if not effective_damage:
            message = f'You YELLOWmissWHITE the {target.name}'

        self.dungeon.add_log(message + '\n')
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

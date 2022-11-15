from core.actions import BaseAction
from core.dungeon import Dungeon


class AttackAction(BaseAction):
    """
    Action of attacking an entity in the room.
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

    def __str__(self) -> str:
        """
        Return the string used to render the action.

        Returns:
        A string
        """
        return 'attack'

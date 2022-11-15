from core.actions.base_action import BaseAction
from core.dungeon import Dungeon


class QuitAction(BaseAction):
    """

    """

    def can_be_performed(self, _: Dungeon) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        context - the current dungeon

        Returns:
        a boolean
        """
        return True

    def __str__(self) -> str:
        """
        Return the string used to render the action.

        Returns:
        A string
        """
        return 'quit'

from abc import ABC
from abc import abstractmethod

from core.dungeon import Dungeon


class BaseAction(ABC):

    def __init__(self, *, pass_turn: bool = True, quiet: bool = False) -> None:
        """
        Constructor creating an abstract action with its actor.

        Argument:
        actor - the character realizing the action
        pass_turn - whether the action consumes a turn or not upon success
        quiet - whether the action should display it messages
        """
        self.pass_turn = pass_turn
        self.quiet = quiet

        self._success = True

    @abstractmethod
    def can_be_performed(self, context: Dungeon) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        context - the currently opened dungeon

        Returns:
        a boolean
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Return the string used to render the action.

        Returns:
        A string
        """
        pass

    def execute(self) -> bool:
        """

        """
        return True

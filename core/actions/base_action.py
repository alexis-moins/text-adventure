from abc import ABC, abstractmethod

from core.entities import Character
from core.actions.exception import ActionException


class BaseAction(ABC):

    def __init__(self, actor: Character, *, takes_a_turn: bool = True, quiet: bool = False) -> None:
        """
        Constructor creating an abstract action with its actor.

        Argument:
        actor - the character realizing the action
        """
        self.actor = actor
        self.takes_a_turn = takes_a_turn
        self.quiet = quiet

        self._success = True

    @abstractmethod
    def validate(self, parameters: list[str]) -> bool:
        """
        Return true if the action is valid and can be executed, otherwise
        return false.

        Returns:
        A boolean
        """
        pass

    @abstractmethod
    def _execute(self, parameters: list[str]) -> None:
        """
        """
        pass

    def execute(self, parameters: list[str]) -> bool:
        """
        Start the life-cycle of the action, by validating then executing
        the action.

        Argument:
        parameters - the list of parameters passed to the action

        Returns:
        A boolean, true if the action consumes a turn.
        """
        try:
            self.validate(parameters)
            self._execute(parameters)

        except ActionException as exception:
            if not self.quiet:
                print(exception)
        else:
            self._success = False
        finally:
            return self.takes_a_turn and self._success

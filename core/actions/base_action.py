from __future__ import annotations
from typing import TYPE_CHECKING

from abc import ABC
from abc import abstractmethod

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.controllers.controller import Controller


class BaseAction(ABC):

    def __init__(self, *, key: str = '', pass_turn: bool = True, quiet: bool = False) -> None:
        """
        Constructor creating an abstract action with its actor.

        Argument:
        key - the key that need to be pressed in order to trigegr the action
        pass_turn - whether the action consumes a turn or not upon success
        quiet - whether the action should display it messages
        """
        self.key = key
        self.pass_turn = pass_turn
        self.quiet = quiet

        self._aborted = False

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
    def execute(self, controller: Controller) -> bool:
        """
        Execute this action. Return true if the action should trigger the next
        round.

        Argument:
        controller - the controller of the current scene

        Returns:
        A boolean
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

from __future__ import annotations
from typing import TYPE_CHECKING

from abc import ABC
from abc import abstractmethod
from core.entities.describable import Describable

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.controllers.controller import Controller


class BaseAction(Describable, ABC):

    def __init__(self, dungeon: Dungeon) -> None:
        """
        Constructor creating a new base action.

        Argument:
        dungeon - the current dungeon
        """
        super().__init__()
        self.dungeon = dungeon

    @abstractmethod
    def can_be_performed(self, controller: Controller) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        controller - the current controller

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
        controller - the current controller

        Returns:
        A boolean
        """
        pass

    def long_description(self) -> str:
        """
        Return the long description of this element.

        Returns:
        A string
        """
        return 'NOT IMPLEMENTED'

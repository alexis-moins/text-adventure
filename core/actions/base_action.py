from __future__ import annotations
from typing import TYPE_CHECKING

from abc import ABC
from abc import abstractmethod
from core.entities.describable import Describable

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.controllers.controller import Controller
    from core.controllers.scene_controller import SceneController


class BaseAction(Describable, ABC):

    @abstractmethod
    def can_be_performed(self, context: Dungeon, controller: SceneController) -> bool:
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

    def long_description(self) -> str:
        """
        Return the long description of this element.

        Returns:
        A string
        """
        return 'NOT IMPLEMENTED'

import os
from abc import ABC
from abc import abstractmethod
from core.actions import ActionList

from core.actions.base_action import BaseAction
from core.dungeon import Dungeon
from core.utils.strings import StringBuilder


class View(ABC):
    """
    Abstract view used to render models and interfaces.
    """

    def __init__(self, dungeon: Dungeon, model) -> None:
        """

        """
        self.model = model
        self.dungeon = dungeon

        self._builder = StringBuilder()

    @abstractmethod
    def show(self, actions: list[BaseAction]) -> None:
        """
        Show the scenery on screen.
        """
        pass

    def clear(self) -> None:
        """
        Clear the screen.
        """
        os.system('clear')

    def show_actions(self, actions: list[BaseAction]) -> None:
        """

        """
        actions = [
            action for action in actions if action.can_be_performed(self.dungeon)]

        if actions:
            self._builder.add('\n')

        for index, action in enumerate(actions):
            self._builder.add(f'[CYAN{index}WHITE] {action}')

        print(self._builder.build())

import os
from abc import ABC
from abc import abstractmethod

from core.actions import BaseAction
from core.dungeon import Dungeon
from core.utils.strings import StringBuilder


class View(ABC):
    """
    Abstract view used to render models and interfaces.
    """

    def __init__(self, dungeon: Dungeon, model) -> None:
        """
        Constructor creating a new abstract view or interface.

        Arguments:
        dungeon - the currently opened dungeon
        model - the model to render
        """
        self.model = model
        self.dungeon = dungeon
        self.builder = StringBuilder()

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
        if actions:
            self.builder.add('\n')

        for index, action in enumerate(actions):
            self.builder.add(f'[CYAN{index}WHITE] {action}')

        print(self.builder.build())

from __future__ import annotations
from enum import Enum
import os

from abc import ABC
from abc import abstractmethod
from typing import TYPE_CHECKING

from core.utils.strings import parse_colors
from core.utils.strings import StringBuilder


if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.actions.base_action import BaseAction


class Render(Enum):
    """

    """
    PINNED_FIRST = 0
    PINNED_LAST = 1


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

    def _get_bar(self, value: int, maximum: int, color: str, character: str, *, length: int = 15, empty_char: str = ' ') -> str:
        """
        Return a status bar with the given values, color and character to fill the bar.

        Arguments:
        value - the current value of the statistics
        maximum - the maximum that the value can take
        color - the color of the bar

        Keyword Arguments:
        length - the length of the bar in characters
        empty_chars - the character to use in place of empty characters

        Returns:
        A string
        """
        percentage = round(value / maximum * length)
        bar = f'[{color}{character * percentage}WHITE{empty_char * (length - percentage)}]'
        return parse_colors(f'{bar} {color}{value}WHITE/{color}{maximum}WHITE')

    def show_status_bar(self) -> None:
        """
        Display the status bar of the player.
        """
        player = self.dungeon.player.fighter
        health = self._get_bar(player.health, player.max_health, 'RED', '=')
        magic = self._get_bar(player.magic, player.max_magic, 'GREEN', '=')

        print(f'health {health}    magic {magic}\n')

    def clear_screen(self) -> None:
        """
        Clear the screen.
        """
        os.system('clear')

    @abstractmethod
    def show(self) -> None:
        """
        Show the scenery on screen.
        """
        pass

    def show_actions(self, actions: list[BaseAction], pinned: dict[str, BaseAction], *, pinned_first: bool = True) -> None:
        """
        Show the available actions on screen.

        Argument:
        actions - the list of (anonymous) actions
        pinned - the dictionary of pinned (named) actions

        Keyword Argument:
        pinned_first - whether the pinned should be rendered first
        """
        self.builder.add('\n')

        if pinned_first:
            for key, action in pinned.items():
                self.builder.add(f'[GREEN{key}WHITE] {action}')
            self.builder.add('\n')

        for index, action in enumerate(actions):
            self.builder.add(f'[CYAN{index}WHITE] {action}')

        if not pinned_first:
            self.builder.add('\n')
            for key, action in pinned.items():
                self.builder.add(f'[GREEN{key}WHITE] {action}')

        print(self.builder.build())

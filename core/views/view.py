from __future__ import annotations
from typing import TYPE_CHECKING

from abc import ABC
from abc import abstractmethod

import os
from core.utils.strings import StringBuilder

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.actions.base_action import BaseAction


class View(ABC):
    """
    Abstract view used to render models and menu.
    """

    def __init__(self, dungeon: Dungeon, *, pinned_first: bool = True) -> None:
        """
        Constructor creating a new abstract view.

        Arguments:
        dungeon - the currently opened dungeon
        """
        self.pinned_first = pinned_first
        self.dungeon = dungeon
        self.b = StringBuilder()

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
        return f'{bar} {color}{value}WHITE/{color}{maximum}WHITE'

    def show_status_bar(self) -> None:
        """
        Display the status bar of the player.
        """
        player = self.dungeon.player
        health = self._get_bar(player.health, player.max_health, 'RED', '=')
        magic = self._get_bar(player.magic, player.max_magic, 'GREEN', '=')

        self.b.add(f'health {health}    magic {magic}', wrap=False)
        self.b.new_line()

    def clear_screen(self) -> None:
        """
        Clear the screen.
        """
        os.system('clear')

    def show_actions(self, actions: list[BaseAction], pinned: dict[str, BaseAction]) -> None:
        """
        Show the available actions on screen.

        Argument:
        actions - the list of (anonymous) actions
        pinned - the dictionary of pinned (named) actions

        Keyword Argument:
        pinned_first - whether the pinned should be rendered first
        """
        self.b.new_line()

        if self.pinned_first:
            for key, action in pinned.items():
                self.b.add(f'[GREEN{key}WHITE] {action}')
            self.b.new_line()

        for index, action in enumerate(actions):
            self.b.add(f'[CYAN{index}WHITE] {action}')

        if not self.pinned_first:
            self.b.new_line()
            for key, action in pinned.items():
                self.b.add(f'[GREEN{key}WHITE] {action}')

    def show(self, actions: list[BaseAction], pinned: dict[str, BaseAction]) -> None:
        """
        Display the view on screen.

        Argument:
        actions - the list of (anonymous) actions
        pinned - the dictionary of pinned (named) actions
        """
        self.clear_screen()

        self.on_show()

        if actions or pinned:
            self.show_actions(actions, pinned)

        self.b.print()
        self.after_show()

    @abstractmethod
    def on_show(self) -> None:
        """
        Method executed after clearing the view and before displaying
        the actions for the view.
        """
        pass

    def after_show(self) -> None:
        """
        Method executed after showing the view.
        """
        pass

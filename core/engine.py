from __future__ import annotations
from typing import TYPE_CHECKING

from core.parser.action import ActionManager
from core.parser.parser import Parser

if TYPE_CHECKING:
    from typing import Callable
    from core.world import World

class Engine:

    def __init__(self, world: World, actions: dict[str, Callable]) -> None:
        """"""
        self.is_running = True
        self.parser = Parser()

        self.world = world

    def get_input(self) -> str:
        """
        Ask the user to write text on the console, then returns the input.

        Returns:
        A string
        """
        return input('\n> ').strip().lower()

    def run(self):
        """"""
        while self.is_running:
            user_input = self.get_input()

            action, args = self.manager.get_action(user_input)

            if not action or not args:
                continue

            action(self.world, args)

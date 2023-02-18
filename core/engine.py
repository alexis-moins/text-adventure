from __future__ import annotations
from typing import TYPE_CHECKING

from core.parser.parser import Parser

if TYPE_CHECKING:
    from core.world import World
    from core.shortcuts import ActionConfig

class Engine:

    def __init__(self, world: World, actions: dict[str, ActionConfig]) -> None:
        """"""
        self.is_running = True
        self.parser = Parser()

        self.actions = self.parser.parse_actions(actions)

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

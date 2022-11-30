from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from core.controllers import ActionDict
    from core.actions.base_action import BaseAction


class Parser:
    """
    Class offering ways to parse the user input.
    """

    def get_action(self, actions: ActionDict) -> BaseAction | None:
        """
        Format and parse the user input and return the corresponding action
        or None if the input was invalid.

        Argument:
        actions - list of actions the user can choose from

        Returns:
        A BaseAction instance or None
        """
        user_input = self.get_input()

        if user_input in actions['key']:
            return actions['key'][user_input]

        if not user_input.isnumeric():
            return None

        user_input = int(user_input)

        if user_input > len(actions['default']) - 1 or user_input < 0:
            return None

        return actions['default'][user_input]

    def get_valid_input(self) -> int | None:
        """
        Return
        """
        user_input = self.get_input()
        return None if not user_input.isnumeric() else int(user_input)

    def format_input(self, user_input: str) -> str:
        """
        Format and return the given input. Currently, the function strips the
        input then turns all letters to lower case.


        Argument:
        user_input - the string that need to be formatted

        Returns:
        A string
        """
        return user_input.strip().lower()

    def get_input(self) -> str:
        """
        Ask the user to write text on the console, then returns the input.

        Returns:
        A string
        """
        user_input = input('\n> ')
        return self.format_input(user_input)

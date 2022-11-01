from typing import Callable

import core.engine.prompt as prompt
from core.actions import BaseAction, get_action


def get_input(*, builder: Callable[[], str] | None = None) -> str:
    """
    Ask the user to write text on the console, then returns the input.

    Argument:
    builder - an optional function that will be executed to build the
    prompt before asking for input. If None, defaults to the return value
    of core.engine.prompt.build_prompt

    Returns:
    A string
    """
    _prompt = prompt.build_prompt() if not builder else builder()
    return input(_prompt)


def format_input(_input: str) -> list[str]:
    """
    Format and return the given input. Currently, the function turns all letters
    to lower case then split the string on spaces.

    Argument:
    _input - the string that need to be formatted

    Returns:
    A list of strings
    """
    return _input.strip().lower().split(' ')


def parse_input(_input: str) -> tuple[BaseAction | None, list[str] | None]:
    """
    Parse the given input into a command function and its arguments.

    Argument:
    _input - the string that need to be parsed into a command

    Returns:
    A tuple of Callable and its arguments (as a list)
    """
    if not _input:
        return None, None

    words = format_input(_input)
    action = get_action(words.pop(0))

    return action, words

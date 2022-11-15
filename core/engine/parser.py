from typing import Callable
import core.engine.prompt as prompt


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
    return format_input(input(_prompt))


def format_input(_input: str) -> str:
    """
    Format and return the given input. Currently, the function strips the
    input then turns all letters to lower case.


    Argument:
    _input - the string that need to be formatted

    Returns:
    A string
    """
    return _input.strip().lower()

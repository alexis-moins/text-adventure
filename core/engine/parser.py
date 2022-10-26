from core.engine.prompt import build_prompt
from core.engine.commands import get_command, Command


def get_input(prompt: str | None = None) -> str:
    """
    Ask the user to write text on the console, then returns the input.

    Argument:
    prompt - the text to display before asking for input. If None, defaults
    to the return value of core.engine.prompt.build_prompt

    Returns:
    A string
    """
    return input(prompt or build_prompt())


def format_input(user_input: str) -> list[str]:
    """
    Format and return the given input. Currently, the function turns all letters
    to lower case then split the string on spaces.

    Argument:
    user_input - the string that need to be formatted

    Returns:
    A list of strings
    """
    return user_input.strip().lower().split(' ')


def parse_input(user_input: str) -> tuple[Command | None, list[str] | None]:
    """
    Parse the given input into a command function and its arguments.

    Argument:
    user_input - the string that need to be parsed into a command

    Returns:
    A tuple of Callable and its arguments (as a list)
    """
    if not user_input:
        return None, None

    words = format_input(user_input)
    command = get_command(words.pop(0))

    return command, words

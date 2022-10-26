from typing import Callable

before_prompt_hooks: list[Callable] = []

def build_prompt() -> str:
    """
    Build a prompt to display before getting the player's input.

    Returns:
    A string
    """
    return '> '

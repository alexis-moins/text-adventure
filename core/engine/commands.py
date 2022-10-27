from typing import Any, Callable

# Type of a Command function
Command = Callable[..., None]

# Dictionary of all the available commands
commands: dict[str, Command] = dict()


def get_command(name: str) -> Command | None:
    """
    Return the command matching the given name or None no command
    is found.

    Argument:
    name - the name of the command

    Returns:
    A function to execute the command or None
    """
    return commands.get(name, None)


def register_command(name: str, function: Command, *, override: bool = False) -> bool:
    """
    Register a new command.

    Arguments:
    name - the name of the command. Corresponds to the text that the user
    will have to type to trigger the command

    function - the function that will be executed

    override - whether or not to override any pre-existing command

    Returns:
    True if the operation succeeds, False otherwise
    """
    if name in commands and not override:
        return False

    commands[name] = function
    return True

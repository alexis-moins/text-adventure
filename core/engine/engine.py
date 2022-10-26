from core.engine import parser
from core.engine import commands

def say_hello(person: str, *args):
    print(person, args)

commands.register_command('echo', say_hello)


def handle_input() -> None:
    """
    """
    user_input = parser.get_input()
    command, arguments = parser.parse_input(user_input)

    if command:
        command(*arguments)


def start_engine() -> None:
    """
    """
    while True:
        handle_input()

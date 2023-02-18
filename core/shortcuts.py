"""
Helper module providing an easy way of kickstarting the creation of
a new world.
"""
from core.parser.action import Action
from core.validation import Validator

from core.world import World
from core.engine import Engine


ActionConfig = Action | tuple[Action, Validator | tuple[Validator]]


def start(scenario: str, actions: dict[str, ActionConfig]) -> None:
    """
    Create a new world using the given scenarios and actions, then
    start the engine.

    Arguments:
    scenario - path to the scenario file (relative to the data directory)
    actions  - pattern to action dectionary
    """
    world = World.create(scenario)
    Engine(world, actions).run()

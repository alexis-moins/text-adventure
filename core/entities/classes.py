from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Callable

import core.engine.parser as parser


@dataclass
class Entity:
    """
    Represents a generic entity, wether it be an item or a character.
    """
    name: str
    description: str = ''

    actions: list[str] = field(default_factory=list)

    @property
    def indefinite_name(self) -> str:
        """
        Return the name of the entity.

        Returns:
        A string
        """
        return indefinite_determiner(self)

    def __str__(self) -> str:
        """
        Return the string representation of the current entity.

        Returns:
        A string
        """
        return self.name


def indefinite_determiner(entity: Entity) -> str:
    """Return the correct indefinite determiner followed by the given entity name"""
    vowels = 'aeiouy'
    determiner = 'an' if entity.name[0] in vowels else 'a'
    return f'{determiner} {entity}'


@dataclass
class Character(ABC, Entity):
    """
    """

    @abstractmethod
    def take_turn(self) -> bool:
        pass


@dataclass(kw_only=True)
class Player(Character):

    def take_turn(self) -> bool:
        """
        Let the player write something and behave based on the input.

        Returns:
        true if the player has executed a command, false otherwise
        """
        user_input = parser.get_input()
        command, arguments = parser.parse_input(user_input)

        if not command:
            print('I don\'t understand that')
            return False

        command(arguments)


@dataclass(kw_only=True)
class NPC(Character):
    # ai_function: Callable[[], bool]  # To be determined, default to idle ?

    def take_turn(self) -> bool:
        """
        Make the NPC take its turn.

        Returns:
        true if the actor has executed an action, false otherwise
        """
        return self.ai_function()

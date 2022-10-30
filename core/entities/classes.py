from abc import ABC, abstractmethod

import core.engine.parser as parser
from core.utils.strings import StringBuilder


def indefinite_determiner(entity_name: str) -> str:
    """
    Return the correct indefinite determiner for the given entity name.

    Arguments:
    entity_name - the name of an entity

    Returns:
    A string corresponding to a determiner
    """
    return 'an' if entity_name[0] in 'aeiouy' else 'a'


class Entity(ABC):
    """
    Represents a generic entity, wether it be an item or a character.
    """

    def __init__(self, name: str, description: str) -> None:
        """
        """
        self.name = name
        self.description = description

        self.indefinite_name = indefinite_determiner(self.name)

        self.builder = StringBuilder()
        # actions: list[str] = field(default_factory=list)

    @abstractmethod
    def __str__(self) -> str:
        """
        Return the string representation of the current entity.

        Returns:
        A string
        """
        pass


class Character(Entity, ABC):

    def __init__(self, name: str, description: str) -> None:
        """
        Constructor creating a new Character, whether it be a NPC or a Player.

        Arguments:
        name - the name of the character
        description - the description of the character
        """
        super().__init__(name, description)

    @abstractmethod
    def take_turn(self) -> bool:
        """
        Make the character take its turn.

        Returns:
        true if the actor has executed an action, false otherwise
        """
        pass


class Player(Character):

    def __init__(self) -> None:
        """
        Constructor creating a new player.

        Arguments:
        name - the name of the player
        description - the description of the player
        """
        super().__init__(name='Hero', description='Whaou! A hero!')

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

    def __str__(self) -> str:
        """
        Return the string representation of the current entity.

        Returns:
        A string
        """
        return self.name


class NPC(Character):

    def __init__(self, name: str, description: str) -> None:
        """
        Constructor creating a new NPC, whether it is hostile or not.

        Arguments:
        name - the name of the NPC
        description - the description of the NPC
        """
        super().__init__(name, description)

    def take_turn(self) -> bool:
        """
        Make the NPC take its turn.

        Returns:
        true if the actor has executed an action, false otherwise
        """
        pass

    def __str__(self) -> None:
        """
        Return the string representation of the current entity.

        Returns:
        A string
        """
        return self.builder.add(self.name + f' RED[!]WHITE').build()

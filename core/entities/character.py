from abc import ABC, abstractmethod

from core.entities.entity import Entity


class Character(Entity, ABC):

    def __init__(self, name: str, description: str) -> None:
        """
        Constructor creating a new abstract character.

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

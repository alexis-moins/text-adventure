from abc import ABC, abstractmethod

from core.entities.entity import Entity
from core.fight.fighter import Fighter


class Character(Entity, ABC):

    def __init__(self, name: str, description: str, fighter: Fighter) -> None:
        """
        Constructor creating a new abstract character.

        Arguments:
        name - the name of the character
        description - the description of the character
        """
        super().__init__(name, description)
        self.fighter = fighter

    @abstractmethod
    def take_turn(self) -> bool:
        """
        Make the character take its turn.

        Returns:
        true if the actor has executed an action, false otherwise
        """
        pass

from abc import ABC, abstractmethod

from core.entities.entity import Entity
from core.fight.fighter import Fighter
from core.fight.statistics import Statistics


class Character(Entity, Fighter, ABC):

    def __init__(self, name: str, description: str, statistics: Statistics) -> None:
        """
        Constructor creating a new abstract character.

        Arguments:
        name - the name of the character
        description - the description of the character
        """
        Entity.__init__(self, name, description)
        Fighter.__init__(self, **statistics)

    @abstractmethod
    def take_turn(self) -> bool:
        """
        Make the character take its turn.

        Returns:
        true if the actor has executed an action, false otherwise
        """
        pass

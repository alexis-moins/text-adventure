from __future__ import annotations
from typing import TYPE_CHECKING

from abc import ABC, abstractmethod
from core.entities.entity import Entity

if TYPE_CHECKING:
    from core.dungeon import Dungeon


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
    def take_turn(self, dungeon: Dungeon) -> bool:
        """
        Make the character take its turn.

        Argument:
        dungeon - the current dungeon

        Returns:
        true if the actor has executed an action, false otherwise
        """
        pass

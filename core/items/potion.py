from __future__ import annotations
from typing import TYPE_CHECKING

from abc import ABC, abstractmethod
from core.items.item import Item

if TYPE_CHECKING:
    from core.fight.fighter import Fighter


class Potion(Item, ABC):

    def __init__(self, name: str, description: str, price: int) -> None:
        """

        """
        super().__init__(name, description, price)
        self.stack_size = 5

    @abstractmethod
    def drink(self, actor: Fighter) -> None:
        """
        Make the given fighter drink the potion. Also
        remove the potion from its inventory.

        Argument:
        fighter - the fighter drinking the potion
        """
        pass

    @abstractmethod
    def drink_sentence(self) -> str:
        """
        Return the sentence to display when a potion is drank.

        Returns:
        A string
        """
        pass

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.b.add(f'{self.name} GREEN(+10 health)WHITE').build()

    def long_description(self) -> str:
        """
        Return the long description of this element.

        Returns:
        A string
        """
        return ''

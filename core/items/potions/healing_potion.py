from __future__ import annotations
from typing import TYPE_CHECKING

from core.items.potion import Potion

if TYPE_CHECKING:
    from core.fight.fighter import Fighter


class HealingPotion(Potion):

    def __init__(self, name: str, description: str, price: int, health: int) -> None:
        """
        """
        super().__init__(name, description, price)
        self.recovery = health

    def drink(self, fighter: Fighter) -> None:
        """
        Make the given fighter drink the potion. Also
        remove the potion from its inventory.

        Argument:
        fighter - the fighter drinking the potion
        """
        fighter.health += self.recovery
        fighter.inventory.remove(self)

    def drink_sentence(self) -> str:
        """
        Return the sentence to display when a potion is drank.

        Returns:
        A string
        """
        word = 'point' if self.recovery == 1 else 'points'
        return f'You regained GREEN{self.recovery} health {word}!WHITE'

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.b.add(f'{self.name_and_id} GREEN(+{self.recovery} health)WHITE').build()

    def long_description(self) -> str:
        """
        Return the long description of this element.

        Returns:
        A string
        """
        return ''

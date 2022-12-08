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

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.b.add(f'{self.name} GREEN(+{self.recovery} health)WHITE').build()

    def long_description(self) -> str:
        """
        Return the long description of this element.

        Returns:
        A string
        """
        return ''

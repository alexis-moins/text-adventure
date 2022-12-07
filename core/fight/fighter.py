from __future__ import annotations

import random
from typing import TYPE_CHECKING

from core.entities.character import Character
from core.fight.statistics import Statistics

if TYPE_CHECKING:
    from core.containers.inventory import Inventory


class Fighter(Character):

    def __init__(self, name: str, description: str, statistics: Statistics, inventory: Inventory) -> None:
        """
        Constructor creating a character with the ability to fight.

        Arguments:
        inventory - all the possessions of the fighter
        """
        super().__init__(name, description)

        self._health = statistics['health']
        self.max_health = statistics['health']

        self._magic = statistics['magic']
        self.max_magic = statistics['magic']

        self.strength = statistics['strength']
        self.defence = statistics['defence']

        self.inventory = inventory

    @property
    def health(self) -> int:
        """
        Return the health of the fighter.

        Returns:
        An integer
        """
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        """
        Set the health of the fighter. The method ensures the
        value of health stays between 0 and max_health.

        Argument:
        value - the new health of the fighter
        """
        self._health = max(0, min(value, self.max_health))

    @property
    def magic(self) -> int:
        """
        Return the magic of the fighter.

        Returns:
        An integer
        """
        return self._magic

    @magic.setter
    def magic(self, value: int) -> None:
        """
        Set the magic of the fighter. The method ensures the
        value of magic stays between 0 and max_magic.

        Argument:
        value - the new magic of the fighter
        """
        self._magic = max(0, min(value, self.max_magic))

    def receive_damage(self, amount: int) -> None:
        """
        Decrease the health of the fighter according to the
        amount of damage received.

        Argument:
        amount - how many damage is received
        """
        self.health -= amount

    def consume_magic(self, amount: int) -> None:
        """
        Decrease the magic of the fighter according to the
        amount of magic consumed.

        Argument:
        amount - how many magic is consumed
        """
        self.magic -= amount

    def is_alive(self) -> bool:
        """
        Return true if this character is alive, return false otherwise.

        Returns:
        A boolean
        """
        return self.health > 0

    def get_damage(self) -> int:
        """
        Return the damage dealt by the fighter this turn.

        Returns:
        An integer
        """
        weapon = self.inventory.equipments.get('weapon')
        weapon_damage = 0 if not weapon else weapon.damage

        return max(self.strength + weapon_damage + random.randint(-2, 2), 0)

from core.items.equipable import Equipable


class Weapon(Equipable):

    def __init__(self, name: str, description: str, price: int, damage: int) -> None:
        """
        Constructor creating a new weapon.

        Arguments:
        name - the name of the weapon
        description - the description of the weapon
        damage - the damage dealt by the weapon
        """
        super().__init__(name, description, price, 'weapon')
        self.damage = damage

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        held = 'RED[!]WHITE' if self.equiped else ''
        return self.b.add(f'{self.name} MAGENTA({self.damage} damage)WHITE {held}').build()

    def long_description(self) -> str:
        """
        Return the long description of this element.

        Returns:
        A string
        """
        return ''

from core.items.equipable import Equipable


class Armor(Equipable):

    def __init__(self, name: str, description: str, price: int, protection: int) -> None:
        """
        Constructor creating a new armor.

        Arguments:
        name - the name of the armor
        description - the description of the armor
        protection - the amount of protection given by the armor
        """
        super().__init__(name, description, price, 'armor')
        self.protection = protection

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        wore = 'RED[wore]WHITE' if self.is_equiped else ''
        return self.b.add(f'{self.name} MAGENTA({self.protection} protection)WHITE {wore}').build()

    def long_description(self) -> str:
        """
        Return the long description of this element.

        Returns:
        A string
        """
        return ''

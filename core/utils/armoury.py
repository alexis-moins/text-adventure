from yaml import safe_load
from core.items.item import Item
from core.items.potions.healing_potion import HealingPotion
from core.items.weapon import Weapon


class Armoury:

    def __init__(self) -> None:
        """

        """
        self._safe: dict[str, dict] = {}
        self.load('data/items.yaml')

    def take(self, item: str) -> Item:
        """
        Take the given item from the armoury's safe

        Argment:
        item - the type of item

        Returns:
        A new Item
        """
        data = self._safe[item].copy()
        item_type = data.pop('type')

        return {
            'weapon': Weapon,
            'healing potion': HealingPotion,
        }[item_type](**data)

    def load(self, path: str) -> None:
        """
        Load the given file into the bestiary.

        Argument:
        path - the path to the armoury
        """
        with open(path, 'r') as file:
            self._safe = safe_load(file)

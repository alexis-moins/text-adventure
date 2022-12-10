from yaml import safe_load
from core.containers.inventory import Inventory

from core.entities.npc import NPC
from core.utils.armory import Armory


class Bestiary:
    """
    Class used as a NPC factory to generate creatures.
    """

    def __init__(self) -> None:
        """
        Constructor creating a new bestiary.
        """
        self.book: dict[str, dict] = {}
        self.armoury = Armory()
        self.load('data/bestiary.yaml')

    def make_inventory(self, items: list[str]) -> Inventory:
        """

        """
        return Inventory([self.armoury.take(item) for item in items])

    def summon(self, creature: str) -> NPC:
        """
        Summon the given creature from the bestiary.

        Argment:
        creature - the type of creature

        Returns:
        A new NPC
        """
        data = self.book[creature].copy()
        inventory = self.make_inventory(data.pop('inventory'))
        return NPC(**data, inventory=inventory)

    def load(self, path: str) -> None:
        """
        Load the given file into the bestiary.

        Argument:
        path - the path to the bestiary
        """
        with open(path, 'r') as file:
            self.book = safe_load(file)

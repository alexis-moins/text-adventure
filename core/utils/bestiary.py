from yaml import safe_load

from core.entities.npc import NPC
from core.entities.trader import Trader
from core.containers.inventory import Inventory


class Bestiary:
    """
    Class used as a NPC factory to generate creatures.
    """

    def __init__(self) -> None:
        """
        Constructor creating a new bestiary.
        """
        self.book: dict[str, dict] = {}

        self.load('data/bestiary.yaml')

    def summon(self, creature: str) -> NPC:
        """
        Summon the given creature from the bestiary.

        Argment:
        creature - the type of creature

        Returns:
        A new NPC
        """
        data = self.book[creature].copy()
        inventory = Inventory.create(data.pop('inventory'))
        creature_type = data.pop('type')

        return {
            'npc': NPC,
            'trader': Trader,
        }[creature_type](**data, inventory=inventory)

    def load(self, path: str) -> None:
        """
        Load the given file into the bestiary.

        Argument:
        path - the path to the bestiary
        """
        with open(path, 'r') as file:
            self.book = safe_load(file)

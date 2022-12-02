from yaml import safe_load

from core.fight.fighter import Fighter
from core.entities.npc import NPC


class Bestiary:
    """
    Class used as a NPC factory to generate creatures.
    """

    def __init__(self) -> None:
        """
        Constructor creating a new bestiary.
        """
        self._book: dict[str, dict] = {}
        self.load('assets/bestiary.yaml')

    def summon(self, creature: str) -> NPC:
        """
        Summon the given creature from the bestiary.

        Argment:
        creature - the type of creature

        Returns:
        A new NPC
        """
        data = self._book[creature].copy()
        return NPC(**data)

    def load(self, path: str) -> None:
        """
        Load the given file into the bestiary.

        Argument:
        path - the path to the bestiary
        """
        with open(path, 'r') as file:
            self._book = safe_load(file)
